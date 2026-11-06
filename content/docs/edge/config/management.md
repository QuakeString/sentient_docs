+++
title = "Edge"
description = "Edge"

[extra]
status = "imported"
checked = ""
source = "docs/edge/config/management.md"
+++
## Overview

**SENTIENT** offers two distinct deployment options: **SENTIENT Edge** and **SENTIENT Cloud**.

**SENTIENT Edge** is designed specifically for local, distributed data processing, enabling data analysis and management directly at the source of data generation. This approach allows for local processing, storage, and immediate response to critical situations, even without a continuous connection to the central server. For more information, see the [What is SENTIENT Edge](/docs/edge/getting-started-guides/what-is-edge/) article.

In contrast, **SENTIENT Cloud** is a fully managed, scalable, and fault-tolerant platform hosted in the cloud. The devices connected to the cloud transfer data over the internet. It is perfect for centralized data collection, processing, and management. For more information, see the [What is SENTIENT](/docs/edge/getting-started-guides/what-is-edge/) article.

### The Key Differences Between Edge and Cloud 

Although **Edge is designed similarly to Cloud**, the main difference lies **in the location of data processing**:
* **Edge** stores and processes data **locally** on the edge device.
* **Cloud** stores and processes data **centrally** in the cloud.

**Connectivity requirements** also differ: 
* Devices connected to the **Edge** can operate over a local area network (LAN) **without requiring cloud connectivity**.
* Devices connected to the **Cloud** are **require internet connectivity** to communicate with the platform.

**Cluster deployment** refers to the deployment in a distributed architecture, where multiple nodes (instances) work together to ensure scalability, fault tolerance, and high availability.
* The older versions of **Edge do not support cluster deployment**. It is designed to operate, process and analyze data locally before synchronizing with the central SENTIENT server.
* Starting with release 4.0 **Edge supports clustering**. Multiple Edge nodes can be clustered to provide high availability. If one node fails, the others can seamlessly continue to handle workloads. 
* **Cloud supports cluster deployment** and is crucial for handling large-scale IoT applications with numerous devices and high data throughput.

## Synchronization Architecture

