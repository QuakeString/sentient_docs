#!/usr/bin/env python3
# Copyright © 2016-2025 The SENTIENT Authors
"""Repair internal links in content/ after the audit removed pages.

  python3 tools/convert/fixlinks.py SITE [--ref 78bb93d2]

SITE is a built site (tools/build.sh output): every directory with an
index.html, including redirect pages, counts as a valid target.
- downloadable files (json, csv, pem, ...) that pages link to are copied from
  the legacy docs tree at --ref into static/, at the path the page links to;
- links into removed editions (/docs/pe/, /docs/paas/) and Edge copies of
  platform pages go to the matching platform page;
- links to the old marketing site (pricing, products, contact) are unlinked.
Prints what is still broken.
"""
import re, subprocess, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT, STATIC = ROOT / "content", ROOT / "static"
site = Path(sys.argv[1])
ref = sys.argv[sys.argv.index("--ref") + 1] if "--ref" in sys.argv else "78bb93d2"

pages = {"/" + str(p.parent.relative_to(site)).strip(".").strip("/") + "/" for p in site.rglob("index.html")}
pages = {p.replace("//", "/") for p in pages}
legacy = set(subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "docs"], cwd=ROOT,
                            capture_output=True, text=True, check=True).stdout.split())

MAP = {
    "/docs/user-guide/rule-engine/": "/docs/user-guide/rule-engine-2-0/overview/",
    "/docs/user-guide/visualization/": "/docs/user-guide/dashboards/",
    "/docs/user-guide/rule-engine-2-0/tutorials/create-clear-alarms/": "/docs/tutorials/create-clear-alarms/",
    "/docs/user-guide/rule-engine-2-0/tutorials/send-email/": "/docs/tutorials/send-email/",
    "/docs/user-guide/rule-engine-2-0/tutorials/validate-incoming-telemetry/": "/docs/tutorials/validate-incoming-telemetry/",
    "/docs/user-guide/rule-engine-2-0/tutorials/transform-incoming-telemetry/": "/docs/user-guide/rule-engine-2-0/tutorials/transform-telemetry-using-previous-record/",
    "/docs/user-guide/install/pe/installation-options/": "/docs/installation/",
    "/docs/user-guide/install/installation-options/": "/docs/installation/",
    "/docs/user-guide/rbac/": "/docs/administration/roles/",
    "/docs/user-guide/groups/": "/docs/administration/entity-groups/",
    "/docs/user-guide/reporting/": "/docs/reports/",
    "/docs/user-guide/scheduler/": "/docs/user-guide/scheduler/",
    "/docs/user-guide/secrets-storage/": "/docs/administration/secrets/",
    "/docs/getting-started-guides/helloworld-pe/": "/docs/getting-started-guides/helloworld/",
    "/docs/solution-templates/overview/": "/docs/solution-hub/",
    "/docs/user-guide/custom-translation/": "/docs/administration/translations/",
    "/docs/user-guide/ui/trip-animation-widget/": "/docs/user-guide/widgets/map-widgets/",
    "/docs/iot-gateway/integration-with-telegram-bot/": "/docs/user-guide/rule-engine-2-0/tutorials/integration-with-telegram-bot/",
    "/docs/rule-engine/rule-chain-templates/": "/docs/edge/rule-engine/rule-chain-templates/",
    "/docs/getting-started-guides/what-is-edge/": "/docs/edge/getting-started-guides/what-is-edge/",
    "/docs/user-guide/contribution/ui/widget-library/": "/docs/user-guide/ui/widget-library/",
    "/device-library/": "/docs/getting-started-guides/connectivity/",
    "/docs/device-library/": "/docs/getting-started-guides/connectivity/",
    "/docs/devices-library/": "/docs/getting-started-guides/connectivity/",
}
UNLINK = re.compile(r"^/(products|installations|pricing|contact-us|docs/contact-us|partners|company|blog|usecases|industries|trendz|services|case-studies)(/|$)")
EDITION = re.compile(r"^/docs/(pe/edge|pe|paas/eu|paas)/")
LINK = re.compile(r"(\]\(|href=\")(/[^)\"\s#?]*)([#?][^)\"\s]*)?")
copied, fixed, unlinked, still = 0, 0, 0, Counter()


def is_file(u):
    return "." in u.rsplit("/", 1)[-1]


def norm(u):
    u = re.sub(r"/{2,}", "/", u)
    return u if is_file(u) or u.endswith("/") else u + "/"


def ok(u):
    return (u in pages) if not is_file(u) else (STATIC / u.lstrip("/")).exists() or (site / u.lstrip("/")).exists()


def fetch(u):
    """Copy a downloadable file from the legacy tree (any edition) to static/u."""
    global copied
    rel = u.lstrip("/")
    cands = [rel] + [re.sub(r"^docs/", f"docs/{e}/", rel) for e in ("pe", "paas", "paas/eu")]
    for c in cands:
        if c in legacy:
            dst = STATIC / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(subprocess.run(["git", "show", f"{ref}:{c}"], cwd=ROOT, capture_output=True, check=True).stdout)
            copied += 1
            return True
    return False


def resolve(u):
    n = norm(u)
    if ok(n):
        return n
    if n in MAP and ok(MAP[n]):
        return MAP[n]
    m = EDITION.match(n)
    if m:
        cand = "/docs/" + n[m.end():]
        if is_file(cand) and fetch(cand):
            return cand
        r = resolve(cand) if cand != n else None
        if r:
            return r
    if n.startswith("/docs/edge/") and not n.startswith("/docs/edge/getting-started"):
        for cand in ("/docs/" + n[len("/docs/edge/"):], n.replace("/docs/edge/user-guide/", "/docs/user-guide/")):
            if ok(cand):
                return cand
    if is_file(n) and fetch(n):
        return n
    return None


for f in sorted(CONTENT.rglob("*.md")):
    text = f.read_text(encoding="utf-8")

    def sub(m):
        global fixed
        pre, url, tail = m.group(1), m.group(2), m.group(3) or ""
        if url.startswith(("/images/", "/pagefind/")) or ok(norm(url)):
            return m.group(0)
        r = resolve(url)
        if r:
            fixed += 1
            return pre + r + tail
        still[norm(url)] += 1
        return m.group(0)

    new = LINK.sub(sub, text)

    # [text](/marketing/...) -> text ; <a href="/marketing/...">text</a> -> text
    def unlink_md(m):
        global unlinked
        if UNLINK.match(m.group(2)):
            unlinked += 1
            return m.group(1)
        return m.group(0)

    new = re.sub(r"\[([^\]]*)\]\((/[^)\s]*)\)", unlink_md, new)
    new = re.sub(r'<a [^>]*href="(/[^"]*)"[^>]*>(.*?)</a>',
                 lambda m: m.group(2) if UNLINK.match(m.group(1)) else m.group(0), new, flags=re.S)
    if new != text:
        f.write_text(new, encoding="utf-8")

for u in [u for u in still if UNLINK.match(u)]:
    del still[u]
print(f"links fixed: {fixed}  files copied: {copied}  marketing links removed: {unlinked}  still broken: {sum(still.values())}")
for u, n in still.most_common(40):
    print(f"  {n:3d}  {u}")
