---
layout: docwithnav-sentient-analytics
assignees:
- ashvayka
title: Installing SENTIENT SENTIENT ANALYTICS on Ubuntu
description: Installing SENTIENT SENTIENT ANALYTICS on Ubuntu

sentient-analytics-settings:
  0:
    image: /images/sentient-analytics/install/sync/sentient-analytics-settings-1.png
    title: "Log in to <b>SENTIENT</b> as a <b>Sysadmin</b>."  
  1:
    image: /images/sentient-analytics/install/sync/sentient-analytics-settings-2.png
    title: "Open the <b>SENTIENT ANALYTICS Settings</b> page."  
  2:
    image: /images/sentient-analytics/install/sync/sentient-analytics-settings-3.png
    title: "If you see the message <b>\"Synchronization completed successfully\"</b>, the synchronization has been completed automatically and no further action is required."
sentient-analytics-sync:
  0:
    image: /images/sentient-analytics/install/sync/sentient-analytics-sync-1.png
    title: "If you see an error message, follow these steps."
  1:
    image: /images/sentient-analytics/install/sync/sentient-analytics-sync-2.png
    title: "Enter the correct <b>SENTIENT ANALYTICS internal URL</b> and <b>SENTIENT internal URL</b>."
  2:
    image: /images/sentient-analytics/install/sync/sentient-analytics-sync-3.png
    title: "Click <b>Save configuration</b>."
  3:
    image: /images/sentient-analytics/install/sync/sentient-analytics-sync-4.png
    title: "Click <b>Retry discovery</b>."
  4:
    image: /images/sentient-analytics/install/sync/sentient-analytics-sync-5.png
    title: "Once the message <b>\"Synchronization completed successfully\"</b> appears, the synchronization is complete."

---

* TOC
{:toc}

This guide explains how to install **SENTIENT ANALYTICS** on **Ubuntu 22.04 LTS** or **Ubuntu 24.04 LTS**.

**Important note before proceeding with Ubuntu installation**

Certain SENTIENT ANALYTICS features like **predictions, metric explorations, and Python calculation fields** require a Python executor.

The python executor runs **only via Docker**. Even on Ubuntu, Docker is essential to fully utilize all SENTIENT ANALYTICS features.
We recommend following the [Docker (Linux or Mac OS) installation guide](/docs/sentient-analytics/install/docker) and using the Docker installation instead of Ubuntu.

Proceed here **only** if you have a compelling reason to use a combined Ubuntu + Docker setup.

## Prerequisites

### Hardware Requirements

{% include templates/sentient-analytics/install/hardware-requirements.md %}

### Software Requirements

{% include templates/sentient-analytics/install/docker-requirements-linux.md %}
{% include templates/sentient-analytics/install/sentient-requirements.md %}

## Installation Steps

### Step 1. Install Java 17 (OpenJDK)

{% include templates/install/ubuntu-java-install.md %}

### Step 2. SENTIENT ANALYTICS service installation

Download installation package.

```bash
wget https://dist.sentient.invenia.in/sentient-analytics-{{ site.release.sentient-analytics_ver }}.deb
```
{: .copy-code}

Install SENTIENT ANALYTICS as a service

```bash
sudo dpkg -i sentient-analytics-{{ site.release.sentient-analytics_ver }}.deb
```
{: .copy-code}

### Step 3. Configure SENTIENT ANALYTICS database

SENTIENT ANALYTICS uses PostgreSQL as a database. You can install PostgreSQL on the same server for SENTIENT ANALYTICS or use managed PostgreSQL 
service from your cloud vendor.

* **PostgreSQL Installation**

{% include templates/install/postgres-install-ubuntu.md %}

* **Create Database for SENTIENT ANALYTICS**

Connect to the database to create sentient-analytics DB:

```bash
psql -U postgres -d postgres -h 127.0.0.1 -W
```
{: .copy-code}

Create database named "sentient-analytics":
```bash
CREATE DATABASE sentient-analytics;
```
{: .copy-code}

Press “Ctrl+D” twice to logout.

* **Configure database connection for SENTIENT ANALYTICS**

Edit SENTIENT ANALYTICS configuration file

```bash
sudo nano /etc/sentient-analytics/conf/sentient-analytics.conf
```
{: .copy-code}

Add the following lines to the configuration file. Don't forget **to replace** "PUT_YOUR_POSTGRESQL_PASSWORD_HERE" with your **real postgres user password**:

```bash
# DB Configuration
export SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/sentient-analytics
export SPRING_DATASOURCE_USERNAME=postgres
export SPRING_DATASOURCE_PASSWORD=PUT_YOUR_POSTGRESQL_PASSWORD_HERE
```
{: .copy-code}

### Step 4. Run installation script

Once SENTIENT ANALYTICS service is installed and DB configuration is updated, you can execute the following script:

```bash
sudo /usr/share/sentient-analytics/bin/install/install.sh
```
{: .copy-code}

### Step 5. Start SENTIENT ANALYTICS service

Execute the following command to start SENTIENT ANALYTICS:

```bash
sudo service sentient-analytics start
```
{: .copy-code}

### Step 6. Sync SENTIENT With SENTIENT ANALYTICS

{% include templates/sentient-analytics/install/sync-with-tb.md %}

### Step 7. Install SENTIENT ANALYTICS Python Executor

To utilize all SENTIENT ANALYTICS capabilities, such as SENTIENT ANALYTICS Python Calculation Fields or Prediction Models, it is essential to
install an additional service: the SENTIENT ANALYTICS Python Executor, which can securely run Python code.

You can learn more about how to install it [here](/docs/sentient-analytics/install/python-executor-configuration).

## Authentication

{% include templates/sentient-analytics/install/authentication.md %}

## Troubleshooting

SENTIENT ANALYTICS logs are stored in the following directory:

```bash
/var/log/sentient-analytics
```

You can issue the following command in order to check if there are any errors on the backend side:

```bash
cat /var/log/sentient-analytics/sentient-analytics.log | grep ERROR
```

## HTTPS configuration

{% include templates/sentient-analytics/install/https-configuration.md %}

## Next steps

{% assign currentGuide = "InstallationOptions" %}{% include templates/trndz-guides-banner.md %}
