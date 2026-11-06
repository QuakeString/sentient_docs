#!/usr/bin/env python3
# Copyright © 2016-2025 The SENTIENT Authors
"""Content audit: one row per page with a verdict, the wave that handles it,
and the SENTIENT UI help links that point at it.

  python3 tools/audit.py [--helplinks audit/ui-help-links.txt]  -> audit/pages.csv, audit/SUMMARY.md

Verdicts
  delete   does not apply to SENTIENT (ThingsBoard-only product, Java install,
           ThingsBoard hardware library, release history of another product)
  rewrite  the feature exists in SENTIENT but screens or behaviour differ
  check    concept or API page that is probably still right; verify and refresh
  planned  new SENTIENT page that does not exist yet (stub with an outline)
The rules below are ordered; the first match wins.
"""
import csv, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

# Rule nodes documented by ThingsBoard that SENTIENT's rule engine does not ship.
MISSING_NODES = {
    "add-to-group", "remove-from-group", "change-owner", "generate-report", "generate-dashboard-report",
    "save-to-custom-table", "gcp-pubsub", "twilio-sms", "twilio-voice", "aggregate-latest",
    "aggregate-stream", "alarms-count-deprecated", "alarms-count", "duplicate-to-group",
    "duplicate-to-group-by-name", "duplicate-to-related", "change-originator-pe", "integration-downlink-pe",
}

RULES = [
    # (regex on path relative to content/, verdict, wave, reason)
    (r"^docs/user-guide/install/(?!_index)", "delete", "-", "ThingsBoard Java install; replaced by SENTIENT install guides"),
    (r"^docs/(edge/)?releases/", "delete", "-", "ThingsBoard release history; SENTIENT release notes come from CHANGELOG.md"),
    (r"^docs/devices-library/", "delete", "-", "ThingsBoard hardware library built on ThingsBoard device profiles"),
    (r"^docs/samples/(?!_index)", "delete", "-", "Vendor tutorials built on ThingsBoard demo assets"),
    (r"^docs/reference/(performance|msa|monolithic|iot-platform-deployment-scenarios|mcp-server)", "delete", "-", "ThingsBoard architecture/performance material"),
    (r"^docs/user-guide/contribution/(how-to-contribute|rule-node-development)", "delete", "-", "Contributing to ThingsBoard on GitHub / Java rule nodes"),
    (r"^docs/mobile/(.*before-v1\.7|release|customization|customize-|app-icon|localization)", "delete", "-", "Building your own ThingsBoard mobile app; SENTIENT ships a ready APK"),
    (r"^docs/edge/(.*install|getting-started-guides/.*pe)", "delete", "-", "ThingsBoard Edge installation"),
    (r"^docs/(live-demo|domains)\.md|^docs/user-guide/live-demo", "delete", "-", "ThingsBoard cloud / live demo"),
    (r"^docs/user-guide/rule-engine-2-5/(?!queues)", "delete", "-", "ThingsBoard Kafka queue internals"),
    (r"^docs/iot-gateway/(install/|custom/|roadmap|guides/how-to-use-remote-converter-update|guides/how-to-enable-remote-shell|guides/how-to-use-gateway-shell)", "delete", "-", "Python gateway install, customization and shell; SENTIENT Gateway is a Rust binary"),
    (r"^docs/user-guide/integrations/ibm-watson", "delete", "-", "Integration type not available in SENTIENT"),
    (r"^docs/user-guide/edge-computing", "delete", "-", "Duplicate of the SENTIENT Edge section"),
    (r"^docs/(guides|getting-started)\.md$", "delete", "-", "ThingsBoard landing page (edition picker / video gallery)"),
    # rewrite: exists in SENTIENT with different screens or behaviour
    (r"^docs/(getting-started|getting-started-guides)", "rewrite", "W1", "First steps on SENTIENT"),
    (r"^docs/user-guide/(ui/|dashboards|widgets|scada|visualization|advanced-guides-for-working-with-dashboard)", "rewrite", "W2", "UI and widgets differ in SENTIENT"),
    (r"^docs/user-guide/(alarms|alarm-rules|notifications|device-profiles|asset-profiles|tenant-profiles|calculated-fields|device-connectivity-status|device-provisioning|claiming-devices|bulk-provisioning|ota-updates|entity-views)", "rewrite", "W2", "Device and alarm screens differ in SENTIENT"),
    (r"^docs/iot-gateway/", "rewrite", "W2", "SENTIENT Gateway is a new Rust gateway with its own admin UI and connectors"),
    (r"^docs/user-guide/rule-engine", "rewrite", "W3", "SENTIENT rule engine (Rust) implements the nodes differently"),
    (r"^docs/user-guide/integrations/", "rewrite", "W3", "Integration screens differ in SENTIENT"),
    (r"^docs/user-guide/(security|ssl|oauth-2-support|two-factor-authentication|certificates|mqtt-over-ssl|coap-over-dtls|version-control|audit-log|api-limits|image-gallery|resources|templatization|tbel|psm|troubleshooting|customization)", "rewrite", "W3", "Administration features differ in SENTIENT"),
    (r"^docs/user-guide/contribution/", "rewrite", "W3", "Widget development against SENTIENT"),
    (r"^docs/edge/", "rewrite", "W3", "SENTIENT Edge"),
    (r"^docs/mobile/", "rewrite", "W3", "SENTIENT mobile app (APK)"),
    (r"^docs/reference/", "check", "W7", "Protocol and API reference; verify against SENTIENT"),
    (r"^docs/user-guide/(attributes|telemetry|rpc|entities-and-relations|access-token|basic-mqtt|device-credentials|advanced-filters)", "check", "W2", "Concept page; verify against SENTIENT"),
    (r".*", "check", "W3", "Review"),
]


