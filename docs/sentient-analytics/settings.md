---
layout: docwithnav-sentient-analytics
assignees:
- vparomskiy
title: SENTIENT ANALYTICS Settings
description: SENTIENT ANALYTICS Settings Description
---

* TOC
{:toc}

To access settings, go to the **Settings** page by clicking the **“Settings”** button in the bottom-left corner of the screen.

![Settings Navigation](/images/sentient-analytics/signing-key-1.png)

## System

### Import / Export

To migrate data from one SENTIENT ANALYTICS instance to another, use the built-in **Import/Export** mechanism.

You can export and import the following:

- Business Entities and their Fields
- View Configurations and View Collections
- Calculation Fields
- Prediction Models
- Anomaly Models and Anomalies
- AI Assistant Chats and Messages
- Prompts
- Tasks
 
**Exporting**

Just click the **Export** button—no additional steps are needed.  
The file will be downloaded automatically.

**Importing**

Click the **Import** button, choose the previously exported file, and configure the **Skip duplicates** option:
- **True** – Duplicate items in the import file will be ignored.
- **False** – Duplicate items will cause import errors.

Once ready, click **Import Configuration**. If successful, a confirmation message will appear.

**Limitations**
- Migration between **different SENTIENT ANALYTICS versions** is not supported.
- Migration between **different tenants** is not supported.

### Cache Management

This section allows you to manage various cache layers used in SENTIENT ANALYTICS, such as clearing local or telemetry cache.  
For more details, see the [Cache Settings documentation](/docs/sentient-analytics/cache-settings).

### External Data Source

Here you can configure and manage external SQL data sources and integrate them with SENTIENT ANALYTICS views.  
Learn more in the [external datasource guide](/docs/sentient-analytics/mix-sql-datasource).

## AI Settings

Here it's possible to configure the AI Model for the next features:

* [Metric Explorer](/docs/sentient-analytics/metric/overview)
* [View AI Assistant](/docs/sentient-analytics/ai-assistance-overview)
* [AI Widget Summary](/docs/sentient-analytics/ai-widget-summary)

You can learn how to configure AI Setting [here](/docs/sentient-analytics/custom-ai-model-configuration/).

## White Labeling

You can customize the SENTIENT ANALYTICS user interface (logo, colors, labels) to reflect your brand identity.  
Refer to the [White Labeling documentation](/docs/sentient-analytics/white-labeling) for full configuration options.

## General (Deprecated)

This tab is available only if SENTIENT ANALYTICS is connected to SENTIENT 4.2.1 or older.

### Signing Key

For the application to function properly, it must authenticate with SENTIENT on behalf of a user. This is required
for background operations such as:

- Sending generated telemetry
- Fetching data for continuous prediction model fitting and forecasting

Storing user credentials in application memory is not secure. Instead, SENTIENT ANALYTICS supports a secure mechanism using a
**JWT signing key**, which should be stored in configuration files. It is expected that SENTIENT ANALYTICS is installed on a
secured server (as is SENTIENT and similar systems).

You can alternatively store the signing key in the SENTIENT ANALYTICS database automatically, but this method is **not recommended** due to security concerns.

An indicator in the settings shows whether the signing key is set and valid.

**How to Check Your Signing Key**

Scroll to the bottom of the **Settings** page to find the **Signing Key** panel. You will see one of two options:

- **The signing key is not valid (not set or expired)**  
  ![Signing Key Invalid](/images/sentient-analytics/signing-key-2.png)

- **The signing key is valid**  
  ![Signing Key Valid](/images/sentient-analytics/signing-key-3.png)

**Setting the Signing Key**

Follow these steps to configure the signing key:

1. **Log in to SENTIENT as a System Administrator**  
   ![Login](/images/sentient-analytics/signing-key-4.png)

2. Go to **Security → General**  
   ![Security General Page](/images/sentient-analytics/signing-key-5.png)

3. Scroll to the **JWT Security Settings** section  
   ![JWT Security](/images/sentient-analytics/signing-key-6.png)

4. Copy the value from the **Signing key** field.

**Installation-specific Instructions**
- *Ubuntu Installation*

    1. SSH into the server running SENTIENT ANALYTICS.

    2. Open the SENTIENT ANALYTICS configuration file:

       ```bash
       sudo nano /etc/sentient-analytics/conf/sentient-analytics.conf
       ```
       {: .copy-code}

    3. Add the signing key to the end of the file:

       ```bash
       export JWT_TOKEN_SIGNING_KEY=<signing-key>
       ```
       {: .copy-code}
       ![Ubuntu Signing Key](/images/sentient-analytics/signing-key-7.png)

    4. Save the file and restart the SENTIENT ANALYTICS service.


- *Docker Compose Installation*
    1. Open your `docker-compose.yml` file.

    2. Add a new environment variable under the SENTIENT ANALYTICS service:

       ```yaml
       environment:
         - JWT_TOKEN_SIGNING_KEY=<signing-key>
       ```
       {: .copy-code}
       ![Docker Signing Key](/images/sentient-analytics/signing-key-8.png)

    3. Save the file and restart the SENTIENT ANALYTICS container.

### SENTIENT ANALYTICS Widget Bundle

Uploading the SENTIENT ANALYTICS Widget Bundle is **required** to enable view sharing from SENTIENT ANALYTICS to SENTIENT dashboards.  
*(Learn how to use widgets after installation [here](/docs/sentient-analytics/embed-visuals))*

In the **SENTIENT ANALYTICS Widget Bundle** section, you’ll see one of the following status indicators:

- **Not installed** – Bundle is missing.
- **Update required** – A newer version is available.
- **Latest version installed** – You’re good to go.
- **Bundle is invalid** – The current bundle is corrupted or incomplete.

**Action Steps:**

- If status is **Latest version installed** – no action is needed.
- For other statuses, click the **Upload bundle** button:
    - If not installed - uploads the bundle.
    - If outdated - updates it to the latest version.

### SENTIENT ANALYTICS JS Summary Module

Uploading the SENTIENT ANALYTICS JS Summary Module is **recommended** for configuring AI Widget Summaries across SENTIENT widgets.  
*(Learn how to configure AI Widget Summaries [here](/docs/sentient-analytics/ai-widget-summary))*

Check the status under the **SENTIENT ANALYTICS JS Summary Module** section:

- **Not installed** – Module is missing.
- **Update required** – A newer version is available.
- **Latest version installed** – No action needed.

**Action Steps:**

- If status is **Latest version installed** – you’re done.
- Otherwise, click the **Upload Module** button:
    - If not installed - uploads the module.
    - If outdated - updates it.
