+++
title = "Back up and restore"
description = "Back up the database, the telemetry history and the secrets key, and restore them on the same or a new server."
weight = 14

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A complete SENTIENT backup has three parts. A backup that misses one of them cannot be fully restored.

| Part | Holds |
|---|---|
| **PostgreSQL database** | Devices, assets, dashboards, rule chains, users, alarms, latest values, and the time series history unless you use ClickHouse |
| **ClickHouse database** (ClickHouse installs only) | Telemetry history |
| **Data folder** `/var/lib/sentient` | `secrets.key`, generated reports, version control repositories |

<div class="st-callout warn">

**Always back up `secrets.key` with the database.** Every password and API key that SENTIENT stores is encrypted with it, including mail server, integration and AI model credentials. A database restored without its key can't read them, and you must enter them all again.

</div>

## With Platform Manager (Windows and Linux)

Open the Platform Manager and go to **Backup and restore**. A backup is one file with the database, the telemetry and the file stores, and a checksum for every part.

**Back up**

1. Enter the **Database password**, and also the **ClickHouse password** if you use ClickHouse.
2. Choose how much **Telemetry history** to include: **All**, **Last days** or **None**. Less history makes a much smaller file, which is useful before an update.
3. Optional: **encrypt the backup** with a password. Keep the password somewhere safe, because the backup cannot be opened without it.
4. Click **Back up**. When it finishes, the screen shows the file, its size and its checksum.

**Restore**

1. Click **Choose backup…** and pick the file. Enter its password if it is encrypted.
2. Give a **New database name**. The backup is restored next to the data SENTIENT uses now, so nothing is overwritten yet. You can restore into another database type, for example a PostgreSQL backup into a ClickHouse installation.
3. Check the restored data, then click **Put the restored data into service**.

Copy backup files to another machine or storage. A backup on the same disk does not protect you from a disk failure.

## With Docker

Run these commands from the folder with your compose file (`F` is your compose file).

**Back up**

```bash
F=docker-compose.yml
STAMP=$(date +%Y%m%d-%H%M)
# 1. PostgreSQL (consistent while running)
docker compose -f $F exec -T postgres pg_dump -U sentient -Fc sentient > sentient-$STAMP.dump
# 2. Data folder with secrets.key
docker run --rm -v st-data:/data -v "$PWD":/out alpine tar czf /out/st-data-$STAMP.tgz -C /data .
```

On a ClickHouse installation, also back up ClickHouse. `pg_dump` does not include the telemetry history there. Stop the stack and copy the volume:

```bash
docker compose -f $F stop
docker run --rm -v st-ch-data:/data -v "$PWD":/out alpine tar czf /out/st-ch-data-$STAMP.tgz -C /data .
docker compose -f $F up -d
```

**Restore** into a fresh installation of the **same SENTIENT version**:

```bash
docker compose -f $F up -d postgres
docker compose -f $F exec -T postgres pg_restore -U sentient -d sentient --clean --if-exists < sentient-<stamp>.dump
docker run --rm -v st-data:/data -v "$PWD":/in alpine sh -c "cd /data && tar xzf /in/st-data-<stamp>.tgz"
docker compose -f $F up -d
```

Restore the ClickHouse volume the same way, with the stack stopped.

## How often

- Back up before every update, and before larger changes such as importing many devices.
- Back up on a schedule, for example every night, and keep several generations.
- Test a restore on a spare machine now and then. Only a backup you have restored is a backup you can trust.

## Related

- [Upgrade and roll back](/docs/operations/upgrade/)
- [Move to a new server](/docs/operations/move-server/)
