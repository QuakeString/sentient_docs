+++
title = "Map widgets"
description = "Map widgets"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/widgets/map-widgets.md"
+++
Map widgets in SENTIENT enable you to visualize entities and data on a map. They allow placing markers, zones, routes, and other geo-objects in space, which is especially useful for IoT solutions involving physical locations.

In SENTIENT version 4.0, we&#39;ve completely reworked our Map widgets to make them more flexible, easier to configure, and more powerful for working with geospatial data.

<b><font size="4">Use cases</font></b>

- Real-time entity location tracking (vehicles, drones, people)
- Route visualization and movement analysis (logistics, public transport, historical paths)
- Visualization of object layouts (factory layouts, parking, floor plans)
- Interactive mapping (user-placed markers, geofence creation)

<b><font size="4">Types of map widgets</font></b>

- **Map** widget: Displays real-world locations using base maps like OpenStreetMap, Google Maps, HERE or Tencent.
- **Image Map** widget: Ideal for indoor layouts or relative positioning — perfect for floor plans, smart parking, factory zones, and more. Works with custom image backgrounds.
- **Trip Map** and **Route Map** widgets: Visualize movement on the map. The Trip Map includes animated playback and timeline control for enhanced tracking visualization.

<b><font size="4">Key improvements:</font></b>

- **Easily place elements on the map**. Add items like markers, polygons, or circles to the map with just a few clicks. Under the hood, this triggers a custom function that captures the clicked location’s coordinates and stores them as attributes on the target entity.
- **New unified Trip Map widget**. Combines the features of the older Trip Animation and Router Map widgets into one powerful tool:
  - Supports animated routes, moving markers, and stop points.
  - Includes a set of dedicated marker icons.
  - Offers multiple route styling options, including path decorators and visible points.
  - Comes with customizable timeline controls — change date formats, playback speed, and more.
- **Dynamic map layer switching**. Switch between map types — standard, satellite, hybrid, or even your own custom layers — directly inside the widget.
- **Reference layer support**. Add an transparent overlay layer to provide extra map context or background visuals.
- **Improved configuration for map items (Marker / Polygon / Circle)**
  - Each overlay type now has separate settings, so they don’t conflict with one another. 
  - Better coordinate validation reduces the chance of mistakes — fewer missing keys or misconfigured sources. 
  - Built-in marker shapes available out of the box, with full support for custom icons too. 
  - New "Range" color mode added — dynamically change marker color based on key values (e.g., temperature or status). 
  - Set separate "Action on click" and "Tag action" for each overlay for more precise interactivity. 
  - Easily group overlays — toggle visibility for multiple map items in one click.
  - Improved editing experience — click on any map item to see contextual edit options right away. 
  - You can now choose the attribute scope (e.g., shared, server-side, telemetry) when setting coordinate values.
- **Use extra data sources**. Pull in additional values for labels, tooltips, or any extra info you want to show on the map.
- **Flexible control panel placement**. Move map controls (zoom, layer switchers, custom buttons) to any corner of the widget — perfect for adapting to different UI layouts. 
- **Map scale display**. Add an optional scale bar to help users visually estimate distances on the map.
- **Custom action buttons**. Add your own buttons right on the map — each can trigger a specific custom action (like creating an entity, switching views, or opening URLs).

All of this — and more — is now available in the new Map widgets in SENTIENT 4.0.

## Adding a Map widget to the dashboard

To add a Map widget to the dashboard, follow these steps:

- In dashboard edit mode, click the "Add widget" button at the top of the screen, or click the large "Add new widget" icon in the center of the screen (if this is your first widget on the dashboard).
- Find the "Maps" widget bundle and click on it. This category includes all available map widget types.
- Select the map widget that best fits your use case.
- Configure the widget to match your data and visualization requirements. You can adjust data sources, appearance, map provider settings, and more.
- Click the "Add" in the bottom-right corner of the widget configuration window to place it on your dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/adding-map-widget-1-ce.webp" alt="In dashboard edit mode, click the &quot;Add widget&quot; button at the top of the screen, or click the large &quot;Add new widget&quot; icon in the center of the screen (if this is your first widget on the dashboard)." loading="lazy"><figcaption>In dashboard edit mode, click the "Add widget" button at the top of the screen, or click the large "Add new widget" icon in the center of the screen (if this is your first widget on the dashboard).</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/adding-map-widget-2-ce.webp" alt="Find the &quot;Maps&quot; widget bundle and click on it. This category includes all available map widget types." loading="lazy"><figcaption>Find the "Maps" widget bundle and click on it. This category includes all available map widget types.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/adding-map-widget-3-ce.webp" alt="Select the map widget that best fits your use case." loading="lazy"><figcaption>Select the map widget that best fits your use case.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/adding-map-widget-4-ce.webp" alt="Configure the widget to match your data and visualization requirements. You can adjust data sources, appearance, map provider settings, and more. Click the &quot;Add&quot; in the bottom-right corner of the widget configuration window to place it on your dashboard." loading="lazy"><figcaption>Configure the widget to match your data and visualization requirements. You can adjust data sources, appearance, map provider settings, and more. Click the "Add" in the bottom-right corner of the widget configuration window to place it on your dashboard.</figcaption></figure></div>


## Map type

The first step in configuring the map widget is selecting the map type.
SENTIENT offers several map widgets, including Image Map, which allows you to use a custom background image as the map.

You can also configure map layers, enabling flexible switching between different map styles — such as satellite, hybrid, or custom layers — directly within the widget, with just a few clicks.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/map-type-1-ce.webp" alt="The first step in configuring the map widget is selecting the map type. SENTIENT offers several map widgets, including Image Map, which allows you to use a custom background image as the map. You can also configure map layers, enabling flexible switching between different map styles — such as satellite, hybrid, or custom layers — directly within the widget, with just a few clicks." loading="lazy"><figcaption>The first step in configuring the map widget is selecting the map type. SENTIENT offers several map widgets, including Image Map, which allows you to use a custom background image as the map. You can also configure map layers, enabling flexible switching between different map styles — such as satellite, hybrid, or custom layers — directly within the widget, with just a few clicks.</figcaption></figure></div>


<br>

**Adding a new map layer**

You can add additional layer to the map widget by following these steps:

- Click "Add layer".
- Enter a label for the layer — this name will be shown in the widget&#39;s layer switcher.
- Choose the map provider by selecting from the available options (OpenStreetMap, Google, HERE, Tencent) or by specifying a custom tile server.
- Apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/map-type-adding-layer-1-ce.webp" alt="Click &quot;Add layer&quot;." loading="lazy"><figcaption>Click "Add layer".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-type-adding-layer-2-ce.webp" alt="Enter a label for the layer. Select a provider from the available options, or add a custom provider and specify its layer." loading="lazy"><figcaption>Enter a label for the layer. Select a provider from the available options, or add a custom provider and specify its layer.</figcaption></figure></div>


Now switch to the new layer on the widget.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/changing-map-type-1-ce.webp" alt="Click the &quot;Layer&quot; icon button on the widget." loading="lazy"><figcaption>Click the "Layer" icon button on the widget.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/changing-map-type-2-ce.webp" alt="You will see the available map layers. Switch between them." loading="lazy"><figcaption>You will see the available map layers. Switch between them.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/changing-map-type-3-ce.webp" alt="Enter a label for the layer — this name will be shown in the widget&#39;s layer switcher. Choose the map provider by selecting from the available options (OpenStreetMap, Google, HERE, Tencent) or by specifying a custom tile server. Apply changes." loading="lazy"><figcaption>Enter a label for the layer — this name will be shown in the widget&#39;s layer switcher. Choose the map provider by selecting from the available options (OpenStreetMap, Google, HERE, Tencent) or by specifying a custom tile server. Apply changes.</figcaption></figure></div>


<br>

In the "**Layer settings**", you can also enable the "**Reference layer**" option — a special transparent layer that contains labeled map elements: 

- Go to the "Layer settings" by clicking the "gear" icon.
- From the dropdown menu, select the layer type, or leave it as "No layer" if you don&#39;t want to use one.
- Apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/map-type-reference-layer-1-ce.webp" alt="Go to the &quot;Layer settings&quot; by clicking the &quot;gear&quot; icon." loading="lazy"><figcaption>Go to the "Layer settings" by clicking the "gear" icon.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-type-reference-layer-2-ce.webp" alt="From the dropdown menu, select the layer type, or leave it as &quot;No layer&quot; if you don&#39;t want to use one. Apply changes." loading="lazy"><figcaption>From the dropdown menu, select the layer type, or leave it as "No layer" if you don&#39;t want to use one. Apply changes.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-type-reference-layer-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Overlays

Map items are visual elements displayed on a map widget to represent the spatial position, area, or influence zone of entities and data.
These elements help visualize and interact with your devices, assets, or other tracked objects based on their spatial data.

SENTIENT supports the following map item types:

- A **marker** is a point on the map based on the coordinates specified in the entity. It is used to display the location of a device, asset, vehicles or any tracked object.
- A **polygon** is a flat, closed shape made up of multiple connected points. It is used to represent areas or boundaries on the map. You can use the polygon option to mark your assets or any other objects. The polygon is based on coordinates specified in the entity.
- A **circle** is a flat shape defined by a center point and a radius, with all boundary points equidistant from the central point. It is ideal for visualizing zones of influence or coverage areas. The circle is based on coordinates specified in the entity.

