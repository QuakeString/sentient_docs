+++
title = "Widgets Library"
description = "SENTIENT Dashboard Widgets Library"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/widget-library.md"
+++
All [IoT Dashboards](/docs/user-guide/dashboards/) are constructed using **SENTIENT widgets** defined in the Widget Library.

A widget is an element that displays a specific type of information or functionality on a dashboard.
Widgets are used to display data and visualize information obtained from devices connected to the SENTIENT platform, remote device control, alarms management, and display static custom HTML content.

## Widget Types

According to the provided features, each widget definition represents a specific widget type.
There are five widget types:

 - [Latest values;](#latest-values)
 - [Time series;](#time-series)
 - [Control widget;](#control-widget)
 - [Alarm widget;](#alarm-widget)
 - [Static widget.](#static)


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-dashboard-widgets-ce.webp" alt="The widget type is displayed in the corresponding column on the &quot;Widget Library&quot; page." loading="lazy"><figcaption>The widget type is displayed in the corresponding column on the "Widget Library" page.</figcaption></figure></div>


 
Each widget type has its own specific data source configuration to visualize data. Types of available data sources depend on widget type:

 - **Alarm source** - this data source type, used primarily in Alarm widgets, requires a source entity to display related alarms and their corresponding fields;
 - **Alarms count** - this data source type is used in latest values widgets. You need to specify the target entity;
 - **Device** - this data source type is used in both time-series and latest values widgets. Basically, you need to specify the target device, and the time series key, or the attribute name, or entity field;
 - **Entities count** - this data source type is used in latest values widgets. You need to specify the target entity;
 - **Entity** - this data source type is used in both time-series and latest values widgets. Basically, you need to select the target entity by specifying an [entity alias](/docs/user-guide/ui/aliases/), and the time series key, or the attribute name;
 - **Function** - this data source type is used in both time series and latest values widgets for debugging. Basically, you can specify a JavaScript function that will simulate data from a device in order to set up visualization.

### Latest values

The Latest values widget type is designed to showcase the latest values of a specific entity attribute or time series data point (e.g., any Gauge Widget or Entities Table widget).
This type of widget uses values of entity attribute(s) or time series as a data source.
Digital Gauge in the example is displays the current temperature value.
 


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/latest-values-datasource-1-ce.webp" alt="This widget type uses values of entity time series as a data source;" loading="lazy"><figcaption>This widget type uses values of entity time series as a data source;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/latest-values-datasource-2-ce.webp" alt="Digital Gauge displaying current temperature value." loading="lazy"><figcaption>Digital Gauge displaying current temperature value.</figcaption></figure></div>


### Time series

The Time series widget type displays historical values for the selected period of time, or the latest values in the certain time window (e.g., Timeseries Line Chart or Timeseries Bar Chart).
This widget type uses only the values of entity time series as a data source.
In order to specify the time frame of displayed values, _Time window_ settings are used.
The time window can be specified on the dashboard page or via widget details. It can be either _Realtime_ - the dynamically changed time frame for a certain latest interval, or _History_ - a fixed historical time frame.
All these settings are part of Timeseries widget configuration.
In the example, the "Timeseries Line Chart" displays the speed value of the device in real-time.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-timeseries-1-ce.webp" alt="This kind of widgets uses only the values of entity time series as a data source;" loading="lazy"><figcaption>This kind of widgets uses only the values of entity time series as a data source;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-timeseries-2-ce.webp" alt="An example of timeseries widget is the &quot;Timeseries Line Chart&quot;. It displays temperature values of devices in real-time." loading="lazy"><figcaption>An example of timeseries widget is the "Timeseries Line Chart". It displays temperature values of devices in real-time.</figcaption></figure></div>


### Control widget

The Control widget allows sending RPC commands to devices, it handles and visualizes replies from the device (e.g., Raspberry Pi GPIO Control).
The RPC widgets are configured by specifying the target device as the target endpoint for RPC commands.
In the example, the “Basic GPIO Control” widget sends GPIO switch commands and detects the current GPIO switch status.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-control-widget-1-ce.webp" alt="RPC widgets are configured by specifying target device as target endpoint for RPC commands;" loading="lazy"><figcaption>RPC widgets are configured by specifying target device as target endpoint for RPC commands;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-control-widget-2-ce.webp" alt="An example of RPC widget is “Basic GPIO Control”. It sends GPIO switch commands and detects current GPIO switch status." loading="lazy"><figcaption>An example of RPC widget is “Basic GPIO Control”. It sends GPIO switch commands and detects current GPIO switch status.</figcaption></figure></div>


### Alarm Widget

The Alarm Widget type displays alarms related to the specified entity in the certain time window (e.g., Alarms table).
To configure the Alarm widget, you designate an entity as the alarm source and define the corresponding alarm fields.
As the _Timeseries widgets_, Alarm widgets have the _time window_ configuration to specify the time frame of the displayed alarms.
Additionally, the configuration includes parameters such as "Alarm status", "Alarm severity", and "Alarm type".
The “Alarm status” parameter shows the status of the alarms being fetched.
The "Alarm severity" parameter shows the frequency of alarm fetches in seconds.
The "Alarm Type" parameter helps identify the primary source of the alarm.
For instance, "HighTemperature" and "LowHumidity" represent two different alarms.
In this context, the "Alarms table" widget displays the latest alarm for the device in real-time.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-alarms-1-ce.webp" alt="Alarm widget is configured by specifying an entity as the alarm source, and the corresponding alarm fields;" loading="lazy"><figcaption>Alarm widget is configured by specifying an entity as the alarm source, and the corresponding alarm fields;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-alarms-2-ce.webp" alt="An example of Alarm widget is the “Alarms table” widget that displays the latest alarm for the device in real-time." loading="lazy"><figcaption>An example of Alarm widget is the “Alarms table” widget that displays the latest alarm for the device in real-time.</figcaption></figure></div>


### Static

The Static widget type displays static customizable HTML content (e.g., HTML card).
Static widgets don’t use any data sources and are usually configured by specifying static HTML content and, optionally, CSS styles.
An example of a Static widget is the “HTML card” that displays the specified HTML content.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-static-1-ce.webp" alt="Static widget type is configured by specifying static HTML content and, optionally, CSS styles;" loading="lazy"><figcaption>Static widget type is configured by specifying static HTML content and, optionally, CSS styles;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-static-2-ce.webp" alt="An example of a Static widget is the “HTML card” that displays the specified HTML content." loading="lazy"><figcaption>An example of a Static widget is the “HTML card” that displays the specified HTML content.</figcaption></figure></div>


<details>

<summary>
<b>An example of a CSS style function to adjust an HTML card style.</b>
</summary>

<figure class="highlight"><pre><code class="language-ruby" data-lang="ruby"><span class="p">.</span><span class="nf">card</span> <span class="p">{</span>
<span class="n">font</span><span class="o">-</span><span class="ss">weight: </span><span class="n">bold</span><span class="p">;</span>
<span class="n">font</span><span class="o">-</span><span class="ss">size: </span><span class="mi">32</span><span class="n">px</span><span class="p">;</span>
<span class="ss">color: </span><span class="c1">#999;</span>
<span class="ss">width: </span><span class="mi">100</span><span class="o">%</span><span class="p">;</span>
<span class="ss">height: </span><span class="mi">100</span><span class="o">%</span><span class="p">;</span>
<span class="ss">display: </span><span class="n">flex</span><span class="p">;</span>
<span class="n">align</span><span class="o">-</span><span class="ss">items: </span><span class="n">center</span><span class="p">;</span>
<span class="n">justify</span><span class="o">-</span><span class="ss">content: </span><span class="n">center</span><span class="p">;</span>
<span class="p">}</span></code></pre></figure>

</details>

<details>

<summary>
<b>An example of an HTML code for specifying card content.</b>
</summary>

<figure class="highlight"><pre><code class="language-ruby" data-lang="ruby"><span class="o">&lt;</span><span class="n">h1</span><span class="o">&gt;</span><span class="no">Static</span> <span class="n">widget</span> <span class="n">title</span><span class="o">&lt;</span><span class="sr">/h1&gt;
&lt;div class='card'&gt;Your text here&lt;/</span><span class="n">div</span><span class="o">&gt;</span></code></pre></figure>

</details>
 
## Widgets Library (Bundles)

Widgets are grouped into widget bundles according to their purposes.
Some widgets can be found in multiple packages simultaneously. For example, the Alarm Count widget can be both found in the Alarm widgets bundle and the Count widgets bundle.

There are system-level and tenant-level widget bundles. Initial SENTIENT installation comes with a basic set of system-level widget bundles.

The system-level bundles can be managed by a **System administrator** and are available for use by any tenant in the system.
The tenant-level bundles can be managed by a **Tenant administrator** and are available for use only by this tenant and his customers.
You can always implement and add your widgets by following this [guide](/docs/user-guide/contribution/widgets-development/).

To find the widget you need among all the widget bundles, you can use the search function.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/widgets-library-bundles-list-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


You can also find the widget you need by its name on the "Widgets" tab. Here, all available widgets are listed by default in alphabetical order.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/widgets-library-list-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Air quality

This widgets bundle includes widgets for visualizing air quality data.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-air-quality-bundle-ce.webp" alt="For visualizing air quality data." loading="lazy"><figcaption>For visualizing air quality data.</figcaption></figure></div>


### Alarm widgets

The Alarm widgets bundle is useful for visualization of alarms for specific entities, both in real-time and history modes.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-alarm-bundle-ce.webp" alt="For visualization of alarms for specific entities both in real-time and history mode." loading="lazy"><figcaption>For visualization of alarms for specific entities both in real-time and history mode.</figcaption></figure></div>


### Analog gauges

The Analog Gauges widgets bundle is useful for visualization of temperature, humidity, speed, and other integer or float values.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-analog-gauges-bundle-ce.webp" alt="For visualization of temperature, humidity, speed, and other integer or float values." loading="lazy"><figcaption>For visualization of temperature, humidity, speed, and other integer or float values.</figcaption></figure></div>


### Buttons

The Buttons bundle allows you to organize navigation between dashboard states, send RPC commands to devices, and update device attributes or time-series data.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-buttons-bundle-ce.webp" alt="The Buttons bundle allows you to organize navigation between dashboard states, send RPC commands to devices, and update device attributes or time-series data." loading="lazy"><figcaption>The Buttons bundle allows you to organize navigation between dashboard states, send RPC commands to devices, and update device attributes or time-series data.</figcaption></figure></div>


### Cards

The Cards bundle is useful for visualization of time series data or attributes in table or card widgets.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-cards-bundle-ce.webp" alt="For visualization of time series data or attributes in a table or card widgets." loading="lazy"><figcaption>For visualization of time series data or attributes in a table or card widgets.</figcaption></figure></div>


### Charts

The Charts bundle is useful for visualization of historical or real-time data with a time window.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-charts-bundle-ce.webp" alt="For visualization of historical or real-time data with a time window." loading="lazy"><figcaption>For visualization of historical or real-time data with a time window.</figcaption></figure></div>


### Control widgets

The Control widgets bundle is useful for visualization of the current state and sending RPC commands to target devices.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-control-bundle-ce.webp" alt="For visualization of current state and sending RPC commands to target devices." loading="lazy"><figcaption>For visualization of current state and sending RPC commands to target devices.</figcaption></figure></div>


### Count widgets

The Counter widgets bundle is useful for counting and visualizing the current number of alarms and entities based on the selected filter.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-count-bundle-ce.webp" alt="For counting and visualizing the number of alarms and entities based on the selected filter." loading="lazy"><figcaption>For counting and visualizing the number of alarms and entities based on the selected filter.</figcaption></figure></div>


### Date

The Date widgets bundle is useful for changing the data range for other widgets on the dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-date-bundle-ce.webp" alt="For changing the data range for other widgets on the dashboard." loading="lazy"><figcaption>For changing the data range for other widgets on the dashboard.</figcaption></figure></div>


### Digital gauges

The Digital Gauges bundle is useful for visualization of temperature, humidity, speed and other integer or float values.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-digital-bundle-ce.webp" alt="For visualization of temperature, humidity, speed, and other integer or float values." loading="lazy"><figcaption>For visualization of temperature, humidity, speed, and other integer or float values.</figcaption></figure></div>


### Edge widgets

The Edge widgets bundle is useful for an overview of entities related to the specified SENTIENT Edge instance.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-edge-bundle-ce.webp" alt="For an overview of entities related to the specified SENTIENT Edge instance." loading="lazy"><figcaption>For an overview of entities related to the specified SENTIENT Edge instance.</figcaption></figure></div>


### Entity admin widgets

The Entity admin widgets are templates of complex widgets that allow listing and creating/updating/deleting devices and assets.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-entity-admin-bundle-ce.webp" alt="For listing and creating/updating/deleting devices and assets." loading="lazy"><figcaption>For listing and creating/updating/deleting devices and assets.</figcaption></figure></div>


### Entity widgets

The Entity admin widgets display a list of entities with their data, counting entities, and display the hierarchy of entities based on their relations.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-entity-widgets-bundle-ce.webp" alt="For displaying a list of entities with their data, counting entities, and displays the hierarchy of entities based on their relations." loading="lazy"><figcaption>For displaying a list of entities with their data, counting entities, and displays the hierarchy of entities based on their relations.</figcaption></figure></div>


### Files


<div class="st-callout info">


**Available only in PE and PaaS.**


</div>


The Files widgets display a list of files or PDF reports as a table. Allows to download and delete the file.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-files-bundle-pe.webp" alt="For displaying a list of files or PDF reports as a table. Allows to download and delete the file." loading="lazy"><figcaption>For displaying a list of files or PDF reports as a table. Allows to download and delete the file.</figcaption></figure></div>


### Gateway widgets

The Gateway widgets bundle is useful for managing extensions.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-gateway-bundle-ce.webp" alt="The Gateway widgets bundle is useful to manage SENTIENT IoT Gateway instances." loading="lazy"><figcaption>The Gateway widgets bundle is useful to manage SENTIENT IoT Gateway instances.</figcaption></figure></div>


### General high-performance SCADA symbols

This bundle contains high-performance SCADA widgets for broad industrial monitoring and control. It covers elements ranging from panels and gauges to mechanical assets and site facilities. 
Use it to assemble clean, high-contrast HMI screens that convey status at a glance across mixed-equipment dashboards.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-scada-hp-general-symbols-1-ce.webp" alt="This bundle contains high-performance SCADA widgets for broad industrial monitoring and control. It covers elements ranging from panels and gauges to mechanical assets and site facilities. Use it to assemble clean, high-contrast HMI screens that convey status at a glance across mixed-equipment dashboards." loading="lazy"><figcaption>This bundle contains high-performance SCADA widgets for broad industrial monitoring and control. It covers elements ranging from panels and gauges to mechanical assets and site facilities. Use it to assemble clean, high-contrast HMI screens that convey status at a glance across mixed-equipment dashboards.</figcaption></figure></div>


### GPIO widgets

The GPIO widgets bundle is useful for visualization and controlling GPIO state for target devices.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-gpio-ce.webp" alt="For visualization and control of GPIO state for target devices." loading="lazy"><figcaption>For visualization and control of GPIO state for target devices.</figcaption></figure></div>


### High-performance SCADA energy system

This bundle contains high-performance SCADA symbols that cover the complete electrical flow — from renewable generation (solar, wind) and backup generators through storage, conversion, protection, metering, and low/high-voltage distribution to residential and industrial consumers. 
It is ideal for building interactive dashboards that visualize production, quality, and consumption across modern energy infrastructures.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-scada-hp-energy-system-1-ce.webp" alt="This bundle contains high-performance SCADA symbols that cover the complete electrical flow — from renewable generation (solar, wind) and backup generators through storage, conversion, protection, metering, and low/high-voltage distribution to residential and industrial consumers. It is ideal for building interactive dashboards that visualize production, quality, and consumption across modern energy infrastructures." loading="lazy"><figcaption>This bundle contains high-performance SCADA symbols that cover the complete electrical flow — from renewable generation (solar, wind) and backup generators through storage, conversion, protection, metering, and low/high-voltage distribution to residential and industrial consumers. It is ideal for building interactive dashboards that visualize production, quality, and consumption across modern energy infrastructures.</figcaption></figure></div>


### High-performance SCADA fluid system

This high-performance symbol bundle is focused on fluid-handling processes in oil-and-gas, chemical, and water-treatment domains. 
It spans drilling and well-control components, pumps and pipelines, separators, heat-exchange units, turbines, and related equipment—ideal for flow diagrams, production dashboards, and process-safety views.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-scada-hp-fluid-system-1-ce.webp" alt="This high-performance symbol bundle is focused on fluid-handling processes in oil-and-gas, chemical, and water-treatment domains. It spans drilling and well-control components, pumps and pipelines, separators, heat-exchange units, turbines, and related equipment—ideal for flow diagrams, production dashboards, and process-safety views." loading="lazy"><figcaption>This high-performance symbol bundle is focused on fluid-handling processes in oil-and-gas, chemical, and water-treatment domains. It spans drilling and well-control components, pumps and pipelines, separators, heat-exchange units, turbines, and related equipment—ideal for flow diagrams, production dashboards, and process-safety views.</figcaption></figure></div>


### High-performance SCADA oil & gas

The bundle of high-performance SCADA symbols designed for upstream and early-stage processing workflows in the oil and gas sector.
It covers drilling and well-control equipment, artificial lift and drive units, surface gathering lines, separator trains, heat exchange, and power generation assets — everything needed to visualize the complete flow from wellhead to initial treatment in a clean High-performance SCADA style.
Perfect for real-time dashboards that track drilling progress, production efficiency, and safety barriers across both onshore and offshore installations.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-scada-hp-fluid-oil-and-gas-1-ce.webp" alt="The bundle of high-performance SCADA symbols designed for upstream and early-stage processing workflows in the oil and gas sector. It covers drilling and well-control equipment, artificial lift and drive units, surface gathering lines, separator trains, heat exchange, and power generation assets — everything needed to visualize the complete flow from wellhead to initial treatment in a clean High-performance SCADA style. Perfect for real-time dashboards that track drilling progress, production efficiency, and safety barriers across both onshore and offshore installations." loading="lazy"><figcaption>The bundle of high-performance SCADA symbols designed for upstream and early-stage processing workflows in the oil and gas sector. It covers drilling and well-control equipment, artificial lift and drive units, surface gathering lines, separator trains, heat exchange, and power generation assets — everything needed to visualize the complete flow from wellhead to initial treatment in a clean High-performance SCADA style. Perfect for real-time dashboards that track drilling progress, production efficiency, and safety barriers across both onshore and offshore installations.</figcaption></figure></div>


### Home page widgets

The Home page widgets bundle is useful for customizing and displaying quick links to the platform's UI components, documentation, or any other resources on the home page, displaying statistics about the number of entities and API usege, etc.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-home-page-bundles-ce.webp" alt="For customize and display quick links to the platform&#39;s UI components, documentation or any other resources on the home page, display statistics about the number of entities and API usage, etc." loading="lazy"><figcaption>For customize and display quick links to the platform&#39;s UI components, documentation or any other resources on the home page, display statistics about the number of entities and API usage, etc.</figcaption></figure></div>


### HTML widgets

The HTML widgets bundle is useful for injecting custom HTML code. Or for displaying configurable HTML with the ability to inject values from the selected data source.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-html-bundle-ce.webp" alt="For injecting custom HTML code. And for displaying configurable HTML with the ability to inject values from the selected data source." loading="lazy"><figcaption>For injecting custom HTML code. And for displaying configurable HTML with the ability to inject values from the selected data source.</figcaption></figure></div>


### Indoor Environment

The Indoor Environment widget bundle is effective in visualizing data related to indoor environments.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-indoor-environment-bundle-ce.webp" alt="The Indoor Environment widgets bundle is useful for displaying indoor environment telemetry data." loading="lazy"><figcaption>The Indoor Environment widgets bundle is useful for displaying indoor environment telemetry data.</figcaption></figure></div>


### Industrial widgets

The Industrial widgets bundle is useful for displaying industrial telemetry data.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-industrial-bundle-1-ce.webp" alt="The Industrial widgets bundle is useful for displaying industrial telemetry data." loading="lazy"><figcaption>The Industrial widgets bundle is useful for displaying industrial telemetry data.</figcaption></figure></div>


### Input widgets

The Input widgets bundle is useful for modifying the attributes of an entity.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-input-bundle-ce.webp" alt="For changing entity attributes." loading="lazy"><figcaption>For changing entity attributes.</figcaption></figure></div>


### Liquid level

The Liquid level widgets bundle includes widgets for visualizing the level of liquid inside the tank.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-liquid-level-bundle-ce.webp" alt="For changing entity attributes." loading="lazy"><figcaption>For changing entity attributes.</figcaption></figure></div>


### Maps

The Map widgets bundle is useful for visualizing the geographic location of devices and tracking device routes in both real-time and history modes.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-maps-bundle-ce.webp" alt="For visualization of devices&#39; geolocations and tracking devices routes both in real-time and history mode." loading="lazy"><figcaption>For visualization of devices&#39; geolocations and tracking devices routes both in real-time and history mode.</figcaption></figure></div>


### Navigation widgets

The Navigation widgets bundle is useful for defining the home dashboard of the user.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-navigation-bundle-ce.webp" alt="For defining home dashboard of the user." loading="lazy"><figcaption>For defining home dashboard of the user.</figcaption></figure></div>


### Outdoor Environment

The Outdoor Environment widget bundle is effective in visualizing data related to outdoor environments.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-outdoor-environment-bundle-ce.webp" alt="For scheduling various types of events with flexible schedule configuration." loading="lazy"><figcaption>For scheduling various types of events with flexible schedule configuration.</figcaption></figure></div>


### SCADA symbols

Use for uploading SVG symbols to your SCADA dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-scada-symbols-bundle-ce.webp" alt="For uploading SVG symbols to your SCADA dashboard." loading="lazy"><figcaption>For uploading SVG symbols to your SCADA dashboard.</figcaption></figure></div>


### Scheduling


<div class="st-callout info">


**Available only in PE and PaaS.**


</div>


The Scheduling widgets bundle is useful for [scheduling](/docs/user-guide/scheduler/) various types of events with flexible schedule configuration.  


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-scheduling-bundle-pe.webp" alt="For scheduling various types of events with flexible schedule configuration." loading="lazy"><figcaption>For scheduling various types of events with flexible schedule configuration.</figcaption></figure></div>


### Status indicators

The Status indicators widgets bundle includes widgets for visualizing battery level, signal strength, and progress bar.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-status-indicators-bundle-ce.webp" alt="For scheduling various types of events with flexible schedule configuration." loading="lazy"><figcaption>For scheduling various types of events with flexible schedule configuration.</figcaption></figure></div>


### Tables

The Tables widgets bundle is useful when you need to display a list of entities, a list of alarm signals, and time series data for one or several entities.
Additionally, this widget bundle showcases Persistent RPC requests, which are based on entity alias. 
It can also be filtered optionally and supports pagination for enhanced usability.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-tables-bundle-ce.webp" alt="For displaying a list of entities, a list of alarm signals, and time series data for one or several entities, and for displaying Persistent RPC requests based on entity alias and optional filter with the ability of pagination." loading="lazy"><figcaption>For displaying a list of entities, a list of alarm signals, and time series data for one or several entities, and for displaying Persistent RPC requests based on entity alias and optional filter with the ability of pagination.</figcaption></figure></div>


### Traditional SCADA fluid system

This bundle of SCADA symbols in a traditional design style covers the essentials for many industrial diagrams. 
It packs straight and elbow pipes, tees, drains, flow & level meters, pumps, filters, valves, tanks of various shapes, pools, and other core components - everything you need to assemble piping, hydraulic, and other process-control schematics with ease.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-scada-traditional-fluid-system-1-ce.webp" alt="This bundle of SCADA symbols in a traditional design style covers the essentials for many industrial diagrams. It packs straight and elbow pipes, tees, drains, flow & level meters, pumps, filters, valves, tanks of various shapes, pools, and other core components - everything you need to assemble piping, hydraulic, and other process-control schematics with ease." loading="lazy"><figcaption>This bundle of SCADA symbols in a traditional design style covers the essentials for many industrial diagrams. It packs straight and elbow pipes, tees, drains, flow & level meters, pumps, filters, valves, tanks of various shapes, pools, and other core components - everything you need to assemble piping, hydraulic, and other process-control schematics with ease.</figcaption></figure></div>


## Operations with Widget

### Adding Widget

When a system administrator adds a new widget, it automatically becomes a system widget.
This means that only the administrator has the privilege to modify, or delete the widget.
Tenant administrators can also create widgets, but they are granted permission to modify only the widgets they have created.
You can always implement and add your widgets by following this [guide](/docs/user-guide/contribution/widgets-development/).

To add a new widget, you should:


1. Navigate to the "Widgets Library" page using the main menu on the left. Click the "+" icon in the upper right corner of the screen, and select the "Create new widget" option from the drop-down menu;

1. In the pop-up window select widget type;

1. In the dialog window that appears, enter the name of the new widget, input the widget JavaScript code, and then click "Save" to complete the widget creation;

1. The new widget is created.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-add-new-widget-1-ce.webp" alt="Navigate to the &quot;Widgets Library&quot; page using the main menu on the left. Click the &quot;+&quot; icon in the upper right corner of the screen, and select the &quot;Create new widget&quot; option from the drop-down menu;" loading="lazy"><figcaption>Navigate to the "Widgets Library" page using the main menu on the left. Click the "+" icon in the upper right corner of the screen, and select the "Create new widget" option from the drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-add-new-widget-2-ce.webp" alt="In the pop-up window select widget type;" loading="lazy"><figcaption>In the pop-up window select widget type;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-add-new-widget-3-ce.webp" alt="In the dialog window that appears, enter the name of the new widget, input the widget JavaScript code, and then click &quot;Save&quot; to complete the widget creation;" loading="lazy"><figcaption>In the dialog window that appears, enter the name of the new widget, input the widget JavaScript code, and then click "Save" to complete the widget creation;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-add-new-widget-4-ce.webp" alt="The new widget is created." loading="lazy"><figcaption>The new widget is created.</figcaption></figure></div>


### Exporting Widget

You can export a specific type of widget from a widget bundle in JSON format, and import it in the same or different SENTIENT instance.

In order to export a widget type, you should go to the Widgets Library page, navigate to the "Widgets" tab and click the export button on the particular widget card. The widget configuration file will be saved in JSON format on your computer.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-export-widget-1-ce.webp" alt="Click the export button on the particular widget card. The widget configuration file will be saved in JSON format on your computer." loading="lazy"><figcaption>Click the export button on the particular widget card. The widget configuration file will be saved in JSON format on your computer.</figcaption></figure></div>


### Importing Widget

Please note that only system administrators can modify system (default) widgets. This includes the ability to edit, delete, add, or import widgets within the bundle.
When a system administrator creates a new widget bundle, it's set as a system-level item for tenants, preventing them from modifying it.
Nevertheless, tenants can add their own widgets. In this case, they have full rights to manage created widget types inside the bundle.

To import a widget, you should:


1. Click the "+" button in the upper right corner of the "Widgets" page. Select "Import widget" from the drop-down menu;

1. In the pop-up, you will be prompted to upload the JSON file. Drag and drop a file from your computer, then click the "Import" to add a widget to the widget bundle;

1. The widget is imported.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-import-widget-1-ce.webp" alt="Click the &quot;+&quot; button in the upper right corner of the &quot;Widgets&quot; page. Select &quot;Import widget&quot; from the drop-down menu;" loading="lazy"><figcaption>Click the "+" button in the upper right corner of the "Widgets" page. Select "Import widget" from the drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-import-widget-2-ce.webp" alt="In the pop-up, you will be prompted to upload the JSON file. Drag and drop a file from your computer, then click the &quot;Import&quot; to add a widget to the widget bundle;" loading="lazy"><figcaption>In the pop-up, you will be prompted to upload the JSON file. Drag and drop a file from your computer, then click the "Import" to add a widget to the widget bundle;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-import-widget-3-ce.webp" alt="The widget is imported." loading="lazy"><figcaption>The widget is imported.</figcaption></figure></div>


### Deleting Widget

The system administrator or tenant administrator can delete a widget type using one of the following ways:

First way:


1. Click a "Trash" icon in the widget&#39;s row you want to delete;

1. Confirm deleting the widget in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-delete-widget-1-ce.webp" alt="Click a &quot;Trash&quot; icon in the widget&#39;s row you want to delete;" loading="lazy"><figcaption>Click a "Trash" icon in the widget&#39;s row you want to delete;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-delete-widget-2-ce.webp" alt="Confirm deleting the widget in the dialog box." loading="lazy"><figcaption>Confirm deleting the widget in the dialog box.</figcaption></figure></div>


Second way:


1. Click a "Pencil" icon in the widget&#39;s row to open widget details;

1. Click the "Delete widget" button;

1. Confirm deleting the widget in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-delete-widget-3-ce.webp" alt="Click a &quot;Pencil&quot; icon in the widget&#39;s row to open widget details;" loading="lazy"><figcaption>Click a "Pencil" icon in the widget&#39;s row to open widget details;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-delete-widget-4-ce.webp" alt="Click the &quot;Delete widget&quot; button;" loading="lazy"><figcaption>Click the "Delete widget" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-delete-widget-5-ce.webp" alt="Confirm deleting the widget in the dialog box." loading="lazy"><figcaption>Confirm deleting the widget in the dialog box.</figcaption></figure></div>


## Operations with Widgets Bundle

### Adding Widgets Bundle

When a system administrator adds a new widgets bundle, it automatically becomes a system widgets bundle.
It means that only they can delete, edit, and add widget to the bundle. 
Tenant administrators can create widget bundles as well. In this case, they have permission to modify already created bundles.
You can always implement and add your widgets by following this [guide](/docs/user-guide/contribution/widgets-development/).

To add a new widgets bundle, you should:


1. Navigate to the "Widgets bundle" page using the main menu on the left. Click the "+" icon in the upper right corner of the screen, and select the "Create new widgets bundle" option from the drop-down menu;

1. In the opened dialog window, enter the name of the new bundle. Adding an image and a description is optional. Click "Add";

1. After creating the widget bundle, it will be automatically opened. Now, you can add widgets there. To add your own existing widget, click the "+ Add existing widget" button in the center of the window. To create (or import) a new widget, click the plus icon in the top right corner of the window. Now, click the "+Add existing widget" button in the center of the window;

1. Click on the "Widgets" row and select your widget from drop-down menu;

1. Click "Save" to complete adding the widget to your widget bundle;

1. Since widget bundles are alphabetically ordered, the newly created one may be on a different page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-add-new-bundle-1-ce.webp" alt="Navigate to the &quot;Widgets bundle&quot; page using the main menu on the left. Click the &quot;+&quot; icon in the upper right corner of the screen, and select the &quot;Create new widgets bundle&quot; option from the drop-down menu;" loading="lazy"><figcaption>Navigate to the "Widgets bundle" page using the main menu on the left. Click the "+" icon in the upper right corner of the screen, and select the "Create new widgets bundle" option from the drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-add-new-bundle-2-ce.webp" alt="In the opened dialog window, enter the name of the new bundle. Adding an image and a description is optional. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the opened dialog window, enter the name of the new bundle. Adding an image and a description is optional. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-add-new-bundle-3-ce.webp" alt="After creating the widget bundle, it will be automatically opened. Now, you can add widgets there. To add your own existing widget, click the &quot;+ Add existing widget&quot; button in the center of the window. To create (or import) a new widget, click the plus icon in the top right corner of the window. Now, click the &quot;+Add existing widget&quot; button in the center of the window;" loading="lazy"><figcaption>After creating the widget bundle, it will be automatically opened. Now, you can add widgets there. To add your own existing widget, click the "+ Add existing widget" button in the center of the window. To create (or import) a new widget, click the plus icon in the top right corner of the window. Now, click the "+Add existing widget" button in the center of the window;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-add-new-bundle-4-ce.webp" alt="Click on the &quot;Widgets&quot; row and select your widget from drop-down menu;" loading="lazy"><figcaption>Click on the "Widgets" row and select your widget from drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-add-new-bundle-5-ce.webp" alt="Click &quot;Save&quot; to complete adding the widget to your widget bundle;" loading="lazy"><figcaption>Click "Save" to complete adding the widget to your widget bundle;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-add-new-bundle-6-ce.webp" alt="Since widget bundles are alphabetically ordered, the newly created one may be on a different page." loading="lazy"><figcaption>Since widget bundles are alphabetically ordered, the newly created one may be on a different page.</figcaption></figure></div>


### Exporting Widgets Bundle 

You can export a widgets bundle in JSON format, and import it in the same or different SENTIENT instance.

In order to export widgets bundle, you should:


1. Click the export button on the specific widgets bundle row;

1. In the pop-up window, optionally check the "Include bundle widget types in exported data", then click "Export". The widgets bundle configuration file will be saved in JSON format on your computer.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-export-bundle-1-ce.webp" alt="Click the export button on the specific widgets bundle row;" loading="lazy"><figcaption>Click the export button on the specific widgets bundle row;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-export-bundle-2-ce.webp" alt="In the pop-up window, optionally check the &quot;Include bundle widget types in exported data&quot;, then click &quot;Export&quot;. The widgets bundle configuration file will be saved in JSON format on your computer." loading="lazy"><figcaption>In the pop-up window, optionally check the "Include bundle widget types in exported data", then click "Export". The widgets bundle configuration file will be saved in JSON format on your computer.</figcaption></figure></div>


### Importing Widgets Bundle

To import a widgets bundle, you should: 


1. Click the "+" button in the upper right corner of the "Widgets Bundles" page. Select "Import widgets bundle" from the drop-down menu;

1. In the pop-up, you will be prompted to upload the JSON file. Drag and drop a file from your computer, then click "Import" to add a widget bundle to the library;

1. The widgets bundle is imported


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-import-bundle-1-ce.webp" alt="Click the &quot;+&quot; button in the upper right corner of the &quot;Widgets Bundles&quot; page. Select &quot;Import widgets bundle&quot; from the drop-down menu;" loading="lazy"><figcaption>Click the "+" button in the upper right corner of the "Widgets Bundles" page. Select "Import widgets bundle" from the drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-import-bundle-2-ce.webp" alt="In the pop-up, you will be prompted to upload the JSON file. Drag and drop a file from your computer, then click &quot;Import&quot; to add a widget bundle to the library;" loading="lazy"><figcaption>In the pop-up, you will be prompted to upload the JSON file. Drag and drop a file from your computer, then click "Import" to add a widget bundle to the library;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-import-bundle-3-ce.webp" alt="The widgets bundle is imported" loading="lazy"><figcaption>The widgets bundle is imported</figcaption></figure></div>


### Deleting Widgets Bundle

The system administrator or tenant administrator can delete a widgets bundle using one of the following ways:

First way:


1. Click a "Trash" icon next to the name of the widgets bundle you want to delete;

1. Confirm deleting the widgets bundle in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-delete-widget-bundle-1-ce.webp" alt="Click a &quot;Trash&quot; icon next to the name of the widgets bundle you want to delete;" loading="lazy"><figcaption>Click a "Trash" icon next to the name of the widgets bundle you want to delete;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-delete-widget-bundle-2-ce.webp" alt="Confirm deleting the widgets bundle in the dialog box." loading="lazy"><figcaption>Confirm deleting the widgets bundle in the dialog box.</figcaption></figure></div>


Second way:


1. Click a "Pencil" icon in the widgets bundle row to open widgets bundle details;

1. Click the "Delete widgets bundle" button;

1. Confirm deleting the widgets bundle in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-delete-widget-bundle-3-ce.webp" alt="Click a &quot;Pencil&quot; icon in the widgets bundle row to open widgets bundle details;" loading="lazy"><figcaption>Click a "Pencil" icon in the widgets bundle row to open widgets bundle details;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-delete-widget-bundle-4-ce.webp" alt="Click the &quot;Delete widgets bundle&quot; button;" loading="lazy"><figcaption>Click the "Delete widgets bundle" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/widget-library/wl-delete-widget-bundle-5-ce.webp" alt="Confirm deleting the widgets bundle in the dialog box." loading="lazy"><figcaption>Confirm deleting the widgets bundle in the dialog box.</figcaption></figure></div>
