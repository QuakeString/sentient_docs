+++
title = "Calculated fields"
description = "Compute new values from device and asset data as it arrives: unit conversions, efficiencies, totals across a plant, zone presence and batch analysis."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **calculated field** computes a new value whenever the data it depends on changes, and stores the result like any other telemetry or attribute. Dashboards, alarm rules and reports then use it without any rule chain. Examples from a plant:

- the flow per ampere of a pump, from its flow and motor current;
- a temperature in °C from a sensor that reports °F;
- the total power of a production line, from the meters of its machines;
- whether a forklift is inside the loading bay, from its GPS position.

![Calculated fields list of the Demo Plant tenant](/images/st/calculated-fields.webp)

## Where they live

A calculated field belongs to one of:

- a **device** or **asset**: it runs for that one entity;
- a **device profile** or **asset profile**: it runs for every device or asset of the profile. Use this in most cases; a new pump of the same profile gets the field at once.

Add one from the **Calculated fields** tab of the entity or profile, or from **Calculated fields** in the left menu, which lists all of them in the tenant.

## Types

| Type | Computes | Page |
|---|---|---|
| **Simple** | One arithmetic expression, for example `flow / current` | [Simple](/docs/user-guide/calculated-fields/simple-calculated-field/) |
| **Script** | Anything a short script can do: conditions, several outputs, values over a time window | [Script](/docs/user-guide/calculated-fields/script-calculated-field/) |
| **Geofencing** | Whether an entity is inside zones, and when it enters or leaves them | [Geofencing](/docs/user-guide/calculated-fields/geofencing-calculated-field/) |
| **Propagation** | Copies values, or a result computed from them, to related entities, for example from a meter to its line | [Propagation](/docs/user-guide/calculated-fields/propagation-calculated-field/) |
| **Related entities aggregation** | Sum, average, minimum, maximum or count over related entities, for example the power of all machines of a line | [Related entities aggregation](/docs/user-guide/calculated-fields/related-entities-aggregation-calculated-field/) |
| **Time series data aggregation** | Hourly, daily, weekly or monthly figures from the entity's own history, for example energy per shift | [Time series aggregation](/docs/user-guide/calculated-fields/time-series-data-aggregation-calculated-field/) |
| **Event / batch analysis** | Finds events such as batches, cycles or downtime in the data, and builds a result for each | |

## Arguments

**Arguments** are the inputs. Each has a name you use in the expression or script, and says where the value comes from:

| Setting | Choices |
|---|---|
| **Entity** | **Current entity**, another **Device** or **Asset**, the **Customer**, or the **Current tenant** |
| **Argument type** | **Latest telemetry** (the newest value of a time-series key), **Attribute**, or **Time series rolling** (the values of the last **Time window**, up to **Max values**) |
| **Key** | The time-series or attribute key |
| **Default value** | Used until the first value arrives |

Argument names may only contain letters, digits and `_`, and must not start with a digit. `ctx`, `e` and `pi` are reserved.

## Output

| Setting | What it does |
|---|---|
| **Output type** | **Time series** (keeps history, can be charted) or **Attribute** (keeps only the newest value) |
| **Output key** | The key the result is stored under |
| **Decimals by default** | Rounds the result |
| **Use latest timestamp** | Stores the result with the time of the newest input instead of the time of the calculation. Use it when devices send late or buffered data, for example through the [gateway](/docs/iot-gateway/) |

## Expressions and scripts

A **Simple** expression uses the argument names, `+ - * / % ^`, brackets, the functions `abs`, `sqrt`, `cbrt`, `pow`, `min`, `max`, `round`, `floor`, `ceil`, `log`, `ln`, `log10`, `exp`, `sin`, `cos`, `tan`, `toFixed` and others, and the constants `PI` and `E`:

```text
(temperatureF - 32) / 1.8
```

A **Script** returns an object with one entry per output key. SENTIENT runs scripts in **Rhai**. Scripts written in Rhai are translated when they run, so this works as it is:

```text
return {
    "temperatureC": (temperatureF - 32) / 1.8
};
```

**Test script function** in the editor runs the script with values you type, before you save.

## Reprocess old data

A new field only computes from data that arrives after you save it. To fill in its history, click **Reprocess** in the field's row, choose the **Time window** and start. SENTIENT shows the progress and can be cancelled.

## Find out why a field gives no value

1. Switch on debugging in the field's row, then click **See debug events**. Each calculation shows its inputs, its result or the error.
2. Check that every argument's key exists on the entity, with the same spelling and case. An argument without a value and without a **Default value** stops the calculation.
3. Check the limits in the [tenant profile](/docs/user-guide/tenant-profiles/): calculated fields per entity, arguments per field, data points in a rolling argument, state size.

Debugging switches itself off after the time set in the tenant profile, to protect the database.

## Related

- [Alarm rules](/docs/user-guide/alarm-rules/)
- [Device profiles](/docs/user-guide/device-profiles/)
- [Time series data](/docs/user-guide/telemetry/)
