#!/usr/bin/env python3
# Copyright © 2016-2025 The SENTIENT Authors
"""Create the "Demo Plant" tenant that every documentation screenshot shows.

  python3 tools/screenshots/seed.py --url http://localhost:8080 \
      [--sysadmin admin@sentient.local:PASSWORD] [--hours 24]

Idempotent: existing tenant, user, devices and assets are reused; telemetry
history is written again for the last --hours (default 24) so charts are
never empty. Credentials come from --sysadmin or ST_DOCS_SYSADMIN
("email:password"). The docs user is docs@demo.plant / ST_DOCS_PASSWORD
(default "DocsDemo#2025"); keep this tenant for screenshots only.
"""
import argparse, json, math, os, random, sys, time, urllib.error, urllib.request

TENANT = "Demo Plant"
DOCS_USER = "docs@demo.plant"

# name, type, label, telemetry generators {key: (base, amplitude, noise)}
DEVICES = [
    ("Feed pump P-101", "Pump", "Boiler house", {"flow": (42, 6, 0.8), "pressure": (6.2, 0.4, 0.05), "motorCurrent": (18, 2, 0.3), "vibration": (2.1, 0.6, 0.15)}),
    ("Feed pump P-102", "Pump", "Boiler house", {"flow": (40, 5, 0.8), "pressure": (6.0, 0.3, 0.05), "motorCurrent": (17, 2, 0.3), "vibration": (3.4, 0.9, 0.2)}),
    ("Belt conveyor BC-1", "Conveyor", "Packing line", {"speed": (1.6, 0.2, 0.02), "load": (62, 18, 2), "motorCurrent": (24, 4, 0.5)}),
    ("Air compressor C-201", "Compressor", "Utilities", {"pressure": (7.4, 0.3, 0.04), "temperature": (71, 5, 0.6), "power": (55, 9, 1.2)}),
    ("Cooling tower CT-1", "Cooling tower", "Utilities", {"waterTemperature": (29, 3, 0.3), "fanSpeed": (1180, 120, 10)}),
    ("Energy meter EM-1", "Energy meter", "Main incomer", {"activePower": (410, 70, 6), "voltage": (415, 4, 0.8), "powerFactor": (0.93, 0.02, 0.003)}),
    ("Tank level LT-301", "Level sensor", "Tank farm", {"level": (68, 15, 0.4), "temperature": (34, 2, 0.2)}),
]
ASSETS = [("Plant", "Site"), ("Boiler house", "Area"), ("Packing line", "Area"), ("Utilities", "Area"), ("Tank farm", "Area"), ("Main incomer", "Area")]
ATTRIBUTES = {"Pump": {"ratedFlow": 50, "maker": "KSB", "commissioned": "2021-03-14"},
              "Compressor": {"ratedPressure": 8, "maker": "Atlas Copco"}}
GATEWAY = "Plant gateway GW-1"
DASHBOARDS = ["Boiler house overview", "Utilities energy", "Packing line OEE"]
ALARMS = [("Feed pump P-102", "High vibration", "MAJOR"), ("Air compressor C-201", "High temperature", "WARNING"),
          ("Tank level LT-301", "Level low", "MINOR")]


class Api:
    def __init__(self, url):
        self.url, self.token = url.rstrip("/"), None

    def call(self, method, path, body=None, ok404=False):
        data = None if body is None else json.dumps(body).encode()
        req = urllib.request.Request(self.url + path, data=data, method=method)
        req.add_header("Content-Type", "application/json")
        if self.token:
            req.add_header("X-Authorization", "Bearer " + self.token)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                return json.loads(raw) if raw.strip() else None
        except urllib.error.HTTPError as e:
            if ok404 and e.code == 404:
                return None
            sys.exit(f"{method} {path} -> {e.code} {e.read()[:300].decode(errors='replace')}")

    def login(self, user, pw):
        self.token = self.call("POST", "/api/auth/login", {"username": user, "password": pw})["token"]

    def can_login(self, user, pw):
        req = urllib.request.Request(self.url + "/api/auth/login", data=json.dumps({"username": user, "password": pw}).encode(),
                                     method="POST", headers={"Content-Type": "application/json"})
        try:
            urllib.request.urlopen(req, timeout=30).read()
            return True
        except urllib.error.HTTPError:
            return False


