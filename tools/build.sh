#!/usr/bin/env bash
# Copyright © 2016-2025 The SENTIENT Authors
# Build ONE docs version from this checkout.
#   tools/build.sh                       -> public/ served at the site root (latest)
#   tools/build.sh --prefix /v/4.3.0.57  -> public/ meant to be served under /v/4.3.0.57/
# Needs zola (0.19) and pagefind (1.3) on PATH, or ZOLA / PAGEFIND set.
set -euo pipefail
cd "$(dirname "$0")/.."
OUT=public PREFIX="" VERSION=""
while [ $# -gt 0 ]; do
  case "$1" in
    --out) OUT=$2; shift 2;;
    --prefix) PREFIX=${2%/}; shift 2;;
    --version) VERSION=$2; shift 2;;
    *) echo "unknown option $1" >&2; exit 2;;
  esac
done
ZOLA=${ZOLA:-zola} PAGEFIND=${PAGEFIND:-pagefind}
start=$(date +%s)
"$ZOLA" build --output-dir "$OUT" --force
if [ -n "$PREFIX" ]; then
  python3 tools/prefix.py "$OUT" "$PREFIX"
fi
"$PAGEFIND" --site "$OUT" --output-subdir pagefind --quiet
[ -f versions.json ] && cp versions.json "$OUT/versions.json"
echo "built $(find "$OUT" -name index.html | wc -l) pages, $(du -sh "$OUT" | cut -f1) in $(( $(date +%s) - start ))s -> $OUT${PREFIX:+ (prefix $PREFIX)}"
