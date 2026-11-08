+++
title = "Install on Windows with Platform Manager"
description = "Install SENTIENT and its database on Windows 10 or later with SENTIENT Platform Manager."
weight = 8

[extra]
status = "checked"
checked = "4.3.0.57"
+++
**SENTIENT Setup** installs SENTIENT, its database and the **Platform Manager** in one wizard. On Windows, SENTIENT always runs as Windows services, not in containers, because its licence is bound to the Windows hardware identity.

After installation, the same program becomes the Platform Manager. You use it to see the status, start and stop SENTIENT, read logs, update, back up and restore, and change the database type.

## Download

Get **SENTIENT Setup** from the SENTIENT release page (`github.com/QuakeString/sentient-release`) or from your supplier. There are two kinds of package:

- **Online:** Setup downloads the SENTIENT release you choose during installation and checks every file against its SHA-256 before using it.
- **Offline package:** Setup comes with a `payload` folder next to it. Use this for plants without internet access. Nothing is downloaded.

<div class="st-callout warn">

Setup is not code-signed yet, so Windows SmartScreen may show *Windows protected your PC*. Click **More info**, then **Run anyway**, but only for a file you got from the release page or your supplier.

</div>

## Run the wizard

Run Setup as an administrator. Nothing changes on the computer until you click **Install** on the **Summary** page.

1. **Licence agreement:** accept it to continue.
2. **What to install:** choose **SENTIENT and the Platform Manager**. Choose **Platform Manager** alone only to manage a SENTIENT that is already installed.
3. **System check:** Setup checks the Windows version, administrator rights, disk space, internet access to the download servers (online package only), an existing PostgreSQL and the ports. For ClickHouse it also checks CPU virtualization and WSL. You must resolve any item marked **Blocker**, then run the check again. A port that is already in use is only a warning, and you can pick another port later.
4. **Database:** choose how history is stored:
   - **PostgreSQL:** everything in PostgreSQL. This is the simplest choice and suits small sites.
   - **PostgreSQL with TimescaleDB:** history is compressed and kept in time chunks.
   - **ClickHouse:** history in ClickHouse, which runs in Docker inside WSL2, with everything else in PostgreSQL. This is for large sites. See [Windows with ClickHouse (WSL2)](/docs/installation/windows-clickhouse/).
5. **Database settings:** the database name, user and password, and the PostgreSQL administrator password. The default folders are `C:\Program Files\SENTIENT` for SENTIENT and `C:\PostgreSQL\18` for PostgreSQL.
6. **Network ports:** the web UI, MQTT, MQTT over TLS, CoAP, CoAP over DTLS, PostgreSQL and (for ClickHouse) the ClickHouse ports. See [Ports and firewall](/docs/operations/ports/).
7. **Administrator:** the system administrator's email and password, at least 8 characters. Write them down, because you sign in with them later.
8. **Configuration:** optional. You can change any SENTIENT setting here. Search by name or by variable, for example `batch`. Leave the **SENTIENT default** unless you know you need a change. See [Environment settings](/docs/operations/settings/).
9. **Shortcuts and startup:** shortcuts, and optionally an **operator screen** that opens SENTIENT after a reboot and signs in automatically.
10. **Summary:** check your choices and click **Install**. Each long step shows what it is doing.

When it finishes, open SENTIENT from the shortcut, or go to `http://localhost:8080`, and [activate your licence](/docs/installation/licence/).

## If Setup finds an earlier installation

- **SENTIENT already installed:** Setup opens in maintenance mode. You can update, repair or uninstall from there.
- **A database from an earlier install:** Setup asks whether to **Keep using it** or **Start fresh**. If you keep it, Setup first checks that its history table fits the database type you chose. If you start fresh, Setup sets the old database aside under **Kept**, where you can remove it later.

## The Platform Manager

Open **SENTIENT Platform Manager** from the Start menu.

| Screen | What you do there |
|---|---|
| **Status** | See whether SENTIENT, the database and the gateway are running. Start, stop and restart them. |
| **Logs** | Read the SENTIENT and database logs. |
| **Update** | Install a newer SENTIENT, or **Roll back last update**. See [Upgrade and roll back](/docs/operations/upgrade/). |
| **Backup and restore** | One backup file with the database, telemetry and file stores. See [Back up and restore](/docs/operations/backup-restore/). |
| **Migration** | Change the database type, with all history copied and checked. |
| **Gateway** | Install, update, start and stop SENTIENT Gateway on this computer. |
| **Settings** | Change SENTIENT settings after installation. |

**Updates** has an update channel: **Stable**, **Release candidate** or **Nightly**. There is also a daily check that shows a notice when a newer SENTIENT or Platform Manager is out. The Platform Manager also updates itself.

## Repair

If SENTIENT will not start after a Windows update or a missing file, run Setup again and choose **Repair**. It registers the services again and restores missing program files. Your data and settings are kept.

## Known problem: PostgreSQL does not initialise

On computers with an old Visual C++ runtime, PostgreSQL 18 could crash during setup. Setup 0.8.0-rc9 and later install Visual C++ runtime 14.44 first. With an older Setup, install `vc_redist.x64.exe` from the same release page, then click **Retry**. See [Installation and upgrade errors](/docs/troubleshooting/install-errors/).