Each map item type is bound to an entity and visualized based on its coordinates, provided as either attributes or telemetry.
You can customize their appearance, behavior, and interaction rules directly in the widget settings.

### Marker

Markers are commonly used to indicate the location of buildings, fixed sensors, vehicle tracking, or any other static or moving entities.

To be placed on the map, the entity must have coordinates as attributes or telemetry in the following format:
```
Latitude,Longitude
```


![image](/images/user-guide/widgets/maps/marker-1-ce.webp)


#### Place marker on map

To place a marker on the map, follow these steps:

- Enter widget edit mode and go to the "Overlays" section.
- Make sure you&#39;re on the "Marker" tab and click "Add marker".
- Select the data source - it can be a device, an entity alias, or a function.
- Define the coordinate keys. By default, SENTIENT uses *latitude* and *longitude* attributes as the coordinate keys for the marker. If your entity uses different key names, update them here.
- Apply the changes.

The marker will appear on the map based on the specified coordinates.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/add-marker-1-ce.webp" alt="Enter widget edit mode and go to the &quot;Overlays&quot; section. Make sure you&#39;re on the &quot;Marker&quot; tab and click &quot;Add marker&quot;." loading="lazy"><figcaption>Enter widget edit mode and go to the "Overlays" section. Make sure you&#39;re on the "Marker" tab and click "Add marker".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/add-marker-2-ce.webp" alt="Select the data source - it can be a device, an entity alias, or a function. Define the coordinate keys. By default, SENTIENT uses *latitude* and *longitude* attributes as the coordinate keys for the marker. If your entity uses different key names, update them here. Apply the changes." loading="lazy"><figcaption>Select the data source - it can be a device, an entity alias, or a function. Define the coordinate keys. By default, SENTIENT uses *latitude* and *longitude* attributes as the coordinate keys for the marker. If your entity uses different key names, update them here. Apply the changes.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/add-marker-3-ce.webp" alt="The marker will appear on the map based on the specified coordinates." loading="lazy"><figcaption>The marker will appear on the map based on the specified coordinates.</figcaption></figure></div>


#### Marker configuration

To configure a specific marker, switch to the map widget&#39;s edit mode. In the "Overlays" section, click the "gear" icon button next to the desired marker to open its configuration panel.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-configuration-1-ce.webp" alt="To configure a specific marker, switch to the map widget&#39;s edit mode and, in the Overlays section, click the gear icon next to the desired marker to open its configuration panel." loading="lazy"><figcaption>To configure a specific marker, switch to the map widget&#39;s edit mode and, in the Overlays section, click the gear icon next to the desired marker to open its configuration panel.</figcaption></figure></div>


<br>

**Datasource**

Specify the data source for the marker. It can be:
- A [device](/docs/user-guide/ui/devices/)
- An [entity alias](/docs/user-guide/ui/aliases/)
- A function

If needed, use the data filter to refine the selection (e.g., filter by name or type).


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-configuration-datasource-1-ce.webp" alt="Specify the marker data source — it can be a device, entity alias, or function. If necessary, use a filter." loading="lazy"><figcaption>Specify the marker data source — it can be a device, entity alias, or function. If necessary, use a filter.</figcaption></figure></div>


<br>

**Keys**

Define the coordinate keys.
By default, SENTIENT uses *latitude* and *longitude* attributes as the default coordinate keys.
If your entity uses custom key names, update them accordingly.

You can also define additional keys for dynamic display elements, such as marker color, tooltip content, Label text, etc.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-configuration-keys-1-ce.webp" alt="Define the coordinate keys. SENTIENT automatically sets the coordinate keys as latitude and longitude. If your entity uses custom coordinate key names, update them here. Additional data keys can be used for labels, tooltips, and displaying extra information directly on the map." loading="lazy"><figcaption>Define the coordinate keys. SENTIENT automatically sets the coordinate keys as latitude and longitude. If your entity uses custom coordinate key names, update them here. Additional data keys can be used for labels, tooltips, and displaying extra information directly on the map.</figcaption></figure></div>


<br>

**Marker**

This section defines how marker appear on the map.
Customize the marker by selecting a different one from a variety of standard shapes and icons, adjusting its size and color, or use your own images for full visual flexibility.

*Marker styling example*: This example demonstrates how to configure marker styling so that its color changes automatically based on the value of the "state" key:
- Green marker — when state = "opened"
- Red marker — when state has any other value
- Gray marker — if the state key does not exist

This approach visually reflects the status of the marker, greatly enhancing monitoring convenience.


1. Customize the marker by selecting a different one from a variety of standard shapes and icons, and adjusting its size.

1. Use a function that dynamically changes the marker color based on the value of the "state" key.

1. Apply all changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-icon-color-1-ce.webp" alt="Customize the marker by selecting a different one from a variety of standard shapes and icons, and adjusting its size." loading="lazy"><figcaption>Customize the marker by selecting a different one from a variety of standard shapes and icons, and adjusting its size.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-icon-color-2-ce.webp" alt="Use a function that dynamically changes the marker color based on the value of the &quot;state&quot; key." loading="lazy"><figcaption>Use a function that dynamically changes the marker color based on the value of the "state" key.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-icon-color-3-ce.webp" alt="Apply all changes." loading="lazy"><figcaption>Apply all changes.</figcaption></figure></div>


Color-changing function based on the "state" key value:
```js
var state = data.state;
if (state  !== '') {
  if (state == 'opened'){
    return 'green';
  } else {
    return 'red';
  }
} else {
  return 'grey';
}
```


Currently, the "state" key has the value "opened", so the marker is displayed in green.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-icon-color-4-ce.webp" alt="Currently, the &quot;state&quot; key has the value &quot;opened&quot;, so the marker is displayed in green." loading="lazy"><figcaption>Currently, the "state" key has the value "opened", so the marker is displayed in green.</figcaption></figure></div>


As soon as the value of the "state" key changes to anything else, the marker will turn red.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-icon-color-5-ce.webp" alt="As soon as the value of the &quot;state&quot; key changes to anything else, the marker will turn red." loading="lazy"><figcaption>As soon as the value of the "state" key changes to anything else, the marker will turn red.</figcaption></figure></div>


<br>

**Label**

The marker label is placed above the icon and, by default, displays the entity name. 
You can edit the label text or use a label function to show more dynamic information.

Label styling example:

```html
<div style='position: relative; white-space: nowrap; text-align: center; font-size: 14px; top: 2px;'>
    <span style='margin-left: -500%;'></span>
    <div style='border: 2px solid #EC9704; border-radius: 10px; color: #000; background-color: #fff;  padding-left: 8px; padding-right: 8px; padding-top: 3px; padding-bottom: 3px;'>${entityName}</div>
</div>
```


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-label-1-ce.webp" alt="Here, you can customize the label displayed above the marker. By default, the label displays the entity name. You can edit the label text or use a label function to display more dynamic information;" loading="lazy"><figcaption>Here, you can customize the label displayed above the marker. By default, the label displays the entity name. You can edit the label text or use a label function to display more dynamic information;</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-label-2-ce.webp" alt="Customized marker label." loading="lazy"><figcaption>Customized marker label.</figcaption></figure></div>


<br>

**Tooltip**

Here you can configure a tooltip that appears when you click on or hover over the marker.
Use the tooltip pattern or tooltip function to define more dynamic content. Alternatively, you can hide the tooltip altogether.

For example, you want the tooltip displays the status of a fueling station (open/closed) by retrieving the value from the "state" key, which is specified as one of the "Additional data keys" in the "Keys" section.   
Use the function below and paste it into the Tooltip function window:

```js
const stateObj = {
    "opened": "#4CAF50",
    "closed": "#D12730"
};

const currentState = data.state;

return `<div style="display: flex; justify-content: space-between; align-items: center; gap: 7px">
        <span style="font-weight: 600; font-size: 13px; line-height: 20px; color: #000000de">${data.entityName} is ${currentState}</span>
        <span style="width: 10px; height: 10px; border-radius: 100px; background-color: ${stateObj[currentState]}"></span>
    </div>`;
```


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-tooltip-1-ce.webp" alt="Use the tooltip pattern or tooltip function;" loading="lazy"><figcaption>Use the tooltip pattern or tooltip function;</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-tooltip-2-ce.webp" alt="Click on the marker to display a tooltip." loading="lazy"><figcaption>Click on the marker to display a tooltip.</figcaption></figure></div>


**Tag actions**

You can add an action to a tooltip as a tag. This can be to switch to a new dashboard state or another dashboard, to open an external URL, or even to initiate a custom action. 
Learn more about the available action types and how to configure them in the [widget actions documentation](/docs/user-guide/ui/widget-actions/).

First, you need to add a tag action and then reference its name in the tooltip function:


1. Click the "Add tag action" icon button.

1. Configure the action and click "Add".

1. Now, you need to add the tag action link to the tooltip function. Expand the tooltip function window to fullscreen for easier editing.

