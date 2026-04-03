---
layout: docwithnav-sentient-analytics
title: SENTIENT ANALYTICS Python Executor Configuration
description: How to configure SENTIENT ANALYTICS Python Executor on Linux or Mac OS

---

* TOC
{:toc}

## Overview

SENTIENT ANALYTICS Python Executor is required to run:

* Python Calculation fields
* All prediction models (except Fourier Transformation)
* Code generation for Metric Explorer

Starting from version 1.14.0, the only way to run these features is via SENTIENT ANALYTICS Python Executor using Docker (or Kubernetes).

## Prerequisites

### Windows

{% include templates/sentient-analytics/install/docker-requirements-windows.md %}

### Linux

{% include templates/sentient-analytics/install/docker-requirements-linux.md %}

## Python Executor Standalone Installation

### Step 1: Create Docker Compose File

Create the Docker Compose file with the following configuration:

```yml
services:
  sentient-analytics-python-executor:
    restart: always
    image: "sentient/sentient-analytics-python-executor:{{ site.release.sentient-analytics_ver }}"
    ports:
      - "8181:8181"
    environment:
      EXECUTOR_MANAGER: 1
      EXECUTOR_SCRIPT_ENGINE: 6
      THROTTLING_QUEUE_CAPACITY: 10
      THROTTLING_THREAD_POOL_SIZE: 6
      NETWORK_BUFFER_SIZE: 5242880
    volumes:
      - sentient-analytics-python-executor-conf:/python-executor-config-files
      - sentient-analytics-python-executor-data:/data
```
{: .copy-code}

Explanation of key fields:

* `8181` - Python executor port for communication with SENTIENT ANALYTICS service
* `restart: always` - automatically restarts the executor on failure or system reboot
* `sentient/sentient-analytics-python-executor:{{ site.release.sentient-analytics_ver }}` - Docker image for SENTIENT ANALYTICS Python Executor
* `sentient-analytics-python-executor-conf:/python-executor-config-files` - mounts the volume ``sentient-analytics-python-executor-conf` to SENTIENT ANALYTICS Python Executor directory with configuration files
* `sentient-analytics-python-executor-data:/data` - mounts the volume `sentient-analytics-python-executor-data` to SENTIENT ANALYTICS Python Executor additional data directory

### Step 2: Start Python Executor

```bash
docker compose up -d
docker compose logs -f sentient-analytics-python-executor
```
{: .copy-code}

### Step 3: Connect SENTIENT ANALYTICS to Python Executor

* **Linux or Mac OS**

Configure SENTIENT ANALYTICS to communicate with the Python Executor.

Edit `/usr/share/sentient-analytics/conf/sentient-analytics.conf` and add:

```bash
export SCRIPT_ENGINE_TIMEOUT=30000
export SCRIPT_ENGINE_PROVIDER=DOCKER_CONTAINER
export SCRIPT_ENGINE_DOCKER_PROVIDER_URL=PYTHON_EXECUTOR_HOST:PYTHON_EXECUTOR_PORT
```
{: .copy-code}

Replace `PYTHON_EXECUTOR_HOST` and `PYTHON_EXECUTOR_PORT` with your Python Executor service values and ensure SENTIENT ANALYTICS can reach this network destination.

* **Windows**

Open Notepad as Administrator and edit:

```text
C:\Program Files (x86)\sentient-analytics\conf\sentient-analytics.yml
```
{: .copy-code}

Locate the `script-engine` block and configure:

```yml
script-engine:
  provider: "${SCRIPT_ENGINE_PROVIDER:DOCKER_CONTAINER}"
  runtime-timeout: "${SCRIPT_ENGINE_TIMEOUT:60000}"
  callback-timeout: "${SCRIPT_ENGINE_TIMEOUT:60000}"
  docker-provider-url: "${SCRIPT_ENGINE_DOCKER_PROVIDER_URL:PYTHON_EXECUTOR_HOST:PYTHON_EXECUTOR_PORT}"
  websocket-buffer-size: "${SCRIPT_ENGINE_WEBSOCKET_BUFFER_SIZE:20971520}"
  websocket-concurrency: "${SCRIPT_ENGINE_WEBSOCKET_CONCURRENCY:5}"
```

Replace `PYTHON_EXECUTOR_HOST` and `PYTHON_EXECUTOR_PORT` with your Python Executor service values and ensure SENTIENT ANALYTICS can reach this network destination.

## How to Migrate SENTIENT ANALYTICS Python Executor 1.13.2 to SENTIENT ANALYTICS Python Executor 1.14.0

If you already have a Python Executor with a version earlier than 1.14.0 connected to SENTIENT ANALYTICS, you should migrate it before updating SENTIENT ANALYTICS to 1.14.0.

### Step 1. Modify Docker Compose File

Locate the `docker-compose.yml` file from which the Python Executor was launched.

Change the Python Executor image tag to version 1.14.0 and update the `volumes` section to include configuration and data directories.

The final `docker-compose.yml` should look like this:

```yml
services:
  sentient-analytics-python-executor:
    restart: always
    image: "sentient/sentient-analytics-python-executor:{{ site.release.sentient-analytics_ver }}"
    ports:
      - "8181:8181"
    environment:
      EXECUTOR_MANAGER: 1
      EXECUTOR_SCRIPT_ENGINE: 6
      THROTTLING_QUEUE_CAPACITY: 10
      THROTTLING_THREAD_POOL_SIZE: 6
      NETWORK_BUFFER_SIZE: 5242880
    volumes:
      - sentient-analytics-python-executor-conf:/python-executor-config-files
      - sentient-analytics-python-executor-data:/data
```
{: .copy-code}

### Step 2. Restart Python Executor

Restart the Python Executor to apply the changes:

```bash
docker compose up -d
docker compose logs -f sentient-analytics-python-executor
```
{: .copy-code}

## How to Connect Additional Libraries to the Python Executor

If necessary, you can add additional Python libraries to the **Python Executor** and use them in your SENTIENT ANALYTICS Calculation Fields or SENTIENT ANALYTICS Custom Prediction Models.

For example, if you want to add the **`emoji`** library (specific version 2.2.0), follow these steps.

### Step 1. Open a shell in the running container

```bash
docker compose exec sentient-analytics-python-executor bash
```

### Step 2. Add library to `requirements.txt`

You need to append the library name and version to the `requirements.txt` file located in your configuration directory (`/python-executor-config-files`):

```bash
echo 'emoji==2.2.0' >> /python-executor-config-files/requirements.txt
```
{: .copy-code}

After append all necessary dependencies type `exit` to exit from a shell.

### Step 3. Restart the Docker Container

Find the container name and restart it:
```bash
docker compose restart sentient-analytics-python-executor
```
{: .copy-code}

### Step 4. Verify Installation

Check the logs to ensure the library was installed successfully:

```bash
docker compose logs sentient-analytics-python-executor
```
{: .copy-code}

You should see:

```text
Installing custom Python requirements...
Requirement already satisfied: emoji==2.2.0 in /usr/local/lib/python3.9/site-packages
```

After the container restarts, you can import and use the custom libraries in your SENTIENT ANALYTICS Calculation Fields or SENTIENT ANALYTICS Custom Prediction Models.

## Next steps

{% assign currentGuide = "InstallationOptions" %}{% include templates/trndz-guides-banner.md %}