def find(items, name):
    return next((x for x in items if x.get("name") == name or x.get("title") == name or x.get("email") == name), None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=os.environ.get("ST_DOCS_URL", "http://localhost:8080"))
    ap.add_argument("--sysadmin", default=os.environ.get("ST_DOCS_SYSADMIN", ""))
    ap.add_argument("--hours", type=int, default=24)
    a = ap.parse_args()
    if ":" not in a.sysadmin:
        sys.exit("give the system administrator as --sysadmin email:password or ST_DOCS_SYSADMIN")
    pw = os.environ.get("ST_DOCS_PASSWORD", "DocsDemo#2025")
    api = Api(a.url)
    api.login(*a.sysadmin.split(":", 1))

    tenants = api.call("GET", "/api/tenants?pageSize=100&page=0&textSearch=" + urllib.request.quote(TENANT))["data"]
    tenant = find(tenants, TENANT) or api.call("POST", "/api/tenant", {"title": TENANT, "country": "India", "city": "Pune"})
    tid = tenant["id"]["id"]
    users = api.call("GET", f"/api/tenant/{tid}/users?pageSize=100&page=0")["data"]
    u = find(users, DOCS_USER) or api.call("POST", "/api/user?sendActivationMail=false", {
        "email": DOCS_USER, "firstName": "Docs", "lastName": "Demo", "authority": "TENANT_ADMIN",
        "tenantId": {"id": tid, "entityType": "TENANT"}})
    if not api.can_login(DOCS_USER, pw):  # new, or left unactivated by an interrupted run
        link = api.call("GET", f"/api/user/{u['id']['id']}/activationLinkInfo")["value"]
        token = link.split("activateToken=")[-1]
        api.token = None
        api.call("POST", "/api/noauth/activate?sendActivationMail=false", {"activateToken": token, "password": pw})
    api.login(DOCS_USER, pw)

    assets = {}
    for name, typ in ASSETS:
        got = api.call("GET", "/api/tenant/assets?assetName=" + urllib.request.quote(name), ok404=True)
        assets[name] = got or api.call("POST", "/api/asset", {"name": name, "type": typ})
    for name, _ in ASSETS[1:]:
        api.call("POST", "/api/relation", {"from": assets["Plant"]["id"], "to": assets[name]["id"], "type": "Contains", "typeGroup": "COMMON"})

    now = int(time.time() * 1000)
    rnd = random.Random(7)
    for name, typ, area, gens in DEVICES:
        dev = api.call("GET", "/api/tenant/devices?deviceName=" + urllib.request.quote(name), ok404=True) \
            or api.call("POST", "/api/device", {"name": name, "type": typ, "label": area})
        api.call("POST", "/api/relation", {"from": assets[area]["id"], "to": dev["id"], "type": "Contains", "typeGroup": "COMMON"})
        if typ in ATTRIBUTES:
            api.call("POST", f"/api/plugins/telemetry/DEVICE/{dev['id']['id']}/attributes/SERVER_SCOPE", ATTRIBUTES[typ])
        token = api.call("GET", f"/api/device/{dev['id']['id']}/credentials")["credentialsId"]
        points = []
        step = 5 * 60 * 1000
        for i in range(a.hours * 12, -1, -1):
            ts = now - i * step
            phase = 2 * math.pi * (ts % 86_400_000) / 86_400_000
            vals = {k: round(b + amp * math.sin(phase - 1.2) + rnd.gauss(0, n), 3) for k, (b, amp, n) in gens.items()}
            points.append({"ts": ts, "values": vals})
        for j in range(0, len(points), 100):
            req = urllib.request.Request(f"{api.url}/api/v1/{token}/telemetry", data=json.dumps(points[j:j + 100]).encode(),
                                         method="POST", headers={"Content-Type": "application/json"})
            urllib.request.urlopen(req, timeout=30).read()
        print(f"  {name}: {len(points)} points")

    # A gateway, so the Gateways page is not empty.
    if not api.call("GET", "/api/tenant/devices?deviceName=" + urllib.request.quote(GATEWAY), ok404=True):
        api.call("POST", "/api/device", {"name": GATEWAY, "type": "Gateway", "label": "Control room",
                                         "additionalInfo": {"gateway": True, "description": "Modbus and OPC UA"}})

    # Dashboards (empty layouts; their names fill the list).
    have = {d["title"] for d in api.call("GET", "/api/tenant/dashboards?pageSize=100&page=0")["data"]}
    for title in DASHBOARDS:
        if title not in have:
            api.call("POST", "/api/dashboard", {"title": title, "configuration": {}})

    # A calculated field on each pump: flow per amp of motor current.
    for name, typ, _, _ in DEVICES:
        if typ != "Pump":
            continue
        dev = api.call("GET", "/api/tenant/devices?deviceName=" + urllib.request.quote(name))
        listed = api.call("GET", f"/api/DEVICE/{dev['id']['id']}/calculatedFields?pageSize=50&page=0", ok404=True) or {}
        if any(f.get("name") == "Flow per amp" for f in listed.get("data", [])):
            continue
        api.call("POST", "/api/calculatedField", {
            "entityId": dev["id"], "type": "SIMPLE", "name": "Flow per amp", "configurationVersion": 1,
            "configuration": {"type": "SIMPLE",
                              "arguments": {"flow": {"refEntityKey": {"key": "flow", "type": "TS_LATEST"}},
                                            "current": {"refEntityKey": {"key": "motorCurrent", "type": "TS_LATEST"}}},
                              "expression": "flow / current",
                              "output": {"type": "TIME_SERIES", "name": "flowPerAmp", "decimalsByDefault": 2}}})

    for dname, atype, sev in ALARMS:
        dev = api.call("GET", "/api/tenant/devices?deviceName=" + urllib.request.quote(dname))
        api.call("POST", "/api/alarm", {"originator": dev["id"], "type": atype, "severity": sev,
                                         "details": {"source": "docs demo"}})
    print(f"Demo Plant ready: sign in as {DOCS_USER}")


if __name__ == "__main__":
    main()
