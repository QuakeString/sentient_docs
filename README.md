# SENTIENT documentation

The SENTIENT manual, built with [Zola](https://www.getzola.org/) and searched
offline with [Pagefind](https://pagefind.app/). It builds in seconds, needs no
Ruby or Node, and the output is plain static files.

## Layout

| Path | What it holds |
|---|---|
| `content/docs/` | The pages (Markdown with TOML front matter). The URL follows the path: `content/docs/user-guide/ui/devices.md` is `/docs/user-guide/ui/devices/`. |
| `data/nav/*.yml` | Left-hand navigation for each area (platform, gateway, edge, mobile). |
| `data/home.yml` | Text and tiles of the docs home page. |
| `templates/` | Page layout (Tera templates). |
| `static/` | CSS (SENTIENT design-system tokens), JS, fonts, images. |
| `tools/` | Build, version, check and one-time conversion scripts. |
| `versions.json` | Every docs version and the SENTIENT releases it covers. |

## Build and preview

```bash
# zola 0.19.x and pagefind 1.3.x on PATH
tools/build.sh --out public          # one version, ~15 s
python3 -m http.server -d public 8090   # open http://localhost:8090/docs/
python3 tools/check.py public        # broken links, missing images, old names
```

Or as an offline Docker image:

```bash
docker build -t quakestring/sentient-docs:4.3.0.57 .
docker run -d -p 8090:80 quakestring/sentient-docs:4.3.0.57
```

## Writing a page

```toml
+++
title = "Connect a Modbus PLC"
description = "Read registers from a PLC and show them as telemetry."

[extra]
status = "checked"          # "imported" = carried over, not yet checked; "planned" = outline only
checked = "4.3.0.57"        # SENTIENT version the page was verified against
changed_in = "4.3.0.57"     # optional: shows a "Changed in" badge
+++
```

- A new sidebar entry goes in `data/nav/*.yml`; add `planned: true` while the
  page is only an outline (shown as SOON, left out of search). `tools/check.py`
  fails when a sidebar entry does not open a page.
- Write from the current SENTIENT UI and code, never from the old text alone.
- Use UI labels exactly as SENTIENT shows them.
- Screenshots come from our own instance: add them to `tools/screenshots/manifest.yml`, never by hand.
- Callouts: `<div class="st-callout info">` or `warn`, with a blank line before
  and after the Markdown inside. Tabs: `<div class="st-tabs">` holding
  `<div class="st-tab" data-label="Windows">` blocks. Image galleries:
  `<div class="st-gallery">` with `<figure>` elements.

## Languages

English is the source; Hindi (`hi`) and Vietnamese (`vi`) are served under
`/hi/docs/` and `/vi/docs/`. The language menu sits next to the version menu.

- A translation is a file next to the English one: `devices.md`,
  `devices.hi.md`, `devices.vi.md`. Write links as `/docs/...` as in English;
  the build points them at the same language.
- A page with no translation yet still exists in every language: `tools/i18n.py`
  copies the English text with a "not translated yet" note, in a build copy, and
  leaves it out of that language's search. Nothing generated is committed.
- Interface labels are in `config.toml` (`[translations]` and
  `[languages.<code>.translations]`). The home page reads `data/home.<code>.yml`
  and the sidebar `data/nav/<area>.<code>.yml` when they exist, else English.
- Fonts for Vietnamese (Roboto) and Hindi (Noto Sans Devanagari) are bundled,
  so every language works offline.

## Versions

- `master` is the newest docs version (`versions.json` → `latest`).
- When a SENTIENT release changes the docs, the previous state is kept on a
  branch `v<version>` (for example `v4.3.0.57`) and added to `versions.json`.
  A release without doc changes is added to the `releases` list of the
  version it shares.
- `tools/build-all.sh site` builds the online site: the latest version at the
  root and every version under `/v/<version>/`. Images live once in `/images/`
  and are shared by all versions, so a changed screenshot gets a new file name.
- The offline image and help pack carry one version only.

## History

The site began as a Jekyll site. `tools/convert/` holds
the one-time conversion (run against commit `78bb93d2`). Pages that still need
review carry `status = "imported"` and show a note at the top.

The content audit (`tools/audit.py` → `audit/pages.csv`, `audit/SUMMARY.md`)
gives every page a verdict and the wave that rewrites it. Pages that did not
apply to SENTIENT were removed with `tools/convert/prune.py` (list in
`audit/deleted.txt`); their old URLs redirect to the nearest SENTIENT page, and
every help link in the SENTIENT UI (`audit/ui-help-links.txt`) opens a page.
