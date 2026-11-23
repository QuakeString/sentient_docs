+++
title = "Recipes"
description = "Keep sets of set points (recipes) for a machine and send them to it in one click, from the recipe list, a dashboard or a schedule."
weight = 42

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **recipe** describes the set points a machine takes for one product or batch, for example a mixer's speed, temperature and mixing time. Each set of values for it, such as *Product A* or *Product B*, is a **recipe data** record. Operators send a record to the machine in one click instead of typing each value.

Open **Features > Recipe manager** in the left menu. It has two pages: **Recipes** (the definitions) and **Recipe data** (the value sets).

## Create a recipe

On **Recipes**, click **+** and enter a **Name**, a **Description** and the **Device** the recipe is for. A recipe belongs to one device; to use the same set points on two machines, create a recipe for each.

Then **Add element** for each set point:

| Field | What it is |
|---|---|
| **Key** | The set point's name, for example `mixSpeed` |
| **Type** | **Integer**, **Double**, **Boolean**, **String**, **Enum** (a list of allowed values) or **Time** (`HH:MM` or `HH:MM:SS`) |
| **Unit**, **Default**, **Min**, **Max** | Shown to the operator; values outside min and max are refused |
| **Enum values** | For Enum: the allowed values. Press Enter or comma after each |
| **Target type** | How the value reaches the device: **RPC call** or **Shared attribute** |
| **Target address** | The RPC method, or the shared attribute key |
| **Description** | Help text for operators |

An element's type cannot be changed once the recipe exists. To change it, create a new recipe with the new type.

## Add recipe data

On **Recipe data**, click **+**, pick the **Recipe**, enter a **Name** (for example `Product A`) and fill in the **Values**. Each field shows its unit and limits.

Turn on **Readonly** to lock the values, so operators can send the record but not change it from a dashboard. **Duplicate** on a record copies it, for example to start *Product B* from *Product A*. **Enable** and **Disable** on a recipe or record hide it from operators without deleting it.

## Send to the device

**Send to device** on a recipe data row sends every value at once:

- **RPC call** elements: one RPC per element, with the target address as the method and the value as the parameters. The gateway's Modbus, OPC UA and other connectors write it to the register or node set up for that method.
- **Shared attribute** elements: all written together as shared attributes, which the device receives as an attribute update.

Sending does not wait for the device to confirm each value. Every send, manual or scheduled, is written to the record's **Audit logs** tab, with the values sent.

## On a dashboard

The **Recipe table** widget, in the **Recipe widgets** bundle, lists the recipe data records of the recipes you choose in its settings. Operators can send a record, edit its values and **Save & send**, add records and delete them, depending on their permissions. **Confirm before sending to device** asks before each send. Customer users see only the records they own.

## On a schedule

To send a recipe at a set time, for example at the start of each shift, add a [scheduler event](/docs/user-guide/scheduler/) of type **Send Recipe to Device** and pick the device, recipe and recipe data record.

## Related

- [Scheduler](/docs/user-guide/scheduler/)
- [RPC](/docs/user-guide/rpc/)
- [Attributes](/docs/user-guide/attributes/)
