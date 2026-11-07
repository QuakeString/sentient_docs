+++
title = "Transformation nodes"
description = "Change a message: its data, its metadata, or the entity it belongs to."
aliases = ["/docs/paas/eu/user-guide/rule-engine-2-0/transformation-nodes/", "/docs/paas/user-guide/rule-engine-2-0/transformation-nodes/", "/docs/pe/user-guide/rule-engine-2-0/transformation-nodes/", "/docs/user-guide/rule-engine-2-0/transformation-nodes/"]

[extra]
status = "checked"
checked = "4.3.0.57"
hide_children = true
+++
| Node | What it does | Outputs |
|---|---|---|
| [script](/docs/user-guide/rule-engine-2-0/nodes/transformation/script/) | Changes the message with a JavaScript or [Rhai](/docs/user-guide/rhai/) script | Success |
| [change originator](/docs/user-guide/rule-engine-2-0/nodes/transformation/change-originator/) | Makes the message belong to a related entity, the customer or the tenant | Success |
| [rename keys](/docs/user-guide/rule-engine-2-0/nodes/transformation/rename-keys/) | Renames keys in the message or its metadata | Success |
| [copy key-value pairs](/docs/user-guide/rule-engine-2-0/nodes/transformation/copy-key-value-pairs/) | Copies keys from the message to the metadata, or back | Success |
| [delete key-value pairs](/docs/user-guide/rule-engine-2-0/nodes/transformation/delete-key-value-pairs/) | Removes keys from the message, the metadata or both | Success |
| [extract with JSONPath](/docs/user-guide/rule-engine-2-0/nodes/transformation/json-path/) | Picks values out of the message with a JSONPath expression | Success |
| [split array msg](/docs/user-guide/rule-engine-2-0/nodes/transformation/split-array-msg/) | Turns a message holding an array into one message per element | Success |
| [deduplication](/docs/user-guide/rule-engine-2-0/nodes/transformation/deduplication/) | Keeps one message per originator within a time window | Success |
| [to email](/docs/user-guide/rule-engine-2-0/nodes/transformation/to-email/) | Builds an e-mail from the message, for the send email node | Success |

Every node also has a **Failure** output, used when the node cannot do its job. Nodes without a link do not have their own page yet.

Related: [All rule nodes](/docs/user-guide/rule-engine-2-0/nodes/), [Script language (Rhai)](/docs/user-guide/rhai/), [Getting started with rule chains](/docs/user-guide/rule-engine-2-0/re-getting-started/)
