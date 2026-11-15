+++
title = "Environment settings"
description = "Settings you can change with environment variables, with their defaults."
weight = 17

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT reads its server settings from environment variables. With Docker, they are set in the `environment:` section of the `sentient` service in your compose file. After a change, run `docker compose -f <file> up -d` to recreate the container.

Settings you change in the web UI, such as mail, security, translations and tenant profiles, are stored in the database and are not listed here.

## Identity

| Variable | Example | Meaning |
|---|---|---|
| `SENTIENT_INSTANCE_ID` | `sentient-docker-01` | Name of this installation. |
| `SENTIENT_SERVICE_ID` | `st-node-1` | Name of this server node. **Give every machine its own value.** Two nodes with the same ID are treated as one. |

## Database

| Variable | Default in compose | Meaning |
|---|---|---|
| `DATABASE_URL` | `postgresql://sentient:sentient@postgres:5432/sentient` | PostgreSQL connection. |
| `TS_TYPE` | `sql`, `timescale` or `clickhouse`, depending on the file | Where telemetry history is stored. Chosen at installation. Don't change it on an existing system without a migration. |
| `TS_LATEST_TYPE` | as above | Where latest values are stored. |
| `CLICKHOUSE_URL` | `http://clickhouse:8123` | ClickHouse address. If this is set during installation, SENTIENT installs the ClickHouse schema too. |
| `CLICKHOUSE_DATABASE`, `CLICKHOUSE_USER`, `CLICKHOUSE_PASSWORD` | `sentient` | ClickHouse login. |
| `DB_POOL_PRIMARY_MIN` / `DB_POOL_PRIMARY_MAX` | 16 / 48 | Connections for the main pool. |
| `DATABASE_POOL_MIN` / `DATABASE_POOL_MAX` | 8 / 24 | Connections for the second pool. |

The two pools together must stay below PostgreSQL's `max_connections`, which is 100 in the compose files.

## Server

| Variable | Default | Meaning |
|---|---|---|
| `HOST` / `PORT` | `0.0.0.0` / `8080` | Address and port for the web UI and API inside the container. |
| `RUST_LOG` | `info,sentient_api=info` | Log detail. Use `debug` only for a short time, because it writes a lot. |
| `LICENSE_SERVER_URL` | `https://license.invenia.in` | Licence server used for activation and the heartbeat. |
| `SECRETS_KEY_FILE` | `/var/lib/sentient/secrets.key` | Master key for stored secrets. It is created on first start. **Back it up with the database.** |
| `REPORT_OUTPUT_DIR` | `/var/lib/sentient/reports` | Where generated reports are kept. |
| `VC_REPOS_PATH` | `/var/lib/sentient/vc-repos` | Local repositories for version control. |
| `ANALYTICS_ENABLED` | `false` (`true` in the compose files) | Turns the analytics pipelines on or off. |
| `SENTIENT_TRANSLATE_URL` | `http://translate:5100` | Address of the optional offline translator. |
| `DASHBOARD_KEEP_ALIVE_MAX` | `10` | The most dashboards a user may keep loaded in the background. 0 means no limit. |

## Writing telemetry

SENTIENT collects writes into batches before it saves them. The defaults suit most plants.

| Variable | Default | Meaning |
|---|---|---|
| `SQL_TS_BATCH_SIZE` / `SQL_TS_BATCH_MAX_DELAY_MS` | 8000 / 100 | Time series: the most rows per batch, and how long to wait for a batch to fill. |
| `SQL_TS_LATEST_BATCH_SIZE` / `…_MAX_DELAY_MS` | 4000 / 50 | Latest values. |
| `SQL_ATTRIBUTES_BATCH_SIZE` / `…_MAX_DELAY_MS` | 4000 / 50 | Attributes. |
| `SQL_*_BATCH_THREADS` | 5 | Parallel writers for each kind. |

## Retention

| Variable | Default | Meaning |
|---|---|---|
| `AUDIT_LOG_TTL_DAYS` | 0 | Delete audit log entries after this many days. 0 keeps them forever. |
| `NOTIFICATIONS_TTL_DAYS` | 0 | The same, for notifications. |
| `SENTIENT__EVENT_CLEANUP__DEBUG_EVENTS_TTL_SECS` | 604800 (7 days) | How long rule node debug events are kept. |
| `SENTIENT__EVENT_CLEANUP__EVENTS_TTL_SECS` | 0 | How long other events are kept. 0 keeps them forever. |

Telemetry retention is set for each tenant in its tenant profile, not here.

## CoAP over DTLS

CoAP over DTLS starts only when it is turned on in the connectivity settings **and** both of these point at readable files:

| Variable | Example |
|---|---|
| `COAP_SSL_PEM_CERT` | `/etc/sentient/certs/coap-server.crt` |
| `COAP_SSL_PEM_KEY` | `/etc/sentient/certs/coap-server-pkcs8.key` |
