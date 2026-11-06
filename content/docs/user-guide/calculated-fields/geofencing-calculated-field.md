+++
title = "Geofencing calculated field"
description = "For evaluating real-time GPS coordinates against defined zones to track entity presence (INSIDE/OUTSIDE) and detect zone transition events (ENTERED/LEFT)."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/calculated-fields/geofencing-calculated-field.md"
+++
The **Geofencing** calculated field monitors entity movement in real time by evaluating incoming GPS coordinates against configured geofence zones.   
It lets you express spatial logic through configuration and automatically detect whether an entity (vehicle, container, tracker, etc.) is located inside specific areas such as restricted zones, parking lots, or operational boundaries.

Use Geofencing calculated fields when you need to:
- Track presence status in operational zones (e.g., “Is the truck inside the warehouse perimeter?”).
- Detect entry/exit transitions and record boundary-crossing events (ENTERED / LEFT).
- Monitor multiple independent zones at the same time (e.g., Safe Area + Restricted Area).
- Avoid false transitions when a logical area is represented by multiple adjacent polygons.
- Generate alarm-ready outputs (status + event keys) that can be used directly in alarms, dashboards, automation, or analytics
- Support dynamic zone assignment via relationships (zones can be added/removed without per-device reconfiguration)

<hr>

## Why use the Geofencing calculated field?

Geofencing calculated fields introduce Zone Groups, which eliminate state conflicts and improve scalability:

<b><font size="3">Independent state per zone group</font></b>   
Each zone group maintains its own INSIDE/OUTSIDE state. This enables simultaneous tracking of multiple zone categories (e.g., INSIDE safeArea while OUTSIDE restrictedArea) without overwriting or incorrect transitions.

<b><font size="3">Logical zone grouping (prevents false transitions)</font></b>   
When zones are discovered dynamically, multiple physical polygons can be treated as one logical group. If an entity moves between adjacent zones within the same group, the field preserves a continuous INSIDE status and does not generate false ENTERED/LEFT events.

<b><font size="3">Standardized outputs for alarms and dashboards</font></b>   
For each zone group, the field produces consistent output keys (&lt;zoneGroupName&gt;Status and &lt;zoneGroupName&gt;Event) that can be used directly in [alarm rules](https://sentient.invenia.in/docs/pe/user-guide/alarm-rules/), dashboards, automation, or analytics.

<hr>

## Configuration


Open the [create calculated field](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#creating-a-calculated-field) dialog and specify:
- the calculated field **title**,
- the **entity or entity profile** to which the calculated field will be applied,
- Select "**Geofencing**" as a calculated field **type**.

<hr>

### Entity coordinates

Map the incoming telemetry keys that represent the entity&#39;s GPS position.
- **Latitude time series key** — e.g., <span class="code-light">latitude</span> or <span class="code-light">lat</span>
- **Longitude time series key** — e.g., <span class="code-light">longitude</span> or <span class="code-light">lng</span>

> **Requirements**
- Values must be numeric.
- If either coordinate is missing or invalid, the calculation is skipped.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-entity-coordinates-1-ce.webp" alt="Specifies the input data for the calculation. You must map the timeseries keys from the incoming telemetry that represent the entity&#39;s GPS location." loading="lazy"><figcaption>Specifies the input data for the calculation. You must map the timeseries keys from the incoming telemetry that represent the entity&#39;s GPS location.</figcaption></figure></div>


<hr>

### Geofencing zone groups

A **Zone Group** is a logical container that bundles one or more physical zones (polygons/circles) into a single evaluation.

The calculated field checks all zones within the group and determines the entity&#39;s state:
- **INSIDE** - the entity is inside **at least one** zone in the group
- **OUTSIDE** - the entity is not located inside **any** zone in the group.

Click **Add zone group** to configure a new group.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-zone-groups-add-1-ce.webp" alt="A **Zone Group** is a logical container that bundles one or more physical zones (polygons/circles) into a single evaluation.Click **Add zone group** to configure a new group." loading="lazy"><figcaption>A **Zone Group** is a logical container that bundles one or more physical zones (polygons/circles) into a single evaluation.<br>Click **Add zone group** to configure a new group.</figcaption></figure></div>


<br>
In the zone group configuration dialog, configure the following settings:

<hr>

<b><font size="5">Zone group settings</font></b>

#### Name

The zone group name is used as a prefix for generated geofencing keys:
- <span class="code-light">&lt;name&gt;Status</span>
- <span class="code-light">&lt;name&gt;Event</span>

Best practice: use camelCase (e.g., <span class="code-light">restrictedArea</span>) to keep keys consistent:
- <span class="code-light">restrictedAreaStatus</span>
- <span class="code-light">restrictedAreaEvent</span>


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-zone-groups-name-1-ce.webp" alt="The zone group **Name** is used as a prefix for the generated geofencing telemetry keys (for example, **Name** + **Status** and **Name** + **Event**)." loading="lazy"><figcaption>The zone group **Name** is used as a prefix for the generated geofencing telemetry keys (for example, **Name** + **Status** and **Name** + **Event**).</figcaption></figure></div>


<hr>

#### Entity type

Choose where zone geometry definitions (polygons/circles) are stored:
- **Current entity** - the current entity to which the calculated field is applied.   
  If the field is created at the **Device profile** or **Asset profile** level, the calculation is performed for each entity associated with that profile.
- Another **Device** or **Asset** — another entity from which data is read.
- **Customer** — the associated customer.
- **Current tenant** — the current tenant.
- **Current owner** — the owner of the current entity.

> ⚠️ **Note on static sources:** selecting a specific device/asset/customer hardcodes the reference and reduces reusability. Prefer profile-level configuration


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-zone-groups-entity-type-1-ce.webp" alt="When you configure a group, the system needs to know where the zone definitions (the polygons) are stored. This is determined by the Entity Type (Source) setting." loading="lazy"><figcaption>When you configure a group, the system needs to know where the zone definitions (the polygons) are stored. This is determined by the Entity Type (Source) setting.</figcaption></figure></div>


<br><b><font size="3">Tips</font></b>

To choose the correct source, consider the following common patterns:

**1) Self-geofencing (each entity has its own zone)**

**Question:** Does each tracker have a unique zone stored on itself (e.g., a personal Home Zone)?   
**Answer:** Yes.   
**Action:** Select **Current entity**.   
**How it works:** The calculated field reads the perimeter attribute directly from the entity where the field is applied. This is ideal for device-specific zones such as _Home_ or custom _Safe Areas_.

<br>
**2) Dynamic zone lists (zones added/removed via relations)**

