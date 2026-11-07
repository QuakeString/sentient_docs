+++
title = "Entities Table Widget"
description = "Advanced Settings of the Entities Table Widget"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/entity-table-widget.md"
+++
## Overview

Entity Table widget displays the latest values with list of entities that matches selected alias and filter with ability of additional full text search and pagination options.
Highly customizable using [widget styles](/docs/user-guide/ui/entity-table-widget/#settings), [data source keys](/docs/user-guide/ui/advanced-data-key-configuration/), and 
[widget actions](/docs/user-guide/ui/widget-actions/).

## Setting up Entities Table widget

To get started with the Entities table widget, you first need to create a dashboard and add a widget to it.

### Creating a dashboard

So let's [create a dashboard](/docs/user-guide/dashboards/#adding-a-dashboard) that will visualize our telemetry.  
You can use an existing one or create a new dashboard for a new use case.
In our example, we've created a new dashboard called “Entity Table” for the purposes of our tutorial.

### Adding a widget to the dashboard

The next step is to visualize telemetry. To add the Entity table widget to your dashboard, you should:


1. Enter dashboard edit mode by clicking the pencil icon in the lower right corner of the screen.

1. Click the big sign in the middle of the screen or the plus icon ("Add new widget") in the lower right corner of the screen. From the drop-up menu, select Create new widget.

1. In the widgets bundle selection dialog window, choose Cards.

1. From the Cards bundle, select the Entities table widget.

1. Click Add to attach a datasource to your widget to specify entity from which we will receive telemetry data.

1. If you have added an alias before, select it from the drop-down menu. If not, click "Create a new one!".

1. You can learn how to add an alias and aliases types  by following the link below the screenshots section. After configuring the alias settings, click Add.

1. Add telemetry from the drop-down menu to be displayed on the widget.

1. When you are done configuring datasource, click Add.

1. Drag the edges of the widget to adjust its size and save all applied changes by clicking the checkmark in the lower right corner of the screen.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/add-widget-ce.webp" alt="Enter dashboard edit mode by clicking the pencil icon in the lower right corner of the screen." loading="lazy"><figcaption>Enter dashboard edit mode by clicking the pencil icon in the lower right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/add-widget-1-ce.webp" alt="Click the big sign in the middle of the screen or the plus icon (&quot;Add new widget&quot;) in the lower right corner of the screen. From the drop-up menu, select Create new widget." loading="lazy"><figcaption>Click the big sign in the middle of the screen or the plus icon ("Add new widget") in the lower right corner of the screen. From the drop-up menu, select Create new widget.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/add-widget-2-ce.webp" alt="In the widgets bundle selection dialog window, choose Cards." loading="lazy"><figcaption>In the widgets bundle selection dialog window, choose Cards.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/add-widget-3-ce.webp" alt="From the Cards bundle, select the Entities table widget." loading="lazy"><figcaption>From the Cards bundle, select the Entities table widget.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/add-widget-4-ce.webp" alt="Click Add to attach a datasource to your widget to specify entity from which we will receive telemetry data." loading="lazy"><figcaption>Click Add to attach a datasource to your widget to specify entity from which we will receive telemetry data.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/add-widget-5-ce.webp" alt="If you have added an alias before, select it from the drop-down menu. If not, click &quot;Create a new one!&quot;." loading="lazy"><figcaption>If you have added an alias before, select it from the drop-down menu. If not, click "Create a new one!".</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/add-widget-6-ce.webp" alt="You can learn how to add an alias and aliases types  by following the link below the screenshots section. After configuring the alias settings, click Add." loading="lazy"><figcaption>You can learn how to add an alias and aliases types  by following the link below the screenshots section. After configuring the alias settings, click Add.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/add-widget-7-ce.webp" alt="Add telemetry from the drop-down menu to be displayed on the widget." loading="lazy"><figcaption>Add telemetry from the drop-down menu to be displayed on the widget.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/add-widget-8-ce.webp" alt="When you are done configuring datasource, click Add." loading="lazy"><figcaption>When you are done configuring datasource, click Add.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/add-widget-9-ce.webp" alt="Drag the edges of the widget to adjust its size and save all applied changes by clicking the checkmark in the lower right corner of the screen." loading="lazy"><figcaption>Drag the edges of the widget to adjust its size and save all applied changes by clicking the checkmark in the lower right corner of the screen.</figcaption></figure></div>


Learn how to [add alias](/docs/user-guide/ui/aliases/) to your widget.

## Settings

To start customizing your widget, you should go to widget edit mode by clicking the pencil icon in the upper right corner of the widget while in the dashboard edit mode.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/entity-edit-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### 1. Title style

You can change widget title tooltip, and title style. Title itself you should change via [Advanced title settings](/docs/user-guide/ui/entity-table-widget/#1-entities-table-title).
Also, you are able to add an icon to the title and adjust its color, opacity, and size. See configuration and the corresponding result below.


1. You are able to change Title setting, its tooltip and customize title style. In addition, you can add an icon and adjust its settings.

1. After setting up all preferred configurations, apply the changes by clicking the checkmark in the upper right corner of the screen.

1. As you can see, the title style has been changed, and the custom has been added icon next to it. To save all applied changes, click the checkmark in the lower right corner of the screen.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/entity-title-ce.webp" alt="You are able to change Title setting, its tooltip and customize title style. In addition, you can add an icon and adjust its settings." loading="lazy"><figcaption>You are able to change Title setting, its tooltip and customize title style. In addition, you can add an icon and adjust its settings.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/entity-title-1-ce.webp" alt="After setting up all preferred configurations, apply the changes by clicking the checkmark in the upper right corner of the screen." loading="lazy"><figcaption>After setting up all preferred configurations, apply the changes by clicking the checkmark in the upper right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/entity-title-2-ce.webp" alt="As you can see, the title style has been changed, and the custom has been added icon next to it. To save all applied changes, click the checkmark in the lower right corner of the screen." loading="lazy"><figcaption>As you can see, the title style has been changed, and the custom has been added icon next to it. To save all applied changes, click the checkmark in the lower right corner of the screen.</figcaption></figure></div>


The checkboxes are responsible for displaying/hiding the widget title, widget shadow, and enabling/disabling fullscreen mode.

### 2. Widget style

You can customize personal style for the widget using CSS properties. 
This style will be applied to the main div element of the widget. 
You can also change the background color, text color, padding, and margin. See the configuration and the corresponding result below.

Please note that the style and background color are just an example and are definitely not part of our guidelines.

```json
{
  "border": "3px solid #2E86C1",
  "cursor": "pointer"
}
```


1. In the widget style field, enter the function to customize the appearance of the widget.

1. You can manually adjust the background and text colors by clicking the corresponding circles and moving sliders to select the color you want. Enter the preferred value in the padding and margin lines. After configuring the desired options, click the checkmark in the upper right corner of the screen.

1. As you can see, the appearance of the widget has changed. To save all applied changes, click the checkmark in the lower right corner of the screen.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/entity-style-ce.webp" alt="In the widget style field, enter the function to customize the appearance of the widget." loading="lazy"><figcaption>In the widget style field, enter the function to customize the appearance of the widget.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/entity-style-1-ce.webp" alt="You can manually adjust the background and text colors by clicking the corresponding circles and moving sliders to select the color you want. Enter the preferred value in the padding and margin lines. After configuring the desired options, click the checkmark in the upper right corner of the screen." loading="lazy"><figcaption>You can manually adjust the background and text colors by clicking the corresponding circles and moving sliders to select the color you want. Enter the preferred value in the padding and margin lines. After configuring the desired options, click the checkmark in the upper right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/entity-style-2-ce.webp" alt="As you can see, the appearance of the widget has changed. To save all applied changes, click the checkmark in the lower right corner of the screen." loading="lazy"><figcaption>As you can see, the appearance of the widget has changed. To save all applied changes, click the checkmark in the lower right corner of the screen.</figcaption></figure></div>


### 3. Special symbol and number of digits after floating point

You can add a special symbol that will be displayed next to the entity values of your widget. Also, you can customize the number of digits to be displayed after the floating point number of your value.
See the configuration and the corresponding result below.


1. Enter the desired symbol to be shown next to the value. Enter the number of the digits to be displayed after the floating point number. Apply the changes by clicking the checkmark in the upper right corner of the screen.

1. As you can see, the special symbol has been added, and the number of digits has been changed.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/entity-digits-ce.webp" alt="Enter the desired symbol to be shown next to the value. Enter the number of the digits to be displayed after the floating point number. Apply the changes by clicking the checkmark in the upper right corner of the screen." loading="lazy"><figcaption>Enter the desired symbol to be shown next to the value. Enter the number of the digits to be displayed after the floating point number. Apply the changes by clicking the checkmark in the upper right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/entity-digits-1-ce.webp" alt="As you can see, the special symbol has been added, and the number of digits has been changed." loading="lazy"><figcaption>As you can see, the special symbol has been added, and the number of digits has been changed.</figcaption></figure></div>


### 4. Legend settings

Legend settings make sense configure only in time series widgets where this option is enabled by default. You can read more about Legend settings [here](/docs/user-guide/dashboards/#3-legend-settings).

## Advanced settings

Advanced settings of the Entities Table widget allows [adjusting the title of the widget](#1-entities-table-title), [changing visibility of objects on widget](#2-checkbox-settings), 
[customizing the columns](#3-the-columns-settings), [setting up the pagination](#4-the-pagination),
[sorting the data](#5-sorting-data-in-the-table-widget) and [changing style of widget rows](#6-row-style-function).

To enter the advanced mode and start adjusting the settings above, you should:


1. Click the pencil icon ("Enter edit mode") in the lower right corner of the screen.

1. Click the pencil icon (“Edit widget”) in the upper right corner of the Entity Table widget itself.

1. Move to the Advanced cell.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/enter-edit-ce.webp" alt="Click the pencil icon (&quot;Enter edit mode&quot;) in the lower right corner of the screen." loading="lazy"><figcaption>Click the pencil icon ("Enter edit mode") in the lower right corner of the screen.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/pencil-edit-enter.webp" alt="Click the pencil icon (“Edit widget”) in the upper right corner of the Entity Table widget itself." loading="lazy"><figcaption>Click the pencil icon (“Edit widget”) in the upper right corner of the Entity Table widget itself.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/entitytable-advncd.webp" alt="Move to the Advanced cell." loading="lazy"><figcaption>Move to the Advanced cell.</figcaption></figure></div>


### 1. Entities table title

SENTIENT has no name restrictions, either in symbols or in a number of characters.
Nevertheless, in case the title is too long, it will not display completely in the Entity Table widget, but will be terminated with three dots.
However, after applying the changes and opening the widget in full-screen mode, you will be able to see the full name of the widget.
For example, let’s use something simple for the title like “The New Widget Title”:


1. Enter the desired title in the title bar. Click the orange checkmark in the upper right corner.

1. The title of the widget has been changed.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/table-widgetname-advncd.webp" alt="Enter the desired title in the title bar. Click the orange checkmark in the upper right corner." loading="lazy"><figcaption>Enter the desired title in the title bar. Click the orange checkmark in the upper right corner.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/namechanged-table-advncd.webp" alt="The title of the widget has been changed." loading="lazy"><figcaption>The title of the widget has been changed.</figcaption></figure></div>


### 2. Checkbox settings


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/checkoboxes.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- Enable entities search

If the checkbox is checked, the magnifying glass in the upper right corner of the widget allows you to search for widget entities.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/entities-search-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- Enable select columns to display

If the checkbox is checked, the black bars in the upper right corner of the widget allow you to choose which columns you prefer to hide and which to display.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/columns-to-display-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- Always display header

If the checkbox is checked, the widget header is always visible when we scroll through the list of entities. If the box is not checked, the widget header remains at the top.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/display-header-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- Always display actions column

If the checkbox is checked, the row action cell is always visible when we scroll through the widget's telemetry. When unchecked, the row action cell remains at the end of the row.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/actions-column-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- Display entity name column

If the checkbox is checked, the entity name column is visible. If it's unchecked, it will be hidden.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/entity-name-column-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### 3. The columns settings

#### 3.1. Entity column title

To change the title of the column, you should:


1. Enter the new title in the corresponding line.

1. Click the orange checkmark in the upper right corner to apply changes. An entity column title has been changed.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/appropriate-line-clumn-title.webp" alt="Enter the new title in the corresponding line." loading="lazy"><figcaption>Enter the new title in the corresponding line.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/column-name-changed.webp" alt="Click the orange checkmark in the upper right corner to apply changes. An entity column title has been changed." loading="lazy"><figcaption>Click the orange checkmark in the upper right corner to apply changes. An entity column title has been changed.</figcaption></figure></div>


#### 3.2. Displaying an entity label column

If the checkbox “Display entity label column” is checked, you can add the label column and name it.
After clicking on the orange checkmark in the upper right corner, the label column with the custom name will appear in the widget.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/lanelcolumn-name-input.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/labelcolumn-added.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### 3.3. Displaying an entity type column

The checkbox "Displaying entity type column" is responsible for showing the type of the entity on the widget (e.g. "device").
By default, an entity type column is shown, but you can hide it by unchecking the box.

### 4. The Pagination

By default, the widget shows how many items per page can be visible and how many pages there are in general. Displaying this information is optional.
It changes by checking/unchecking the checkbox called “Display pagination”.
If the checkbox is disabled, the information about items per page and number of pages won’t be displayed.
To apply the changes, click the orange checkmark in the upper right corner.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/paggination-off.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


**Please, note:** to understand the next settings, we need to enable the “Display pagination” checkbox to see the number of items per a page.

By default, **the page size** is set to 10 items per page.
If you need to change this number, you should:


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/paggination15.webp" alt="Enter the numbers manually or use the arrows at the end of the line." loading="lazy"><figcaption>Enter the numbers manually or use the arrows at the end of the line.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/15done.webp" alt="Click the orange checkmark in the upper right corner to apply the changes. The page will now have the desired number of items as shown in our table widget." loading="lazy"><figcaption>Click the orange checkmark in the upper right corner to apply the changes. The page will now have the desired number of items as shown in our table widget.</figcaption></figure></div>


### 5. Sorting data in the table widget

By default, the data in the Table widget is sorted in ascending order.
If the values in the column are not numeric (for example name and type), then the sorting will be done according to the alphabetical ordering rules.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/sortingorder-name.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


If you’d like to sort the data, for instance, by the telemetry data key type (temperature, humidity, etc.),
you can do this by inputting the name of your value in the default sort order row.
In the example, the temperature is used.
If you need to make the sort order descending, you should:


1. As was mentioned, the default sort order is ascending.

1. Type the “-” (minus) symbol in front of the data key name in the Default sort order line. Click the orange checkmark in the upper right corner to apply the changes

1. Now, the telemetry data is sorted in the descending order we needed.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/ascendingorder.webp" alt="As was mentioned, the default sort order is ascending." loading="lazy"><figcaption>As was mentioned, the default sort order is ascending.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/descending-minus.webp" alt="Type the “-” (minus) symbol in front of the data key name in the Default sort order line. Click the orange checkmark in the upper right corner to apply the changes" loading="lazy"><figcaption>Type the “-” (minus) symbol in front of the data key name in the Default sort order line. Click the orange checkmark in the upper right corner to apply the changes</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/descending-done.webp" alt="Now, the telemetry data is sorted in the descending order we needed." loading="lazy"><figcaption>Now, the telemetry data is sorted in the descending order we needed.</figcaption></figure></div>


### 6. Row style function

Since version 3.2.2, the opportunity to change style of widget rows depending on their conditions appeared. Let's see how it works on the simple example:  
assume, we need to observe which device is active and which is not. To make our mission easier, we should use the Row style function.

An example of it and the corresponding results:

```ruby
result = {background:"white"};
if (entity.active == "false") {
   result.background = '#FF0000';
} else {
   result.background = '#00FF00';
}
return result;
```


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/style-function-сe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/ui/widgets/entitywidget/style-function-1-сe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Saving changes

For the changes to be applied and saved, you have to click the orange checkmark in the lower right corner of the dashboard.

Then you can be sure that the changes to the table widget are applied and saved correctly.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/entitywidget/saving-changes.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>
