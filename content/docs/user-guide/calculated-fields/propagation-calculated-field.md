+++
title = "Propagation calculated field"
description = "For complex calculations, Rhai is used. It enables advanced operations such as conditional statements, loops, and access to historical data."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/calculated-fields/propagation-calculated-field.md"
+++
**Propagation** automatically transfers data from the current entity to one or more related entities resolved through entity relations. 
It can either **copy values as-is** or **compute a new value before sending**, which makes it ideal for synchronizing telemetry and attributes across entity hierarchies.

Use "Propagation" when you need to:
- Mirror device telemetry to a parent asset (e.g., battery level, signal quality, last known status)
- Push configuration attributes from an asset to child devices (e.g., HVAC mode, setpoints, operating profiles)
- Transform data before sharing it (e.g., calculate dew point on a device and store it on the greenhouse asset)
- Propagate to multiple entities (e.g., update all devices managed by a building or a group)

<hr>

## Configuration


Open the [create calculated field](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#creating-a-calculated-field) dialog and specify:
- the calculated field **title**,
- the **entity or entity profile** to which the calculated field will be applied,
- Select "**Propagation**" as a calculated field **type**.

<hr>

### Propagation path to related entities

<b><font size="3">Relation direction</font></b>   
Define the path from the current entity to the entity to which the data will be propagated:
- **Up to parent** — data is propagated to the parent entity.
- **Down to child** — data is propagated to the child entity.

> Propagation works only with direct (single-level) relationships — without recursion or multi-level traversal.

<b><font size="3">Relation type</font></b>   
Defines the relationship type between the target entity and the related entities (for example, _Contains_, _Manages_, or any other type).

> If multiple entities match the selected relationship direction and relationship type, the data will be propagated to each of them.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-path-to-related-entities-1-ce.webp" alt="Define the path to the entity to which the data will be propagated, as well as the relationship type between the entities." loading="lazy"><figcaption>Define the path to the entity to which the data will be propagated, as well as the relationship type between the entities.</figcaption></figure></div>


<hr>

### Data to propagate

Define which data will be propagated to the related entity.   
The data to propagate is configured as arguments. For details on argument types and configuration, see the [Arguments](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments) section.

Two modes are available:

<b><font size="3">1. Arguments only</font></b>   
  Works as direct data copying data ([attribute](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments) or [latest telemetry](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=latestTelemetry#arguments)) from the _current entity_ to the related entity, with the option to rename the propagated key before storing it.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/data-to-propagate-1-ce.webp" alt="Click **Add argument** (1)." loading="lazy"><figcaption>Click **Add argument** (1).</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/data-to-propagate-2-ce.webp" alt="The data source will be the current entity to which the calculated field is applied.Specify the **argument type** (2), **time series key / attribute key** (3), **output key** (4), and **default value** (5), then click **Add** (6)." loading="lazy"><figcaption>The data source will be the current entity to which the calculated field is applied.<br>Specify the **argument type** (2), **time series key / attribute key** (3), **output key** (4), and **default value** (5), then click **Add** (6).</figcaption></figure></div>


<b><font size="3">2. Calculation result</font></b>   
  Allows you to compute or transform data ([attribute](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments), [latest telemetry](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=latestTelemetry#arguments), or [time series rolling](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=timeSeriesRolling#arguments)) from multiple entities (_Current entity / Device / Asset / Customer / Current tenant / Current owner_) before propagating it to the related entity.

The sequence of actions is as follows:
- Configure the arguments that will provide input data  from the selected entity for further processing.
- Provide a [Rhai](/docs/user-guide/rhai/) script that will calculate a new value based on the defined arguments.
- The computed result is then propagated to the related entity.

> The variable name that stores the computed result must be defined directly in the function body.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/data-to-propagate-3-ce.webp" alt="Switch to **Calculation result** mode (1). Click **Add argument** (2)." loading="lazy"><figcaption>Switch to **Calculation result** mode (1). Click **Add argument** (2).</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/data-to-propagate-4-ce.webp" alt="The data source will be the **current entity** (3) to which the calculated field is applied.Specify the **argument type** (4), **time series key / attribute key** (5), **output key** (6), and **default value** (7), then click **Add** (8)." loading="lazy"><figcaption>The data source will be the **current entity** (3) to which the calculated field is applied.<br>Specify the **argument type** (4), **time series key / attribute key** (5), **output key** (6), and **default value** (7), then click **Add** (8).</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/data-to-propagate-5-ce.webp" alt="Provide a Rhai script that will calculate a new value based on the defined arguments." loading="lazy"><figcaption>Provide a Rhai script that will calculate a new value based on the defined arguments.</figcaption></figure></div>


<hr>

<b><font size="4">Script</font></b>

Define the calculation logic using a [Rhai](/docs/user-guide/rhai/) function based on the variables configured in [Arguments](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments).

Script calculated fields must implement:

```js
function calculate(ctx, arg1, arg2, ...): object | object[]
```
The function can return a single JSON object (multiple output keys) or an array of JSON objects (multiple time series records).

> The output variable names are defined directly in the returned object.

Example: Dew point calculation

```js
// Constants for Magnus formula
var a = 17.625;
var b = 243.04;

var alpha = ((a * temperature) / (b + temperature)) + Math.log(humidity / 100.0);
var dewPoint = toFixed((b * alpha) / (a - alpha), 1);

return {"dewPoint": dewPoint};
```


The function uses the <span class="code-light">temperature</span> and <span class="code-light">humidity</span> arguments to calculate the dew point value.
The calculation result will be stored in the variable <span class="code-light">dewPoint</span>, rounding the value to one decimal places.

<b><font size="4">Direct argument access</font></b>   
Arguments are also passed as function parameters (`arg1`, `arg2`, ...), so you can use them directly (for example, temperature, humidity) for cleaner scripts.

> Use either direct parameters or `ctx.args.<arg>` depending on clarity and your preferred style.

<br><b><font size="4">Context object (ctx)</font></b>

The `ctx` object provides metadata and access to argument values:
- `ctx.latestTs` — the most recent timestamp (milliseconds) from telemetry-based arguments. Useful for storing results with the same timestamp as incoming data.
- `ctx.args` — an object containing all configured arguments, accessible via dot (`.`) notation:
    - **Single-value arguments** <i>(attributes or latest telemetry)</i>
        - `ctx.args.<arg>.ts` — timestamp of the argument.
        - `ctx.args.<arg>.value` — value of the argument.
    - **Rolling time series arguments**
        - `ctx.args.<arg>.timeWindow` — object with start and end timestamps `{ startTs, endTs }`.
        - `ctx.args.<arg>.values` — array of `{ ts, value }` records representing timestamped telemetry.
        - `ctx.args.<arg>.<method>()` — built-in methods such as `mean()`, `sum()`, `min()`, `max()`, `first()`, `last()`, `merge()`, and others.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-function-1-ce.webp" alt="Define a function that will perform calculations using the variables defined in the &quot;Arguments&quot; section. The variable name that will store the calculation result is defined within the function itself." loading="lazy"><figcaption>Define a function that will perform calculations using the variables defined in the "Arguments" section. The variable name that will store the calculation result is defined within the function itself.</figcaption></figure></div>


<hr>

### Output

Data is propagated to each related entity and stored there as either [time series](/docs/user-guide/telemetry/) or [attributes](/docs/user-guide/attributes/).

For more details about output types and processing strategies, see the [Output](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#output) section.

<hr>

## Examples

To help you get started, here are three common configuration patterns applied to real-world scenarios.

### Example 1: Propagate device battery level to the parent Asset

<b><font size="4">Use case</font></b>   
The Tracker A device sends its battery charge level (<span class="code-light">batteryLevel</span>) to SENTIENT as telemetry.

<b><font size="4">Goal</font></b>   
Automatically propagate the device battery level to the related Truck 1 asset and store it as a server-side attribute under a new key: <span class="code-light">deviceBatteryLevel</span>.

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Battery level propagation" calculated field configuration (JSON)](/docs/user-guide/resources/calculated-fields/propagation/battery_level_propagation_cf.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo device</font></b>

Import a device that publishes battery telemetry.
1. Download the CSV file: [battery-level-device-data.csv](/docs/user-guide/resources/calculated-fields/propagation/battery-level-device-data.csv)
2. Go to the **Devices** and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Tracker A
- **Type:** tracker
- **Time series:** <span class="code-light">batteryLevel</span>

> **Important note about the CSV:** the column type for the <span class="code-light">batteryLevel</span> key must be set to "**Time series**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-1-1-ce.webp" alt="Import a device that publishes **battery level** telemetry." loading="lazy"><figcaption>Import a device that publishes **battery level** telemetry.</figcaption></figure></div>


<br><b><font size="3">2. Import demo asset</font></b>

Import an asset that represents the tracked truck.
1. Download the CSV file: [battery-level-asset-data.csv](/docs/user-guide/resources/calculated-fields/propagation/battery-level-asset-data.csv)
2. Go to **Assets** and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Truck 1
- **Type:** truck


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-1-2-ce.webp" alt="Import the demonstration asset Truck 1." loading="lazy"><figcaption>Import the demonstration asset Truck 1.</figcaption></figure></div>


<br><b><font size="3">3. Create a relation between the asset and the device</font></b>

Create a relation so the calculated field can resolve the target asset.

Create a relationship between the **Track 1** asset and the **Tracker A** device:
- Relation direction: **From**
- Relation type: **Contains**

This relation is used by the propagation calculated field to locate the parent entity.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-1-3-ce.webp" alt="The **Tracker** device linked to the **Track 1** asset via the **Contains** relation." loading="lazy"><figcaption>The **Tracker** device linked to the **Track 1** asset via the **Contains** relation.</figcaption></figure></div>


<br><b><font size="3">4. Apply the Propagation calculated field to the device profile</font></b>

Configure a **Propagation** calculated field in the **tracker** device profile (automatically created during device import) so that it works for Tracker A.
1. [Download the calculated field configuration file](/docs/user-guide/resources/calculated-fields/propagation/battery_level_propagation_cf.json).
2. Go to the "Calculated fields" tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.

This configuration propagates the latest telemetry value of <span class="code-light">batteryLevel</span> to the parent asset (**Truck 1**).


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-1-4-ce.webp" alt="Go to the **Calculated fields** tab and import the calculated field configuration." loading="lazy"><figcaption>Go to the **Calculated fields** tab and import the calculated field configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-1-5-ce.webp" alt="Apply the calculated field to the **tracker** profile so it runs for all devices using it.Propagation path to related entities: Relation direction: Up to parent; Relation type: Contains" loading="lazy"><figcaption>Apply the calculated field to the **tracker** profile so it runs for all devices using it.<br>Propagation path to related entities: Relation direction: Up to parent; Relation type: Contains</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-1-6-ce.webp" alt="Argument settings:- **Entity type:** Current entity- **Argument type:** Latest telemetry- **Time series key:** batteryLevel- **Output key:** deviceBatteryLevel- **Default value:** no data." loading="lazy"><figcaption>Argument settings:<br>- **Entity type:** Current entity<br>- **Argument type:** Latest telemetry<br>- **Time series key:** batteryLevel<br>- **Output key:** deviceBatteryLevel<br>- **Default value:** no data.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-1-7-ce.webp" alt="The output value will be stored as a server-side **attribute**.Click **Add** to save the calculated field." loading="lazy"><figcaption>The output value will be stored as a server-side **attribute**.<br>Click **Add** to save the calculated field.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

The <span class="code-light">deviceBatteryLevel</span> attribute is propagated and stored on the **Truck 1** asset as a **server-side attribute**.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-1-8-ce.webp" alt="The **deviceBatteryLevel** attribute is propagated and stored on the **Truck 1** asset as a **server-side attribute**." loading="lazy"><figcaption>The **deviceBatteryLevel** attribute is propagated and stored on the **Truck 1** asset as a **server-side attribute**.</figcaption></figure></div>


<hr>

### Example 2: Dew point calculation and propagation to a parent Asset

<b><font size="4">Scenario</font></b>   
A Smart Device sends <span class="code-light">temperature</span> and <span class="code-light">humidity</span> telemetry to SENTIENT and is linked to the Greenhouse A asset via the _Contains_ relation.

<b><font size="4">Goal</font></b>   
Calculate the **dew point**, propagate the result to the related asset (**Greenhouse A**), and store it as a **telemetry**.

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Dew point propagation" calculated field configuration (JSON)](/docs/user-guide/resources/calculated-fields/propagation/dew_point_propagation_cf.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo device</font></b>

Import a device that publishes temperature and humidity telemetry.
1. Download the CSV file: [dew-point-calculation-device-data.csv](/docs/user-guide/resources/calculated-fields/propagation/dew-point-calculation-device-data.csv)
2. Go to the **Devices** and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Smart Device
- **Type:** smart-device
- **Time series:** <span class="code-light">humidity</span>, <span class="code-light">temperature</span>

> **Important note about the CSV:** the column type for the <span class="code-light">humidity</span> and <span class="code-light">temperature</span> keys must be set to "**Time series**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-2-1-ce.webp" alt="Import a device that publishes **temperature** and **humidity** telemetry." loading="lazy"><figcaption>Import a device that publishes **temperature** and **humidity** telemetry.</figcaption></figure></div>


<br><b><font size="3">2. Import demo asset</font></b>

Import the asset that represents the greenhouse.
1. Download the CSV file: [dew-point-calculation-and-propagation-asset-data.csv](/docs/user-guide/resources/calculated-fields/propagation/dew-point-calculation-and-propagation-asset-data.csv)
2. Go to **Assets** and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Greenhouse A
- **Type:** greenhouse


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-2-2-ce.webp" alt="Import the demonstration asset Greenhouse A." loading="lazy"><figcaption>Import the demonstration asset Greenhouse A.</figcaption></figure></div>


<br><b><font size="3">3. Create a relation between the asset and the device</font></b>

Create a relationship between the **Greenhouse A** asset and the **Smart Device**:
- Relation direction: **From**
- Relation type: **Contains**

This relation allows the calculated field to locate the parent asset when propagating output.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-2-3-ce.webp" alt="Create a relationship between the **Greenhouse A** asset and the **Smart Device**." loading="lazy"><figcaption>Create a relationship between the **Greenhouse A** asset and the **Smart Device**.</figcaption></figure></div>


<br><b><font size="3">4. Apply the calculated field to the device profile</font></b>

Configure the calculated field on the "smart-device" device profile (created automatically during device import), so it runs for Smart Device.
1. [Download the calculated field configuration file](/docs/user-guide/resources/calculated-fields/propagation/dew_point_propagation_cf.json).
3. Go to the "Calculated fields" tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.

This scenario calculates the dew point value from the specified input data. The value is propagated and stored as telemetry on the parent asset (**Greenhouse A**) under the <span class="code-light">dewPoint</span> key.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-2-4-ce.webp" alt="Go to the **Calculated fields** tab and import the calculated field configuration." loading="lazy"><figcaption>Go to the **Calculated fields** tab and import the calculated field configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-2-5-ce.webp" alt="Apply the calculated field to the **smart-device** profile so it runs for all devices using it.Propagation path to related entities: **Relation direction**: Up to parent; **Relation type**: Contains.**Data to propagate:** switch to **Calculation result** mode." loading="lazy"><figcaption>Apply the calculated field to the **smart-device** profile so it runs for all devices using it.<br>Propagation path to related entities: **Relation direction**: Up to parent; **Relation type**: Contains.<br><br>**Data to propagate:** switch to **Calculation result** mode.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-2-6-ce.webp" alt="First argument settings:- **Entity type:** Current entity- **Argument type:** Latest telemetry- **Time series key:** humidity- **Argument name:** humidity." loading="lazy"><figcaption>First argument settings:<br>- **Entity type:** Current entity<br>- **Argument type:** Latest telemetry<br>- **Time series key:** humidity<br>- **Argument name:** humidity.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-2-7-ce.webp" alt="Second argument settings:- **Entity type:** Current entity- **Argument type:** Latest telemetry- **Time series key:** temperature- **Argument name:** temperature." loading="lazy"><figcaption>Second argument settings:<br>- **Entity type:** Current entity<br>- **Argument type:** Latest telemetry<br>- **Time series key:** temperature<br>- **Argument name:** temperature.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-2-8-ce.webp" alt="This scenario calculates the dew point value from the specified input data. The value is propagated and stored as telemetry on the parent asset under the **dewPoint** key.Click **Add** to save the calculated field." loading="lazy"><figcaption>This scenario calculates the dew point value from the specified input data. The value is propagated and stored as telemetry on the parent asset under the **dewPoint** key.<br>Click **Add** to save the calculated field.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

The calculated value is propagated to the **Greenhouse A** asset and stored as a **telemetry** under the key <span class="code-light">dewPoint</span>.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-2-9-ce.webp" alt="The calculated value is propagated to the **Greenhouse A** asset and stored as a **telemetry** under the key **dewPoint**." loading="lazy"><figcaption>The calculated value is propagated to the **Greenhouse A** asset and stored as a **telemetry** under the key **dewPoint**.</figcaption></figure></div>


<hr>

### Example 3: Propagate HVAC mode to multiple child devices

<b><font size="4">Scenario</font></b>   
The Building A asset manages multiple child HVAC devices linked via the _Manages_ relation. The asset-level <span class="code-light">hvacMode</span> server attribute defines the operating mode for all devices (for example, _cooling_, _heating_, _off_).

<b><font size="4">Goal</font></b>   
Automatically propagate the <span class="code-light">hvacMode</span> attribute from Building A to all related HVAC devices.

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Propagate HVAC mode" calculated field configuration (JSON)](/docs/user-guide/resources/calculated-fields/propagation/cooling_propagation_cf.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo devices</font></b>
1. Download the CSV file: [propagate-hvac-mode-device-data.csv](/docs/user-guide/resources/calculated-fields/propagation/propagate-hvac-mode-device-data.csv)
2. Go to the **Devices** and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Room Sensor 1
- **Type:** sensor


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-3-1-ce.webp" alt="Go to the **Devices** and **import** device configurations from a CSV file." loading="lazy"><figcaption>Go to the **Devices** and **import** device configurations from a CSV file.</figcaption></figure></div>


<br><b><font size="3">2. Import demo asset</font></b>

Import an asset that represents the building.
1. Download the CSV file: [propagate-hvac-mode-asset-data.csv](/docs/user-guide/resources/calculated-fields/propagation/propagate-hvac-mode-asset-data.csv)
2. Go to **Assets** and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Building A
- **Type:** building
- **Server attributes:** <span class="code-light">hvacMode</span>

> **Important note about the CSV:** the column type for the <span class="code-light">hvacMode</span> keys must be set to "**Server attributes**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-3-2-ce.webp" alt="The imported **Building A** asset publishes the **hvacMode** value as an attribute." loading="lazy"><figcaption>The imported **Building A** asset publishes the **hvacMode** value as an attribute.</figcaption></figure></div>


<hr>

<b><font size="3">3. Create a relation between the asset and the devices</font></b>

Create a relationship between the **Building A** asset and the **room devices**.
- Relation direction: **From**
- Relation type: **Manages**

This relation is used by the propagation calculated field to locate the parent entity.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-3-3-ce.webp" alt="Create a relationship between the **Building A** asset and the **room devices**." loading="lazy"><figcaption>Create a relationship between the **Building A** asset and the **room devices**.</figcaption></figure></div>


<br><b><font size="3">4. Apply the calculated field to the asset profile</font></b>

Configure a **Propagation** calculated field on the "building" asset profile (created automatically during asset import), so it runs for Building A.
1. [Download the calculated field configuration file](/docs/user-guide/resources/calculated-fields/propagation/cooling_propagation_cf.json).
3. Go to the Calculated fields tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.

This configuration propagates the attribute value of <span class="code-light">hvacMode</span> to the child devices.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-3-4-ce.webp" alt="Go to the **Calculated fields** tab and import the calculated field configuration." loading="lazy"><figcaption>Go to the **Calculated fields** tab and import the calculated field configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-3-5-ce.webp" alt="Apply the calculated field to the **building** profile so it runs for all asset using it.Propagation path to related entities: **Relation direction**: Down to child; **Relation type**: Manages" loading="lazy"><figcaption>Apply the calculated field to the **building** profile so it runs for all asset using it.<br>Propagation path to related entities: **Relation direction**: Down to child; **Relation type**: Manages</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-3-6-ce.webp" alt="Argument settings.The propagated value will be stored on devices as an attribute.Click Add to save the calculated field." loading="lazy"><figcaption>Argument settings.<br>The propagated value will be stored on devices as an attribute.<br>Click <b>Add</b> to save the calculated field.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

Each HVAC device received the <span class="code-light">hvacMode</span> attribute with the value **cooling**.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-3-7-ce.webp" alt="Each HVAC device received the **hvacMode** attribute with the value **cooling**." loading="lazy"><figcaption>Each HVAC device received the **hvacMode** attribute with the value **cooling**.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-3-8-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/calculated-fields/propagation/propagation-cf-example-3-9-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<hr>

## Troubleshooting

### Propagation path settings do not apply after the update

**Problem:** When editing an existing Calculated Field to change the **Relation direction** or **Relation type** (e.g., switching from *Contains* to *Manages*), the field ignores these changes and continues to propagate data using the originally configured path.

**Cause:** The Calculated Field logic caches the **Propagation path to related entities** defined during the initial creation. It does not correctly detect updates made specifically to the relation direction or relation type in the configuration, resulting in the field failing to re-initialize the path.

**Solution:** To force the Calculated Field to apply the new propagation path settings,
the system requires a configuration change to the **Data to propagate** section.
Any modification to the arguments will trigger the necessary re-initialization.

Choose one of the following safe methods:

1. Re-create the Field (Cleanest)
   If you must keep your current arguments exactly as they are (e.g., you cannot change default values), the only way to trigger the update is to delete the existing Calculated Field and create a new one with the correct propagation path settings.

2. Modify Default Value (Recommended Workaround)
   If you want to fix the issue without re-creating the field,
   edit an existing argument and change its **Default value** (e.g., set a value if it was empty, or update it).
   > If the source data is missing, the new default value will be used. However, if the source data is always present, this is the smartest method as it forces the update with zero impact on your data.

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please contact us.
