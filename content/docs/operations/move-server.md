+++
title = "Move to a new server"
description = "Move a SENTIENT installation, its data and its licence to new hardware."
weight = 16

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Moving SENTIENT means four things: release the licence on the old machine, copy the data, install the same SENTIENT version on the new machine, and point devices and gateways to the new address.

## 1. Plan the downtime

Devices and gateways cannot deliver data while you move, unless they buffer it. SENTIENT Gateway buffers data while SENTIENT is unreachable, and sends it later. Pick a quiet time and tell users.

## 2. Back up the old server

Make a complete backup: the database, ClickHouse if you use it, and the data folder with `secrets.key`. See [Back up and restore](/docs/operations/backup-restore/). Stop SENTIENT after the backup so that no new data is written that the backup doesn't have.

## 3. Release the licence

The licence is bound to the old machine's hardware. On the old server, open **License** and click **Deactivate**. This releases the binding on the licence server so that the same key can be activated on the new machine.

If the old machine is broken or already gone, ask your supplier to release the binding instead.

## 4. Install the same version on the new server

Install **the same SENTIENT version** as on the old server, with the same database type. Use [Platform Manager](/docs/installation/windows/) or [Docker](/docs/installation/docker/). Upgrade only after the move works, as a separate step.

## 5. Restore the data

Restore the backup on the new server, including `secrets.key`. With the Platform Manager, use **Restore**, then **Put the restored data into service**.

## 6. Activate the licence

Sign in as the system administrator, open **License** and activate the same key. See [Activate your licence](/docs/installation/licence/).

## 7. Point devices and gateways to the new server

- If the new server takes over the old server's IP address or DNS name, devices reconnect by themselves.
- If not, change the server address in every gateway (the gateway's admin UI or its remote configuration) and in every device that connects directly. Device access tokens and certificates come with the database, so they do not change.

## 8. Check

- Devices show **Active** and new telemetry arrives.
- Dashboards show recent data, and alarms and notifications arrive.
- Settings that use stored secrets still work: send a test mail from the mail server settings.

Keep the old server's backup until you are sure everything works.
