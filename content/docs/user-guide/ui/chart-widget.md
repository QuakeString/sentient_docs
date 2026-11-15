+++
title = "Chart Widgets"
description = "SENTIENT Chart Widgets management"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/chart-widget.md"
+++
## Overview

This guide will study Chart widgets: their functionality, features, basic and advanced settings of the widgets, and widgets’ data keys.

Chart widgets allow you to display time series data with customizable line charts and bar charts. Moreover, you can use various pie charts to display the latest values.

## How to create a Chart widget

To add any chart widgets to your dashboards, you should:


1. Enter edit mode by clicking the pencil icon in the lower right corner of the screen.

1. To add a widget, either click the sign "Add new widget" in the center of the screen or open the drop up menu by clicking the plus icon and selecting "Create new widget".

1. From the widgets bundle, select Charts.

1. Select the preferred widget from the Chart bundle.

1. In the "Add Widget" dialog, click the Add button to add a Data source.

1. Add Entity alias and Entity time series, then click "Add".

1. While still in edit mode, drag the widget corners to adjust its size. After that, click the orange checkmark to save all applied changes.

1. Now you have the Chart widget on your dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/charts-addwidget-ce.webp" alt="Enter edit mode by clicking the pencil icon in the lower right corner of the screen." loading="lazy"><figcaption>Enter edit mode by clicking the pencil icon in the lower right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/charts-addwidget-1-ce.webp" alt="To add a widget, either click the sign &quot;Add new widget&quot; in the center of the screen or open the drop up menu by clicking the plus icon and selecting &quot;Create new widget&quot;." loading="lazy"><figcaption>To add a widget, either click the sign "Add new widget" in the center of the screen or open the drop up menu by clicking the plus icon and selecting "Create new widget".</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/charts-addwidget-2-ce.webp" alt="From the widgets bundle, select Charts." loading="lazy"><figcaption>From the widgets bundle, select Charts.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/charts-addwidget-3-ce.webp" alt="Select the preferred widget from the Chart bundle." loading="lazy"><figcaption>Select the preferred widget from the Chart bundle.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/charts-addwidget-4-ce.webp" alt="In the &quot;Add Widget&quot; dialog, click the Add button to add a Data source." loading="lazy"><figcaption>In the "Add Widget" dialog, click the Add button to add a Data source.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/charts-addwidget-5-ce.webp" alt="Add Entity alias and Entity time series, then click &quot;Add&quot;." loading="lazy"><figcaption>Add Entity alias and Entity time series, then click "Add".</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/charts-addwidget-6-ce.webp" alt="While still in edit mode, drag the widget corners to adjust its size. After that, click the orange checkmark to save all applied changes." loading="lazy"><figcaption>While still in edit mode, drag the widget corners to adjust its size. After that, click the orange checkmark to save all applied changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/charts-addwidget-7-ce.webp" alt="Now you have the Chart widget on your dashboard." loading="lazy"><figcaption>Now you have the Chart widget on your dashboard.</figcaption></figure></div>


## Chart widget types

Chart widgets are divided into Time series and Latest value widgets. Time series widgets are useful for visualizing changes in time series data over time.
Latest values widgets are used when you need to see the latest attribute values or time series data for multiple entities.

### Time series widgets

