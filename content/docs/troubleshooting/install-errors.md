+++
title = "Installation and upgrade errors"
description = "Problems during installation or upgrade, what causes them and how to solve them."
weight = 186

[extra]
status = "checked"
checked = "4.3.0.57"
+++
## SENTIENT is not installed (Docker)

Error ID: [ST-INS-003](/docs/troubleshooting/errors/st-ins-003/)

```
✗ Nothing to upgrade: this database is EMPTY — SENTIENT is not installed.
```

The server started on an empty database, and the container keeps restarting.

**Fix:** run the installer once, then start again:

```bash
docker compose -f <compose file> run --rm -e INSTALL_SENTIENT=true sentient
docker compose -f <compose file> up -d
```

If you did run the installer, it stopped before it created the schema. Scroll up in that run's output for the first error. With ClickHouse, the installer sets up ClickHouse first, so a ClickHouse problem stops it early.

## PostgreSQL does not initialise (Windows)

Error ID: [ST-INS-002](/docs/troubleshooting/errors/st-ins-002/)

Platform Manager stops while it creates the PostgreSQL database, and `initdb` crashes.

**Cause:** PostgreSQL 18 needs Visual C++ runtime 14.44 or newer, and the computer has an older one.

**Fix:** Setup 0.8.0-rc9 and later install the runtime themselves. With an older Setup, run `vc_redist.x64.exe` from the SENTIENT release page, then click **Retry**.

## Port already in use

Error ID: [ST-INS-001](/docs/troubleshooting/errors/st-ins-001/)

```
Already in use: 8080. Choose another port, or stop what is listening on it.
```

Another program, or an earlier SENTIENT, already listens on that port.

**Fix:** in the Platform Manager wizard, choose another port on the **Network ports** page. With Docker, change the left-hand number of the port mapping, for example `"8090:8080"`. To see what holds the port, run `netstat -ano | findstr :8080` on Windows or `ss -tlnp | grep 8080` on Linux.

## PostgreSQL stays on 5432 although you chose another port (Windows)

This happened with Setup up to 0.8.0-rc5: the chosen port was not written to `postgresql.conf`. **Fix:** use Setup 0.8.0-rc6 or later.

## ClickHouse: connection refused although PostgreSQL is running

Error ID: [ST-DB-004](/docs/troubleshooting/errors/st-db-004/)

During `--backfill-clickhouse` or a hybrid install, you get *connection refused* for PostgreSQL even though PostgreSQL is up.

**Cause:** ClickHouse opens that connection itself. A `DATABASE_URL` with `localhost` then points at ClickHouse's own container, not at PostgreSQL.

**Fix:** use the address that ClickHouse can reach. Inside Docker Compose, that is the service name: `postgres:5432`.

## ClickHouse reports healthy but every client gets "connection reset"

Error ID: [ST-DB-004](/docs/troubleshooting/errors/st-db-004/)

**Cause:** a custom ClickHouse configuration was mounted as the whole `config.d` folder. That hides the file that makes ClickHouse listen on the network, so it listens only inside its own container.

**Fix:** mount your settings as a single file inside `config.d`, as the SENTIENT compose files do, and never as the whole folder.

## The upgrade stopped halfway

Error ID: [ST-INS-006](/docs/troubleshooting/errors/st-ins-006/)

- **Platform Manager:** it has already put the previous version and database copy back. Open **Logs** to see which step failed, then send the log to support.
- **Docker:** the log shows the step that failed (`docker compose -f <file> logs sentient`). Go back to the previous image tag and restore the backup you made before the upgrade. See [Upgrade and roll back](/docs/operations/upgrade/).

## Not enough disk space

Error ID: [ST-INS-005](/docs/troubleshooting/errors/st-ins-005/)

Platform Manager's **System check** reports **Disk space** as a blocker, or the database stops with *No space left on device*.

**Fix:** free space or add a disk before you continue. Common space users on a running system:

- update copies and old history kept after a database change: remove them under **Kept after earlier changes** in the Platform Manager
- ClickHouse's own system logs on older installations: see [ClickHouse's own logs](/docs/operations/tuning/#clickhouse-s-own-logs)
- old Docker images: `docker image prune`

## The licence is refused after installation

See [Licence errors](/docs/troubleshooting/licence-errors/).
