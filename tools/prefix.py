#!/usr/bin/env python3
# Copyright © 2016-2025 The SENTIENT Authors
"""Rewrite root-relative links in a built docs version so it can be served
under a path prefix such as /v/4.3.0.55/. Images (/images/) and the version
list (/versions.json) stay at the site root, shared by every version."""
import re, sys
from pathlib import Path

out, prefix = Path(sys.argv[1]), sys.argv[2].rstrip("/")
SHARED = ("/images/", "/versions.json")
rx = re.compile(r'((?:href|src|content)=")(/(?!/)[^"]*)"')

def fix(m):
    url = m.group(2)
    if url.startswith(SHARED) or url.startswith(prefix + "/"):
        return m.group(0)
    return f'{m.group(1)}{prefix}{url}"'

n = 0
for f in out.rglob("*.html"):
    s = f.read_text(encoding="utf-8")
    t = rx.sub(fix, s)
    t = re.sub(r'(http-equiv="refresh" content="0; ?url=)(/(?!v/)[^"]*)"', lambda m: f'{m.group(1)}{prefix}{m.group(2)}"', t).replace('<meta name="st-docs-base" content="">', f'<meta name="st-docs-base" content="{prefix}">')
    if t != s:
        f.write_text(t, encoding="utf-8"); n += 1
print(f"prefix {prefix}: rewrote {n} pages")
