+++
title = "Entity views"
description = "Entity views in SENTIENT 4.3.0.57: what they are meant for, their current state, and how to share part of a device's data with a customer meanwhile."
aliases = ["/docs/user-guide/ui/entity-views", "/docs/user-guide/ui/entity-views/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
An **entity view** is meant to show a customer only part of a device or asset: chosen time-series keys and attributes, and only for a period, for example while the customer rents the machine. Several views of one device can go to different customers.

> **Note for 4.3.0.57:** entity views can be created and assigned, but they do not show data yet. Widgets that use an entity view stay empty, and reading its time series through the REST API fails with "Unsupported entity type for telemetry". A later version will complete them. Use the ways below meanwhile.

## Meanwhile: share part of a device's data

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
| **Time series** | The keys the view shows |
| **Client attributes**, **Shared attributes**, **Server attributes** | The attributes the view shows |

## Related

- [Customers](/docs/user-guide/ui/customers/)
- [Devices](/docs/user-guide/ui/devices/)
