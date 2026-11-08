+++
title = "What is SENTIENT Edge?"
description = "SENTIENT Edge features, FAQ"
aliases = ["/docs/user-guide/edge-computing/"]

[extra]
status = "imported"
checked = ""
source = "docs/edge/getting-started-guides/what-is-edge.md"
+++
<div class="st-callout info">


SENTIENT is an open-source IoT platform that provides a robust suite of features for data collection, processing, visualization, and device management.
If you are a new platform user, we suggest reading [**What is SENTIENT?**](/docs/getting-started-guides/what-is-sentient/) before proceeding with SENTIENT Edge.  


</div>


**SENTIENT Edge** is a robust software product by SENTIENT, designed to leverage edge computing.


With SENTIENT Edge, data analysis and management is brought to the edge, where data generation happens. 
It synchronizes effortlessly with SENTIENT according to your business requirements.

SENTIENT Edge CE is designed for a **single** tenant and/or **single** customer. 
Sharing SENTIENT Edge between multiple tenants or customers is not feasible, and devices from different tenants or customers cannot be connected to a single SENTIENT Edge.
In such cases, multiple SENTIENT Edge instances need to be provisioned for each tenant or customer.


<div class="st-callout info">


Looking for **white-labeling** or **premium features**? <a href="/docs/" target="_blank">Explore Edge Professional Edition documentation →</a>


</div>


<br>

{{ diagram(name="edge-overview") }}

## Use-Cases for SENTIENT Edge

- **Autonomous Vehicles**
  Edge computing allows for the collection, processing, and response to road events with minimal latency. Modern autonomous vehicles generate enormous amounts of data - ranging from 5 TB to 20 TB per day. 4G or 5G networks might not be able to handle such high throughput, but SENTIENT Edge can filter this data, processing most of it locally, and only pushing a subset of this data to the cloud.

- **Smart Farming**
  Rapidly respond to failures of silo aeration systems at remote sites, even if the cloud connectivity from the on-field location is currently weak.

- **Smart Houses**
  Processing and analyzing data closer to smart houses allows for enhanced security of sensitive user information. The low latency of smart house solutions results in a better user experience, with quicker responses from end devices compared to the time it takes for edge devices to connect to the cloud for decision-making.

- **Security Solutions**
  Responding to security violations and threats in a matter of seconds is a necessity. Edge computing provides this capability, making the quality of your connectivity to the cloud irrelevant - decisions will be made by the local edge engine on a remote site in real-time.

- **In-Hospital Monitoring**
  For data privacy in healthcare devices, data processing must occur at the edge. Only necessary pieces of readings from medical devices are pushed to the cloud, while all other sensitive data is stored on the edge. An additional benefit of edge processing in this scenario is the ability to react to critical medical cases as quickly as possible due to real-time processing of data from edge medical devices.

- **Predictive Maintenance**
  Processing and storing data from edge devices closer to the equipment enables analysis of vast amounts of data locally. This allows detection of changes in production lines before a failure occurs, with only average readings from production lines being sent to the cloud, according to your business needs.

## Features of SENTIENT Edge

With **SENTIENT Edge**, you get:

- **Local deployment and storage**: Process and store data from local (edge) devices without connecting to the cloud. Push updates to the cloud once the connection is restored.

{{ diagram(name="edge-offline") }}

- **Traffic filtering**: Filter data from local (edge) devices on the SENTIENT Edge service and push only a subset of the data to the cloud for further processing or storage.

{{ diagram(name="edge-filtering") }}

- **Local alarms**: Instantly respond to critical situations on site, without the need for a cloud connection.

{{ diagram(name="edge-alarm") }}

- **Real-time dashboards**: Monitor local events and time series data.
- **Local storage**: Store data from edge devices on the edge if the cloud connection is inactive and push updates to the cloud once the connection is restored.
- **Batch Update**: Update thousands of edge configurations with a single click.

{{ diagram(name="edge-dashboards") }}

SENTIENT Edge inherits features from SENTIENT, providing the same experience for connecting, managing, and processing data from your devices.

It supports the following **SENTIENT** features:
* [**Attributes**](/docs/user-guide/attributes/) - Assign and manage custom attributes to your entities.
* [**Telemetry**](/docs/user-guide/telemetry/) - API for collecting time series data from your devices.
* [**Entities and relations**](/docs/user-guide/entities-and-relations/) - Model physical world objects (e.g., devices and assets) and the relationships between them.
* [**Data visualization**](/docs/guides/#AnchorIDDataVisualization) - Develop custom dashboards and widgets.
* [**Rule engine**](/docs/user-guide/rule-engine-2-0/re-getting-started/) - Manage data processing & actions on incoming telemetry and events.
* [**RPC**](/docs/user-guide/rpc/) - Send remote procedure calls (RPC) **from both edge and cloud sides** to devices, and vice versa.
* [**Audit log**](/docs/user-guide/audit-log/) - Track user activity.
* [**API Limits**](/docs/user-guide/api-limits/) - Control and limit the number of API requests from a single host.


## Project Roadmap

<p><a href="/docs/edge/roadmap" class="button">SENTIENT Edge Roadmap</a></p>

## Next Steps

<p><a href="/docs/edge/getting-started" class="button">Getting Started Guide</a></p>
