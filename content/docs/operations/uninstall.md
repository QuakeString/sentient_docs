+++
title = "Uninstall"
description = "Remove SENTIENT cleanly, with or without its data."
weight = 20

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Before you uninstall, decide whether you still need the data. If you might, make a [backup](/docs/operations/backup-restore/) and copy it to another machine first. If the licence should move to another machine, **Deactivate** it on the **License** page first. See [Move to a new server](/docs/operations/move-server/).

## With Platform Manager

Run Setup again, or use **Uninstall** in Windows **Apps & features**, then choose one of these:

- **Uninstall:** removes SENTIENT and the Platform Manager. **The database is kept**, and a new installation can use it again.
- **Uninstall and delete the data:** removes SENTIENT, the Platform Manager, PostgreSQL and every database. This can't be undone.

If a step gets stuck, the uninstaller gives up on it after a while (services after 1 minute, the ClickHouse WSL distribution after 3 minutes) and says what was left behind.

## With Docker

```bash
docker compose -f $F down        # stop and remove the containers, keep the data
```

The volumes `st-pg-data`, `st-ch-data` and `st-data` stay, so a later `up -d` starts again with all data. To delete the data as well, run:

```bash
docker compose -f $F down -v     # also deletes the volumes: all data is gone
```

`down -v` can't be undone.
