---
layout: docwithnav-sentient-analytics
title: Use New Metrics in SENTIENT 
description: Step-by-step guide to use new Metrics in SENTIENT

calculation-create:
  0:
    image: /images/sentient-analytics/metric/use-in-sentient/calculation-create-1.png
    title: "Click <b>Save Calculation</b>."
  1:
    image: /images/sentient-analytics/metric/use-in-sentient/calculation-create-2.png
    title: "Specify the following parameters: <b>Calculation Name</b> and <b>Calculation Key</b>"
  2:
    image: /images/sentient-analytics/metric/use-in-sentient/calculation-create-3.png
    title: "Click <b>Save</b>"
  3:
    image: /images/sentient-analytics/metric/use-in-sentient/calculation-create-4.png
    title: "The calculation field appears in the <b>Calculation</b> folder."
  4:
    image: /images/sentient-analytics/metric/use-in-sentient/calculation-create-5.png
    title: "The calculation field appears in the <b>Calculation</b> folder."

calculation-parameters:
  0:
    image: /images/sentient-analytics/metric/use-in-sentient/calculation-parameters-1.png
    title: "Before saving telemetry to SENTIENT, verify <b>Grouping Interval</b>, <b>Aggregation</b> and <b>Time</b>."
  1:
    image: /images/sentient-analytics/metric/use-in-sentient/calculation-parameters-2.png
    title: "Click <b>Save Field</b> to apply changes."
  2:
    image: /images/sentient-analytics/metric/use-in-sentient/calculation-parameters-3.png
    title: "Click <b>save</b>."
  3:
    image: /images/sentient-analytics/metric/use-in-sentient/calculation-parameters-4.png
    title: "You will be prompted to enable the calculation field (run refresh task). You can do it right away or later. The process of running the refresh task is described in another article."

calculation-reprocess:
  0:
    image: /images/sentient-analytics/metric/use-in-sentient/reprocess-task-1.png
    title: "Open the <b>Tasks</b> tab and click <b>Run Reprocess Task</b> button."
  1:
    image: /images/sentient-analytics/metric/use-in-sentient/reprocess-task-2.png
    title: "Select a time range for reprocessing."
  2:
    image: /images/sentient-analytics/metric/use-in-sentient/reprocess-task-3.png
    title: "Choose items to run the job on (you can apply the same calculation to all entities with the same entity profile)."
  3:
    image: /images/sentient-analytics/metric/use-in-sentient/reprocess-task-4.png
    title: "Click <b>Run</b> button."

calculation-refresh:
  0:
    image: /images/sentient-analytics/metric/use-in-sentient/refresh-task-1.png
    title: "Click the <b>Jobs</b> button."
  1:
    image: /images/sentient-analytics/metric/use-in-sentient/refresh-task-2.png
    title: "Enable <b>calculation result saving</b>."
  2:
    image: /images/sentient-analytics/metric/use-in-sentient/refresh-task-3.png
    title: "Set the <b>start date</b> (from which data will be saved)."
  3:
    image: /images/sentient-analytics/metric/use-in-sentient/refresh-task-4.png
    title: "Define the <b>frequency</b> (how often the job runs)."
  4:
    image: /images/sentient-analytics/metric/use-in-sentient/refresh-task-5.png
    title: "Choose the target items (entities with the same entity profile) for automatic updates."
  5:
    image: /images/sentient-analytics/metric/use-in-sentient/refresh-task-6.png
    title: "Click <b>Save</b> button."
  6:
    image: /images/sentient-analytics/metric/use-in-sentient/refresh-task-7.png
    title: "Once the refresh job is set up, you will see the <b>Enabled</b> status next to the calculation name.  "

use-alarms:
  0:
    image: /images/sentient-analytics/metric/use-in-sentient/use-alarms-1.png
    title: "Open the entity profile where the calculation is created."
  1:
    image: /images/sentient-analytics/metric/use-in-sentient/use-alarms-2.png
    title: "Navigate to <b>Alarm Rules</b> and toggle <b>Edit mode</b>."
  2:
    image: /images/sentient-analytics/metric/use-in-sentient/use-alarms-3.png
    title: "Click <b>Add alarm rule</b> and set up create and clear alarm rules."
  3:
    image: /images/sentient-analytics/metric/use-in-sentient/use-alarms-4.png
    title: "Click <b>Apply changes</b>."
  4:
    image: /images/sentient-analytics/metric/use-in-sentient/use-alarms-5.png
    title: "Alarm rules are set up."
  5:
    image: /images/sentient-analytics/metric/use-in-sentient/use-alarms-6.png
    title: "Alarm was created by alarm rule."

---

* TOC
{:toc}

All metrics created with Metric Explorer can be integrated into SENTIENT. They can be used wherever telemetry is supported:

* Visualizations
* Rule Engine
* Alarm Profiles

SENTIENT ANALYTICS allows you to automatically save metrics as telemetry to SENTIENT or generate metrics from historical data and store them as telemetry.
In this guide, we explore how to configure automatic saving of metrics to SENTIENT and how to use this telemetry in SENTIENT.

## Save to SENTIENT

Setting up saving a metric to SENTIENT is divided into 3 parts:

* Create a calculation field: an entity that supports telemetry save to SENTIENT.
* Run a reprocess task to process historical data.
* Run a refresh task to automatically update telemetry.