1. Edit the function by adding a link to the tag action. Be sure to specify the tag action name correctly.

1. Apply all changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-tooltip-action-1-ce.webp" alt="Click the &quot;Add tag action&quot; icon button." loading="lazy"><figcaption>Click the "Add tag action" icon button.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-tooltip-action-2-ce.webp" alt="Configure the action and click &quot;Add&quot;." loading="lazy"><figcaption>Configure the action and click "Add".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-tooltip-action-3-ce.webp" alt="Now, you need to add the tag action link to the tooltip function. Expand the tooltip function window to fullscreen for easier editing." loading="lazy"><figcaption>Now, you need to add the tag action link to the tooltip function. Expand the tooltip function window to fullscreen for easier editing.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-tooltip-action-4-ce.webp" alt="Edit the function by adding a link to the tag action. Be sure to specify the tag action name correctly." loading="lazy"><figcaption>Edit the function by adding a link to the tag action. Be sure to specify the tag action name correctly.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-tooltip-action-5-ce.webp" alt="Apply all changes." loading="lazy"><figcaption>Apply all changes.</figcaption></figure></div>


The function below already includes a reference to the tag action named "my-action".
If you gave your tag action a different name, please replace "my-action" with your actual tag name.
Use this function to replace the previous tooltip function:

```js
const stateObj = {
  "opened": "#4CAF50",
  "closed": "#D12730"
};

const currentState = data.state;

return `<div style="text-align: center">
            <div style="display: flex; justify-content: space-between; align-items: center; gap: 7px">
                <span style="font-weight: 600; font-size: 13px; line-height: 20px; color: #000000de">${data.entityName} is ${currentState}</span>
                <span style="width: 10px; height: 10px; border-radius: 100px; background-color: ${stateObj[currentState]}"></span>
            </div>
            <link-act name='my-action'>Details</link-act>
    </div>`;
```


Click on the marker. In the tooltip that appears, you&#39;ll see a tag — click on it. The action you defined in the tag&#39;s settings will be executed.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-tooltip-action-6-ce.webp" alt="Click on the marker. In the tooltip that appears, you&#39;ll see a tag — click on it." loading="lazy"><figcaption>Click on the marker. In the tooltip that appears, you&#39;ll see a tag — click on it.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-tooltip-action-7-ce.webp" alt="The action you defined in the tag&#39;s settings will be executed." loading="lazy"><figcaption>The action you defined in the tag&#39;s settings will be executed.</figcaption></figure></div>


<br>

**Behavior**

Set the behavior of the marker when you click it.


1. Go to the "Behavior" section and click the "On click" action field to define the action instead of the default "Do nothing".

1. Set up the desired action and apply the changes.

1. Click on the marker.

1. The action you specified in the action settings will be triggered.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-behavior-1-ce.webp" alt="Go to the &quot;Behavior&quot; section and click the &quot;On click&quot; action field to define the action instead of the default &quot;Do nothing&quot;." loading="lazy"><figcaption>Go to the "Behavior" section and click the "On click" action field to define the action instead of the default "Do nothing".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-behavior-2-ce.webp" alt="Set up the desired action and apply the changes." loading="lazy"><figcaption>Set up the desired action and apply the changes.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-behavior-3-ce.webp" alt="Click on the marker." loading="lazy"><figcaption>Click on the marker.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-behavior-4-ce.webp" alt="The action you specified in the action settings will be triggered." loading="lazy"><figcaption>The action you specified in the action settings will be triggered.</figcaption></figure></div>


<br>

**Groups**

Markers can be grouped, allowing you to easily show or hide grouped elements later using the "Groups" tab.

- In the "Groups" section, enter a name for the group to which you want to add this marker.
- A "Groups" icon button will appear on the widget. Click on it.
- To hide a group, uncheck the box next to its name.
- The markers that belong to this group have been hidden.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-groups-1-ce.webp" alt="In the &quot;Groups&quot; section, enter a name for the group to which you want to add this marker." loading="lazy"><figcaption>In the "Groups" section, enter a name for the group to which you want to add this marker.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-groups-2-ce.webp" alt="A &quot;Groups&quot; icon button will appear on the widget. Click on it." loading="lazy"><figcaption>A "Groups" icon button will appear on the widget. Click on it.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-groups-3-ce.webp" alt="To hide a group, uncheck the box next to its name." loading="lazy"><figcaption>To hide a group, uncheck the box next to its name.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-groups-4-ce.webp" alt="The markers that belong to this group have been hidden." loading="lazy"><figcaption>The markers that belong to this group have been hidden.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/marker-configuration-appearance-groups-5-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<br>

**Marker editing tools**

You can use the built-in tools to perform operations on markers such as **Add** / **Move** / **Delete**. By default, these tools are disabled.

Check the boxes next to the tools you want to enable.


1. You can use the built-in tools to perform operations on markers such as Add / Move / Delete. By default, these tools are disabled. Check the boxes next to the tools you want to enable.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/marker-editing-tools-1-ce.webp" alt="You can use the built-in tools to perform operations on markers such as Add / Move / Delete. By default, these tools are disabled. Check the boxes next to the tools you want to enable." loading="lazy"><figcaption>You can use the built-in tools to perform operations on markers such as Add / Move / Delete. By default, these tools are disabled. Check the boxes next to the tools you want to enable.</figcaption></figure></div>


**Adding marker**

If your entity doesn&#39;t have coordinates set, you can **manually place marker using the map widget tools** — its coordinates will be automatically saved to the entity as attributes.

First, add the marker placement tool to the map:

- In the "**Edit marker**" section, check the "**Add**" tool.
- Next, select the **attribute scope** where the coordinates will be stored: "**Server**" or "**Shared**".
- Optionally, enable snapping to other vertices for precision drawing.
- Then, save the changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/manually-add-marker-1-ce.webp" alt="In the &quot;Edit marker&quot; section, check the &quot;Add&quot; tool. Next, select the attribute scope where the coordinates will be stored: &quot;Server&quot; or &quot;Shared&quot;. Optionally, enable snapping to other vertices for precision drawing. Then, save the changes." loading="lazy"><figcaption>In the "Edit marker" section, check the "Add" tool. Next, select the attribute scope where the coordinates will be stored: "Server" or "Shared". Optionally, enable snapping to other vertices for precision drawing. Then, save the changes.</figcaption></figure></div>


You can now place the marker on the map:

- On the map widget, locate and click the "Place marker" icon button. If you&#39;re using an alias with multiple entities as the data source, you&#39;ll need to select the appropriate entity from the dropdown menu.
- Find the location on the map where you want to place the marker and click on it.
- The marker will be added, and its coordinates will be automatically saved to the entity as attributes.


1. On the map widget, locate and click the "Place marker" icon button. If you&#39;re using an alias with multiple entities as the data source, you&#39;ll need to select the appropriate entity from the dropdown menu.

1. Find the location on the map where you want to place the marker and click on it.

1. The marker will be added, and its coordinates will be automatically saved to the entity as attributes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/place-marker-1-ce.webp" alt="On the map widget, locate and click the &quot;Place marker&quot; icon button. If you&#39;re using an alias with multiple entities as the data source, you&#39;ll need to select the appropriate entity from the dropdown menu." loading="lazy"><figcaption>On the map widget, locate and click the "Place marker" icon button. If you&#39;re using an alias with multiple entities as the data source, you&#39;ll need to select the appropriate entity from the dropdown menu.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/place-marker-2-ce.webp" alt="Find the location on the map where you want to place the marker and click on it." loading="lazy"><figcaption>Find the location on the map where you want to place the marker and click on it.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/place-marker-3-ce.webp" alt="The marker will be added, and its coordinates will be automatically saved to the entity as attributes." loading="lazy"><figcaption>The marker will be added, and its coordinates will be automatically saved to the entity as attributes.</figcaption></figure></div>


<br>
Also, by selecting the checkboxes next to the desired tools, you&#39;ll be able to **move** or **remove** a marker.

**Moving marker**


<div class="st-callout info">


Don&#39;t forget to enable the "**Move**" tool in the marker settings under the "**Edit marker**" section.


</div>


To move the marker, click and hold the marker with your mouse, drag it to the new location, and then release the mouse button.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/move-marker-1-ce.webp" alt="To move the marker, click and hold the marker with your mouse, drag it to the new location, and then release the mouse button." loading="lazy"><figcaption>To move the marker, click and hold the marker with your mouse, drag it to the new location, and then release the mouse button.</figcaption></figure></div>


**Removing marker**


<div class="st-callout info">


Don&#39;t forget to enable the "**Remove**" tool in the marker settings under the "**Edit marker**" section.


</div>


To delete a marker, simply click on it, then click the trash bin icon in the menu at the bottom of the widget.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/remove-marker-1-ce.webp" alt="To delete a marker, simply click on it, then click the trash bin icon in the menu at the bottom of the widget." loading="lazy"><figcaption>To delete a marker, simply click on it, then click the trash bin icon in the menu at the bottom of the widget.</figcaption></figure></div>


<br>

**Use map markers clustering**

Map clustering is a feature that automatically groups multiple markers located within the same visible area at a certain zoom level into a single cluster — a circular icon displaying the number of grouped items inside, instead of showing each marker individually.

