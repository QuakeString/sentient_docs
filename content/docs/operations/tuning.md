+++
title = "Performance tuning"
description = "Tell when the server is overloaded, and size the database, connection pools, write batching and retention for your load."
weight = 19

[extra]
status = "checked"
checked = "4.3.0.57"
+++
The default settings suit a single plant on a modest server. Change them only when you see one of the signs below, one setting at a time, and compare before and after. The settings themselves are listed in [Environment settings](/docs/operations/settings/).

## Signs that the server is overloaded

| Sign | Where to look | Usual cause |
|---|---|---|
| Messages queue up or arrive late | **API usage > View statistics**: **Queue Stats** shows successful, failed and timed-out messages per queue; **Processing Failures and Timeouts** shows timeouts | Rule chains doing slow work (external calls, heavy scripts) on every message, or too little CPU |
| `Pool timed out` in the server log | The server log (`docker logs sentient`, or **Logs** in Platform Manager) | All database connections busy: the database is too slow for the write rate, or the pool is too small |
| `too many clients already` in the log | The server and PostgreSQL logs | The pools together ask for more connections than PostgreSQL's `max_connections` |
| Dashboards slow to open, charts slow over long ranges | The browser | Long history read from PostgreSQL. Consider ClickHouse, below |
| The database disk keeps growing | Disk use, **API usage > Data points storage days** | Retention too long for the write rate |

Check CPU and memory of the server and of the database at the same time. When the database is at 100 % and SENTIENT is not, tune the database; when SENTIENT is at 100 %, look at rule chains and scripts first.

## Database connections

SENTIENT keeps two connection pools to PostgreSQL:

| Setting | Default | Used for |
|---|---|---|
| `DB_POOL_PRIMARY_MIN` / `DB_POOL_PRIMARY_MAX` | 16 / 48 | Telemetry writes and most requests |
| `DATABASE_POOL_MIN` / `DATABASE_POOL_MAX` | 8 / 24 | Other work |

Both maxima together (72) must stay below PostgreSQL's `max_connections` (100 in the compose files, 200 in a Platform Manager installation), with room for backups and your own tools. If you raise a pool, raise `max_connections` too.

More connections do not make a slow database faster. If the pool times out while PostgreSQL is already at full CPU or disk, give the database more resources or move history to ClickHouse instead.

## PostgreSQL memory

**Platform Manager** sizes PostgreSQL for the computer during setup, on the **Configuration** step (**Recommended**): with 2 GB of memory or more it sets `shared_buffers` to a quarter of the memory, `effective_cache_size` to three quarters, `work_mem` to 16 MB and `max_connections` to 200. Change them later on **Settings** in Platform Manager, for example after adding memory.

The **Docker Compose** files start PostgreSQL with small settings so that it fits next to SENTIENT on a small machine: `max_connections=100`, `shared_buffers=128MB`, `work_mem=2MB`, `effective_cache_size=384MB`. On a server with more memory, raise them in the `command:` of the `postgres` service and restart the stack:

| Setting | Starting point |
|---|---|
| `shared_buffers` | About 25 % of the memory you give PostgreSQL |
| `effective_cache_size` | About 75 % of that memory |
| `work_mem` | 4 to 16 MB. It is used per sort, per connection, so keep it modest |

## Write batching

SENTIENT writes telemetry, latest values and attributes in batches. Each kind has a batch size, a delay and a number of writer threads (`SQL_TS_BATCH_SIZE`, `SQL_TS_BATCH_MAX_DELAY_MS`, `SQL_TS_BATCH_THREADS` and the same for `SQL_TS_LATEST_…` and `SQL_ATTRIBUTES_…`).

- A larger batch writes more rows per database round trip, so the database does less work per value, at the cost of a little delay.
- A longer delay lets batches fill at low rates. Values reach the database, and charts reading history, that much later; live widgets are not delayed.
- More threads help only when the database has spare CPU and disk.

The defaults handle well over 100,000 values per second on suitable hardware. Leave them unless the queue statistics or pool timeouts point at writes.

## Retention

Telemetry is kept for the **Storage TTL** days in each [tenant profile](/docs/user-guide/tenant-profiles/); 0 keeps it forever. Shorter retention keeps the database smaller and faster.

Audit logs, notifications and rule engine events have their own retention in [Environment settings](/docs/operations/settings/#retention). Debug events grow fastest: switch debug mode off on rule nodes when you are done.

## When to move to ClickHouse

Move history to ClickHouse when:

- you store tens of thousands of values per second or more,
- you keep history for years, or
- charts over weeks or months are slow.

With ClickHouse, history and latest values are stored in ClickHouse, and latest values are served from a memory cache in SENTIENT (`TS_LATEST_CACHE=inprocess`, up to `TS_LATEST_CACHE_MAX_ENTRIES` keys, 1,000,000 by default). PostgreSQL then keeps only devices, dashboards, alarms and other configuration, and its load stops growing with the number of values. In our measurements, PostgreSQL's CPU at 200,000 values per second fell from about 60 % of a core to about 2 %.

The latest-value cache works only with ClickHouse history. SENTIENT refuses to start with `TS_LATEST_CACHE` set on a PostgreSQL-only installation.

Moving an existing installation to ClickHouse needs a data migration: use **Migration** in Platform Manager. See [System requirements](/docs/installation/requirements/#disk) to choose a database for a new installation.

## ClickHouse's own logs

ClickHouse writes logs about itself into its `system` database all the time, even when idle. On a plant server these logs can outgrow the telemetry: one installation had 1.4 GB of logs next to 0.6 GB of data. SENTIENT's ClickHouse settings, in the compose file and in Platform Manager installations, therefore switch most of them off and keep only `query_log` and `part_log` for 7 days and `error_log` for 30 days. They also limit ClickHouse's caches to suit an 8 GB machine.

Installations set up before these settings may still hold the old log tables. The settings stop new rows but leave the old ones. To free the space, empty the tables that are switched off, for example:

```bash
docker exec sentient-clickhouse clickhouse-client -q "TRUNCATE TABLE IF EXISTS system.metric_log"
docker exec sentient-clickhouse clickhouse-client -q "TRUNCATE TABLE IF EXISTS system.asynchronous_metric_log"
docker exec sentient-clickhouse clickhouse-client -q "TRUNCATE TABLE IF EXISTS system.trace_log"
docker exec sentient-clickhouse clickhouse-client -q "TRUNCATE TABLE IF EXISTS system.text_log"
```

To see which tables use the space:

```bash
docker exec sentient-clickhouse clickhouse-client -q "SELECT database, table, formatReadableSize(sum(bytes_on_disk)) AS size FROM system.parts WHERE active GROUP BY database, table ORDER BY sum(bytes_on_disk) DESC LIMIT 10"
```

## Rule chains and scripts

The rule engine often costs more than storage. On every message:

- Keep the device profile's rule chain short, and filter early so that most messages skip the expensive nodes.
- Prefer built-in nodes over scripts where one does the job.
- Call external systems (REST, email, AI) only for the messages that need it, not for every telemetry message.
- Switch off debug mode on nodes when you have finished.

## Related

- [Environment settings](/docs/operations/settings/)
- [System requirements](/docs/installation/requirements/)
- [API usage and limits](/docs/administration/api-usage/)
