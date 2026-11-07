#!/usr/bin/env python3
# Copyright © 2016-2025 The SENTIENT Authors
"""Mark screenshots that have a dark-theme twin (X.webp + X-dark.webp).

Adds a bare `data-dark` attribute to each such <img>; static/js/site.js
swaps the src to the -dark file while the page is shown dark.
Usage: tools/darkimg.py <built site dir>
"""
import re, sys
from pathlib import Path

site = Path(sys.argv[1])
static = Path(__file__).resolve().parents[1] / "static"
IMG = re.compile(r'<img src="(/images/[^"]+?)(\.webp|\.png)"')

def mark(m):
    base, ext = m.group(1), m.group(2)
    if base.endswith("-dark") or not (static / f"{base.lstrip('/')}-dark{ext}").exists():
        return m.group(0)
    return f'<img data-dark src="{base}{ext}"'

n = 0
for p in site.rglob("*.html"):
    s = p.read_text(encoding="utf-8")
    t = IMG.sub(mark, s)
    if t != s:
        p.write_text(t, encoding="utf-8"); n += 1
print(f"dark screenshots marked on {n} pages")