This greatly improves map readability, especially when visualizing a large number of markers.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/use-map-markers-clustering-1-ce.webp" alt="To enable clustering for map markers, check the corresponding option and configure the necessary settings." loading="lazy"><figcaption>To enable clustering for map markers, check the corresponding option and configure the necessary settings.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/use-map-markers-clustering-2-ce.webp" alt="Change the zoom level." loading="lazy"><figcaption>Change the zoom level.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/use-map-markers-clustering-3-ce.webp" alt="Your markers with clustering enabled will group into a circular icon that shows the number of clustered items inside." loading="lazy"><figcaption>Your markers with clustering enabled will group into a circular icon that shows the number of clustered items inside.</figcaption></figure></div>


### Polygon

The polygon is a flat shape defined by a finite number of points. 
It can be used to mark areas such as buildings, fields, service areas, visualize coverage areas or restricted regions, etc.


![image](/images/user-guide/widgets/maps/polygon-1-ce.webp)


<br>

To display an entity as a polygon, it must have coordinates provided as attributes or telemetry in the following format:

```
[[1Latitude,1Longitude],[2Latitude,2Longitude],...,[nLatitude,nLongitude]]
```

where **n** - number of coordinates which polygon is described by.

#### Adding polygon

To place the polygon on the map, follow these steps:

- Enter widget edit mode and go to the "Overlays" section.
- Switch to the "Polygons" tab and click "Add polygon".
- Select the entity that will be represented as a polygon. This can be a device, entity alias, or function.
- Define the key with the coordinates of the polygon. SENTIENT will use the "perimeter" key by default to read the polygon coordinates from the entity&#39;s attributes. If you use a different key, update it accordingly.
- Click "Apply" — the polygon will appear on the map based on the entity&#39;s data.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/add-polygon-1-ce.webp" alt="Enter widget edit mode and go to the &quot;Overlays&quot; section. Switch to the &quot;Polygons&quot; tab and click &quot;Add polygon&quot;." loading="lazy"><figcaption>Enter widget edit mode and go to the "Overlays" section. Switch to the "Polygons" tab and click "Add polygon".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/add-polygon-2-ce.webp" alt="Select the entity that will be represented as a polygon. This can be a device, entity alias, or function. Define the key with the coordinates of the polygon. SENTIENT will use the &quot;perimeter&quot; key by default to read the polygon coordinates from the entity&#39;s attributes. If you use a different key, update it accordingly. Click &quot;Apply&quot;." loading="lazy"><figcaption>Select the entity that will be represented as a polygon. This can be a device, entity alias, or function. Define the key with the coordinates of the polygon. SENTIENT will use the "perimeter" key by default to read the polygon coordinates from the entity&#39;s attributes. If you use a different key, update it accordingly. Click "Apply".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/add-polygon-3-ce.webp" alt="The polygon will appear on the map based on the entity&#39;s data." loading="lazy"><figcaption>The polygon will appear on the map based on the entity&#39;s data.</figcaption></figure></div>


#### Polygon configuration

To configure a specific polygon, switch to the map widget&#39;s edit mode.
Then, in the "Polygon" tab under the "Overlays" section, click the "gear" icon button next to the desired polygon to open its configuration panel.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/polygon-configuration-1-ce.webp" alt="To configure a specific polygon, switch to the map widget&#39;s edit mode. Then, in the &quot;Polygon&quot; tab under the &quot;Overlays&quot; section, click the &quot;gear&quot; icon button next to the desired polygon to open its configuration panel." loading="lazy"><figcaption>To configure a specific polygon, switch to the map widget&#39;s edit mode. Then, in the "Polygon" tab under the "Overlays" section, click the "gear" icon button next to the desired polygon to open its configuration panel.</figcaption></figure></div>


<br>

**Datasource**

Specify the polygon’s data source — it can be a device, an entity alias, or a function.

If needed, apply a filter to narrow down the selection.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/polygon-configuration-datasource-1-ce.webp" alt="Specify the polygon data source — it can be a device, entity alias, or function. If necessary, use a filter." loading="lazy"><figcaption>Specify the polygon data source — it can be a device, entity alias, or function. If necessary, use a filter.</figcaption></figure></div>


<br>

**Keys**

Define the key that contains the polygon coordinates.
By default, SENTIENT uses "perimeter" as the polygon key. If your entity uses a different key name, make sure to update it here.

Additional data keys can be used for labels, tooltips, or to display extra information directly on the map.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/polygon-configuration-keys-1-ce.webp" alt="Define the key that contains the polygon coordinates. By default, SENTIENT uses &quot;perimeter&quot; as the polygon key. If your entity uses a different key name, make sure to update it here. Additional data keys can be used for labels, tooltips, or to display extra information directly on the map." loading="lazy"><figcaption>Define the key that contains the polygon coordinates. By default, SENTIENT uses "perimeter" as the polygon key. If your entity uses a different key name, make sure to update it here. Additional data keys can be used for labels, tooltips, or to display extra information directly on the map.</figcaption></figure></div>


<br>

**Filling the polygon**

**Fill** — defines how the polygon is filled on the map:
- Color – Sets a solid fill color.
- Stripe – Applies diagonal hatching instead of a solid color, useful for indicating special zones.
- Image – Allows you to use an image as the background fill.

**Stroke** – defines the polygon outline:
- Border color
- Line thickness


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/polygon-color-1-ce.webp" alt="Change the fill color and stroke color of the polygon. For the fill, you can also use stripes or an image as a background." loading="lazy"><figcaption>Change the fill color and stroke color of the polygon. For the fill, you can also use stripes or an image as a background.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/polygon-color-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<br>

**Label** 

Configure the label displayed above the polygon.
By default, the label shows the name of the entity linked to that polygon. You can manually edit the label text or use a label function to display dynamic information.

For example, the label can show the current status of the polygon, providing users with a quick and clear understanding of its state.
If desired, you can also hide the label entirely.

```html
<div style='position: relative; white-space: nowrap; text-align: center; font-size: 10px; top: -7px;'>
  <span style='margin-left: -500%;'></span>
  <div style='border: 2px solid #3388FF; border-radius: 5px; color: #000; background-color: #fff;  padding-left: 4px; padding-right: 4px; padding-top: 2px; padding-bottom: 2px;'>${entityLabel}</div>
</div>
```


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/polygon-label-1-ce.webp" alt="Configure the label displayed above the polygon. By default, the label shows the name of the entity linked to that polygon. You can manually edit the label text or use a label function to display dynamic information." loading="lazy"><figcaption>Configure the label displayed above the polygon. By default, the label shows the name of the entity linked to that polygon. You can manually edit the label text or use a label function to display dynamic information.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/polygon-label-2-ce.webp" alt="Custom polygon label." loading="lazy"><figcaption>Custom polygon label.</figcaption></figure></div>


<br>

**Tooltip**

Here you can configure a tooltip that appears when you click on or hover over the polygon. 
Use the tooltip pattern or tooltip function to define more dynamic content. 
Alternatively, you can hide the tooltip altogether.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/polygon-tooltip-1-ce.webp" alt="Here you can configure a tooltip that appears when you click on or hover over the polygon. Use the tooltip pattern or tooltip function to define more dynamic content. Alternatively, you can hide the tooltip altogether." loading="lazy"><figcaption>Here you can configure a tooltip that appears when you click on or hover over the polygon. Use the tooltip pattern or tooltip function to define more dynamic content. Alternatively, you can hide the tooltip altogether.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/polygon-tooltip-2-ce.webp" alt="Click on the polygon to display the tooltip." loading="lazy"><figcaption>Click on the polygon to display the tooltip.</figcaption></figure></div>


<br>

**Behavior**


1. Go to the "Behavior" section and click the "On click" action field to define the action instead of the default "Do nothing".

1. Set up the desired action and apply the changes.

1. Click on the polygon.

1. The action you specified in the action settings will be triggered.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/polygon-behavior-1-ce.webp" alt="Go to the &quot;Behavior&quot; section and click the &quot;On click&quot; action field to define the action instead of the default &quot;Do nothing&quot;." loading="lazy"><figcaption>Go to the "Behavior" section and click the "On click" action field to define the action instead of the default "Do nothing".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/polygon-behavior-2-ce.webp" alt="Set up the desired action and apply the changes." loading="lazy"><figcaption>Set up the desired action and apply the changes.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/polygon-behavior-3-ce.webp" alt="Click on the polygon." loading="lazy"><figcaption>Click on the polygon.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/polygon-behavior-4-ce.webp" alt="The action you specified in the action settings will be triggered." loading="lazy"><figcaption>The action you specified in the action settings will be triggered.</figcaption></figure></div>


<br>

**Groups**

Polygons can be grouped, allowing you to easily show or hide grouped elements later using the "Groups" tab.


1. In the "Groups" section, enter a name for the group to which you want to add this polygon;

1. A "Groups" icon button will appear on the widget. Click on it;

1. To hide a group, uncheck the box next to its name.

