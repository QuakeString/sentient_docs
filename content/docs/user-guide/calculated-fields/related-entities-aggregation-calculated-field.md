+++
title = "Related entities aggregation calculated field"
description = "For complex calculations, TBEL is used. It enables advanced operations such as conditional statements, loops, and access to historical data."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/calculated-fields/related-entities-aggregation-calculated-field.md"
+++
Related entities aggregation collects the **latest telemetry** or **attribute** values from multiple entities (devices, assets, customer, or tenant) related to the target entity, applies one or more aggregation functions, and stores the aggregated result on the target entity.   

Aggregation is performed only across **direct (single-level) relations**, ensuring predictable selection of entities.

Use "Related entities aggregation" when you need to compute a "group-level" metric from many entities, for example:
- **Fleet / building dashboards**: average temperature across all sensors, total power across all meters, max vibration across machines
- **Operational KPIs**: number of active devices, count of alarms, percentage of online units
- **Occupancy / presence tracking**: count how many devices are in a certain state (e.g., motion = true)
- **Energy and usage totals**: sum energy consumption across multiple devices or zones
- **Quality monitoring**: detect min/max readings across a group (e.g., lowest freezer temperature, highest humidity)
- **Filtered aggregation**: aggregate only a subset of entities (e.g., only "active" devices or only readings above a threshold)

<hr>

## Configuration


