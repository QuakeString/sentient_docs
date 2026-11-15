#!/usr/bin/env bash
# Copyright © 2016-2025 The SENTIENT Authors
# Build the online site with EVERY docs version listed in versions.json.
#   site/            latest version at the root (/docs/...)
#   site/v/<ver>/    each version, including the latest, under a stable prefix
#   site/images/     screenshots shared by all versions (new screenshots get new names)
# Each version lives on branch "v<version>"; the latest is this checkout.
set -euo pipefail
cd "$(dirname "$0")/.."
SITE=${1:-site}
rm -rf "$SITE"; mkdir -p "$SITE"
latest=$(python3 -c 'import json;print(json.load(open("versions.json"))["latest"])')
tools/build.sh --out "$SITE"
work=$(mktemp -d)
for v in $(python3 -c 'import json;[print(x["version"]) for x in json.load(open("versions.json"))["versions"]]'); do
  if [ "$v" = "$latest" ]; then src=.; else
    git worktree add -f "$work/$v" "v$v" >/dev/null 2>&1 || { echo "skip $v: no branch v$v"; continue; }
    src="$work/$v"
  fi
  (cd "$src" && tools/build.sh --out "$OLDPWD/$work/out-$v" --prefix "/v/$v") || true
  if [ -d "$work/out-$v" ]; then
    # merge images into the shared folder without overwriting existing files
    if [ -d "$work/out-$v/images" ]; then cp -rn "$work/out-$v/images/." "$SITE/images/"; rm -rf "$work/out-$v/images"; fi
    mkdir -p "$SITE/v"; mv "$work/out-$v" "$SITE/v/$v"
  fi
  [ "$src" != . ] && git worktree remove --force "$src"
done
cp versions.json "$SITE/versions.json"
rm -rf "$work"
echo "site ready in $SITE ($(du -sh "$SITE" | cut -f1))"