1. The polygon that belong to this group have been hidden.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/polygon-groups-1-ce.webp" alt="In the &quot;Groups&quot; section, enter a name for the group to which you want to add this polygon;" loading="lazy"><figcaption>In the "Groups" section, enter a name for the group to which you want to add this polygon;</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/polygon-groups-2-ce.webp" alt="A &quot;Groups&quot; icon button will appear on the widget. Click on it;" loading="lazy"><figcaption>A "Groups" icon button will appear on the widget. Click on it;</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/polygon-groups-3-ce.webp" alt="To hide a group, uncheck the box next to its name." loading="lazy"><figcaption>To hide a group, uncheck the box next to its name.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/polygon-groups-4-ce.webp" alt="The polygon that belong to this group have been hidden." loading="lazy"><figcaption>The polygon that belong to this group have been hidden.</figcaption></figure></div>


<br>

**Polygon editing tools**

You can use the built-in tools to perform operations on markers such as **Add** / **Edit** / **Move** / **Delete**. By default, these tools are disabled.

Check the boxes next to the tools you want to enable.


1. You can use the built-in tools to perform operations on markers such as Add / Move / Delete. By default, these tools are disabled. Check the boxes next to the tools you want to enable.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/polygon-editing-tools-1-ce.webp" alt="You can use the built-in tools to perform operations on markers such as Add / Move / Delete. By default, these tools are disabled. Check the boxes next to the tools you want to enable." loading="lazy"><figcaption>You can use the built-in tools to perform operations on markers such as Add / Move / Delete. By default, these tools are disabled. Check the boxes next to the tools you want to enable.</figcaption></figure></div>


<br>

**Adding polygon**

If an entity doesn&#39;t have polygon coordinates set, you can **manually place polygon using the map widget tools** — its coordinates will be automatically saved to the entity as attribute.

First, add the polygon placement tool to the map:

- In the "**Edit marker**" section, check the "**Add**" tool.
- Next, select the **attribute scope** where the coordinates will be stored: "**Server**" or "**Shared**".
- Optionally, enable snapping to other vertices for precision drawing.
- Then, save the changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/manually-add-polygon-1-ce.webp" alt="In the &quot;Edit polygon&quot; section, check the &quot;Add&quot; tool. Next, select the attribute scope where the coordinate will be stored: &quot;Server&quot; or &quot;Shared&quot;. Optionally, enable snapping to other vertices for precision drawing. Then, save the changes." loading="lazy"><figcaption>In the "Edit polygon" section, check the "Add" tool. Next, select the attribute scope where the coordinate will be stored: "Server" or "Shared". Optionally, enable snapping to other vertices for precision drawing. Then, save the changes.</figcaption></figure></div>


You can now place the polygon on the map:


1. The map widget now offers two tools for adding a polygon: "Drew rectangle" and "Drew polygon". Choose the option that suits your needs.

1. If you&#39;re using an alias with multiple entities as the data source, select the desired entity from the dropdown list.

1. Find the desired location on the map and click to place the first point;

1. Adjust the polygon to the desired size, then click again to finish. If you&#39;re using "Drew polygon", make sure to close the shape by clicking the first point once you&#39;ve placed all others.

1. The polygon will be added, and its coordinates will be automatically saved to the entity as attribute.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/place-polygon-1-ce.webp" alt="The map widget now offers two tools for adding a polygon: &quot;Drew rectangle&quot; and &quot;Drew polygon&quot;. Choose the option that suits your needs." loading="lazy"><figcaption>The map widget now offers two tools for adding a polygon: "Drew rectangle" and "Drew polygon". Choose the option that suits your needs.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/place-polygon-2-ce.webp" alt="If you&#39;re using an alias with multiple entities as the data source, select the desired entity from the dropdown list." loading="lazy"><figcaption>If you&#39;re using an alias with multiple entities as the data source, select the desired entity from the dropdown list.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/place-polygon-3-ce.webp" alt="Find the desired location on the map and click to place the first point;" loading="lazy"><figcaption>Find the desired location on the map and click to place the first point;</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/place-polygon-4-ce.webp" alt="Adjust the polygon to the desired size, then click again to finish. If you&#39;re using &quot;Drew polygon&quot;, make sure to close the shape by clicking the first point once you&#39;ve placed all others." loading="lazy"><figcaption>Adjust the polygon to the desired size, then click again to finish. If you&#39;re using "Drew polygon", make sure to close the shape by clicking the first point once you&#39;ve placed all others.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/place-polygon-5-ce.webp" alt="The polygon will be added, and its coordinates will be automatically saved to the entity as attribute." loading="lazy"><figcaption>The polygon will be added, and its coordinates will be automatically saved to the entity as attribute.</figcaption></figure></div>


<br>

**Editing polygon**


<div class="st-callout info">


Don&#39;t forget to enable the "**Edit**" tool in the polygon settings under the "**Edit polygon**" section.


</div>


To resize the polygon, click on it — its vertices will appear. Drag any of the points to adjust the polygon’s size.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/edit-polygon-1-ce.webp" alt="To resize the polygon, click on it — its vertices will appear. Drag any of the points to adjust the polygon&#39;s size." loading="lazy"><figcaption>To resize the polygon, click on it — its vertices will appear. Drag any of the points to adjust the polygon&#39;s size.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/edit-polygon-2-ce.webp" alt="Once you&#39;re satisfied with the new size, click anywhere outside the polygon to apply the current dimensions." loading="lazy"><figcaption>Once you&#39;re satisfied with the new size, click anywhere outside the polygon to apply the current dimensions.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/edit-polygon-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<br>

**Moving polygon**


<div class="st-callout info">


Don&#39;t forget to enable the "**Move" tool in the polygon settings under the "**Edit polygon**" section.


</div>


To move the polygon, click on the polygon, hold down the mouse button, and drag it to the new location.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/move-polygon-1-ce.webp" alt="To enable moving a polygon on the map, activate the &quot;Move&quot; tool in the polygon settings under the &quot;Edit polygon&quot; section." loading="lazy"><figcaption>To enable moving a polygon on the map, activate the "Move" tool in the polygon settings under the "Edit polygon" section.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/move-polygon-2-ce.webp" alt="Now, click on the polygon, hold down the mouse button, and drag it to the new location." loading="lazy"><figcaption>Now, click on the polygon, hold down the mouse button, and drag it to the new location.</figcaption></figure></div>


<br>

**Rotating polygon**

TO rotate a polygon:


1. Select the polygon by clicking on it, then click the "Rotate polygon" icon button from the tools at the bottom.

1. Grab any point of the polygon and drag it in the desired direction to rotate it.

1. Once you&#39;re satisfied with the rotation, click the "Rotate polygon" icon button again to finish.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/rotate-polygon-1-ce.webp" alt="Select the polygon by clicking on it, then click the &quot;Rotate polygon&quot; icon button from the tools at the bottom." loading="lazy"><figcaption>Select the polygon by clicking on it, then click the "Rotate polygon" icon button from the tools at the bottom.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/rotate-polygon-2-ce.webp" alt="Grab any point of the polygon and drag it in the desired direction to rotate it." loading="lazy"><figcaption>Grab any point of the polygon and drag it in the desired direction to rotate it.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/rotate-polygon-3-ce.webp" alt="Once you&#39;re satisfied with the rotation, click the &quot;Rotate polygon&quot; icon button again to finish." loading="lazy"><figcaption>Once you&#39;re satisfied with the rotation, click the "Rotate polygon" icon button again to finish.</figcaption></figure></div>


<br>

**Cut polygon area**

To cut out an area from a polygon:


1. Select the polygon by clicking on it, then choose "Cut polygon area" from the tools at the bottom.

1. Draw the area you want to remove by outlining it on the polygon.

1. Close the shape by connecting the first and last points.

1. Click anywhere outside the polygon to save the changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/cut-polygon-area-1-ce.webp" alt="Select the polygon by clicking on it, then choose &quot;Cut polygon area&quot; from the tools at the bottom." loading="lazy"><figcaption>Select the polygon by clicking on it, then choose "Cut polygon area" from the tools at the bottom.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/cut-polygon-area-2-ce.webp" alt="Draw the area you want to remove by outlining it on the polygon." loading="lazy"><figcaption>Draw the area you want to remove by outlining it on the polygon.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/cut-polygon-area-3-ce.webp" alt="Close the shape by connecting the first and last points." loading="lazy"><figcaption>Close the shape by connecting the first and last points.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/cut-polygon-area-4-ce.webp" alt="Click anywhere outside the polygon to save the changes." loading="lazy"><figcaption>Click anywhere outside the polygon to save the changes.</figcaption></figure></div>


<br>

**Removing polygon**


<div class="st-callout info">


Don&#39;t forget to enable the "**Remove**" tool in the polygon settings under the "**Edit polygon**" section.


</div>


To delete a polygon, simply click on it, then click the "trash bin" icon in the menu at the bottom of the widget.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/remove-polygon-1-ce.webp" alt="To delete a polygon, simply click on it, then click the &quot;trash bin&quot; icon in the menu at the bottom of the widget." loading="lazy"><figcaption>To delete a polygon, simply click on it, then click the "trash bin" icon in the menu at the bottom of the widget.</figcaption></figure></div>


### Circle

