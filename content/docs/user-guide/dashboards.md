+++
title = "Working with IoT dashboards"
description = "IoT dashboards using SENTIENT"
aliases = ["/docs/user-guide/ui/dashboards/"]

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/dashboards.md"
+++
<div class="st-callout info">


Before proceeding with this guide, it&#39;s recommended that you follow [Getting Started](/docs/getting-started-guides/helloworld/) guide to become familiar with SENTIENT devices and widgets. This will enhance your learning experience and understanding of the concepts presented here.


</div>


## Introduction

SENTIENT offers a powerful feature – the ability to create and customize interactive visualizations, also known as dashboards. These dashboards are instruments for monitoring and managing your data and devices efficiently.
With SENTIENT dashboards, users can adapt interfaces to their specific needs, making it easier than ever to inspect their IoT devices and data. What's brilliant is that each dashboard can be populated with numerous widgets, offering flexibility and customization.
These dashboards aren't limited to a single data source; they can display data from various entities, including devices, assets, and more. Plus, you can assign dashboards to specific Customers, ensuring that the right individuals or teams have access to the data they need.


![image](/images/user-guide/dashboards/overview/dashboard-introduction-ce.webp)


Dashboards in SENTIENT provide users with the following capabilities:

 - **Data Visualization**: Users can create various widgets such as charts, graphs, tables, and more to visualize data obtained from connected devices. This enables operators and analysts to easily analyze information and track device statuses.
 - **Device Management**: Dashboards can be used to perform management operations on devices, such as turning devices on or off, changing parameters, and so on. Users can set actions and respond to real-time data from devices.
 - **Interactivity**: Dashboards can be designed with interactive elements such as buttons, switches, allowing users to interact with devices and data.
 - **Display Customization**: Users can customize the arrangement and size of widgets, choose color palettes, fonts, and other visualization aspects to create a user-friendly and informative interface.
 - **Role-Based Access**: SENTIENT allows controlling access to dashboards with different levels of privileges based on user [roles](/docs/user-guide/rbac/). This ensures data security and confidentiality.


This guide covers main concepts and various dashboard settings.

## Create new dashboard

To add a new dashboard, you should:


1. Login to your SENTIENT instance and navigate to the "Dashboards" page through the main menu on the left of the screen. Then, click the "+" sign in the upper right corner of the screen, and select "Create new dashboard" from the drop-down menu;

1. In the opened dialog, it is necessary to enter a dashboard title, description is optional. Click "Add";

1. Once you have created the dashboard, it will be automatically opened. Save it by clicking the "Save" button in the upper right corner.

1. Your first dashboard has been successfully created. As you continue to add new dashboards, they will appear at the top of the list. This default sort is based on the creation timestamp.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/create-dashboard-1-ce.webp" alt="Login to your SENTIENT instance and navigate to the &quot;Dashboards&quot; page through the main menu on the left of the screen. Then, click the &quot;+&quot; sign in the upper right corner of the screen, and select &quot;Create new dashboard&quot; from the drop-down menu;" loading="lazy"><figcaption>Login to your SENTIENT instance and navigate to the "Dashboards" page through the main menu on the left of the screen. Then, click the "+" sign in the upper right corner of the screen, and select "Create new dashboard" from the drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/create-dashboard-2-ce.webp" alt="In the opened dialog, it is necessary to enter a dashboard title, description is optional. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the opened dialog, it is necessary to enter a dashboard title, description is optional. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/create-dashboard-3-ce.webp" alt="Once you have created the dashboard, it will be automatically opened. Save it by clicking the &quot;Save&quot; button in the upper right corner." loading="lazy"><figcaption>Once you have created the dashboard, it will be automatically opened. Save it by clicking the "Save" button in the upper right corner.</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/create-dashboard-4-ce.webp" alt="Your first dashboard has been successfully created. As you continue to add new dashboards, they will appear at the top of the list. This default sort is based on the creation timestamp." loading="lazy"><figcaption>Your first dashboard has been successfully created. As you continue to add new dashboards, they will appear at the top of the list. This default sort is based on the creation timestamp.</figcaption></figure></div>


## Dashboard toolbar

Before starting working with a dashboard, get familiar with its interface to understand which features are responsible for what actions.

