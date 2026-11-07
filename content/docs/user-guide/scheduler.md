+++
title = "Scheduler"
description = "Run actions at set times or when a value crosses a limit: write attributes, send commands, send recipes, generate reports or start your own rule chain logic."
weight = 43

[extra]
status = "checked"
checked = "4.3.0.57"
+++
The **scheduler** runs actions by itself: write a set point every morning, switch lighting off at night, send a recipe at the start of each shift, or generate a report when a batch ends.

Open **Features > Scheduler** in the left menu. **Reporting > Scheduling** shows the same scheduler, for reports.

## Event types

| Event type | What it does |
|---|---|
| **Update Attributes** | Writes server or shared attributes on the target entities. Shared attributes also reach the device |
| **Send RPC Request** | Sends a command (an RPC method with JSON parameters) to the target devices |
| **Send Recipe to Device** | Sends a [recipe](/docs/user-guide/recipes/) data record to its device |
| **Generate Report** | Generates a report and sends it to people. See [Schedule and send reports](/docs/reports/scheduling/) |
| **Custom** | Sends a message with your own message type, body and metadata into the rule engine, for logic you build in a [rule chain](/docs/user-guide/rule-engine-2-0/re-getting-started/) |
| **Update Firmware** | Assigns a firmware package and starts the [OTA update](/docs/user-guide/ota-updates/) on each device whose firmware changes. *From the release after 4.3.0.57; in 4.3.0.57 the event does not run, so assign firmware on the device or profile instead* |

Update Attributes, Send RPC Request and Custom events pass through the rule engine with the metadata `schedulerEventId`, `schedulerEventName` and `schedulerEventType`, so a rule chain can tell scheduled messages apart.

## Add an event

1. Click **+** (**Create new schedule**), enter a **Name** and choose the **Event type**.
2. Choose the **Target**:
   - **Single entity**: one device or asset.
   - **Group of entities**: every member of an [entity group](/docs/administration/entity-groups/).
   - **Entities group owner**: every entity of a type owned by the tenant or a customer.
3. Fill in what to do:
   - Update Attributes: the **Entity attributes scope** (**Server attributes** or **Shared attributes**), then **Add attribute** for each key and value.
   - Send RPC Request: the **RPC method** and **RPC parameters (JSON)**, for example method `setValue` with `{"value": 75}`.
   - Send Recipe to Device: the device, the **Recipe** and the **Recipe data**. The recipe always goes to the recipe's own device.
   - Update Firmware: the package, by title and version. For a device profile target the profile's firmware is set, and the devices that follow the profile update.
   - Custom: the **Message type**, **Message body (JSON)** and **Metadata**.
4. On the **Schedule** tab, set when it runs.
5. Turn on **Enable scheduler** and save.

## When it runs

Set the **Start time**, turn on **Repeat** and choose how it **Repeats**: **Once**, **Daily**, **Every N days**, **Weekly** (on chosen days), **Every N weeks**, **Monthly**, **Yearly**, or **Timer-based** (every so many seconds, minutes or hours). **Ends on** stops it at a date.

The **Trigger** option runs an event when a value crosses a limit; see [By a trigger](/docs/reports/scheduling/#by-a-trigger). It works for every event type, and it reacts to values that devices send over MQTT, HTTP or CoAP. *This is from the release after 4.3.0.57.* In 4.3.0.57, **Trigger** works only for **Generate Report** and only for values posted through the REST API; an event of another type with **Trigger** on does not run, so use **Repeat** for those.

## Table and calendar

**Table view** lists the events with their type, owner, user and schedule. Filter by event type, user and whether they are enabled. **Calendar view** shows when each event runs, by month or year; **Go to date** jumps to a day.

**Enable** and **Disable** pause an event without deleting it. **Export** saves selected events as JSON, and **Import schedule** loads them, for example to copy a schedule to another server.

## Related

- [Recipes](/docs/user-guide/recipes/)
- [Schedule and send reports](/docs/reports/scheduling/)
- [RPC](/docs/user-guide/rpc/)
