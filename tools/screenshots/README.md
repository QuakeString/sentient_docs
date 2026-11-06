# Documentation screenshots

Every screenshot in the manual is taken from a running SENTIENT by
`shoot.mjs`, as listed in `manifest.yml`. Nothing is drawn or edited by hand,
so a new release only needs a new run.

```bash
export ST_DOCS_URL=http://localhost:8080
export ST_DOCS_SYSADMIN='admin@sentient.local:<password>'   # never commit this
tools/screenshots/run.sh                  # seed the Demo Plant tenant, then shoot everything
tools/screenshots/run.sh --no-seed --only devices-list,alarms-list
```

- `seed.py` creates the **Demo Plant** tenant (user `docs@demo.plant`): seven
  plant devices, an asset tree, 24 hours of telemetry, attributes and three
  alarms. It needs a licensed SENTIENT (an unlicensed one answers 402,
  error code 50). Run it on a test instance, not on a customer system.
- `shoot.mjs` signs in through the real login form, uses a fixed window
  (1440 x 900), time zone (Asia/Kolkata) and locale, switches off animations,
  closes the licence notice, and writes WebP files to `static/images/st/`
  (`<id>.webp`, `<id>-dark.webp` for dark mode). `report.json` lists what
  was taken or failed; the run fails when any shot fails.
- In a page: `![Devices list](/images/st/devices-list.webp)`.
- Hide secrets with `mask:` (access tokens, keys, IP addresses).
