#!/usr/bin/env python3
# Copyright © 2016-2025 The SENTIENT Authors
"""Content checks on a built site (tools/build.sh output).

Fails only for pages that are marked as checked (front matter extra.status is
not "imported"), so carried-over pages can be fixed wave by wave. Everything
else is reported as a count, with the worst pages listed.

  python3 tools/check.py public [--all]   (--all: list every problem)
"""
import re, sys
from collections import Counter, defaultdict
from pathlib import Path

site = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
show_all = "--all" in sys.argv
pages = {p for p in site.rglob("index.html")}
existing = set()
for p in pages:
    rel = "/" + str(p.parent.relative_to(site)).strip(".") + "/"
    existing.add(rel.replace("//", "/"))
files = {"/" + str(p.relative_to(site)) for p in site.rglob("*") if p.is_file()}

HREF = re.compile(r'href="(/[^"#?]*)')
SRC = re.compile(r'src="(/images/[^"]+)"')
BODY = re.compile(r"<article[^>]*>(.*?)</article>", re.S)
problems = defaultdict(list)
imported_pages = 0
strict_fail = []
for p in sorted(pages):
    html = p.read_text(encoding="utf-8", errors="replace")
    m = BODY.search(html)
    if not m:
        continue
    body = m.group(1)
    if "data-fallback" in m.group(0)[:300]:
        continue   # an untranslated page shown in English; the English page is checked
    imported = 'data-status="imported"' in body or "This page was carried over" in body
    imported_pages += imported
    url = "/" + str(p.parent.relative_to(site)).strip(".") + "/"
    found = []
    for h in HREF.findall(body):
        if h.startswith(("/images/", "/pagefind/")):
            continue
        n = h if h.endswith("/") or "." in h.rsplit("/", 1)[-1] else h + "/"
        if n not in existing and h not in files:
            found.append(("broken-link", h))
    for s in SRC.findall(body):
        if s not in files:
            found.append(("missing-image", s))
    text = re.sub(r"<[^>]+>", " ", body)
    for w in re.findall(r"\bThings[Bb]oard\b|\bTrendz\b|thingsboard\.io", text):
        found.append(("old-name", w))
    if found:
        problems[url] = found
        if not imported:
            strict_fail.append(url)

# every sidebar entry must open a real page (not a redirect)
nav_fail = []
for nav in sorted((Path(__file__).resolve().parents[1] / "data" / "nav").glob("*.yml")):
    for path in re.findall(r"^\s*path:\s*(\S+)", nav.read_text(encoding="utf-8"), re.M):
        f = site / path.strip("/") / "index.html"
        if not f.exists() or 'http-equiv="refresh"' in f.read_text(encoding="utf-8", errors="replace")[:600]:
            nav_fail.append(f"{nav.name}: {path}")

kinds = Counter(k for v in problems.values() for k, _ in v)
print(f"pages: {len(pages)}  carried over (not yet checked): {imported_pages}")
for k, n in kinds.most_common():
    print(f"  {k}: {n}")
worst = sorted(problems.items(), key=lambda kv: -len(kv[1]))
for url, found in (worst if show_all else worst[:10]):
    print(f"  {len(found):4d}  {url}")
    if show_all:
        for k, v in found:
            print(f"          {k}: {v}")
if nav_fail:
    print("\nSidebar entries that do not open a page:")
    for u in nav_fail:
        print("  " + u)
if strict_fail:
    print("\nChecked pages with problems (these fail the build):")
    for u in strict_fail:
        print("  " + u)
if strict_fail or nav_fail:
    sys.exit(1)
