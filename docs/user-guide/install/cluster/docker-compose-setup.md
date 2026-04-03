---
layout: docwithnav
assignees:
- ashvayka
title: Cluster setup with Docker Compose
description: SENTIENT IoT platform cluster setup with Docker Compose guide

---

* TOC
{:toc}

This guide will help you to setup SENTIENT in cluster mode using Docker Compose tool. 

## Prerequisites

SENTIENT Microservices are running in dockerized environment.
Before starting please make sure Docker Engine and Docker Compose are installed in your system. 

{% include templates/install/docker-install.md %}

{% include templates/install/docker-install-note.md %}

## Step 1. Pull SENTIENT Images

Make sure your have [logged in](https://docs.docker.com/engine/reference/commandline/login/) to docker hub using command line.

```bash
docker pull sentient/tb-node:{{ site.release.ce_full_ver }}
docker pull sentient/tb-web-ui:{{ site.release.ce_full_ver }}
docker pull sentient/tb-js-executor:{{ site.release.ce_full_ver }}
docker pull sentient/tb-http-transport:{{ site.release.ce_full_ver }}
docker pull sentient/tb-mqtt-transport:{{ site.release.ce_full_ver }}
docker pull sentient/tb-coap-transport:{{ site.release.ce_full_ver }}
docker pull sentient/tb-lwm2m-transport:{{ site.release.ce_full_ver }}
docker pull sentient/tb-snmp-transport:{{ site.release.ce_full_ver }}
```

## Step 2. Review the architecture page

Starting SENTIENT v2.2, it is possible to install SENTIENT cluster using new microservices architecture and docker containers. 
See [**microservices**](/docs/reference/msa/) architecture page for more details.

## Step 3. Clone SENTIENT repository

```bash
git clone -b {{ site.release.branch }} https://github.com/sentient/sentient.git --depth 1
cd sentient/docker
```
{: .copy-code}

## Step 4. Configure SENTIENT database

{% include templates/install/configure-db-docker-compose.md %}

## Step 5. Choose SENTIENT queue service 

{% include templates/install/install-queue-docker-compose.md %}

{% capture contenttogglespecqueue %}
Kafka <small>(default, recommended for on-prem, production installations)</small>%,%kafka%,%templates/install/cluster-queue-kafka.md%br%
Confluent Cloud <small>(Event Streaming Platform based on Kafka)</small>%,%confluent-cloud%,%templates/install/cluster-queue-confluent-cloud.md{% endcapture %}
{% include content-toggle.liquid content-toggle-id="ubuntuSentientQueue" toggle-spec=contenttogglespecqueue %} 

## Step 6. Enable monitoring (optional)

{% include templates/install/configure-monitoring-docker-compose.md %}

## Step 7. Running

### Create and check required host volumes
{% include templates/install/docker/docker-compose-setup-volumes.md %}

### Install and run SENTIENT
{% assign dockerComposeFileLocation = "" %}
{% include templates/install/docker/docker-compose-setup-running.md %}

## Post-installation steps

{% include templates/install/generate_certificate_docker-compose.md %}

### Upgrading to new SENTIENT version

{% include templates/install/upgrade-sentient.md %}

## Next steps

{% assign currentGuide = "InstallationGuides" %}{% include templates/guides-banner.md %}