Time series widgets visualize changes in time series data over time. Read [here](/docs/user-guide/dashboards/#time-window) how to set up the time window.

#### Bar Chart

[Bar Chart](/docs/user-guide/ui/chart-widget/#timeseries-bar-chart) widget displays changes to time series data over time. The example shows the temperature readings.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/charts-bar-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### Line Chart

[Line Chart](/docs/user-guide/ui/chart-widget/#timeseries-line-chart) widget displays changes to time series data over time. The example shows temperature and humidity readings.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/charts-line-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### State Chart

[State Chart](/docs/user-guide/ui/chart-widget/#state-chart-1) widget displays changes to the state of the entity over time. 
For example, if a device on and off, its states and conditions.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/charts-state-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Last values widgets

Latest values widgets render the latest values of attributes or time series data for multiple entities. Latest values widgets mostly support numeric values.

#### Radar

Radar widget displays the latest attribute or time series data values for multiple entities in a radar chart. Supports numeric values only.

In the example, the widget displays the latest pressure time series data for three devices.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/charts-radar-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### Polar Area

Polar Area widget displays the latest attribute or time series data values for multiple entities in a polar area chart. Supports numeric values only.

In the example, the widget displays the latest pressure time series data for three devices.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/charts-polar-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### Pie - Chart.js

Pie - Chart.js widget displays the latest attribute or time series data values for multiple entities in a pie chart. Supports numeric values only.

In the example, the widget displays the latest temperature time series data values for three devices.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/charts-piejs-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### Pie - Flot

[Pie - Flot](/docs/user-guide/ui/chart-widget/#latest-values-pie---flot) widget displays the latest attribute or time series data values for multiple entities in a pie chart. 
Supports numeric values only.

In the example, the widget displays the latest pressure time series data values for three devices.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/charts-pieflot-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### Doughnut

[Doughnut](/docs/user-guide/ui/chart-widget/#latest-values-doughnut) widget displays the latest attribute or time series data values for multiple entities in a donut chart. 
Supports numeric values only.

In the example, the widget displays the latest humidity time series data values for three devices.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/charts-doughnut-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### Bars

Bars widget displays the latest values of the attributes or time series data for multiple entities as separate bars.
The only latest values chart widget that allows using not only numeric values.

In the example, widget is displaying the latest pressure time series data values for three devices.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/charts-bars-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Chart widget settings

### Basic widget settings 

Basic widget settings are responsible for the appearance and style of the widget: from the title style and legend configuration to the settings for mobile devices. 
All of SENTIENT widgets have the same basic settings, you can learn how to customize them [here](/docs/user-guide/dashboards/#basic-widget-settings).

### Advanced widgets settings

Advanced widget settings vary for different widget types. Advanced settings are responsible for configuring the unique features of the specific widget.  
To enter the widget Edit mode and start configuring its Advanced settings, first enter the dashboard edit mode. Then, you should:


1. Click the pencil icon in the right corner of the widget to enter the widget edit mode.

1. Click the third tab "Advanced".


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/barchart-advanced-ce.webp" alt="Click the pencil icon in the right corner of the widget to enter the widget edit mode." loading="lazy"><figcaption>Click the pencil icon in the right corner of the widget to enter the widget edit mode.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/barchart-advanced-1-ce.webp" alt="Click the third tab &quot;Advanced&quot;." loading="lazy"><figcaption>Click the third tab "Advanced".</figcaption></figure></div>


#### Time series Bar Chart

##### 1. Common Settings

**1.1.** Stacking

Use this function if the data aggregation function **is not** set to None.
If the Stacking box checked, the bar will be split according to the values of the entities used.
If this box isn't checked, the widget will show you the sum of the used entity values. To see the values of all entities, you need to hover your mouse over the bar.


1. In the upper right corner of the screen, click on the Time window configuration and choose any preferred Data aggregation function other than None. Click "Update" to apply changes.

1. Go to widgets Edit mode by clicking the pencil icon in the upper right corner of the screen.

1. In the Advanced tab, disable the Stacking box and apply changes by clicking the orange checkmark in the upper right corner of the window.

1. After changes have been applied, click the orange checkmark in the lower corner of the screen to save them.

1. Hover the mouse over a bar to see values of all entities.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/bars-stacking-ce.webp" alt="In the upper right corner of the screen, click on the Time window configuration and choose any preferred Data aggregation function other than None. Click &quot;Update&quot; to apply changes." loading="lazy"><figcaption>In the upper right corner of the screen, click on the Time window configuration and choose any preferred Data aggregation function other than None. Click "Update" to apply changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-stacking-1-ce.webp" alt="Go to widgets Edit mode by clicking the pencil icon in the upper right corner of the screen." loading="lazy"><figcaption>Go to widgets Edit mode by clicking the pencil icon in the upper right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-stacking-2-ce.webp" alt="In the Advanced tab, disable the Stacking box and apply changes by clicking the orange checkmark in the upper right corner of the window." loading="lazy"><figcaption>In the Advanced tab, disable the Stacking box and apply changes by clicking the orange checkmark in the upper right corner of the window.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-stacking-3-ce.webp" alt="After changes have been applied, click the orange checkmark in the lower corner of the screen to save them." loading="lazy"><figcaption>After changes have been applied, click the orange checkmark in the lower corner of the screen to save them.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-stacking-4-ce.webp" alt="Hover the mouse over a bar to see values of all entities." loading="lazy"><figcaption>Hover the mouse over a bar to see values of all entities.</figcaption></figure></div>


If your data is not aggregated, you can adjust **the Default bar width for non-aggregated data (milliseconds)** by changing the number. This action makes the bars of the chart wider.

**Bar alignment** is responsible for the placement of the bars on the Chart widget relative to the time point.

**Default line width for all thresholds**, **Shadow size**, **Font color and size** work for Time series Line Chart and State Chart widgets.

**Tooltip value format function, f(value)** is used when you want to manually customize the tooltip.
You can customize the values that will be displayed in the tooltip via [Settings](/docs/user-guide/dashboards/#5-other-settings) or 
[Advanced Data key configuration](/docs/user-guide/ui/advanced-data-key-configuration/#2-charts). 
Tooltip configuration via Settings is basic and applied to all entities at the same time. When configured in the Advanced Data key configuration,
it is applied only to the specific time series data, and the basic tooltip function will be overwritten by this configuration.

But, if you need something really special for your widget, the Tooltip value format function is for you.
Suppose you have temperature readings, and you'd like to see Celsius and Fahrenheit values on your widget, which will be displayed with two floating points.


1. Input your custom Tooltip value format function and apply changes by clicking orange checkmark in the upper right corner of the window.

1. To see tooltip, you need to save applied changes by clicking the orange checkmark in the lower corner of the screen.

1. Hover the mouse over the widget to see tooltip with applied Tooltip value format function.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/bars-tooltipfunction-ce.webp" alt="Input your custom Tooltip value format function and apply changes by clicking orange checkmark in the upper right corner of the window." loading="lazy"><figcaption>Input your custom Tooltip value format function and apply changes by clicking orange checkmark in the upper right corner of the window.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-tooltipfunction-1-ce.webp" alt="To see tooltip, you need to save applied changes by clicking the orange checkmark in the lower corner of the screen." loading="lazy"><figcaption>To see tooltip, you need to save applied changes by clicking the orange checkmark in the lower corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-tooltipfunction-2-ce.webp" alt="Hover the mouse over the widget to see tooltip with applied Tooltip value format function." loading="lazy"><figcaption>Hover the mouse over the widget to see tooltip with applied Tooltip value format function.</figcaption></figure></div>


**1.2.** Grid settings

You can change the appearance of the Chart grid: customize the color of the background, the grid frame and its ticks; change the width of the lines and turn off their visibility.


1. In Advanced tab, go to the Grid settings and click on the icon of Primary color circle. In the opened dialog box, move sliders to adjust color and transparency. Click "Select" when you finished, to apply changes.

1. Configure preferred Grid settings and apply changes by clicking orange checkmark in the upper right corner of the window.

1. This set of applied colors is just an example. To save applied changes, click the orange checkmark in the lower corner of the screen.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/bars-grid-ce.webp" alt="In Advanced tab, go to the Grid settings and click on the icon of Primary color circle. In the opened dialog box, move sliders to adjust color and transparency. Click &quot;Select&quot; when you finished, to apply changes." loading="lazy"><figcaption>In Advanced tab, go to the Grid settings and click on the icon of Primary color circle. In the opened dialog box, move sliders to adjust color and transparency. Click "Select" when you finished, to apply changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-grid-1-ce.webp" alt="Configure preferred Grid settings and apply changes by clicking orange checkmark in the upper right corner of the window." loading="lazy"><figcaption>Configure preferred Grid settings and apply changes by clicking orange checkmark in the upper right corner of the window.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-grid-2-ce.webp" alt="This set of applied colors is just an example. To save applied changes, click the orange checkmark in the lower corner of the screen." loading="lazy"><figcaption>This set of applied colors is just an example. To save applied changes, click the orange checkmark in the lower corner of the screen.</figcaption></figure></div>


**1.3.** Axis settings


1. Configure preferred axis settings and click the orange checkmark in the upper right corner of the window to apply changes.

1. As you see, titles have been added, colors of axis have been changed and values have been adjusted according to the applied changes. To save these changes, click the orange checkmark in the lower corner of the screen.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/bars-axis-ce.webp" alt="Configure preferred axis settings and click the orange checkmark in the upper right corner of the window to apply changes." loading="lazy"><figcaption>Configure preferred axis settings and click the orange checkmark in the upper right corner of the window to apply changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-axis-1-ce.webp" alt="As you see, titles have been added, colors of axis have been changed and values have been adjusted according to the applied changes. To save these changes, click the orange checkmark in the lower corner of the screen." loading="lazy"><figcaption>As you see, titles have been added, colors of axis have been changed and values have been adjusted according to the applied changes. To save these changes, click the orange checkmark in the lower corner of the screen.</figcaption></figure></div>


**1.4.** Ticks formatter function, f(value)

Let's say we have telemetry which takes values of very large numbers, especially when there is a special symbol near values.
However, we need to build a small graph (since we don't have a lot of free space on the dashboard).
Therefore, using the ticks-formatter function, we can convert the ticks values to a more compact form.


1. Enter widget edit mode by clicking the pencil icon in the right corner of the widget.

1. In the Advanced tab, in the Ticks formatter function field, enter the custom function and apply changes by clicking the checkmark in the upper right corner of the window.

1. Function has been applied and values became more compact. Save changes by clicking the checkmark in the lower right corner of the screen.

1. By hovering the mouse over a widget you can see the tooltip with not reduced values.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/bars-ticksfun-ce.webp" alt="Enter widget edit mode by clicking the pencil icon in the right corner of the widget." loading="lazy"><figcaption>Enter widget edit mode by clicking the pencil icon in the right corner of the widget.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-ticksfun-1-ce.webp" alt="In the Advanced tab, in the Ticks formatter function field, enter the custom function and apply changes by clicking the checkmark in the upper right corner of the window." loading="lazy"><figcaption>In the Advanced tab, in the Ticks formatter function field, enter the custom function and apply changes by clicking the checkmark in the upper right corner of the window.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-ticksfun-2-ce.webp" alt="Function has been applied and values became more compact. Save changes by clicking the checkmark in the lower right corner of the screen." loading="lazy"><figcaption>Function has been applied and values became more compact. Save changes by clicking the checkmark in the lower right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-ticksfun-3-ce.webp" alt="By hovering the mouse over a widget you can see the tooltip with not reduced values." loading="lazy"><figcaption>By hovering the mouse over a widget you can see the tooltip with not reduced values.</figcaption></figure></div>


##### 2. Comparison Settings

Comparison settings allow you to compare the difference in values over a specific period of time. Works only in the History time window.


1. Since comparison settings work only in History time window mode, click on the clock icon in the upper right corner and select the History time window there. Click "Update" to apply.

1. In Advanced tab, enable comparison and from the drop-down menu select time to show historical data with which to compare. In the "Second X axis" section, select axis position, where the compared axis will be located on the widget. If you would like title for the second axis, enable "Show labels" and enter the Axis title. When you are done with Comparison Settings configuration, click the orange checkmark in the upper right corner of the window to apply changes.

1. You can see in the widget legend that Comparison Settings have been applied. Save changes by clicking the orange checkmark in the lower right corner of the screen.

1. You can see the tooltip with the comparison data when you hover the mouse over the widget.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/bars-comparison-ce.webp" alt="Since comparison settings work only in History time window mode, click on the clock icon in the upper right corner and select the History time window there. Click &quot;Update&quot; to apply." loading="lazy"><figcaption>Since comparison settings work only in History time window mode, click on the clock icon in the upper right corner and select the History time window there. Click "Update" to apply.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-comparison-1-ce.webp" alt="In Advanced tab, enable comparison and from the drop-down menu select time to show historical data with which to compare. In the &quot;Second X axis&quot; section, select axis position, where the compared axis will be located on the widget. If you would like title for the second axis, enable &quot;Show labels&quot; and enter the Axis title. When you are done with Comparison Settings configuration, click the orange checkmark in the upper right corner of the window to apply changes." loading="lazy"><figcaption>In Advanced tab, enable comparison and from the drop-down menu select time to show historical data with which to compare. In the "Second X axis" section, select axis position, where the compared axis will be located on the widget. If you would like title for the second axis, enable "Show labels" and enter the Axis title. When you are done with Comparison Settings configuration, click the orange checkmark in the upper right corner of the window to apply changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-comparison-2-ce.webp" alt="You can see in the widget legend that Comparison Settings have been applied. Save changes by clicking the orange checkmark in the lower right corner of the screen." loading="lazy"><figcaption>You can see in the widget legend that Comparison Settings have been applied. Save changes by clicking the orange checkmark in the lower right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-comparison-3-ce.webp" alt="You can see the tooltip with the comparison data when you hover the mouse over the widget." loading="lazy"><figcaption>You can see the tooltip with the comparison data when you hover the mouse over the widget.</figcaption></figure></div>


##### 3. Custom Legend Settings

Custom Legend Settings are for cases when you need to display data that cannot be displayed in the chart such as attributes or display specific time series only in the Chart legend.
For the example let's use active/inactive attributes that can not be displayed on a Chart, only in a Table widget.


1. In the Advanced tab, enable custom legend to use attribute or time series values in key labels. Click the "+ New" button. From the appeared drop-down menu, select key type. The Key name is entered in the line below. Apply all configured settings by click the orange checkmark in the upper right corner of the window.

1. Go to Data tab and click the pencil icon on the data key to enter Data key configuration.

1. In the label line, enter the patter ${} with the data key name inside the brackets. Click "Save" to apply new label name.

1. Click the orange checkmark in the upper right corner of the screen to apply data key changes.

1. As you can see on the widget, custom legend settings have been applied. To save changes, click the orange checkmark in the lower right corner of the screen.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/bars-legend-ce.webp" alt="In the Advanced tab, enable custom legend to use attribute or time series values in key labels. Click the &quot;+ New&quot; button. From the appeared drop-down menu, select key type. The Key name is entered in the line below. Apply all configured settings by click the orange checkmark in the upper right corner of the window." loading="lazy"><figcaption>In the Advanced tab, enable custom legend to use attribute or time series values in key labels. Click the "+ New" button. From the appeared drop-down menu, select key type. The Key name is entered in the line below. Apply all configured settings by click the orange checkmark in the upper right corner of the window.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-legend-1-ce.webp" alt="Go to Data tab and click the pencil icon on the data key to enter Data key configuration." loading="lazy"><figcaption>Go to Data tab and click the pencil icon on the data key to enter Data key configuration.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-legend-2-ce.webp" alt="In the label line, enter the patter ${} with the data key name inside the brackets. Click &quot;Save&quot; to apply new label name." loading="lazy"><figcaption>In the label line, enter the patter ${} with the data key name inside the brackets. Click "Save" to apply new label name.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-legend-3-ce.webp" alt="Click the orange checkmark in the upper right corner of the screen to apply data key changes." loading="lazy"><figcaption>Click the orange checkmark in the upper right corner of the screen to apply data key changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/bars-legend-4-ce.webp" alt="As you can see on the widget, custom legend settings have been applied. To save changes, click the orange checkmark in the lower right corner of the screen." loading="lazy"><figcaption>As you can see on the widget, custom legend settings have been applied. To save changes, click the orange checkmark in the lower right corner of the screen.</figcaption></figure></div>


#### Time series Line Chart

Advanced settings for the _Time series Line Chart_ widget are the same as for Time series Bar Chart. You can learn about these settings [above](/docs/user-guide/ui/chart-widget/#timeseries-bar-chart).

##### 1. Display smooth (curved) lines 


1. In the Advanced tab, enable "Display smooth (curved) lines" and click the orange checkmark in the upper right corner of the window to apply changes.

1. As you can see on the widget, lines became smooth. Click the orange checkmark in the lower right corner of the screen to save changes.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/lines-smooth-ce.webp" alt="In the Advanced tab, enable &quot;Display smooth (curved) lines&quot; and click the orange checkmark in the upper right corner of the window to apply changes." loading="lazy"><figcaption>In the Advanced tab, enable "Display smooth (curved) lines" and click the orange checkmark in the upper right corner of the window to apply changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/lines-smooth-1-ce.webp" alt="As you can see on the widget, lines became smooth. Click the orange checkmark in the lower right corner of the screen to save changes." loading="lazy"><figcaption>As you can see on the widget, lines became smooth. Click the orange checkmark in the lower right corner of the screen to save changes.</figcaption></figure></div>


###### 2. Default line width for all thresholds


1. In the Data tab, click the pencil icon on the data key to enter Data key configuration.

1. In the Advanced tab of the opened dialog, enter preferred threshold value, pick the color of the threshold and click "Save".

1. To apply changes click the orange checkmark in the upper right corner of the window..

1. In the Advanced tab, enter line width for all thresholds and apply changes by clicking the orange checkmark in the upper right corner of the window.

1. Thresholds width has been changed. Save all applied changes by clicking the orange checkmark in the lower right corner of the screen.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/lines-thresholds-ce.webp" alt="In the Data tab, click the pencil icon on the data key to enter Data key configuration." loading="lazy"><figcaption>In the Data tab, click the pencil icon on the data key to enter Data key configuration.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/lines-thresholds-1-ce.webp" alt="In the Advanced tab of the opened dialog, enter preferred threshold value, pick the color of the threshold and click &quot;Save&quot;." loading="lazy"><figcaption>In the Advanced tab of the opened dialog, enter preferred threshold value, pick the color of the threshold and click "Save".</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/lines-thresholds-2-ce.webp" alt="To apply changes click the orange checkmark in the upper right corner of the window.." loading="lazy"><figcaption>To apply changes click the orange checkmark in the upper right corner of the window..</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/lines-thresholds-3-ce.webp" alt="In the Advanced tab, enter line width for all thresholds and apply changes by clicking the orange checkmark in the upper right corner of the window." loading="lazy"><figcaption>In the Advanced tab, enter line width for all thresholds and apply changes by clicking the orange checkmark in the upper right corner of the window.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/lines-thresholds-4-ce.webp" alt="Thresholds width has been changed. Save all applied changes by clicking the orange checkmark in the lower right corner of the screen." loading="lazy"><figcaption>Thresholds width has been changed. Save all applied changes by clicking the orange checkmark in the lower right corner of the screen.</figcaption></figure></div>


#### State Chart

##### 1. Common Settings

**1.1.** Stacking

Stacking mode works in widgets where you need to see entity values.

**1.2.** Display smooth (curved) lines works only in Line Charts.

**1.3.** Hover individual points

When the box **Hover individual points** is checked, you won't see value points on the lines. 

**1.4.** Cumulative values in stacking mode

While stacking mode is on, you can check the box "Cumulative values" to enable your chart to display sum of all entity values.

**1.5. Tooltip value format function, f(value)** is used when you want to manually customize the tooltip.
You can customize the values that will be displayed in the tooltip via [Settings](/docs/user-guide/dashboards/#5-other-settings) or
[Advanced Data key configuration](/docs/user-guide/ui/advanced-data-key-configuration/#2-charts).
Tooltip configuration via Settings is basic and applied to all entities at the same time. When configured in the Advanced Data key configuration,
it is applied only to the specific time series data, and the basic tooltip function will be overwritten by this configuration.

In State Chart, you can configure entity states to be shown on a tooltip depending on entity values.

<summary>
<b>Let's use function to set the needed configuration:</b>
</summary>

<figure class="highlight"><pre><code class="language-ruby" data-lang="ruby"><span class="n">let</span> <span class="n">celsiusValue</span> <span class="o">=</span> <span class="n">parseFloat</span><span class="p">(</span><span class="n">value</span><span class="p">).</span><span class="nf">toFixed</span><span class="p">(</span><span class="mi">2</span><span class="p">);</span>
<span class="n">let</span> <span class="n">farenheitValue</span> <span class="o">=</span> <span class="n">parseFloat</span><span class="p">(</span><span class="n">celsiusValue</span><span class="o">*</span><span class="mf">1.8</span> <span class="o">+</span> <span class="mi">32</span><span class="p">).</span><span class="nf">toFixed</span><span class="p">(</span><span class="mi">2</span><span class="p">);</span>
<span class="k">return</span> <span class="n">celsiusValue</span> <span class="o">+</span> <span class="s1">' °C ('</span> <span class="o">+</span> <span class="n">farenheitValue</span> <span class="o">+</span> <span class="s1">' °F)'</span><span class="p">;</span></code></pre></figure>


1. In the Tooltip value format function field, enter your function (our example you can find under screenshots section). Apply changes by clicking the orange checkmark in the upper right corner of the window.

1. You need to save changes to see tooltip. Do it by clicking the orange checkmark in the lower right corner of the screen.

1. Hover with your mouse over the widget to see tooltip with applied value format function.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/state-tooltipfunction-ce.webp" alt="In the Tooltip value format function field, enter your function (our example you can find under screenshots section). Apply changes by clicking the orange checkmark in the upper right corner of the window." loading="lazy"><figcaption>In the Tooltip value format function field, enter your function (our example you can find under screenshots section). Apply changes by clicking the orange checkmark in the upper right corner of the window.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/state-tooltipfunction-1-ce.webp" alt="You need to save changes to see tooltip. Do it by clicking the orange checkmark in the lower right corner of the screen." loading="lazy"><figcaption>You need to save changes to see tooltip. Do it by clicking the orange checkmark in the lower right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/state-tooltipfunction-2-ce.webp" alt="Hover with your mouse over the widget to see tooltip with applied value format function." loading="lazy"><figcaption>Hover with your mouse over the widget to see tooltip with applied value format function.</figcaption></figure></div>


**1.6. Grid settings**

Grid settings are the same as in [Time series Bar Chart](/docs/user-guide/ui/chart-widget/#1-common-settings). 

**1.7. Axis settings**

Axis settings are the same as in [Time series Bar Chart](/docs/user-guide/ui/chart-widget/#1-common-settings).

**1.8. Ticks formatter function**


1. In the Advanced tab, you can edit the default function according to your entity values.

1. After you edited values and text to be returned, apply changes by clicking the orange checkmark in the upper right corner of the window.

1. Ticks formatter function has been applied. To save it, click the orange checkmark in the lower right corner of the page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/state-ticksfun-ce.webp" alt="In the Advanced tab, you can edit the default function according to your entity values." loading="lazy"><figcaption>In the Advanced tab, you can edit the default function according to your entity values.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/state-ticksfun-1-ce.webp" alt="After you edited values and text to be returned, apply changes by clicking the orange checkmark in the upper right corner of the window." loading="lazy"><figcaption>After you edited values and text to be returned, apply changes by clicking the orange checkmark in the upper right corner of the window.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/state-ticksfun-2-ce.webp" alt="Ticks formatter function has been applied. To save it, click the orange checkmark in the lower right corner of the page." loading="lazy"><figcaption>Ticks formatter function has been applied. To save it, click the orange checkmark in the lower right corner of the page.</figcaption></figure></div>


##### 2. Comparison Settings


1. In Advanced tab, enable comparison and from the drop-down menu select time to show historical data with which to compare. In the "Second X axis" section, select axis position, where the compared axis will be located on the widget. If you would like title for the second axis, enable "Show labels" and enter the Axis title. When you are done with Comparison Settings configuration, click the orange checkmark in the upper right corner of the window to apply changes.

1. Since comparison settings work only in History time window mode, click on the clock icon in the upper right corner and select the History time window there. Click "Update" to apply.

1. As you can see on the widget, now you can compare value for last minute and the one from day ago. Click the big orange checkmark in the lower right corner to apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/state-comparison-ce.webp" alt="In Advanced tab, enable comparison and from the drop-down menu select time to show historical data with which to compare. In the &quot;Second X axis&quot; section, select axis position, where the compared axis will be located on the widget. If you would like title for the second axis, enable &quot;Show labels&quot; and enter the Axis title. When you are done with Comparison Settings configuration, click the orange checkmark in the upper right corner of the window to apply changes." loading="lazy"><figcaption>In Advanced tab, enable comparison and from the drop-down menu select time to show historical data with which to compare. In the "Second X axis" section, select axis position, where the compared axis will be located on the widget. If you would like title for the second axis, enable "Show labels" and enter the Axis title. When you are done with Comparison Settings configuration, click the orange checkmark in the upper right corner of the window to apply changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/state-comparison-1-ce.webp" alt="Since comparison settings work only in History time window mode, click on the clock icon in the upper right corner and select the History time window there. Click &quot;Update&quot; to apply." loading="lazy"><figcaption>Since comparison settings work only in History time window mode, click on the clock icon in the upper right corner and select the History time window there. Click "Update" to apply.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/state-comparison-2-ce.webp" alt="As you can see on the widget, now you can compare value for last minute and the one from day ago. Click the big orange checkmark in the lower right corner to apply changes." loading="lazy"><figcaption>As you can see on the widget, now you can compare value for last minute and the one from day ago. Click the big orange checkmark in the lower right corner to apply changes.</figcaption></figure></div>


##### 3. Custom Legend Settings

Custom Legend Settings are the same as in [Time series Bar Chart](/docs/user-guide/ui/chart-widget/#3-custom-legend-settings).

#### Latest values Pie - Flot

##### 1. Radius

Sets the radius of the pie. If the value is between 0 and 1 (inclusive) then it will use that as a percentage of the available space (size of the container). 
Otherwise, it will use the value as a direct pixel length.


1. In the Advanced tab, enter preferred radius (0 to 1) and click the orange checkmark in the upper right corner of the window to apply changes.

1. Radius became smaller. Click the big orange checkmark in the lower right corner to apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/pieflot-radius-ce.webp" alt="In the Advanced tab, enter preferred radius (0 to 1) and click the orange checkmark in the upper right corner of the window to apply changes." loading="lazy"><figcaption>In the Advanced tab, enter preferred radius (0 to 1) and click the orange checkmark in the upper right corner of the window to apply changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/pieflot-radius-1-ce.webp" alt="Radius became smaller. Click the big orange checkmark in the lower right corner to apply changes." loading="lazy"><figcaption>Radius became smaller. Click the big orange checkmark in the lower right corner to apply changes.</figcaption></figure></div>


##### 2. Inner radius

Sets the radius of the donut hole. If value is between 0 and 1 (inclusive) then it will use that as a percentage of the radius, otherwise it will use the value as a direct pixel length.


1. In the Advanced tab, enter preferred inner radius (0 to 1) and click the orange checkmark in the upper right corner of the window to apply changes.

1. Inner radius has been added. Click the big orange checkmark in the lower right corner to apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/pieflot-innerradius-ce.webp" alt="In the Advanced tab, enter preferred inner radius (0 to 1) and click the orange checkmark in the upper right corner of the window to apply changes." loading="lazy"><figcaption>In the Advanced tab, enter preferred inner radius (0 to 1) and click the orange checkmark in the upper right corner of the window to apply changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/pieflot-innerradius-1-ce.webp" alt="Inner radius has been added. Click the big orange checkmark in the lower right corner to apply changes." loading="lazy"><figcaption>Inner radius has been added. Click the big orange checkmark in the lower right corner to apply changes.</figcaption></figure></div>


##### 3. Enable pie animation

With the changing of entities values the Pie - Flot obviously moves, but these moves are rather sharp movements. Nevertheless, Pie animation makes these moves smoother and softer. 


1. In the Advanced tab, enable the experimental pie animation function and click the big orange checkmark in the upper right corner of the window to apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/pieflot-animation-ce.webp" alt="In the Advanced tab, enable the experimental pie animation function and click the big orange checkmark in the upper right corner of the window to apply changes." loading="lazy"><figcaption>In the Advanced tab, enable the experimental pie animation function and click the big orange checkmark in the upper right corner of the window to apply changes.</figcaption></figure></div>


##### 4. Tilt

Percentage of tilt ranging from 0 and 1, where 1 has no change (fully vertical) and 0 is completely flat (fully horizontal, in which case nothing actually gets drawn).
The tilt value is now used when calculating the maximum radius of the pie in relation to the height of the container. 
This should prevent the pie from being smaller than it needed to in some cases, as well as reducing the amount of extra white space generated above and below the pie.


1. In the Advanced tab, enter preferred tilt (0 to 1) and click the orange checkmark in the upper right corner of the window to apply changes.

1. As you can see, the Pie - Flot has been tilted. Save changes by clicking the big orange checkmark in the lower right of the page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/pieflot-tilt-ce.webp" alt="In the Advanced tab, enter preferred tilt (0 to 1) and click the orange checkmark in the upper right corner of the window to apply changes." loading="lazy"><figcaption>In the Advanced tab, enter preferred tilt (0 to 1) and click the orange checkmark in the upper right corner of the window to apply changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/pieflot-tilt-1-ce.webp" alt="As you can see, the Pie - Flot has been tilted. Save changes by clicking the big orange checkmark in the lower right of the page." loading="lazy"><figcaption>As you can see, the Pie - Flot has been tilted. Save changes by clicking the big orange checkmark in the lower right of the page.</figcaption></figure></div>


##### 5. Stroke


1. In the Advanced tab, click on the stroke color circle. In the opened dialog window, move sliders to adjust color and transparency of the stroke. Click "Select" when you are done.

1. Also, you can change stroke width and disable labels visibility. Apply changes by clicking the orange checkmark in the upper right corner of the page.

1. As you can see, stroke has been added to the Pie - Flot.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/pieflot-stroke-ce.webp" alt="In the Advanced tab, click on the stroke color circle. In the opened dialog window, move sliders to adjust color and transparency of the stroke. Click &quot;Select&quot; when you are done." loading="lazy"><figcaption>In the Advanced tab, click on the stroke color circle. In the opened dialog window, move sliders to adjust color and transparency of the stroke. Click "Select" when you are done.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/pieflot-stroke-1-ce.webp" alt="Also, you can change stroke width and disable labels visibility. Apply changes by clicking the orange checkmark in the upper right corner of the page." loading="lazy"><figcaption>Also, you can change stroke width and disable labels visibility. Apply changes by clicking the orange checkmark in the upper right corner of the page.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/pieflot-stroke-2-ce.webp" alt="As you can see, stroke has been added to the Pie - Flot." loading="lazy"><figcaption>As you can see, stroke has been added to the Pie - Flot.</figcaption></figure></div>


#### Latest values Doughnut

##### 1. Border


1. In the Advanced tab, click the border color circle. In the opened dialog, move sliders to adjust color and click "Select".

1. Also, you can change border width. After configuring all preferred border settings, click the orange checkmark in the upper right corner of the window.

1. As you can see on the widget, custom borders have been added to the Doughnut widget.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/donut-border-ce.webp" alt="In the Advanced tab, click the border color circle. In the opened dialog, move sliders to adjust color and click &quot;Select&quot;." loading="lazy"><figcaption>In the Advanced tab, click the border color circle. In the opened dialog, move sliders to adjust color and click "Select".</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/donut-border-1-ce.webp" alt="Also, you can change border width. After configuring all preferred border settings, click the orange checkmark in the upper right corner of the window." loading="lazy"><figcaption>Also, you can change border width. After configuring all preferred border settings, click the orange checkmark in the upper right corner of the window.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/donut-border-2-ce.webp" alt="As you can see on the widget, custom borders have been added to the Doughnut widget." loading="lazy"><figcaption>As you can see on the widget, custom borders have been added to the Doughnut widget.</figcaption></figure></div>


##### 2. Legend settings


1. In the Advanced tab, click the Labels font color circle. In the opened dialog, move sliders to adjust color and click "Select".

1. Also, you can disable legend visibility. After you are done configuring legend settings, click the orange checkmark in the upper right corner of the window to apply changes.

1. As you can see on the widget, color of the labels font has been changed. 


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/charts/donut-legend-ce.webp" alt="In the Advanced tab, click the Labels font color circle. In the opened dialog, move sliders to adjust color and click &quot;Select&quot;." loading="lazy"><figcaption>In the Advanced tab, click the Labels font color circle. In the opened dialog, move sliders to adjust color and click "Select".</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/donut-legend-1-ce.webp" alt="Also, you can disable legend visibility. After you are done configuring legend settings, click the orange checkmark in the upper right corner of the window to apply changes." loading="lazy"><figcaption>Also, you can disable legend visibility. After you are done configuring legend settings, click the orange checkmark in the upper right corner of the window to apply changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/charts/donut-legend-2-ce.webp" alt="As you can see on the widget, color of the labels font has been changed. " loading="lazy"><figcaption>As you can see on the widget, color of the labels font has been changed. </figcaption></figure></div>
