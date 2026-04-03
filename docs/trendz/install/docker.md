---
layout: docwithnav-sentient-analytics
assignees:
  - ashvayka
title: Installing SENTIENT SENTIENT ANALYTICS using Docker (Linux or Mac OS)
description: Installing SENTIENT SENTIENT ANALYTICS using Docker (Linux or Mac OS)

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


This guide will help you to install and start SENTIENT ANALYTICS using Docker on Linux or Mac OS.

## Prerequisites

{% include templates/sentient-analytics/install/docker-requirements-linux.md %}
{% include templates/sentient-analytics/install/sentient-requirements.md %}

## Installation Steps

### Step 1. Docker Compose setup

SENTIENT ANALYTICS can be run either in the same Docker Compose file as SENTIENT or in a separate Docker Compose file.

For small and medium installations, we recommend installing SENTIENT ANALYTICS in the same Docker Compose file as SENTIENT.

{% capture contenttogglespec %}
The same Docker Compose file with SENTIENT%,%theSameFile%,%templates/sentient-analytics/install/docker-compose-the-same-file-linux.md%br%
Separate Docker Compose file%,%separateFile%,%templates/sentient-analytics/install/docker-compose-separate-file-linux.md{% endcapture %}
{% include content-toggle.liquid content-toggle-id="runOption" toggle-spec=contenttogglespec %}

### Step 2. Start SENTIENT ANALYTICS service

{% include templates/sentient-analytics/install/docker-start-sentient-analytics-service.md %}

### Step 3. Sync SENTIENT With SENTIENT ANALYTICS

{% include templates/sentient-analytics/install/sync-with-tb.md %}

## Authentication

{% include templates/sentient-analytics/install/authentication.md %}

## Detaching, stop and start commands

{% include templates/sentient-analytics/install/docker-detach-stop-start-commands.md %}

## Upgrade SENTIENT ANALYTICS Service

{% capture upgrade_version_by_version%}
**Note, that you can upgrade SENTIENT ANALYTICS from any version to the latest at once (for example, 1.2.0 -> {{ site.release.sentient-analytics_ver }} ,etc).**
{% endcapture %}
{% include templates/info-banner.md content=upgrade_version_by_version %}

Below is an example of how to upgrade from any SENTIENT ANALYTICS version to {{ site.release.sentient-analytics_ver }}

* Create a dump of your database:

```bash
docker compose exec sentient-analytics-postgres sh -c "pg_dump -U postgres sentient-analytics > /var/lib/postgresql/data/sentient-analytics_dump"
```
{: .copy-code}

When a new SENTIENT ANALYTICS release is available, follow these steps to update your installation without losing data:

{% capture old_manifests_info %}
**If you are upgrading using previous version of deployment files, make sure to follow steps described in this [instruction](/docs/sentient-analytics/install/old-docker-migrate/) first.**
{% endcapture %}
{% include templates/warn-banner.md content=old_manifests_info %}

1. Change the version of the `sentient/sentient-analytics` and `sentient/sentient-analytics-python-executor` in the `docker-compose.yml` file to the {{ site.release.sentient-analytics_ver }}.

2. Execute the following commands:

```bash
docker pull sentient/sentient-analytics:{{ site.release.sentient-analytics_ver }}
docker compose stop sentient-analytics
docker compose run --rm -e UPGRADE_TRENDZ=true sentient-analytics
docker compose up -d
```
{: .copy-code}

## Troubleshooting

### DNS issues

{% include templates/troubleshooting/dns-issues.md %}

## Next steps

{% assign currentGuide = "InstallationOptions" %}{% include templates/trndz-guides-banner.md %}