Circle is a plane figure, boundary points of which are always the same distance away from a fixed central point.
A circle can be used to define areas of influence, such as a Wi-Fi zone or the range of a sensor, and more.
You may mark your assets and any other entities with a circle option.

Circle coordinates must follow this format:

```
{"latitude":CoordinateLatitude, "longitude":CoordinateLongitude, "radius":radius}
``` 


![image](/images/user-guide/widgets/maps/circle-1-ce.webp)


#### Add circle

You can mark your assets and any other entities with a circle using predefined coordinates received as attributes or telemetry. In this example, I&#39;ll use a device, which refers to assets of the type “Parking spots” as the data source.

To place the circle on the map, follow these steps:

- Enter widget edit mode and go to the "Overlays" section.
- Switch to the "Circles" tab and click "Add circle".
- Select the entity that will be represented as a circle. This can be a device, entity alias, or function.
- Define the key with the coordinates of the circle. SENTIENT will use the "perimeter" key by default to read the circle coordinates from the entity&#39;s attribute. If your entity uses a different key name, update it here.
- Click "Apply" — the circle will appear on the map based on the entity's data.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/add-circle-1-ce.webp" alt="Enter widget edit mode and go to the &quot;Overlays&quot; section. Switch to the &quot;Circles&quot; tab and click &quot;Add circle&quot;." loading="lazy"><figcaption>Enter widget edit mode and go to the "Overlays" section. Switch to the "Circles" tab and click "Add circle".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/add-circle-2-ce.webp" alt="Select the entity that will be represented as a circle. This can be a device, entity alias, or function. Define the key with the coordinates of the circle. SENTIENT will use the &quot;perimeter&quot; key by default to read the circle coordinates from the entity&#39;s attribute. If your entity uses a different key name, update it here. Click &quot;Apply&quot; — the circle will appear on the map based on the entity&#39;s data." loading="lazy"><figcaption>Select the entity that will be represented as a circle. This can be a device, entity alias, or function. Define the key with the coordinates of the circle. SENTIENT will use the "perimeter" key by default to read the circle coordinates from the entity&#39;s attribute. If your entity uses a different key name, update it here. Click "Apply" — the circle will appear on the map based on the entity&#39;s data.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/add-circle-3-ce.webp" alt="The circle has been successfully added to the map." loading="lazy"><figcaption>The circle has been successfully added to the map.</figcaption></figure></div>


#### Circle configuration

To configure a specific circle, switch to the map widget&#39;s edit mode.
Then, in the "Circle" tab under the "Overlays" section, click the "gear" icon button next to the desired circle to open its configuration panel.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/circle-configuration-1-ce.webp" alt="To configure a specific circle, switch to the map widget&#39;s edit mode. Then, in the &quot;Circle&quot; tab under the &quot;Overlays&quot; section, click the &quot;gear&quot; icon button next to the desired circle to open its configuration panel." loading="lazy"><figcaption>To configure a specific circle, switch to the map widget&#39;s edit mode. Then, in the "Circle" tab under the "Overlays" section, click the "gear" icon button next to the desired circle to open its configuration panel.</figcaption></figure></div>


<br>

**Datasource**

Specify the circle&#39;s data source — it can be a device, an entity alias, or a function.   
If needed, apply a filter to narrow down the selection.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/circle-configuration-datasource-1-ce.webp" alt="Specify the circle&#39;s data source — it can be a device, an entity alias, or a function. If needed, apply a filter to narrow down the selection." loading="lazy"><figcaption>Specify the circle&#39;s data source — it can be a device, an entity alias, or a function. If needed, apply a filter to narrow down the selection.</figcaption></figure></div>


<br>

**Keys**

Define the key that contains the circle coordinates. By default, SENTIENT uses "perimeter" as the circle key. If your entity uses a different key name, make sure to update it here.

Additional data keys can be used for labels, tooltips, or to display extra information directly on the map.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/circle-configuration-keys-1-ce.webp" alt="Define the key that contains the circle coordinates. By default, SENTIENT uses &quot;perimeter&quot; as the circle key. If your entity uses a different key name, make sure to update it here. Additional data keys can be used for labels, tooltips, or to display extra information directly on the map." loading="lazy"><figcaption>Define the key that contains the circle coordinates. By default, SENTIENT uses "perimeter" as the circle key. If your entity uses a different key name, make sure to update it here. Additional data keys can be used for labels, tooltips, or to display extra information directly on the map.</figcaption></figure></div>


<br>

**Filling the circle**

**Fill** — defines how the circle is filled on the map:
- Color – Sets a solid fill color.
- Stripe – Applies diagonal hatching instead of a solid color, useful for indicating special zones.
- Image – Allows you to use an image as the background fill.

**Stroke** – defines the circle outline: 
- Border color
- Line thickness


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/circle-color-1-ce.webp" alt="Change the fill color and stroke color of the circle. For the fill, you can also use stripes or an image as a background." loading="lazy"><figcaption>Change the fill color and stroke color of the circle. For the fill, you can also use stripes or an image as a background.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/circle-color-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<br>

**Label**

Configure the label displayed above the circle. By default, the label shows the name of the entity linked to that circle. You can manually edit the label text or use a label function to display dynamic information.

For example, the label can show the current status of the circle, providing users with a quick and clear understanding of its state. If desired, you can also hide the label entirely.

```html
<div style='position: relative; white-space: nowrap; text-align: center; font-size: 10px; top: -7px;'>
    <span style='margin-left: -500%;'></span>
    <div style='border: 2px solid #3B7FE1; border-radius: 5px; color: #000; background-color: #fff;  padding-left: 4px; padding-right: 4px; padding-top: 2px; padding-bottom: 2px;'>${entityLabel}</div>
</div>
```


1. Configure the label displayed above the circle. By default, the label shows the name of the entity linked to that circle. You can manually edit the label text or use a label function to display dynamic information.

1. Custom circle label.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/circle-label-1-ce.webp" alt="Configure the label displayed above the circle. By default, the label shows the name of the entity linked to that circle. You can manually edit the label text or use a label function to display dynamic information." loading="lazy"><figcaption>Configure the label displayed above the circle. By default, the label shows the name of the entity linked to that circle. You can manually edit the label text or use a label function to display dynamic information.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/circle-label-2-ce.webp" alt="Custom circle label." loading="lazy"><figcaption>Custom circle label.</figcaption></figure></div>


<br>

**Tooltip**


1. Use tooltip pattern or tooltip function.

1. Click on the circle to display the tooltip.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/circle-tooltip-1-ce.webp" alt="Use tooltip pattern or tooltip function." loading="lazy"><figcaption>Use tooltip pattern or tooltip function.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/circle-tooltip-2-ce.webp" alt="Click on the circle to display the tooltip." loading="lazy"><figcaption>Click on the circle to display the tooltip.</figcaption></figure></div>


<br>

**Behavior**

Set the behavior of the circle when you click it.


1. Go to the "Behavior" section and click the "On click" action field to define the action instead of the default "Do nothing".

1. Set up the desired action and apply the changes.

1. Click on the circle.

1. The action you specified in the action settings will be triggered.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/circle-behavior-1-ce.webp" alt="Go to the &quot;Behavior&quot; section and click the &quot;On click&quot; action field to define the action instead of the default &quot;Do nothing&quot;." loading="lazy"><figcaption>Go to the "Behavior" section and click the "On click" action field to define the action instead of the default "Do nothing".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/circle-behavior-2-ce.webp" alt="Set up the desired action and apply the changes." loading="lazy"><figcaption>Set up the desired action and apply the changes.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/circle-behavior-3-ce.webp" alt="Click on the circle." loading="lazy"><figcaption>Click on the circle.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/circle-behavior-4-ce.webp" alt="The action you specified in the action settings will be triggered." loading="lazy"><figcaption>The action you specified in the action settings will be triggered.</figcaption></figure></div>


<br>

**Groups**

Circles can be grouped, allowing you to easily show or hide grouped elements later using the "Groups" tab.


1. In the "Groups" section, enter a name for the group to which you want to add this circle.

1. Click on the "Groups" icon button.

1. To hide a group, uncheck the box next to its name.

1. The circle that belong to this group have been hidden.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/circle-groups-1-ce.webp" alt="In the &quot;Groups&quot; section, enter a name for the group to which you want to add this circle." loading="lazy"><figcaption>In the "Groups" section, enter a name for the group to which you want to add this circle.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/circle-groups-2-ce.webp" alt="Click on the &quot;Groups&quot; icon button." loading="lazy"><figcaption>Click on the "Groups" icon button.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/circle-groups-3-ce.webp" alt="To hide a group, uncheck the box next to its name." loading="lazy"><figcaption>To hide a group, uncheck the box next to its name.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/circle-groups-4-ce.webp" alt="The circle that belong to this group have been hidden." loading="lazy"><figcaption>The circle that belong to this group have been hidden.</figcaption></figure></div>


<br>

**Circle editing tools**

You can use the built-in tools to perform operations on circles such as **Add** / **Move** / **Delete**. By default, these tools are disabled.

