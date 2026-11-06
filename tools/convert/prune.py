#!/usr/bin/env python3
# Copyright © 2016-2025 The SENTIENT Authors
"""Apply the content audit: remove pages marked "delete" in audit/pages.csv,
keep their URLs working as redirects to the nearest SENTIENT page, add the
redirects the SENTIENT UI help links need, and drop images no page uses.

  python3 tools/convert/prune.py [--dry-run]

Run tools/audit.py first. Safe to run again: it only touches pages that are
still marked "delete".
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"
IMAGES = ROOT / "static" / "images"
DRY = "--dry-run" in sys.argv

# Deleted pages redirect to the first matching target (path prefix -> page file).
REDIRECTS = [
    ("docs/getting-started.md", "docs/getting-started-guides/helloworld.md"),
    ("docs/user-guide/install/", "docs/installation/_index.md"),
    ("docs/edge/releases/", "docs/reference/release-notes.md"),
    ("docs/releases/", "docs/reference/release-notes.md"),
    ("docs/devices-library/", "docs/getting-started-guides/connectivity.md"),
    ("docs/reference/", "docs/reference/architecture.md"),
    ("docs/user-guide/contribution/", "docs/user-guide/contribution/widgets-development.md"),
    ("docs/mobile/", "docs/mobile/_index.md"),
    ("docs/edge/", "docs/edge/_index.md"),
    ("docs/user-guide/rule-engine-2-5/", "docs/user-guide/rule-engine-2-5/queues.md"),
    ("docs/user-guide/rule-engine-2-0/nodes/", "docs/user-guide/rule-engine-2-0/nodes/_index.md"),
    ("docs/iot-gateway/install/", "docs/iot-gateway/installation.md"),
    ("docs/iot-gateway/", "docs/iot-gateway/_index.md"),
    ("docs/user-guide/integrations/", "docs/user-guide/integrations/_index.md"),
    ("docs/user-guide/edge-computing", "docs/edge/_index.md"),
    ("", "docs/_index.md"),
]

# URLs the SENTIENT UI help buttons open (ui-ngx HelpLinks) that have no page
# of their own: send them to the page that covers the screen.
HELP_ALIASES = {
    "/docs/user-guide/rule-engine-2-0/action-nodes/": "docs/user-guide/rule-engine-2-0/nodes/action/_index.md",
    "/docs/user-guide/rule-engine-2-0/enrichment-nodes/": "docs/user-guide/rule-engine-2-0/nodes/enrichment/_index.md",
    "/docs/user-guide/rule-engine-2-0/external-nodes/": "docs/user-guide/rule-engine-2-0/nodes/external/_index.md",
    "/docs/user-guide/rule-engine-2-0/filter-nodes/": "docs/user-guide/rule-engine-2-0/nodes/filter/_index.md",
    "/docs/user-guide/rule-engine-2-0/flow-nodes/": "docs/user-guide/rule-engine-2-0/nodes/flow/_index.md",
    "/docs/user-guide/rule-engine-2-0/transformation-nodes/": "docs/user-guide/rule-engine-2-0/nodes/transformation/_index.md",
    "/docs/user-guide/queue/": "docs/user-guide/rule-engine-2-5/queues.md",
    "/docs/user-guide/ui/asset-profiles/": "docs/user-guide/asset-profiles.md",
    "/docs/user-guide/ui/device-profiles/": "docs/user-guide/device-profiles.md",
    "/docs/user-guide/ui/tenant-profiles/": "docs/user-guide/tenant-profiles.md",
    "/docs/user-guide/ui/dashboards/": "docs/user-guide/dashboards.md",
    "/docs/user-guide/ui/rule-chains/": "docs/user-guide/rule-engine-2-0/overview.md",
    "/docs/user-guide/ui/jwt-security-settings/": "docs/user-guide/ui/security-settings.md",
    "/docs/trendz/": "docs/administration/_index.md",
}

FM = re.compile(r"\A\+\+\+\n(.*?)\n\+\+\+\n", re.S)


def url_of(rel):
    p = Path(rel)
    return "/" + str(p.parent if p.name == "_index.md" else p.with_suffix("")).strip("/") + "/"


def read_aliases(text):
    m = FM.match(text)
    a = re.search(r"^aliases = \[(.*?)\]$", m.group(1), re.M) if m else None
    return re.findall(r'"([^"]+)"', a.group(1)) if a else []


def norm(u):
    return "/" + u.strip("/") + "/"


def set_aliases(path, aliases):
    text = path.read_text(encoding="utf-8")
    m = FM.match(text)
    fm = m.group(1)
    line = "aliases = [" + ", ".join(f'"{a}"' for a in aliases) + "]"
    if re.search(r"^aliases = \[.*\]$", fm, re.M):
        fm = re.sub(r"^aliases = \[.*\]$", line, fm, count=1, flags=re.M)
    else:
        # top-level keys must come before the first [table]
        head, sep, tail = fm.partition("\n[")
        fm = head.rstrip("\n") + "\n" + line + ("\n\n[" + tail if sep else "")
    path.write_text("+++\n" + fm + "\n+++\n" + text[m.end():], encoding="utf-8")


def main():
    rows = list(csv.DictReader(open(ROOT / "audit" / "pages.csv", encoding="utf-8")))
    doomed = [r for r in rows if r["verdict"] == "delete" and (CONTENT / r["path"]).exists()]
    keep_urls = {r["url"] for r in rows if r["verdict"] != "delete"}
    extra = {}  # target file -> aliases to add
    for r in doomed:
        src = CONTENT / r["path"]
        olds = [r["url"]] + [norm(a) for a in read_aliases(src.read_text(encoding="utf-8"))]
        target = next(t for prefix, t in REDIRECTS if r["path"].startswith(prefix) and (CONTENT / t).exists())
        extra.setdefault(target, []).extend(olds)
    for u, t in HELP_ALIASES.items():
        extra.setdefault(t, []).append(u)
    # every alias may exist once and never shadow a real page
    taken = set(keep_urls)
    for f in CONTENT.rglob("*.md"):
        if str(f.relative_to(CONTENT)) not in {r["path"] for r in doomed}:
            taken.update(norm(a) for a in read_aliases(f.read_text(encoding="utf-8")))
    added = 0
    for target, aliases in sorted(extra.items()):
        path = CONTENT / target
        if not path.exists():
            print("missing redirect target", target)
            continue
        have = read_aliases(path.read_text(encoding="utf-8"))
        new = []
        for a in aliases:
            if norm(a) in taken or a == url_of(target):
                continue
            taken.add(norm(a))
            new.append(a)
        if new and not DRY:
            set_aliases(path, have + new)
        added += len(new)
    for r in doomed:
        if not DRY:
            (CONTENT / r["path"]).unlink()
    # drop generated folder indexes that no longer hold anything
    for d in sorted({p for p in CONTENT.rglob("*") if p.is_dir()}, key=lambda p: -len(p.parts)):
        idx = d / "_index.md"
        others = [p for p in d.iterdir() if p.name != "_index.md"]
        if idx.exists() and not others:
            t = idx.read_text(encoding="utf-8")
            if "transparent = true" in t and "[extra]" not in t and not DRY:
                idx.unlink()
        if not any(d.iterdir()) and not DRY:
            d.rmdir()
    # images that no remaining page, template or data file references
    used = set()
    for base in (CONTENT, ROOT / "templates", ROOT / "data"):
        for f in base.rglob("*"):
            if f.is_file() and f.suffix in (".md", ".html", ".yml", ".toml"):
                used.update(re.findall(r"/images/([^\s\"')\]>?#]+)", f.read_text(encoding="utf-8", errors="replace")))
    dropped = size = 0
    for img in IMAGES.rglob("*"):
        rel = str(img.relative_to(IMAGES))
        if img.is_file() and rel not in used and not rel.startswith("st/"):  # st/ = tools/screenshots output
            size += img.stat().st_size
            dropped += 1
            if not DRY:
                img.unlink()
    for d in sorted((p for p in IMAGES.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts)):
        if not any(d.iterdir()) and not DRY:
            d.rmdir()
    print(f"deleted pages: {len(doomed)}  redirects added: {added}  unused images: {dropped} ({size / 1e6:.0f} MB)")


if __name__ == "__main__":
    main()
