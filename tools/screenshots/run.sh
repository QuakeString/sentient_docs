#!/usr/bin/env bash
# Copyright © 2016-2025 The SENTIENT Authors
# Seed the Demo Plant tenant and take every screenshot in manifest.yml.
#   ST_DOCS_URL=http://localhost:8080 ST_DOCS_SYSADMIN='admin@sentient.local:...' tools/screenshots/run.sh [--only id,...] [--no-seed]
set -euo pipefail
cd "$(dirname "$0")"
[ -d node_modules ] || { npm install --no-audit --no-fund; npx playwright install chromium; }
if [[ " $* " != *" --no-seed "* ]]; then
  python3 seed.py --url "${ST_DOCS_URL:-http://localhost:8080}"
fi
args=(); for a in "$@"; do [ "$a" = "--no-seed" ] || args+=("$a"); done
node shoot.mjs "${args[@]}"
