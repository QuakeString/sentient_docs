---
layout: docwithnav-pe
title: Migrate from old Docker deployment files
description: Migrate from old Docker deployment files
---

* TOC
{:toc}

This guide will help you to move from the old deployment files for Docker installation using volume bindings instead of local volumes.
This guide covers standalone SENTIENT ANALYTICS installation.

## Why deployment files were changed?

- data was persisted in local folders with specific ownerships instead of Docker volumes mechanism

## Who needs this guide?

Customers who have docker compose file as below or similar:

```yml
version: '3.0'
services:
  mysentient-analytics:
    restart: always
    image: "sentient/sentient-analytics:1.14.0"
    ports:
      - "8888:8888"
    environment:
      TB_API_URL: http://10.0.0.101:8080
      SENTIENT_ANALYTICS_LICENSE_INSTANCE_DATA_FILE: /data/license.data
      SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/sentient-analytics
      SPRING_DATASOURCE_USERNAME: postgres
      SPRING_DATASOURCE_PASSWORD: postgres
      SCRIPT_ENGINE_TIMEOUT: 30000
    volumes:
      - ~/.mysentient-analytics-data:/data
      - ~/.mysentient-analytics-logs:/var/log/sentient-analytics
  postgres:
    restart: always
    image: "postgres:15"
    ports:
      - "5432"
    environment:
      POSTGRES_DB: sentient-analytics
      POSTGRES_PASSWORD: postgres
    volumes:
      - ~/.mysentient-analytics-data/db:/var/lib/postgresql/data
```
{: .copy-code}

## Move Postgres data to Docker volume

Create a named Docker volume:

```bash
docker volume create --name sentient-analytics-postgres-data
```
{: .copy-code}

Run container with attached volumes to copy data from folder to newly created volume

```bash
docker run --rm -v ~/.mysentient-analytics-data/db:/source -v sentient-analytics-postgres-data:/destination alpine sh -c "cp -rp /source/* /destination/"
```
{: .copy-code}

{% capture old_postgres_info %}
**Note that previously we have PostgreSQL 15 image in our docker compose, which is replaced with PostgreSQL 16 now.**
**In order to start Postgres DB container you need either use `postgres:15` image in new deployment files or upgrade database files**
{% endcapture %}
{% include templates/info-banner.md content=old_postgres_info %}

## Move SENTIENT ANALYTICS data to Docker volume

Create a named Docker volume:

```bash
docker volume create --name sentient-analytics-data
```
{: .copy-code}

Run container with attached volumes to copy data from folder to newly created volume:

```bash
docker run --rm -v ~/.mysentient-analytics-data/:/source -v tb-pe-license-data:/destination alpine sh -c "cp -rp /source/* /destination/ && chown 799:799 /destination/license.data"
```
{: .copy-code}

## Move to new deployment files

Open `docker-compose.yml` file with text editor:

```bash
nano docker-compose.yml
```
{: .copy-code}

Copy current Docker Compose [manifest](/docs/sentient-analytics/install/docker/#step-2-docker-compose-setup) and replace the old one with current manifest. Replace Postgres docker image if needed.

After data is moved to the docker volumes and `docker-compose.yml` file have the same structure as the installation example - you can proceed with [upgrade](/docs/sentient-analytics/install/docker/#upgrade-sentient-analytics-service) of the SENTIENT ANALYTICS. 