Open the [create calculated field](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#creating-a-calculated-field) dialog and specify:
- the calculated field **title**,
- the **entity or entity profile** to which the calculated field will be applied,
- Select "**Related entities aggregation**" as a calculated field **type**.

<hr>

### Aggregation path to related entities

SENTIENT will collect data for aggregation from all entities that match the selected relationship direction and relationship type.

<b><font size="3">Relation direction</font></b>   
Define the path to the entities from which the data will be read:
- **Down to child** — data is aggregated from child entities.
- **Up to parent** — data is aggregated from parent entities.

Aggregation works only with direct (single-level) relationships, without recursion or multi-level traversal.

<b><font size="3">Relation type</font></b>   
Define the relationship type between the target entity and the related entities (for example, Contains, Manages, or any relation type).


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-aggregation-path-to-related-entities-1-ce.webp" alt="Define the path to the entities from which the data will be read for aggregation, as well as the relationship type between the target entity and the related entities." loading="lazy"><figcaption>Define the path to the entities from which the data will be read for aggregation, as well as the relationship type between the target entity and the related entities.</figcaption></figure></div>


<hr>

### Arguments

The arguments define the data that will be retrieved from each related entity for aggregation.

Click **Add argument** and fill in the required fields:
- **Argument type**: [Latest telemetry](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=latestTelemetry#arguments) or [Attribute](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments)
- **Time series key / Attribute key**: the key to read
- **Argument name**: variable name used in metrics
- **Default value**: fallback if data is missing

For more details about arguments and configuration, see the [Arguments](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments) section.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-aggregation-argument-1-ce.webp" alt="Click **Add argument** (1) and fill in the required fields:select the **Argument type** (2), specify the **Time series key / Attribute key** (3) to read data from, enter the **Argument name** (4) that will be used in the metrics, and set the **Default value** (5).Then click **Add** (6).”" loading="lazy"><figcaption>Click **Add argument** (1) and fill in the required fields:<br>select the **Argument type** (2), specify the **Time series key / Attribute key** (3) to read data from, enter the **Argument name** (4) that will be used in the metrics, and set the **Default value** (5).<br>Then click **Add** (6).”</figcaption></figure></div>


<hr>

### Metrics

Define the function type (aggregation) that will be applied to the data specified in the arguments, and the key under which the aggregated result will be stored.

Each metric includes:
- **Metric name**: the output key name under which the aggregated result will be stored on the target entity.
- **Aggregation**: Average / Min / Max / Sum / Count / Count unique
- **Filter** (optional): include/exclude entity values before aggregation
- **Value source**: use a direct argument value (Key) or a function result (Function)
- **Argument name**: the [argument](#arguments) whose data is being aggregated

<b><font size="3">Filter</font></b>   
The filter is a function that returns <span class="code-light">true/false</span> and can use any defined arguments. If it returns <span class="code-light">true</span>, the entity value is included in the aggregation; otherwise, it is skipped.

Example:

```js
return temperature > 10 && status == "active";
```


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-aggregation-metrics-1-ce.webp" alt="Click **Add metric** (1) and configure the following:specify the **metric name** (2), select the **aggregation type** (3), optionally enable a **filter** (4), choose the **value source** (Key or Function) (5), and enter the **argument name** (6) that will be used as the data source.Then click **Add** (7)." loading="lazy"><figcaption>Click **Add metric** (1) and configure the following:<br>specify the **metric name** (2), select the **aggregation type** (3), optionally enable a **filter** (4), choose the **value source** (Key or Function) (5), and enter the **argument name** (6) that will be used as the data source.<br>Then click **Add** (7).</figcaption></figure></div>


<br><b><font size="4">Deduplication interval</font></b>

The Deduplication interval limits how often aggregation is executed when many related entities send frequent updates.

How it works:
- the first update triggers aggregation
- additional updates arriving within the interval do not trigger aggregation again
- after the interval ends, aggregation run again using the latest available data

> Minimum time between telemetry aggregations: 10 seconds.

This prevents excessive reprocessing and reduces system load in high-frequency environments.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-aggregation-metrics-2-ce.webp" alt="**Deduplication interval** is the minimum time period between repeated aggregations. It limits how often a calculated field can re-aggregate data from related entities in response to frequent updates." loading="lazy"><figcaption>**Deduplication interval** is the minimum time period between repeated aggregations. It limits how often a calculated field can re-aggregate data from related entities in response to frequent updates.</figcaption></figure></div>


<hr>

### Output

The calculation result is stored either as a [time series](/docs/user-guide/telemetry/) or an [attribute](/docs/user-guide/attributes/).   
If needed, set Decimals to round the value.

> **[Only for Time series]**   
Enable **Use latest timestamp** to store the result using the most recent argument timestamp instead of server time.

For more details about output types and processing strategies, see the [Output](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#output) section.

<hr>

## Example: Aggregate temperature values from multiple child devices

<b><font size="4">Scenario</font></b>   
Multiple temperature sensor devices are installed in **Building A** and continuously publish telemetry values.

<b><font size="4">Goal</font></b>   
Collect temperature telemetry from all sensors related to Building A and compute:
- <span class="code-light">avgTemperature</span> — average temperature in the building
- <span class="code-light">maxTemperature</span> — maximum temperature in the building

Store both values as **telemetry** on the **Building A** asset.

What you will configure

You will apply an "Aggregation" calculated field to the Building A asset that:
- reads the latest temperature value from related devices (child sensors)
- computes average and maximum
- writes the results back to Building A as telemetry keys <span class="code-light">avgTemperature</span> and <span class="code-light">maxTemperature</span>.

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Related entities aggregation" calculated field configuration (JSON)](/docs/user-guide/resources/calculated-fields/related-entities-aggregation/temperature_aggregation_cf.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo devices</font></b>

Import multiple smart devices that publish <span class="code-light">temperature</span> telemetry.
1. Download the CSV file: [device-data-with-temperature-telemetry.csv](/docs/user-guide/resources/calculated-fields/related-entities-aggregation/device-data-with-temperature-telemetry.csv)
2. Go to the **Devices** and [import](/docs/user-guide/bulk-provisioning/) the CSV file

**CSV includes:**
- **Name:** Smart Device 1
- **Type:** sensor
- **Time series:** <span class="code-light">temperature</span>

> **Important note about the CSV:** the column type for the <span class="code-light">temperature</span> key must be set to "**Time series**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-1-ce.webp" alt="Go to the **Devices** and **import** device configurations from a CSV file." loading="lazy"><figcaption>Go to the **Devices** and **import** device configurations from a CSV file.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-2-ce.webp" alt="Name: Smart Device 1Type: sensorTime series: temperature" loading="lazy"><figcaption>Name: Smart Device 1<br>Type: sensor<br>Time series: temperature</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-3-ce.webp" alt="Imported smart devices that publish **temperature** telemetry." loading="lazy"><figcaption>Imported smart devices that publish **temperature** telemetry.</figcaption></figure></div>


<br><b><font size="3">2. Import demo asset</font></b>

Import the asset that represents the building.
1. Download the CSV file: [building-asset-data.csv](/docs/user-guide/resources/calculated-fields/related-entities-aggregation/building-asset-data.csv)
2. Go to **Assets** and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Building A
- **Type:** building


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-4-ce.webp" alt="Import the demonstration asset Building A." loading="lazy"><figcaption>Import the demonstration asset Building A.</figcaption></figure></div>


<br><b><font size="3">3. Create relations between the asset and devices</font></b>

Create relationships between Building A and all smart sensors:
- **Relation direction:** From (Device &#8702; Building A)
- **Relation type:** Manages

These relations define the set of related entities whose telemetry will be aggregated.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-5-ce.webp" alt="Create relationships between Building A and all smart sensors: Relationship direction: From (Devices &#8702; Building A); Relationship type: Manages" loading="lazy"><figcaption>Create relationships between Building A and all smart sensors: Relationship direction: From (Devices &#8702; Building A); Relationship type: Manages</figcaption></figure></div>


<br><b><font size="3">4. Apply the calculated field to the asset</font></b>

Apply the **Related Entities Aggregation** calculated field to the **Building A** asset.
1. [Download the calculated field configuration file](/docs/user-guide/resources/calculated-fields/related-entities-aggregation/temperature_aggregation_cf.json).
2. Go to the "Calculated fields" tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.

The field will:
- read latest temperature value from all child devices
- compute avg/max
- store results on Building A


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-6-ce.webp" alt="Go to the **Calculated fields** tab and import the calculated field configuration." loading="lazy"><figcaption>Go to the **Calculated fields** tab and import the calculated field configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-7-ce.webp" alt="Apply the calculated field to the **building** asset profile.Propagation path to related entities: **Relation direction**: Down to child; **Relation type**: Manages." loading="lazy"><figcaption>Apply the calculated field to the **building** asset profile.<br>Propagation path to related entities: **Relation direction**: Down to child; **Relation type**: Manages.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-8-ce.webp" alt="Argument settings:- **Argument type:** Latest telemetry- **Time series key:** temperature- **Argument name:** temperature- **Default value:** 0." loading="lazy"><figcaption>Argument settings:<br>- **Argument type:** Latest telemetry<br>- **Time series key:** temperature<br>- **Argument name:** temperature<br>- **Default value:** 0.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-9-ce.webp" alt="First metric settings:- **Metric name:** avgTemperature- **Aggregation:** Average- **Value source:** key- **Argument name:** temperature." loading="lazy"><figcaption>First metric settings:<br>- **Metric name:** avgTemperature<br>- **Aggregation:** Average<br>- **Value source:** key<br>- **Argument name:** temperature.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-10-ce.webp" alt="Second metric settings:- **Metric name:** maxTemperature- **Aggregation:** Maximum- **Value source:** key- **Argument name:** temperature." loading="lazy"><figcaption>Second metric settings:<br>- **Metric name:** maxTemperature<br>- **Aggregation:** Maximum<br>- **Value source:** key<br>- **Argument name:** temperature.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-11-ce.webp" alt="Deduplication interval: 10 seconds.The output value will be stored as a telemetry. Click **Add** to save the calculation field." loading="lazy"><figcaption>Deduplication interval: 10 seconds.<br>The output value will be stored as a telemetry. Click **Add** to save the calculation field.</figcaption></figure></div>


> (Optional) Enable [Debug mode](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#debug) and review execution events using the **Events** icon.

<br><b><font size="4">Result</font></b>

The Building A asset stores aggregated telemetry such as:
- <span class="code-light">avgTemperature</span> — average temperature across all sensors
- <span class="code-light">maxTemperature</span> — maximum temperature reported by any sensor

Example:
```json
{ "avgTemperature": 22.7, "maxTemperature": 25.1 }
```


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/related-entities/related-entities-cf-example-1-12-ce.webp" alt="The Building A asset stores the aggregated telemetry values, such as:- **avgTemperature** — average temperature across all sensors- **maxTemperature** — maximum temperature measured by one of the sensors" loading="lazy"><figcaption>The Building A asset stores the aggregated telemetry values, such as:<br>- **avgTemperature** — average temperature across all sensors<br>- **maxTemperature** — maximum temperature measured by one of the sensors</figcaption></figure></div>


<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please contact us.
