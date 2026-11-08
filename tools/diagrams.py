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


ICONS = {
    "server": '<rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><path d="M6 6h.01M6 18h.01"/>',
    "cpu": '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6" rx="1"/><path d="M15 2v2M15 20v2M2 15h2M2 9h2M20 15h2M20 9h2M9 2v2M9 20v2"/>',
    "router": '<rect x="2" y="14" width="20" height="8" rx="2"/><path d="M6.01 18H6M10.01 18H10M15 10v4M17.84 7.17a4 4 0 0 0-5.66 0M20.66 4.34a8 8 0 0 0-11.31 0"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14a9 3 0 0 0 18 0V5M3 12a9 3 0 0 0 18 0"/>',
    "cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>',
    "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4M16 13H8M16 17H8M10 9H8"/>',
    "workflow": '<rect x="3" y="3" width="8" height="8" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect x="13" y="13" width="8" height="8" rx="2"/>',
    "chart": '<path d="M3 3v18h18M18 17V9M13 17V5M8 17v-3"/>',
    "layers": '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83ZM22 17.65l-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65M22 12.65l-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
    "plug": '<path d="M12 22v-5M9 8V2M15 8V2M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8Z"/>',
    "code": '<path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/>',
    "key": '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6M15.5 7.5l3 3L22 7l-3-3"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "languages": '<path d="m5 8 6 6M4 14l6-6 2-3M2 5h12M7 2h1M22 22l-5-10-5 10M14 18h6"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20M2 12h20"/>',
    "activity": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
    "refresh": '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8M21 3v5h-5M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16M8 16H3v5"/>',
    "gauge": '<path d="m12 14 4-4M3.34 19a10 10 0 1 1 17.32 0"/>',
    "factory": '<path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2ZM17 18h1M12 18h1M7 18h1"/>',
    "box": '<path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16ZM3.3 7l8.7 5 8.7-5M12 22V12"/>',
    "check": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1zM9 12l2 2 4-4"/>',
    "filter": '<path d="M22 3H2l8 9.46V19l4 2v-8.54Z"/>',
    "help": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3M12 17h.01"/>',
    "fan": '<path d="M10.83 8.4c-1.2-2.7.3-6.4 3.37-6.4 2.13 0 3.8 1.9 2.8 4.5M15.6 10.83c2.7-1.2 6.4.3 6.4 3.37 0 2.13-1.9 3.8-4.5 2.8M13.17 15.6c1.2 2.7-.3 6.4-3.37 6.4-2.13 0-3.8-1.9-2.8-4.5M8.4 13.17C5.7 14.37 2 12.87 2 9.8 2 7.67 3.9 6 6.5 7"/><circle cx="12" cy="12" r="2"/>',
    "thermo": '<path d="M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z"/>',
    "send": '<path d="m22 2-7 20-4-9-9-4ZM22 2 11 13"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "monitor": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "smartphone": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
}

# keyword -> icon, first match wins (used when a box does not name its icon)
AUTO_ICON = [
    ("server", "server"), ("edge", "server"), ("gateway", "router"), ("postgres", "database"), ("timescale", "database"),
    ("clickhouse", "database"), ("database", "database"), ("storage", "database"), ("rule engine", "workflow"),
    ("dashboard", "chart"), ("alarm", "bell"), ("notification", "mail"), ("scheduler", "clock"), ("report", "file"),
    ("operator", "user"), ("other systems", "code"), ("application", "code"), ("converter", "refresh"),
    ("integration", "plug"), ("cloud", "cloud"), ("aws", "cloud"), ("azure", "cloud"), ("plc", "factory"),
    ("translator", "languages"), ("platform manager", "wrench"), ("licence", "key"), ("queue", "layers"),
    ("actor", "activity"), ("web ui", "globe"), ("analytics", "chart"), ("fan", "fan"), ("temperature", "thermo"),
    ("moisture", "gauge"), ("irrigation", "gauge"), ("sensor", "gauge"), ("device", "cpu"), ("region", "box"),
    ("field", "box"), ("asset", "box"), ("broker", "send"), ("opc ua", "server"), ("sigfox", "cloud"),
    ("thingpark", "cloud"), ("oceanconnect", "cloud"), ("platform", "cloud"), ("checks", "check"), ("creates", "check"),
    ("saves", "lock"), ("filter", "filter"), ("custom", "code"), ("meters", "gauge"), ("databases", "database"),
    ("brokers", "send"), ("local web", "monitor"), ("ask us", "help"),
]


def auto_icon(title):
    t = title.lower()
    for k, ic in AUTO_ICON:
        if k in t:
            return ic
    return None


def tw(s, size=14, bold=True):
    """Rough text width for layout."""
    return len(s) * size * (0.5 if bold else 0.45)


