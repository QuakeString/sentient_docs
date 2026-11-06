+++
title = "Getting Started with SENTIENT"
description = "Getting started with SENTIENT open-source IoT platform and simulated IoT devices"


[extra]
status = "imported"
checked = ""
source = "docs/getting-started-guides/helloworld.md"
+++
This guide demonstrates basic usage of popular SENTIENT features. You will learn how to:

- Connect devices to SENTIENT
- Push data from devices to SENTIENT
- Build real-time dashboards
- Create a Customer and assign the dashboard with them.
- Define thresholds and trigger alarms
- Set up notifications.

For simplicity, we&#39;ll visualize data from a temperature sensor.

<hr>

## Prerequisites

You will need a SENTIENT server up and running:

* **SENTIENT Cloud:** The fastest way to start with zero setup. Click for the [North America](/docs/paas/getting-started-guides/helloworld/) or [Europe](/docs/paas/eu/getting-started-guides/helloworld/) region (these links lead to a separate "Getting Started" guide for our managed service).
* **Self-Managed Installation:** Alternatively, you can manually install SENTIENT using our guides for [Windows (Docker)](/docs/user-guide/install/docker-windows/) or [Linux and MacOS (Docker)](/docs/user-guide/install/docker/).

<hr>

## Step 1. Provision device

Let&#39;s add a device that sends temperature data to SENTIENT:


1. Log in to SENTIENT and navigate to the "Devices" page of the "Entities" section.

1. Click on the "+" icon in the top right corner of the table and select "Add new device" from drop-down menu.

1. Enter a device name (e.g., "My New Device") No other changes required at this time. Click "Add".

1. A window for checking the device connection will open — we&#39;ll skip this step for now and return to connection checking in the next step.

1. Congratulations, you&#39;ve added your first device! As you add more devices, they will be added at the top of the table, as the table automatically sorts devices by their creation time, with the newest ones listed first.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-1-ce.webp" alt="Log in to SENTIENT and navigate to the &quot;Devices&quot; page of the &quot;Entities&quot; section." loading="lazy"><figcaption>Log in to SENTIENT and navigate to the "Devices" page of the "Entities" section.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-2-ce.webp" alt="Click on the &quot;+&quot; icon in the top right corner of the table and select &quot;Add new device&quot; from drop-down menu." loading="lazy"><figcaption>Click on the "+" icon in the top right corner of the table and select "Add new device" from drop-down menu.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-3-ce.webp" alt="Enter a device name (e.g., &quot;My New Device&quot;) No other changes required at this time. Click &quot;Add&quot;." loading="lazy"><figcaption>Enter a device name (e.g., "My New Device") No other changes required at this time. Click "Add".</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-4-ce.webp" alt="A window for checking the device connection will open — we&#39;ll skip this step for now and return to connection checking in the next step." loading="lazy"><figcaption>A window for checking the device connection will open — we&#39;ll skip this step for now and return to connection checking in the next step.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-5-ce.webp" alt="Congratulations, you&#39;ve added your first device! As you add more devices, they will be added at the top of the table, as the table automatically sorts devices by their creation time, with the newest ones listed first." loading="lazy"><figcaption>Congratulations, you&#39;ve added your first device! As you add more devices, they will be added at the top of the table, as the table automatically sorts devices by their creation time, with the newest ones listed first.</figcaption></figure></div>


You will also receive a notification upon adding devices. Click the bell icon (top right) to view notifications.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-6-ce.webp" alt="You will also receive a notification upon adding devices. Click the bell icon (top right) to view notifications." loading="lazy"><figcaption>You will also receive a notification upon adding devices. Click the bell icon (top right) to view notifications.</figcaption></figure></div>


