---
layout: docwithnav
assignees:
- ashvayka
title: Installing SENTIENT using Docker (Windows)
description: Installing SENTIENT IoT Platform using Docker (Windows)

---

{% include templates/live-demo-banner.md %}

* TOC
{:toc}

This guide will help you to install and start SENTIENT using Docker on Windows.


## Prerequisites

- [Install Docker Toolbox for Windows](https://docker-docs.uclv.cu/toolbox/toolbox_install_windows/)

## Running

Running this image requires a server with at least 4GB of RAM (8GB is recommended) and minimum load (few messages per second).

## Choose SENTIENT queue service

{% include templates/install/install-queue.md %}

{% capture contenttogglespecqueue %}
In Memory <small>(built-in and default)</small>%,%inmemory%,%templates/install/windows-docker-queue-in-memory.md%br%
Kafka <small>(recommended for on-prem, production installations)</small>%,%kafka%,%templates/install/windows-docker-queue-kafka.md%br%
Confluent Cloud <small>(Event Streaming Platform based on Kafka)</small>%,%confluent-cloud%,%templates/install/windows-docker-queue-confluent-cloud.md{% endcapture %}

{% include content-toggle.liquid content-toggle-id="ubuntuSentientQueue" toggle-spec=contenttogglespecqueue %} 

here: 

- `8080:8080`            - connect local port 8080 to exposed internal HTTP port 8080
- `1883:1883`            - connect local port 1883 to exposed internal MQTT port 1883
- `8883:8883`            - connect local port 8883 to exposed internal MQTT over SSL port 8883
- `7070:7070`            - connect local port 7070 to exposed internal Edge RPC port 7070
- `5683-5688:5683-5688/udp`            - connect local UDP ports 5683-5688 to exposed internal COAP and LwM2M ports
- `tb-postgres-data` - name of the docker volume that stores the PostgreSQL's data
- `sentient-ce`             - friendly local name of the SENTIENT container
- `restart: always`        - automatically start SENTIENT in case of system reboot and restart in case of failure.
- `image: "sentient/tb-node:{{ site.release.ce_full_ver }}"`          - SENTIENT docker image and version.


## Initialize database schema & system assets

Before you start SENTIENT, initialize the database schema and load built-in assets by running:   

```bash
docker compose run --rm -e INSTALL_TB=true -e LOAD_DEMO=true sentient-ce
```

Environment variables:

- `INSTALL_TB=true` - Installs the core database schema and system resources (widgets, images, rule chains, etc.).
- `LOAD_DEMO=true` - Loads sample tenant account, dashboards and devices for evaluation and testing.

## Start the platform & tail logs

Bring up all containers in detached mode, then follow the SENTIENT logs (use PowerShell for the command below):

```bash
docker compose up -d; docker compose logs -f sentient-ce
```

After executing this command you can open `http://{your-host-ip}:8080` in you browser (for ex. `http://localhost:8080`). You should see SENTIENT login page.
Use the following default credentials:

- **System Administrator**: sysadmin@sentient.org / sysadmin
- **Tenant Administrator**: tenant@sentient.org / tenant
- **Customer User**: customer@sentient.org / customer
    
You can always change passwords for each account in account profile page.

You can safely detach from the log stream (e.g. Ctrl+C); containers will continue running.

## Inspect logs & control container lifecycle

If something goes wrong, you can stream the SENTIENT container logs in real time:

```bash
docker compose logs -f sentient-ce
```

Bring down every container defined in your Compose file:

```bash
docker compose down
```

Launch all services in detached mode:

```bash
docker compose up -d
```

## Post-installation steps

### Upgrading to new SENTIENT version

{% include templates/install/upgrade-sentient.md %}

## Troubleshooting

### DNS issues

{% include templates/troubleshooting/dns-issues-windows.md %}

## Next steps

{% assign currentGuide = "InstallationGuides" %}{% include templates/guides-banner.md %}