class D:
    R = 10        # node corner radius
    BEND = 10     # connector corner radius

    def __init__(self, name, w, h, title):
        self.name, self.w, self.h, self.title = name, w, h, title
        self.el, self.boxes, self.labels = [], {}, []

    # ---------- shapes ----------
    def icon(self, name, x, y, size, cls):
        s = size / 24
        self.el.append(f'<g class="{cls}" transform="translate({x:.1f} {y:.1f}) scale({s:.3f})">{ICONS[name]}</g>')

    def box(self, key, x, y, w, h, title, sub=None, k="b", small=False, icon=None):
        self.boxes[key] = (x, y, w, h)
        lines = title.split("\n")
        if k == "chip":
            self.el.append(f'<rect class="dg-chip" x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}"/>')
            self.el.append(f'<text class="dg-ct" x="{x + w / 2}" y="{y + h / 2 + 4.5}">{escape(title)}</text>')
            return self
        self.el.append(f'<rect class="dg-n dg-n{k}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{self.R}"/>')
        ic = icon if icon is not None else auto_icon(title.replace("\n", " "))
        if ic is False:
            ic = None
        tsize = 13.5 if small or w < 170 else 14.5
        title_w = max(tw(t, tsize) for t in lines)
        sub_w = tw(sub, 12, False) if sub else 0
        tile = 32 if h >= 52 else 26
        lh = tsize + 3
        n = len(lines) + (1 if sub else 0)
        if ic and w >= 30 + tile + max(title_w, sub_w) and h >= 36:
            # icon tile on the left, text left-aligned
            tx, ty = x + 12, y + (h - tile) / 2
            self.el.append(f'<rect class="dg-tile dg-tile{k}" x="{tx}" y="{ty}" width="{tile}" height="{tile}" rx="8"/>')
            isz = tile * 0.56
            self.icon(ic, tx + (tile - isz) / 2, ty + (tile - isz) / 2, isz, f"dg-ic dg-ic{k}")
            x0 = tx + tile + 11
            y0 = y + h / 2 - (n - 1) * lh / 2 + 4.5
            for i, t in enumerate(lines):
                self.el.append(f'<text class="dg-t dg-t{k}" style="text-anchor:start;font-size:{tsize}px" x="{x0}" y="{y0 + i * lh}">{escape(t)}</text>')
            if sub:
                self.el.append(f'<text class="dg-u" style="text-anchor:start" x="{x0}" y="{y0 + len(lines) * lh}">{escape(sub)}</text>')
        elif ic and h >= 80:
            # narrow and tall: icon on top, text centred below
            tx, ty = x + (w - tile) / 2, y + 12
            self.el.append(f'<rect class="dg-tile dg-tile{k}" x="{tx}" y="{ty}" width="{tile}" height="{tile}" rx="8"/>')
            isz = tile * 0.56
            self.icon(ic, tx + (tile - isz) / 2, ty + (tile - isz) / 2, isz, f"dg-ic dg-ic{k}")
            y0 = ty + tile + 18
            for i, t in enumerate(lines):
                self.el.append(f'<text class="dg-t dg-t{k}" style="font-size:{tsize}px" x="{x + w / 2}" y="{y0 + i * lh}">{escape(t)}</text>')
            if sub:
                self.el.append(f'<text class="dg-u" x="{x + w / 2}" y="{y0 + len(lines) * lh}">{escape(sub)}</text>')
        else:
            y0 = y + h / 2 - (n - 1) * lh / 2 + 4.5
            for i, t in enumerate(lines):
                self.el.append(f'<text class="dg-t dg-t{k}" style="font-size:{tsize}px" x="{x + w / 2}" y="{y0 + i * lh}">{escape(t)}</text>')
            if sub:
                self.el.append(f'<text class="dg-u" x="{x + w / 2}" y="{y0 + len(lines) * lh}">{escape(sub)}</text>')
        return self

    def stack(self, key, x, y, w, h, title, sub=None, k="b", icon=None):
        """A card drawn as a pile of several (many devices, many assets)."""
        for d in (8, 4):
            self.el.append(f'<rect class="dg-n dg-n{k} dg-ghost" x="{x + d}" y="{y - d}" width="{w}" height="{h}" rx="{self.R}"/>')
        return self.box(key, x, y, w, h, title, sub, k, icon=icon)

    def cyl(self, key, x, y, w, h, title, sub=None):
        return self.box(key, x, y, w, h, title, sub, "b", icon="database")

    def group(self, x, y, w, h, title=None, k="g", right=None):
        self.el.append(f'<rect class="dg-{k}" x="{x}" y="{y}" width="{w}" height="{h}" rx="16"/>')
        if title:
            self.el.append(f'<text class="dg-gh dg-gh{k}" style="text-anchor:start" x="{x + 18}" y="{y + 27}">{escape(title)}</text>')
        if right:
            self.el.append(f'<text class="dg-gs" style="text-anchor:end" x="{x + w - 18}" y="{y + 27}">{escape(right)}</text>')
        return self

    def text(self, x, y, s, cls="dg-lbl", anchor="start"):
        if cls == "dg-lbl":
            self.labels.append((x, y, s, anchor))
            return self
        self.el.append(f'<text class="{cls}" style="text-anchor:{anchor}" x="{x}" y="{y}">{escape(s)}</text>')
        return self

    def heading(self, x, y, s):
        return self.text(x, y, s, "dg-h")

    # ---------- lines ----------
    def _rounded(self, pts):
        pts = [(float(a), float(b)) for a, b in pts]
        d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
        for i in range(1, len(pts) - 1):
            (x0, y0), (x1, y1), (x2, y2) = pts[i - 1], pts[i], pts[i + 1]
            l1 = abs(x1 - x0) + abs(y1 - y0)
            l2 = abs(x2 - x1) + abs(y2 - y1)
            r = min(self.BEND, l1 / 2, l2 / 2)
            if r <= 0.5:
                d += f" L{x1:.1f} {y1:.1f}"
                continue
            ax = x1 - (x1 - x0) / l1 * r if l1 else x1
            ay = y1 - (y1 - y0) / l1 * r if l1 else y1
            bx = x1 + (x2 - x1) / l2 * r if l2 else x1
            by = y1 + (y2 - y1) / l2 * r if l2 else y1
            d += f" L{ax:.1f} {ay:.1f} Q{x1:.1f} {y1:.1f} {bx:.1f} {by:.1f}"
        d += f" L{pts[-1][0]:.1f} {pts[-1][1]:.1f}"
        return d

    def path(self, pts, end=True, start=False, dash=False, label=None, at=None, anchor="middle"):
        cls = "dg-dl" if dash else "dg-ar"
        m = ""
        if end:
            m += f' marker-end="url(#{self.name}-a)"'
        if start:
            m += f' marker-start="url(#{self.name}-a)"'
        self.el.append(f'<path class="{cls}" d="{self._rounded(pts)}"{m}/>')
        if label:
            lx, ly = at if at else ((pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2 - 7)
            self.labels.append((lx, ly, label, anchor))
        return self

    def side(self, key, s, f=0.5):
        x, y, w, h = self.boxes[key]
        return {"l": (x, y + h * f), "r": (x + w, y + h * f), "t": (x + w * f, y), "b": (x + w * f, y + h)}[s]

    def link(self, a, b, label=None, sa="r", sb="l", fa=0.5, fb=0.5, mid=None, **kw):
        """Elbow line from one box to another (right side to left side by default)."""
        p, q = self.side(a, sa, fa), self.side(b, sb, fb)
        gap = 2
        q = {"l": (q[0] - gap, q[1]), "r": (q[0] + gap, q[1]), "t": (q[0], q[1] - gap), "b": (q[0], q[1] + gap)}[sb]
        if sa in "lr" and sb in "lr":
            mx = mid if mid is not None else (p[0] + q[0]) / 2
            pts = [p, (mx, p[1]), (mx, q[1]), q] if p[1] != q[1] else [p, q]
            if label and "at" not in kw:
                kw["at"] = (q[0] - 10, q[1] - 9)
                kw.setdefault("anchor", "end")
        elif sa in "tb" and sb in "tb":
            my = mid if mid is not None else (p[1] + q[1]) / 2
            pts = [p, (p[0], my), (q[0], my), q] if p[0] != q[0] else [p, q]
            if label and "at" not in kw:
                kw["at"] = (q[0] + 10, (p[1] + q[1]) / 2 + 4)
                kw.setdefault("anchor", "start")
        elif sa in "lr":
            pts = [p, (q[0], p[1]), q]
        else:
            pts = [p, (p[0], q[1]), q]
        return self.path(pts, label=label, **kw)

    def svg(self):
        out = []
        for x, y, s, anchor in self.labels:   # labels sit on small pills above the lines
            w = tw(s, 11.5, False) + 14
            lx = x - w / 2 if anchor == "middle" else (x - w + 7 if anchor == "end" else x - 7)
            out.append(f'<rect class="dg-pill" x="{lx:.1f}" y="{y - 12.5:.1f}" width="{w:.1f}" height="18" rx="9"/>'
                       f'<text class="dg-lbl" style="text-anchor:{anchor}" x="{x}" y="{y}">{escape(s)}</text>')
        head = (f'<svg class="st-diagram-svg" viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="{self.name}-t" xmlns="http://www.w3.org/2000/svg">'
                f'<title id="{self.name}-t">{escape(self.title)}</title>'
                f'<defs><marker id="{self.name}-a" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto-start-reverse">'
                f'<path class="dg-ah" d="M1 1.5 9 5 1 8.5 2.6 5Z"/></marker></defs>')
        return head + "".join(self.el) + "".join(out) + "</svg>\n"


ALL = []


def diagram(fn):
    ALL.append(fn)
    return fn


# ====================================================================== platform
@diagram
def architecture():
    d = D("architecture", 1160, 680, "SENTIENT architecture: equipment connects to the SENTIENT server, which keeps its data in PostgreSQL and optionally TimescaleDB or ClickHouse, and serves operators and other systems")
    EX, EW = 24, 256          # equipment column
    GX, GW = 336, 500         # server group
    IX, IW = GX + 20, GW - 40  # inside the group
    RX, RW = 892, 244         # right column
    d.group(GX, 44, GW, 508, "SENTIENT server", right="one program, service or container")
    d.heading(EX, 70, "Equipment").heading(RX, 70, "Storage").heading(RX, 390, "People and systems")
    d.box("dev", EX, 96, EW, 64, "Devices and sensors", "MQTT · HTTP · CoAP · SNMP")
    d.box("plc", EX, 200, EW, 64, "PLCs, meters, drives", "Modbus · OPC UA · S7 · BACnet", icon="factory")
    d.box("gw", EX, 320, EW, 64, "SENTIENT Gateway", "near the equipment, sends MQTT", "s")
    d.box("cloud", EX, 440, EW, 64, "Cloud services", "AWS IoT · Azure · TCP · UDP")
    # device connections panel
    d.el.append(f'<rect class="dg-n" x="{IX}" y="88" width="{IW}" height="86" rx="10"/>')
    d.text(IX + 16, 112, "Device connections", "dg-h2")
    for i, n in enumerate(["MQTT", "HTTP", "CoAP", "SNMP", "Integrations"]):
        cw = 104 if i == 4 else 74
        cx = IX + 16 + i * 84
        d.box(f"t{i}", cx, 126, cw, 30, n, k="chip")
    d.link("plc", "gw", sa="b", sb="t")
    E = EX + EW
    d.path([(E, 128), (IX - 2, 128)])
    d.path([(E, 352), (E + 26, 352), (E + 26, 144), (IX - 2, 144)])
    d.path([(E, 472), (E + 42, 472), (E + 42, 160), (IX - 2, 160)])
    # processing
    d.box("act", IX, 200, 218, 60, "Device actors", "sessions · commands")
    d.box("q", IX + IW - 218, 200, 218, 60, "Queues", "Main · HighPriority")
    d.path([(IX + 109, 174), (IX + 109, 198)])
    d.path([(IX + 218, 230), (IX + IW - 220, 230)])
    d.box("re", IX, 286, IW, 64, "Rule engine", "rule chains · alarm rules · calculated fields", "a")
    d.path([(IX + IW - 109, 260), (IX + IW - 109, 284)])
    cw = (IW - 3 * 12) / 4
    for i, (t, sub) in enumerate([("Alarms", "live push"), ("Notifications", "email · SMS"), ("Scheduler", "timed jobs"), ("Reports", "PDF · CSV")]):
        x = IX + i * (cw + 12)
        d.box(f"r{i}", x, 376, cw, 90, t, sub, small=True)
        d.path([(x + cw / 2, 350), (x + cw / 2, 374)])
    d.box("web", IX, 482, IW, 50, "Web UI · REST API · WebSocket", k="s", icon="globe")
    # storage
    for i, (key, t, sub) in enumerate([("pg", "PostgreSQL", "configuration, alarms, telemetry"), ("ts", "TimescaleDB", "optional: compressed history"), ("ch", "ClickHouse", "optional: high-rate history")]):
        d.cyl(key, RX, 92 + i * 80, RW, 64, t, sub)
    B = GX + GW + 28
    d.path([(IX + IW, 318), (B, 318), (B, 124), (RX - 2, 124)])
    d.path([(B, 204), (RX - 2, 204)]).path([(B, 284), (RX - 2, 284)])
    d.box("op", RX, 411, RW, 56, "Operators", "browser · mobile app")
    d.box("ext", RX, 479, RW, 56, "Other systems", "ERP · MES · scripts")
    d.path([(IX + IW, 507), (B, 507), (B, 439), (RX - 2, 439)])
    d.path([(B, 507), (RX - 2, 507)])
    # around the server
    d.heading(EX, 612, "Around the server")
    for i, (t, sub, ic) in enumerate([("SENTIENT translator", "offline translation", "languages"), ("Platform Manager", "install · update · backup", "wrench"), ("Licence server", "activation", "key")]):
        x = IX + i * 256
        d.path([(GX + GW / 2, 552), (GX + GW / 2, 566), (x + 116, 566), (x + 116, 584)], dash=True)
        d.box(f"o{i}", x, 586, 232, 60, t, sub, "o", icon=ic)
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
