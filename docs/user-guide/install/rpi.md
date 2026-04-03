---
layout: docwithnav
assignees:
- ashvayka
title: Installing SENTIENT on Raspberry Pi
description: Installing SENTIENT IoT Platform on Raspberry Pi

---

{% include templates/live-demo-banner.md %}

* TOC
{:toc}



## Prerequisites

This guide describes how to install SENTIENT on a Raspberry Pi.
Hardware requirements depend on chosen database and amount of devices connected to the system. 
To run SENTIENT and PostgreSQL you will need at least 4Gb of RAM.
To run SENTIENT and Cassandra you will need at least 8Gb of RAM.


## Step 1. Install Java 17 (OpenJDK) 
{% include templates/install/ubuntu-java-install.md %}
{: .copy-code}

## Step 2. SENTIENT service installation

Download installation package.

```bash
wget https://github.com/sentient/sentient/releases/download/{{ site.release.ce_tag }}/sentient-{{ site.release.ce_ver }}.deb
```
{: .copy-code}

Install SENTIENT as a service

```bash
sudo dpkg -i sentient-{{ site.release.ce_ver }}.deb
```
{: .copy-code}

## Step 3. Configure SENTIENT database

{% include templates/install/rpi-db-postgresql.md %}

## Step 4. Choose SENTIENT queue service

{% include templates/install/rpi-install-queue.md %}

{% capture contenttogglespecqueue %}
In Memory <small>(built-in and default)</small>%,%inmemory%,%templates/install/queue-in-memory.md%br%
Confluent Cloud <small>(Event Streaming Platform based on Kafka)</small>%,%confluent-cloud%,%templates/install/ubuntu-queue-confluent-cloud.md{% endcapture %}

{% include content-toggle.liquid content-toggle-id="ubuntuSentientQueue" toggle-spec=contenttogglespecqueue %} 

## Step 5. Memory update for slow machines (4GB of RAM) 

{% include templates/install/memory-on-slow-machines.md %} 

## Step 6. Run installation script
{% include templates/run-install.md %} 


## Step 7. Start SENTIENT service

{% include templates/start-service.md %}

{% capture 90-sec-ui %}
Please allow up to 90 seconds for the Web UI to start.{% endcapture %}
{% include templates/info-banner.md content=90-sec-ui %}

## Post-installation steps

### Upgrading to new SENTIENT version

The upgrade procedure for Raspberry Pi is identical to the Ubuntu instructions.

{% include templates/install/upgrade-sentient.md %}

## Troubleshooting

{% include templates/install/troubleshooting.md %}

## Next steps

{% assign currentGuide = "InstallationGuides" %}{% include templates/guides-banner.md %}
