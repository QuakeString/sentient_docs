+++
title = "Entities and relations"
description = "IoT asset management using SENTIENT entities and relations feature"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/entities-and-relations.md"
+++
## Entities Overview

SENTIENT provides the user interface and REST APIs to provision and manage multiple entity types and their relations in your IoT application.
Supported entities are:

 - **[Tenants](/docs/user-guide/ui/tenants/)** - you can treat the tenant as a separate business-entity: it's an individual or an organization who owns or produce devices and assets;
 Tenant may have multiple tenant administrator users and millions of customers, devices and assets;
 - **[Customers](/docs/user-guide/ui/customers/)** - the customer is also a separate business-entity: individual or organization who purchase or uses tenant devices and/or assets;
 Customer may have multiple users and millions of devices and/or assets;
 - **[Users](/docs/user-guide/ui/users/)** - users are able to browse dashboards and manage entities;
 - **[Devices](/docs/user-guide/ui/devices/)** - basic IoT entities that may produce telemetry data and handle RPC commands. For example, sensors, actuators, switches;
 - **[Assets](/docs/user-guide/ui/assets/)** - abstract IoT entities that may be related to other devices and assets. For example factory, field, vehicle;
 - **[Entity Views](/docs/user-guide/entity-views/)** - useful if you like to share only part of device or asset data to the customers;
 - **[Alarms](/docs/user-guide/alarms/)** - events that identify issues with your assets, devices, or other entities;
 - **[Dashboards](/docs/user-guide/dashboards/)** - visualization of your IoT data and ability to control particular devices through the user interface;
 - **Rule Node** - processing units for incoming messages, entity lifecycle events, etc;
 - **Rule Chain** - defines the flow of the processing in the [Rule Engine](/docs/user-guide/rule-engine-2-0/re-getting-started/). May contain many rule nodes and links to other rule chains;

Each entity supports:

 - **[Attributes](/docs/user-guide/attributes/)** - static and semi-static key-value pairs associated with entities. For example serial number, model, firmware version;
 - **[Time-series data](/docs/user-guide/telemetry/)** - time-series data points available for storage, querying and visualization. For example temperature, humidity, battery level;
 - **[Relations](#relations)** - directed connections to other entities. For example contains, manages, owns, produces.

Some entities support profiles:

  - **[Tenant Profiles](/docs/user-guide/tenant-profiles/)** - contains common settings for multiple tenants: entity, API and rate limits, etc. Each Tenant has the one and only profile at a single point in time.
  - **[Device Profiles](/docs/user-guide/device-profiles/)** - contains common settings for multiple devices: processing and transport configuration, etc. Each Device has the one and only profile at a single point in time.
  - **[Asset Profiles](/docs/user-guide/asset-profiles/)** - contains common settings for multiple assets: processing configuration, etc. Each Asset has the one and only profile at a single point in time.


This guide provides an overview of the features listed above, some useful links to get more details, and real-life examples of their usage.

## Relations

Entity relation defines connection between two SENTIENT entities that belong to the same [Tenant](/docs/user-guide/ui/tenants/).
The relation has an arbitrary type: Contains, Manages, Supports, etc. The relation is also directional.
You may treat SENTIENT relations as a [Has-a](https://en.wikipedia.org/wiki/Has-a) relationship from object-oriented programming.

Relations help to model physical world objects in SENTIENT. The easiest way to understand them is using the example.
Let’s assume we want to build an application that collects data from soil moisture and temperature sensors, visualize this data on the dashboard, detect issues, raise alarms and control the irrigation.
Let’s also assume we want to support multiple fields with hundreds of sensors. Fields may be also grouped into the Geo regions.

The following diagram explains how those entities are configured and stored in SENTIENT:

{{ diagram(name="entities-and-relations") }}


See ["add and delete assets"](/docs/user-guide/ui/assets/#add-and-delete-assets) and ["manage asset relations"](/docs/user-guide/ui/assets/#manage-asset-relations)
to learn how to configure this entities via Administration UI. You may also use [REST API](/docs/reference/rest-client/) to create entities and relations programmatically.

## Next steps

**Assign attributes to the assets and devices**

SENTIENT provides the ability to assign attributes to entities and manage them.
You are welcome to learn how to do it here:
<p><a href="/docs/user-guide/attributes" class="button">Working with device attributes</a></p>


**Upload telemetry data from devices**

SENTIENT provides the ability to work with telemetry data for devices and other entities.
You are welcome to learn how to do it here:
<p><a href="/docs/user-guide/telemetry" class="button">Working with telemetry data</a></p>

**Creating Rules for Alarms**

SENTIENT provides the ability to raise alarms using rule engine for devices and other entities.
You are welcome to learn how to do it here:
<p><a href="/docs/user-guide/alarms" class="button">Working with alarms</a></p>

**Design your dashboard**

Please [import](/docs/user-guide/ui/dashboards/#dashboard-import) the following [**dashboard**](/docs/user-guide/resources/region_fields_dashboard.json) that demonstrates Map, Alarm, Entity Table and Charts widgets.
