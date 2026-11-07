+++
title = "Alarm rules"
description = "Raise and clear alarms by themselves from telemetry and attributes: arguments, trigger conditions with severities, duration and repeat counts, schedules, clear conditions and propagation."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
An **alarm rule** watches a device's or asset's data and raises an [alarm](/docs/user-guide/alarms/) when a condition is met, at the severity you choose. It can also clear the alarm by itself once the values are back to normal.

A rule belongs to one of these:

| Rule on | Applies to |
|---|---|
| A **device profile** or **asset profile** | Every device or asset with that profile. Use this in most cases, so one rule covers every pump of a kind |
| A **device** or **asset** | That one device or asset |
| A **customer** | That customer |

## Where to find them

- **Alarms > Alarm rules** in the left menu lists every rule. **Alarm rule filter** narrows it by alarm type and entity.
- The **Alarm rules** tab of a device, asset, customer, device profile or asset profile lists the rules on it.

Click **+** and choose **Add alarm rule**. **Import alarm rule** reads a rule exported earlier, and **Add from solution hub** takes a ready-made one from the [solution hub](/docs/solution-hub/).

## 1. General

- **Alarm type**: a short, unique name such as `High temperature`. Operators see it in the alarm list, and it decides which alarm the rule updates (see [One alarm per problem](/docs/user-guide/alarms/#one-alarm-per-problem)). When other languages are switched on, the **Translations** panel under it shows the alarm type in each language. SENTIENT translates it in the background when you save. See [Translations](/docs/administration/translations/).
- **Entity type** and the entity: what the rule is on. Not shown when you add the rule from an entity's own tab.
- The bug button sets **debugging**. While it is on, every evaluation is stored as an event, which helps when a rule does not fire. All events are kept only for the first 15 minutes, then only errors, because events fill the database quickly.

## 2. Arguments

Arguments are the values the rule looks at. Click **Add argument** and set:

| Setting | Choices |
|---|---|
| Where the value comes from | **Current entity**, another device or asset, **Customer**, **Current tenant** or **Current owner** |
| **Argument type** | **Latest telemetry** (a time series key, such as `temperature`), or **Attribute** with its **Attribute scope** (**Server**, **Client** or **Shared**) and **Attribute key** |
| **Default value** | Used while the key has no value yet |
| **Argument name** | The name you use in conditions, for example `temperature` or `maxTemperature` |

Keep limits in attributes, such as a server attribute `maxTemperature` on the profile's devices, rather than typing them into the condition. Then each device can have its own limit, and you change it without editing the rule.

## 3. Trigger conditions

Click **Add trigger condition**, **Select alarm severity**, and set the condition. Add a condition per severity, for example **Major** above 80 °C and **Critical** above 95 °C. SENTIENT checks the most severe first and raises or moves the alarm to the highest severity whose condition holds.

### The condition

In **Mode** **Simple**, you build the condition from **argument filters**: an argument, its value type (**String**, **Numeric**, **Boolean**), an operation (**equal**, **not equal**, **greater than**, **less than**, **greater or equal**, **less or equal**, **starts with**, **ends with**, **contains**, **not contains**) and a value. The value is **Static** (typed in) or **Dynamic** (another argument, such as `maxTemperature`). Several filters combine with **AND** or **OR**, and **Complex** groups them. **Filter preview** shows the result in words.

In **Mode** **Script**, you write a **Rhai** expression over the argument names that returns `true` or `false`:

```rhai
temperature > maxTemperature && pumpRunning
```

**Test script function** runs it with values you type before you save. Scripts written in TBEL are translated when they run.

> **Note for 4.3.0.57:** the **missing for** filter (no data for a time) does not fire yet. To raise an alarm when a device stops sending, use [Alarm when a device is offline](/docs/user-guide/rule-engine-2-0/tutorials/create-inactivity-alarm/).

### How long the condition must hold

| Condition type | Raises the alarm |
|---|---|
| **Simple** | As soon as the condition is true |
| **Duration** | When the condition stays true for a time, for example 5 minutes. A short spike does not raise it. The time can come from an argument |
| **Repeating** | When the condition is true a number of times in a row, for example 3 readings. The count can come from an argument |

### Schedule

By default a condition is **Active all the time**. **Specific time** limits it to some days of the week and hours, for example only during the day shift. **Custom** sets different hours per day. The schedule is **Static**, or **Dynamic** when an attribute holds it. Outside its schedule, the condition does not raise alarms.

### Alarm details and dashboard

- **Alarm details** is a text stored with the alarm, shown under **Details** in the alarm. `${argument name}` puts in the value, for example `Bearing at ${temperature} °C, limit ${maxTemperature} °C. Check lubrication.`
- **Mobile dashboard** is the dashboard the alarm opens in the mobile app.

## 4. Clear condition

Click **Add clear condition** and set it the same way, for example `temperature` **less or equal** `75`. The alarm is cleared once it holds.

Without a clear condition, the alarm stays active until someone clears it. Leave a gap between the trigger and clear values (here 80 and 75), so that a value hovering at the limit does not raise and clear the alarm over and over.

## 5. Advanced settings

Under **Advanced settings**, choose who else sees the alarm: **Propagate alarm to related entities** (optionally only along some **Relation types**), **Propagate alarm to entity owner (Customer or Tenant)**, **Propagate alarm to entity owners hierarchy** and **Propagate alarm to Tenant**. See [Propagation](/docs/user-guide/alarms/#propagation).

Click **Add**. The rule works at once, for every entity it applies to.

## Manage rules

Each row in the list shows the alarm type, the entity, the severities and whether there is a clear condition. Its buttons:

- **Copy alarm rule** starts a new rule from this one.
- **Export** saves the rule as a JSON file, to import on another SENTIENT installation.
- **Save to solution hub** shares it through the [solution hub](/docs/solution-hub/).
- **Events** shows the debug events and errors.
- **Edit** and **Delete**.

## Example: bearing temperature on every pump

On the device profile **Centrifugal pump**:

1. **Alarm type** `High bearing temperature`.
2. Arguments: `temperature` (**Latest telemetry**, key `bearingTemp`) and `maxTemperature` (**Attribute**, **Server**, default value `80`).
3. Trigger condition **Major**: `temperature` **greater than** the dynamic value `maxTemperature`, **Duration** 2 minutes.
4. Trigger condition **Critical**: Script `temperature > maxTemperature + 15`.
5. Clear condition: Script `temperature <= maxTemperature - 5`.

Each pump with this profile now raises its own alarm. To give one pump a different limit, set its `maxTemperature` attribute.

## Related

- [Working with alarms](/docs/user-guide/alarms/)
- [Notification center](/docs/user-guide/notifications/)
- [Calculated fields](/docs/user-guide/calculated-fields/)
