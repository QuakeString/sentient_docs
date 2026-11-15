+++
title = "Flow nodes"
description = "Move a message between rule chains and queues."
aliases = ["/docs/paas/eu/user-guide/rule-engine-2-0/flow-nodes/", "/docs/paas/user-guide/rule-engine-2-0/flow-nodes/", "/docs/pe/user-guide/rule-engine-2-0/flow-nodes/", "/docs/user-guide/rule-engine-2-0/flow-nodes/"]

[extra]
status = "checked"
checked = "4.3.0.57"
hide_children = true
+++
| Node | What it does | Outputs |
|---|---|---|
| [rule chain](/docs/user-guide/rule-engine-2-0/nodes/flow/rule-chain/) | Sends the message to another rule chain | Success |
| [output](/docs/user-guide/rule-engine-2-0/nodes/flow/output/) | Ends a rule chain that another chain called, and returns the message to it through the output's name | Names of the output nodes |
| [checkpoint](/docs/user-guide/rule-engine-2-0/nodes/flow/checkpoint/) | Passes the message straight on. Kept for imported rule chains. **In 4.3.0.57 this node does not run** and a rule chain that uses it does not load; it works from the release after | Success |
| [acknowledge](/docs/user-guide/rule-engine-2-0/nodes/flow/acknowledge/) | Marks the message as processed so the queue does not retry it | Success |

Every node also has a **Failure** output, used when the node cannot do its job. Nodes without a link do not have their own page yet.

Related: [All rule nodes](/docs/user-guide/rule-engine-2-0/nodes/), [Script language (Rhai)](/docs/user-guide/rhai/), [Getting started with rule chains](/docs/user-guide/rule-engine-2-0/re-getting-started/)
