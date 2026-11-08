#!/usr/bin/env python3
# Copyright © 2016-2025 The SENTIENT Authors
"""Draw the documentation diagrams as plain SVG in SENTIENT's colours.

Each diagram is written to data/diagrams/<name>.svg and shown on a page with
    {{ diagram(name="<name>") }}
The SVG only carries class names; static/css/site.css colours them from the
site's theme tokens, so every diagram follows the light and dark theme.

Box kinds:  a = part of the SENTIENT server (filled teal)
            s = SENTIENT program around the server (gateway, Edge, converter: teal tint)
            b = anything else (outlined)
            o = optional or outside (dashed outline)
Run: python3 tools/diagrams.py            (writes every diagram)
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parents[1] / "data" / "diagrams"


class D:
    def __init__(self, name, w, h, title):
        self.name, self.w, self.h, self.title = name, w, h, title
        self.el, self.boxes = [], {}

    # ---------- shapes ----------
    def box(self, key, x, y, w, h, title, sub=None, k="b", small=False):
        self.boxes[key] = (x, y, w, h)
        r = 6 if k in ("s", "chip") else 8
        self.el.append(f'<rect class="dg-{k}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>')
        tc = {"a": "dg-ta", "s": "dg-ts", "b": "dg-t", "o": "dg-t", "chip": "dg-ts dg-ct"}[k]
        sc = "dg-ua" if k == "a" else "dg-u"
        if small:
            tc += " dg-sm"
        lines = title.split("\n")
        cx = x + w / 2
        n = len(lines) + (1 if sub else 0)
        lh = 17
        y0 = y + h / 2 - (n - 1) * lh / 2 + 5
        for i, t in enumerate(lines):
            self.el.append(f'<text class="{tc}" x="{cx}" y="{y0 + i * lh}">{escape(t)}</text>')
        if sub:
            self.el.append(f'<text class="{sc}" x="{cx}" y="{y0 + len(lines) * lh - 1}">{escape(sub)}</text>')
        return self

    def stack(self, key, x, y, w, h, title, sub=None, k="b"):
        """A box drawn as a pile of several (many devices, many assets)."""
        for d in (8, 4):
            self.el.append(f'<rect class="dg-{k}" x="{x + d}" y="{y - d}" width="{w}" height="{h}" rx="8"/>')
        return self.box(key, x, y, w, h, title, sub, k)

    def cyl(self, key, x, y, w, h, title, sub=None):
        self.boxes[key] = (x, y, w, h)
        e, r = 8, w / 2
        self.el.append(f'<path class="dg-b" d="M{x} {y + e} A{r} {e} 0 0 1 {x + w} {y + e} V{y + h - e} A{r} {e} 0 0 1 {x} {y + h - e} Z"/>'
                       f'<path class="dg-ln" d="M{x} {y + e} A{r} {e} 0 0 0 {x + w} {y + e}"/>')
        cx = x + w / 2
        if sub:
            self.el.append(f'<text class="dg-t" x="{cx}" y="{y + h / 2 + 2}">{escape(title)}</text><text class="dg-u" x="{cx}" y="{y + h / 2 + 18}">{escape(sub)}</text>')
        else:
            self.el.append(f'<text class="dg-t" x="{cx}" y="{y + h / 2 + 8}">{escape(title)}</text>')
        return self

    def group(self, x, y, w, h, title=None, k="g", right=None):
        self.el.append(f'<rect class="dg-{k}" x="{x}" y="{y}" width="{w}" height="{h}" rx="12"/>')
        if title:
            self.el.append(f'<text class="dg-gh{"" if k == "g" else " dg-gn"}" x="{x + 16}" y="{y + 26}">{escape(title)}</text>')
        if right:
            self.el.append(f'<text class="dg-gs" x="{x + w - 16}" y="{y + 26}">{escape(right)}</text>')
        return self

    def text(self, x, y, s, cls="dg-lbl", anchor="start"):
        self.el.append(f'<text class="{cls}" style="text-anchor:{anchor}" x="{x}" y="{y}">{escape(s)}</text>')
        return self

    def heading(self, x, y, s):
        return self.text(x, y, s, "dg-h")

    # ---------- lines ----------
    def path(self, pts, end=True, start=False, dash=False, label=None, at=None, anchor="middle"):
        d = "M" + " L".join(f"{px} {py}" for px, py in pts)
        cls = "dg-dl" if dash else "dg-ar"
        m = ""
        if end:
            m += f' marker-end="url(#{self.name}-a)"'
        if start:
            m += f' marker-start="url(#{self.name}-a)"'
        self.el.append(f'<path class="{cls}" d="{d}"{m}/>')
        if label:
            lx, ly = at if at else ((pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2 - 7)
            self.text(lx, ly, label, "dg-lbl", anchor)
        return self

    def side(self, key, s, f=0.5):
        x, y, w, h = self.boxes[key]
        return {"l": (x, y + h * f), "r": (x + w, y + h * f), "t": (x + w * f, y), "b": (x + w * f, y + h)}[s]

    def link(self, a, b, label=None, sa="r", sb="l", fa=0.5, fb=0.5, mid=None, **kw):
        """Elbow line from one box to another (right side to left side by default)."""
        p, q = self.side(a, sa, fa), self.side(b, sb, fb)
        gap = 3
        if sb == "l":
            q = (q[0] - gap, q[1])
        elif sb == "r":
            q = (q[0] + gap, q[1])
        elif sb == "t":
            q = (q[0], q[1] - gap)
        else:
            q = (q[0], q[1] + gap)
        if sa in "lr" and sb in "lr":
            mx = mid if mid is not None else (p[0] + q[0]) / 2
            pts = [p, (mx, p[1]), (mx, q[1]), q] if p[1] != q[1] else [p, q]
            if label and "at" not in kw:
                kw["at"] = (q[0] - 8, q[1] - 7)
                kw.setdefault("anchor", "end")
        elif sa in "tb" and sb in "tb":
            my = mid if mid is not None else (p[1] + q[1]) / 2
            pts = [p, (p[0], my), (q[0], my), q] if p[0] != q[0] else [p, q]
            if label and "at" not in kw:
                kw["at"] = (q[0] + 8, (p[1] + q[1]) / 2 + 4)
                kw.setdefault("anchor", "start")
        elif sa in "lr":
            pts = [p, (q[0], p[1]), q]
        else:
            pts = [p, (p[0], q[1]), q]
        return self.path(pts, label=label, **kw)

    def svg(self):
        head = (f'<svg class="st-diagram-svg" viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="{self.name}-t" xmlns="http://www.w3.org/2000/svg">'
                f'<title id="{self.name}-t">{escape(self.title)}</title>'
                f'<defs><marker id="{self.name}-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                f'<path class="dg-ah" d="M0 0 10 5 0 10z"/></marker></defs>')
        return head + "".join(self.el) + "</svg>\n"


ALL = []


def diagram(fn):
    ALL.append(fn)
    return fn


# ====================================================================== platform
@diagram
def architecture():
    d = D("architecture", 1040, 600, "SENTIENT architecture: equipment connects to the SENTIENT server, which keeps its data in PostgreSQL and optionally TimescaleDB or ClickHouse, and serves operators and other systems")
    d.heading(20, 62, "Equipment").heading(800, 62, "Storage").heading(800, 384, "People and systems")
    d.box("dev", 20, 92, 200, 60, "Devices and sensors", "MQTT · HTTP · CoAP · SNMP")
    d.box("plc", 20, 220, 200, 56, "PLCs, meters, drives", "Modbus · OPC UA · S7 · BACnet")
    d.box("gw", 20, 334, 200, 56, "SENTIENT Gateway", "next to the equipment", "s")
    d.box("cloud", 20, 452, 200, 56, "Cloud services", "AWS IoT · Azure · TCP · UDP")
    d.group(290, 40, 470, 442, "SENTIENT server", right="one program, service or container")
    d.el.append('<rect class="dg-b" x="305" y="84" width="440" height="78" rx="8"/>')
    d.text(316, 102, "Device connections", "dg-h2")
    for i, n in enumerate(["MQTT", "HTTP", "CoAP", "SNMP", "Integrations"]):
        d.box(f"t{i}", 316 + i * 85, 114, 78, 36, n, k="chip")
    d.link("plc", "gw", sa="b", sb="t")
    d.path([(220, 118), (303, 118)])
    d.path([(220, 362), (265, 362), (265, 130), (303, 130)], label="MQTT", at=(224, 354), anchor="start")
    d.path([(220, 480), (280, 480), (280, 142), (303, 142)])
    d.box("act", 305, 190, 210, 52, "Device actors", "sessions, activity, commands")
    d.cyl("q", 545, 186, 200, 60, "Queues", "Main · HighPriority")
    d.path([(410, 162), (410, 186)]).path([(515, 216), (541, 216)])
    d.box("re", 305, 268, 440, 56, "Rule engine", "rule chains · alarm rules · calculated fields", "a")
    d.path([(645, 246), (645, 264)])
    for i, (t, s) in enumerate([("Alarms", "live push"), ("Notifications", "email · SMS"), ("Scheduler", "timed jobs"), ("Reports", "PDF · CSV")]):
        d.box(f"r{i}", 305 + i * 113, 348, 101, 52, t, s, small=True)
    d.path([(525, 324), (525, 344)])
    d.box("web", 305, 418, 440, 48, "Web UI · REST API · WebSocket", k="a")
    d.cyl("pg", 800, 72, 220, 64, "PostgreSQL", "configuration, alarms, telemetry")
    d.cyl("ts", 800, 150, 220, 64, "TimescaleDB", "optional: compressed history")
    d.cyl("ch", 800, 228, 220, 64, "ClickHouse", "optional: high-rate history")
    d.path([(745, 296), (784, 296), (784, 104)], end=False)
    for y in (104, 182, 260):
        d.path([(784, y), (797, y)])
    d.box("op", 800, 396, 220, 48, "Operators", "browser · mobile app")
    d.box("ext", 800, 456, 220, 48, "Other systems", "ERP · MES · scripts")
    d.path([(745, 442), (780, 442)], end=False).path([(780, 420), (780, 480)], end=False)
    d.path([(780, 420), (797, 420)]).path([(780, 480), (797, 480)])
    d.heading(20, 550, "Around the server")
    for i, (t, s) in enumerate([("SENTIENT translator", "offline translation"), ("Platform Manager", "install · update"), ("Licence server", "activation")]):
        x = 305 + i * 150
        d.path([(x + 70, 482), (x + 70, 522)], end=False, dash=True)
        d.box(f"o{i}", x, 522, 140, 52, t, s, "o", small=True)
    return d


@diagram
def connectivity():
    d = D("connectivity", 1040, 700, "How to connect a device to SENTIENT: a decision tree from the device's network and protocol to the API, integration or gateway to use")
    d.box("ip", 20, 300, 170, 56, "Is the device on\nan IP network?")
    d.box("fw", 230, 130, 180, 56, "Can you change\nits firmware?")
    d.box("lp", 230, 520, 180, 56, "Does it use LoRaWAN,\nSigfox or NB-IoT?")
    d.box("gwq", 450, 60, 180, 56, "Is it a gateway\nfor other devices?")
    d.box("pr1", 450, 170, 180, 44, "Choose a protocol")
    d.box("cl", 450, 280, 180, 56, "Does it already send data\nto a cloud platform?")
    d.box("wh", 450, 390, 180, 56, "Can it call a\nwebhook (HTTP)?")
    d.box("pr2", 450, 474, 180, 44, "Choose a protocol")
    d.box("ind", 450, 590, 180, 56, "Modbus, OPC UA, S7,\nBACnet, CAN or BLE?")
    O = 820
    d.box("o1", O, 20, 200, 40, "MQTT Gateway API", k="a", small=True)
    d.box("o2", O, 72, 200, 40, "MQTT API", k="a", small=True)
    d.box("o3", O, 124, 200, 40, "HTTP API", k="a", small=True)
    d.box("o4", O, 176, 200, 40, "CoAP API", k="a", small=True)
    d.box("o5", O, 228, 200, 40, "MQTT Sparkplug API", k="a", small=True)
    d.box("o6", O, 282, 200, 52, "Integration", "AWS IoT · Azure · MQTT · OPC UA", "s", small=True)
    d.box("o7", O, 352, 200, 40, "HTTP integration", k="s", small=True)
    d.box("o8", O, 404, 200, 40, "SNMP API", k="a", small=True)
    d.box("o9", O, 456, 200, 40, "CoAP integration", k="s", small=True)
    d.box("o10", O, 508, 200, 40, "Ask us", k="b", small=True)
    d.box("o11", O, 560, 200, 40, "Platform integrations", k="s", small=True)
    d.box("o12", O, 612, 200, 40, "SENTIENT Gateway", k="s", small=True)
    d.box("o13", O, 652 + 4, 200, 36, "Ask us", k="b", small=True)
    d.link("ip", "fw", "Yes", mid=210).link("ip", "lp", "No", mid=210)
    d.link("fw", "gwq", "Yes", mid=430).link("fw", "cl", "No", mid=430)
    d.link("gwq", "o1", "Yes", mid=700)
    d.link("gwq", "pr1", "No", sa="b", sb="t")
    for o, lab in (("o2", "MQTT"), ("o3", "HTTP"), ("o4", "CoAP"), ("o5", "Sparkplug")):
        d.link("pr1", o, lab, mid=720)
    d.link("cl", "o6", "Yes", mid=700)
    d.link("cl", "wh", "No", sa="b", sb="t")
    d.link("wh", "o7", "Yes", mid=700)
    d.link("wh", "pr2", "No", sa="b", sb="t")
    for o, lab in (("o8", "SNMP"), ("o9", "CoAP"), ("o10", "Other")):
        d.link("pr2", o, lab, mid=740)
    d.link("lp", "o11", "Yes", fa=0.3, mid=700)
    d.link("lp", "ind", "No", fa=0.75, mid=430)
    d.link("ind", "o12", "Yes", fa=0.35, mid=760).link("ind", "o13", "No", fa=0.75, mid=740)
    return d


# ====================================================================== attributes and RPC
def three(name, title, left, right, faded_device=False, note=None):
    """Device - SENTIENT server - server-side application, with labelled arrows.
    left/right: list of (label, direction) where direction is '>' or '<'."""
    d = D(name, 900, 230, title)
    d.box("dev", 20, 70, 150, 90, "Device", "firmware", "o" if faded_device else "b")
    d.box("srv", 370, 50, 160, 130, "SENTIENT server", None, "a")
    d.box("app", 730, 70, 150, 90, "Server-side\napplication", "dashboard, script, API")
    for side, items in (("l", left), ("r", right)):
        x0, x1 = (176, 364) if side == "l" else (536, 724)
        n = len(items)
        for i, (lab, dirn) in enumerate(items):
            y = 115 + (i - (n - 1) / 2) * 44
            pts = [(x0, y), (x1, y)] if dirn == ">" else [(x1, y), (x0, y)]
            d.path(pts, start=(dirn == "="), label=lab, at=((x0 + x1) / 2, y - 8))
    if note:
        d.text(95, 196, note, "dg-lbl", "middle")
    return d


@diagram
def client_side_attributes():
    return three("client-side-attributes", "Client-side attributes: the device saves and reads them; applications read them and subscribe to changes",
                 [("Save attributes", ">"), ("Read attributes", "=")], [("Read attributes", "="), ("Updates pushed", ">")])


@diagram
def server_side_attributes():
    return three("server-side-attributes", "Server-side attributes: only applications on the server side save and read them; the device cannot see them",
                 [], [("Save attributes", "<"), ("Read attributes", "=")], faded_device=True, note="does not see them")


@diagram
def shared_attributes():
    return three("shared-attributes", "Shared attributes: applications save them, SENTIENT pushes the values to the device, and the device can read them",
                 [("Updates pushed", "<"), ("Read attributes", "=")], [("Save attributes", "<"), ("Read attributes", "=")])


@diagram
def client_side_rpc():
    return three("client-side-rpc", "Client-side RPC: the device sends a request that the server side answers",
                 [("RPC request", ">"), ("RPC response", "<")], [("RPC request", ">"), ("RPC response", "<")])


@diagram
def one_way_rpc():
    return three("one-way-rpc", "One-way server-side RPC: an application sends a command to the device and expects no reply",
                 [("RPC request", "<")], [("RPC request", "<"), ("Empty response", ">")])


@diagram
def two_way_rpc():
    return three("two-way-rpc", "Two-way server-side RPC: an application sends a command and receives the device's reply",
                 [("RPC request", "<"), ("RPC response", ">")], [("RPC request", "<"), ("RPC response", ">")])


@diagram
def device_provisioning():
    d = D("device-provisioning", 900, 380, "Device provisioning: the device sends a provisioning request, SENTIENT checks it and creates credentials, and the device connects with them")
    d.box("dev", 120, 20, 150, 44, "Device")
    d.box("srv", 520, 20, 180, 44, "SENTIENT server", k="a")
    for x in (195, 610):
        d.path([(x, 64), (x, 360)], end=False, dash=True)
    d.path([(198, 120), (606, 120)], label="Provisioning request", at=(400, 100))
    d.text(400, 136, "provision key and secret, device name, credentials", "dg-u", "middle")
    for i, t in enumerate(["Checks the key and secret against\nthe device profile's provisioning rule", "Checks the device is not\nregistered yet", "Creates the device and\nstores its credentials"]):
        y = 96 + i * 66
        d.box(f"s{i}", 640, y, 240, 54, t, small=True)
        d.path([(612, y + 27), (636, y + 27)], end=False)
    d.path([(606, 270), (198, 270)], label="Provisioning response", at=(400, 250))
    d.text(400, 286, "new credentials", "dg-u", "middle")
    d.box("st", 10, 300, 165, 40, "Saves the credentials", small=True)
    d.path([(178, 320), (193, 320)], end=False)
    d.path([(198, 340), (606, 340)], label="Connects with the new credentials", at=(400, 330))
    return d


@diagram
def entities_and_relations():
    d = D("entities-and-relations", 900, 420, "Entities and relations: a region asset contains field assets, and each field contains its devices")
    d.stack("reg", 360, 30, 180, 60, "Region A", "asset", "s")
    d.stack("fa", 140, 170, 180, 60, "Field A", "asset", "s")
    d.stack("fb", 580, 170, 180, 60, "Field B", "asset", "s")
    d.stack("d1", 20, 320, 190, 60, "Moisture sensors", "devices")
    d.stack("d2", 250, 320, 190, 60, "Irrigation valves", "devices")
    d.stack("d3", 480, 320, 190, 60, "Moisture sensors", "devices")
    d.stack("d4", 700, 320, 190, 60, "Irrigation valves", "devices")
    d.link("reg", "fa", sa="b", sb="t").link("reg", "fb", sa="b", sb="t")
    for p, c in (("fa", "d1"), ("fa", "d2"), ("fb", "d3"), ("fb", "d4")):
        d.link(p, c, sa="b", sb="t")
    d.text(250, 122, "Contains", "dg-lbl").text(560, 122, "Contains", "dg-lbl")
    d.text(244, 267, "Contains", "dg-lbl").text(684, 267, "Contains", "dg-lbl")
    return d


# ====================================================================== gateway
@diagram
def gateway_overview():
    d = D("gateway-overview", 1040, 556, "SENTIENT Gateway: connectors read equipment over industrial protocols, converters turn the data into telemetry and attributes, and the gateway sends it to the SENTIENT server over MQTT")
    d.box("srv", 400, 16, 240, 52, "SENTIENT server", k="a")
    d.group(20, 104, 1000, 290, "SENTIENT Gateway", right="Windows, Linux or Docker, next to the equipment")
    d.box("core", 300, 142, 200, 48, "Gateway service", "keeps sending, reconnects", "s", small=True)
    d.cyl("buf", 540, 140, 180, 52, "Local storage", "holds data while offline")
    d.box("web", 760, 142, 200, 48, "Local web page", "setup and status", small=True)
    d.path([(520, 68), (520, 138)], start=True, label="MQTT over TLS", at=(530, 90), anchor="start")
    d.path([(500, 166), (536, 166)], start=True)
    names = ["Modbus", "OPC UA", "Siemens S7", "BACnet", "EtherNet/IP", "Beckhoff ADS", "Mitsubishi MC", "Omron FINS",
             "DNP3", "IEC 61850", "KNX", "PROFINET", "MQTT", "REST", "Request", "Socket",
             "Serial", "BLE", "CAN", "SNMP", "ODBC", "FTP", "OCPP", "XMPP"]
    d.text(40, 232, "Connectors, each with a converter", "dg-h2")
    for i, n in enumerate(names):
        r, c = divmod(i, 8)
        d.box(f"c{i}", 40 + c * 121, 244 + r * 46, 112, 36, n, k="chip")
    d.path([(400, 190), (400, 240)], start=True)
    eq = [("PLCs and drives", "Modbus · S7 · EtherNet/IP"), ("OPC UA servers", "SCADA, historians"), ("Meters and sensors", "serial, BLE, CAN"),
          ("Brokers and APIs", "MQTT · HTTP"), ("Databases and files", "ODBC · FTP")]
    for i, (t, s) in enumerate(eq):
        x = 20 + i * 204
        d.box(f"e{i}", x, 450, 188, 56, t, s, small=True)
        d.path([(x + 94, 446), (x + 94, 398)], start=True)
    d.heading(20, 540, "Equipment on the local network")
    return d


# ====================================================================== integrations
def integration(name, source, proto, label, payload="JSON · binary · text", source_sub=None):
    d = D(name, 1000, 250, f"{label}: {source} sends data over {proto}; the integration hands it to the uplink converter, which turns it into telemetry and attributes for the rule engine. Attribute updates and RPC go back through the downlink converter")
    d.box("src", 20, 95, 170, 60, source, source_sub)
    d.box("int", 250, 95, 170, 60, label, "integration", "s", small=True)
    d.box("up", 490, 40, 170, 52, "Uplink converter", "decodes the payload", "s", small=True)
    d.box("down", 490, 158, 170, 52, "Downlink converter", "encodes commands", "s", small=True)
    d.group(740, 20, 240, 210, "SENTIENT server")
    d.box("re", 758, 60, 204, 56, "Rule engine", "rule chains, alarms", "a", small=True)
    d.box("db", 758, 140, 204, 56, "Dashboards", "live values", "a", small=True)
    d.path([(190, 125), (246, 125)], start=True, label=proto, at=(218, 117))
    d.path([(420, 112), (455, 112), (455, 66), (486, 66)], label=payload, at=(455, 125 - 100))
    d.path([(486, 184), (455, 184), (455, 138), (424, 138)])
    d.path([(660, 66), (700, 66), (700, 88), (754, 88)])
    d.text(700, 28, "telemetry,", "dg-lbl", "middle").text(700, 42, "attributes", "dg-lbl", "middle")
    d.path([(758, 160), (700, 160), (700, 184), (664, 184)])
    d.text(700, 224, "attribute", "dg-lbl", "middle").text(700, 238, "updates, RPC", "dg-lbl", "middle")
    return d


INTEGRATIONS = [
    ("aws-iot-integration", "AWS IoT", "MQTT", "AWS IoT"),
    ("azure-event-hub-integration", "Azure Event Hub", "AMQP", "Azure Event Hub"),
    ("azure-iot-hub-integration", "Azure IoT Hub", "MQTT", "Azure IoT Hub"),
    ("coap-integration", "Devices", "CoAP", "CoAP"),
    ("http-integration", "Devices or a\nplatform", "HTTP", "HTTP"),
    ("mqtt-integration", "MQTT broker", "MQTT", "MQTT"),
    ("ocean-connect-integration", "OceanConnect", "HTTP", "OceanConnect"),
    ("opc-ua-integration", "OPC UA server", "OPC UA", "OPC UA"),
    ("sigfox-integration", "Sigfox backend", "HTTP", "Sigfox"),
    ("tcp-integration", "Devices", "TCP", "TCP"),
    ("thingpark-integration", "ThingPark", "HTTP", "ThingPark"),
    ("udp-integration", "Devices", "UDP", "UDP"),
]
for _n, _s, _p, _l in INTEGRATIONS:
    ALL.append(lambda n=_n, s=_s, p=_p, l=_l: integration(n, s, p, l))


@diagram
def integrations_overview():
    d = D("integrations-overview", 1000, 500, "Integrations: devices that already talk to IoT platforms, LoRaWAN and NB-IoT networks or OPC UA servers reach SENTIENT through integrations and converters")
    groups = [("IoT platforms", ["AWS IoT", "IBM Watson", "Microsoft Azure"], "MQTT"),
              ("LoRaWAN networks", ["ThingPark", "The Things Network", "TEKTELIC"], "LoRaWAN"),
              ("NB-IoT", ["TCP / UDP"], "TCP / UDP")]
    y = 20
    ys = []
    for gi, (g, items, proto) in enumerate(groups):
        h = 44 + len(items) * 42
        d.group(190, y, 220, h, g, k="gd")
        for i, it in enumerate(items):
            d.box(f"g{gi}{i}", 206, y + 38 + i * 42, 188, 34, it, small=True)
        d.stack(f"dv{gi}", 20, y + h / 2 - 22, 120, 44, "Devices")
        d.path([(144, y + h / 2), (186, y + h / 2)], start=True, label=proto, at=(165, y + h / 2 - 8))
        ys.append(y + h / 2)
        y += h + 16
    d.group(520, 150, 460, 190, "SENTIENT server")
    d.box("int", 540, 190, 180, 52, "Integrations", None, "s")
    d.box("conv", 540, 270, 180, 52, "Converters", "uplink and downlink", "s", small=True)
    d.box("re", 760, 190, 200, 52, "Rule engine", k="a")
    d.box("db", 760, 270, 200, 52, "Dashboards", k="a")
    d.path([(630, 242), (630, 266)], start=True)
    d.path([(720, 216), (756, 216)], start=True)
    d.path([(860, 242), (860, 266)], start=True)
    for i, yy in enumerate(ys):
        d.path([(410, yy), (470, yy), (470, 216), (536, 216)], start=True)
    d.stack("sig", 620, 30, 140, 44, "Devices")
    d.path([(690, 74), (690, 186)], start=True, label="Sigfox", at=(700, 120), anchor="start")
    d.stack("opc", 560, 400, 140, 44, "Devices")
    d.path([(630, 396), (630, 326)], start=True, label="OPC UA", at=(640, 370), anchor="start")
    return d


@diagram
def embedded_integrations():
    d = D("embedded-integrations-overview", 1000, 320, "Integrations that run inside the SENTIENT server connect to cloud platforms and networks directly")
    d.group(470, 40, 510, 240, "SENTIENT server")
    for i, (t, s) in enumerate([("IoT platforms", "AWS IoT · Azure · IBM Watson"), ("LoRaWAN networks", "ThingPark · TTN · TEKTELIC"), ("Brokers and servers", "MQTT · OPC UA · HTTP")]):
        d.box(f"p{i}", 20, 30 + i * 96, 230, 64, t, s)
        y = 62 + i * 96
        d.path([(254, y), (486, y)] if i == 1 else [(254, y), (420, y), (420, 158), (486, 158)], start=True)
    d.box("int", 490, 128, 200, 60, "Integrations", "run inside the server", "s")
    d.box("conv", 490, 210, 200, 52, "Converters", None, "s")
    d.box("re", 750, 128, 210, 60, "Rule engine", k="a")
    d.box("db", 750, 210, 210, 52, "Dashboards", k="a")
    d.path([(690, 158), (746, 158)], start=True).path([(590, 188), (590, 206)], start=True).path([(855, 188), (855, 206)], start=True)
    return d


@diagram
def remote_integrations():
    d = D("remote-integrations-overview", 1000, 400, "Remote integrations run on the local network next to the devices and forward the data to the SENTIENT server")
    for i, src in enumerate(["OPC UA server", "MQTT broker", "Custom source"]):
        y = 20 + i * 126
        d.group(20, y, 640, 110, "Local network", k="gd")
        d.stack(f"dv{i}", 40, y + 40, 120, 44, "Devices")
        d.box(f"s{i}", 200, y + 40, 160, 44, src, small=True)
        d.box(f"r{i}", 400, y + 34, 230, 44, "Remote integration", None, "s", small=True)
        d.box(f"f{i}", 430, y + 82, 200, 22, "", None, "o")
        d.text(530, y + 98, "local file storage", "dg-u", "middle")
        d.path([(164, y + 62), (196, y + 62)], start=True).path([(364, y + 58), (396, y + 58)], start=True)
        d.path([(634, y + 56), (700, y + 56), (700, 196), (736, 196)], start=True)
    d.box("srv", 740, 160, 240, 72, "SENTIENT server", "rule engine, dashboards", "a")
    d.text(706, 186, "HTTPS", "dg-lbl")
    return d


# ====================================================================== Edge
@diagram
def edge_overview():
    d = D("edge-overview", 960, 430, "SENTIENT Edge runs on site: devices and gateways connect to it, it stores data, runs rules, dashboards and alarms locally and syncs with the SENTIENT server")
    d.box("srv", 360, 16, 240, 52, "SENTIENT server", "cloud or head office", "a")
    d.group(20, 100, 920, 310, "SENTIENT Edge", right="on site")
    d.box("gw", 40, 150, 170, 48, "SENTIENT Gateway", None, "s", small=True)
    d.stack("dev", 40, 300, 170, 48, "Devices")
    d.box("core", 290, 220, 180, 52, "Edge core", None, "a")
    d.cyl("db", 290, 130, 180, 56, "Database")
    d.box("re", 540, 220, 180, 52, "Rule engine", None, "a")
    d.box("dash", 540, 130, 180, 52, "Dashboards", "real time", "a", small=True)
    d.box("al", 540, 310, 180, 52, "Alarms", "email and push", "a", small=True)
    d.box("an", 290, 330, 180, 48, "Analytics", None, "b", small=True)
    d.box("op", 780, 220, 140, 52, "Operators", "on site")
    d.path([(480, 68), (480, 96)], start=True, label="sync when online", at=(490, 88), anchor="start")
    d.link("gw", "core", "MQTT", fb=0.3)
    d.link("dev", "core", "MQTT · HTTP · CoAP", fb=0.7)
    d.path([(380, 216), (380, 190)], start=True)
    d.path([(474, 246), (536, 246)], start=True)
    d.path([(630, 216), (630, 186)]).path([(630, 276), (630, 306)])
    d.path([(380, 276), (380, 326)], start=True)
    d.link("dash", "op", fb=0.3).link("al", "op", fb=0.7)
    return d


@diagram
def edge_architecture():
    d = D("edge-architecture", 960, 260, "SENTIENT Edge components: device transports, the Edge core with its rule engine, and the cloud connection to the SENTIENT server")
    d.group(190, 20, 560, 220, "SENTIENT Edge")
    d.stack("dev", 20, 100, 130, 48, "Devices")
    for i, t in enumerate(["HTTP", "MQTT", "CoAP"]):
        d.box(f"t{i}", 210, 50 + i * 56, 100, 40, t, k="chip")
        d.path([(154, 124), (180, 124), (180, 70 + i * 56), (206, 70 + i * 56)], start=True)
    d.box("core", 360, 98, 160, 52, "Edge core", None, "a")
    d.box("re", 560, 98, 170, 52, "Rule engine", "push to cloud", "a", small=True)
    for i in range(3):
        d.path([(310, 70 + i * 56), (335, 70 + i * 56), (335, 124), (356, 124)], end=(i == 1))
    d.path([(520, 124), (556, 124)], start=True)
    d.box("srv", 800, 40, 150, 52, "SENTIENT server", None, "a", small=True)
    d.box("user", 800, 120, 150, 44, "Operators", small=True)
    d.box("app", 800, 180, 150, 44, "Other systems", "REST API", small=True)
    d.path([(730, 110), (770, 110), (770, 66), (796, 66)], start=True, label="gRPC", at=(753, 56), anchor="start")
    d.path([(730, 138), (770, 138), (770, 202), (796, 202)], start=True)
    d.path([(770, 142), (796, 142)])
    return d


def edge_site(d, x, y, label, faded=False, sensors=True):
    d.group(x, y, 150, 120, label, k="gd")
    d.box(f"{label}f", x + 14, y + 38, 122, 32, "Fan", small=True)
    d.box(f"{label}t", x + 14, y + 78, 122, 32, "Temperature", small=True)


@diagram
def edge_offline():
    d = D("edge-offline", 900, 470, "Local deployment: SENTIENT Edge keeps processing and storing data from on-site equipment while the cloud connection is down, and syncs when it returns")
    d.box("srv", 330, 16, 240, 48, "SENTIENT server", None, "a")
    d.path([(450, 64), (450, 100)], start=True, dash=True, label="syncs when the connection returns", at=(462, 88), anchor="start")
    d.group(20, 104, 860, 350, "On site", k="gd")
    d.box("edge", 350, 140, 200, 52, "SENTIENT Edge", None, "a")
    d.box("re", 120, 140, 170, 44, "Rule engine", small=True)
    d.box("dash", 120, 196, 170, 40, "Dashboards", small=True)
    d.cyl("st", 610, 136, 190, 56, "Local storage")
    d.box("gw", 350, 236, 200, 44, "SENTIENT Gateway", None, "s", small=True)
    d.path([(294, 162), (346, 162)], start=True).path([(294, 216), (320, 216), (320, 180), (346, 180)], start=True)
    d.path([(550, 166), (606, 166)], start=True).path([(450, 196), (450, 232)], start=True)
    for i, nm in enumerate(["Line 1", "Line 2", "Line 3"]):
        x = 150 + i * 220
        edge_site(d, x, 310, nm)
        d.path([(x + 75, 306), (x + 75, 294), (450, 294), (450, 280)], end=False)
    return d


@diagram
def edge_filtering():
    d = D("edge-filtering", 900, 200, "Traffic filtering: SENTIENT Edge receives all readings on site and sends only the ones you choose to the SENTIENT server")
    d.group(20, 30, 200, 140, "Line 1", k="gd")
    d.box("f", 40, 70, 160, 36, "Fan", small=True)
    d.box("t", 40, 116, 160, 36, "Temperature sensor", small=True)
    d.box("edge", 320, 60, 220, 84, "SENTIENT Edge", "filter rule chain", "a")
    d.box("srv", 660, 72, 220, 60, "SENTIENT server", None, "a")
    d.path([(224, 100), (316, 100)], label="every reading", at=(270, 90))
    d.path([(544, 102), (656, 102)], label="selected values", at=(600, 92))
    return d


@diagram
def edge_alarm():
    d = D("edge-alarm", 900, 390, "Local alarms: SENTIENT Edge raises alarms and shows them on site even when the connection to the server is down")
    d.box("srv", 330, 16, 240, 48, "SENTIENT server", "not reachable", "o")
    d.path([(450, 64), (450, 98)], dash=True, end=False)
    d.text(462, 86, "network down", "dg-lbl")
    d.box("edge", 350, 102, 200, 52, "SENTIENT Edge", None, "a")
    d.box("re", 110, 106, 180, 44, "Rule engine", "raises the alarm", "b", small=True)
    d.box("dash", 610, 106, 180, 44, "Dashboard and alarms", "on site", "b", small=True)
    d.box("gw", 350, 184, 200, 40, "SENTIENT Gateway", None, "s", small=True)
    d.path([(294, 128), (346, 128)], start=True).path([(550, 128), (606, 128)])
    d.path([(450, 158), (450, 180)], start=True)
    for i, nm in enumerate(["Line 1", "Line 2", "Line 3"]):
        x = 150 + i * 220
        edge_site(d, x, 250, nm)
        d.path([(x + 75, 246), (x + 75, 236)], end=False)
    d.path([(225, 236), (675, 236)], end=False).path([(450, 224), (450, 236)], end=False)
    return d


@diagram
def edge_dashboards():
    d = D("edge-dashboards", 900, 260, "Batch update: change a dashboard once on the SENTIENT server and it is sent to every Edge")
    d.box("srv", 330, 16, 240, 60, "SENTIENT server", "dashboard changed once", "a")
    for i in range(3):
        x = 40 + i * 290
        d.box(f"e{i}", x, 160, 240, 60, f"SENTIENT Edge {i + 1}", "gets the new dashboard", "s")
        d.path([(450, 80), (450, 120), (x + 120, 120), (x + 120, 156)])
    return d


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    names = []
    for fn in ALL:
        d = fn()
        (OUT / f"{d.name}.svg").write_text(d.svg(), encoding="utf-8")
        names.append(d.name)
    print(f"wrote {len(names)} diagrams to {OUT}")


if __name__ == "__main__":
    main()
