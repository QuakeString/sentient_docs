+++
title = "Working with widgets"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/widgets.md"
+++
<div class="st-callout info">


Before proceeding with this guide, it&#39;s recommended that you follow [Getting Started](/docs/getting-started-guides/helloworld/) guide to become familiar with SENTIENT devices and dashboards. This will enhance your learning experience and understanding of the concepts presented here.


</div>


A **widget** is a dashboard element that displays a specific type of data or provides functionality.   
Widgets are used to:
- Visualize device data (telemetry and attributes)
- Remotely control devices (RPC)
- Work with alarms (create/view/acknowledge)
- Show static custom HTML content

### Widget types

SENTIENT provides five main widget types:

- **Time series widgets**. Show data over a selected time window. The window can be:
  - **Real time** — a rolling interval such as the last 5 minutes or last 24 hours.
  - **Historical** — a fixed, past interval.   

  *Example:* line, bar, or area chart widgets.   

  **Note**: Time series widgets are designed for telemetry (time series) rather than attributes.

- **Latest values widgets**. Display the most recent values of selected [attributes](/docs/user-guide/attributes/) or [telemetry](/docs/user-guide/telemetry/) keys.   
*Examples:* device model attribute, latest temperature reading.

- **Control widgets**. Send [RPC commands](/docs/user-guide/rpc/) to your devices.   
  *Example:* set a target temperature on a thermostat.

- **Alarm widgets**. Display and manage [alarms](/docs/user-guide/alarms/) and notifications.
- **Static widgets**. Present static content such as a floor plan or company information (including custom HTML).

Learn more about widget types [here](/docs/user-guide/ui/widget-library/).

## Adding a widget to the dashboard

To add a new widget to a dashboard, you should:


1. Open your dashboard and switch to <b>Edit mode</b>;

1. Click the <b>+ Add widget</b> at the top of the screen. If this is your first widget on the dashboard, you can also click <b>Add new widget</b> in the center of the screen to open the Widget bundle dialog;

1. Choose a <b>widget bundle</b> (for example, <b>Charts</b>). To quickly find your desired widget, use the search bar by clicking the magnifying glass icon and entering the widget&#39;s name;

1. Select a widget (for example, <b>Time series chart</b>) to open the <b>Add widget</b> dialog;

1. Specify the <b>data source</b>, add at least one <b>data key</b>, and click <b>Add</b>. Then <b>Apply changes</b>.

1. The widget is now created.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-1-ce.webp" alt="Open your dashboard and switch to Edit mode;" loading="lazy"><figcaption>Open your dashboard and switch to <b>Edit mode</b>;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-2-ce.webp" alt="Click the + Add widget at the top of the screen. If this is your first widget on the dashboard, you can also click Add new widget in the center of the screen to open the Widget bundle dialog;" loading="lazy"><figcaption>Click the <b>+ Add widget</b> at the top of the screen. If this is your first widget on the dashboard, you can also click <b>Add new widget</b> in the center of the screen to open the Widget bundle dialog;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-3-ce.webp" alt="Choose a widget bundle (for example, Charts). To quickly find your desired widget, use the search bar by clicking the magnifying glass icon and entering the widget&#39;s name;" loading="lazy"><figcaption>Choose a <b>widget bundle</b> (for example, <b>Charts</b>). To quickly find your desired widget, use the search bar by clicking the magnifying glass icon and entering the widget&#39;s name;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-4-ce.webp" alt="Select a widget (for example, Time series chart) to open the Add widget dialog;" loading="lazy"><figcaption>Select a widget (for example, <b>Time series chart</b>) to open the <b>Add widget</b> dialog;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-5-ce.webp" alt="Specify the data source, add at least one data key, and click Add. Then Apply changes." loading="lazy"><figcaption>Specify the <b>data source</b>, add at least one <b>data key</b>, and click <b>Add</b>. Then <b>Apply changes</b>.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-6-ce.webp" alt="The widget is now created." loading="lazy"><figcaption>The widget is now created.</figcaption></figure></div>


## Widget settings