[Learn more about notifications here](#step-6-alarm-notifications).

**Additional provisioning methods**
- [Bulk provisioning](/docs/user-guide/bulk-provisioning/): Import multiple devices via CSV through the UI.
- [Device provisioning](/docs/user-guide/device-provisioning/): Configure devices to self-register automatically. 
- [REST API](/docs/api/) provisioning: Manage devices programmatically through APIs.

<hr>

## Step 2. Connect device

Let&#39;s verify your device&#39;s connection to SENTIENT:


1. Click on your device, then click the "Check connectivity” button in the "Device details" window.

1. In the opened window, choose your messaging protocol and operating system. Install any necessary client tools and copy the provided command.

1. Execute the copied command in Terminal. Once telemetry data (e.g., temperature readings) is successfully published, the device status will change from "Inactive" to "Active," and you&#39;ll see the data displayed. You can now close the connectivity window.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/check-connectivity-device-1-ce.webp" alt="Click on your device, then click the &quot;Check connectivity” button in the &quot;Device details&quot; window." loading="lazy"><figcaption>Click on your device, then click the "Check connectivity” button in the "Device details" window.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/check-connectivity-device-2-ce.webp" alt="In the opened window, choose your messaging protocol and operating system. Install any necessary client tools and copy the provided command." loading="lazy"><figcaption>In the opened window, choose your messaging protocol and operating system. Install any necessary client tools and copy the provided command.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/check-connectivity-device-3-ce.webp" alt="Execute the copied command in Terminal. Once telemetry data (e.g., temperature readings) is successfully published, the device status will change from &quot;Inactive&quot; to &quot;Active,&quot; and you&#39;ll see the data displayed. You can now close the connectivity window." loading="lazy"><figcaption>Execute the copied command in Terminal. Once telemetry data (e.g., temperature readings) is successfully published, the device status will change from "Inactive" to "Active," and you&#39;ll see the data displayed. You can now close the connectivity window.</figcaption></figure></div>


<br>
Explore [SENTIENT API reference](/docs/api). Here you will find more detailed information about all supported protocols for connecting devices.

<hr>

## Step 3. Create dashboard

A dashboard in SENTIENT allows users to visualize and monitor data collected from IoT devices.

Let&#39;s create a dashboard and add three widgets to it in order to display a list of entities and their latest values, as well as show alarm signals related to the specified entity.

### Step 3.1 Create an empty dashboard

To create a new dashboard, follow these steps:


1. Navigate to the "Dashboards" page through the main menu on the left of the screen. Then, click the "+" sign in the upper right corner of the screen, and select "Create new dashboard" from the drop-down menu.

1. In the opened dialog, it is necessary to enter a dashboard title, description is optional. Click "Add".

1. After creating the dashboard, it will open automatically, and you can immediately start adding widgets to it. To save the dashboard, click "Save" button in the upper right corner.

1. Your first dashboard has been successfully created. As you continue to add new dashboards, they will appear at the top of the list. This default sorting is based on the creation timestamp.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/create-dashboard-1-ce.webp" alt="Navigate to the &quot;Dashboards&quot; page through the main menu on the left of the screen. Then, click the &quot;+&quot; sign in the upper right corner of the screen, and select &quot;Create new dashboard&quot; from the drop-down menu." loading="lazy"><figcaption>Navigate to the "Dashboards" page through the main menu on the left of the screen. Then, click the "+" sign in the upper right corner of the screen, and select "Create new dashboard" from the drop-down menu.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/create-dashboard-2-ce.webp" alt="In the opened dialog, it is necessary to enter a dashboard title, description is optional. Click &quot;Add&quot;." loading="lazy"><figcaption>In the opened dialog, it is necessary to enter a dashboard title, description is optional. Click "Add".</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/create-dashboard-3-ce.webp" alt="After creating the dashboard, it will open automatically, and you can immediately start adding widgets to it. To save the dashboard, click &quot;Save&quot; button in the upper right corner." loading="lazy"><figcaption>After creating the dashboard, it will open automatically, and you can immediately start adding widgets to it. To save the dashboard, click "Save" button in the upper right corner.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/create-dashboard-4-ce.webp" alt="Your first dashboard has been successfully created. As you continue to add new dashboards, they will appear at the top of the list. This default sorting is based on the creation timestamp." loading="lazy"><figcaption>Your first dashboard has been successfully created. As you continue to add new dashboards, they will appear at the top of the list. This default sorting is based on the creation timestamp.</figcaption></figure></div>


### Step 3.2 Add an Entities table widget

The "Entities table" widget displays a list of entities and their latest values.
The list of entities corresponds to selected devices or other entities, and filters with the ability of additional full-text search and pagination options.

To add the table widget we need to select it from the widget library. Widgets are grouped into widget bundles.
Each widget has a data source. This is how the widget "knows" what data to display.
To see the latest value of our "temperature" data that we sent during step 2, we should configure the data source.

Let&#39;s add your first widget:


1. Enter dashboard edit mode. Simply open the dashboard and click the "Edit mode" button found in the upper right corner of the screen;

1. Click the "Add widget" button at the top of the screen or click the large "Add new widget" icon in the center of the screen (if this is your first widget on this dashboard);

1. Find the "Tables" widget bundle and click on it;

1. Select the "Entities table" widget;

1. The "Add Widget" window will appear. Specify the previously created device "My New Device" as the data source in the "Device" field. The "name" key has already been added to the "Columns" section, which is responsible for the column with the device name. You need to add another column that will display the value of the "temperature" key. To do this, click "Add column" to add a new field to enter the data key;

1. Click on the newly appeared data key input field. A list of available data keys will open. Select "temperature" data key;

1. Click the "Add" button in the bottom right corner of the widget to complete adding the widget.

1. To make the widget slightly larger, simply grab the bottom right corner and drag it. Once you&#39;re happy with the new size, don&#39;t forget to click "Save" to save your changes to the dashboard.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-table-widget-0-ce.webp" alt="Enter dashboard edit mode. Simply open the dashboard and click the &quot;Edit mode&quot; button found in the upper right corner of the screen;" loading="lazy"><figcaption>Enter dashboard edit mode. Simply open the dashboard and click the "Edit mode" button found in the upper right corner of the screen;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-table-widget-1-ce.webp" alt="Click the &quot;Add widget&quot; button at the top of the screen or click the large &quot;Add new widget&quot; icon in the center of the screen (if this is your first widget on this dashboard);" loading="lazy"><figcaption>Click the "Add widget" button at the top of the screen or click the large "Add new widget" icon in the center of the screen (if this is your first widget on this dashboard);</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-table-widget-2-ce.webp" alt="Find the &quot;Tables&quot; widget bundle and click on it;" loading="lazy"><figcaption>Find the "Tables" widget bundle and click on it;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-table-widget-3-ce.webp" alt="Select the &quot;Entities table&quot; widget;" loading="lazy"><figcaption>Select the "Entities table" widget;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-table-widget-4-ce.webp" alt="The &quot;Add Widget&quot; window will appear. Specify the previously created device &quot;My New Device&quot; as the data source in the &quot;Device&quot; field. The &quot;name&quot; key has already been added to the &quot;Columns&quot; section, which is responsible for the column with the device name. You need to add another column that will display the value of the &quot;temperature&quot; key. To do this, click &quot;Add column&quot; to add a new field to enter the data key;" loading="lazy"><figcaption>The "Add Widget" window will appear. Specify the previously created device "My New Device" as the data source in the "Device" field. The "name" key has already been added to the "Columns" section, which is responsible for the column with the device name. You need to add another column that will display the value of the "temperature" key. To do this, click "Add column" to add a new field to enter the data key;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-table-widget-5-ce.webp" alt="Click on the newly appeared data key input field. A list of available data keys will open. Select &quot;temperature&quot; data key;" loading="lazy"><figcaption>Click on the newly appeared data key input field. A list of available data keys will open. Select "temperature" data key;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-table-widget-6-ce.webp" alt="Click the &quot;Add&quot; button in the bottom right corner of the widget to complete adding the widget." loading="lazy"><figcaption>Click the "Add" button in the bottom right corner of the widget to complete adding the widget.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-table-widget-7-ce.webp" alt="To make the widget slightly larger, simply grab the bottom right corner and drag it. Once you&#39;re happy with the new size, don&#39;t forget to click &quot;Save&quot; to save your changes to the dashboard." loading="lazy"><figcaption>To make the widget slightly larger, simply grab the bottom right corner and drag it. Once you&#39;re happy with the new size, don&#39;t forget to click "Save" to save your changes to the dashboard.</figcaption></figure></div>


Congratulations! You&#39;ve added your first widget.

In the "Entities table" widget, there are two columns.
The first column displays the device&#39;s name, and the second column displays the value of the "temperature" key (device telemetry).
So, each column corresponds to an added key.

Now you are able to send a new telemetry reading (as in [Step 1](#step-1-provision-device)), and it will immediately appear in the table.

### Step 3.3 Add a Chart widget

Chart widgets allow you to display time series data with customizable line charts and bar charts.

To add the chart widget we need to select it from the widget library.
Chart widget displays multiple historical values of the same data key ("temperature" in our case).
We should also configure the time window to use the chart widget.


1. Enter edit mode and click the "Add new widget" button at the top of the screen;

1. Find the "Charts" widget bundle and click on it;

1. Select the "Time series сhart" widget;

1. Specify the previously created device "My New Device" as the data source in the "Device" field. In the "Series" section, specify the data key "temperature" to start monitoring the temperature values of the device. Then, click "Add";

1. Resize the widget and apply changes. Publish different telemetry values multiple times, as in Step 2. Note that the widget displays only one minute of data by default. Click "Save" to apply changes;


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-chart-widget-1-ce.webp" alt="Enter edit mode and click the &quot;Add new widget&quot; button at the top of the screen;" loading="lazy"><figcaption>Enter edit mode and click the "Add new widget" button at the top of the screen;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-chart-widget-2-ce.webp" alt="Find the &quot;Charts&quot; widget bundle and click on it;" loading="lazy"><figcaption>Find the "Charts" widget bundle and click on it;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-chart-widget-3-ce.webp" alt="Select the &quot;Time series сhart&quot; widget;" loading="lazy"><figcaption>Select the "Time series сhart" widget;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-chart-widget-4-ce.webp" alt="Specify the previously created device &quot;My New Device&quot; as the data source in the &quot;Device&quot; field. In the &quot;Series&quot; section, specify the data key &quot;temperature&quot; to start monitoring the temperature values of the device. Then, click &quot;Add&quot;;" loading="lazy"><figcaption>Specify the previously created device "My New Device" as the data source in the "Device" field. In the "Series" section, specify the data key "temperature" to start monitoring the temperature values of the device. Then, click "Add";</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-chart-widget-5-ce.webp" alt="Resize the widget and apply changes. Publish different telemetry values multiple times, as in Step 2. Note that the widget displays only one minute of data by default. Click &quot;Save&quot; to apply changes;" loading="lazy"><figcaption>Resize the widget and apply changes. Publish different telemetry values multiple times, as in Step 2. Note that the widget displays only one minute of data by default. Click "Save" to apply changes;</figcaption></figure></div>


Congratulations! You have added the chart widget. Now you are able to send a new telemetry reading, and it will immediately appear in the chart.

You can also adjust the time interval for displaying data in the widget, change the aggregation function, and specify the grouping interval.
To do this, open the [Time window](/docs/user-guide/dashboards/#time-window) and make the necessary adjustments. Update the time window settings by clicking the "Update" button.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-1-add-chart-widget-6-ce.webp" alt="You can also adjust the time interval for displaying data in the widget, change the aggregation function, and specify the grouping interval. To do this, open the Time window and make the necessary adjustments. Update the time window settings by clicking the &quot;Update&quot; button." loading="lazy"><figcaption>You can also adjust the time interval for displaying data in the widget, change the aggregation function, and specify the grouping interval. To do this, open the Time window and make the necessary adjustments. Update the time window settings by clicking the "Update" button.</figcaption></figure></div>


### Step 3.4 Add an Alarms table widget

The alarms table widget displays alarms related to the specified entity in the certain time window.
Alarm widget is configured by specifying an entity as the alarm source, and the corresponding alarm fields.


1. Enter edit mode and click the "Add new widget" button at the top of the screen;

1. Find the "Alarm widgets" bundle and click on it;

1. Select "Alarms table" widget;

1. Specify the previously created device "My New Device" as the data source in the "Device" field. Next, we will configure the filters. All alarms have specific severities and statuses. Mark those you want to see in the widget. If none are marked, all alarms will be displayed regardless of their status or severity;

1. Congratulations! You have added the alarm widget. By default, new widgets are added one below the other, stacking downwards. Let&#39;s organize our widgets a bit to tidy up their arrangement. Drag the "Time series chart" widget to the top right corner of the dashboard to make room for the "Alarms table" widget;

1. Scroll down, find the "Alarms table" widget, and drag it over to a free spot. Adjust its size to fit your needs. After you&#39;re done tweaking, click "Save" to save the dashboard.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-4-add-alarm-widget-1-ce.webp" alt="Enter edit mode and click the &quot;Add new widget&quot; button at the top of the screen;" loading="lazy"><figcaption>Enter edit mode and click the "Add new widget" button at the top of the screen;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-4-add-alarm-widget-2-ce.webp" alt="Find the &quot;Alarm widgets&quot; bundle and click on it;" loading="lazy"><figcaption>Find the "Alarm widgets" bundle and click on it;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-4-add-alarm-widget-3-ce.webp" alt="Select &quot;Alarms table&quot; widget;" loading="lazy"><figcaption>Select "Alarms table" widget;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-4-add-alarm-widget-4-ce.webp" alt="Specify the previously created device &quot;My New Device&quot; as the data source in the &quot;Device&quot; field. Next, we will configure the filters. All alarms have specific severities and statuses. Mark those you want to see in the widget. If none are marked, all alarms will be displayed regardless of their status or severity;" loading="lazy"><figcaption>Specify the previously created device "My New Device" as the data source in the "Device" field. Next, we will configure the filters. All alarms have specific severities and statuses. Mark those you want to see in the widget. If none are marked, all alarms will be displayed regardless of their status or severity;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-4-add-alarm-widget-5-ce.webp" alt="Congratulations! You have added the alarm widget. By default, new widgets are added one below the other, stacking downwards. Let&#39;s organize our widgets a bit to tidy up their arrangement. Drag the &quot;Time series chart&quot; widget to the top right corner of the dashboard to make room for the &quot;Alarms table&quot; widget;" loading="lazy"><figcaption>Congratulations! You have added the alarm widget. By default, new widgets are added one below the other, stacking downwards. Let&#39;s organize our widgets a bit to tidy up their arrangement. Drag the "Time series chart" widget to the top right corner of the dashboard to make room for the "Alarms table" widget;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-3-4-add-alarm-widget-6-ce.webp" alt="Scroll down, find the &quot;Alarms table&quot; widget, and drag it over to a free spot. Adjust its size to fit your needs. After you&#39;re done tweaking, click &quot;Save&quot; to save the dashboard." loading="lazy"><figcaption>Scroll down, find the "Alarms table" widget, and drag it over to a free spot. Adjust its size to fit your needs. After you&#39;re done tweaking, click "Save" to save the dashboard.</figcaption></figure></div>


Now it&#39;s time to configure alarm rules and raise some alarms.

> **Note:** in this documentation, we are using a single device as a data source for the widgets. 
To use dynamic entities (for example, devices of a certain type or related to a certain asset) as data source, you should use the alias.
Alias is a reference to a single entity or a group of entities that are used in the widgets. 
You may learn more [about different aliases here](/docs/user-guide/ui/aliases/).

<hr>

## Step 4. Configure alarm rules

We will use the [alarm rules](/docs/user-guide/alarm-rules/) feature to define a rule that triggers when the temperature exceeds **25°C**.   
Alarm rules can be configured either at the **device level** or at the [device profile](/docs/user-guide/device-profiles/) level used by the target device.

> **Recommendation:** If the same rule needs to be applied to multiple devices, create it at the **Device profile** level.   
This ensures centralized alarm logic management, simplifies maintenance, and eliminates configuration duplication.

In this example, we will configure the alarm rule directly on the device "**My New Device**".

<br><b><font size="4">Step 4.1 Open the device settings</font></b>
- Go to the **Devices** page in the **Entities** section.
- Click **My New Device** to open its details.
- Navigate to the **Alarm rules** tab.
- Click the "**+**" button and select **Create new alarm rule**.

<b><font size="4">Step 4.2 Configure the General parameters</font></b>

In the **General** section, specify the **alarm type** — *High temperature* (or any other name you prefer) — which serves as both the name and the unique identifier of the alarm.

<b><font size="4">Step 4.3 Add argument</font></b>

Before defining the alarm trigger condition, you must add at least one **argument** — the data source that the rule will use.

In the **Arguments** section, click **Add argument** and fill in:
- **Entity type:** *Current entity*
- **Argument type:** *Latest telemetry*
- **Time series key:** <span class="code-light">temperature</span>
- **Argument name:** temperature
- Click **Add**.

This creates the <span class="code-light">temperature</span> variable that will be used in the alarm rule conditions.

<b><font size="4">Step 4.4 Configure the alarm trigger condition</font></b>

In the **Trigger condition** section, click **Add trigger condition**.

- **Severity:** *Critical*
- **Condition**
  - Click **Add condition**.
  - In the configuration window, click **Add argument filter** and specify:
    - **General** block:
      - **Argument:** temperature (the argument added earlier)
      - **Value type:** *Numeric*
    - **Filters** block:
      - Click **Add**
      - **Operation:** *greater than*
      - **Value source:** Static
      - **Value:** <span class="code-light">25</span>
    - Click **Add**.
  - **Type:** *Simple*
  - Click **Save**.

As a result, the alarm will trigger immediately when the temperature exceeds **25°C**.

<b><font size="4">Save the rule</font></b>

Click the **Add** button to save the new alarm creation rule.

The rule takes effect immediately after it is saved.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-4-configure-alarm-rules-1-ce.webp" alt="Go to the Devices page in the Entities section.Click My New Device to open its details, and navigate to the Alarm rules tab.Click the &quot;+&quot; button, and select Create new alarm rule." loading="lazy"><figcaption>Go to the <b>Devices</b> page in the <b>Entities</b> section.<br>Click <b>My New Device</b> to open its details, and navigate to the <b>Alarm rules</b> tab.<br>Click the "<b>+</b>" button, and select <b>Create new alarm rule</b>.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-4-configure-alarm-rules-2-ce.webp" alt="In the General section, specify the alarm type — High temperature (or any other name you prefer) — which serves as both the name and the unique identifier of the alarm." loading="lazy"><figcaption>In the <b>General</b> section, specify the <b>alarm type</b> — <i>High temperature</i> (or any other name you prefer) — which serves as both the name and the unique identifier of the alarm.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-4-configure-alarm-rules-3-ce.webp" alt="Add the argument — the data source that the rule will use when evaluating the conditions." loading="lazy"><figcaption>Add the argument — the data source that the rule will use when evaluating the conditions.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-4-configure-alarm-rules-4-ce.webp" alt="Click Add trigger condition." loading="lazy"><figcaption>Click <b>Add trigger condition</b>.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-4-configure-alarm-rules-5-ce.webp" alt="Keep the Critical severity level and click Add condition." loading="lazy"><figcaption>Keep the <b>Critical</b> severity level and click <b>Add condition</b>.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-4-configure-alarm-rules-6-ce.webp" alt="Click the Add argument filter." loading="lazy"><figcaption>Click the <b>Add argument filter</b>.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-4-configure-alarm-rules-7-ce.webp" alt="General: Argument: temperature (the argument added earlier); Value type: NumericFilters: Click Add; Operation: greater than; Value source: Static; Value: 25.Click Add." loading="lazy"><figcaption><b>General:</b> <b>Argument:</b> temperature (the argument added earlier); <b>Value type:</b> Numeric<br><b>Filters:</b> Click <b>Add</b>; <b>Operation:</b> greater than; <b>Value source:</b> Static; <b>Value:</b> 25.<br>Click <b>Add</b>.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-4-configure-alarm-rules-8-ce.webp" alt="Type: Simple.Save condition." loading="lazy"><figcaption><b>Type:</b> Simple.<br><b>Save</b> condition.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-4-configure-alarm-rules-9-ce.webp" alt="Finally, click the Add." loading="lazy"><figcaption>Finally, click the <b>Add</b>.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-4-configure-alarm-rules-10-ce.webp" alt="The new alarm rule will be created and activated." loading="lazy"><figcaption>The new alarm rule will be created and activated.</figcaption></figure></div>


We also recommend reviewing the [alarm rule configuration examples](/docs/user-guide/alarm-rules/#examples-of-alarm-rule-configurations/)

<hr>

## Step 5. Create alarm

Now that the alarm rule is active (see [Step 4](#step-4-configure-alarm-rules)), you need to send new telemetry data from the device (see [Step 2](#step-2-connect-device)) to trigger the alarm.

> **Important:** The alarm will be created only when the temperature value exceeds the threshold of 25°C defined in the alarm creation condition.

**What happens after sending telemetry**


1. As soon as a new <b>temperature</b> value goes above the threshold, a new active alarm will appear on the dashboard.

1. You can <b>acknowledge</b> and <b>clear</b> alarms using the <b>Alarm table</b> widget.

1. After the alarm is created, you will also receive a notification in the <b>Notification center</b>. Click the bell icon in the top-right corner to view the latest notifications.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-5-create-alarm-1-ce.webp" alt="As soon as a new temperature value goes above the threshold, a new active alarm will appear on the dashboard." loading="lazy"><figcaption>As soon as a new <b>temperature</b> value goes above the threshold, a new active alarm will appear on the dashboard.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-5-create-alarm-2-ce.webp" alt="You can acknowledge and clear alarms using the Alarm table widget." loading="lazy"><figcaption>You can <b>acknowledge</b> and <b>clear</b> alarms using the <b>Alarm table</b> widget.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-5-create-alarm-3-ce.webp" alt="After the alarm is created, you will also receive a notification in the Notification center. Click the bell icon in the top-right corner to view the latest notifications." loading="lazy"><figcaption>After the alarm is created, you will also receive a notification in the <b>Notification center</b>. Click the bell icon in the top-right corner to view the latest notifications.</figcaption></figure></div>


<hr>

## Step 6. Alarm notifications

The SENTIENT [Notification center](/docs/user-guide/notifications/) allows personalized notifications to end-users regarding device activities, environmental changes, or events in your IoT ecosystem, and more. 
Notifications can be delivered via email, SMS, or integrated third-party systems.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/notification-center-getting-started-1-ce.webp" alt="The SENTIENT Notification center allows sending personalized notifications to end-users. These can include notifications about device activity, changes in temperature within your environment, or other events detected in your IoT ecosystem." loading="lazy"><figcaption>The SENTIENT Notification center allows sending personalized notifications to end-users. These can include notifications about device activity, changes in temperature within your environment, or other events detected in your IoT ecosystem.</figcaption></figure></div>


Additionally, [SENTIENT Mobile Application](/docs/mobile/) provides instant push notifications directly to your smartphone, ensuring you&#39;re always informed of critical events wherever you are.

Follow [this guide](/docs/mobile/getting-started/) to install the SENTIENT mobile app and set up notifications. 

Enjoy exploring SENTIENT!

<hr>

## Step 7. Assign device and dashboard to customer

One of the most important SENTIENT features is the ability to assign Dashboards to Customers. 
You may assign different devices to different customers. Then, you may create a Dashboard(s) and assign it to multiple customers.
Each customer user will see his own devices and will not be able to see devices or any other data that belongs to a different customer.

We have already created a Device (see [Step 1](#step-1-provision-device)), and a Dashboard (see [Step 3](#step-3-create-dashboard)).
Now it&#39;s time to create a Customer and a Customer User and make sure they will have access to the device's data and the dashboard.

### Step 7.1 Create customer

Let&#39;s create a customer with the title "My New Customer". Please see the instruction below:


1. Navigate to the Customers page. Click the "+" sign to add a customer;

1. Input customer title and click "Add".

1. The new customer has been created.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-create-customer-1-ce.webp" alt="Navigate to the Customers page. Click the &quot;+&quot; sign to add a customer;" loading="lazy"><figcaption>Navigate to the Customers page. Click the "+" sign to add a customer;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-create-customer-2-ce.webp" alt="Input customer title and click &quot;Add&quot;." loading="lazy"><figcaption>Input customer title and click "Add".</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-create-customer-3-ce.webp" alt="The new customer has been created." loading="lazy"><figcaption>The new customer has been created.</figcaption></figure></div>


### Step 7.2 Assign the device to customer

Let&#39;s assign device to the customer. The customer users will have ability to read and write telemetry and send commands to devices. 


1. Open "Devices" page, then select your device to open its details;

1. Click "Assign to customer" button;

1. Select the customer to whom you want to assign the device, and then click "Assign";

1. You have changed the owner of the device. In the "Customer" column, you can see the owners name of the device;


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-device-to-customer-1-ce.webp" alt="Open &quot;Devices&quot; page, then select your device to open its details;" loading="lazy"><figcaption>Open "Devices" page, then select your device to open its details;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-device-to-customer-2-ce.webp" alt="Click &quot;Assign to customer&quot; button;" loading="lazy"><figcaption>Click "Assign to customer" button;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-device-to-customer-3-ce.webp" alt="Select the customer to whom you want to assign the device, and then click &quot;Assign&quot;;" loading="lazy"><figcaption>Select the customer to whom you want to assign the device, and then click "Assign";</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-device-to-customer-4-ce.webp" alt="You have changed the owner of the device. In the &quot;Customer&quot; column, you can see the owners name of the device;" loading="lazy"><figcaption>You have changed the owner of the device. In the "Customer" column, you can see the owners name of the device;</figcaption></figure></div>


Make sure that the device is assigned to your customer.


1. Navigate to "Customers" page to make sure that the device is assigned to your customer. Find your customer in the list of customers and then click on the "Manage customer devices" icon;

1. The device is with your client.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-device-to-customer-5-ce.webp" alt="Navigate to &quot;Customers&quot; page to make sure that the device is assigned to your customer. Find your customer in the list of customers and then click on the &quot;Manage customer devices&quot; icon;" loading="lazy"><figcaption>Navigate to "Customers" page to make sure that the device is assigned to your customer. Find your customer in the list of customers and then click on the "Manage customer devices" icon;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-device-to-customer-6-ce.webp" alt="The device is with your client." loading="lazy"><figcaption>The device is with your client.</figcaption></figure></div>


You can make the customer the owner of the device during its creation stage. To do this, follow this steps:


1. Click on the "+" icon in the top right corner of the table and then select "Add new device" from drop-down menu;

1. Input device name (for example, "Thermostat") and select the customer in the "Assign to customer" field to whom you want to assign the new device. Then, click "Add";

1. Close check connectivity window;

1. The device has been created, and it immediately belongs to the selected customer.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-device-to-customer-8-ce.webp" alt="Click on the &quot;+&quot; icon in the top right corner of the table and then select &quot;Add new device&quot; from drop-down menu;" loading="lazy"><figcaption>Click on the "+" icon in the top right corner of the table and then select "Add new device" from drop-down menu;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-device-to-customer-9-ce.webp" alt="Input device name (for example, &quot;Thermostat&quot;) and select the customer in the &quot;Assign to customer&quot; field to whom you want to assign the new device. Then, click &quot;Add&quot;;" loading="lazy"><figcaption>Input device name (for example, "Thermostat") and select the customer in the "Assign to customer" field to whom you want to assign the new device. Then, click "Add";</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-device-to-customer-10-ce.webp" alt="Close check connectivity window;" loading="lazy"><figcaption>Close check connectivity window;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-device-to-customer-11-ce.webp" alt="The device has been created, and it immediately belongs to the selected customer." loading="lazy"><figcaption>The device has been created, and it immediately belongs to the selected customer.</figcaption></figure></div>


### Step 7.3 Assign the dashboard to customer

Let&#39;s share our dashboard with the customer. The customer users will have read-only access to the dashboard. 


1. Open "Dashboards" page. Mark your dashboard and click the "Assign dashboards" icon;

1. Mark "My New Customer" and click "Assign";

1. Navigate to the "Customers" page. Click "Manage customer dashboards" icon for "My New Customer";

1. "My New Dashboard" is assigned to your customer.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-dashboard-to-customer-3-ce.webp" alt="Open &quot;Dashboards&quot; page. Mark your dashboard and click the &quot;Assign dashboards&quot; icon;" loading="lazy"><figcaption>Open "Dashboards" page. Mark your dashboard and click the "Assign dashboards" icon;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-dashboard-to-customer-4-ce.webp" alt="Mark &quot;My New Customer&quot; and click &quot;Assign&quot;;" loading="lazy"><figcaption>Mark "My New Customer" and click "Assign";</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-dashboard-to-customer-5-ce.webp" alt="Navigate to the &quot;Customers&quot; page. Click &quot;Manage customer dashboards&quot; icon for &quot;My New Customer&quot;;" loading="lazy"><figcaption>Navigate to the "Customers" page. Click "Manage customer dashboards" icon for "My New Customer";</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-71-assign-dashboard-to-customer-6-ce.webp" alt="&quot;My New Dashboard&quot; is assigned to your customer." loading="lazy"><figcaption>"My New Dashboard" is assigned to your customer.</figcaption></figure></div>


### Step 7.4 Create customer user

Now, let&#39;s create a user that will belong to the customer and will have `read-only` access both to the dashboard and the device.
You may optionally configure the dashboard to appear just after user logs in to the platform&#39;s web UI.


1. Navigate to "Customers" page. Find your customer in the list of customers and then click on the "Manage customer users" icon;

1. Click the "Add user" icon in the top right corner of the table;

1. Specify email that you will use to login as a customer user and click "Add";

1. Copy the activation link and save it to a safe place. You will use it later to set the password. Click "OK";

1. Click on the created user to open details. Click "pencil" icon to enter edit mode;

1. Select your "My New Dashboard" as default dashboard and check "Always fullscreen". Apply changes.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-create-customer-user-1-ce.webp" alt="Navigate to &quot;Customers&quot; page. Find your customer in the list of customers and then click on the &quot;Manage customer users&quot; icon;" loading="lazy"><figcaption>Navigate to "Customers" page. Find your customer in the list of customers and then click on the "Manage customer users" icon;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-create-customer-user-2-ce.webp" alt="Click the &quot;Add user&quot; icon in the top right corner of the table;" loading="lazy"><figcaption>Click the "Add user" icon in the top right corner of the table;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-create-customer-user-3-ce.webp" alt="Specify email that you will use to login as a customer user and click &quot;Add&quot;;" loading="lazy"><figcaption>Specify email that you will use to login as a customer user and click "Add";</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-create-customer-user-4-ce.webp" alt="Copy the activation link and save it to a safe place. You will use it later to set the password. Click &quot;OK&quot;;" loading="lazy"><figcaption>Copy the activation link and save it to a safe place. You will use it later to set the password. Click "OK";</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-create-customer-user-6-ce.webp" alt="Click on the created user to open details. Click &quot;pencil&quot; icon to enter edit mode;" loading="lazy"><figcaption>Click on the created user to open details. Click "pencil" icon to enter edit mode;</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-create-customer-user-7-ce.webp" alt="Select your &quot;My New Dashboard&quot; as default dashboard and check &quot;Always fullscreen&quot;. Apply changes." loading="lazy"><figcaption>Select your "My New Dashboard" as default dashboard and check "Always fullscreen". Apply changes.</figcaption></figure></div>


### Step 7.5 Activate customer user

Finally, log in to SENTIENT as a customer user.


1. Paste the previously copied link into a new browser tab and press the "Enter" key. Now create a password by entering it twice and clicking "Create Password".

1. You are now logged in as a customer user. You may browse the data and acknowledge/clear alarms.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-5-activate-customer-user-1-ce.webp" alt="Paste the previously copied link into a new browser tab and press the &quot;Enter&quot; key. Now create a password by entering it twice and clicking &quot;Create Password&quot;." loading="lazy"><figcaption>Paste the previously copied link into a new browser tab and press the "Enter" key. Now create a password by entering it twice and clicking "Create Password".</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-7-5-activate-customer-user-2-ce.webp" alt="You are now logged in as a customer user. You may browse the data and acknowledge/clear alarms." loading="lazy"><figcaption>You are now logged in as a customer user. You may browse the data and acknowledge/clear alarms.</figcaption></figure></div>


<hr>

## Next steps


<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word. 
If you have any questions about this sample, please [contact us](/docs/contact-us/).
