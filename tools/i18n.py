#!/usr/bin/env python3
# Copyright © 2016-2026 The SENTIENT Authors
"""Prepare a build copy of the site with every page present in every language.

English is the source. A translation is content/**/name.<lang>.md next to
name.md. For each language in config.toml [languages]:
  - a translated page gets its /docs/ page links (not file links) and its
    aliases (old URLs that redirect) pointed at the same language;
  - a page with no translation yet is copied from English with
    extra.fallback = true, so the page exists under /<lang>/ and shows a
    "not translated yet" note instead of a dead link.
The repository is not changed; everything goes into the build directory.

Usage: tools/i18n.py <build dir>
"""
import os, re, shutil, sys, tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = Path(sys.argv[1]).resolve()
LANGS = sorted(tomllib.loads((ROOT / "config.toml").read_text(encoding="utf-8")).get("languages", {}))
TRANSLATED = re.compile(r"\.(%s)\.md$" % "|".join(map(re.escape, LANGS))) if LANGS else None
FRONT = re.compile(r"\A\+\+\+\n(.*?)\n\+\+\+\n?", re.S)
ALIASES = re.compile(r"^(aliases\s*=\s*\[)(.*?)(\]\s*)$", re.S | re.M)
# a page link: /docs/... whose last part has no file extension (images, JSON samples stay shared)
LINKS = re.compile(r'(\]\(|href=")/docs/([^)"\s#?]*)')


def link(m, lang):
    last = m.group(2).rstrip("/").rsplit("/", 1)[-1]
    if "." in last:
        return m.group(0)
    return f"{m.group(1)}/{lang}/docs/{m.group(2)}"


def localise(text, lang, fallback):
    m = FRONT.match(text)
    if not m:
        return text
    front, body = m.group(1), text[m.end():]
    front = ALIASES.sub(lambda a: a.group(1) + re.sub(r'"([^"]*)"', lambda q: f'"/{lang}/{q.group(1).lstrip("/")}"', a.group(2)) + a.group(3), front)
    if fallback:
        if re.search(r"^\[extra\]\s*$", front, re.M):
            front = re.sub(r"^\[extra\]\s*$", "[extra]\nfallback = true", front, count=1, flags=re.M)
        else:
            front = front.rstrip("\n") + "\n\n[extra]\nfallback = true"
    body = LINKS.sub(lambda x: link(x, lang), body)
    return f"+++\n{front}\n+++\n{body}"


if BUILD == ROOT or ROOT in BUILD.parents and BUILD.name in ("content", "static", "templates"):
    sys.exit("refusing to build into the source tree")
shutil.rmtree(BUILD, ignore_errors=True)
BUILD.mkdir(parents=True)
for name in ("config.toml",):
    shutil.copy2(ROOT / name, BUILD / name)
for name in ("templates", "data", "content"):
    shutil.copytree(ROOT / name, BUILD / name)
os.symlink(ROOT / "static", BUILD / "static")

made = {l: 0 for l in LANGS}
done = {l: 0 for l in LANGS}
for src in sorted((BUILD / "content").rglob("*.md")):
    if TRANSLATED and TRANSLATED.search(src.name):
        continue
    english = src.read_text(encoding="utf-8")
    for lang in LANGS:
        dst = src.with_name(f"{src.stem}.{lang}.md")
        if dst.exists():
            dst.write_text(localise(dst.read_text(encoding="utf-8"), lang, False), encoding="utf-8")
            done[lang] += 1
        else:
            dst.write_text(localise(english, lang, True), encoding="utf-8")
            made[lang] += 1
for lang in LANGS:
    print(f"{lang}: {done[lang]} translated, {made[lang]} shown in English until translated")
