+++
title = "System requirements"
description = "Operating systems, processor, memory, disk and browsers for SENTIENT, with measured throughput to size a server from."
weight = 7

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT runs on one 64-bit x86 server (x86-64) together with its database. The same machine can serve a single plant with a few devices or hundreds of thousands of values per second; what changes is the CPU, memory and disk you give it.

## Operating systems

| Way to install | Needs |
|---|---|
| [Windows, Platform Manager](/docs/installation/windows/) | Windows 10 version 2004 (build 19041) or later, or Windows 11, 64-bit. Administrator rights. With ClickHouse: CPU virtualization switched on in the BIOS or UEFI, and WSL2, which Setup installs |
| [Linux, Platform Manager, Docker mode](/docs/installation/linux/) | Docker Engine with the Compose plugin |
| [Linux, Platform Manager, native mode](/docs/installation/linux/) | systemd, and one of the package managers apt (Debian, Ubuntu), dnf (RHEL, Fedora, Rocky, Alma), zypper (openSUSE) or pacman (Arch) |
| [Docker Compose by hand](/docs/installation/docker/) | Docker Engine 24 or later with the Compose plugin |

The online installers download PostgreSQL and ClickHouse during setup. For a server without internet access, use the offline package from the release page.

## Disk

Setup asks for at least **10 GB free** for the program, the database engine and the first data. Beyond that, disk use grows with your history: the number of values stored per second, multiplied by how long you keep them (**Storage TTL** in the [tenant profile](/docs/user-guide/tenant-profiles/)).

- **PostgreSQL** stores each value as a row with its indexes. It is the simplest choice and fits small and medium plants.
- **PostgreSQL with TimescaleDB** compresses older history.
- **PostgreSQL with ClickHouse** stores history in a column store, which takes much less disk per value and stays fast for charts over months. Choose it when you store many values per second or keep history for years.

Measure your own rate after a week (see [API usage](/docs/administration/api-usage/), **Data points storage days**) and size the disk from that. Use an SSD for the database; a spinning disk limits write speed long before the CPU does.

Keep room for backups too. A backup holds the whole database, so plan for at least the size of the database again, on another disk or machine.

## Processor and memory

The table is a starting point for one server running SENTIENT and its database together. Watch CPU, memory and the [queue statistics](/docs/operations/tuning/) under real load, and grow from there.

| Plant | Values per second | CPU cores | Memory | Database |
|---|---|---|---|---|
| Small: one line, a few hundred tags | up to 1,000 | 2 | 4 GB | PostgreSQL |
| Medium: a plant, thousands of tags | up to 20,000 | 4 | 8 GB | PostgreSQL or TimescaleDB |
| Large: several plants or fast sampling | 20,000 and more | 8 or more | 16 GB or more | PostgreSQL with ClickHouse |

Add memory for the [offline translator](/docs/administration/translations/#the-sentient-translator) if it runs on the same machine: each language pack shows its memory need when you choose it.

### Measured throughput

Measured on one 20-core machine with 7 GB of memory, with SENTIENT, PostgreSQL and ClickHouse on the same machine, 100 devices sending over MQTT, history and latest values in ClickHouse:

| Values per second | CPU used, all three together |
|---|---|
| 100,000 | about 0.85 of one core |
| 200,000 | about 1.4 cores |

Both rates ran with no errors. The same load with latest values in PostgreSQL used about 1.4 and 2 cores. HTTP devices cost more than MQTT, because each HTTP request is authenticated on its own.

## Browsers

The web UI supports the current versions of **Chrome**, **Edge**, **Firefox** (and Firefox ESR) and **Safari**, including on Android and iOS. Internet Explorer is not supported.

For control-room screens that show large SCADA dashboards all day, use Chrome or Edge on a machine with a dedicated graphics card or a recent integrated one.

## Network

See [Ports and firewall](/docs/operations/ports/) for the ports SENTIENT, its databases and the gateway use. The licence is checked against the licence server over HTTPS; see [Licence](/docs/installation/licence/) for offline servers.

## Related

- [Performance tuning](/docs/operations/tuning/)
- [Environment settings](/docs/operations/settings/)
