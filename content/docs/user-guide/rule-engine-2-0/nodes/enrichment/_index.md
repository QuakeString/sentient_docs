+++
title = "Enrichment nodes"
description = "Add data to a message: attributes, latest values, history, or details of the originator and the entities around it."
aliases = ["/docs/paas/eu/user-guide/rule-engine-2-0/enrichment-nodes/", "/docs/paas/user-guide/rule-engine-2-0/enrichment-nodes/", "/docs/pe/user-guide/rule-engine-2-0/enrichment-nodes/", "/docs/user-guide/rule-engine-2-0/enrichment-nodes/"]

[extra]
status = "checked"
checked = "4.3.0.57"
hide_children = true
+++
| Node | What it does | Outputs |
|---|---|---|
| [originator attributes](/docs/user-guide/rule-engine-2-0/nodes/enrichment/originator-attributes/) | Adds attributes and latest values of the originator | Success |
| [originator fields](/docs/user-guide/rule-engine-2-0/nodes/enrichment/originator-fields/) | Adds fields of the originator, such as name, type or label | Success |
| [originator telemetry](/docs/user-guide/rule-engine-2-0/nodes/enrichment/originator-telemetry/) | Adds the originator's values over a time range | Success |
| [calculate delta](/docs/user-guide/rule-engine-2-0/nodes/enrichment/calculate-delta/) | Adds the difference between this value and the previous one, for meters and counters | Success |
| [customer attributes](/docs/user-guide/rule-engine-2-0/nodes/enrichment/customer-attributes/) | Adds attributes or latest values of the originator's customer | Success |
| [customer details](/docs/user-guide/rule-engine-2-0/nodes/enrichment/customer-details/) | Adds the customer's details, such as e-mail, phone and address | Success |
| [tenant attributes](/docs/user-guide/rule-engine-2-0/nodes/enrichment/tenant-attributes/) | Adds attributes or latest values of the tenant | Success |
| [tenant details](/docs/user-guide/rule-engine-2-0/nodes/enrichment/tenant-details/) | Adds the tenant's details, such as e-mail, phone and address | Success |
| [related entity data](/docs/user-guide/rule-engine-2-0/nodes/enrichment/related-entity-data/) | Adds attributes, latest values or fields of a related entity | Success |
| [related device attributes](/docs/user-guide/rule-engine-2-0/nodes/enrichment/related-device-attributes/) | Adds attributes or latest values of a related device | Success |
| [fetch device credentials](/docs/user-guide/rule-engine-2-0/nodes/enrichment/fetch-device-credentials/) | Adds the device's credentials | Success |
| entity details | Adds the originator's name, type and label | Success |
| asset details | Adds details of an asset originator | Success |
| entity data | Adds data from an entity query, with filters and sorting | Success |

Every node also has a **Failure** output, used when the node cannot do its job. Nodes without a link do not have their own page yet.

Related: [All rule nodes](/docs/user-guide/rule-engine-2-0/nodes/), [Script language (Rhai)](/docs/user-guide/rhai/), [Getting started with rule chains](/docs/user-guide/rule-engine-2-0/re-getting-started/)
