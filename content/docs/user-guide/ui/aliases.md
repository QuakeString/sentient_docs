+++
title = "Aliases"
description = "SENTIENT Aliases"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/aliases.md"
+++
Alias is a reference to a single entity or group of entities that are used in the widgets. Alias may be static or dynamic.

They can range from a simple reference to a single device to a complex search query for specific assets from a list.

In this tutorial, aliases will be used in the system according to the scheme shown below. And all devices transmit telemetry values - "temperature".

![image](/images/user-guide/ui/alias/alias-scheme.webp)

## Prerequisites

Before proceeding with this guide, it's recommended that you follow [Getting Started](/docs/getting-started-guides/helloworld/) guide to become familiar with SENTIENT devices, dashboards and widgets. This will enhance your learning experience and understanding of the concepts presented here.

## Creating alias

To create an alias, you need to define the entities from which data will be extracted.

Then follow these steps:


1. Open your dashboard and switch to Edit mode;

1. Click the "Entity aliases" icon in the upper right corner of the window;

1. In the opened "Entity aliases" window click the “Add alias” button on the left side of the dialog box;

1. In the opened "Add alias" dialog, enter a name for the alias and select a filter type. Then, fill in all required fields and click the "Add" button in the lower right corner;

1. We can now see that a new alias has been added. In this window you can view, edit and delete your aliases. Click "Save" in the lower right corner of the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/overview/add-new-dashboard-1-ce.webp" alt="Open your dashboard and switch to Edit mode;" loading="lazy"><figcaption>Open your dashboard and switch to Edit mode;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/create-alias-2-ce.webp" alt="Click the &quot;Entity aliases&quot; icon in the upper right corner of the window;" loading="lazy"><figcaption>Click the "Entity aliases" icon in the upper right corner of the window;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/create-alias-3-ce.webp" alt="In the opened &quot;Entity aliases&quot; window click the “Add alias” button on the left side of the dialog box;" loading="lazy"><figcaption>In the opened "Entity aliases" window click the “Add alias” button on the left side of the dialog box;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/create-alias-4-ce.webp" alt="In the opened &quot;Add alias&quot; dialog, enter a name for the alias and select a filter type. Then, fill in all required fields and click the &quot;Add&quot; button in the lower right corner;" loading="lazy"><figcaption>In the opened "Add alias" dialog, enter a name for the alias and select a filter type. Then, fill in all required fields and click the "Add" button in the lower right corner;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/create-alias-5-ce.webp" alt="We can now see that a new alias has been added. In this window you can view, edit and delete your aliases. Click &quot;Save&quot; in the lower right corner of the dialog box." loading="lazy"><figcaption>We can now see that a new alias has been added. In this window you can view, edit and delete your aliases. Click "Save" in the lower right corner of the dialog box.</figcaption></figure></div>


Now, let’s use the added alias in a widget:


1. Click the "Add widget" button at the top of the screen or click the large "Add new widget" icon in the center of the screen (if this is your first widget on this dashboard);

1. Select the widget bundle. For example, select "Indoor Environment" widgets bundle;

1. Now, select the "Indoor temperature card with background" widget;

1. The "Add Widget" window will appear. Navigate to the "Entity alias" tab. Specify the previously created "A new entity alias" in the "Entity alias" field.

1. Specify the data key(s) in the "Data key" field. In our example is the "temperature" data key. Then, click "Add";

1. You have added a widget that uses the previously configured alias as a data source.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/create-alias-6-ce.webp" alt="Click the &quot;Add widget&quot; button at the top of the screen or click the large &quot;Add new widget&quot; icon in the center of the screen (if this is your first widget on this dashboard);" loading="lazy"><figcaption>Click the "Add widget" button at the top of the screen or click the large "Add new widget" icon in the center of the screen (if this is your first widget on this dashboard);</figcaption></figure><figure><img src="/images/user-guide/ui/alias/create-alias-7-ce.webp" alt="Select the widget bundle. For example, select &quot;Indoor Environment&quot; widgets bundle;" loading="lazy"><figcaption>Select the widget bundle. For example, select "Indoor Environment" widgets bundle;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/create-alias-8-ce.webp" alt="Now, select the &quot;Indoor temperature card with background&quot; widget;" loading="lazy"><figcaption>Now, select the "Indoor temperature card with background" widget;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/create-alias-9-ce.webp" alt="The &quot;Add Widget&quot; window will appear. Navigate to the &quot;Entity alias&quot; tab. Specify the previously created &quot;A new entity alias&quot; in the &quot;Entity alias&quot; field." loading="lazy"><figcaption>The "Add Widget" window will appear. Navigate to the "Entity alias" tab. Specify the previously created "A new entity alias" in the "Entity alias" field.</figcaption></figure><figure><img src="/images/user-guide/ui/alias/create-alias-10-ce.webp" alt="Specify the data key(s) in the &quot;Data key&quot; field. In our example is the &quot;temperature&quot; data key. Then, click &quot;Add&quot;;" loading="lazy"><figcaption>Specify the data key(s) in the "Data key" field. In our example is the "temperature" data key. Then, click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/create-alias-11-ce.webp" alt="You have added a widget that uses the previously configured alias as a data source." loading="lazy"><figcaption>You have added a widget that uses the previously configured alias as a data source.</figcaption></figure></div>


