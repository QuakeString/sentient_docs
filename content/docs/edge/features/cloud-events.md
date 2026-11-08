+++
title = "Cloud Events"
description = "Cloud Events"

[extra]
status = "imported"
checked = ""
source = "docs/edge/features/cloud-events.md"
+++
**Cloud Events** page shows events that SENTIENT Edge pushes to the cloud.


<div class="st-gallery"><figure><img src="/images/edge/cloud-events.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Check **Status** column to know if an event has been pushed to the cloud.
There are two status types:
* **Deployed** - event has been already pushed to the SENTIENT/PE server.
* **Pending** - event has been created on the SENTIENT Edge, stored to the local database and will be pushed to cloud as soon as connection is restored.

List of possible cloud actions:
* Added
* Deleted
* Updated
* Attributes Updated
* Attributes Deleted
* Timeseries Deleted
* Timeseries Updated
* RPC Call
* Credentials Updated
* Relation Add or Update
* Relation Deleted
* Relations Deleted
* Alarm Ack
* Alarm Clear
* Attributes Request
* Rule Chain Metadata Request
* Relation Request
* Credentials Request

## Next steps
