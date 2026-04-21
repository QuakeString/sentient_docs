---
layout: docwithnav-sentient-analytics
assignees:
  - vparomskiy
title: SENTIENT ANALYTICS widget actions
description: SENTIENT ANALYTICS widget actions

---

* TOC
{:toc}

## Configure OnRowClick action
SENTIENT ANALYTICS Table view support onRowClick action. You can configure what should happen when user click on a Row in a table.
For example, you can save entity to the Dashboard state alias or open new dashboard state.

To enable row click event:
* Add SENTIENT ANALYTICS Table View on SENTIENT dashboard.
* Open widget edit mode and switch to **Actions** tab.
* Press **Add action** button.
* In **Action source** field select **On row click**.
* Proceed standard widget action configuration.

Each row has multiple fields from on or multiple devices/assets. It means that 1 row can be connected with multiple items.
If you want to use 'onRowClick' action - you need to define what item is selected when row clicked.
* Open **View Settings** in SENTIENT ANALYTICS View edit mode.
* Open **View Mode fields** section.
* Select required Device/Asset type in **Row click entity** dropdown.
* Save changes.

## Configure OnRowClick action for Anomaly

If you use the Anomaly Table on your dashboard and want to create an action that not only sets the selected entity but also updates the time window, follow these straightforward steps:
1. **Configure Row Click Entity.** Head to the chart settings in SENTIENT ANALYTICS and set the "Row click entity."

   ![image](/images/sentient-analytics/row-click-anomaly.png)

2. **Create Row Click Action.** Go to the Actions tab in your Anomaly view settings on the dashboard and create a new action. Choose "On Row click" as the Action source and set the type to "Custom action."  
   Then you have to add some custom code to define the chosen entity as the selected entity on your dashboard. Begin by obtaining the state ID and parameters for the new state entity. In our example, we used "selectedDevice,"
   but feel free to adapt this name based on your specific use case. Lastly, update both the time window and the state.

```javascript
let stateId = widgetContext.stateController.getStateId();
let stateParams = widgetContext.stateController.getStateParams();
stateParams.selectedDevice = {
    'entityId': entityId,
    'entityName': entityName
}

widgetContext.dashboard.onUpdateTimewindow(additionalParams.startTs, additionalParams.endTs); 
widgetContext.stateController.updateState(stateId, stateParams);
```
## Configure Date selected action

SENTIENT ANALYTICS Calendar and Anomaly table support date-selected action, allowing you to dynamically update the time window of your SENTIENT dashboard based on the selected date in either the calendar or the anomaly timerange.
To enable the date-select event:
1. Add a SENTIENT ANALYTICS View to your dashboard.
2. Enter widget edit mode and navigate to the Actions tab.
3. Click on the "Add action" button.
4. In the "Action source" field, choose "date-selected."
5. Set the type to "Custom action." You will receive the startTs and endTs parameters in the additionalParams argument of the custom function. Use the following code example to update the time window of your dashboard:

```javascript
widgetContext.dashboard.onUpdateTimewindow(additionalParams.startTs, additionalParams.endTs);
```

[//]: # (#### Configure Switch Field action)

## Configure Row Click to Select Multiple Entities

To implement the selection of multiple entities via row click in a SENTIENT ANALYTICS view, follow these steps. For this example, we have a table displaying a list of buildings, each with a count of energy meters and aggregated energy consumption.
Our goal is to send a list of energy meters to an alias on the dashboard upon clicking a specific table row.

![image](/images/sentient-analytics/row-click-select-entities.png)

**Step 1. Set Up the SENTIENT ANALYTICS View**
1. Set the entity type of the entities that you want to send as the alias. In our case it is EM energy meter.

   ![image](/images/sentient-analytics/set-up-sentient-analytics-view.png)
2. Send this view to the SENTIENT Dashboard.

**Step 2. Create New Alias on the Dashboard**
1. Name the Alias (Remember the alias name for later reference).
2. Toggle on "Resolve as multiple entities".
3. Choose "Entity list" as Filter Type.
4. In the Entity Type field choose the type of entities selectable via row click.
5. Select default entities to be displayed initially.

![image](/images/sentient-analytics/create-new-alias.png)

**Step 3. Configure the Action in SENTIENT ANALYTICS View**
1. Select “On Row Click” as action source.
2. Provide a name for the action.
3. Select "Custom action" as Action Type.

   ![image](/images/sentient-analytics/configure-action.png)
4. Write custom code to set ids to previously created alias:

* Find the alias:
```javascript
let entityAlias = 
Object.values(widgetContext.aliasController.entityAliases).find(el => el.alias 
=== "Selected entities");
```

* SENTIENT ANALYTICS view will send additionalParams containing an array of entities. Transform this array to extract only entity IDs and assign this array of entity IDs to the entityList in your alias.
```javascript
if(entityAlias && additionalParams["entityIds"] && additionalParams["entityIds"].length) {
    let devices = additionalParams["entityIds"].map(entity => entity.entityId.id);
    entityAlias.filter.entityList = devices;

    widgetContext.updateAliases();    
}
```

## Next Steps

{% assign currentGuide = "EmbedVisualizations" %}{% include templates/trndz-guides-banner.md %}
