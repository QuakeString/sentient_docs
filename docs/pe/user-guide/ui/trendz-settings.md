---
layout: docwithnav-pe
title: SENTIENT ANALYTICS settings
description: SENTIENT IoT platform SENTIENT ANALYTICS settings

sentient-analytics-settings:
  0:
    image: /images/user-guide/ui/sentient-analytics/sentient-analytics-settings.png
    title: 'SENTIENT ANALYTICS settings page.'

sentient-analytics-settings-sync-status:
  0:
    image: /images/user-guide/ui/sentient-analytics/sentient-analytics-settings-sync-status-1.png
    title: 'If SENTIENT ANALYTICS synchronization is successful, you will see: <b>Synchronization completed successfully</b>.'
  1:
    image: /images/user-guide/ui/sentient-analytics/sentient-analytics-settings-sync-status-2.png
    title: 'If there are issues, an error message with explanations will be displayed.'

---

* TOC
{:toc}

On the **SENTIENT ANALYTICS Settings** page, you can configure the connection to the [SENTIENT ANALYTICS add-on](/docs/sentient-analytics/what-is-sentient-analytics).

## Prerequisites

* SENTIENT ANALYTICS addon should be activated for SENTIENT instance on which you want to use SENTIENT ANALYTICS. You can find out how to activate it [here](/docs/sentient-analytics/activation/self-managed).
* SENTIENT ANALYTICS should be installed and accessible from SENTIENT. You can find out how to install SENTIENT ANALYTICS [here](/docs/sentient-analytics/install/installation-options).

## How to Access

* Log in to SENTIENT as a System Administrator.
* Click **SENTIENT ANALYTICS settings** tab in the left menu.

{% include images-gallery.html imageCollection="sentient-analytics-settings" %}

## SENTIENT ANALYTICS Configuration

Here you can set up **SENTIENT ANALYTICS Configuration**:
* **SENTIENT ANALYTICS Internal URL** - URL used by SENTIENT to communicate with SENTIENT ANALYTICS.
* **SENTIENT Internal URL** - URL used by SENTIENT ANALYTICS to communicate with SENTIENT.

### Examples

Url examples for different installation types:

* **Ubuntu / Windows / CentOS / RHEL (SENTIENT ANALYTICS and SENTIENT installed on the same machine)**:
  - SENTIENT ANALYTICS Internal URL - `http://localhost:8888` 
  - SENTIENT Internal URL - `http://localhost:8080`

* **Docker (SENTIENT ANALYTICS and SENTIENT are in the same docker compose files)**:
  - SENTIENT ANALYTICS Internal URL - `http://sentient-analytics:8888`
  - SENTIENT Internal URL - `http://sentient-pe:8080`

* **Kubernetes (SENTIENT and SENTIENT ANALYTICS are in the same cluster)**:
  - SENTIENT ANALYTICS Internal URL - `http://sentient-analytics-app:8888`
  - SENTIENT Internal URL - `http://tb-node:8080`

If SENTIENT ANALYTICS and SENTIENT are unreachable for each other in the private network, you can use your public URLs. For example, if SENTIENT and SENTIENT ANALYTICS under the same domain **mydomain**:
  - SENTIENT ANALYTICS Internal URL - `https://mydomain`
  - SENTIENT Internal URL - `https://mydomain`

## Actions

You can do the next **Actions** on this page:

* **Save Configuration** - Saves the URLs entered in the text boxes for SENTIENT ANALYTICS and SENTIENT.
* **Retry Discovery** - Initiates synchronization with SENTIENT ANALYTICS using the **saved configuration**.
* **Retry Healthcheck** - (Visible only if SENTIENT ANALYTICS is synced with SENTIENT) Checks if the SENTIENT ANALYTICS sync contains any errors at the current moment.

You can check sync result in the header of this page: 
* If SENTIENT ANALYTICS synchronization is successful, you will see: **Synchronization completed successfully**.
* If there are issues, an error message with explanations will be displayed.

{% include images-gallery.html imageCollection="sentient-analytics-settings-sync-status" %}