**Question:** Will the zone group contain multiple zones, or will zones change dynamically over time?   
**Answer:** Yes.   
**Action:** Select **Related entities** and configure a [Path from the entity to the zone](#path-from-entity-to-zones).   
**How it works:** The calculated field discovers zones by traversing the configured relation path starting from the source entity. The path can include multiple steps and directions (UP/DOWN), allowing you to reach zone assets through hierarchy relations.

**Example path:**   
**-** Go **UP** from _Vehicle_ to _Fleet_ using relation type _FleetToVehicle_   
**-** Then go **DOWN** from _Fleet_ to _Zone_ using relation type _FleetToRestrictedZone_

**Best practice:**   
This approach scales best. You can store all geometries in a single **Zone asset profile** and use relation types (e.g., _FleetToParking_, _FleetToRestricted_) to build multiple logical zone groups without duplicating configuration.

<br>
**3) Organization-level zones (inherited from Tenant/Owner)**

**Question:** Is the zone defined at an organizational level for an entire hierarchy (e.g., per Tenant or per Customer/Owner)?   
**Answer:** Yes.   
**Action:** Select **Current tenant** or **Current owner**.   
**How it works**: The calculated field retrieves the perimeter attribute from the Tenant or Customer that owns the entity. The device effectively inherits a zone defined at the business level.

**Best practice:**   
This is ideal for high-level policies. For example, in a multi-customer solution, each Customer can define its own global _Service Area_ polygon, and all devices under that customer automatically apply it without per-device configuration.

<hr>

#### Path from Entity to Zones

<table style="width:auto">
   <thead>
     <tr>
	 <td style="text-align: center"><b><em>* only for the "Related Entities" entity type</em></b></td>
     </tr>
   </thead>
</table> 

This section defines the precise "road map" the system follows to find the zone entities.
The path starts from the **source entity** (the Device or Asset running this Calculated Field) and follows the relations you specify.

<b><font size="3">Level</font></b>   
The sequence number indicating the depth of the relation step.
> **⚠️ Note:** The minimum level is 1. The maximum allowed depth is determined by the "Maximum relation level per 'Related entities' argument" in your Tenant Profile configuration.

<b><font size="3">Direction</font></b>   
- **Up:** Looks for parent entities (e.g., from Device up to Fleet).
- **Down:** Looks for child entities (e.g., from Fleet down to Zone).

<b><font size="3">Relation type</font></b>   
The specific connection name to follow for each step (e.g., "FleetToVehicle", "FleetToRestrictedZone", "FleetToNoParkingZone").