Check the boxes next to the tools you want to activate.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/circle-editing-tools-1-ce.webp" alt="You can use the built-in tools to perform operations on circles such as Add / Move / Delete. By default, these tools are disabled. Check the boxes next to the tools you want to activate." loading="lazy"><figcaption>You can use the built-in tools to perform operations on circles such as Add / Move / Delete. By default, these tools are disabled. Check the boxes next to the tools you want to activate.</figcaption></figure></div>


<br>

**Adding circle**

If an entity doesn&#39;t have circle coordinates set, you can **manually place polygon using the map widget tools** — its coordinates will be automatically saved to the entity as attribute.

First, add the circle placement tool to the map:

- In the "**Edit marker**" section, check the "**Add**" tool.
- Next, select the **attribute scope** where the coordinates will be stored: "**Server**" or "**Shared**".
- Optionally, enable snapping to other vertices for precision drawing.
- Then, save the changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/manually-add-circle-1-ce.webp" alt="In the &quot;Edit marker&quot; section, check the &quot;Add&quot; tool. Next, select the attribute scope where the coordinates will be stored: &quot;Server&quot; or &quot;Shared&quot;. Optionally, enable snapping to other vertices for precision drawing. Then, save the changes." loading="lazy"><figcaption>In the "Edit marker" section, check the "Add" tool. Next, select the attribute scope where the coordinates will be stored: "Server" or "Shared". Optionally, enable snapping to other vertices for precision drawing. Then, save the changes.</figcaption></figure></div>


You can now place the circle on the map:


1. The map widget now offers a tool for adding a circle: "Draw circle". Click on this icon button to begin.

1. Find the desired location on the map and click to place the first point;

1. Adjust the circle to the desired size, then click again to finish.

1. The circle has been added to the map.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/place-circle-1-ce.webp" alt="The map widget now offers a tool for adding a circle: &quot;Draw circle&quot;. Click on this icon button to begin." loading="lazy"><figcaption>The map widget now offers a tool for adding a circle: "Draw circle". Click on this icon button to begin.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/place-circle-2-ce.webp" alt="Find the desired location on the map and click to place the first point;" loading="lazy"><figcaption>Find the desired location on the map and click to place the first point;</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/place-circle-3-ce.webp" alt="Adjust the circle to the desired size, then click again to finish." loading="lazy"><figcaption>Adjust the circle to the desired size, then click again to finish.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/place-circle-4-ce.webp" alt="The circle has been added to the map." loading="lazy"><figcaption>The circle has been added to the map.</figcaption></figure></div>


<br>

**Editing circle**


<div class="st-callout info">


Don&#39;t forget to enable the "**Edit**" tool in the circle settings under the "**Edit polygon**" section.


</div>


To resize the circle, click on it — the radius handle will appear. Drag this point to adjust the size of the circle.
Once you&#39;re satisfied with the new size, click anywhere outside the circle to apply the current dimensions.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/edit-circle-1-ce.webp" alt="To resize the circle, click on it, and a radius edi point will appear. Drag it to adjust the size of the circle." loading="lazy"><figcaption>To resize the circle, click on it, and a radius edi point will appear. Drag it to adjust the size of the circle.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/edit-circle-2-ce.webp" alt="Once you&#39;re satisfied with the new size, click anywhere outside the circle to apply the current dimensions." loading="lazy"><figcaption>Once you&#39;re satisfied with the new size, click anywhere outside the circle to apply the current dimensions.</figcaption></figure></div>


<br>

**Moving circle**


<div class="st-callout info">


Don&#39;t forget to enable the "**Move**" tool in the circle settings under the "**Edit circle**" section.


</div>


To move a circle, click on it, hold down the mouse button, and drag circle to the new location.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/move-circle-1-ce.webp" alt="To move a circle, click on it, hold down the mouse button, and drag circle to the new location." loading="lazy"><figcaption>To move a circle, click on it, hold down the mouse button, and drag circle to the new location.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/move-circle-2-ce.webp" alt="To move a circle, click on it, hold down the mouse button, and drag circle to the new location." loading="lazy"><figcaption>To move a circle, click on it, hold down the mouse button, and drag circle to the new location.</figcaption></figure></div>


<br>

**Removing circle**


<div class="st-callout info">


Don&#39;t forget to enable the "**Remove**" tool in the circle settings under the "**Edit polygon**" section.


</div>


To delete a circle, simply click on it, then click the "trash bin" icon in the menu at the bottom of the widget.'


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/remove-circle-1-ce.webp" alt="To delete a circle, simply click on it, then click the &quot;trash bin&quot; icon in the menu at the bottom of the widget." loading="lazy"><figcaption>To delete a circle, simply click on it, then click the "trash bin" icon in the menu at the bottom of the widget.</figcaption></figure></div>


## Additional datasources

**Additional datasources** are auxiliary data sources that can be used for processing, filtering, or overlaying data on the main entities.
They are often used in map overlay features or tooltips when additional context or information needs to be provided.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/additional-datasources-1-ce.webp" alt="Additional datasources are auxiliary data sources that can be used for processing, filtering, or overlaying data on the main entities. They are often used in map overlay features or tooltips when additional context or information needs to be provided." loading="lazy"><figcaption>Additional datasources are auxiliary data sources that can be used for processing, filtering, or overlaying data on the main entities. They are often used in map overlay features or tooltips when additional context or information needs to be provided.</figcaption></figure></div>


## Map controls

**Map controls** are settings for configuring map control buttons within the widget. They allow you to:
- Specify the **position of control elements** (e.g., top-left, bottom-right, etc.);
- Configure **zoom** interactions (via buttons, mouse wheel, or double-click);
- Choose the zoom **scale units**: metric or imperial.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/map-controls-1-ce.webp" alt="Enable the &quot;Remove&quot; tool in the circle settings under the &quot;Edit circle&quot; section." loading="lazy"><figcaption>Enable the "Remove" tool in the circle settings under the "Edit circle" section.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-controls-2-ce.webp" alt="To delete a circle, simply click on it, then click the &quot;trash bin&quot; icon in the menu at the bottom of the widget." loading="lazy"><figcaption>To delete a circle, simply click on it, then click the "trash bin" icon in the menu at the bottom of the widget.</figcaption></figure></div>


## Map action buttons

**Map action buttons** are interactive buttons displayed on top of the map that trigger predefined actions.
Learn more about the available action types and how to configure them in the [widget actions](/docs/user-guide/ui/widget-actions/) documentation.

Let&#39;s consider an example of adding an action button that will allow users to place new objects on the map.

- In the "**Map action buttons**" section, click "**Add button**".
- Specify a name for the new button — for our example, "Add building" — and set its icon and color.
- Now click the "**Action**" field to define the action, and instead of the default "Do nothing", select "**Place map item**".
- Select the map item type to be placed — in this case, it&#39;s "Marker".
- The custom action function field contains a default function that displays a dialog for creating a device or an asset — exactly what we need.
- Save the changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-1-ce.webp" alt="In the &quot;Map action buttons&quot; section, click &quot;Add button&quot;." loading="lazy"><figcaption>In the "Map action buttons" section, click "Add button".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-2-ce.webp" alt="Specify a name for the new button — for our example, &quot;Add building&quot; — and set its icon and color. Click the &quot;Action&quot; field to define the action, and instead of the default &quot;Do nothing&quot;" loading="lazy"><figcaption>Specify a name for the new button — for our example, "Add building" — and set its icon and color. Click the "Action" field to define the action, and instead of the default "Do nothing"</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-3-ce.webp" alt="Choose the &quot;Place map item&quot; action." loading="lazy"><figcaption>Choose the "Place map item" action.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-4-ce.webp" alt="Select the map item type to be placed — in this case, it&#39;s &quot;Marker&quot;. The custom action function field contains a default function that displays a dialog for creating a device or an asset — exactly what we need. Then, click &quot;Add&quot;." loading="lazy"><figcaption>Select the map item type to be placed — in this case, it&#39;s "Marker". The custom action function field contains a default function that displays a dialog for creating a device or an asset — exactly what we need. Then, click "Add".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-5-ce.webp" alt="Save the changes." loading="lazy"><figcaption>Save the changes.</figcaption></figure></div>


To ensure that newly created entities are immediately displayed on the map, you need to properly configure the data source.

- In the "**Overlays**" section, under the "**Marker**" tab, create a new entity alias as the data source. Name it "**buildings**".
- Since I&#39;ll be creating assets with the asset type "**buildings**", set the filter type to "**Asset type**" and specify the type as "**buildings**".
- Apply all changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-6-ce.webp" alt="In the &quot;Overlays&quot; section, under the &quot;Marker&quot; tab, create a new entity alias as the data source. Name it &quot;buildings&quot;." loading="lazy"><figcaption>In the "Overlays" section, under the "Marker" tab, create a new entity alias as the data source. Name it "buildings".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-7-ce.webp" alt="Since I&#39;ll be creating assets with the asset type &quot;buildings&quot;, set the filter type to &quot;Asset type&quot; and specify the type as &quot;buildings&quot;. Apply all changes." loading="lazy"><figcaption>Since I&#39;ll be creating assets with the asset type "buildings", set the filter type to "Asset type" and specify the type as "buildings". Apply all changes.</figcaption></figure></div>


Now, the action button labeled "Add building" has appeared at the top of the map.

