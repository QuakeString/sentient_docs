+++
title = "Action nodes"
description = "Do something with a message: save it, raise or clear an alarm, call a device, or change entities and relations."
aliases = ["/docs/paas/eu/user-guide/rule-engine-2-0/action-nodes/", "/docs/paas/user-guide/rule-engine-2-0/action-nodes/", "/docs/pe/user-guide/rule-engine-2-0/action-nodes/", "/docs/user-guide/rule-engine-2-0/action-nodes/"]

[extra]
status = "checked"
checked = "4.3.0.57"
hide_children = true
+++
| Node | What it does | Outputs |
|---|---|---|
| [save time series](/docs/user-guide/rule-engine-2-0/nodes/action/save-timeseries/) | Saves the message's values as time series | Success |
| [save attributes](/docs/user-guide/rule-engine-2-0/nodes/action/save-attributes/) | Saves the message's values as attributes | Success |
| [delete attributes](/docs/user-guide/rule-engine-2-0/nodes/action/delete-attributes/) | Deletes attributes of the originator | Success |
| [device profile](/docs/user-guide/rule-engine-2-0/nodes/action/device-profile/) | Raises and clears alarms from the alarm rules in the device profile | Success, Alarm Created, Alarm Updated, Alarm Severity Updated, Alarm Cleared |
| [calculated fields](/docs/user-guide/rule-engine-2-0/nodes/action/calculated-fields/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Runs the originator's calculated fields on the message without saving it | Success |
| [create alarm](/docs/user-guide/rule-engine-2-0/nodes/action/create-alarm/) | Creates an alarm, or updates the open one | Created, Updated, False |
| [clear alarm](/docs/user-guide/rule-engine-2-0/nodes/action/clear-alarm/) | Clears the open alarm | Cleared, False |
| [math function](/docs/user-guide/rule-engine-2-0/nodes/action/math-function/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Calculates a value with a math operation or formula and saves it | Success |
| [rpc call request](/docs/user-guide/rule-engine-2-0/nodes/action/rpc-call-request/) | Sends a command to a device and passes on its answer | Success |
| [rpc call reply](/docs/user-guide/rule-engine-2-0/nodes/action/rpc-call-reply/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Answers a command that a device sent | Success |
| [rest call reply](/docs/user-guide/rule-engine-2-0/nodes/action/rest-call-reply/) | Answers a REST API call that was sent into the rule engine | Success |
| [integration downlink](/docs/user-guide/rule-engine-2-0/nodes/action/integration-downlink/) | Sends the message out through an integration | Success |
| [device state](/docs/user-guide/rule-engine-2-0/nodes/action/device-state/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Reports device activity, connect and disconnect events | Success |
| [gps geofencing events](/docs/user-guide/rule-engine-2-0/nodes/action/gps-geofencing-events/) | Reports when a device enters or leaves an area, or stays inside or outside | Entered, Left, Inside, Outside |
| [create relation](/docs/user-guide/rule-engine-2-0/nodes/action/create-relation/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Creates a relation between the originator and another entity | Success |
| [delete relation](/docs/user-guide/rule-engine-2-0/nodes/action/delete-relation/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Deletes relations of the originator | Success |
| [assign to customer](/docs/user-guide/rule-engine-2-0/nodes/action/assign-to-customer/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Assigns the originator to a customer | Success |
| [unassign from customer](/docs/user-guide/rule-engine-2-0/nodes/action/unassign-from-customer/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Removes the originator from its customer | Success |
| [copy to view](/docs/user-guide/rule-engine-2-0/nodes/action/copy-to-view/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Copies attributes to the device's or asset's entity views | Success |
| [message count](/docs/user-guide/rule-engine-2-0/nodes/action/message-count/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Counts messages over an interval and sends the count as telemetry | Success |
| [generator](/docs/user-guide/rule-engine-2-0/nodes/action/generator/) | Creates messages on a timer, for tests and simulation | Success |
| [log](/docs/user-guide/rule-engine-2-0/nodes/action/log/) | Writes the message to the server log | Success |
| analytics | Sends the message's values to an analytics pipeline from the [Solution hub](/docs/solution-hub/). The message itself passes on at once | Success |
| [push to edge](/docs/user-guide/rule-engine-2-0/nodes/action/push-to-edge/) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Sends the message to a SENTIENT Edge | Success |
| checkpoint | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Moves the message to another queue | Success |
| [delay (deprecated)](/docs/user-guide/rule-engine-2-0/nodes/action/delay/) | Holds messages for a time. Kept for old rule chains | Success |
| synchronization start, synchronization end (deprecated) | **Not working yet in 4.3.0.57:** a rule chain that uses it does not load. Kept for old rule chains. Use checkpoint instead | Success |

Every node also has a **Failure** output, used when the node cannot do its job. Nodes without a link do not have their own page yet.

Related: [All rule nodes](/docs/user-guide/rule-engine-2-0/nodes/), [Script language (Rhai)](/docs/user-guide/rhai/), [Getting started with rule chains](/docs/user-guide/rule-engine-2-0/re-getting-started/)