> **💡 Configuration flexibility:** You are not restricted to a specific topology.
> You can configure a single-level path (e.g., just one Up step if the zone is directly related to the source entity)
> or a complex multi-level path (mixing Up and Down) depending on your entities hierarchy.

<b><font size="4">Example configuration</font></b>   
To find zones for a vehicle (Source Entity) that belongs to a fleet:
- **Level 1:** Direction: "Up", Relation type: VehicleToFleet (Finds the Fleet).
- **Level 2:** Direction: "Down", Relation type: "FleetToRestrictedZone" (Finds all zone entities linked to that Fleet with the "FleetToRestrictedZone" relation type).


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-path-from-entity-to-zones-1-ce.webp" alt="This section defines the precise &quot;road map&quot; the system follows to find the zone entities.The path starts from the **Source Entity** (the Device or Asset running this Calculated Field) and follows the relations you specify." loading="lazy"><figcaption>This section defines the precise "road map" the system follows to find the zone entities.<br>The path starts from the **Source Entity** (the Device or Asset running this Calculated Field) and follows the relations you specify.</figcaption></figure></div>


<hr>

#### Perimeter attribute key

Specify the server-side attribute key on zone entities that stores the geometry. Supports [polygons](/docs/user-guide/widgets/map-widgets/#polygon) and [circles](/docs/user-guide/widgets/map-widgets/#circle).


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-zone-groups-perimeter-attribute-key-1-ce.webp" alt="Specify the server-side attribute key on zone entities that stores the geometry." loading="lazy"><figcaption>Specify the server-side attribute key on zone entities that stores the geometry.</figcaption></figure></div>


<hr>

#### Report strategy

Controls what telemetry the zone group generates:

<b><font size="3">Transition events only</font></b>


<b><font size="3">Presence status only</font></b>


<b><font size="3">Presence status and transition events</font></b>


This setting controls which telemetry the calculated field generates for the zone group. Choose the option that best matches your monitoring requirements:

<b><font size="3">Transition events only</font></b>
- Generates only transition events (**ENTERED / LEFT**) when the status changes.
- Event-driven workflows and minimal storage. Use this when you only care about boundary crossings (for example, counting how many times a vehicle entered a site).

<b><font size="3">Presence status only</font></b>
- Generates only the current status (**INSIDE / OUTSIDE**).
- Simple state monitoring. Use this when you only need the current location state (for example, "Is the truck in the garage?") without keeping an event history.

<b><font size="3">Presence status and transition events</font></b>
- Generates both status (**INSIDE / OUTSIDE**) and transition events (**ENTERED / LEFT**).
- Full monitoring and automation. This option supports dashboards (current state) and real-time alerts/notifications based on entry/exit events.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-zone-report-strategy-1-ce.webp" alt="This setting controls what telemetry data the calculated field generates for the group." loading="lazy"><figcaption>This setting controls what telemetry data the calculated field generates for the group.</figcaption></figure></div>


<hr>

#### Create relations with matched zones

<table style="width:auto">
   <thead>
     <tr>
	 <td style="text-align: center"><b><em>* only for the "Related entities" entity type</em></b></td>
     </tr>
   </thead>
</table> 

When enabled, the calculated field automatically creates/removes relations between the source entity and zones the entity is currently inside.

**Lifecycle:**   
Relations are managed dynamically based on movement:
- **On Enter:** A relation is created immediately when the entity enters a zone.
- **On Leave:** The relation is removed immediately when the entity leaves the zone.

<b><font size="4">Configuration</font></b>

<b><font size="3">Relation direction:</font></b>   
- **From zone to entity** — the Zone is treated as the parent, and the Source Entity as the child.
- **From entity to zone** — the Source Entity is treated as the parent, and the Zone as the child.

<b><font size="3">Relation type</font></b>   
Defines the relation type name to create (for example, <span class="code-light">currentlyInside</span>).

<b><font size="4">Use case</font></b>   
List which entities are currently inside a specific zone.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-create-relations-with-matched-zones-1-ce.webp" alt="When enabled, the calculated field automatically creates/removes relations between the source entity and zones the entity is currently inside." loading="lazy"><figcaption>When enabled, the calculated field automatically creates/removes relations between the source entity and zones the entity is currently inside.</figcaption></figure></div>


<hr>

#### Zone groups refresh interval

<table style="width:auto">
   <thead>
     <tr>
	 <td style="text-align: center"><strong><em>* available when at least one group uses "Related entities" entity type</em></strong></td>
     </tr>
   </thead>
</table> 

Controls how often SENTIENT refreshes the cached list of discovered zones:
- **Disabled:** Zone relations are fetched once and never refreshed. Use this only when entity relations are permanent and will not change at runtime (for example, static infrastructure).
- **Enabled:** Zone relations are refreshed periodically based on the configured interval (in seconds).

<b><font size="3">Tuning guidelines</font></b>
- **Low interval (e.g., 60s):** if relations change often. The system detects reassignment sooner and applies the latest zones with minimal delay.
- **High interval (e.g., 3600s):** if relations rarely change. This reduces database load by caching relations longer and improves overall performance.
  > ⚠️ Minimum allowed value is controlled by tenant profile setting "Min allowed update interval for 'Related entities' arguments".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-zone-groups-refresh-interval-1-ce.webp" alt="Controls how often SENTIENT refreshes the cached list of discovered zones." loading="lazy"><figcaption>Controls how often SENTIENT refreshes the cached list of discovered zones.</figcaption></figure></div>


<hr>

### Output

For each zone group, SENTIENT generates internal variables:
- <span class="code-light">&lt;zoneGroupName&gt;Status</span> -> **INSIDE / OUTSIDE**
- <span class="code-light">&lt;zoneGroupName&gt;Event</span> -> **ENTERED / LEFT**

Example for a group named **restrictedArea**:
- <span class="code-light">restrictedAreaStatus</span>
- <span class="code-light">restrictedAreaEvent</span>

In the Output section, map these variables to the target output keys and save them as [telemetry](/docs/user-guide/telemetry/) (recommended) or [attributes](/docs/user-guide/attributes/).

> **Best practice:** store the output data as telemetry, as this provides the greatest flexibility for dashboards, analytics, and alarms.

<hr>

## Examples

To help you get started, here are three common configuration patterns applied to real-world scenarios.

### Example 1: Pet Tracker (Self-Geofencing)

<b><font size="4">Scenario</font></b>   
You are building a pet tracking solution. Each dog collar tracker sends GPS coordinates (<span class="code-light">latitude</span>, <span class="code-light">longitude</span>) and stores its own "Home Zone" geometry (a circle) in a server-side attribute <span class="code-light">safeZone</span>.

Each dog has a unique zone (e.g., Buddy and Rex live in different locations), so the geofence geometry must be stored on the device itself.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/pet-tracking-example-1.webp" alt="You are building a pet tracking solution. Each dog collar has a unique “Home Zone” defined by the owner (e.g., a 40-meter radius around their specific house)." loading="lazy"><figcaption>You are building a pet tracking solution. Each dog collar has a unique “Home Zone” defined by the owner (e.g., a 40-meter radius around their specific house).</figcaption></figure></div>


<b><font size="4">Goal</font></b>   
Detect when the dog enters/leaves its safe zone and generate:
- presence status (INSIDE / OUTSIDE)
- transition events (ENTERED / LEFT)

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Pet Tracker" calculated field configuration (JSON)](/docs/user-guide/resources/calculated-fields/geofencing/pets-tracking-dashboard.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo devices</font></b>   
Import **two devices** — each device represents a tracker built into a dog collar. These devices will publish GPS coordinates as telemetry and a server-side <span class="code-light">safeZone</span> attribute that contains the home zone coordinates in the form of a circle.
1. [Download the CSV file](/docs/user-guide/resources/calculated-fields/geofencing/pets-tracking-device-data.csv) containing device configurations.
2. Go to the **Devices** and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Buddy, Rex
- **Type:** pet-tracking
- **Time series:** <span class="code-light">latitude</span>, <span class="code-light">longitude</span>
- **Server attribute:** <span class="code-light">safeZone</span>

> **Important notes about the CSV:**
- The CSV delimiter must be <b><span class="code-light">;</span></b>.
- <span class="code-light">latitude</span> and <span class="code-light">longitude</span> are **time series** keys that define the dog&#39;s current coordinates.
- <span class="code-light">safeZone</span> is a **server-side attribute** that defines the zone perimeter as a circle.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-1-ce.webp" alt="Go to the **Devices** and **import** device configurations from a CSV file." loading="lazy"><figcaption>Go to the **Devices** and **import** device configurations from a CSV file.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-2-ce.webp" alt="The CSV delimiter must be **;**" loading="lazy"><figcaption>The CSV delimiter must be **;**</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-3-ce.webp" alt="**Time series:** latitude, longitude, **Server attribute:** safeZone" loading="lazy"><figcaption>**Time series:** latitude, longitude, **Server attribute:** safeZone</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-4-ce.webp" alt="Imported devices that publish GPS coordinates as telemetry." loading="lazy"><figcaption>Imported devices that publish GPS coordinates as telemetry.</figcaption></figure></div>


<br><b><font size="3">2. Apply the calculated field to the device profile</font></b>   
When importing the devices, the "pet-tracking" profile is created automatically and assigned to them.
Apply the calculated field to this profile so it runs for all devices using it.
1. [Download the calculated field configuration file](/docs/user-guide/resources/calculated-fields/geofencing/pets-tracking-example-geofencing-cf.json).
2. Go to the "Calculated fields" tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.

This calculated field evaluates whether each dog is inside its own <span class="code-light">safeZone</span> and generates status/events accordingly.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-5-ce.webp" alt="Go to the **Calculated fields** tab and import the calculated field configuration." loading="lazy"><figcaption>Go to the **Calculated fields** tab and import the calculated field configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-6-ce.webp" alt="Apply the calculated field to the **pet-tracking** profile so it runs for all devices using it.Entity coordinates: latitude, longitude" loading="lazy"><figcaption>Apply the calculated field to the **pet-tracking** profile so it runs for all devices using it.<br>Entity coordinates: latitude, longitude</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-7-ce.webp" alt="Geofencing zone group settings." loading="lazy"><figcaption>Geofencing zone group settings.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-8-ce.webp" alt="The output values must be saved as telemetry." loading="lazy"><figcaption>The output values must be saved as telemetry.</figcaption></figure></div>


(Optional) Enable [Debug mode](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#debug) and inspect execution via the **Events** button.

<br><b><font size="3">3. Import the demo dashboard</font></b>   
Import the dashboard JSON to monitor devices:
- [Download the dashboard configuration file](/docs/user-guide/resources/calculated-fields/geofencing/pets-tracking-dashboard.json).
- Go to the **Dashboards** page and [import](/docs/pe/user-guide/dashboards/#import-dashboard/) the JSON file with dashboard configuration.

The dashboard includes:
- A map widget showing dog locations.
- An attribute card widget that displays:
  - The dog&#39;s current presence status relative to its safe zone (**INSIDE / OUTSIDE**)
  - The most recent safe zone transition event (**ENTERED / LEFT**)


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-9-ce.webp" alt="Import the demo dashboard." loading="lazy"><figcaption>Import the demo dashboard.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

As you move the dogs&#39; markers outside of or back into the home zone:
- status updates (INSIDE / OUTSIDE)
- event updates (ENTERED / LEFT)


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-10-ce.webp" alt="As you move the dogs&#39; markers outside of or back into the home zone:- status updates (INSIDE / OUTSIDE)- event updates (ENTERED / LEFT)" loading="lazy"><figcaption>As you move the dogs&#39; markers outside of or back into the home zone:<br>- status updates (INSIDE / OUTSIDE)<br>- event updates (ENTERED / LEFT)</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-11-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-12-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-13-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<hr>

### Example 2: Warehouse equipment (Direct Association)

<b><font size="4">Scenario</font></b>   
You manage a large distribution center. You have **two forklifts**. Each forklift tracker publishes GPS telemetry (<span class="code-light">latitude</span>, <span class="code-light">longitude</span>).   
The **warehouse** asset publishes the geofence perimeter as an attribute.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/warehouse-equipment-example-2.webp" alt="You manage a large distribution center. You have 2 forklifts, and each forklift is assigned to a specific “Warehouse Building” asset." loading="lazy"><figcaption>You manage a large distribution center. You have 2 forklifts, and each forklift is assigned to a specific “Warehouse Building” asset.</figcaption></figure></div>


<b><font size="4">Goal</font></b>   
Detect when a forklift leaves the perimeter of its assigned building, and generate:
- the current presence status (**INSIDE / OUTSIDE**)
- transition events (**ENTERED / LEFT**)

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Warehouse equipment" calculated field configuration (JSON).](/docs/user-guide/resources/calculated-fields/geofencing/warehouse-equipment-example-geofencing-cf.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo devices</font></b>   
Import **two devices** — each device represents a tracker installed in a forklift. The devices publish GPS coordinates as telemetry.
1. [Download the CSV file](/docs/user-guide/resources/calculated-fields/geofencing/warehouse-equipment-example-devices-data.csv) containing device configurations.
2. Go to the **Devices** page and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Forklift A, Forklift B
- **Type:** forklift
- **Time series:** <span class="code-light">latitude</span>, <span class="code-light">longitude</span>

> **Important notes about the CSV:** 
- the CSV delimiter must be <b><span class="code-light">;</span></b>.
- the column type for the <span class="code-light">latitude</span> and <span class="code-light">longitude</span> keys must be set to "**Time series**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-1-ce.webp" alt="Go to the **Devices** and **import** device configurations from a CSV file." loading="lazy"><figcaption>Go to the **Devices** and **import** device configurations from a CSV file.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-2-ce.webp" alt="The CSV delimiter must be **;**" loading="lazy"><figcaption>The CSV delimiter must be **;**</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-2-ce.webp" alt="**Time series:** latitude, longitude" loading="lazy"><figcaption>**Time series:** latitude, longitude</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-3-ce.webp" alt="Imported devices that publish GPS coordinates as telemetry." loading="lazy"><figcaption>Imported devices that publish GPS coordinates as telemetry.</figcaption></figure></div>


<br><b><font size="3">2. Import demo asset</font></b>   

- Download the CSV file: [warehouse-equipment-example-asset-data.csv](/docs/user-guide/resources/calculated-fields/geofencing/warehouse-equipment-example-asset-data.csv)
- Go to the **Assets** page and [import](/docs/user-guide/bulk-provisioning/) the CSV file into your SENTIENT instance:

**CSV includes:**
- **Name:** Warehouse A
- **Type:** warehouse
- **Server attribute:** <span class="code-light">perimeter</span>

> **Important notes about the CSV:** 
- the CSV delimiter must be <b><span class="code-light">;</span></b>.
- the column type for the <span class="code-light">perimeter</span> key must be set to "**Server attribute**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-4-ce.webp" alt="The Warehouse A asset publishes the geofence perimeter as an attribute." loading="lazy"><figcaption>The Warehouse A asset publishes the geofence perimeter as an attribute.</figcaption></figure></div>


<br><b><font size="3">3. Create relations</font></b>

Create a relationship between the **Warehouse Building A** asset and the **Forklift A** and **Forklift B** devices:
- Relation direction: **From**
- Relation type: **Contains**

This relation is used by the calculated field to resolve the assigned building zone for each forklift.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-5-ce.webp" alt="Create a relationship between the **Warehouse Building A** asset and the **Forklift A** and **Forklift B** devices." loading="lazy"><figcaption>Create a relationship between the **Warehouse Building A** asset and the **Forklift A** and **Forklift B** devices.</figcaption></figure></div>


<br><b><font size="3">4. Apply the calculated field to the device profile</font></b>   
When importing the devices, the "forklift" profile is created automatically and assigned to them.
Apply the calculated field to this profile so it runs for all devices using it.
1. [Download the calculated field configuration file](/docs/user-guide/resources/calculated-fields/geofencing/warehouse-equipment-example-geofencing-cf.json).
2. Go to the "Calculated fields" tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.

This calculated field resolves the warehouse zone via relations and generates status/events.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-6-ce.webp" alt="Go to the &quot;Calculated fields&quot; tab and import the configuration." loading="lazy"><figcaption>Go to the "Calculated fields" tab and import the configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-7-ce.webp" alt="Apply the calculated field to the **forklift** device profile so it runs for all devices using it.Entity coordinates: latitude, longitude" loading="lazy"><figcaption>Apply the calculated field to the **forklift** device profile so it runs for all devices using it.<br>Entity coordinates: latitude, longitude</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-8-ce.webp" alt="Geofencing zone group settings." loading="lazy"><figcaption>Geofencing zone group settings.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-9-ce.webp" alt="The output values must be saved as telemetry." loading="lazy"><figcaption>The output values must be saved as telemetry.</figcaption></figure></div>


<br><b><font size="3">5. Import the dashboard</font></b>   
Import the dashboard to monitor forklifts in real time.
- [Download the dashboard configuration file](/docs/user-guide/resources/calculated-fields/geofencing/warehouse_equipment_tracking_dashboard.json).
- Go to the **Dashboards** page and [import](/docs/pe/user-guide/dashboards/#import-dashboard/) the JSON file with dashboard configuration.

The dashboard includes:
- a **Map widget** showing the current position of each fork lift
- an **Attributes card widget** showing:
    - current presence state (**INSIDE / OUTSIDE**)
    - the last transition event (**ENTERED / LEFT**)


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-10-ce.webp" alt="Import the dashboard to monitor forklifts in real time." loading="lazy"><figcaption>Import the dashboard to monitor forklifts in real time.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

When you move the forklift markers outside of or back into the perimeter of **Warehouse Building A**, the **Forklifts** widget is updated automatically:
- the presence status is updated,
- transition events are generated when boundary crossings occur.

This confirms that geofencing based on a direct device-to-asset association is working correctly.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-11-ce.webp" alt="When you move the forklift markers outside of or back into the perimeter of **Warehouse Building A**, the **Forklifts** widget is updated automatically:- the presence status is updated,- transition events are generated when boundary crossings occur." loading="lazy"><figcaption>When you move the forklift markers outside of or back into the perimeter of **Warehouse Building A**, the **Forklifts** widget is updated automatically:<br>- the presence status is updated,<br>- transition events are generated when boundary crossings occur.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-12-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-13-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-2-14-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<hr>

### Example 3: Complex Fleet Management (Multiple Zone Types)

<b><font size="4">Scenario</font></b>   
A logistics company operates a fleet of trucks. Each truck must be monitored against multiple zone categories at the same time, such as a designated service area and restricted "no-go" areas.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/complex-fleet-management-example-3.webp" alt="A logistics company manages a fleet of trucks. Each fleet must comply with complex rules involving multiple different types of areas simultaneously." loading="lazy"><figcaption>A logistics company manages a fleet of trucks. Each fleet must comply with complex rules involving multiple different types of areas simultaneously.</figcaption></figure></div>


<b><font size="4">Goal</font></b>   
Track two independent conditions for each truck simultaneously:
- **Service area** — whether the truck is currently **INSIDE/OUTSIDE** its assigned service zone.
- **Restricted area** — detect if the truck **ENTERED/LEFT** any no-go zone.

This example uses two Zone Groups inside a single Geofencing calculated field. Both groups discover zones dynamically через Fleet relations, but use different relation types to separate logic:
- <span class="code-light">serviceArea</span> group: **UP** to fleet (Contains) → **DOWN** to zone (FleetToAllowedZone)
- <span class="code-light">restrictedArea</span> group: **UP** to fleet (Contains) → **DOWN** to zone (FleetToRestrictedZone)

> **Note (visualization only):** Zone assets may include a zoneType server attribute (for example, allowed / restricted) used only for map color-coding. The calculated field logic relies on relation types, not on zoneType.

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Fleet Geofencing" calculated field configuration (JSON)](/docs/user-guide/resources/calculated-fields/geofencing/complex-fleet-management-example-geofencing-cf.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo devices</font></b>   
Import **two devices** — each represents a tracker installed in a truck. Devices publish GPS coordinates as telemetry.
1. [Download the CSV file](/docs/user-guide/resources/calculated-fields/geofencing/complex-fleet-management-example-devices-data.csv) containing device configurations.
2. Go to the **Devices** page and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Truck 101, Truck 102
- **Type:** truck
- **Time series:** <span class="code-light">latitude</span>, <span class="code-light">longitude</span>

> **Important notes about the CSV:**
- the CSV delimiter must be <b><span class="code-light">;</span></b>. 
- the column type for the <span class="code-light">latitude</span> and <span class="code-light">longitude</span> keys must be set to "**Time series**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-1-ce.webp" alt="Go to the **Devices** and **import** device configurations from a CSV file." loading="lazy"><figcaption>Go to the **Devices** and **import** device configurations from a CSV file.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-1-2-ce.webp" alt="The CSV delimiter must be **;**" loading="lazy"><figcaption>The CSV delimiter must be **;**</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-2-ce.webp" alt="**Time series:** latitude, longitude" loading="lazy"><figcaption>**Time series:** latitude, longitude</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-3-ce.webp" alt="Imported devices that publish GPS coordinates as telemetry." loading="lazy"><figcaption>Imported devices that publish GPS coordinates as telemetry.</figcaption></figure></div>


<br><b><font size="3">2. Import demo asset</font></b>   
Import assets representing the fleet and zones.
- Download the CSV file: [complex-fleet-management-example-assets-data.csv](/docs/user-guide/resources/calculated-fields/geofencing/complex-fleet-management-example-assets-data.csv)
- Go to the "Assets" page and [import](/docs/user-guide/bulk-provisioning/) the CSV file into your SENTIENT instance:

**CSV includes:**
- **Name:** No-Go Zone A, Service Zone A, North East Fleet
- **Type:** zone, fleet
- **Server attribute:** <span class="code-light">perimeter</span>, <span class="code-light">zoneType</span>

> **Important notes about the CSV:** 
- the CSV delimiter must be <b><span class="code-light">;</span></b>.
- the column type for the <span class="code-light">perimeter</span> and <span class="code-light">zoneType</span> keys must be set to "**Server attribute**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-4-ce.webp" alt="Go to the **Assets** and **import** asset configurations from a CSV file." loading="lazy"><figcaption>Go to the **Assets** and **import** asset configurations from a CSV file.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-5-ce.webp" alt="The CSV delimiter must be **;**" loading="lazy"><figcaption>The CSV delimiter must be **;**</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-6-ce.webp" alt="**Server attribute:** zoneType, perimeter" loading="lazy"><figcaption>**Server attribute:** zoneType, perimeter</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-7-ce.webp" alt="Imported assets." loading="lazy"><figcaption>Imported assets.</figcaption></figure></div>


<br><b><font size="3">3. Create relations</font></b>   
Create the relations used by the calculated field to discover the fleet and its zones.

1. Link trucks to the fleet:
   - **North East Fleet** &#8702; **Truck 101** and **Truck 102**
     - **Relation direction:** From
     - **Relation type:** Contains

2. Link the fleet to service zones:
   - **North East Fleet** &#8702; **Service Zone A**
     - **Relation direction:** From
     - **Relation type:** FleetToAllowedZone

3. Link the fleet to restricted zones:
   - **North East Fleet** &#8702; **No-Go Zone A**
     - **Relation direction:** From
     - **Relation type:** FleetToRestrictedZone


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-8-ce.webp" alt="Create a relationship." loading="lazy"><figcaption>Create a relationship.</figcaption></figure></div>


<br><b><font size="3">4. Apply the calculated field to the device profile</font></b>   
When importing the devices, the "truck" device profile is created automatically and assigned to them.
Apply the calculated field to this profile so it runs for all trucks using it.
1. [Download the calculated field configuration file](/docs/user-guide/resources/calculated-fields/geofencing/complex-fleet-management-example-geofencing-cf.json)
2. Go to the "Calculated fields" tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-9-ce.webp" alt="Go to the &quot;Calculated fields&quot; tab and import the configuration." loading="lazy"><figcaption>Go to the "Calculated fields" tab and import the configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-10-ce.webp" alt="Apply the calculated field to the **forklift** device profile so it runs for all devices using it.Entity coordinates: latitude, longitude" loading="lazy"><figcaption>Apply the calculated field to the **forklift** device profile so it runs for all devices using it.<br>Entity coordinates: latitude, longitude</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-11-ce.webp" alt="Geofencing zone group settings." loading="lazy"><figcaption>Geofencing zone group settings.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-12-ce.webp" alt="Geofencing zone group settings." loading="lazy"><figcaption>Geofencing zone group settings.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-13-ce.webp" alt="The output values must be saved as telemetry.Click **Add** to save the calculation field." loading="lazy"><figcaption>The output values must be saved as telemetry.<br>Click **Add** to save the calculation field.</figcaption></figure></div>


<br><b><font size="3">5. Import the dashboard</font></b>   
Import the dashboard for real-time monitoring.
- [Download the dashboard configuration file](/docs/user-guide/resources/calculated-fields/geofencing/fleet_trucks_tracking_dashboard.json).
- Go to the "Dashboards" page and [import](/docs/pe/user-guide/dashboards/#import-dashboard/) the JSON file with dashboard configuration.

The dashboard includes:
- Map widget showing truck positions and zone overlays
- an attributes card widget showing:
  - current serviceAreaStatus 
  - current restrictedAreaStatus 
  - last restrictedAreaEvent (ENTERED / LEFT)


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-14-ce.webp" alt="Import the dashboard to monitor truck in real time." loading="lazy"><figcaption>Import the dashboard to monitor truck in real time.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

As you move truck markers across zone boundaries:
- serviceAreaStatus updates as **INSIDE / OUTSIDE**
- restrictedAreaEvent is generated on transitions (**ENTERED / LEFT**)
- both conditions are tracked independently for the same truck at the same time, without state conflicts.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-15-ce.webp" alt="As you move truck markers across zone boundaries:- serviceAreaStatus updates as **INSIDE / OUTSIDE**- restrictedAreaEvent is generated on transitions (**ENTERED / LEFT**)- both conditions are tracked independently for the same truck at the same time, without state conflicts." loading="lazy"><figcaption>As you move truck markers across zone boundaries:<br>- serviceAreaStatus updates as **INSIDE / OUTSIDE**<br>- restrictedAreaEvent is generated on transitions (**ENTERED / LEFT**)<br>- both conditions are tracked independently for the same truck at the same time, without state conflicts.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-16-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-17-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-18-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/calculated-fields/geofencing/geofencing-cf-example-3-19-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please [contact us](/docs/contact-us/).
