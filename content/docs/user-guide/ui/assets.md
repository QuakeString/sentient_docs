+++
title = "Assets"
description = "Model sites, areas, lines and machines as assets, and link them to devices."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
An **asset** is something in your plant that does not send data itself but that you want to organise data around: a site, a building, a production line, a machine made of several devices. Assets are linked to devices and to other assets by [relations](/docs/user-guide/entities-and-relations/), which gives you a plant tree, for example *Plant > Boiler house > Feed pump P-101*.

Assets can hold attributes and telemetry of their own, for example the total energy of an area calculated from its meters with a [calculated field](/docs/user-guide/calculated-fields/), and they can raise alarms.

Open **Entities > Assets** in the left menu.

![The assets list of the Demo Plant tenant: a site and five areas](/images/st/assets-list.webp)

## The assets list

| Column | Meaning |
|---|---|
| **Created time** | When the asset was added |
| **Name** | Unique within the tenant |
| **Asset profile** | Groups assets of one kind, for example *Site*, *Area* or *Line*, and sets their rule chain and queue. See [Asset profiles](/docs/user-guide/asset-profiles/) |
| **Label** | Free text shown beside the name |
| **Customer** | The customer that owns the asset, if any |
| **Groups** | The asset groups it belongs to |

Above the list:

- **All** and **Groups** switch between the full list and [asset groups](/docs/administration/entity-groups/).
- **Asset profile** shows only assets of one profile.
- **Include customer entities** shows assets that belong to customers too.

In each row, the badge icon opens **Manage owner and groups**, and the bin deletes the asset.

## Add an asset

1. Click **+**, then **Add new asset**.
2. Type a **Name**, choose an **Asset profile** (or type a new one to create it), and optionally a **Label** and **Description**.
3. Click **Add**.

To add many at once, click **+**, then **Import assets**, and load a CSV file. See [Bulk provisioning](/docs/user-guide/bulk-provisioning/).

## Build the plant tree

Link each device to the asset it belongs to:

1. Open the asset and select the **Relations** tab.
2. Click **+**, choose the direction **From**, the relation type `Contains`, and pick the device or child asset.
3. Click **Add**.

Dashboards, calculated fields and alarm rules can then follow these relations, for example to show every pump in the boiler house or to sum the power of all meters in an area.

## Asset details

Click an asset to open its details. The tabs are the same as for a device: **Details**, **Attributes**, **Latest telemetry**, **Calculated fields**, **Alarm rules**, **Alarms**, **Events**, **Relations**, **Audit logs** and **Version control**. See [Devices](/docs/user-guide/ui/devices/#device-details) for what each shows.

The buttons at the top are **Open details page**, **Manage owner and groups** and **Delete asset**.

## Delete assets

Click the bin in an asset's row, or tick several assets and click the bin above the list. Deleting an asset removes its relations, so devices linked to it are no longer part of the tree. The devices themselves are not deleted. It cannot be undone.

## Related

- [Entities and relations](/docs/user-guide/entities-and-relations/)
- [Asset profiles](/docs/user-guide/asset-profiles/)
- [Devices](/docs/user-guide/ui/devices/)