### Create Calculation Field

You can create a calculation field from a metric by clicking **Save Calculation**.

Specify the following parameters:

1. **Calculation Name** – the name displayed in SENTIENT ANALYTICS.
2. **Calculation Key** – the telemetry key used in SENTIENT (prefixed with `_ECD_`).

**Example:**

If you save a calculation named **Energy Consumption Rate** with the key **energy_consumption_rate**:

1. SENTIENT ANALYTICS will show a new field called *Energy Consumption Rate*.
2. Telemetry will be saved in SENTIENT with the key `_ECD_energy_consumption_rate` (once refresh and reprocess jobs are configured).

Then click **Save** — after that, the calculation field appears in the **Calculation** folder.

{% include images-gallery.html imageCollection="calculation-create" %}

Before saving telemetry to SENTIENT, verify the following parameters:

1. **Grouping Interval** – defines how data is aggregated (e.g., *HOUR* means one point per hour in SENTIENT).
2. **Aggregation** – specifies how multiple values in the same interval are combined (e.g., *SUM* aggregates values within the same hour).
3. **Time** – defines the time range used by refresh jobs (e.g., *Last 7 Days* for daily updates).

**Recommended time settings:**

* **Today** – for minute or hourly jobs.
* **Last 7 Days** – for daily jobs.
* **Last 14 Days** – for weekly jobs.
* **Last 3 Months** – for monthly jobs.

You can also adjust additional parameters as needed. Read more about the calculation field interface [here](/docs/sentient-analytics/calculations/overview/).

Click **Save Field** and confirm saving by clicking the **Save** button to apply changes.  
You will be prompted to enable the calculation field (run refresh task). You can do it right away or later.  
The process of running the refresh task is described in another article.

{% include images-gallery.html imageCollection="calculation-create" %}

### Run Reprocess Task

Once the calculation field is created and all parameters are set up, you can run a **Reprocess Job** to save historical 
data to SENTIENT.

Steps:

1. Open the **Tasks** tab.
2. Click **Run Reprocess Task** button. 
3. Select a time range for reprocessing. 
4. Choose items to run the job on (you can apply the same calculation to all entities with the same entity profile).
5. Click **Run** button.

After completion, the telemetry will appear in SENTIENT with the appropriate key.

{% include images-gallery.html imageCollection="calculation-reprocess" %}

Read more about reprocess task [here](/docs/sentient-analytics/calculations/save-to-sentient).

### Run Refresh Task

You can automate telemetry updates using a **Refresh Job**.

Steps:

1. Click the **Jobs** button.
2. Enable **calculation result saving**.
3. Set the **start date** (from which data will be saved).
4. Define the **frequency** (how often the job runs).
5. Choose the target items (entities with the same entity profile) for automatic updates.
6. Click **Save** button.

Once the refresh job is set up, you will see the **Enabled** status next to the calculation name.  
From now on, telemetry will update automatically at the specified frequency for the selected items.

{% include images-gallery.html imageCollection="calculation-refresh" %}

Read more about refresh task [here](/docs/sentient-analytics/calculations/save-to-sentient).

## Use in SENTIENT

Once the calculation field, refresh job, and reprocess job are configured,
the generated telemetry remains continuously updated in SENTIENT.

You can now use the metric in SENTIENT.

### Automatic Alarm Creation

Since the telemetry exists in SENTIENT, you can create alarms based on it:

1. Open the entity profile where the calculation is created.
2. Navigate to **Alarm Rules** and toggle **Edit mode**.
3. Click **Add alarm rule** and set up create and clear alarm rules.
4. Click **Apply changes**.

**Example:** You can create a metric that calculates deviations from the average temperature for sensors in a building.  
If the deviation exceeds a threshold, an alarm will be triggered. This can detect device overheating or events such as a
forgotten open window or broken refrigerator.

In this example, we created an alarm rule that triggers alarms when the absolute temperature deviation is greater than 
10 and clears them when it is not. The alarm type is **"Abnormal Temperature"** and the severity is **"Warning"**.

Whenever the calculation refresh produces values that meet the alarm conditions, an alert will be triggered.

{% include images-gallery.html imageCollection="use-alarms" %}

### SENTIENT ANALYTICS Visualizations

Visualize the generated metric using any SENTIENT ANALYTICS widget, such as a line chart, heatmap, or state view
(from the Range Analysis tab). You can also share the view with SENTIENT.

Read about SENTIENT ANALYTICS Visualizations [here](/docs/sentient-analytics/visualizations-overview).

Read about how to share SENTIENT ANALYTICS Views with SENTIENT [here](/docs/sentient-analytics/embed-visuals).

### Predict Future Values

You can use SENTIENT ANALYTICS **Prediction Models** to forecast future values of the generated metric.
You can then visualize them and share this view with SENTIENT. 

Learn more about prediction models [here](/docs/sentient-analytics/prediction).

### Detect Anomalies

You can detect anomalies or outages in the generated metric using **SENTIENT ANALYTICS Anomaly Models**.
If an anomaly is found, you can set up automatic alarm creation. 

Learn more about anomaly detection [here](/docs/sentient-analytics/anomaly/overview).

## Next Steps

{% assign currentGuide = "MetricExplorer" %}{% include templates/trndz-guides-banner.md %}
