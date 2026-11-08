+++
title = "Entity views"
description = "Show a customer only part of a device or asset with an entity view: chosen keys and attributes, for a chosen period."
aliases = ["/docs/user-guide/ui/entity-views", "/docs/user-guide/ui/entity-views/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
An **entity view** is meant to show a customer only part of a device or asset: chosen time-series keys and attributes, and only for a period, for example while the customer rents the machine. Several views of one device can go to different customers.

<div class="st-callout warn">

**In 4.3.0.57 entity views do not show data.** You can create and assign them, but widgets that use a view stay empty, and reading its time series through the REST API fails with "Unsupported entity type for telemetry". **From the release after 4.3.0.57** views work as described on this page. Until then, use one of the ways below.

</div>

### In 4.3.0.57: share part of a device's data another way

| Need | Do this |
|---|---|
| A customer sees a whole device | Move the device to the customer, or add it to a device group the customer can see, under **Manage owner and groups** in the device's details. See [Customers](/docs/user-guide/ui/customers/) |
| A customer sees only some values | Build a dashboard for that customer whose widgets show only those keys, and give the customer that dashboard, not the device list |
| A customer sees values computed for them | Have a [calculated field](/docs/user-guide/calculated-fields/) of type **Propagation** copy the values to an asset that belongs to the customer |

## Create an entity view

Open **Entities > Entity views** in the left menu, click **+** and fill in:

| Setting | What it means |
|---|---|
| **Name**, **Entity view type** | For lists and search |
| **Target entity** | The device or asset the view shows |
| **Start time**, **End time** | The period of data the view gives access to. Empty means no limit |
| **Time series** | The keys the view shows. Leave it empty to show every key |
| **Client attributes**, **Shared attributes**, **Server attributes** | The attributes the view shows |

## What a view shows

*From the release after 4.3.0.57.*

- **Time series:** the target's values for the listed keys, only between the start and end time. This holds everywhere: the **Latest telemetry** tab, dashboards and live updates, and the REST API (`GET /api/plugins/telemetry/ENTITY_VIEW/{id}/values/timeseries`). When the target's newest value is after the end time, the view shows the last value inside its period.
- **Attributes:** saving the view copies the listed client, server and shared attributes from the target onto the view. After that, a [copy to view](/docs/user-guide/rule-engine-2-0/nodes/action/copy-to-view/) rule node keeps them up to date when they change.
- **Writing:** you cannot save time series to a view; the API answers 400 and asks you to write to the target instead. Attributes of the view itself can be read and set.

Assign the view to a customer, and that customer's users see its data in their dashboards.

## Related

- [Customers](/docs/user-guide/ui/customers/)
- [Devices](/docs/user-guide/ui/devices/)