Widget configuration includes setting up one or more [data sources](#data-source-types) (some widgets may have none), as well as configuring **appearance**, **widget card parameters**, **actions**, and **layout**.

When creating a widget, you can switch between **Basic** and **Advanced** modes using the toggle in the top‑right corner of the widget dialog.

<br><b><font size="4">Basic mode</font></b>

Use **Basic** mode for a quick start with a single data source and no extra filters. You’ll configure:

- the [time window](#widget-time-window) (or inherit it from the dashboard),
- the data source ([entity alias](/docs/user-guide/ui/aliases/) or specific [device](/docs/user-guide/ui/devices/)),
- a minimal set of appearance options that depend on the widget type.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/add-widget-basic-mode-1-ce.webp" alt="If you are using basic features to create a widget, you need to select the datasource type (device or entity alias) and add the series key. Then click &quot;Add&quot;." loading="lazy"><figcaption>If you are using basic features to create a widget, you need to select the datasource type (device or entity alias) and add the series key. Then click "Add".</figcaption></figure></div>


<br><b><font size="4">Advanced mode</font></b>

**Advanced** mode supports multiple data sources (when supported by the widget), [filtering](#filters), and five configuration tabs for fine‑grained control: [Data](#data-settings), [Appearance](#appearance), [Widget card](#widget-card), [Actions](#widget-actions), and [Layout](#layout-settings).

Additional data source types are available in Advanced mode (widget‑dependent): [Function](#function-as-datasource), [Entities count](#entities-count), and [Alarms count](#alarms-count).


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/add-widget-advanced-mode-1-ce.webp" alt="Using advanced functionality to create a widget, you need to select multiple datasources (if supported by the widget) and apply filters. Then click &quot;Add&quot;." loading="lazy"><figcaption>Using advanced functionality to create a widget, you need to select multiple datasources (if supported by the widget) and apply filters. Then click "Add".</figcaption></figure></div>


### Data settings

#### Widget time window

The widget&#39;s **time window** defines the time interval and aggregation function used to fetch telemetry or alarm data. 

By default, each widget uses its **own** time window. You can instead use the **dashboard time window** by enabling the corresponding option.

To hide the time-window selector from end users for this widget, turn off the **Display time window** option.

Learn more in the [time window guide](/docs/user-guide/dashboards/#time-window).


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/time-window-1-ce.webp" alt="By default, every widget uses the main time window determined in the dashboard&#39;s toolbar." loading="lazy"><figcaption>By default, every widget uses the main time window determined in the dashboard&#39;s toolbar.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/time-window-2-ce.webp" alt="Toggle the &quot;Use widget time window&quot; checkbox to overwrite the default time window." loading="lazy"><figcaption>Toggle the "Use widget time window" checkbox to overwrite the default time window.</figcaption></figure></div>


#### Data source types

Widget data settings let you add one or multiple data sources.

The data source combines a data source type, [an optional filter](#filters), and a list of data keys ([attributes](/docs/user-guide/attributes/) / [telemetry](/docs/user-guide/telemetry/)).
It defines which specific entity (or entities) the widget will pull data from to display.

**Available types:**
- [Device](#device-as-datasource) — read data from a single, specific device.
- [Entity](#entity-as-datasource) — read data from entities resolved by [an entity alias](/docs/user-guide/dashboards/#entity-aliases) and optional filters.
- [Function](#function-as-datasource) — generate data (e.g., random) to preview a widget without live telemetry.
- [Entities count](#entities-count) — show how many entities match an alias/filter.
- [Alarms count](#alarms-count) — show how many alarms match selected filters.

<hr>

##### Device as datasource

Use this to fetch telemetry from one device.

**Example:** Suppose you have a device that publishes indoor temperature values, and you want to show this data in a widget. Let&#39;s visualize it with the **Thermometer scale** widget.


1. Open your dashboard and enter edit mode. Then click the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the "Widgets bundle” dialog window;

1. Select "Analogue gauge" widget bundle;

1. Then select a "Thermometer scale" widget;

1. The "Add Widget" dialog window will open. Select data source type - "Device" and select your device. Then add data key - "temperature". Click "Add" and save all changes;

1. Thermometer scale widget is created.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-device-1-ce.webp" alt="Open your dashboard and enter edit mode. Then click the &quot;+ Add widget&quot; icon at the top of the screen, or (if this is your first widget on this dashboard) click a large &quot;Add new widget&quot; sign in the middle of the screen to open the &quot;Widgets bundle” dialog window;" loading="lazy"><figcaption>Open your dashboard and enter edit mode. Then click the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the "Widgets bundle” dialog window;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-device-2-ce.webp" alt="Select &quot;Analogue gauge&quot; widget bundle;" loading="lazy"><figcaption>Select "Analogue gauge" widget bundle;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-device-3-ce.webp" alt="Then select a &quot;Thermometer scale&quot; widget;" loading="lazy"><figcaption>Then select a "Thermometer scale" widget;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-device-4-ce.webp" alt="The &quot;Add Widget&quot; dialog window will open. Select data source type - &quot;Device&quot; and select your device. Then add data key - &quot;temperature&quot;. Click &quot;Add&quot; and save all changes;" loading="lazy"><figcaption>The "Add Widget" dialog window will open. Select data source type - "Device" and select your device. Then add data key - "temperature". Click "Add" and save all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-device-5-ce.webp" alt="Thermometer scale widget is created." loading="lazy"><figcaption>Thermometer scale widget is created.</figcaption></figure></div>


<hr>

##### Entity as datasource

Use this to fetch data from entities resolved by an [entity alias](/docs/user-guide/ui/aliases/) (for example: all devices, devices by type, assets in a group, etc.).

**Example:** list all devices in an [Entities table](/docs/user-guide/ui/entity-table-widget/).


1. Open your dashboard and enter edit mode. Then click the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the "Widgets bundle” dialog window;

1. Select "Tables" widget bundle;

1. Then select an "Entities table" widget;

1. The "Add Widget" dialog window will open. Select data source type - "Entity". Now, we need to create a new entity alias. Click "Create new" button in the entity alias row;

1. In the opened Add alias dialog, enter an alias name, select filter type - "Entity type", and choose an entity type - "Device". Click "Add";

1. Add data keys. Then click "Add" and save all changes;

1. A widget has been added that displays all devices using an entity alias as the datasource.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-device-1-ce.webp" alt="Open your dashboard and enter edit mode. Then click the &quot;+ Add widget&quot; icon at the top of the screen, or (if this is your first widget on this dashboard) click a large &quot;Add new widget&quot; sign in the middle of the screen to open the &quot;Widgets bundle” dialog window;" loading="lazy"><figcaption>Open your dashboard and enter edit mode. Then click the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the "Widgets bundle” dialog window;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entity-2-ce.webp" alt="Select &quot;Tables&quot; widget bundle;" loading="lazy"><figcaption>Select "Tables" widget bundle;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entity-3-ce.webp" alt="Then select an &quot;Entities table&quot; widget;" loading="lazy"><figcaption>Then select an "Entities table" widget;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entity-4-ce.webp" alt="The &quot;Add Widget&quot; dialog window will open. Select data source type - &quot;Entity&quot;. Now, we need to create a new entity alias. Click &quot;Create new&quot; button in the entity alias row;" loading="lazy"><figcaption>The "Add Widget" dialog window will open. Select data source type - "Entity". Now, we need to create a new entity alias. Click "Create new" button in the entity alias row;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entity-5-ce.webp" alt="In the opened Add alias dialog, enter an alias name, select filter type - &quot;Entity type&quot;, and choose an entity type - &quot;Device&quot;. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the opened Add alias dialog, enter an alias name, select filter type - "Entity type", and choose an entity type - "Device". Click "Add";</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entity-6-ce.webp" alt="Add data keys. Then click &quot;Add&quot; and save all changes;" loading="lazy"><figcaption>Add data keys. Then click "Add" and save all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entity-7-ce.webp" alt="A widget has been added that displays all devices using an entity alias as the datasource." loading="lazy"><figcaption>A widget has been added that displays all devices using an entity alias as the datasource.</figcaption></figure></div>


<hr>

##### Function as datasource

Use this when you don&#39;t have any data but want to test the widget&#39;s visualization.

**Example:** showing a random value on a **Value card**.


1. Open your dashboard and enter edit mode. Then click the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the "Widgets bundle” dialog window;

1. Select a "Cards" widget bundle;

1. Then select a "Value card" widget;

1. The "Add Widget" dialog window will open. Navigate to the advanced functionality and select data source type - "Random". Then add a function - "Random" and click the "pencil" icon of the "Random" key to open data key configuration window;

1. Change the label name to "temperature" and specify units. Click "Save";

1. Click "Add" and save all changes;

1. Created the value card widget which displays random value.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-device-1-ce.webp" alt="Open your dashboard and enter edit mode. Then click the &quot;+ Add widget&quot; icon at the top of the screen, or (if this is your first widget on this dashboard) click a large &quot;Add new widget&quot; sign in the middle of the screen to open the &quot;Widgets bundle” dialog window;" loading="lazy"><figcaption>Open your dashboard and enter edit mode. Then click the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the "Widgets bundle” dialog window;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-2-ce.webp" alt="Select a &quot;Cards&quot; widget bundle;" loading="lazy"><figcaption>Select a "Cards" widget bundle;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-random-3-ce.webp" alt="Then select a &quot;Value card&quot; widget;" loading="lazy"><figcaption>Then select a "Value card" widget;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-random-4-ce.webp" alt="The &quot;Add Widget&quot; dialog window will open. Navigate to the advanced functionality and select data source type - &quot;Random&quot;. Then add a function - &quot;Random&quot; and click the &quot;pencil&quot; icon of the &quot;Random&quot; key to open data key configuration window;" loading="lazy"><figcaption>The "Add Widget" dialog window will open. Navigate to the advanced functionality and select data source type - "Random". Then add a function - "Random" and click the "pencil" icon of the "Random" key to open data key configuration window;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-random-5-ce.webp" alt="Change the label name to &quot;temperature&quot; and specify units. Click &quot;Save&quot;;" loading="lazy"><figcaption>Change the label name to "temperature" and specify units. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-random-6-ce.webp" alt="Click &quot;Add&quot; and save all changes;" loading="lazy"><figcaption>Click "Add" and save all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-random-7-ce.webp" alt="Created the value card widget which displays random value." loading="lazy"><figcaption>Created the value card widget which displays random value.</figcaption></figure></div>


<hr>

##### Entities count

Shows the number of entities that match an alias/filter (e.g., total devices).

**Example:** display total device count on a **Value card**.


1. Open your dashboard and enter edit mode. Then click the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the "Widgets bundle” dialog window;

1. Select a "Cards" widget bundle;

1. Then select a "Value card" widget;

1. The "Add Widget" dialog window will open. Go to the advanced functionality and select data source type - "Entities count". Now, we need create new entity alias. Click "Create new" button in the entity alias row;

1. In the opened Add alias dialog, enter an alias name, select filter type - "Entity type", and choose an entity type - "Device". Click "Add";

1. In the Data key row click the "pencil" icon of the "count" key to open data key configuration window;

1. Change label name to "Devices count" and specify units. Click "Save";

1. Finally, click "Add" and save all changes;

1. Now we have a widget that displays the number of existing devices.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-device-1-ce.webp" alt="Open your dashboard and enter edit mode. Then click the &quot;+ Add widget&quot; icon at the top of the screen, or (if this is your first widget on this dashboard) click a large &quot;Add new widget&quot; sign in the middle of the screen to open the &quot;Widgets bundle” dialog window;" loading="lazy"><figcaption>Open your dashboard and enter edit mode. Then click the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the "Widgets bundle” dialog window;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-2-ce.webp" alt="Select a &quot;Cards&quot; widget bundle;" loading="lazy"><figcaption>Select a "Cards" widget bundle;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-3-ce.webp" alt="Then select a &quot;Value card&quot; widget;" loading="lazy"><figcaption>Then select a "Value card" widget;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-4-ce.webp" alt="The &quot;Add Widget&quot; dialog window will open. Go to the advanced functionality and select data source type - &quot;Entities count&quot;. Now, we need create new entity alias. Click &quot;Create new&quot; button in the entity alias row;" loading="lazy"><figcaption>The "Add Widget" dialog window will open. Go to the advanced functionality and select data source type - "Entities count". Now, we need create new entity alias. Click "Create new" button in the entity alias row;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-5-ce.webp" alt="In the opened Add alias dialog, enter an alias name, select filter type - &quot;Entity type&quot;, and choose an entity type - &quot;Device&quot;. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the opened Add alias dialog, enter an alias name, select filter type - "Entity type", and choose an entity type - "Device". Click "Add";</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-6-ce.webp" alt="In the Data key row click the &quot;pencil&quot; icon of the &quot;count&quot; key to open data key configuration window;" loading="lazy"><figcaption>In the Data key row click the "pencil" icon of the "count" key to open data key configuration window;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-7-ce.webp" alt="Change label name to &quot;Devices count&quot; and specify units. Click &quot;Save&quot;;" loading="lazy"><figcaption>Change label name to "Devices count" and specify units. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-8-ce.webp" alt="Finally, click &quot;Add&quot; and save all changes;" loading="lazy"><figcaption>Finally, click "Add" and save all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-9-ce.webp" alt="Now we have a widget that displays the number of existing devices." loading="lazy"><figcaption>Now we have a widget that displays the number of existing devices.</figcaption></figure></div>


<hr>

##### Alarms count

Shows the number of alarms that match the selected alias/filter (e.g., all device alarms, severity, status).

**Example:** display total alarms on a **Value card**.


1. Open your dashboard and enter edit mode. Then click the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the "Widgets bundle” dialog window;

1. Select "Cards" widget bundle;

1. Then select a "Value card" widget;

1. The "Add Widget" dialog window will open. Go to the advanced functionality, select data source type - "Alarms count" and specify filters. In the Data key row click the "pencil" icon of the "count" key to open data key configuration window;

1. Change label name to "Alarms count" and specify units. Click "Save";

1. Finally, click "Add" and apply changes;

1. Now we have a widget that displays all alarms of existing devices.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-device-1-ce.webp" alt="Open your dashboard and enter edit mode. Then click the &quot;+ Add widget&quot; icon at the top of the screen, or (if this is your first widget on this dashboard) click a large &quot;Add new widget&quot; sign in the middle of the screen to open the &quot;Widgets bundle” dialog window;" loading="lazy"><figcaption>Open your dashboard and enter edit mode. Then click the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the "Widgets bundle” dialog window;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-2-ce.webp" alt="Select &quot;Cards&quot; widget bundle;" loading="lazy"><figcaption>Select "Cards" widget bundle;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-entities-count-3-ce.webp" alt="Then select a &quot;Value card&quot; widget;" loading="lazy"><figcaption>Then select a "Value card" widget;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-alarms-count-4-ce.webp" alt="The &quot;Add Widget&quot; dialog window will open. Go to the advanced functionality, select data source type - &quot;Alarms count&quot; and specify filters. In the Data key row click the &quot;pencil&quot; icon of the &quot;count&quot; key to open data key configuration window;" loading="lazy"><figcaption>The "Add Widget" dialog window will open. Go to the advanced functionality, select data source type - "Alarms count" and specify filters. In the Data key row click the "pencil" icon of the "count" key to open data key configuration window;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-alarms-count-5-ce.webp" alt="Change label name to &quot;Alarms count&quot; and specify units. Click &quot;Save&quot;;" loading="lazy"><figcaption>Change label name to "Alarms count" and specify units. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-alarms-count-6-ce.webp" alt="Finally, click &quot;Add&quot; and apply changes;" loading="lazy"><figcaption>Finally, click "Add" and apply changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-alarms-count-7-ce.webp" alt="Now we have a widget that displays all alarms of existing devices." loading="lazy"><figcaption>Now we have a widget that displays all alarms of existing devices.</figcaption></figure></div>


<hr>

#### Data keys

A data key identifies the telemetry, attribute, or entity field a widget should use.

<b><font size="3">Sources of keys</font></b>
- **Attributes** — the combined set of Client, Server, and Shared [attributes](/docs/user-guide/attributes/) of the selected entity. If a needed attribute doesn&#39;t exist yet, you can still add the key; the widget will show data once the device reports it.
- **Time series** — telemetry keys reported by devices or written by the [Rule Engine](/docs/user-guide/rule-engine-2-0/overview/) / [REST API](/docs/reference/rest-api/).
- **Entity fields** — metadata fields that depend on entity type and may evolve over time (e.g. created time, entity type, name, type, label).

The data keys list for data source depends on the [widget type](/docs/user-guide/widgets/#widget-types):
- **Timeseries widgets** allow choosing time series data keys. Additionally, you can configure [time window](/docs/user-guide/widgets/#widget-time-window);
- **Latest values widgets** allow choosing time series, attributes and entity fields;
- **Static and Control widgets** do not require a data key;
- **Alarm widgets** allow choosing all data keys: time series, attributes, entity and alarm fields.
  Additionally, you can configure [time window](#widget-time-window) and [alarm filter](#alarm-filter).

<b><font size="3">Adding keys</font></b>

Click the **Data keys** row and select a key from the dropdown. If a key is not yet present in the database, type its name and select the type (**Attribute**, **Entity field**, or **Time series**). The widget will display values once they become available.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/add-data-key-1-ce.webp" alt="To add a key to the data source, click on the data keys row and select the desired key from the dropdown menu." loading="lazy"><figcaption>To add a key to the data source, click on the data keys row and select the desired key from the dropdown menu.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/add-key-in-the-future-1-ce.webp" alt="If a key is not yet present in the database, type its name and select the type (Attribute, Entity field, or Time series). The widget will display values once they become available." loading="lazy"><figcaption>If a key is not yet present in the database, type its name and select the type (Attribute, Entity field, or Time series). The widget will display values once they become available.</figcaption></figure></div>


<b><font size="3">Configuring data keys</font></b>

Data keys can be configured in two modes:

- **General** — common options shown in **Basic mode** and during widget creation.
- **Advanced** — full per‑key controls; open by clicking the **pencil** icon next to a key in **Advanced** widget settings.

<b><font size="3">Basic options (vary by widget)</font></b>

In **Basic** mode, these settings appear in the **Add widget** dialog.
- **Key** — specify the key to show its data).
- **Label** — the human‑readable name shown in the widget (e.g., table column header or legend item).
- **Units** — a symbol or unit shown next to values.   
  **Note:** Starting with SENTIENT 4.1, widgets support automatic data conversion and [unit switching](/docs/user-guide/ui/unit-conversion/) based on the selected unit system.
- **Decimals** — number of digits after the decimal point.
- **Color** — used by many chart widgets for series styling.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/edit-basic-key-configuration-key-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<b><font size="3">Advanced options</font></b>

In **Advanced** mode, open settings via the key&#39;s **pencil** icon.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/edit-key-configuration-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Let&#39;s look at the basic data key settings an example of the "Entities table" widget from the "Tables" bundle:

- **Key.** You can change the name of the key. In this case, will be displayed data of the key, which key name you specify in the "Key" line. Change the name of the key and click “Save”.


<div class="st-callout info">


**Please note:** There are four types of keys: Attributes, Time Series, Entity Field and Alarm Field (only for Alarm widget). To correctly display data, change the key name to the existing key name of the same type. If you don’t have the required time series or attribute key in the database yet, you can still add a key to the data source. The widget will start displaying the data as soon as the device will send it to SENTIENT.


</div>


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-key-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-key-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-key-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-key-4-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Label.** In your widget, the name of the data column is the label name. Change the label name as desired and click “Save” in the lower right corner of the dialog window.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-label-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-label-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-label-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-label-4-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Units.** You can indicate a special symbol that will be displayed next to the value. Enter the desired character in the units field and click "Save".


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-special-symbol-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-special-symbol-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


> Starting from SENTIENT 4.1, widgets also support automatic data conversion and unit switching based on the selected unit system. Learn more about this [here](/docs/user-guide/ui/unit-conversion/).

- **Decimals.** Specify the desired number of digits to be displayed after floating-point number and click “Save”.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-decimals-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-decimals-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Color.** Each key is assigned a different color. In some widgets (for example, Chart), the color of the graph line displayed in the widget is the color of the key. You can change color of the key. Click on the colored circle, select the desired label color and press “Select”.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-color-1-ce.webp" alt="Click on the colored icon of the data key;" loading="lazy"><figcaption>Click on the colored icon of the data key;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-color-2-ce.webp" alt="Select the desired label color and press &quot;Select&quot;;" loading="lazy"><figcaption>Select the desired label color and press "Select";</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-color-3-ce.webp" alt="The label color is changed. Save all changes;" loading="lazy"><figcaption>The label color is changed. Save all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-color-4-ce.webp" alt="The graph line color is changed;" loading="lazy"><figcaption>The graph line color is changed;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-color-5-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- [**Use data post-processing function**](#data-post-processing-function) — enable a custom function to transform raw values before display.

##### Aggregation of key

By default, the Latest values widgets do not have the time window. If you enable aggregation for any data
key in the **Latest values** widgets, the time window control will appear. You can set up aggregation for each telemetry
key individually, which you want to display and at the same time do not need to store it in the database. The time window
configuration is limited to the real-time intervals (**Current Hour/Day/Month**) and **History** time intervals. The real-time
intervals like **last 30 minutes** or **last 24 hours** are not supported for performance reasons. If you need to store the
aggregation as telemetry, follow for more details at [the link](https://sentient.invenia.in/docs/user-guide/rule-engine-2-0/nodes/analytics/).


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-aggregation-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-aggregation-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-aggregation-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


**Aggregation options:**

- **Min** or **Max**:
  <br>
  Selects the minimum or maximum value from the given interval. Using to detect peak negative or positive values.
  For example, power surges in the power cable, air pollution, equipment workload, etc.
  

<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-agg-max-0-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Average:**
  <br>
  Calculates the average from the selected interval (Summarizes, then divides by the count of telemetry from the selected interval).
  For example, you can use average aggregation for weekly fuel consumption, acoustical noise in dB, rotation fan speed, signal quality, etc.
  

<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-agg-avg-0-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Sum:**
  <br>
  Summarizes all telemetry for the specified period.
  Aggregation, for example, uses for different types of telemetry, mileage (km), water consumption, idle time, etc.
  

<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-agg-sum-0-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Count:**
  <br>
  Calculates the total number of transmitted messages for the selected period. It can be useful in setting up and
  optimizing devices running on battery power or when evaluating sensor activation sensitivity, etc.
  

<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-agg-count-0-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


  **Delta function:**

Allows you to calculate the delta between aggregated values for current and relative time window intervals.

  **Comparison period** - is a parameter that takes the history interval as a basis and converts it according to the selected option. List of options below.
- **Previous interval** (default) - set as a default option, when calculating, not only time is taken into account, but
  also the type of interval (**Current day** or **Current day so far**, etc.)
  <br>
  Example: **History** - **Current month so far** option, suppose is interval 1.09.22 to 25.09.22 then previous interval will be 1.08.22 to 25.08.22

  

<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-agg-max-delta-0-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Day ago** - from the start and end of the history interval, takes away 24 hours.
  <br>
  For example, with the amount of water spent **Current day** and **Delta** - **Day ago**:
  

<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-agg-sum-delta-dayago-0-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Week ago** - takes interval one week earlier from history interval (168 hours).
  <br>
  Example with average, history interval - **Current day**, and **Week ago** delta:
  

<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-agg-avg-delta-week-0-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Month ago** - The same interval (in days) as the history interval and subtracts from the current history interval.
  Example, if the current month is February (28 days) then **Month ago** would be the previous 28 days, not the entire previous month.
  <br>
  Example, with sum water, history - **Current day** and **Delta** - **Month ago**:

  

<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-agg-max-delta-monthago-0-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Year ago** - Interval that was 365 days ago from the current history interval.
  <br>If it is necessary to compare, suppose the aggregation for the previous month and the month of the past year.
  

<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-agg-max-delta-yearago-0-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- **Custom interval** - This option is for setting individual intervals. The maximum allowed value is limited to the **int** type. Example: 43200000 = 12 hours.

  

<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-agg-max-delta-custom-0-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


**Delta calculation result:**

This option allows you to specify how the result should be displayed:
<br>
- **Previous Value** - Displays aggregation value of compare interval (not current history interval).
- **Delta (absolute)** - Displays the difference between compared intervals, this option is set by default.
- **Delta (percent)** - Displays the result as a percentage relative to the previous interval <br>formula: **(IntervalValue - prevIntervalValue)/prevIntervalValue*100**

##### Data post-processing function
The data post-processing function enables real-time transformation of incoming telemetry values before they are displayed 
in widgets. This feature allows you to apply custom JavaScript logic to each data point — for example, convert units, 
filter out anomalies, or calculate derived metrics without touching upstream sources.

  **How to use:**
 - In the widget → go to section with **Data keys** → click the **Pencil** icon of the target data key.
 - Enable toggle **Use data post-processing function**.
 - Enter your code in the function body. The platform automatically injects the function header:
<br>     **function** (time, value, prevValue, timePrev, prevOrigValue) {
<br>        **`YOUR_JS_CODE`**
<br>     }
 - Click **Save** button.

**Once enabled, the function has access to the following parameters:**

- **time** – timestamp of the current value,
- **value** – the current value,
- **prevValue** – value returned by the previous function call,
- **timePrev** – timestamp of the previous value,
- **prevOrigValue** – original previous value.

The function must **return** a value (**number**|**string**|**boolean**|**null**).
Returning **null** excludes the data point from visualization.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-key-configuration-settings-post-processing-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


**Advanced data key settings**

Advanced data keys configuration is responsible for the visibility, style, and appearance of a specific data key column on the widget.
Entity table widget, alarms table widget, and entity admin widget bundles have the same advanced data key configuration.
Charts widget bundle has its own unique advanced data key configuration. All other widget bundles have only basic data key configuration.

Learn more about advanced data key settings [here](/docs/user-guide/ui/advanced-data-key-configuration/).

#### Filters

**Filters** let you narrow which data a widget retrieves from its data sources. Filters are built by adding keys and defining conditions on those keys. You can combine multiple keys and conditions.

**Key types:**

When adding a filter, choose one of the following key types:

- **Entity field**. A built‑in field on the entity (e.g., **device name**, **type**, **label**, **createdTime**, etc.). Useful for targeting entities by metadata rather than telemetry.
- **Attribute**. A generic attribute key when you don’t need to distinguish where the attribute is stored.
- **Client attribute**. Attributes set or reported by the device/edge client (typically via MQTT/HTTP/CoAP). Example: firmware **build** reported by the device at runtime.
- **Server attribute**. Attributes stored on the platform and usually configured by users or services. Example: **targetTemperature**, **threshold**.
- **Shared attribute**. Often used to deliver configuration from the server to devices (e.g., **displayUnits**).
- **Time series**. Telemetry keys that represent values over time (e.g., **temperature**, **humidity**, **voltage**). Best for conditions based on recent or historical readings.

**Operations**

Use operations to define how the key is compared to a value: **equal**, **not equal**, **greater than**, **less than**, **greater or equal**, **less or equal**.

For the comparison value, you can use a **fixed literal** or a **Dynamic source type**. Dynamic sources let the filter pull the value from context at runtime. This makes filters adaptable—for instance, "temperature **greater or equal** than **targetTemperature** (server attribute)" or "voltage **less than** the value the user selects in a **control widget**".


<div class="st-callout info">


**Tip:** Prefer **Dynamic source** for thresholds that may change, so you don’t have to edit filters whenever the value updates.


</div>


##### Alarm filter

Alarm widgets allow you to filter [alarms](/docs/user-guide/alarms/) based on [status](/docs/user-guide/alarms/#lifecycle), [severity](/docs/user-guide/alarms/#severity), and [type](/docs/user-guide/alarms/#type).
You can choose a combination of alarm statuses and severity. You may also define specific alarm types as well as enable search of [propagated](/docs/user-guide/alarms/#propagation) alarms.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/alarm-filters-2-ce.webp" alt="Filter alarms by status, severity and type." loading="lazy"><figcaption>Filter alarms by status, severity and type.</figcaption></figure></div>


### Appearance

Let&#39;s assume you have added the "Timeseries Line Chart" widget to display thermometers using the widget data configuration [step](/docs/user-guide/widgets/#data-settings) only.
You should see a similar widget (note that you should send/simulate some data to see the actual lines in the chart):

![image](/images/user-guide/widgets/overview/widget-example.webp)

Let&#39;s use the basic widget settings to customize the widget. We will demonstrate how each setting affects the widget.

#### Data settings

You can choose which symbol to display next to the value and the number of digits after the floating-point number.
These settings are useful if you want to apply the same settings for all axes.

- **Units by default**. If you are showing temperature readings for multiple devices, you can add symbol (e.g., °C or °F).
However, if you are displaying both temperature and humidity, you have to configure these data keys separately using data key settings.

- **Decimals by default**. Controls how many decimal places are displayed when a data key doesn&#39;t have its own formatting.
- **"No data to display" message**. An alternative message shown when the widget has no data in the selected time window or cannot render values (e.g., missing keys). Use it to provide helpful next steps.<br>
**Examples:**<br>
• "No data to display"<br>
• "No data for the selected time range"<br>
• "No telemetry received yet — check the device connection or time range".


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/default-data-settings-1-ce.webp" alt="You can choose which symbol to display next to the value and the number of digits after the floating-point number;" loading="lazy"><figcaption>You can choose which symbol to display next to the value and the number of digits after the floating-point number;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/default-data-settings-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### Common settings

**Stacking mode**

This option is relevant to the "Timeseries Bar Chart" widget.
The Stacking mode function displays the summed entity values to prevent overlap, with each value distinguished by a unique color. 
This function can be used only if the data aggregation function **is not** set to None.
Without activating the "Enable stacking mode", the bars will be split according to the values of the entities used. 
To view the values of all entities, you need to hover your mouse over the bar.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-stacking-mode-1-ce.webp" alt="In the upper right corner of the screen, click on the Time window configuration and choose any preferred Data aggregation function other than None. Click &quot;Update&quot; to apply changes;" loading="lazy"><figcaption>In the upper right corner of the screen, click on the Time window configuration and choose any preferred Data aggregation function other than None. Click "Update" to apply changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-stacking-mode-2-ce.webp" alt="In the widget settings, on the &quot;Appearance&quot; tab, toggle &quot;Enable stacking mode&quot; checkbox and apply changes;" loading="lazy"><figcaption>In the widget settings, on the "Appearance" tab, toggle "Enable stacking mode" checkbox and apply changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-stacking-mode-3-ce.webp" alt="To view the values of all entities, you need to hover your mouse over the bar." loading="lazy"><figcaption>To view the values of all entities, you need to hover your mouse over the bar.</figcaption></figure></div>


If you need to exclude a specific key from stacking, go to the [advanced data key configuration](/docs/user-guide/ui/advanced-data-key-configuration/#exclude-from-stacking), and check the "Exclude from stacking" checkbox.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-stacking-mode-4-ce.webp" alt="If you need to exclude a specific key from stacking, go to the advanced configuration of that data key;" loading="lazy"><figcaption>If you need to exclude a specific key from stacking, go to the advanced configuration of that data key;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-stacking-mode-5-ce.webp" alt="Check the &quot;Exclude from stacking&quot; checkbox. Apply changes." loading="lazy"><figcaption>Check the "Exclude from stacking" checkbox. Apply changes.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-stacking-mode-6-ce.webp" alt="Hover the mouse over a bar to see values of all entities." loading="lazy"><figcaption>Hover the mouse over a bar to see values of all entities.</figcaption></figure></div>


#### Legend settings

The <b>legend</b> displays statistical values including <b>minimum, maximum, average, total</b>, and <b>latest</b> values.

By default, the <b>show legend</b> option is enabled only for chart widgets. For other widgets, this option is disabled, but you can enable it by switching the <b>Legend</b> toggle in the widget settings.

In the legend settings, you can:
- Configure <b>font settings</b> and <b>colors</b> for labels, values, and column headers.
- Choose the <b>legend position</b>.
- Select which statistical values to display (<b>minimum, maximum, average, total, latest</b>).
- Enable <b>sorting of data keys</b> or keep them unsorted.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-legend-settings-1-ce.webp" alt="In the legend settings, you can:- Configure font settings and colors for labels, values, and column headers.- Choose the legend position.- Select which statistical values to display (minimum, maximum, average, total, latest).- Enable sorting of data keys or keep them unsorted." loading="lazy"><figcaption>In the legend settings, you can:<br>- Configure <b>font settings</b> and <b>colors</b> for labels, values, and column headers.<br>- Choose the <b>legend position</b>.<br>- Select which statistical values to display (<b>minimum, maximum, average, total, latest</b>).<br>- Enable <b>sorting of data keys</b> or keep them unsorted.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-legend-settings-2-ce.webp" alt="The legend displays statistical values including minimum, maximum, average, total, and latest values." loading="lazy"><figcaption>The <b>legend</b> displays statistical values including <b>minimum, maximum, average, total</b>, and <b>latest</b> values.</figcaption></figure></div>


The legend displays a label for each [data key](/docs/user-guide/widgets/#data-keys). When a widget contains data from multiple devices, or when several devices use the same data key name (for example, temperature), it may be difficult to determine which key value corresponds to which device in the legend or tooltip.

To make the legend clearer, you should use **${entityName}** or **${entityLabel}** in the **Label** field of the data key configuration.

- **${entityName}** – a variable that automatically inserts the system name of the entity in the legend. This helps clearly identify the object, especially when its technical name or unique identifier is important.   
  Example: If a device has the name **sensor-101**, then in the field where **${entityName}** is used, you will see **sensor-101**.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/entity-name-legend-1-ce.webp" alt="When a widget contains data from multiple devices, or when several devices use the same data key name, it may be difficult to determine which key value corresponds to which device in the legend or tooltip." loading="lazy"><figcaption>When a widget contains data from multiple devices, or when several devices use the same data key name, it may be difficult to determine which key value corresponds to which device in the legend or tooltip.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/entity-name-legend-2-ce.webp" alt="Open the data key configuration." loading="lazy"><figcaption>Open the data key configuration.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/entity-name-legend-3-ce.webp" alt="Use the ${entityName} variable in the key label, which automatically inserts the system name of the entity. This helps clearly identify the object, especially when its technical name or unique identifier is important." loading="lazy"><figcaption>Use the <b>${entityName}</b> variable in the key label, which automatically inserts the system name of the entity. This helps clearly identify the object, especially when its technical name or unique identifier is important.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/entity-name-legend-4-ce.webp" alt="Use this variable for other data keys as well." loading="lazy"><figcaption>Use this variable for other data keys as well.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/entity-name-legend-5-ce.webp" alt="Now, each key includes the name of the device it belongs to." loading="lazy"><figcaption>Now, each key includes the name of the device it belongs to.</figcaption></figure></div>


- **${entityLabel}** – a variable that inserts the entity's label in the legend. This is often used as a human-readable label and allows you to display a more descriptive name of the device or entity.   
   Example: A device has:
    - **Name** = **sensor-101**
    - **Label** = **Temperature Sensor, Warehouse #1**

    In the field where **${entityLabel}** is used, the operator will see the more understandable text: **Temperature Sensor, Warehouse #1**.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/entity-label-legend-1-ce.webp" alt="Use the ${entityLabel} variable in the key label, that inserts the entity&#39;s label in the legend or tooltip. This is often used as a human-readable label and allows you to display a more descriptive name of the device or entity." loading="lazy"><figcaption>Use the <b>${entityLabel}</b> variable in the key label, that inserts the entity&#39;s label in the legend or tooltip. This is often used as a human-readable label and allows you to display a more descriptive name of the device or entity.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/entity-label-legend-2-ce.webp" alt="Use this variable for other data keys as well." loading="lazy"><figcaption>Use this variable for other data keys as well.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/entity-label-legend-3-ce.webp" alt="Now, each key includes a human-readable label of the device it belongs to." loading="lazy"><figcaption>Now, each key includes a human-readable label of the device it belongs to.</figcaption></figure></div>


#### Axis settings

Configure the preferred axis parameters.

Specify the titles of the vertical and horizontal axes, and set the minimum and maximum scale values.

You can also set the ticks color, the number of decimal places, and step size between ticks.

**Vertical axis settings**:


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-vertical-axis-1-ce.webp" alt="Set the minimum and maximum scale values. Also, you can specify the vertical axis title, set the ticks color, decimals and step size between ticks of the vertical axis." loading="lazy"><figcaption>Set the minimum and maximum scale values. Also, you can specify the vertical axis title, set the ticks color, decimals and step size between ticks of the vertical axis.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-vertical-axis-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


**Horizontal axis settings**:


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-horizontal-axis-1-ce.webp" alt="You can specify the title of the horizontal axis and set the ticks color." loading="lazy"><figcaption>You can specify the title of the horizontal axis and set the ticks color.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-horizontal-axis-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


**Ticks formatter function, f(value)**

Let&#39;s say we have telemetry which takes values of very large numbers, especially when there is a special symbol near values. 
However, we need to build a small graph (since we don’t have a lot of free space on the dashboard). 
Therefore, using the ticks-formatter function, we can convert the ticks values to a more compact form.

```ruby
return value.toExponential(1) + " C";
```


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-ticks-formatter-function-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-ticks-formatter-function-2-ce.webp" alt="In the &quot;Appearance&quot; tab, in the Ticks formatter function field, enter the custom function and apply changes." loading="lazy"><figcaption>In the "Appearance" tab, in the Ticks formatter function field, enter the custom function and apply changes.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-ticks-formatter-function-3-ce.webp" alt="The function has been applied and values became more compact. By hovering the mouse over a widget you can see the tooltip with not reduced values." loading="lazy"><figcaption>The function has been applied and values became more compact. By hovering the mouse over a widget you can see the tooltip with not reduced values.</figcaption></figure></div>


#### Chart background settings

You can change the appearance of the chart grid: customize the color of the background, the grid frame and its ticks, and turn off lines visibility.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-chart-background-1-ce.webp" alt="Configure preferred grid settings and apply changes;" loading="lazy"><figcaption>Configure preferred grid settings and apply changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-chart-background-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### Tooltip settings

- **Hover individual points**. When the box "Hover individual points" is checked, you won&#39;t see value points on the lines.
- **Show cumulative values in stacking mode**. While stacking mode is on, you can check the box "Cumulative values" to enable your chart to display sum of all entity values.

Tooltip value format function, **f(value, latestData)** is used when you want to manually customize the tooltip.

To make the tooltip clearer, you should use **${entityName}** or **${entityLabel}** in the **Label** field of the data key configuration.

- **${entityName}** – a variable that automatically inserts the system name of the entity in the tooltip. This helps clearly identify the object, especially when its technical name or unique identifier is important.   
  Example: If a device has the name **Sensor 1**, then in the field where **${entityName}** is used, you will see **Sensor 1**.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/tooltipName-before-configuration-CE.webp" alt="When a widget contains data from multiple devices, or when several devices use the same data key name, it may be difficult to determine which key value corresponds to which device in the tooltip." loading="lazy"><figcaption>When a widget contains data from multiple devices, or when several devices use the same data key name, it may be difficult to determine which key value corresponds to which device in the tooltip.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/tooltipName-configuration-1-CE.webp" alt="Open the data key configuration." loading="lazy"><figcaption>Open the data key configuration.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/tooltipName-configuration-2-CE.webp" alt="Use the ${entityName} variable in the key label, which automatically inserts the system name of the entity. This helps clearly identify the object, especially when its technical name or unique identifier is important." loading="lazy"><figcaption>Use the <b>${entityName}</b> variable in the key label, which automatically inserts the system name of the entity. This helps clearly identify the object, especially when its technical name or unique identifier is important.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/tooltipName-configuration-3-CE.webp" alt="Use this variable for other data keys as well." loading="lazy"><figcaption>Use this variable for other data keys as well.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/tooltipName-after-configuration-CE.webp" alt="Now, each key includes the name of the device it belongs to." loading="lazy"><figcaption>Now, each key includes the name of the device it belongs to.</figcaption></figure></div>


- **${entityLabel}** – a variable that inserts the entity's label in the tooltip. This is often used as a human-readable label and allows you to display a more descriptive name of the device or entity.   
   Example: A device has:
    - **Name** = **Sensor 1**
    - **Label** = **Sensor 1 Label**

    In the field where **${entityLabel}** is used, the operator will see the more understandable text: **Sensor 1 Label**.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/tooltipLabel-configuration-1-CE.webp" alt="Use the ${entityLabel} variable in the key label, that inserts the entity&#39;s label in the tooltip. This is often used as a human-readable label and allows you to display a more descriptive name of the device or entity." loading="lazy"><figcaption>Use the <b>${entityLabel}</b> variable in the key label, that inserts the entity&#39;s label in the tooltip. This is often used as a human-readable label and allows you to display a more descriptive name of the device or entity.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/tooltipLabel-configuration-2-CE.webp" alt="Use this variable for other data keys as well." loading="lazy"><figcaption>Use this variable for other data keys as well.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/tooltipLabel-after-configuration-CE.webp" alt="Now, each key includes a human-readable label of the device it belongs to." loading="lazy"><figcaption>Now, each key includes a human-readable label of the device it belongs to.</figcaption></figure></div>


You can customize the values that will be displayed in the tooltip via tooltip settings or
[Advanced Data key configuration](/docs/user-guide/ui/advanced-data-key-configuration/#tooltip-settings).
Tooltip configuration via Settings is basic and applied to all entities at the same time. When configured in the Advanced Data key configuration,
it is applied only to the specific time series data, and the basic tooltip function will be overwritten by this configuration.

In State Chart, you can configure entity states to be shown on a tooltip depending on entity values.

Let&#39;s use the function to convert values from Celsius to Fahrenheit and display these values side by side:

```ruby
let celsiusValue = parseFloat(value).toFixed(2);
let farenheitValue = parseFloat(celsiusValue*1.8 + 32).toFixed(2);
return celsiusValue + ' °C (' + farenheitValue + ' °F)';
```


1. In the Tooltip value format function field, enter your tooltip function, then apply changes;

1. Hover with your mouse over the widget to see tooltip with applied value format function.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-tooltip-function-1-ce.webp" alt="In the Tooltip value format function field, enter your tooltip function, then apply changes;" loading="lazy"><figcaption>In the Tooltip value format function field, enter your tooltip function, then apply changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-tooltip-function-2-ce.webp" alt="Hover with your mouse over the widget to see tooltip with applied value format function." loading="lazy"><figcaption>Hover with your mouse over the widget to see tooltip with applied value format function.</figcaption></figure></div>


#### Comparison settings

You can show historical data with which to compare.


1. In the "Appearance" tab, toggle the "Enable comparison" checkbox and from the drop-down menu select time to show historical data with which to compare. In the "Comparison X axis settings" section, select axis position, where the compared axis will be located on the widget. Also, you can enter the axis title and show axis tick labels;

1. Navigate to the "Data" tab and click the “pencil” icon of a key in the data keys row;

1. In the data key configuration window, navigate to the "Advanced" tab and choose the comparison line color. When you are done with Comparison Settings configuration, then apply changes;

1. Since comparison settings work only in history time window mode, click "Edit time window" icon in the dashboard toolbar, go to the "History" tab, and select the time interval with which you want to compare the current data. Then click "Update" to apply;

1. Now you can compare the value for the current minute and the five minutes ago.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-comparison-1-ce.webp" alt="In the &quot;Appearance&quot; tab, toggle the &quot;Enable comparison&quot; checkbox and from the drop-down menu select time to show historical data with which to compare. In the &quot;Comparison X axis settings&quot; section, select axis position, where the compared axis will be located on the widget. Also, you can enter the axis title and show axis tick labels;" loading="lazy"><figcaption>In the "Appearance" tab, toggle the "Enable comparison" checkbox and from the drop-down menu select time to show historical data with which to compare. In the "Comparison X axis settings" section, select axis position, where the compared axis will be located on the widget. Also, you can enter the axis title and show axis tick labels;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-comparison-2-ce.webp" alt="Navigate to the &quot;Data&quot; tab and click the “pencil” icon of a key in the data keys row;" loading="lazy"><figcaption>Navigate to the "Data" tab and click the “pencil” icon of a key in the data keys row;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-comparison-3-ce.webp" alt="In the data key configuration window, navigate to the &quot;Advanced&quot; tab and choose the comparison line color. When you are done with Comparison Settings configuration, then apply changes;" loading="lazy"><figcaption>In the data key configuration window, navigate to the "Advanced" tab and choose the comparison line color. When you are done with Comparison Settings configuration, then apply changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-comparison-4-ce.webp" alt="Since comparison settings work only in history time window mode, click &quot;Edit time window&quot; icon in the dashboard toolbar, go to the &quot;History&quot; tab, and select the time interval with which you want to compare the current data. Then click &quot;Update&quot; to apply;" loading="lazy"><figcaption>Since comparison settings work only in history time window mode, click "Edit time window" icon in the dashboard toolbar, go to the "History" tab, and select the time interval with which you want to compare the current data. Then click "Update" to apply;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-comparison-5-ce.webp" alt="Now you can compare the value for the current minute and the five minutes ago." loading="lazy"><figcaption>Now you can compare the value for the current minute and the five minutes ago.</figcaption></figure></div>


#### Custom legend settings

Use Custom Legend Settings when you need to showcase data that isn&#39;t suitable for chart representation, such as specific attributes, or when you want to display only certain time series in the Chart legend. 
For instance, consider active/inactive attributes that can be displayed in a Table widget but not on a Chart.


1. Navigate to the "Appearance" tab. Activate the "Enable custom legend" option to use attribute or time series values as key labels. Click on "+ Add new key". In the drop-down menu that appears, input the key name and choose the key type;

1. Proceed to the "Data" tab. Click the pencil icon next to a data key to access the Data key configuration window;

1. In the label line, input the pattern ${} and place the data key name within the brackets. Click "Save" to set the new label name and apply all changes;

1. Now, when you view the widget, you&#39;ll see that the custom legend settings have been applied.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-custom-legend-settings-1-ce.webp" alt="Navigate to the &quot;Appearance&quot; tab. Activate the &quot;Enable custom legend&quot; option to use attribute or time series values as key labels. Click on &quot;+ Add new key&quot;. In the drop-down menu that appears, input the key name and choose the key type;" loading="lazy"><figcaption>Navigate to the "Appearance" tab. Activate the "Enable custom legend" option to use attribute or time series values as key labels. Click on "+ Add new key". In the drop-down menu that appears, input the key name and choose the key type;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-custom-legend-settings-2-ce.webp" alt="Proceed to the &quot;Data&quot; tab. Click the pencil icon next to a data key to access the Data key configuration window;" loading="lazy"><figcaption>Proceed to the "Data" tab. Click the pencil icon next to a data key to access the Data key configuration window;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-custom-legend-settings-3-ce.webp" alt="In the label line, input the pattern ${} and place the data key name within the brackets. Click &quot;Save&quot; to set the new label name and apply all changes;" loading="lazy"><figcaption>In the label line, input the pattern ${} and place the data key name within the brackets. Click "Save" to set the new label name and apply all changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/appearance/appearance-custom-legend-settings-4-ce.webp" alt="Now, when you view the widget, you&#39;ll see that the custom legend settings have been applied." loading="lazy"><figcaption>Now, when you view the widget, you&#39;ll see that the custom legend settings have been applied.</figcaption></figure></div>


### Widget card

#### Widget title settings

You can input custom widget title, tooltip and title style. You may also add an icon to the title and control icon color and size. See configuration and the corresponding result below.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/widget-card-title-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/widget-card-title-3-ce.webp" alt="Edit widget title settings and apply changes;" loading="lazy"><figcaption>Edit widget title settings and apply changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/widget-card-title-4-ce.webp" alt="The title style have been changed." loading="lazy"><figcaption>The title style have been changed.</figcaption></figure></div>


Title style from the screen above:

```json
{
  "fontSize": "15px",
  "fontWeight": 600
}
```


#### Widget style settings

You can customize personal  style for the widget using CSS properties. This style will be applied to the main div element of the widget.

You may also disable the widget shadow using the "Drop shadow" checkbox and disable fullscreen using the "Enable fullscreen" checkbox.
All those settings are enabled by default.

You can also change the background color, text color, padding, and margin.
See the configuration and the corresponding result below.

Please note that the style and background color are just an example and are definitely not part of our guidelines.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/widget-card-style-2-ce.webp" alt="Customize the widget style and apply changes;" loading="lazy"><figcaption>Customize the widget style and apply changes;</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/widget-card-style-3-ce.webp" alt="The widget style has been changed." loading="lazy"><figcaption>The widget style has been changed.</figcaption></figure></div>


Widget style from the screen above:

```json
{
  "border": "3px solid #2E86C1",
  "cursor": "pointer"
}
```


#### Widget buttons settings


**Enable fullscreen**

You may disable fullscreen using the "Enable fullscreen" checkbox. This setting is enabled by default.

All those settings are enabled by default.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-key-configuration-settings-enable-fullscreen-1-ce.webp" alt="By default, fullscreen is enabled." loading="lazy"><figcaption>By default, fullscreen is enabled.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-key-configuration-settings-enable-fullscreen-2-ce.webp" alt="To expand widget to fullscreen, click on the “Expand to fullscreen” icon at the top right of the widget." loading="lazy"><figcaption>To expand widget to fullscreen, click on the “Expand to fullscreen” icon at the top right of the widget.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/data-key-configuration-settings-enable-fullscreen-3-сe.webp" alt="You can disable the ability to expand widget to fullscreen." loading="lazy"><figcaption>You can disable the ability to expand widget to fullscreen.</figcaption></figure></div>


<hr>

### Widget actions

Actions allow quickly and easily configuring the transition to the created state, transferring to other dashboards, or even updating the dashboard you are in. Depending on the widget, the action sources differ.
However, the type of action you are able to choose will be the same for all widgets.
Actions are adjusted in the Edit mode of the needed widget.
To fully understand how to use Actions, you have to [add a State to your widget](/docs/user-guide/dashboards/#manage-dashboard-states).

Read more about [widget actions](/docs/user-guide/ui/widget-actions/) in the documentation dedicated to it.

### Layout settings

Use the **Layout** tab to control how the widget behaves inside the dashboard grid across desktop and mobile layouts.

<b><font size="3">Resize options</font></b>

- **Resizable**. Allows the widget to be resized by the user in Edit mode. When disabled, the widget keeps its current size and resize handles are hidden.
- **Preserve aspect ratio**. Keeps the widget&#39;s width‑to‑height ratio when it is resized. This helps charts and media avoid distortion across different screen sizes and grid breakpoints. If disabled, width and height can change independently.


<div class="st-callout info">


**Tip**: Enable **Preserve aspect ratio** for charts, images, and video; disable it for tables and lists where extra vertical space is useful.

</div>


<b><font size="3">Mobile</font></b>

These options control visibility and sizing in **mobile mode** (responsive layout):

- **Hide widget in mobile mode**. Do not render this widget when the dashboard is viewed on a mobile layout. Useful for large visualizations that don’t fit small screens.
- **Hide widget in desktop mode**. Render this widget only on mobile; hide it on desktop. Handy when you design a compact, mobile‑only alternative to a complex desktop widget.
- **Order**. Sets the widget&#39;s position relative to other widgets in the mobile layout. Lower numbers appear earlier (top‑left). Use integers (e.g., 1, 2, 3…).
- **Height**. Defines the widget’s height in the mobile grid (in grid rows). Increase the value to give lists and cards more space on phones; reduce it for small KPIs.

**Best practices:**
- Keep mobile **Order** consistent across related widgets to maintain reading flow.
- Test with real devices or the dashboard’s mobile preview to validate **Height** and scrolling behavior.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/widget-settings-mobile-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/widget-settings-mobile-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/widgets/overview/widget-settings-mobile-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Import and Export widget

### Import widget

You can import a widget from a **JSON** file.


1. Open your dashboard and switch to <b>Edit mode</b>. Click <b>+ Add widget</b>. The <b>Select widgets bundle</b> dialog opens.

1. Click <b>Import widget</b> in the top‑right corner.

1. In the import dialog, upload the <b>JSON</b> file and click <b>Import</b>.

1. The widget has been added to the dashboard. It may not show data yet because the data source needs to be updated.

1. Enter widget <b>edit mode</b>, specify the <b>data source</b>, add the required <b>data key(s)</b>, and <b>apply</b> changes.

1. Verify that the widget displays data (e.g., a temperature chart) and <b>Save</b> the dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/data-settings/data-source-type-device-1-ce.webp" alt="Open your dashboard and switch to Edit mode. Click + Add widget. The Select widgets bundle dialog opens." loading="lazy"><figcaption>Open your dashboard and switch to <b>Edit mode</b>. Click <b>+ Add widget</b>. The <b>Select widgets bundle</b> dialog opens.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/import-widget-2-ce.webp" alt="Click Import widget in the top‑right corner." loading="lazy"><figcaption>Click <b>Import widget</b> in the top‑right corner.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/import-widget-3-ce.webp" alt="In the import dialog, upload the JSON file and click Import." loading="lazy"><figcaption>In the import dialog, upload the <b>JSON</b> file and click <b>Import</b>.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/import-widget-4-ce.webp" alt="The widget has been added to the dashboard. It may not show data yet because the data source needs to be updated." loading="lazy"><figcaption>The widget has been added to the dashboard. It may not show data yet because the data source needs to be updated.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/import-widget-5-ce.webp" alt="Enter widget edit mode, specify the data source, add the required data key(s), and apply changes." loading="lazy"><figcaption>Enter widget <b>edit mode</b>, specify the <b>data source</b>, add the required <b>data key(s)</b>, and <b>apply</b> changes.</figcaption></figure><figure><img src="/images/user-guide/widgets/overview/import-widget-6-ce.webp" alt="Verify that the widget displays data (e.g., a temperature chart) and Save the dashboard." loading="lazy"><figcaption>Verify that the widget displays data (e.g., a temperature chart) and <b>Save</b> the dashboard.</figcaption></figure></div>


<div class="st-callout info">


**Tip:** If the imported widget uses entity aliases or keys that don&#39;t exist in your environment, map them during Edit widget.

</div>


### Export widget

Export saves a widget&#39;s configuration (as **JSON**) so you can reuse it elsewhere.

**Steps:**
- Open the dashboard containing the widget and switch to **Edit mode**.
- On the widget&#39;s top‑right toolbar, click **Export widget**.
- A **JSON** file with the widget configuration is downloaded to your computer.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/export-widget-1-ce.webp" alt="Open the dashboard containing the widget and switch to Edit mode. On the widget&#39;s top‑right toolbar, click Export widget. A JSON file with the widget configuration is downloaded to your computer." loading="lazy"><figcaption>Open the dashboard containing the widget and switch to <b>Edit mode</b>. On the widget&#39;s top‑right toolbar, click <b>Export widget</b>. A <b>JSON</b> file with the widget configuration is downloaded to your computer.</figcaption></figure></div>


<div class="st-callout info">


**Note:** Exports include widget settings but not data.


</div>


## Next steps
