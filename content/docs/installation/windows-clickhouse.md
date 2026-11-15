+++
title = "Windows with ClickHouse (WSL2)"
description = "Run the hybrid PostgreSQL and ClickHouse setup on Windows, with ClickHouse inside WSL2."
weight = 9

[extra]
status = "checked"
checked = "4.3.0.57"
+++
With the **ClickHouse** database option, SENTIENT keeps telemetry history in ClickHouse and everything else in PostgreSQL. ClickHouse has no native Windows build, so Platform Manager runs it in Docker inside WSL2 and sets all of it up for you. You do not need to install WSL, Linux or Docker yourself.

## When to choose ClickHouse

Choose ClickHouse when the site stores a lot of history: many thousands of data points per second, or years of history that people chart and report on. ClickHouse compresses telemetry far better than PostgreSQL and answers long-range charts much faster.

For a small or medium site, **PostgreSQL** alone is simpler: one database to back up, nothing extra running. You can move to ClickHouse later with Platform Manager's **Migration** screen.

## Before you start

| Need | Detail |
|---|---|
| Windows | Windows 10 version 2004 (build 19041) or newer, or Windows 11 |
| CPU virtualization | Switched on in the BIOS or UEFI (Intel VT-x, AMD-V / SVM). The **System check** step fails if it is off |
| Administrator rights | Setup enables Windows features and creates a service account |
| Disk | 10 GB free or more for the images and data, plus room for your history |
| Internet | The online package downloads WSL, Docker and ClickHouse |

## Install

1. Run Platform Manager setup as described in [Windows with Platform Manager](/docs/installation/windows/).
2. At **Database**, choose **ClickHouse**.
3. At **System check**, the items **WSL2** and **SENTIENT WSL distro** may show that setup will install them. That is expected. Fix anything marked **Blocker**, usually CPU virtualization.
4. At **Network ports**, keep or change the ClickHouse ports.
5. Finish the wizard. Setup installs PostgreSQL and SENTIENT, then ClickHouse.

**If Windows must restart:** when WSL was not enabled before, Windows needs a restart before WSL works. Setup says so and restarts Windows. After you sign in again, setup continues on its own where it stopped. You do not need to enter anything again.

## What setup creates

| Item | Name | Purpose |
|---|---|---|
| WSL distribution | `sentient` | The small Linux system that runs Docker and ClickHouse |
| Windows account | `sentient-clickhouse` | Hidden from the sign-in screen. WSL runs only inside a user's session, so ClickHouse gets an account of its own and runs with nobody signed in |
| Scheduled task | **SENTIENT ClickHouse** | Starts ClickHouse at every boot under that account |
| Folder | `C:\ProgramData\SENTIENT\clickhouse` | Its settings, logs and the distribution's disk |

Do not delete the account or the task: ClickHouse would stop starting at boot. **Uninstall and delete the data** in Platform Manager removes the distribution, the account and the task. A plain **Uninstall** keeps them, together with the history, for a later reinstall.

## After a restart

ClickHouse starts about half a minute after Windows boots, before anyone signs in. If charts of history are empty right after a restart, wait a minute and refresh.

## Check that ClickHouse is healthy

Platform Manager's **Status** screen shows whether SENTIENT is running and which database option it uses. If SENTIENT runs but charts of history stay empty or show errors, check ClickHouse:

1. In **Task Scheduler**, find **SENTIENT ClickHouse**. It must show **Running**. If it does not, run it once by hand.
2. Check that CPU virtualization is still switched on. A BIOS update can switch it off.
3. Open **Logs** in Platform Manager and look for ClickHouse connection errors.
4. Look in `C:\ProgramData\SENTIENT\clickhouse` for `job.log`, the log of the last setup step.

## Back up

A ClickHouse installation has two databases. Platform Manager's **Backup and restore** screen backs up both together, see [Back up and restore](/docs/operations/backup-restore/).

## Related

- [Windows with Platform Manager](/docs/installation/windows/)
- [Ports and firewall](/docs/operations/ports/)
- [Installation errors](/docs/troubleshooting/install-errors/)