- Find the location on the map where you want to place the entity and click on it.
- In the "Add entity" dialog window that appears, make sure to **enter a name for the new entity** and **select its type — Asset**. Other fields are optional. 
- Then, click "**Create**".

The new marker is now added to the map.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-8-ce.webp" alt="Now, the action button labeled &quot;Add building&quot; has appeared at the top of the map. Find the location on the map where you want to place the entity and click on it." loading="lazy"><figcaption>Now, the action button labeled "Add building" has appeared at the top of the map. Find the location on the map where you want to place the entity and click on it.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-9-ce.webp" alt="In the &quot;Add entity&quot; dialog window that appears, make sure to enter a name for the new entity and select its type — Asset. Other fields are optional. Then, click &quot;Create&quot;." loading="lazy"><figcaption>In the "Add entity" dialog window that appears, make sure to enter a name for the new entity and select its type — Asset. Other fields are optional. Then, click "Create".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-10-ce.webp" alt="The new marker is now added to the map." loading="lazy"><figcaption>The new marker is now added to the map.</figcaption></figure></div>


Go to the "**Assets**" page — here you&#39;ll find your newly created asset, "Building A".


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/map-action-buttons-11-ce.webp" alt="Go to the &quot;Assets&quot; page — here you&#39;ll find your newly created asset, &quot;Building A&quot;." loading="lazy"><figcaption>Go to the "Assets" page — here you&#39;ll find your newly created asset, "Building A".</figcaption></figure></div>


## Common map settings

**Common map settings** are the basic global settings for the Map widget in SENTIENT. They define how the map behaves on load and what is displayed initially.

- **Fit map bounds to cover all markers**: Automatically adjusts the map zoom and position so that all markers are visible when the widget loads.
- **Default map center position**: Sets the center of the map (lat/lng coordinates) if auto-zoom is disabled. Used as the initial map position when the widget is opened.
- **Default map zoom level**: Sets the default zoom level (e.g., 7 for country-level view, 15 for street-level view).
- **Limit of entities to load**: Restricts the number of entities loaded onto the map. This helps protect performance when working with large datasets (for example, a limit of 100 will prevent more than 100 markers from loading at once).


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/common-map-settings-1-ce.webp" alt="Common map settings are the basic global settings for the Map widget in SENTIENT. They define how the map behaves on load and what is displayed initially." loading="lazy"><figcaption>Common map settings are the basic global settings for the Map widget in SENTIENT. They define how the map behaves on load and what is displayed initially.</figcaption></figure></div>


## Appearance

Customize the widget&#39;s appearance.

- **Title** – Sets the name of the widget that appears at the top of the map. This helps identify the map on the dashboard (e.g., "Vehicle Tracking", "Sensor Locations").
- **Card icon** – Defines the icon displayed in the widget header (next to the title). It can be used to visually indicate the map’s context or theme (e.g., GPS, map, transportation icons).


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/appearance-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Card appearance

**Card appearance** section controls the visual appearance of the widget on the dashboard.

- **Background**: Sets the background color of the card.
- **Show card buttons**: Enables or disables the edit and fullscreen buttons in the top-right corner.
- **Card border radius**: Defines the corner rounding of the card.
- **Card padding**: Sets the inner spacing between the map content and the card edges.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/card-appearance-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Actions

You can add buttons to the widget header that will trigger predefined actions. You can learn more about the available action types at [this link](/docs/user-guide/ui/widget-actions/#action-types/).

<br>
As an example, let&#39&#39;s add a button that allows users to place charging stations on the map:

To start, and to ensure that newly created entities are instantly displayed on the map, you need to properly configure the data source.

- In the "**Overlays**" section, under the "**Marker**" tab, create a new entity alias as the data source. Name it "**EV stations**".
- Since we&#39;ll be creating entities of the type "**EV station**", set the filter type to "**Asset type**" and specify the type as "**EV station**".
- Apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/data-source-for-action-1-ce.webp" alt="In the &quot;Overlays&quot; section, under the &quot;Marker&quot; tab, create a new entity alias as the data source. Name it &quot;EV stations&quot;." loading="lazy"><figcaption>In the "Overlays" section, under the "Marker" tab, create a new entity alias as the data source. Name it "EV stations".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/data-source-for-action-2-ce.webp" alt="Since we&#39;ll be creating entities of the type &quot;EV station&quot;, set the filter type to &quot;Asset type&quot; and specify the type as &quot;EV station&quot;. Apply changes." loading="lazy"><figcaption>Since we&#39;ll be creating entities of the type "EV station", set the filter type to "Asset type" and specify the type as "EV station". Apply changes.</figcaption></figure></div>


Now let&#39;s move on to configuring the action:

- Scroll down to the "**Actions**" section and click the "**Add action**" button.
- A new window will open, displaying all your created actions. Click the "plus" icon button in the top-right corner to add one.
- Select the action source as "**Widget header button**", enter a name for the button, and choose its type.
- Optionally, change the icon that will appear next to the button or hide it entirely. You can also set a custom color for the button.
- From the dropdown menu, select the type of action to be performed. In our case, it&#39;s "**Place map item**".
- Next, choose the **type of map item** to be placed — we&#39;ll be placing a "**Marker**".
- The **custom action function** field already contains a default function that opens a dialog for creating a device or an asset — exactly what we need.
- In the "**Action**" section, choose "**Place map item**" from the dropdown menu. Select the type of map item to be placed — in our case, it&#39;s "**Marker**". The Custom action function field contains a default function that opens a dialog to create a device or an asset — exactly what we need.
- Then click "**Add**".
- Apply all changes and save the dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/action-1-ce.webp" alt="Scroll down to the &quot;Actions&quot; section and click the &quot;Add action&quot; button." loading="lazy"><figcaption>Scroll down to the "Actions" section and click the "Add action" button.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-2-ce.webp" alt="A new window will open, displaying all your created actions. Click the &quot;plus&quot; icon button in the top-right corner to add one." loading="lazy"><figcaption>A new window will open, displaying all your created actions. Click the "plus" icon button in the top-right corner to add one.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-3-ce.webp" alt="Select the action source as &quot;Widget header button&quot;, enter a name for the button, and choose its type." loading="lazy"><figcaption>Select the action source as "Widget header button", enter a name for the button, and choose its type.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-4-ce.webp" alt="Optionally, change the icon that will appear next to the button or hide it entirely. You can also set a custom color for the button." loading="lazy"><figcaption>Optionally, change the icon that will appear next to the button or hide it entirely. You can also set a custom color for the button.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-5-ce.webp" alt="From the dropdown menu, select the type of action to be performed. In our case, it&#39;s &quot;Place map item&quot;. Next, choose the type of map item to be placed — we&#39;ll be placing a &quot;Marker&quot;. The custom action function field already contains a default function that opens a dialog for creating a device or an asset — exactly what we need. Then, click &quot;Add&quot;." loading="lazy"><figcaption>From the dropdown menu, select the type of action to be performed. In our case, it&#39;s "Place map item". Next, choose the type of map item to be placed — we&#39;ll be placing a "Marker". The custom action function field already contains a default function that opens a dialog for creating a device or an asset — exactly what we need. Then, click "Add".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-6-ce.webp" alt="Apply all changes and save the dashboard." loading="lazy"><figcaption>Apply all changes and save the dashboard.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-7-ce.webp" alt="A new action button labeled &quot;Add EV station&quot; has now appeared at the top of the map." loading="lazy"><figcaption>A new action button labeled "Add EV station" has now appeared at the top of the map.</figcaption></figure></div>


A new action button labeled "**Add EV station**" has now appeared at the top of the map. Let&#39;s use it.


1. Click the newly created "Add EV station" button. Then, find the location on the map where you want to place the EV station and click on it.

1. In the "Add entity" dialog that appears, make sure to enter a name for the new entity and select its type — Asset. The other fields are optional. Then click "Create".

1. The new "EV station" marker is now added to the map.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/action-place-marker-1-ce.webp" alt="Click the newly created &quot;Add EV station&quot; button. Then, find the location on the map where you want to place the EV station and click on it." loading="lazy"><figcaption>Click the newly created "Add EV station" button. Then, find the location on the map where you want to place the EV station and click on it.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-place-marker-2-ce.webp" alt="In the &quot;Add entity&quot; dialog that appears, make sure to enter a name for the new entity and select its type — Asset. The other fields are optional. Then click &quot;Create&quot;." loading="lazy"><figcaption>In the "Add entity" dialog that appears, make sure to enter a name for the new entity and select its type — Asset. The other fields are optional. Then click "Create".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-place-marker-3-ce.webp" alt="The new &quot;EV station&quot; marker is now added to the map." loading="lazy"><figcaption>The new "EV station" marker is now added to the map.</figcaption></figure></div>


Go to the "**Assets**" page — there you&#39;ll find your newly created asset, "**EV station 1**".


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/action-created-asset-1-ce.webp" alt="Go to the &quot;Assets&quot; page — there you&#39;ll find your newly created asset, &quot;EV station 1&quot;." loading="lazy"><figcaption>Go to the "Assets" page — there you&#39;ll find your newly created asset, "EV station 1".</figcaption></figure></div>