## Alias types


In the SENTIENT, there are various types of aliases, each offering different capabilities for configuring widgets: [Single entity](#single-entity), [Entity list](#entity-list), [Entity name](#entity-name), [Entity type](#entity-type), [Entity from dashboard state](#entity-from-dashboard-state), [Asset type](#asset-type), [Device type](#device-type), [Entity view type](#entity-view-type), [Edge type](#edge-type), [Api Usage State](#api-usage-state), [Relations query](#relations-query), [Asset search query](#asset-search-query), [Device search query](#device-search-query), [Entity view search query](#entity-view-search-query), and [Edge search query](#edge-search-query).


They provide flexibility and powerful capabilities for configuring dashboards in SENTIENT, allowing users to efficiently organize and visualize data from various sources.

Let's take a look at each of them.

### Single entity


This alias allows choosing a single entity. It can be a device, asset, entity view, tenant, customer, user, dashboard, edge, current customer, current tenant, current user or current user owner.


Adding an alias: in the "Add alias" dialog, enter the alias name, and select the "Single entity" filter type. Then choose the entity type and specify the final entity.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/single-entity-1-ce.webp" alt="In the &quot;Add Alias&quot; dialog box, enter the alias name, and select the &quot;Single Entity&quot; filter type. Then choose the entity type and specify the final entity/entities." loading="lazy"><figcaption>In the "Add Alias" dialog box, enter the alias name, and select the "Single Entity" filter type. Then choose the entity type and specify the final entity/entities.</figcaption></figure></div>


In this example, an alias has been created that filters one device - Thermometer A1. 

Let's use an added alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Single entity" alias in the "Entity alias" field and "temperature" data key in the "Columns" section. Click "Add" and apply changes. 
The Entities table widget with the alias that displays one device - Thermometer A1 has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/single-entity-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Single entity&quot; alias in the &quot;Entity alias&quot; field and &quot;temperature&quot; data key in the &quot;Columns&quot; section. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Single entity" alias in the "Entity alias" field and "temperature" data key in the "Columns" section. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/single-entity-3-ce.webp" alt="The Entities table widget with the alias that filters one device - Thermometer A1 has been added." loading="lazy"><figcaption>The Entities table widget with the alias that filters one device - Thermometer A1 has been added.</figcaption></figure></div>


### Entity list


This alias allows you to display multiple entities. It can be devices, assets, entity views, tenants, customers, dashboards, users or edges.


Adding an alias: in the "Add alias" dialog, enter the alias name, and select the "Entity list" filter type. Then choose the entities type and specify entities whose data you want to display on the widget.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-list-1-ce.webp" alt="In the &quot;Add alias&quot; dialog box, enter the alias name, and select the &quot;Entity list&quot; filter type. Then choose the entities type and select the entity group." loading="lazy"><figcaption>In the "Add alias" dialog box, enter the alias name, and select the "Entity list" filter type. Then choose the entities type and select the entity group.</figcaption></figure></div>


This alias filters a list from specified devices: Thermometer A1, Thermometer A2, and Thermometer A3.


Let's use an added alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Entity list" alias in the "Entity alias" field and "temperature" data key in the "Columns" section. Click "Add" and apply changes. 


The Entities table widget with the alias that displays a list of several devices, which in this case are Thermometer A1, Thermometer A2, and Thermometer A3 has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-list-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Entity list&quot; alias in the &quot;Entity alias&quot; field and &quot;temperature&quot; data key in the &quot;Columns&quot; section. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Entity list" alias in the "Entity alias" field and "temperature" data key in the "Columns" section. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-list-3-ce.webp" alt="The Entities table widget with the alias that displays a list of several devices, which in this case are Thermometer A1, Thermometer A2, and Thermometer A3 has been added." loading="lazy"><figcaption>The Entities table widget with the alias that displays a list of several devices, which in this case are Thermometer A1, Thermometer A2, and Thermometer A3 has been added.</figcaption></figure></div>


### Entity name


This alias allows you to display entities whose names start with the entered expression. These objects can be devices, assets, entity views, tenants, customers, users, dashboards or edges.


Adding an alias: in the "Add alias" dialog, enter the alias name, and select the "Entity name" filter type. Then choose the entities type and enter an expression that will filter the names of the displayed entities.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-name-1-ce.webp" alt="In the &quot;Add alias&quot; dialog box, enter the alias name, and select the &quot;Entity name&quot; filter type. Then choose the entities type and enter an expression that will filter the names of the displayed entities." loading="lazy"><figcaption>In the "Add alias" dialog box, enter the alias name, and select the "Entity name" filter type. Then choose the entities type and enter an expression that will filter the names of the displayed entities.</figcaption></figure></div>


This alias filters devices with names start with "Compressor". 

Let's use an added alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Entity name" alias in the "Entity alias" field and "temperature" data key in the "Columns" section. Click "Add" and apply changes. 
The Entities table widget with alias that filters devices, which names start with ‘Compressor’, has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-name-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Entity name&quot; alias in the &quot;Entity alias&quot; field and &quot;temperature&quot; data key in the &quot;Columns&quot; section. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Entity name" alias in the "Entity alias" field and "temperature" data key in the "Columns" section. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-name-3-ce.webp" alt="The Entities table widget with alias that filters devices, which names start with ‘Compressor’, has been added." loading="lazy"><figcaption>The Entities table widget with alias that filters devices, which names start with ‘Compressor’, has been added.</figcaption></figure></div>


### Entity type


This alias allows you to display all your entities and your customers' entities of the specified type. These objects can be devices, assets, entity views, tenants, customers, users, dashboards or edges.


Adding an alias: in the "Add Alias" dialog, enter the alias name, select the filter as "Entity Type", and choose the entity type.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-type-1-ce.webp" alt="In the &quot;Add alias&quot; dialog box, enter the alias name, select the &quot;Entity type &quot; filter type, and choose the entity type - &quot;Device&quot;. Then, click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Add alias" dialog box, enter the alias name, select the "Entity type " filter type, and choose the entity type - "Device". Then, click "Add";</figcaption></figure></div>


This alias displays all your and your customers' devices. 

Let's use an added alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Entity type" alias in the "Entity alias" field and "temperature" data key in the "Columns" section. Click "Add" and apply changes. 
The Entities table widget displaying all your devices and your customers' devices has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-type-2-ce.webp" alt="Add an Entity table widget that will display a list of entities. Use the &quot;Entity type&quot; alias as a data source;" loading="lazy"><figcaption>Add an Entity table widget that will display a list of entities. Use the "Entity type" alias as a data source;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-type-3-ce.webp" alt="The Entity table widget that displays a list of devices has been added." loading="lazy"><figcaption>The Entity table widget that displays a list of devices has been added.</figcaption></figure></div>


### Entity from dashboard state


This alias allows choosing one or more entities from the dashboard state. The entities can be a device, asset, entity view, tenant, customer, user, dashboard, edge, current customer, current tenant, current user, or current user owner.


For example, if Entities table widget is created on a [root dashboard state](/docs/user-guide/dashboards/#states) with several entities displayed on it, and you'd like to create a dashboard state which will display a widget with the entity you clicked on, you need to use this alias.

Adding an alias: in the "Add alias" dialog, enter the alias name, and select the filter type "Entity from dashboard state". Then click "Add".


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-2-ce.webp" alt="To add this alias, enter the alias name, and select the filter type &quot;Entity from dashboard state&quot; in the &quot;Add alias&quot; dialog. Then click &quot;Add&quot;." loading="lazy"><figcaption>To add this alias, enter the alias name, and select the filter type "Entity from dashboard state" in the "Add alias" dialog. Then click "Add".</figcaption></figure></div>


This alias is used for filtering data for other dashboard states.


For the next example, we will need two aliases: the previously discussed "[Entity type](#entity-type)" alias and the "Entity from dashboard state" alias. Let's start:

First we need to create an Entity table widget that will display a list of entities: add an Entities table widget that will display a list of entities. Use the "Entity type" alias as a data source.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-3-ce.webp" alt="In the &quot;Add alias&quot; dialog box, enter the alias name, select the &quot;Entity type&quot; filter type and choose the entity type;" loading="lazy"><figcaption>In the "Add alias" dialog box, enter the alias name, select the "Entity type" filter type and choose the entity type;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-4-ce.webp" alt="Add an Entity table widget that will display a list of entities. Use the &quot;Entity type&quot; alias as a data source;" loading="lazy"><figcaption>Add an Entity table widget that will display a list of entities. Use the "Entity type" alias as a data source;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-5-ce.webp" alt="The Entity table widget that will display a list of devices has been added." loading="lazy"><figcaption>The Entity table widget that will display a list of devices has been added.</figcaption></figure></div>


After adding the Entities table widget, add a new a [state](/docs/user-guide/dashboards/#states):


1. Click the layers icon in the top left corner of the dashboard to create a new state. In the opened dialog window, click a "+" icon to add a new state;

1. Enter state&#39;s name. For the state to be named after the entity, use <b>${entityName}</b> as the name of the state. Thus, during the action, you will be transitioned to a state named after the entity that took part in the action. Click "Add";

1. Now you see a list with two states: the root one, and the one that has just been created. Click "Save" in the lower right corner of the dialog.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-6-ce.webp" alt="Click the layers icon in the top left corner of the dashboard to create a new state. In the opened dialog window, click a &quot;+&quot; icon to add a new state;" loading="lazy"><figcaption>Click the layers icon in the top left corner of the dashboard to create a new state. In the opened dialog window, click a "+" icon to add a new state;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-7-ce.webp" alt="Enter state&#39;s name. For the state to be named after the entity, use ${entityName} as the name of the state. Thus, during the action, you will be transitioned to a state named after the entity that took part in the action. Click &quot;Add&quot;;" loading="lazy"><figcaption>Enter state&#39;s name. For the state to be named after the entity, use <b>${entityName}</b> as the name of the state. Thus, during the action, you will be transitioned to a state named after the entity that took part in the action. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-8-ce.webp" alt="Now you see a list with two states: the root one, and the one that has just been created. Click &quot;Save&quot; in the lower right corner of the dialog." loading="lazy"><figcaption>Now you see a list with two states: the root one, and the one that has just been created. Click "Save" in the lower right corner of the dialog.</figcaption></figure></div>


Time to add an [action](/docs/user-guide/ui/widget-actions) to a root dashboard widget and execute it using an Entity from dashboard state alias on the widget in the created state:


1. In the root dashboard state, enter widget Edit mode by clicking the “pencil” icon in the upper right corner;

1. Scroll down to find "Actions" section. Click "Add action" button;

1. The "Entities table: Actions" window will be opened. Click the "Add action" button in the top right corner;

1. In the "Add action" dialog, enter the action name, and select an action source responsible for each entity separately (action cell button, on row click etc.). Then, choose the action type "Navigate to new dashboard state" and specify the new dashboard state to which the transition will be made. After, click "Add";

1. After successfully adding the action, click the "Save" button. Then, click the "Apply" button;

1. Now, go to the created state by selecting it from the drop-down menu accessed through the layers icon in the upper left corner;

1. Click the “Add new widget” icon in the center of the screen;

1. In the opened widget bundles selection, select "Indoor Environment";

1. Select the "Indoor temperature card with background" widget;

1. In the add widget window, navigate to the "Entity alias" tab. Specify the "Entity from dashboard state" alias in the "Entity alias" field and "temperature" data key in the “Columns” section. Click the "Add" button in the lower right corner;

1. After adding the widget save all applied changes;


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-9-ce.webp" alt="In the root dashboard state, enter widget Edit mode by clicking the “pencil” icon in the upper right corner;" loading="lazy"><figcaption>In the root dashboard state, enter widget Edit mode by clicking the “pencil” icon in the upper right corner;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-10-ce.webp" alt="Scroll down to find &quot;Actions&quot; section. Click &quot;Add action&quot; button;" loading="lazy"><figcaption>Scroll down to find "Actions" section. Click "Add action" button;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-11-ce.webp" alt="The &quot;Entities table: Actions&quot; window will be opened. Click the &quot;Add action&quot; button in the top right corner;" loading="lazy"><figcaption>The "Entities table: Actions" window will be opened. Click the "Add action" button in the top right corner;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-12-ce.webp" alt="In the &quot;Add action&quot; dialog, enter the action name, and select an action source responsible for each entity separately (action cell button, on row click etc.). Then, choose the action type &quot;Navigate to new dashboard state&quot; and specify the new dashboard state to which the transition will be made. After, click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Add action" dialog, enter the action name, and select an action source responsible for each entity separately (action cell button, on row click etc.). Then, choose the action type "Navigate to new dashboard state" and specify the new dashboard state to which the transition will be made. After, click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-13-ce.webp" alt="After successfully adding the action, click the &quot;Save&quot; button. Then, click the &quot;Apply&quot; button;" loading="lazy"><figcaption>After successfully adding the action, click the "Save" button. Then, click the "Apply" button;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-14-ce.webp" alt="Now, go to the created state by selecting it from the drop-down menu accessed through the layers icon in the upper left corner;" loading="lazy"><figcaption>Now, go to the created state by selecting it from the drop-down menu accessed through the layers icon in the upper left corner;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-15-ce.webp" alt="Click the “Add new widget” icon in the center of the screen;" loading="lazy"><figcaption>Click the “Add new widget” icon in the center of the screen;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-16-ce.webp" alt="In the opened widget bundles selection, select &quot;Indoor Environment&quot;;" loading="lazy"><figcaption>In the opened widget bundles selection, select "Indoor Environment";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-17-ce.webp" alt="Select the &quot;Indoor temperature card with background&quot; widget;" loading="lazy"><figcaption>Select the "Indoor temperature card with background" widget;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-18-ce.webp" alt="In the add widget window, navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Entity from dashboard state&quot; alias in the &quot;Entity alias&quot; field and &quot;temperature&quot; data key in the “Columns” section. Click the &quot;Add&quot; button in the lower right corner;" loading="lazy"><figcaption>In the add widget window, navigate to the "Entity alias" tab. Specify the "Entity from dashboard state" alias in the "Entity alias" field and "temperature" data key in the “Columns” section. Click the "Add" button in the lower right corner;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-19-ce.webp" alt="After adding the widget save all applied changes;" loading="lazy"><figcaption>After adding the widget save all applied changes;</figcaption></figure></div>


Now, click the action button next to any entity. You will be transitioned to an inner state, which contains a widget with the details of the selected entity.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-20-ce.webp" alt="Now, click an action button opposite any entity;" loading="lazy"><figcaption>Now, click an action button opposite any entity;</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-from-dashboard-state-21-ce.webp" alt="You will be transitioned to an inner state, which contains a widget with the details of the selected entity." loading="lazy"><figcaption>You will be transitioned to an inner state, which contains a widget with the details of the selected entity.</figcaption></figure></div>


### Asset type

This alias allows you to filter assets by the specified asset profile(s) (and optionally by names starting with the entered query).

Adding an alias: in the “Add alias” dialog, enter the alias name, and select the “Asset type” filter type. Then specify the asset profile(s) and enter an expression that will filter the names of the displayed assets.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/asset-type-1-ce.webp" alt="In the &quot;Add alias&quot; dialog, enter the alias name, and select the “Asset type” filter type. Next, specify the asset profile(s) and optionally enter an expression to filter the names of the displayed assets;" loading="lazy"><figcaption>In the "Add alias" dialog, enter the alias name, and select the “Asset type” filter type. Next, specify the asset profile(s) and optionally enter an expression to filter the names of the displayed assets;</figcaption></figure></div>


This alias filters assets whose asset profile is "buildings" and whose names start with “Build”.

Let’s use an added alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Asset type" alias in the "Entity alias" field. Click "Add" and apply changes. The Entities table widget that displays assets with the asset profile "buildings" and whose name begins with "Build" has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/asset-type-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Asset type&quot; alias in the &quot;Entity alias&quot; field. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Asset type" alias in the "Entity alias" field. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/asset-type-3-ce.webp" alt="The Entities table widget that displays assets with the asset profile &quot;buildings&quot; and whose names begins with &quot;Build&quot; has been added" loading="lazy"><figcaption>The Entities table widget that displays assets with the asset profile "buildings" and whose names begins with "Build" has been added</figcaption></figure></div>


 
### Device type

This alias allows you to filter devices by the specified device profile(s) (and optionally by names starting with the entered query).

Adding an alias: in the “Add alias” dialog, enter the alias name, and select the “Device type” filter type. Then specify the device profile(s) and enter an expression that will filter the names of the displayed devices.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/device-type-1-ce.webp" alt="In the &quot;Add alias&quot; dialog, enter the alias name, and select the &quot;Device type&quot; filter type. Then specify the device profile(s) and optionally enter an expression to filter the names of the displayed devices;" loading="lazy"><figcaption>In the "Add alias" dialog, enter the alias name, and select the "Device type" filter type. Then specify the device profile(s) and optionally enter an expression to filter the names of the displayed devices;</figcaption></figure></div>


This alias filters devices whose device profile is "thermometers" and whose names start with “Therm”.

Let’s use an added alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Device type" alias in the "Entity alias" field. Click "Add" and apply changes. The Entities table widget that displays devices with the device profile "thermometers" and whose name begins with "Therm" has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/device-type-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Device type&quot; alias in the &quot;Entity alias&quot; field. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Device type" alias in the "Entity alias" field. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/device-type-3-ce.webp" alt="The Entities table widget that displays assets with the asset profile &quot;thermometers&quot; and whose names begins with &quot;Therm&quot; has been added" loading="lazy"><figcaption>The Entities table widget that displays assets with the asset profile "thermometers" and whose names begins with "Therm" has been added</figcaption></figure></div>


 
### Entity View type

This alias allows you to filter devices by the specified entity view type(s) (and optionally by names starting with the entered query).

Adding an alias: in the “Add alias” dialog, enter the alias name, and select the "Entity view type" filter type. Then specify the entity view type(s) and enter an expression that will filter the names of the displayed entity views.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-view-type-1-ce.webp" alt="In the &quot;Add alias&quot; dialog, enter the alias name, and select the &quot;Entity view type&quot; filter type. Then specify the entity view type(s) and optionally enter an expression to filter the names of the displayed entity views;" loading="lazy"><figcaption>In the "Add alias" dialog, enter the alias name, and select the "Entity view type" filter type. Then specify the entity view type(s) and optionally enter an expression to filter the names of the displayed entity views;</figcaption></figure></div>


This alias filters entity views of type "Compressors Entity View Type" and with name starting with "Compressor".

Let's see an example. Entity views named "Compressor BC-10 Entity View" and "Compressor QA-32 Entity View" have been created with the type "Compressors Entity View Type," providing access to the 'Power' timeseries from Compressor BC-10 and Compressor QA-32.

Let’s use an added alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Entity view type" alias in the "Entity alias" field. Click "Add" and apply changes. The Entities table widget that displays entity views with the entity view type "Compressors Entity View Type" and whose name begins with "Compressor" has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-view-type-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Entity view type&quot; alias in the &quot;Entity alias&quot; field. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Entity view type" alias in the "Entity alias" field. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-view-type-3-ce.webp" alt="The Entities table widget that displays entity views with the entity view type &quot;Entity view type&quot; and whose names begins with &quot;Compressor&quot; has been added" loading="lazy"><figcaption>The Entities table widget that displays entity views with the entity view type "Entity view type" and whose names begins with "Compressor" has been added</figcaption></figure></div>


### Edge type

This alias allows you to filter devices by the specified edge type(s) (and optionally by names starting with the entered query).

Adding an alias: in the “Add alias” dialog, enter the alias name, and select the “Entity view type” filter type. Then specify the entity view type(s) and enter an expression that will filter the names of the displayed entity view.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/edge-type-1-ce.webp" alt="In the &quot;Add alias&quot; dialog, enter the alias name, and select the &quot;Edge type&quot; filter type. Then specify the edge type(s) and enter an expression that will filter the names of the displayed edges;" loading="lazy"><figcaption>In the "Add alias" dialog, enter the alias name, and select the "Edge type" filter type. Then specify the edge type(s) and enter an expression that will filter the names of the displayed edges;</figcaption></figure></div>


This alias filters edges with an edge type of "edge instance" and names starting with "Edge".

Let’s use an added alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Edge type" alias in the "Entity alias" field. Click "Add" and apply changes. The Entities table widget that displays edges with the edge type "edge instance" and whose name begins with "Edge" has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/edge-type-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Edge type&quot; alias in the &quot;Entity alias&quot; field. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Edge type" alias in the "Entity alias" field. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/edge-type-3-ce.webp" alt="The Entities table widget that displays edges with the edge type &quot;edge instance&quot; and whose names begins with &quot;Edge&quot; has been added" loading="lazy"><figcaption>The Entities table widget that displays edges with the edge type "edge instance" and whose names begins with "Edge" has been added</figcaption></figure></div>


### API Usage State

There is an API Usage layout in the main menu of the TB platform. API Usage shows full statistics on the platform.  
Api Usage State alias allows fetching only the data you need from the user dashboard statistics.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/api-usage-state-1-ce.webp" alt="In the &quot;Add alias&quot; dialog, enter the alias name, and select the &quot;Api Usage State&quot; filter type." loading="lazy"><figcaption>In the "Add alias" dialog, enter the alias name, and select the "Api Usage State" filter type.</figcaption></figure></div>


Let's learn how to use the "Api Usage State" alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Api Usage State" alias in the "Entity alias" field and add data key(s) in the "Columns" section that fetches statistics from an API usage. Click "Add" and apply changes. The Entities table widget that displays API usage statistics has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/api-usage-state-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Api Usage State&quot; alias in the &quot;Entity alias&quot; field and add data key(s) in the &quot;Columns&quot; section that fetches statistics from an API usage. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Api Usage State" alias in the "Entity alias" field and add data key(s) in the "Columns" section that fetches statistics from an API usage. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/api-usage-state-3-ce.webp" alt="The Entities table widget that displays API usage statistics has been added." loading="lazy"><figcaption>The Entities table widget that displays API usage statistics has been added.</figcaption></figure></div>


### Relations query

This alias allows displaying entities that are related to a specified originator up to a specified level and in a specified direction.

Adding an alias: in the "Add alias" dialog, enter the alias name, specify the "Relations query" filter type.
Then, select the entity type and the entity itself for which you want to display the relationship. Set direction to "From" or "To" and max relation level.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/relations-query-1-ce.webp" alt="In the &quot;Add alias&quot; dialog, enter the alias name, specify the &quot;Relations query&quot; filter type. Then, select the type of entity and the entity itself, the relationship with which you want to display. Set direction to &quot;From&quot; or &quot;To&quot; and max relation level." loading="lazy"><figcaption>In the "Add alias" dialog, enter the alias name, specify the "Relations query" filter type. Then, select the type of entity and the entity itself, the relationship with which you want to display. Set direction to "From" or "To" and max relation level.</figcaption></figure></div>


In the example alias displays entities that have any relation to asset ‘District A’ up to relation level 3.

Let's learn how to use the "Relations query" alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Relations query" alias in the "Entity alias" field and add the "entityType" data key in the "Columns" section. Click "Add" and apply changes. The Entities table widget displays entities and their type that have any relation to the asset "District A" up to relation level 3.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/relations-query-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Relations query&quot; alias in the &quot;Entity alias&quot; field and add the &quot;entityType&quot; data key in the &quot;Columns&quot; section. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Relations query" alias in the "Entity alias" field and add the "entityType" data key in the "Columns" section. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/relations-query-3-ce.webp" alt="The Entities table widget displays entities and their type that have any relation to the asset &quot;District A&quot; up to relation level 3." loading="lazy"><figcaption>The Entities table widget displays entities and their type that have any relation to the asset "District A" up to relation level 3.</figcaption></figure></div>


### Asset search query

This alias allows displaying assets of the specified asset profile(s) that are related to a specified entity up to a specified level and in a specified direction.  

Adding an alias: in the "Add alias" dialog, enter the alias name, select the "Asset search query" filter type, and select the entity type and an entity itself, for which you want to display the relationship. Set direction to "From" or "To", max relation level and specify the asset profile(s) by which the assets will be filtered.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/asset-search-query-1-ce.webp" alt="in the &quot;Add alias&quot; dialog, enter the alias name, select the &quot;Asset search query&quot; filter type, and select the entity type and an entity itself, the relationship with which you want to display. Set direction to &quot;From&quot; or &quot;To&quot; and max relation level and specify the asset profile(s) by which the assets will be filtered." loading="lazy"><figcaption>in the "Add alias" dialog, enter the alias name, select the "Asset search query" filter type, and select the entity type and an entity itself, the relationship with which you want to display. Set direction to "From" or "To" and max relation level and specify the asset profile(s) by which the assets will be filtered.</figcaption></figure></div>


This alias displays assets with "buildings" and "district" asset profiles that have any relation to the device "Compressor QA-32" with a direction "From" and a relation level of 2.

Let's learn how to use the "Asset search query" alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Asset search query" alias in the "Entity alias" field, and add "name" and "type" data keys in the "Columns" section. Click "Add" and apply changes. The Entities table widget that displays assets that have any relation to the device "Compressor QA-32" with relation level of 2 has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/asset-search-query-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Asset search query&quot; alias in the &quot;Entity alias&quot; field and add &quot;name&quot; and &quot;type&quot; data keys in the &quot;Columns&quot; section. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Asset search query" alias in the "Entity alias" field and add "name" and "type" data keys in the "Columns" section. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/asset-search-query-3-ce.webp" alt="The Entities table widget that displays assets that have any relation to the device &quot;Compressor QA-32&quot; with relation level 2 has been added." loading="lazy"><figcaption>The Entities table widget that displays assets that have any relation to the device "Compressor QA-32" with relation level 2 has been added.</figcaption></figure></div>


### Device search query

This alias allows displaying devices of specified device profile(s) that are related to a specified originator up to a specified level and in a specified direction.  

Adding an alias: in the "Add alias" dialog, enter the alias name, select the "Device search query" filter type, and select the entity type and an entity itself, for which you want to display the relationship. Set direction to "From" or "To", max relation level and specify the device profile(s) by which the devices will be filtered.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/device-search-query-1-ce.webp" alt="In the &quot;Add alias&quot; dialog, enter the alias name, select the &quot;Device search query&quot; filter type, and select the entity type and choose an entity itself, the relationship with which you want to display. Set direction to &quot;From&quot; or &quot;To&quot; and max relation level and specify the device profile(s) by which the devices will be filtered." loading="lazy"><figcaption>In the "Add alias" dialog, enter the alias name, select the "Device search query" filter type, and select the entity type and choose an entity itself, the relationship with which you want to display. Set direction to "From" or "To" and max relation level and specify the device profile(s) by which the devices will be filtered.</figcaption></figure></div>


This alias displays devices with the "thermometers" device profile that have any relation to the asset "Building A" with direction "From" and relation level of 1.


Let's learn how to use the "Device search query alias" in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Device search query" alias in the "Entity alias" field and add "name", "type" and "temperature" data keys in the "Columns" section. Click "Add" and apply changes. The Entities table widget that displays devices that have any relation to the asset "Building A" up to relation level of 1 has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/device-search-query-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Device search query&quot; alias in the &quot;Entity alias&quot; field and add &quot;name&quot;, &quot;type&quot; and &quot;temperature&quot; data keys in the &quot;Columns&quot; section. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Device search query" alias in the "Entity alias" field and add "name", "type" and "temperature" data keys in the "Columns" section. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/device-search-query-3-ce.webp" alt="The Entities table widget that displays devices that have any relation to the asset “Building A” up to relation level 1 has been added." loading="lazy"><figcaption>The Entities table widget that displays devices that have any relation to the asset “Building A” up to relation level 1 has been added.</figcaption></figure></div>


### Entity view search query

This alias allows displaying entity views of the specified type that are related to a specified originator up to a specified level and in a specified direction.

A "Compressor BC-10 Entity View" entity view which has a relation to the "Compressor BC-10" device was created with a type "compressors entity view type" providing access to “temperature” timeseries from Compressor BC-10.

Adding an alias: in the "Add alias" dialog, enter the alias name, select the "Entity view search query" filter type, and select the entity type and an entity itself, for which you want to display the relationship. Set direction to "From" or "To", max relation level and specify the entity view type(s) by which entity views will be filtered.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-view-search-query-1-ce.webp" alt="In the “Add alias” dialog, enter the alias name, select the &quot;Entity view search query&quot; filter type, and select the entity type and choose an entity itself, the relationship with which you want to display. Set direction to &quot;From&quot; or &quot;To&quot; and max relation level and specify the entity view type(s) by which entity views will be filtered" loading="lazy"><figcaption>In the “Add alias” dialog, enter the alias name, select the "Entity view search query" filter type, and select the entity type and choose an entity itself, the relationship with which you want to display. Set direction to "From" or "To" and max relation level and specify the entity view type(s) by which entity views will be filtered</figcaption></figure></div>


This alias filters entity views with the "compressors entity view type" type that have any relation to the asset "Building A" with direction "From" and relation level of 1.


Let's learn how to use the "Entity view search query" alias in a widget. In the "Tables" widgets bundle, select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Entity view search query" alias in the "Entity alias" field and add "name", "type" and "temperature" data keys in the "Columns" section. Click "Add" and apply changes. The Entities table widget displaying entity views that have any relation to the asset "Building A" up to relation level of 1 has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/entity-view-search-query-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Entity view search query&quot; alias in the &quot;Entity alias&quot; field and add &quot;name&quot;, &quot;type&quot; and &quot;temperature&quot; data keys in the &quot;Columns&quot; section. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Entity view search query" alias in the "Entity alias" field and add "name", "type" and "temperature" data keys in the "Columns" section. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/entity-view-search-query-3-ce.webp" alt="The Entities table widget that displays entity views that have any relation to the asset &quot;Building A&quot; up to relation level 1 has been added." loading="lazy"><figcaption>The Entities table widget that displays entity views that have any relation to the asset "Building A" up to relation level 1 has been added.</figcaption></figure></div>


### Edge search query

This alias allows displaying edges of the specified type that are related to a specified originator up to a specified level and in a specified direction.

Adding an alias: in the "Add alias" dialog, enter the alias name, select the "Edge search query" filter type, and select the entity type and an entity itself, for which you want to display the relationship. Set direction to "From" or "To", max relation level and specify the edge type(s) by which the edges will be filtered.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/edge-search-query-1-ce.webp" alt="In the &quot;Add alias&quot; dialog, enter the alias name, select the &quot;Edge search query&quot; filter type, and select the entity type and an entity itself, the relationship with which you want to display. Set the direction to &quot;From&quot; or &quot;To&quot;, max relation level and specify the edge type(s) by which the edges will be filtered." loading="lazy"><figcaption>In the "Add alias" dialog, enter the alias name, select the "Edge search query" filter type, and select the entity type and an entity itself, the relationship with which you want to display. Set the direction to "From" or "To", max relation level and specify the edge type(s) by which the edges will be filtered.</figcaption></figure></div>


This alias filters edges with the "edge instance" type that have any relation to the asset "Building A" with a direction "From" and relation level of 1.

Let's learn how to use the "Edge search query" alias in a widget. In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Edge search query" alias in the "Entity alias" field and add "name" and "type" data keys in the "Columns" section. Click "Add" and apply changes. The Entities table widget displaying edges with any relation to the asset "Building A" up to relation level of 1 has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/alias/edge-search-query-2-ce.webp" alt="In the &quot;Tables&quot; widgets bundle select the &quot;Entities table&quot; widget. Navigate to the &quot;Entity alias&quot; tab. Specify the &quot;Edge search query&quot; alias in the &quot;Entity alias&quot; field and add &quot;name&quot; and &quot;type&quot; data keys in the &quot;Columns&quot; section. Click &quot;Add&quot;;" loading="lazy"><figcaption>In the "Tables" widgets bundle select the "Entities table" widget. Navigate to the "Entity alias" tab. Specify the "Edge search query" alias in the "Entity alias" field and add "name" and "type" data keys in the "Columns" section. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/alias/edge-search-query-3-ce.webp" alt="The Entities table widget that displays edges that have any relation to the asset &quot;Building A&quot; up to relation level 1 has been added." loading="lazy"><figcaption>The Entities table widget that displays edges that have any relation to the asset "Building A" up to relation level 1 has been added.</figcaption></figure></div>
