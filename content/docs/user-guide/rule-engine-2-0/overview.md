+++
title = "Rule engine overview"
description = "How SENTIENT processes every incoming message: rule chains, nodes, connections, the Root Rule Chain, scripts in JavaScript or Rhai, and debugging."
aliases = ["/docs/user-guide/ui/rule-chains/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Every value a device sends, every attribute change, every alarm and every device that connects or goes quiet becomes a **message**. The **rule engine** passes each message through a **rule chain**: a flow of **nodes** that decide what to do with it. Out of the box, the rule chain stores telemetry and attributes and passes commands on. You change it to filter bad readings, add context, convert units, call other systems, or forward data to a historian.

For computed values and alarms, prefer [calculated fields](/docs/user-guide/calculated-fields/) and [alarm rules](/docs/user-guide/alarm-rules/): they need no rule chain. Use the rule engine for routing and integration.

## Messages

A message has:

| Part | Holds |
|---|---|
| **Originator** | The device, asset or other entity it is about |
| **Type** | What happened: **Post telemetry**, **Post attributes**, **RPC Request from Device**, **RPC Request to Device**, **Connect Event**, **Disconnect Event**, **Activity Event**, **Inactivity Event**, alarm and entity events, and others |
| **Data** | The payload, as JSON, for example `{"temperature": 72.4}` |
| **Metadata** | Extra key-value pairs, for example `deviceName`, `deviceType` and `ts` |

## Rule chains and nodes

Open **Rule chains** in the left menu. Each tenant has a **Root Rule Chain**, which every message enters unless the device's [profile](/docs/user-guide/device-profiles/) names another rule chain.

![The Root Rule Chain](/images/st/rule-chain-root.webp)

The Root Rule Chain of a new tenant has six nodes:

1. **Message Type Switch** sends each message on by its type.
2. **Save Timeseries** stores **Post telemetry** messages.
3. **Save Client Attributes** stores **Post attributes** messages.
4. **RPC Call Request** passes **RPC Request to Device** messages to the device.
5. **Log RPC from Device** and **Log Other** write the rest to the server log.

Nodes are joined by **connections** named after the node's result: **Success** or **Failure** for most nodes, **True** or **False** for filters, and the message type for a switch. A message follows every connection that matches; a result with no connection ends there.

### Node groups

| Group | Does | Examples |
|---|---|---|
| [Filter](/docs/user-guide/rule-engine-2-0/nodes/filter/) | Decides where a message goes | Message type switch, script filter, check relation, geofencing |
| [Enrichment](/docs/user-guide/rule-engine-2-0/nodes/enrichment/) | Adds data to the message | Originator attributes, latest telemetry, customer or tenant details |
| [Transformation](/docs/user-guide/rule-engine-2-0/nodes/transformation/) | Changes the message | Script transformation, change originator, to email |
| [Action](/docs/user-guide/rule-engine-2-0/nodes/action/) | Does something | Save time series, save attributes, create or clear alarm, log, RPC, delay |
| [External](/docs/user-guide/rule-engine-2-0/nodes/external/) | Talks to other systems | REST API call, MQTT, Kafka, send email, send SMS |
| [Flow](/docs/user-guide/rule-engine-2-0/nodes/flow/) | Joins chains | Rule chain (go to another chain), output, acknowledge |

## Edit a rule chain

Click a rule chain to open the editor.

- Drag a node from the list on the left onto the canvas, fill in its settings and click **Add**. Type in the search box above the list to find a node.
- Drag from a node's right edge to another node to connect them, and choose the connection's name.
- Double-click a node to change it. Select nodes and press **Delete** to remove them.
- Click **Apply changes** (the tick at the bottom right) to save. Messages use the new chain at once.

Change the Root Rule Chain with care: a broken chain stops data from being stored. Make a copy first (**Export rule chain** in its row, then **Import rule chain**), or use [version control](/docs/user-guide/version-control/).

## Scripts

Script nodes (filters, transformations, switches) run small scripts in **JavaScript** or **Rhai**. Choose the language at the top of the script editor. Scripts written in Rhai run as Rhai. **Test script function** runs the script with a message you type, before you save.

A script that removes a reading above 1000:

```javascript
return msg.temperature === undefined || msg.temperature < 1000;
```

How many scripts a tenant may run in a month is set in its [tenant profile](/docs/user-guide/tenant-profiles/).

## Debugging

Switch on **Debug mode** in a node's settings, send a message, then open the node's **Events** tab: each message shows its data, metadata and the connection it left by, or the error. Debug mode switches itself off after the time set in the tenant profile, because it writes every message to the database.

## Related

- [Queues](/docs/user-guide/rule-engine-2-5/queues/)
- [Calculated fields](/docs/user-guide/calculated-fields/)
- [Alarm rules](/docs/user-guide/alarm-rules/)
