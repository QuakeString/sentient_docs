#!/usr/bin/env python3
# Copyright © 2016-2025 The SENTIENT Authors
"""One-shot migration of the Jekyll docs (ThingsBoard fork, rebrand commit
78bb93d2) into the Zola site in this repository.

Steps:
  1. Export the legacy tree from git into a work dir and drop removed sections.
  2. Run Jekyll with tools/convert/jekyll-plugins (Liquid only, Markdown kept)
     and the include overrides in tools/convert/jekyll-includes, which turn
     galleries, banners and tabs into plain HTML wrappers Zola can pass through.
  3. Post-process every page: TOML front matter, kramdown-only syntax removed,
     redirects as Zola aliases, images converted to WebP.

Usage:  python3 tools/convert/convert.py --ref 78bb93d2 --work /tmp/st-convert
"""
import argparse, json, os, re, shutil, subprocess, sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent

# Sections removed by the 2026-11-06 decision (PE, PaaS, MQTT broker, Trendz, marketing).
DROP = ["docs/paas", "docs/pe", "docs/mqtt-broker", "docs/sentient-analytics",
        "docs/private-cloud", "docs/contact-us.md", "docs/contact-us-thanks.md",
        "docs/contact-us.sass", "docs/newsletter-thanks.md", "docs/search.md",
        "docs/sitemap.md"]
DROP_GLOBS = ["docs/**/search.md", "docs/**/*-pe.md", "docs/**/*-paas.md"]
DROP_DIR_NAMES = {"pe", "paas", "paas-eu", "trendz"}


