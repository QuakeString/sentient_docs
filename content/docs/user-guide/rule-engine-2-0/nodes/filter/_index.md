+++
title = "Filter nodes"
description = "Check a message and send it on through True or False, or through a named output. Filter nodes never change the message."
aliases = ["/docs/paas/eu/user-guide/rule-engine-2-0/filter-nodes/", "/docs/paas/user-guide/rule-engine-2-0/filter-nodes/", "/docs/pe/user-guide/rule-engine-2-0/filter-nodes/", "/docs/user-guide/rule-engine-2-0/filter-nodes/"]

[extra]
status = "checked"
checked = "4.3.0.57"
hide_children = true
+++
| Node | What it does | Outputs |
|---|---|---|
| [script](/docs/user-guide/rule-engine-2-0/nodes/filter/script/) | Runs a JavaScript or [Rhai](/docs/user-guide/rhai/) script that gives back true or false | True, False |
| [switch](/docs/user-guide/rule-engine-2-0/nodes/filter/switch/) | Runs a script that gives back the names of the outputs to use | Names you choose |
| [message type filter](/docs/user-guide/rule-engine-2-0/nodes/filter/message-type-filter/) | Checks the message type, for example telemetry or attributes | True, False |
| [message type switch](/docs/user-guide/rule-engine-2-0/nodes/filter/message-type-switch/) | Sends each message type through its own output | One per message type, Other |
| [entity type filter](/docs/user-guide/rule-engine-2-0/nodes/filter/entity-type-filter/) | Checks the originator's entity type: device, asset, customer and so on | True, False |
| [entity type switch](/docs/user-guide/rule-engine-2-0/nodes/filter/entity-type-switch/) | Sends each entity type through its own output | One per entity type |
| [device profile switch](/docs/user-guide/rule-engine-2-0/nodes/filter/device-profile-switch/) | Sends the message through the output named after the device's profile | Profile names |
| [asset profile switch](/docs/user-guide/rule-engine-2-0/nodes/filter/asset-profile-switch/) | Sends the message through the output named after the asset's profile | Profile names |
| [check fields presence](/docs/user-guide/rule-engine-2-0/nodes/filter/check-fields-presence/) | Checks that given keys exist in the message or its metadata | True, False |
| [check relation presence](/docs/user-guide/rule-engine-2-0/nodes/filter/check-relation-presence/) | Checks that the originator has a given relation to another entity | True, False |
| [alarm status filter](/docs/user-guide/rule-engine-2-0/nodes/filter/alarm-status-filter/) | Checks an alarm's status: active or cleared, acknowledged or not | True, False |
| [gps geofencing filter](/docs/user-guide/rule-engine-2-0/nodes/filter/gps-geofencing-filter/) | Checks whether a latitude and longitude are inside an area | True, False |

Every node also has a **Failure** output, used when the node cannot do its job. Nodes without a link do not have their own page yet.

Related: [All rule nodes](/docs/user-guide/rule-engine-2-0/nodes/), [Script language (Rhai)](/docs/user-guide/rhai/), [Getting started with rule chains](/docs/user-guide/rule-engine-2-0/re-getting-started/)