The dashboard toolbar allows you to 
[add new widgets](#add-new-widget),
manage [states](/docs/user-guide/dashboards/#states),
[layouts](/docs/user-guide/dashboards/#layouts),
[settings](/docs/user-guide/dashboards/#settings),
[aliases](/docs/user-guide/dashboards/#entity-aliases),
[filters](/docs/user-guide/dashboards/#filters),
[version control](/docs/user-guide/version-control/), and configure [time window](/docs/user-guide/dashboards/#time-window) using the corresponding icons in the toolbar.

Some of these icons (states, layout, settings, entity aliases, filters, version control, add new widget) are visible only in the "Edit" mode. All other icons are visible in both "View" and "Edit" modes.
You can hide these icons or configure the toolbar to be minimized by default using [settings](/docs/user-guide/dashboards/#settings).


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-toolbar-view-mode-ce.webp" alt="Dashboard toolbar in view mode." loading="lazy"><figcaption>Dashboard toolbar in view mode.</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-toolbar-edit-mode-ce.webp" alt="Dashboard toolbar in edit mode." loading="lazy"><figcaption>Dashboard toolbar in edit mode.</figcaption></figure></div>


### Edit mode

To enter dashboard edit mode, simply open the dashboard you wish to edit and click the "Edit mode" button found in the upper right corner of the screen.

Once you've switched to edit mode, you access the dashboard toolbar to add new elements and access controls. 
Don't forget to save your changes using the "Save" button, or if you decide to discard any unsaved edits, you can do so by clicking the "Cancel" button.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-settings-edit-mode-1-ce.webp" alt="To enter dashboard edit mode, simply open the dashboard you wish to edit and click the &quot;Edit mode&quot; button found in the upper right corner of the screen;" loading="lazy"><figcaption>To enter dashboard edit mode, simply open the dashboard you wish to edit and click the "Edit mode" button found in the upper right corner of the screen;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-settings-edit-mode-2-ce.webp" alt="Click &quot;Save&quot; button to save the dashboard or click &quot;Cancel&quot; button to rollback all unsaved changes." loading="lazy"><figcaption>Click "Save" button to save the dashboard or click "Cancel" button to rollback all unsaved changes.</figcaption></figure></div>


### Add new widget

All IoT dashboards are constructed using SENTIENT widgets.
A widget is an element that displays a specific type of information or functionality on a dashboard.
Widgets are used to visualize data, remote device control, alarms management, and display static custom HTML content.

To add a widget to a dashboard, you should:


1. Open your dashboard and switch to <b>Edit mode</b>;

1. Click the <b>+ Add widget</b> at the top of the screen. If this is your first widget on the dashboard, you can also click <b>Add new widget</b> in the center of the screen to open the Widget bundle dialog;

1. Choose a <b>widget bundle</b> (for example, <b>Charts</b>). To quickly find your desired widget, use the search bar by clicking the magnifying glass icon and entering the widget&#39;s name;

1. Select a widget (for example, <b>Time series chart</b>) to open the <b>Add widget</b> dialog;

1. Specify the <b>data source</b>, add at least one <b>data key</b>, and click <b>Add</b>. Then <b>Apply changes</b>.

1. The widget is now created.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-1-ce.webp" alt="Open your dashboard and switch to Edit mode;" loading="lazy"><figcaption>Open your dashboard and switch to <b>Edit mode</b>;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-2-ce.webp" alt="Click the + Add widget at the top of the screen. If this is your first widget on the dashboard, you can also click Add new widget in the center of the screen to open the Widget bundle dialog;" loading="lazy"><figcaption>Click the <b>+ Add widget</b> at the top of the screen. If this is your first widget on the dashboard, you can also click <b>Add new widget</b> in the center of the screen to open the Widget bundle dialog;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-3-ce.webp" alt="Choose a widget bundle (for example, Charts). To quickly find your desired widget, use the search bar by clicking the magnifying glass icon and entering the widget&#39;s name;" loading="lazy"><figcaption>Choose a <b>widget bundle</b> (for example, <b>Charts</b>). To quickly find your desired widget, use the search bar by clicking the magnifying glass icon and entering the widget&#39;s name;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-4-ce.webp" alt="Select a widget (for example, Time series chart) to open the Add widget dialog;" loading="lazy"><figcaption>Select a widget (for example, <b>Time series chart</b>) to open the <b>Add widget</b> dialog;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-5-ce.webp" alt="Specify the data source, add at least one data key, and click Add. Then Apply changes." loading="lazy"><figcaption>Specify the <b>data source</b>, add at least one <b>data key</b>, and click <b>Add</b>. Then <b>Apply changes</b>.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-6-ce.webp" alt="The widget is now created." loading="lazy"><figcaption>The widget is now created.</figcaption></figure></div>


Each widget typically has specific settings and parameters that allow users to customize its behavior and appearance according to their needs.
For more information about widgets, how to create them, and their settings, click the button below:

<br>
<p><a href="/docs/user-guide/widgets/" class="button">Widgets documentation</a></p>

<br>

### Time window

The Time window is a tool used to define time intervals when working with telemetry data. 
The time window is used by all time series and alarm widgets unless they are configured to use their own [widget time window](/docs/user-guide/widgets/#widget-time-window).
In the case of a time series widget, SENTIENT fetches telemetry with a timestamp that matches the time window. In the case of an alarm widget, SENTIENT fetches alarms with the created time that matches the time window.


<div id="video">  
    <div id="video_wrapper">
        <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/3xRWm1W1IM4" frameborder="0" allowfullscreen></iframe>
    </div>
</div>

<br>

**The time window can work in two modes**:

- In the **real-time mode**, widgets constantly receive updates from the server and automatically show you only the data that matches the time window for a current timestamp;
- In the **history mode**, widgets receive data only during the initial load and no updates are issued over WebSockets.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/timewindow-real-time-mode-1-ce.webp" alt="In the real-time mode, widgets constantly receive updates from the server and automatically show you only the data that matches the time window for a current timestamp." loading="lazy"><figcaption>In the real-time mode, widgets constantly receive updates from the server and automatically show you only the data that matches the time window for a current timestamp.</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/timewindow-history-mode-1-ce.webp" alt="In the history mode, widgets receive data only during the initial load and no updates are issued over WebSockets." loading="lazy"><figcaption>In the history mode, widgets receive data only during the initial load and no updates are issued over WebSockets.</figcaption></figure></div>


<br>
**Key parameters of the time window:**

- **Last**: Displays real-time data for a specified time interval (e.g., the last 5 minutes, the last hour, or the last 24 hours).
- **Range**: Displays data for a fixed period, such as from December 1, 2024, to December 7, 2024.
- **Relative**: Uses predefined intervals, such as the current day, the previous day, or the previous month.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/time-window-key-parameters-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<br>
To display data for your desired time period, set the time range in the time window and click "Update".


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/displaying-data-for-desired-time-period-1-ce.webp" alt="To display data for your desired time period, set the time range in the time window and click &quot;Update&quot;;" loading="lazy"><figcaption>To display data for your desired time period, set the time range in the time window and click "Update";</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/displaying-data-for-desired-time-period-2-ce.webp" alt="The widget displays data for the specified time period." loading="lazy"><figcaption>The widget displays data for the specified time period.</figcaption></figure></div>


<div class="st-callout info">


**Please note:**
<br>
that the **Current day** interval means 24 hours (12 am at night to 12 am the next night), whereas the **Current day so far** means from 12 am at night until the time when the time window was updated.
All other intervals are distinguished in the same way.


</div>


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/timewindow-interval-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/timewindow-interval-1-ce.webp" alt="From the begging of the specified timestamp (12 am) to the end of it (12 am the next night)." loading="lazy"><figcaption>From the begging of the specified timestamp (12 am) to the end of it (12 am the next night).</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/timewindow-interval-2-ce.webp" alt="The chart shows from the begging of the day (12 am at night) until the time when the time window was updated." loading="lazy"><figcaption>The chart shows from the begging of the day (12 am at night) until the time when the time window was updated.</figcaption></figure></div>


**Aggregation**

The data aggregation function is applied to time series data and does not apply to alarms. Currently, six aggregation functions are available:

- **Min**: Identifies the smallest value among all data in the selected time interval. Useful for displaying the minimum value, such as the lowest temperature recorded in an hour.
- **Max**: Identifies the largest value among all data in the selected time interval. This is useful for displaying the maximum value, such as the highest energy consumption level.
- **Average**: Calculates the arithmetic mean of all data in the selected interval. Useful for analyzing average metrics, such as the average humidity over a day.
- **Sum**: Computes the total sum of all values in the selected time interval. This can be helpful for calculating the total volume of water or electricity consumed.
- **Count**: Counts the number of records in the selected interval. Useful for assessing the volume of data received or to count the number of events.
- **None**: Transmits raw data without applying any aggregation functions. Used when access to each unaltered value is required.

Data aggregation is useful when you do not want to retrieve all raw time series data to the user interface but prefer to pre-aggregate it at the database level.

Using aggregation functions helps save network bandwidth and reduces the computational load on the client's browser. We recommend using aggregation functions whenever possible, especially when dealing with a large amount of raw data points.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/timewindow-aggregation-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<br>
**Grouping interval**

Group time series values by the specified time interval. This enables data analysis within a defined period and provides a more structured and convenient approach to handling large volumes of data.

For example, if a device sends temperature data every 10 minutes, but you need hourly average values, set the grouping interval to 1 hour and use the "Average" aggregation function. This will provide the desired result without additional processing on the client side.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/timewindow-grouping-interval-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/timewindow-grouping-interval-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


There are times when the time intervals are long, and you'd like to see the data closer without changing timestamps, therefore, you need to zoom in.
Move the two sliders towards each other to specify the time period for displaying the data.
To zoom out to the original size of the chart, move the sliders back to their default position.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/timewindow-zoom-1-ce.webp" alt="Move the two sliders towards each other to specify the time period for displaying the data." loading="lazy"><figcaption>Move the two sliders towards each other to specify the time period for displaying the data.</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/timewindow-zoom-2-ce.webp" alt="The data for the selected period is displayed on the chart." loading="lazy"><figcaption>The data for the selected period is displayed on the chart.</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/timewindow-zoom-3-ce.webp" alt="To zoom out to the original size of the chart, move the sliders back to their default position." loading="lazy"><figcaption>To zoom out to the original size of the chart, move the sliders back to their default position.</figcaption></figure></div>


The SENTIENT introduces time zone configurations. By default, the dashboard uses the time zone provided by the browser.
Now it is possible to set the time of your browser or a specific country. To quickly find the needed time zone, start typing its name in the time zone bar.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/timewindow-timezone-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<br>
**Time window settings**

You can customize the time window for the end-user by hiding certain configuration elements. Enter the editing mode of the dashboard, click the "edit time window" icon on the dashboard toolbar. In the popup window, click the "gear" icon. The time window configuration window will open.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/time-window-settings-1-ce.webp" alt="Enter the editing mode of the dashboard, click the &quot;edit time window&quot; icon on the dashboard toolbar. In the popup window, click the &quot;gear&quot; icon;" loading="lazy"><figcaption>Enter the editing mode of the dashboard, click the "edit time window" icon on the dashboard toolbar. In the popup window, click the "gear" icon;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/time-window-settings-2-ce.webp" alt="The time window configuration window will open." loading="lazy"><figcaption>The time window configuration window will open.</figcaption></figure></div>


Here, you can perform the following configurations:

*For time window*:

- **Hide the time window section from end-users**: Users will not be able to change the set time interval.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/hide-time-window-section-from-end-users-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/hide-time-window-section-from-end-users-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


You can also hide the "Last", "Range" (History) or "Relative" intervals from end-users.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/hide-only-last-or-relative-interval-from-end-users-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/hide-only-last-or-relative-interval-from-end-users-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Edit the list of intervals available to users. Additionally, for each interval, you can configure the grouping intervals and set a default grouping interval.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/edit-list-of-intervals-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/edit-list-of-intervals-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/edit-list-of-intervals-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/edit-list-of-intervals-4-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


*For aggregation function*:

- **Hide the aggregation from end-users**: Users will not be able to change or disable the aggregation function you set during configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/hide-aggregation-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/hide-aggregation-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/hide-aggregation-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


You can edit the list of available aggregation functions. List the available aggregation functions for the end-user.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/edit-aggregation-list-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/edit-aggregation-list-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


*For grouping interval*:

- **Hide the grouping interval from end-users**: Users will not be able to change the grouping interval set during configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/hide-grouping-interval-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/hide-grouping-interval-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/hide-grouping-interval-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Hide the time zone from end-users**: Restrict users from changing the timezone.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/hide-time-zone-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/hide-time-zone-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


*Available only when Aggregation is None*:


- **Max values**: Limits the number of data points rendered in time-series widgets within the selected time window. For self-hosted installations, this limit is configurable via the DASHBOARD_MAX_DATAPOINTS_LIMIT [parameter](/docs/user-guide/install/config/#ui-settings-parameters).


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/max-values-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Filters

Entity filters allow you to specify a filter for the list of entities resolved by the entity alias.

Let's look at an example. Suppose you have thousands of "Thermometer" devices, and you would like to display thermometers of a specific model and with certain battery levels.
Let's also assume that thermometer model is stored as an attribute, and the battery level is stored as a time series data.
We will define a filter that checks if the sensor model is "DHT22" and the battery level is less than 20 percent.


<div class="st-callout info">


**Please note:**
<br>
while adding the filter, you can configure the ability to edit it for users by moving the slider opposite the Filter name.


</div>


1. Open your dashboard, enter edit mode and click the "Filters" button in the upper right corner of the dashboard window. In the pop-up window click "Add filter" button;

1. In the pop-up window click "Add key filter" button;

1. Enter key name, select key type and value type. Then add a filter that checks if the sensor model is "DHT22" and click "Add";

1. Add another key filter;

1. Add filter that checks if the battery level is less than 20 percent;

1. Click "Add" button to add new filter;

1. Click "Save" and apply all changes.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-filters-1-ce.webp" alt="Open your dashboard, enter edit mode and click the &quot;Filters&quot; button in the upper right corner of the dashboard window. In the pop-up window click &quot;Add filter&quot; button;" loading="lazy"><figcaption>Open your dashboard, enter edit mode and click the "Filters" button in the upper right corner of the dashboard window. In the pop-up window click "Add filter" button;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-filters-2-ce.webp" alt="In the pop-up window click &quot;Add key filter&quot; button;" loading="lazy"><figcaption>In the pop-up window click "Add key filter" button;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-filters-3-ce.webp" alt="Enter key name, select key type and value type. Then add a filter that checks if the sensor model is &quot;DHT22&quot; and click &quot;Add&quot;;" loading="lazy"><figcaption>Enter key name, select key type and value type. Then add a filter that checks if the sensor model is "DHT22" and click "Add";</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-filters-4-ce.webp" alt="Add another key filter;" loading="lazy"><figcaption>Add another key filter;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-filters-5-ce.webp" alt="Add filter that checks if the battery level is less than 20 percent;" loading="lazy"><figcaption>Add filter that checks if the battery level is less than 20 percent;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-filters-6-ce.webp" alt="Click &quot;Add&quot; button to add new filter;" loading="lazy"><figcaption>Click "Add" button to add new filter;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-filters-7-ce.webp" alt="Click &quot;Save&quot; and apply all changes." loading="lazy"><figcaption>Click "Save" and apply all changes.</figcaption></figure></div>


Filters are applied only to the "latest" value of the attribute or time series key. Don't use this feature to "filter out" historical time series values.

You can combine different logical expressions over one key using "complex" filters. For example: "(A > 0 and A < 20) or (A > 50 and A < 100)".
Also, you can combine two expressions for different keys using the "and" relation. For example: "(A > 0 and A < 20) and (B > 50 and B < 100)".
It's not possible to use "or" in relation to combining different keys yet. For example: "(A > 0 and A < 20) or (B > 50 and B < 100)".

See more examples of how to use filters in this video:

<br>
<div id="video">
  <div id="video_wrapper">
    <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/yTAhUpZiFkM?start=177" frameborder="0" allowfullscreen=""></iframe>
  </div>
</div>

### Entity aliases

Entity Aliases determine which entities (devices, assets, etc.) you would like to display on the dashboard.
An alias can be thought of as a reference to one or more devices. These references can be static or dynamic.

An example of the static alias is the [Single entity](/docs/user-guide/ui/aliases/#single-entity) alias. An entity is configured once in the alias dialog box.
All users see the same data if they have permission to access this device.

An example of a dynamic alias is the [Device type](/docs/user-guide/ui/aliases/#device-type) alias, which displays all devices of a certain type (e.g. "Thermometer").
This alias is dynamic because the list of devices depends on the user using the dashboard.
If you are logged in as a Tenant administrator, this alias will be allowed for all Thermometer devices.
However, if you are logged in as a Customer user, this alias will be resolved to Thermometer devices that are assigned/owned by that Customer.

Let’s create a dynamic alias, which displays all devices of a certain "Smart sensors" type.


1. Open your dashboard, enter edit mode and click the "Entity aliases" button in the upper right corner of the dashboard window. In the pop-up window click "Add alias" button;

1. In the pop-up window enter alias name, select filter type and device type. Then click "Add" button;

1. Click "Save" button to save the alias and save all changes.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-aliases-1-ce.webp" alt="Open your dashboard, enter edit mode and click the &quot;Entity aliases&quot; button in the upper right corner of the dashboard window. In the pop-up window click &quot;Add alias&quot; button;" loading="lazy"><figcaption>Open your dashboard, enter edit mode and click the "Entity aliases" button in the upper right corner of the dashboard window. In the pop-up window click "Add alias" button;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-aliases-2-ce.webp" alt="In the pop-up window enter alias name, select filter type and device type. Then click &quot;Add&quot; button;" loading="lazy"><figcaption>In the pop-up window enter alias name, select filter type and device type. Then click "Add" button;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-aliases-3-ce.webp" alt="Click &quot;Save&quot; button to save the alias and save all changes." loading="lazy"><figcaption>Click "Save" button to save the alias and save all changes.</figcaption></figure></div>


Please see the [Entity aliases documentation](/docs/user-guide/ui/aliases) for more information.

### Settings

Dashboard settings allow adjusting and altering the overall look of the Dashboard. You can change the title, logo, and customize the toolbar.

To start customizing the Dashboard enter [Edit mode](#edit-mode), then click the "gear" icon in the upper right corner of the dashboard window to open the dashboard settings window.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-settings-1-ce.webp" alt="Open the dashboard and click the &quot;Edit mode&quot; button in the upper right corner of the screen;" loading="lazy"><figcaption>Open the dashboard and click the "Edit mode" button in the upper right corner of the screen;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-settings-2-ce.webp" alt="Click the “gear” icon at the top of the window;" loading="lazy"><figcaption>Click the “gear” icon at the top of the window;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-settings-3-ce.webp" alt="The dashboard settings window will open." loading="lazy"><figcaption>The dashboard settings window will open.</figcaption></figure></div>


**Title settings**

If you want the Title to be displayed on the dashboard, you need to enable the "Display dashboard title" checkbox. The default text color is black. 
Color and transparency are easily adjusted using the Title color parameter by clicking the colored circle and choosing the desired color for the title by moving the slider. 
The changed title appears on the top left of the Dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-settings-title-color-1-ce.webp" alt="Check the box &quot;Display dashboard title&quot; and select color of title;" loading="lazy"><figcaption>Check the box "Display dashboard title" and select color of title;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-settings-title-color-2-ce.webp" alt="The changed title appears on the top left of the Dashboard." loading="lazy"><figcaption>The changed title appears on the top left of the Dashboard.</figcaption></figure></div>


**Dashboard logo settings**

You can set dashboard logo which displayed in dashboard fullscreen mode. For this, check the box "Display logo in dashboard fullscreen mode" and add dashboard logo image.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-logo-settings-2-ce.webp" alt="Display logo in dashboard fullscreen mode&quot; and add dashboard logo image. Apply changes;" loading="lazy"><figcaption>Display logo in dashboard fullscreen mode" and add dashboard logo image. Apply changes;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-logo-settings-3-ce.webp" alt="Expand dashboard to fullscreen;" loading="lazy"><figcaption>Expand dashboard to fullscreen;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-logo-settings-4-ce.webp" alt="The added logo appears in the top left corner in the fullscreen mode of the dashboard." loading="lazy"><figcaption>The added logo appears in the top left corner in the fullscreen mode of the dashboard.</figcaption></figure></div>


**Toolbar settings**

The checkboxes "Display dashboard selection", "Display entities selection", "Display filters", "Display time window", "Display export" and "Display update dashboard image" are responsible for the visibility of the appropriate options on the Dashboard toolbar panel.

The "Display filters" option is shown on the toolbar panel only if at least one filter has been created. 
If the filter was created, but you'd like to limit the customer's opportunity to modify the device's indicators, we disable the ability to see filters on the toolbar panel by unchecking the corresponding checkbox.

You can display/hide toolbar icons. Let's hide "Display dashboards selection", "Display time window" and "Display export" icons on the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/toolbar-settings-1-ce.webp" alt="Hide &quot;Display dashboards selection&quot;, &quot;Display time window&quot; and &quot;Display export&quot; icons on the dashboard page;" loading="lazy"><figcaption>Hide "Display dashboards selection", "Display time window" and "Display export" icons on the dashboard page;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/toolbar-settings-2-ce.webp" alt="The specified icons are hidden on the dashboard page." loading="lazy"><figcaption>The specified icons are hidden on the dashboard page.</figcaption></figure></div>


The "Hide Toolbar" option will hide the toolbar from the dashboard page.
Instead of it, on the upper right of the screen, you will find "Enter edit mode" icon.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/toolbar-settings-3-ce.webp" alt="The “Hide Toolbar” will hide the toolbar from the dashboard page." loading="lazy"><figcaption>The “Hide Toolbar” will hide the toolbar from the dashboard page.</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/toolbar-settings-4-ce.webp" alt="Instead of the toolbar, on the upper right of the screen, you will find “Enter edit mode” icon." loading="lazy"><figcaption>Instead of the toolbar, on the upper right of the screen, you will find “Enter edit mode” icon.</figcaption></figure></div>


The "Keep toolbar opened" option is responsible for displaying the toolbar on the dashboard page. 
If we disable it, the toolbar will be closed. Instead of it, on the upper right of the screen you find the three-dots icon. 
By clicking on it, the hidden toolbar will be opened.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/toolbar-settings-5-ce.webp" alt="The &quot;Keep toolbar opened&quot; is responsible for displaying the toolbar on the dashboard page." loading="lazy"><figcaption>The "Keep toolbar opened" is responsible for displaying the toolbar on the dashboard page.</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/toolbar-settings-6-ce.webp" alt="Instead of the toolbar, on the upper right of the screen you find the three-dots icon. By clicking on it, the hidden toolbar will be opened." loading="lazy"><figcaption>Instead of the toolbar, on the upper right of the screen you find the three-dots icon. By clicking on it, the hidden toolbar will be opened.</figcaption></figure></div>


### Layouts

Layouts determine how widgets will be displayed and organized on the dashboard grid. [Read more about layouts in a separate documentation](/docs/user-guide/ui/layouts/).

### States

The States feature exists to create a layered hierarchy in your Dashboard. To use States properly, you need to assign a specific action to a widget that will help you fast "travel" among the required states.
To do this, you should enter [edit mode](#edit-mode) and click the button two-layered squares "Manage dashboard states" in the upper left corner of the dashboard window. The Manage dashboard states configuration window will open.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-1-ce.webp" alt="Enter edit mode and сlick the button two-layered squares &quot;Manage dashboard states&quot; in the upper left corner of the dashboard window. It will open the window with a dashboard state configuration." loading="lazy"><figcaption>Enter edit mode and сlick the button two-layered squares "Manage dashboard states" in the upper left corner of the dashboard window. It will open the window with a dashboard state configuration.</figcaption></figure></div>


Since you haven't created any states yet, you have only your "Root state", namely your Dashboard. Root state defines the main state of your hierarchy.
After creating additional states, you easily can change a root state by clicking the "Pencil" icon (Edit dashboard state) and selecting the “Root state” checkbox.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-root-1-ce.webp" alt="You can change a root state by clicking the “Pencil” icon (Edit dashboard state);" loading="lazy"><figcaption>You can change a root state by clicking the “Pencil” icon (Edit dashboard state);</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-root-2-ce.webp" alt="Tick the “Root state” checkbox, and save changes." loading="lazy"><figcaption>Tick the “Root state” checkbox, and save changes.</figcaption></figure></div>


To add a new state, you need to click on the "+" icon in the right upper of the window, it will open the Add dashboard state window.
Assign a name, and the State ID will automatically generate based on that name, though you have the option to modify it. Click "Add" and then save all changes.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-2-ce.webp" alt="To add a new state, you need to click the “+” button in the right upper of the manage dashboard states window;" loading="lazy"><figcaption>To add a new state, you need to click the “+” button in the right upper of the manage dashboard states window;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-4-ce.webp" alt="Enter a state name, State ID will form automatically according to the name, but you can change it. Click &quot;Add&quot;;" loading="lazy"><figcaption>Enter a state name, State ID will form automatically according to the name, but you can change it. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-5-ce.webp" alt="After adding states, save all changes;" loading="lazy"><figcaption>After adding states, save all changes;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-6-ce.webp" alt="You can navigate between states through a drop-down menu." loading="lazy"><figcaption>You can navigate between states through a drop-down menu.</figcaption></figure></div>


Giving a corresponding action to a particular widget allows traveling between states.
To add an action, you should click the "pencil" icon (Edit widget) in the upper right corner of the widget to enter the widget configuration mode.
There you need to navigate to the "Action" tab and click the "+" icon to add a new action.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-7-ce.webp" alt="Click the “pencil” icon (edit widget) in the upper right corner of the widget to enter the widget configuration mode;" loading="lazy"><figcaption>Click the “pencil” icon (edit widget) in the upper right corner of the widget to enter the widget configuration mode;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-8-ce.webp" alt="Navigate to the “Action” tab and click the “+” icon to add a new action." loading="lazy"><figcaption>Navigate to the “Action” tab and click the “+” icon to add a new action.</figcaption></figure></div>


It will open the "Add action" window.

- The _Action source_ is a particular act that needs to be done to achieve an aim.
- The _Name_ means a preferred title to an action.
- The _Icon_ defines a symbol for action.
- The _Type_ determines an aim of the action.

In our case, a _Type_ should be "Navigate to new dashboard state". After choosing this option, the line "Target dashboard state" will appear, where we have to choose a newly created state.
When the configuration for a new action is done, click the "Add" button. The new action appears in the actions list. Click the "Apply" button at the upper right of the window to apply changes.

As we have chosen the "On row click" action, we need to click on the row of our widget to bring the action into effect. After clicking, we immediately transfer to the chosen state.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-9-ce.webp" alt="Enter the action name, select the action source, an aim of the action, and select the state to which you will be transferred. Then click &quot;Add&quot; button;" loading="lazy"><figcaption>Enter the action name, select the action source, an aim of the action, and select the state to which you will be transferred. Then click "Add" button;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-10-ce.webp" alt="The new action appears in the actions list. Apply changes;" loading="lazy"><figcaption>The new action appears in the actions list. Apply changes;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-11-ce.webp" alt="Click on the button to activate the action;" loading="lazy"><figcaption>Click on the button to activate the action;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-12-ce.webp" alt="After clicking, we immediately transfer to the chosen state." loading="lazy"><figcaption>After clicking, we immediately transfer to the chosen state.</figcaption></figure></div>


For the state to be named after the entity, use **${entityName}** as the name of the state. Thus during the action, you will be transitioned to a state that is called the same as the entity that took part in the action.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-13-ce.webp" alt="For the state to be named after the entity, use ${entityName} as the name of the state;" loading="lazy"><figcaption>For the state to be named after the entity, use ${entityName} as the name of the state;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-14-ce.webp" alt="Click the “pencil” icon (edit widget) in the upper right corner of the widget to enter the widget configuration mode. Navigate to the “Action” tab and click the “+” icon to add a new action;" loading="lazy"><figcaption>Click the “pencil” icon (edit widget) in the upper right corner of the widget to enter the widget configuration mode. Navigate to the “Action” tab and click the “+” icon to add a new action;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-15-ce.webp" alt="Enter action name, select action source, an aim of the action and select a state to which you will be transferred. Then click &quot;Add&quot; button;" loading="lazy"><figcaption>Enter action name, select action source, an aim of the action and select a state to which you will be transferred. Then click "Add" button;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-16-ce.webp" alt="The new action appears in the actions list. Apply changes;" loading="lazy"><figcaption>The new action appears in the actions list. Apply changes;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-17-ce.webp" alt="Click the row of our widget to activate the action;" loading="lazy"><figcaption>Click the row of our widget to activate the action;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/dashboard-states-18-ce.webp" alt="After clicking, you will be transitioned to a state that is called the same as the entity that took part in the action." loading="lazy"><figcaption>After clicking, you will be transitioned to a state that is called the same as the entity that took part in the action.</figcaption></figure></div>


## Managing dashboard


With your dashboards, you can perform operations such as [export dashboard in the JSON format](#export-dashboard), [make dashboard public](#make-dashboard-public), [manage assigned customers](#manage-assigned-customers), [edit dashboard](#edit-dashboard) and [delete dashboard](#delete-dashboard) using the corresponding icon next to the dashboard.


Let's look at each operation.

### Export dashboard

In the SENTIENT you can export a dashboard as a configuration file in JSON format.
You can use this file to transfer your Dashboard or widget configuration to another instance.

To export a dashboard, go to the “Dashboards” page. Find the dashboard you want to export in the list and click on the "Export dashboard" button located next to the dashboard's name. The configuration file in JSON format with all settings on the control panel will be saved on your PC.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/export-dashboard-1-ce.webp" alt="To export a dashboard, go to the &quot;Dashboards&quot; page and click the &quot;Export dashboard&quot; icon next to the dashboard that you want to export. The configuration file in JSON format with all settings on the control panel will be saved on your PC." loading="lazy"><figcaption>To export a dashboard, go to the "Dashboards" page and click the "Export dashboard" icon next to the dashboard that you want to export. The configuration file in JSON format with all settings on the control panel will be saved on your PC.</figcaption></figure></div>


To export the dashboard directly from the toolbar, open the dashboard and click the "Export dashboard" button in the upper right corner of the screen.
Dashboard is exported to the configuration file in JSON format.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-toolbar-export-1-ce.webp" alt="Go to the &quot;Dashboards&quot; page, open the dashboard and click the &quot;Export dashboard&quot; button in the upper right corner of the screen." loading="lazy"><figcaption>Go to the "Dashboards" page, open the dashboard and click the "Export dashboard" button in the upper right corner of the screen.</figcaption></figure></div>


In **SENTIENT Professional Edition**, in addition to exporting the dashboard in JSON format, dashboard export is possible in several additional formats: PDF, PNG & JPEG. This is useful when you need to send the data displayed in your dashboard by email or print.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/overview/dashboard-toolbar-export-png-pdf-1-pe.webp" alt="To enter dashboard edit mode, open the dashboard and click the &quot;Edit mode&quot; button in the upper right corner of the screen;" loading="lazy"><figcaption>To enter dashboard edit mode, open the dashboard and click the "Edit mode" button in the upper right corner of the screen;</figcaption></figure><figure><img src="/images/user-guide/dashboards/overview/pdf-export.webp" alt="The dashboard that was exported as PNG." loading="lazy"><figcaption>The dashboard that was exported as PNG.</figcaption></figure></div>


### Import dashboard

You can import a dashboard from a JSON configuration file. This can be useful when you are migrating your dashboard configuration from another instance.

To import a dashboard, follow these steps:


1. Go to the "Dashboards" page and click on the "+" button in the upper right corner of the page and select "Import dashboard" from the drop-down menu;

1. In the import dashboard window, upload the dashboard configuration JSON file and click "Import";

1. You have imported a dashboard. Open it;

1. As you can see, your dashboard has been imported along with all of its widgets.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/import-dashboard-1-ce.webp" alt="Go to the &quot;Dashboards&quot; page and click on the &quot;+&quot; button in the upper right corner of the page and select &quot;Import dashboard&quot; from the drop-down menu;" loading="lazy"><figcaption>Go to the "Dashboards" page and click on the "+" button in the upper right corner of the page and select "Import dashboard" from the drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/import-dashboard-2-ce.webp" alt="In the import dashboard window, upload the dashboard configuration JSON file and click &quot;Import&quot;;" loading="lazy"><figcaption>In the import dashboard window, upload the dashboard configuration JSON file and click "Import";</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/import-dashboard-3-ce.webp" alt="You have imported a dashboard. Open it;" loading="lazy"><figcaption>You have imported a dashboard. Open it;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/import-dashboard-4-ce.webp" alt="As you can see, your dashboard has been imported along with all of its widgets." loading="lazy"><figcaption>As you can see, your dashboard has been imported along with all of its widgets.</figcaption></figure></div>


### Make dashboard public

You can make the dashboard public and share a link to it with other users.


For this you should:


1. Go to the "Dashboards" page. Click the "Make public" icon next to the dashboard that you want to make public;

1. Dashboard is now public. In the pop-up window, click "Copy public link" icon. You can now share the dashboard using this link, for example, by sending it via email. Or you can use the quick buttons to share the link on social networks;

1. Next time you can find the public link to the dashboard in the dashboard details window;


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/make-public-dashboard-1-ce.webp" alt="Go to the &quot;Dashboards&quot; page. Click the &quot;Make public&quot; icon next to the dashboard that you want to make public;" loading="lazy"><figcaption>Go to the "Dashboards" page. Click the "Make public" icon next to the dashboard that you want to make public;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/make-public-dashboard-2-ce.webp" alt="Dashboard is now public. In the pop-up window, click &quot;Copy public link&quot; icon. You can now share the dashboard using this link, for example, by sending it via email. Or you can use the quick buttons to share the link on social networks;" loading="lazy"><figcaption>Dashboard is now public. In the pop-up window, click "Copy public link" icon. You can now share the dashboard using this link, for example, by sending it via email. Or you can use the quick buttons to share the link on social networks;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/make-public-dashboard-3-ce.webp" alt="Next time you can find the public link to the dashboard in the dashboard details window;" loading="lazy"><figcaption>Next time you can find the public link to the dashboard in the dashboard details window;</figcaption></figure></div>


To make a dashboard private again, follow these steps:


1. Click the "Make private" icon next to the dashboard that you want to make private;

1. In the confirmation dialog box, click "Yes".


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/make-public-dashboard-4-ce.webp" alt="Click the &quot;Make private&quot; icon next to the dashboard that you want to make private;" loading="lazy"><figcaption>Click the "Make private" icon next to the dashboard that you want to make private;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/make-public-dashboard-5-ce.webp" alt="In the confirmation dialog box, click &quot;Yes&quot;." loading="lazy"><figcaption>In the confirmation dialog box, click "Yes".</figcaption></figure></div>


<div class="st-callout info">


**Please note:**
<br>
To display data on a public dashboard, the associated entities must also be made public. This can be done by making the device or asset group public for Professional Edition or by making individual devices or assets for Community Edition.


</div>


### Manage assigned customers

You can assign a dashboard to your client. The customer will only have the ability to view the dashboard and won't be able to perform any other operations on the dashboard.

To assign a dashboard to a customer you should:


1. Go to the "Dashboards" page and click the "Manage assigned customers" icon next to the dashboard that you want to make assigned to the customer;

1. Select the customer(s) to assign the dashboard. Click "Update";

1. The dashboard assigned to the selected customer.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/manage-assigned-customers-1-ce.webp" alt="Go to the &quot;Dashboards&quot; page and click the &quot;Manage assigned customers&quot; icon next to the dashboard that you want to make assigned to the customer;" loading="lazy"><figcaption>Go to the "Dashboards" page and click the "Manage assigned customers" icon next to the dashboard that you want to make assigned to the customer;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/manage-assigned-customers-2-ce.webp" alt="Select the customer(s) to assign the dashboard. Click &quot;Update&quot;;" loading="lazy"><figcaption>Select the customer(s) to assign the dashboard. Click "Update";</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/manage-assigned-customers-3-ce.webp" alt="The dashboard assigned to the selected customer." loading="lazy"><figcaption>The dashboard assigned to the selected customer.</figcaption></figure></div>


You can unassign a dashboard from a customer. For this:


1. Go to the "Dashboards" page and click the "Manage assigned customers" icon next to the dashboard that you want to make assigned to the customer;

1. Remove the customer(s) from the assigned customer list. Click "Update";

1. Assigned customers list updated.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/manage-assigned-customers-1-ce.webp" alt="Go to the &quot;Dashboards&quot; page and click the &quot;Manage assigned customers&quot; icon next to the dashboard that you want to make assigned to the customer;" loading="lazy"><figcaption>Go to the "Dashboards" page and click the "Manage assigned customers" icon next to the dashboard that you want to make assigned to the customer;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/manage-assigned-customers-5-ce.webp" alt="Remove the customer(s) from the assigned customer list. Click &quot;Update&quot;;" loading="lazy"><figcaption>Remove the customer(s) from the assigned customer list. Click "Update";</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/manage-assigned-customers-6-ce.webp" alt="Assigned customers list updated." loading="lazy"><figcaption>Assigned customers list updated.</figcaption></figure></div>


To assign/unassign multiple dashboards to a customer(s) simultaneously, select the desired dashboards and use the "Assign Dashboards" and "Unassign Dashboards" buttons.


1. Go to the "Dashboards" page and mark one or multiple dashboards. Then, select the desired function using the "Assign Dashboards" or "Unassign Dashboards" buttons in the upper right corner of the screen.

1. Select the customer(s) to assign the dashboards, then click "Assign";

1. The list of clients to whom the selected dashboards were assigned has been updated.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/manage-assigned-customers-4-ce.webp" alt="Go to the &quot;Dashboards&quot; page and mark one or multiple dashboards. Then, select the desired function using the &quot;Assign Dashboards&quot; or &quot;Unassign Dashboards&quot; buttons in the upper right corner of the screen." loading="lazy"><figcaption>Go to the "Dashboards" page and mark one or multiple dashboards. Then, select the desired function using the "Assign Dashboards" or "Unassign Dashboards" buttons in the upper right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/manage-assigned-customers-7-ce.webp" alt="Select the customer(s) to assign the dashboards, then click &quot;Assign&quot;;" loading="lazy"><figcaption>Select the customer(s) to assign the dashboards, then click "Assign";</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/manage-assigned-customers-8-ce.webp" alt="The list of clients to whom the selected dashboards were assigned has been updated." loading="lazy"><figcaption>The list of clients to whom the selected dashboards were assigned has been updated.</figcaption></figure></div>


### Edit dashboard

Edit the fields you need, such as the title or description of the dashboard. After making the edits, remember to save all changes.
With these steps, you will have successfully updated the dashboard information.

Let’s see how to do this:


1. Go to the "Dashboards" page and click the "Dashboard details" icon next to the dashboard that you want to edit;

1. Click the "pencil" icon to enter edit mode;

1. Edit the fields you need. For example, edit the title of the dashboard, specify description. After making the edits, remember to save all changes;

1. You have updated the dashboard information.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/dashboard-details-1-ce.webp" alt="Go to the &quot;Dashboards&quot; page and click the &quot;Dashboard details&quot; icon next to the dashboard that you want to edit;" loading="lazy"><figcaption>Go to the "Dashboards" page and click the "Dashboard details" icon next to the dashboard that you want to edit;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/dashboard-details-2-ce.webp" alt="Click the &quot;pencil&quot; icon to enter edit mode;" loading="lazy"><figcaption>Click the "pencil" icon to enter edit mode;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/dashboard-details-3-ce.webp" alt="Edit the fields you need. For example, edit the title of the dashboard, specify description. After making the edits, remember to save all changes;" loading="lazy"><figcaption>Edit the fields you need. For example, edit the title of the dashboard, specify description. After making the edits, remember to save all changes;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/dashboard-details-4-ce.webp" alt="You have updated the dashboard information." loading="lazy"><figcaption>You have updated the dashboard information.</figcaption></figure></div>


### Delete dashboard

You can delete a dashboard using one of the following ways:

First way:


1. Go to the "Dashboards" page and click the "Trash" icon opposite the dashboard`s name you want to delete;

1. Confirm deleting the dashboard in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/delete-dashboard-1-ce.webp" alt="Go to the &quot;Dashboards&quot; page and click the &quot;Trash&quot; icon opposite the dashboard`s name you want to delete;" loading="lazy"><figcaption>Go to the "Dashboards" page and click the "Trash" icon opposite the dashboard`s name you want to delete;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/delete-dashboard-2-ce.webp" alt="Confirm deleting the dashboard in the dialog box." loading="lazy"><figcaption>Confirm deleting the dashboard in the dialog box.</figcaption></figure></div>


Second way:


1. Click the "Dashboard details" icon next to the dashboard that you want to delete;

1. In the dashboard details, click "Delete dashboard" button;

1. Confirm deleting the dashboard in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/delete-dashboard-3-ce.webp" alt="Click the &quot;Dashboard details&quot; icon next to the dashboard that you want to delete;" loading="lazy"><figcaption>Click the "Dashboard details" icon next to the dashboard that you want to delete;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/delete-dashboard-4-ce.webp" alt="In the dashboard details, click &quot;Delete dashboard&quot; button;" loading="lazy"><figcaption>In the dashboard details, click "Delete dashboard" button;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/delete-dashboard-5-ce.webp" alt="Confirm deleting the dashboard in the dialog box." loading="lazy"><figcaption>Confirm deleting the dashboard in the dialog box.</figcaption></figure></div>


You can also delete multiple dashboards at once.


1. Mark one or multiple dashboards you want to delete. Click on the "Trash" bin icon in the top right corner;

1. Confirm deleting dashboards in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/managing-dashboard/delete-dashboard-6-ce.webp" alt="Mark one or multiple dashboards you want to delete. Click on the &quot;Trash&quot; bin icon in the top right corner;" loading="lazy"><figcaption>Mark one or multiple dashboards you want to delete. Click on the "Trash" bin icon in the top right corner;</figcaption></figure><figure><img src="/images/user-guide/dashboards/managing-dashboard/delete-dashboard-7-ce.webp" alt="Confirm deleting dashboards in the dialog box." loading="lazy"><figcaption>Confirm deleting dashboards in the dialog box.</figcaption></figure></div>


## Next steps

 - [Widgets](/docs/user-guide/widgets) - This guide contains instructions for configuring SENTIENT widgets.
 - [Data visualization](/docs/guides/#AnchorIDDataVisualization) - These guides contain instructions how to configure complex SENTIENT dashboards.
 - [Data processing & actions](/docs/guides/#AnchorIDDataProcessing) - Learn how to use SENTIENT Rule Engine.