**SENTIENT Edge** and **SENTIENT Cloud** communicate using the [gRPC (Remote Procedure Call) protocol](https://grpc.io/). This communication channel allows for efficient data synchronization between edge devices and the cloud server, enabling a seamless flow of messages while minimizing overhead and latency.

To optimize this process, messages are serialized using [Protocol Buffers (ProtoBuf)](https://github.com/protocolbuffers/protobuf).

All messages sent from **SENTIENT Edge** to **SENTIENT Cloud** are stored in a local **PostgreSQL** table **(cloud_event table)** prior to transmission. Starting with the **3.9 release**, these events can be stored in **Kafka topics** (in case Kafka is used as a queue). This allows **SENTIENT Edge** to operate without connectivity to the Cloud. Once a connection is established, all messages in the local **cloud_event/ts_cloud_event tables (or Kafka topic)** are sent to the **Cloud** and marked as successfully transferred.

To view the list of messages transferred from the **Cloud** to the **Edge**, go to the **Edge management > Instances** section of your Cloud (Server), click on the **Edge** and select the **"Downlinks"** tab:


<div class="st-gallery"><figure><img src="/images/edge/edge-management/0-downlinks.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Force Synchronization Procedure

During a network outage, or some other communication problem **SENTIENT Edge** could become out of sync from the **Cloud**. The Edge instance continues operating independently, collecting telemetry data, processing device events, and applying local rules. However, this data and state changes does not reach the Cloud, leading to inconsistencies.

To ensure that both the **SENTIENT Edge** and **Cloud** are aligned to deliver accurate and efficient IoT functionality, the synchronisation process can be forced.

To force synchronization procedure, go to the **Edge management > Instances** section of your Cloud (Server), click on the **Edge** and then, click the **"Sync Edge"** button:


<div class="st-gallery"><figure><img src="/images/edge/edge-management/1-force-sync.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Entities Management

Most entities can be created on the **Edge** instance, except for **Customers**, and **Users**, entities. To enable the use of these entities on the **Edge**, these entities must be **assigned** to the **Edge** prior to use.

To **assign** specific entities to the **Edge**, log in to your **Cloud** and navigate to the **Edge management > Instances** section:


1. The following <a href="/docs/pe/user-guide/entities-and-relations/" target="_blank">entities</a> and events can be managed: <ul><li><b>Make edge public:</b> The edge and all its data will be accessible by others.</li><li><b>Assign to customer:</b> Link a specific customer entity to the Edge instance.</li><li><b>Make edge private:</b> The edge and all its data will not be accessible by others.</li><li><b>Manage assets:</b> Monitor and control assets (e.g., buildings, equipment, or other entities) at the Edge. </li><li><b>Manage devices:</b> Administer devices that are managed by the Edge.</li><li><b>Manage entity views:</b> Manage filtered views of entities (e.g., devices or assets) at the Edge to display specific subsets of data or contextual information. Read more about the Entity views in <a href="/docs/user-guide/entity-views/" target="_blank">this article</a>.</li><li><b>Manage dashboards:</b> Customize, and manage dashboards at the Edge.</li><li><b>Manage rule chains:</b> Create, configure, and manage rule chains specifically for the Edge.</li><li><b>Delete:</b> Remove the Edge and all related data.</li></ul>


<div class="st-gallery"><figure><img src="/images/edge/edge-management/2-instances.webp" alt="The following entities and events can be managed: Make edge public: The edge and all its data will be accessible by others.Assign to customer: Link a specific customer entity to the Edge instance.Make edge private: The edge and all its data will not be accessible by others.Manage assets: Monitor and control assets (e.g., buildings, equipment, or other entities) at the Edge. Manage devices: Administer devices that are managed by the Edge.Manage entity views: Manage filtered views of entities (e.g., devices or assets) at the Edge to display specific subsets of data or contextual information. Read more about the Entity views in this article.Manage dashboards: Customize, and manage dashboards at the Edge.Manage rule chains: Create, configure, and manage rule chains specifically for the Edge.Delete: Remove the Edge and all related data." loading="lazy"><figcaption>The following <a href="/docs/pe/user-guide/entities-and-relations/" target="_blank">entities</a> and events can be managed: <ul><li><b>Make edge public:</b> The edge and all its data will be accessible by others.</li><li><b>Assign to customer:</b> Link a specific customer entity to the Edge instance.</li><li><b>Make edge private:</b> The edge and all its data will not be accessible by others.</li><li><b>Manage assets:</b> Monitor and control assets (e.g., buildings, equipment, or other entities) at the Edge. </li><li><b>Manage devices:</b> Administer devices that are managed by the Edge.</li><li><b>Manage entity views:</b> Manage filtered views of entities (e.g., devices or assets) at the Edge to display specific subsets of data or contextual information. Read more about the Entity views in <a href="/docs/user-guide/entity-views/" target="_blank">this article</a>.</li><li><b>Manage dashboards:</b> Customize, and manage dashboards at the Edge.</li><li><b>Manage rule chains:</b> Create, configure, and manage rule chains specifically for the Edge.</li><li><b>Delete:</b> Remove the Edge and all related data.</li></ul></figcaption></figure></div>


Once an entity has been assigned to a specific **Edge**, it will be pushed to the **Edge event queue**. 
If the **connection** between the Edge and the Cloud is **active**, the assigned entity will be created on the Edge **instantly**. 
If the Edge instance is **not connected** to the **Cloud**, the entity will be created **once the connection is established**.

### Edge Details

Additional information about the Edge and the latest events can be found on the **"Edge Details"** page.
Go the **Edge management > Instances** section and click on the Edge: 
* The **"Details"** tab contains general information, such as **Edge ID**, **Edge key** and **Edge secret**. You also can **assign entities** and **force synchronization** on this tab.
* The **"Attributes"** tab displays the latest attributes published to the server. 
* The **"Latest telemetry"** tab displays the most recent telemetry records from your Edge.
* The **"Alarms"** tab displays the list of alarms.
* The **"Events"** tab displays various events related to the Edge. 
* The **"Downlinks"** tab displays the list of messages transferred from the Cloud to the Edge.
* The **"Relations"** tab displays the records of other entities connected to the Edge.
* The **"Audit logs"** tab displays audit records to track user actions.


<div class="st-gallery"><figure><img src="/images/edge/edge-management/3-edge-details.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Edge Status Page

Basic information about the Edge configuration is provided on the Edge instance itself. To view this information, log in to your **Edge instance** and go to the **Edge > Status** section


1. <b>Status:</b> Edge current status (Connected, Disconnected).<li><b>Name:</b> The name of the current Edge instance.</li><li><b>ID:</b> The identification code of the current Edge instance.</li><li><b>Type:</b> The "default" Edge type is by design.</li><li><b>Routing Key:</b> The Edge key used to install the instance.</li><li><b>Last time connected to/disconnected from cloud:</b> The date and time the instance is connected to/disconnected from Cloud. Displayed in a format YYYY-MM-DD H:Min:Sec.</li>


<div class="st-gallery"><figure><img src="/images/edge/edge-management/4-edge-status.webp" alt="Status: Edge current status (Connected, Disconnected).Name: The name of the current Edge instance.ID: The identification code of the current Edge instance.Type: The &quot;default&quot; Edge type is by design.Routing Key: The Edge key used to install the instance.Last time connected to/disconnected from cloud: The date and time the instance is connected to/disconnected from Cloud. Displayed in a format YYYY-MM-DD H:Min:Sec." loading="lazy"><figcaption><b>Status:</b> Edge current status (Connected, Disconnected).<li><b>Name:</b> The name of the current Edge instance.</li><li><b>ID:</b> The identification code of the current Edge instance.</li><li><b>Type:</b> The "default" Edge type is by design.</li><li><b>Routing Key:</b> The Edge key used to install the instance.</li><li><b>Last time connected to/disconnected from cloud:</b> The date and time the instance is connected to/disconnected from Cloud. Displayed in a format YYYY-MM-DD H:Min:Sec.</li></figcaption></figure></div>


### Cloud Events

The **Cloud Events** page shows events that SENTIENT Edge pushes to the Cloud. To view this information, log in to your **Edge instance** and go to the **Edge > Cloud events** section. The following information is displayed:

* **Created time:** The date and time the event is created and pushed to the Cloud. Displayed in a format YYYY-MM-DD H:Min:Sec.
* **Action:** The action pushed to the Cloud. Possible actions: Added, Deleted, Updated, Attributes Updated, Attributes Deleted, Timeseries Deleted, Timeseries Updated, RPC Call, Credentials Updated, Relation Add or Update, Relation Deleted, Relations Deleted, Alarm Ack, Alarm Clear, Attributes Request, Rule Chain Metadata Request, Relation Request, Credential Request.
* **Entity type:** The entity that created the event.
* **Entity ID:** The identification code of the entity.
* **Status:** Defines if the event has been pushed to the Cloud. 
  * **Deployed:** The event was pushed to the SENTIENT server.
  * **Pending:** The event is created on the SENTIENT Edge, stored to the local database and will be pushed to the Cloud as soon as connection is restored.
* **Data:** Click to view the detailed information that was pushed to the Cloud.


<div class="st-gallery"><figure><img src="/images/edge/edge-management/5-cloud-events.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


By default, events are displayed for the last day. To set a different time period, click the **"Time window"** button at the top of the page.

## Next Steps
