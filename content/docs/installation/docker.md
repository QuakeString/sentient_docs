+++
title = "Install with Docker"
description = "Run SENTIENT with Docker Compose on PostgreSQL, TimescaleDB or ClickHouse."
weight = 10

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT runs as one container next to its database. You pick the database once, at installation time. Moving to another one later needs a migration.

| Compose file | Database | Choose it when |
|---|---|---|
| `docker-compose.yml` | PostgreSQL | Small and medium plants. This is the simplest option. |
| `docker-compose.timescaledb.yml` | PostgreSQL with TimescaleDB | You keep months of history and want compressed time series in PostgreSQL. |
| `docker-compose.clickhouse.yml` | PostgreSQL plus ClickHouse | You have high telemetry volume or long history. Telemetry history goes to ClickHouse and everything else stays in PostgreSQL. |

Each file is complete on its own. Don't combine them.

## Before you start

- Docker Engine 24 or later with the Compose plugin (`docker compose version` works).
- The ports in [Ports and firewall](/docs/operations/ports/) are free on the host. Port 8080 is the one you need first.
- A SENTIENT licence key, or internet access to request a demo licence from the licence page.
- On Windows, use [Platform Manager](/docs/installation/windows/) instead. It sets up WSL2 and pins the hardware identity that the licence needs.

## Install

Run these commands in the folder that holds the compose file. The example uses the ClickHouse flavour; replace the file name for the others.

```bash
F=docker-compose.clickhouse.yml
docker compose -f $F pull
docker compose -f $F up -d postgres clickhouse        # databases first (no clickhouse for the other files)
docker compose -f $F run --rm -e INSTALL_SENTIENT=true sentient
docker compose -f $F up -d
```

The installer creates the schema and the system administrator, then prints `INSTALLATION COMPLETE`. If you start the server without installing first, it stops and prints this message:

```
✗ Nothing to upgrade: this database is EMPTY — SENTIENT is not installed.
```

In that case, run the `INSTALL_SENTIENT=true` command above and start again.

<div class="st-callout info">

To try SENTIENT with sample data, add `-e LOAD_DEMO=true` to the install command. This creates a demo tenant (`tenant@sentient.local`, also with password `admin123`) with sample devices, a rule chain and a dashboard. Leave it out on a production system.

</div>

## Open SENTIENT and activate the licence

1. Open `http://<server>:8080` in a browser.
2. Sign in as the system administrator: `admin@sentient.local` with the default password `admin123`. Change this password right away on your profile's **Security** page. Every SENTIENT installation starts with the same default.
3. Open **License** in the menu and activate your key. See [Activate your licence](/docs/installation/licence/).

Until a licence is active, every request except sign-in and the licence page is refused with error code 50 (*No active license*).

## Where the data lives

Docker volumes keep all data. They have the same names whichever file you use:

| Volume | Holds |
|---|---|
| `st-pg-data` | PostgreSQL: devices, dashboards, users, latest values, and time series unless you use ClickHouse |
| `st-ch-data` | ClickHouse telemetry history (ClickHouse flavour only) |
| `st-data` | `/var/lib/sentient`: the secrets key, generated reports, version control repositories |

<div class="st-callout warn">

`st-data` holds `secrets.key`, the master key for every stored password and API key. Back it up together with the database. A database restored without its key cannot read its secrets. See [Back up and restore](/docs/operations/backup-restore/).

</div>

## Linux hosts: keep the licence bound

The licence is bound to a hardware fingerprint made of six signals. On a Linux host, add the host's machine ID to the `sentient` service so the fingerprint survives a container rebuild:

```yaml
    volumes:
      - st-data:/var/lib/sentient
      - /etc/machine-id:/etc/machine-id:ro   # Linux hosts only
```

Don't add this line on Windows or macOS. There the path belongs to Docker's own virtual machine and changes when Docker is reset.

## Everyday commands

```bash
docker compose -f $F ps                  # what is running
docker compose -f $F logs -f sentient    # follow the server log
docker compose -f $F stop                # stop everything
docker compose -f $F up -d               # start again
```

## Pin a release

The files use `quakestring/sentient:latest`. On a plant system, pin the release you tested so that a `pull` never upgrades by surprise:

```yaml
  sentient:
    image: "quakestring/sentient:4.3.0.57"
```

To upgrade, see [Upgrade and roll back](/docs/operations/upgrade/).

## Optional: offline translator

The files include a `translate` service, which is off by default. It translates the user interface without internet access. Start it with:

```bash
docker compose -f $F --profile translate up -d
```

Then install language packs and add the *SENTIENT offline translator* engine under **Settings › Translations**. See [Translations](/docs/administration/translations/).

## If something goes wrong

- The server restarts in a loop: run `docker compose -f $F logs sentient`. The most common cause is the not-installed message shown above.
- Port 8080 is already in use: change the left-hand side of `"8080:8080"`, for example `"8090:8080"`.
- More fixes: [Installation and upgrade errors](/docs/troubleshooting/install-errors/).
