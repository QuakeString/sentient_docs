+++
title = "Operations"
description = "Keep a SENTIENT installation healthy: backups, upgrades, moving servers and settings."
sort_by = "weight"

[extra]
status = "checked"
checked = "4.3.0.57"
+++
These pages are for whoever looks after the SENTIENT server: the plant's IT or automation engineer.

## Regular checks

A few minutes a week prevent most outages.

| Check | How | Why |
|---|---|---|
| The server is running | Platform Manager **Status** screen, or `docker compose ps` | Devices and gateways buffer data for a while, but not forever |
| A recent backup exists and opens | Look at the date of the newest backup; restore one to a test database now and then | A backup that was never restored is a hope, not a backup |
| The `secrets.key` file is backed up with the database | See [Back up and restore](/docs/operations/backup-restore/) | Without it, stored passwords and tokens cannot be decrypted after a restore |
| Free disk space | Windows Explorer, or `df -h` on Linux | Telemetry grows every day; a full disk stops the database |
| Licence expiry | The **License** page warns 30 days before | An expired licence stops all changes, see [Licence errors](/docs/troubleshooting/licence-errors/) |
| Errors in the log | Platform Manager **Logs**, or `docker compose logs` | Repeated errors often show a problem before users notice |

## Tasks

- [Back up and restore](/docs/operations/backup-restore/): database, telemetry history and the secrets key.
- [Upgrade and roll back](/docs/operations/upgrade/): move to a new release, and go back if needed.
- [Move to a new server](/docs/operations/move-server/): new hardware, same data and licence.
- [Environment settings](/docs/operations/settings/): every setting you can change, with its default.
- [Ports and firewall](/docs/operations/ports/): what to open, and what to keep closed.
- [Uninstall](/docs/operations/uninstall/): remove SENTIENT with or without its data.

When something goes wrong, start at [Troubleshooting](/docs/troubleshooting/).
