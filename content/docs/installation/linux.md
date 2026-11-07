+++
title = "Install on Linux"
description = "Install SENTIENT on a Linux server with Platform Manager, in Docker or as native systemd services."
weight = 11

[extra]
status = "checked"
checked = "4.3.0.57"
+++
On Linux you have three choices:

| Way | When to use it |
|---|---|
| **Platform Manager, Docker mode** (recommended) | Most servers. The Platform Manager runs SENTIENT and its database in Docker on this machine, and gives you updates, backups and rollback from one window. |
| **Platform Manager, native mode** | Docker is not allowed on the server. SENTIENT and PostgreSQL run as systemd services. This mode supports PostgreSQL and PostgreSQL with ClickHouse. |
| **Docker Compose by hand** | You manage Docker yourself. See [Install with Docker](/docs/installation/docker/). |

## Install the Platform Manager

Download the Platform Manager for Linux from the SENTIENT release page as a `.deb` package, AppImage or Arch package, and install it the usual way for your distribution. For example, on Debian or Ubuntu, run `sudo apt install ./<downloaded file>.deb`.

Start **SENTIENT Setup** from the application menu, or run the AppImage. The wizard has the same steps as on Windows: licence agreement, system check, database, database settings, ports, administrator, configuration and summary. See [Install on Windows with Platform Manager](/docs/installation/windows/#run-the-wizard) for what each step asks.

In the system check, Docker mode checks for **Docker Engine**, the **Docker daemon** and **Docker Compose**, and native mode checks the **Package manager**. Resolve anything marked **Blocker** first.

Native mode installs SENTIENT from the `sentient-payload-linux-x86_64.tar` package on the release page. For an offline server, put that file next to Setup.

## Manage a SENTIENT you installed yourself

If SENTIENT is already running, installed by hand or with Docker Compose, open the Platform Manager and choose **Add existing instance**. It then manages that installation, including updates and backups.

## The licence on Linux

On a Linux server, the licence fingerprint reads the real hardware even inside Docker, so it stays stable when containers are rebuilt. With your own compose file, also mount `/etc/machine-id`. See [Install with Docker](/docs/installation/docker/#linux-hosts-keep-the-licence-bound).
