+++
title = "Advanced data key configuration"
description = "SENTIENT advanced configuration of data keys"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/advanced-data-key-configuration.md"
+++
## Introduction

Advanced data key configuration is responsible for the visibility, style, and appearance of a specific data key column or line on a chart on the widget.

The "**Alarms table**" widget and "**Tables**", "**Entity widgets**", and "**Entity admin widgets**" bundles have the [same advanced data key configuration](#advanced-data-key-configuration).

The "**Charts**" widget bundle has its [unique advanced data key configuration](#advanced-data-key-configuration-for-charts-widget-bundle).

All other widget bundles have only [basic data key configuration](/docs/user-guide/widgets/#data-keys).

<br>
To enter a data key configuration, click the pencil icon on the specific data key you want to adjust.


![image](/images/user-guide/widgets/advanced-data-key/enter-data-key-configuration-ce.webp)


## Advanced data key configuration

As we know, the "Alarms table" widget, "Tables", "Entity widgets", and "Entity admin widgets" bundles have the same advanced data key configuration.
Let's go through the advanced data key configuration for these widgets using the "Entities table" widget from the "Tables" bundle as an example.

Please follow these steps to start the advanced configuration of the key data.


1. Open the dashboard and enter edit mode by clicking the button in the top right corner of the screen;

1. In the top right corner of the widget, click the "pencil" icon to open the widget editing window;

1. Now, click "pencil" icon next to the key that you want to edit;

1. The data key configuration window has been opened. Navigate to the "Advanced" tab to open advanced data key configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/entity-table-example-1-ce.webp" alt="Open the dashboard and enter edit mode by clicking the button in the top right corner of the screen;" loading="lazy"><figcaption>Open the dashboard and enter edit mode by clicking the button in the top right corner of the screen;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/entity-table-example-2-ce.webp" alt="In the top right corner of the widget, click the &quot;pencil&quot; icon to open the widget editing window;" loading="lazy"><figcaption>In the top right corner of the widget, click the "pencil" icon to open the widget editing window;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/entity-table-example-3-ce.webp" alt="Now, click &quot;pencil&quot; icon next to the key that you want to edit;" loading="lazy"><figcaption>Now, click "pencil" icon next to the key that you want to edit;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/entity-table-example-4-ce.webp" alt="The data key configuration window has been opened. Navigate to the &quot;Advanced&quot; tab to open advanced data key configuration." loading="lazy"><figcaption>The data key configuration window has been opened. Navigate to the "Advanced" tab to open advanced data key configuration.</figcaption></figure></div>


### Custom header title

By default, the column name is the same as the key name. The _"Custom header title"_ option allows you to change the column caption to whatever you prefer.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/custom-header-title-1-ce.webp" alt="By default, the column name is the same as the key name;" loading="lazy"><figcaption>By default, the column name is the same as the key name;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/custom-header-title-3-ce.webp" alt="Manually enter the desired custom header title and save all changes;" loading="lazy"><figcaption>Manually enter the desired custom header title and save all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/custom-header-title-4-ce.webp" alt="Example of the custom header title." loading="lazy"><figcaption>Example of the custom header title.</figcaption></figure></div>


### Column width (px or %)

The _"Column width"_ function allows you to adjust the width of the column in pixels or percentages. Manually enter the desired width (for example, 200px).
In the same way, you can change the width as a percentage.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/column-width-3-ce.webp" alt="Default column width;" loading="lazy"><figcaption>Default column width;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/column-width-1-ce.webp" alt="Manually enter a desired width and save all changes;" loading="lazy"><figcaption>Manually enter a desired width and save all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/column-width-2-ce.webp" alt="Custom column width." loading="lazy"><figcaption>Custom column width.</figcaption></figure></div>


### Cell style function

The _"Cell style function"_ allows adjusting the color of rows based on values, entity, or [ctx](/docs/user-guide/contribution/widgets-development/#basic-widget-api).
To configure the cell style function, you should check the _Use cell style function_ box and input the function in the _Cell style function_ field below. 


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/style-function-3-ce.webp" alt="Default cell style;" loading="lazy"><figcaption>Default cell style;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/style-function-1-ce.webp" alt="Check the box &quot;Use cell style function&quot;, input the function in the &quot;Cell style function&quot; field, and save all changes;" loading="lazy"><figcaption>Check the box "Use cell style function", input the function in the "Cell style function" field, and save all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/style-function-2-ce.webp" alt="The cell color changes depending on its values." loading="lazy"><figcaption>The cell color changes depending on its values.</figcaption></figure></div>


An example of a cell style function where the cell color changes depending on its values:

```ruby
if(value < 0) {
   return {"background-color" : "#5F4DEB"};
} else if (value < 35) {
    return {"background-color" : "#62c5e3", "color" : "#19154a"};
} else if (value < 45) {
    return {"background-color" : "#b50232", "color" : "#f7e18f"};
} else if (value < 55) {
    return {"background-color" : "#e6b500", "color" : "#ff2200"};
} else if (value < 65) {
    return {"background-color" : "#ff9419"};
} else if (value < 75) {
    return {"background-color" : "#d0ff00"};
} else if (value < 85) {
    return {"background-color" : "#35c433"};
} else { 
    return { "background-color" : "red" };
}
```


### Cell content function

The _"Cell content function"_ allows changing the text of the data key column based on the value, entity, or [ctx](/docs/user-guide/contribution/widgets-development/#basic-widget-api).
To configure the cell style function, you should check the _Use cell content function_ box and input the function in the _Cell content function_ field below.

In the example, we have two possible device answers: true or false. Cell content function can change the answers text. It is acceptable when devices are not so many.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/content-function-1-ce.webp" alt="Default display of device status;" loading="lazy"><figcaption>Default display of device status;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/content-function-2-ce.webp" alt="Click &quot;pencil&quot; icon to next to the &quot;active&quot; key;" loading="lazy"><figcaption>Click "pencil" icon to next to the "active" key;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/content-function-3-ce.webp" alt="Check the &quot;Use cell content function&quot; box and input the function in the &quot;Cell content function&quot; field and save all changes;" loading="lazy"><figcaption>Check the "Use cell content function" box and input the function in the "Cell content function" field and save all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/content-function-4-ce.webp" alt="The cell content function will change the text in the device name row based on the device&#39;s status." loading="lazy"><figcaption>The cell content function will change the text in the device name row based on the device&#39;s status.</figcaption></figure></div>


```ruby
if (value == "true") {
    return "Active";
} else {
    return "Inactive";
}
```


However, sometimes reading return text to determine if a device is active or inactive isn't convenient. 
The cell content function offers a more user-friendly approach, allowing the configuration of a custom function to visually represent the device's status as active or inactive (refer to the example function below).


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/content-function-1-ce.webp" alt="Default display of device status;" loading="lazy"><figcaption>Default display of device status;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/content-function-2-ce.webp" alt="Click &quot;pencil&quot; icon to next to the &quot;active&quot; key;" loading="lazy"><figcaption>Click "pencil" icon to next to the "active" key;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/content-function-5-ce.webp" alt="Check the &quot;Use cell content function&quot; box and input the function in the &quot;Cell content function&quot; field and save all changes;" loading="lazy"><figcaption>Check the "Use cell content function" box and input the function in the "Cell content function" field and save all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/content-function-6-ce.webp" alt="The cell content function will change the color of the icon in the device name row based on the device&#39;s status." loading="lazy"><figcaption>The cell content function will change the color of the icon in the device name row based on the device&#39;s status.</figcaption></figure></div>


Configurable function to display an active/inactive status:

```ruby
if (value == "true") {
    return '<div style="border-radius:50%;background-color:green;width:18px;height:18px"></div>';
} else {
    return '<div style="border-radius:50%;background-color:red;width:18px;height:18px"></div>';
}
```


### Default column visibility 

The _"Default column visibility"_ function for the column allows you to choose whether the data key column will be visible on the widget or hidden.
This is especially helpful when exporting a widget when you need to exclude a specific data key.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/column-width-3-ce.webp" alt="The &quot;temperature&quot; data key column is visible on the widget;" loading="lazy"><figcaption>The "temperature" data key column is visible on the widget;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/column-visibility-1-ce.webp" alt="Choose whether the column will be shown in the visibility selection menu so that clients without permissions cannot hide it;" loading="lazy"><figcaption>Choose whether the column will be shown in the visibility selection menu so that clients without permissions cannot hide it;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/column-visibility-2-ce.webp" alt="The &quot;temperature&quot; data key column has been hidden." loading="lazy"><figcaption>The "temperature" data key column has been hidden.</figcaption></figure></div>


### Column selection in 'Column to display'

The _"Column selection in ‘Column to display’"_ function allows you to select whether the column will be shown in the visibility selection menu. Therefore, clients without permission cannot hide it.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/column-to-display-1-ce.webp" alt="The &quot;temperature&quot; column is displayed in the column visibility menu;" loading="lazy"><figcaption>The "temperature" column is displayed in the column visibility menu;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/column-to-display-2-ce.webp" alt="To hide the &quot;temperature&quot; column in the column visibility menu, select &quot;Disabled&quot; in the &quot;Column selection in &#39;Column to Display&#39;&quot; field;" loading="lazy"><figcaption>To hide the "temperature" column in the column visibility menu, select "Disabled" in the "Column selection in &#39;Column to Display&#39;" field;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/column-to-display-3-ce.webp" alt="The &quot;temperature&quot; column has been excluded from the visibility selection." loading="lazy"><figcaption>The "temperature" column has been excluded from the visibility selection.</figcaption></figure></div>


### Include column in export


<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Include in column in export** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>


The _"Include column in export"_ function allows you to choose under what conditions a widget can be exported with a specific data key column.
There are three options: always, only if column is visible (you can change the visibility in [default column visibility](#default-column-visibility)), and never.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/column-export-1-pe.webp" alt="The &quot;Include column in export&quot; function allows you to choose under what conditions a widget can be exported with a specific data key column. There are three options: always, only if column visible (you can change the visibility in default column visibility), and never." loading="lazy"><figcaption>The "Include column in export" function allows you to choose under what conditions a widget can be exported with a specific data key column. There are three options: always, only if column visible (you can change the visibility in default column visibility), and never.</figcaption></figure></div>


## Advanced data key configuration for "Charts" widget bundle

The advanced data key configuration for the "Charts" widget bundle is different from the advanced data key configuration for other widget bundles.

Let’s break down the data key configuration using the "Timeseries Line Chart" widget from the "Charts" bundle as an example.

Please follow these steps to start the advanced configuration of the data key.


1. Open the dashboard and enter edit mode by clicking the button in the top right corner of the screen;

1. In the top right corner of the widget, click the "pencil" icon to open the widget editing window;

1. Now, click "pencil" icon next to the key that you want to edit;

1. The data key configuration window has been opened. Navigate to the "Advanced" tab to open advanced data key configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/timeseries-line-chart-example-1-ce.webp" alt="Open the dashboard and enter edit mode by clicking the button in the top right corner of the screen;" loading="lazy"><figcaption>Open the dashboard and enter edit mode by clicking the button in the top right corner of the screen;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/timeseries-line-chart-example-2-ce.webp" alt="In the top right corner of the widget, click the &quot;pencil&quot; icon to open the widget editing window;" loading="lazy"><figcaption>In the top right corner of the widget, click the "pencil" icon to open the widget editing window;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/timeseries-line-chart-example-3-ce.webp" alt="Now, click &quot;pencil&quot; icon next to the key that you want to edit;" loading="lazy"><figcaption>Now, click "pencil" icon next to the key that you want to edit;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/timeseries-line-chart-example-4-ce.webp" alt="The data key configuration window has been opened. Navigate to the &quot;Advanced&quot; tab to open advanced data key configuration." loading="lazy"><figcaption>The data key configuration window has been opened. Navigate to the "Advanced" tab to open advanced data key configuration.</figcaption></figure></div>


### Data is hidden by default

By default, all data from the keys specified in the data source is displayed on the chart.

Enable the _"Data hidden by default"_ function for the selected key so that the data for this key is hidden by default on the chart.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/data-is-hidden-by-default-1-сe.webp" alt="By default, all data from the keys specified in the data source is displayed on the chart;" loading="lazy"><figcaption>By default, all data from the keys specified in the data source is displayed on the chart;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/data-is-hidden-by-default-2-сe.webp" alt="Enable the “Data hidden by default” option for the selected key so that the data for this key is hidden by default on the chart;" loading="lazy"><figcaption>Enable the “Data hidden by default” option for the selected key so that the data for this key is hidden by default on the chart;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/data-is-hidden-by-default-3-сe.webp" alt="The data for the selected key is hidden. However, you can display it again by clicking on the key&#39;s name in the legend;" loading="lazy"><figcaption>The data for the selected key is hidden. However, you can display it again by clicking on the key&#39;s name in the legend;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/data-is-hidden-by-default-4-сe.webp" alt="The data for the selected key is displayed on the chart again." loading="lazy"><figcaption>The data for the selected key is displayed on the chart again.</figcaption></figure></div>


### Disable data hiding

Enable the _"Disable data hide"_ function for the selected key so that you and your users cannot hide the data on the chart by clicking on the key name.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/disable-data-hiding-1-ce.webp" alt="Enable the &quot;Disable data hide&quot; option in the selected key so that you and your users cannot hide the data on the chart by clicking on the key name;" loading="lazy"><figcaption>Enable the "Disable data hide" option in the selected key so that you and your users cannot hide the data on the chart by clicking on the key name;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/disable-data-hiding-2-ce.webp" alt="Hiding data by clicking on the key name is not possible." loading="lazy"><figcaption>Hiding data by clicking on the key name is not possible.</figcaption></figure></div>


### Remove datakey from legend

Enable the _"Remove datakey from legend"_ function to prevent the selected key from being displayed in the legend.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/remove-datakey-from-legend-1-ce.webp" alt="Enable the &quot;Remove datakey from legend&quot; option to prevent the selected key from being displayed in the legend;" loading="lazy"><figcaption>Enable the "Remove datakey from legend" option to prevent the selected key from being displayed in the legend;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/remove-datakey-from-legend-2-ce.webp" alt="The data key from the legend has been removed." loading="lazy"><figcaption>The data key from the legend has been removed.</figcaption></figure></div>


### Exclude from stacking

You can exclude a specific key from the stacking. This function is only available in "Stacking" mode.
Read more about stacking mode and how to use it [here](/docs/user-guide/widgets/#common-settings).

### Show line

You can show/hide the line on the chart using the _"Show line"_ function and set the line width in pixels.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/show-line-1-ce.webp" alt="Default line width;" loading="lazy"><figcaption>Default line width;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/show-line-2-ce.webp" alt="Set the line width in pixels;" loading="lazy"><figcaption>Set the line width in pixels;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/show-line-3-ce.webp" alt="Now the line width is 6 pixels." loading="lazy"><figcaption>Now the line width is 6 pixels.</figcaption></figure></div>


#### Fill line

Enable the _"Fill line"_ function to fill the space between the line and the bottom border of the chart. You can also specify the fill's opacity within the range of 0 to 1.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/fill-line-1-ce.webp" alt="Enable the &quot;Fill line&quot; option to fill the space between the line and the bottom border of the chart. You can also specify the opacity of the fill in the range of 0 to 1." loading="lazy"><figcaption>Enable the "Fill line" option to fill the space between the line and the bottom border of the chart. You can also specify the opacity of the fill in the range of 0 to 1.</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/fill-line-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Show points

Enable the _"Show points"_ function to display data points on the chart. 
You can also specify the line width of points (in pixels), their radius (in pixels), and their shapes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/show-points-1-ce.webp" alt="Enable the &quot;Show Points&quot; option to display data points on the chart. Specify the line width of points (px), radius of points (px), and point shape of the points." loading="lazy"><figcaption>Enable the "Show Points" option to display data points on the chart. Specify the line width of points (px), radius of points (px), and point shape of the points.</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/show-points-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Tooltip settings

Customizing the _tooltip_ through the advanced widget settings is a basic setting that applies to all data keys simultaneously.
Read more about Tooltip settings for widget [here](/docs/user-guide/widgets/#tooltip-settings).

By using the _"Tooltip value format function"_ for the selected data key, you can configure the values that will be displayed in the tooltip only for that data key, and the basic tooltip function will be overwritten by this configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/tooltip-settings-1-ce.webp" alt="In the &quot;Tooltip value format function&quot; field, enter your tooltip function;" loading="lazy"><figcaption>In the "Tooltip value format function" field, enter your tooltip function;</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/tooltip-settings-2-ce.webp" alt="Hover the mouse pointer over a data point on the chart to see the customized tooltip content." loading="lazy"><figcaption>Hover the mouse pointer over a data point on the chart to see the customized tooltip content.</figcaption></figure></div>


### Vertical axis

Enable _"Show separate axes"_ to display a separate axis for this data key. For this axis, you can set your own title, minimum and maximum values of the scale, specify the number of decimal places, and the step size between ticks on the vertical axis.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/vertical-axis-1-ce.webp" alt="Enable the &quot;Show separate axis&quot; option to display a separate axis for this data key. For this axis, you can set your own title, minimum and maximum values of the scale, specify the number of decimal places, and the step size between ticks on the vertical axis." loading="lazy"><figcaption>Enable the "Show separate axis" option to display a separate axis for this data key. For this axis, you can set your own title, minimum and maximum values of the scale, specify the number of decimal places, and the step size between ticks on the vertical axis.</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/vertical-axis-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


In the _"Ticks formatter function"_ window, specify the function that will format the value to be displayed as Y axis tick.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/vertical-axis-3-ce.webp" alt="In the &quot;Tick Format Function&quot; window, specify the function that will format the value to be displayed as Y axis tick." loading="lazy"><figcaption>In the "Tick Format Function" window, specify the function that will format the value to be displayed as Y axis tick.</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/vertical-axis-4-ce.webp" alt="." loading="lazy"><figcaption>.</figcaption></figure></div>


### Thresholds

Use this function to set a _threshold_ value for the selected key. The threshold value will be displayed on the chart as a horizontal line.
You can specify the color and width of this line.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/advanced-data-key/thresholds-1-ce.webp" alt="Click the &quot;Add Threshold&quot; button, then enter your preferred threshold value and set the color and line width." loading="lazy"><figcaption>Click the "Add Threshold" button, then enter your preferred threshold value and set the color and line width.</figcaption></figure><figure><img src="/images/user-guide/widgets/advanced-data-key/thresholds-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Comparison settings

Display historical data on the graph to easily compare data for different time periods. 
This function works when the _comparison mode_ is activated in the widget settings.
For more details on comparison settings and how to use it, please read [here](/docs/user-guide/widgets/#comparison-settings).