def sh(*cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def export(ref, work):
    if work.exists():
        shutil.rmtree(work)
    (work / "src").mkdir(parents=True)
    tar = subprocess.run(["git", "-C", str(REPO), "archive", ref, "_includes", "_data", "docs"],
                         check=True, capture_output=True).stdout
    subprocess.run(["tar", "-x", "-C", str(work / "src")], input=tar, check=True)
    src = work / "src"
    for d in DROP:
        p = src / d
        if p.is_dir():
            shutil.rmtree(p)
        elif p.exists():
            p.unlink()
    for g in DROP_GLOBS:
        for p in src.glob(g):
            p.unlink()
    for p in sorted((src / "docs").rglob("*"), reverse=True):
        if p.is_dir() and p.name in DROP_DIR_NAMES:
            shutil.rmtree(p)
    shutil.copy(HERE / "jekyll-config.yml", src / "_config.yml")
    shutil.copytree(HERE / "jekyll-plugins", src / "_plugins")
    shutil.copytree(HERE / "jekyll-includes", src / "_includes", dirs_exist_ok=True)
    return src


def jekyll(src, out):
    exe = shutil.which("jekyll") or "/opt/rbenv/versions/3.3.6/bin/jekyll"
    sh(exe, "build", "-d", str(out), cwd=str(src))


FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def front_matter(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(text)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def toml_str(s):
    return json.dumps(str(s), ensure_ascii=False)


KRAMDOWN = [
    (re.compile(r"^\s*\*\s*TOC\s*\n\s*\{:toc\}\s*$", re.M), ""),
    (re.compile(r"\{:\s*target=\"?_blank\"?\s*\}"), ""),
    (re.compile(r"\{:\s*[^}\n]*\}"), ""),          # other inline attribute lists
    (re.compile(r"\{::options[^}]*/\}"), ""),
    (re.compile(r"^&nbsp;\s*$", re.M), ""),
    (re.compile(r"\n{4,}"), "\n\n\n"),
    (re.compile(r"\[([^\]\n]*)\]\(\s*\)"), r"\1"),            # links without a target
    (re.compile(r"^(\s*[-*+] .*)\n\n(?=\s*[-*+] )", re.M), r"\1\n"),  # loose lists left by removed Liquid
    (re.compile(r"^(\s*[-*+] .*)\n\n(?=\s*[-*+] )", re.M), r"\1\n"),
    (re.compile(r"^(\s*)```\s*(shell|console|bash-script)\s*$", re.M), r"\1```bash"),
    (re.compile(r"^(\s*)```\s*(text|plain|none|log)\s*$", re.M), r"\1```"),
]
IMG_RE = re.compile(r"(/images/[^\s\"')]+?\.(?:png|jpe?g|gif|svg|PNG|JPG))")


def clean(body):
    for rx, rep in KRAMDOWN:
        body = rx.sub(rep, body)
    # Zola shortcode syntax must not appear literally in content.
    body = re.sub(r"\{\{(\s*[A-Za-z_][\w]*\s*\()", r"{{/*\1", body)
    return body.strip() + "\n"


def target_path(rel):
    """docs/a/b.md -> content/docs/a/b.md ; docs/a/index.md -> content/docs/a/_index.md"""
    p = Path(rel)
    if p.name == "index.md":
        return p.with_name("_index.md")
    return p


def convert_pages(src, out, content, images):
    pages = sorted(p for p in (src / "docs").rglob("*.md")
                   if "resources" not in p.parts and not any(x.startswith("_") for x in p.parts))
    redirects = yaml.safe_load((src / "_data" / "pages_redirect_info.yml").read_text()) if (src / "_data" / "pages_redirect_info.yml").exists() else {}
    made, report = 0, []
    dirs_with_index = set()
    for p in pages:
        rel = p.relative_to(src)
        rendered = out / rel
        if not rendered.exists():
            report.append(f"not rendered: {rel}")
            continue
        fm = front_matter(p)
        if fm.get("redirect_to"):
            continue
        body = clean(rendered.read_text(encoding="utf-8", errors="replace"))
        for m in IMG_RE.findall(body):
            images.add(m)
        body = IMG_RE.sub(lambda m: re.sub(r"\.(png|jpe?g|PNG|JPG)$", ".webp", m.group(1)), body)
        tgt = target_path(rel)
        # a page "foo.md" next to a directory "foo/" becomes foo/_index.md
        if tgt.name != "_index.md" and (src / rel.with_suffix("")).is_dir():
            tgt = rel.with_suffix("") / "_index.md"
        url = "/" + str(rel.parent if rel.name == "index.md" else rel.with_suffix("")).strip("/") + "/"
        aliases = []
        info = (redirects or {}).get(url) or {}
        for src_list in (info.get("redirect_from"), fm.get("redirect_from")):
            if isinstance(src_list, str):
                src_list = [src_list]
            for a in src_list or []:
                if isinstance(a, str) and a.strip("/") and a.rstrip("/") + "/" != url:
                    aliases.append(a)
        title = fm.get("title") or rel.stem.replace("-", " ").capitalize()
        lines = ["+++", f"title = {toml_str(title)}"]
        if str(rel) == "docs/index.md":
            lines.append('template = "home.html"')
        if fm.get("description"):
            lines.append(f"description = {toml_str(fm['description'])}")
        if aliases:
            lines.append("aliases = [" + ", ".join(toml_str(a) for a in sorted(set(aliases))) + "]")
        lines += ["", "[extra]", 'status = "imported"', 'checked = ""', f"source = {toml_str(str(rel))}", "+++", ""]
        dst = content / tgt
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text("\n".join(lines) + body, encoding="utf-8")
        if tgt.name == "_index.md":
            dirs_with_index.add(dst.parent)
        made += 1
    (content / "_index.md").write_text('+++\ntitle = "SENTIENT Docs"\n+++\n', encoding="utf-8")
    # Every directory needs a section file for Zola's tree and the nav.
    for d in sorted({p.parent for p in content.rglob("*.md")}):
        cur = d
        while cur != content and cur.is_relative_to(content):
            idx = cur / "_index.md"
            if not idx.exists():
                idx.write_text("+++\n" f"title = {toml_str(cur.name.replace('-', ' ').capitalize())}\n"
                               "transparent = true\n+++\n", encoding="utf-8")
            cur = cur.parent
    dedupe_aliases(content)
    return made, report


def dedupe_aliases(content):
    """Drop aliases that point at a real page or that another page already claims."""
    urls, files = set(), sorted(content.rglob("*.md"))
    for f in files:
        rel = f.relative_to(content)
        u = "/" + str(rel.parent if rel.name == "_index.md" else rel.with_suffix("")).strip("/") + "/"
        urls.add(u.replace("//", "/"))
    seen = set()
    for f in files:
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^aliases = (\[.*\])$", text, re.M)
        if not m:
            continue
        keep = []
        for a in json.loads(m.group(1)):
            n = "/" + a.strip("/") + "/"
            if n in urls or n in seen:
                continue
            seen.add(n)
            keep.append(a)
        rep = ("aliases = " + json.dumps(keep, ensure_ascii=False)) if keep else ""
        f.write_text(text[:m.start()] + rep + text[m.end():], encoding="utf-8")


def convert_images(legacy_images_root, images, static):
    from concurrent.futures import ThreadPoolExecutor
    missing, sizes = [], []

    def one(img):
        srcp = legacy_images_root / img.lstrip("/").removeprefix("images/")
        if not srcp.exists():
            return img, None
        is_gif = srcp.suffix.lower() in (".gif", ".svg")
        dst = static / img.lstrip("/")
        if not is_gif:
            dst = dst.with_suffix(".webp")
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists():
            if is_gif:
                shutil.copy(srcp, dst)
            else:
                subprocess.run(["convert", str(srcp), "-strip", "-resize", "1600x1600>", "-quality", "82", str(dst)],
                               check=False, capture_output=True)
        return img, (srcp.stat().st_size, dst.stat().st_size if dst.exists() else 0)

    with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as ex:
        for img, sz in ex.map(one, sorted(images)):
            if sz is None:
                missing.append(img)
            else:
                sizes.append(sz)
    before = sum(a for a, _ in sizes)
    after = sum(b for _, b in sizes)
    return len(sizes), missing, before, after


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="78bb93d2")
    ap.add_argument("--work", default="/tmp/st-convert")
    ap.add_argument("--images", help="legacy images/ dir (default: export from --ref)")
    ap.add_argument("--skip-images", action="store_true")
    a = ap.parse_args()
    work = Path(a.work)
    src = export(a.ref, work)
    out = work / "out"
    jekyll(src, out)
    content = REPO / "content"
    for d in ("docs",):
        if (content / d).exists():
            shutil.rmtree(content / d)
    images = set()
    made, report = convert_pages(src, out, content, images)
    print(f"pages converted: {made}")
    for r in report:
        print("  " + r)
    # nav data
    data = REPO / "data" / "nav"
    data.mkdir(parents=True, exist_ok=True)
    for name, f in {"docs": "docs-home.yml", "edge": "edge/docs-home.yml",
                    "gateway": "gw/docs-home.yml", "mobile": "mobile/docs-home.yml"}.items():
        if (src / "_data" / f).exists():
            nav = (src / "_data" / f).read_text(encoding="utf-8").replace("title: Community Edition", "title: Introduction")
            (data / f"{name}.yml").write_text(nav, encoding="utf-8")
    if a.skip_images:
        return
    if a.images:
        legacy = Path(a.images)
    else:  # export the legacy images folder from the same commit
        tar = subprocess.run(["git", "-C", str(REPO), "archive", a.ref, "images"], check=True, capture_output=True).stdout
        subprocess.run(["tar", "-x", "-C", str(work)], input=tar, check=True)
        legacy = work / "images"
    done, missing, before, after = convert_images(legacy, images, REPO / "static")
    print(f"images: {done} converted, {len(missing)} missing, {before/1e6:.0f} MB -> {after/1e6:.0f} MB")
    (work / "missing-images.txt").write_text("\n".join(missing))


if __name__ == "__main__":
    main()