def front(text):
    m = re.match(r"\+\+\+\n(.*?)\n\+\+\+", text, re.S)
    fm = m.group(1) if m else ""
    title = re.search(r'^title = "(.*)"', fm, re.M)
    status = re.search(r'^status = "(.*)"', fm, re.M)
    return (title.group(1) if title else ""), (status.group(1) if status else "")


def url_of(rel):
    p = Path(rel)
    return "/" + str(p.parent if p.name == "_index.md" else p.with_suffix("")).strip("/") + "/"


def main():
    helpfile = None
    if "--helplinks" in sys.argv:
        helpfile = Path(sys.argv[sys.argv.index("--helplinks") + 1])
    help_by_url = {}
    if helpfile and helpfile.exists():
        for line in helpfile.read_text().splitlines():
            key, _, link = line.partition(" ")
            u = link.split("#")[0].rstrip("/") + "/"
            help_by_url.setdefault(u, []).append(key.rstrip(":"))
    rows, aliases = [], set()
    for f in sorted(CONTENT.rglob("*.md")):
        rel = str(f.relative_to(CONTENT))
        text = f.read_text(encoding="utf-8")
        title, status = front(text)
        if "transparent = true" in text and "[extra]" not in text:
            continue  # generated folder index
        url = url_of(rel)
        if status == "planned":
            verdict, wave, reason = "planned", re.search(r'^wave = "(.*)"', text, re.M), "New SENTIENT page"
            wave = wave.group(1) if wave else "W3"
        elif status == "checked":
            verdict, wave, reason = "done", "-", "Checked"
        else:
            for rx, verdict, wave, reason in RULES:
                if re.search(rx, rel):
                    break
            node = Path(rel).stem
            if "/rule-engine-2-0/nodes/" in rel and node in MISSING_NODES:
                verdict, wave, reason = "delete", "-", "Rule node not available in SENTIENT"
        helps = help_by_url.get(url, [])
        if helps and verdict in ("rewrite", "check"):
            wave = "W1"  # the UI already links here
        for a in re.findall(r'"([^"]+)"', (re.search(r"^aliases = \[(.*)\]$", text, re.M) or [None, ""])[1]):
            aliases.add("/" + a.strip("/") + "/")
        rows.append({"path": rel, "url": url, "title": title, "verdict": verdict, "wave": wave,
                     "ui_help_links": " ".join(helps), "reason": reason})
    out = ROOT / "audit"
    out.mkdir(exist_ok=True)
    with open(out / "pages.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    v = Counter(r["verdict"] for r in rows)
    wv = Counter((r["wave"], r["verdict"]) for r in rows if r["verdict"] != "delete")
    linked = {u for u in help_by_url}
    have = {r["url"] for r in rows if r["verdict"] != "delete"} | aliases
    missing_help = sorted(u for u in linked if u not in have)
    lines = ["# Content audit", "", "Generated by `tools/audit.py`. One row per page in `audit/pages.csv`.", "",
             "| Verdict | Pages |", "|---|---|"] + [f"| {k} | {n} |" for k, n in v.most_common()]
    lines += ["", "| Wave | Rewrite | Check | Planned |", "|---|---|---|---|"]
    for wave in sorted({k[0] for k in wv}):
        lines.append(f"| {wave} | {wv.get((wave, 'rewrite'), 0)} | {wv.get((wave, 'check'), 0)} | {wv.get((wave, 'planned'), 0)} |")
    lines += ["", f"UI help links: {sum(len(x) for x in help_by_url.values())} links to {len(linked)} pages; "
              f"{len(linked) - len(missing_help)} of those open a page or a redirect to one.", ""]
    if missing_help:
        lines += ["Help-link targets with no page yet (each needs a page or a redirect):", ""]
        lines += [f"- `{u}` ({', '.join(help_by_url[u])})" for u in missing_help]
    (out / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:20]))


if __name__ == "__main__":
    main()
