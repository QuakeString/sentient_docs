+++
title = "Rule nodes"
description = "What a rule node is, how messages flow through its outputs, and the six groups of nodes in SENTIENT."
aliases = ["/docs/reference/plugins/messaging/", "/docs/reference/plugins/time/", "/docs/user-guide/rule-engine-2-0/nodes/action/add-to-group/", "/docs/user-guide/rule-engine-2-0/nodes/action/change-owner/", "/docs/user-guide/rule-engine-2-0/nodes/action/generate-dashboard-report/", "/docs/user-guide/rule-engine-2-0/nodes/action/generate-report/", "/docs/user-guide/rule-engine-2-0/nodes/action/remove-from-group/", "/docs/user-guide/rule-engine-2-0/nodes/action/save-to-custom-table/", "/docs/user-guide/rule-engine-2-0/nodes/analytics/aggregate-latest/", "/docs/user-guide/rule-engine-2-0/nodes/analytics/aggregate-stream/", "/docs/user-guide/rule-engine-2-0/nodes/analytics/alarms-count-deprecated/", "/docs/user-guide/rule-engine-2-0/nodes/analytics/alarms-count/", "/docs/user-guide/rule-engine-2-0/nodes/external/gcp-pubsub/", "/docs/user-guide/rule-engine-2-0/nodes/external/twilio-sms/", "/docs/user-guide/rule-engine-2-0/nodes/external/twilio-voice/", "/docs/user-guide/rule-engine-2-0/nodes/transformation/duplicate-to-group-by-name/", "/docs/user-guide/rule-engine-2-0/nodes/transformation/duplicate-to-group/", "/docs/user-guide/rule-engine-2-0/nodes/transformation/duplicate-to-related/", "/docs/user-guide/rule-engine-2-0/nodes/analytics/", "/docs/paas/eu/user-guide/rule-engine-2-0/analytics-nodes/", "/docs/paas/user-guide/rule-engine-2-0/analytics-nodes/", "/docs/pe/user-guide/rule-engine-2-0/analytics-nodes/"]

[extra]
status = "checked"
checked = "4.3.0.57"
hide_children = true
+++
A rule node takes one message at a time, does one job, and passes the result on through one or more named outputs, such as **Success** and **Failure** or **True** and **False**. You connect the outputs to the next nodes in the [rule chain editor](/docs/user-guide/rule-engine-2-0/re-getting-started/).

Every message has three parts that nodes read and change:

| Part | Holds |
|---|---|
| Data | The values, for example `{"temperature": 21.5}` |
| Metadata | Text values about the message, for example `deviceName`, `deviceType`, `ts` |
| Type | What the message is, for example `POST_TELEMETRY_REQUEST` or `ATTRIBUTES_UPDATED` |

Nodes are grouped as in the editor's node list. Some nodes in the list do not run in 4.3.0.57; the group pages mark them.

| Group | Use it to |
|---|---|
| [Filter](/docs/user-guide/rule-engine-2-0/nodes/filter/) | Decide where a message goes |
| [Enrichment](/docs/user-guide/rule-engine-2-0/nodes/enrichment/) | Add attributes, values and details to a message |
| [Transformation](/docs/user-guide/rule-engine-2-0/nodes/transformation/) | Change a message's data, metadata or originator |
| [Action](/docs/user-guide/rule-engine-2-0/nodes/action/) | Save data, raise alarms, send commands, change entities |
| [External](/docs/user-guide/rule-engine-2-0/nodes/external/) | Send a message to another system |
| [Flow](/docs/user-guide/rule-engine-2-0/nodes/flow/) | Move a message between rule chains and queues |

## Debugging a node

Switch on **Debug** in a node to record each message it handles, with its data, metadata and the output it took. Open the node's **Events** tab to read them.

Every node also has a **Failure** output, used when it cannot do its job. Switch on debug to see the error, or connect **Failure** to a **log** node.

## Scripts in nodes

The script filter, switch, script transformation, log, generator and the alarm nodes' details run JavaScript or [Rhai](/docs/user-guide/rhai/). Use **Test script function** in the node's editor to try a script on a message you type.
