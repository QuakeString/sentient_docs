+++
title = "deduplication"
description = "Deduplicates messages from the same originator within a configurable time interval using strategies to return either the first, last, or all messages as a combined result."
aliases = ["/docs/reference/processors/alarm-deduplication-processor/"]

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/rule-engine-2-0/nodes/transformation/deduplication.md"
+++
![image](/images/user-guide/rule-engine-2-0/nodes/transformation-nodes/deduplication-node.webp)

**Deduplicate messages within the same Originator entity for a configurable period based on a specified deduplication strategy.** 

Deduplication strategies:
- FIRST - return first message that arrived during deduplication period.
- LAST - return last message that arrived during deduplication period.
- ALL - return all messages as a single JSON array message. Where each element represents object with msg and metadata inner properties.

Configuration:

<object width="70%" data="/images/user-guide/rule-engine-2-0/nodes/transformation-nodes/deduplication-node-2-ce.webp"></object>
