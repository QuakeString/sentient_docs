+++
title = "Edge Device Management"
description = "Seamlessly create Edge devices and assign them to the Cloud"

[extra]
status = "imported"
checked = ""
source = "docs/edge/config/create-device.md"
+++
## Overview

The **Edge Devices** are basic IoT entities that can generate telemetry data and process RPC commands. They are physical objects, such as sensors, actuators, switches, etc. that can collect, process and transmit data locally or to a nearby network, rather than relying solely on a centralised Cloud system.

To better understand **Devices** as entities in the context of the **SENTIENT platform**, please refer to [this documentation](/docs/user-guide/ui/devices/).

## Device Management on Edge Instance

A **Device** entity can be created directly on the **Edge instance** and automatically pushed to the **Cloud (Server)** once a connection is established. Any changes made to the **Device** entity are seamlessly provisioned to the **Cloud (Server)** without requiring additional action, ensuring that updates are synchronized across all **Edge** instances.

Once the **Device** is created on the **Edge instance**, it is also pushed for creation on the **Cloud (Server)**, ensuring consistency and efficient management of the entire system.

## Creating Device on Edge Instance


<div class="st-callout info">


Before you create a **Device**, make sure to create and configure a [Device Profile](/docs/user-guide/device-profiles/).


</div>


You can create and provision **Device** manually, deploy multiple devices from a CSV file with a [Bulk Provisioning](/docs/user-guide/bulk-provisioning/) option, or use the [REST API](/docs/api/) for programmatic deployment.
To create the **Device** manually, follow these instructions:


1. Any <b>Tenant administrator</b> user is able to create <b>Device</b> entities on the <b>Edge instance</b>. Go to the <b>Entities > Devices</b> section and click the <b>"Add new device"</b> button.

1. In the pop-up window, fill in the required <b>Device details</b> fields, such as <b>"Name"</b> and <b>"Device profile"</b>. Confirm the action by clicking the <b>"Add"</b> button.

1. To check connectivity, send telemetry on behalf of the <b>Device</b> using shell by following the on-screen instructions.

1. To check if the new <b>Device</b> has been deployed to the <b>Cloud (Server)</b>, log in to your <b>Cloud (Server)</b> and navigate to the <b>Entities > Devices</b> section: the newly created <b>Device</b> will be automatically assigned to the <b>Cloud (Server)</b>.


<div class="st-gallery"><figure><img src="/images/edge/config/devices/0-go-to-devices-section.webp" alt="Any Tenant administrator user is able to create Device entities on the Edge instance. Go to the Entities > Devices section and click the &quot;Add new device&quot; button." loading="lazy"><figcaption>Any <b>Tenant administrator</b> user is able to create <b>Device</b> entities on the <b>Edge instance</b>. Go to the <b>Entities > Devices</b> section and click the <b>"Add new device"</b> button.</figcaption></figure><figure><img src="/images/edge/config/devices/1-add-new-device.webp" alt="In the pop-up window, fill in the required Device details fields, such as &quot;Name&quot; and &quot;Device profile&quot;. Confirm the action by clicking the &quot;Add&quot; button." loading="lazy"><figcaption>In the pop-up window, fill in the required <b>Device details</b> fields, such as <b>"Name"</b> and <b>"Device profile"</b>. Confirm the action by clicking the <b>"Add"</b> button.</figcaption></figure><figure><img src="/images/edge/config/devices/2-check-connectivity.webp" alt="To check connectivity, send telemetry on behalf of the Device using shell by following the on-screen instructions." loading="lazy"><figcaption>To check connectivity, send telemetry on behalf of the <b>Device</b> using shell by following the on-screen instructions.</figcaption></figure><figure><img src="/images/edge/config/devices/3-confirm-on-cloud.webp" alt="To check if the new Device has been deployed to the Cloud (Server), log in to your Cloud (Server) and navigate to the Entities > Devices section: the newly created Device will be automatically assigned to the Cloud (Server)." loading="lazy"><figcaption>To check if the new <b>Device</b> has been deployed to the <b>Cloud (Server)</b>, log in to your <b>Cloud (Server)</b> and navigate to the <b>Entities > Devices</b> section: the newly created <b>Device</b> will be automatically assigned to the <b>Cloud (Server)</b>.</figcaption></figure></div>


## Assigning Devices from Cloud to Edge

**Devices** can be created on **Cloud (Server)** and then provisioned to the **Edge instance**. 
Log in to your **Server (Cloud)** and go to the **Edge management > Instances** section.


1. The variety of buttons on the <b>"Instances"</b> page will help you to manage different <a href="/docs/user-guide/entities-and-relations/" target="_blank">entities</a>, and assign them accordingly to the <b>Edge instance</b>. To assign a <b>Device</b>, click the <b>"Manage devices"</b> button.

1. On the <b>"Edge devices"</b> page, click the <b>"+"</b> icon and then select the <b>Device(s)</b> from the drop-down list in the pop-up window. Confirm the action by clicking the <b>"Assign"</b> button.

1. To confirm that the <b>Device</b> has been assigned to the <b>Edge instance</b>, log in to your <b>Edge instance</b> and go to the  <b>Entities > Devices</b> section.


<div class="st-gallery"><figure><img src="/images/edge/config/devices/0-assignment-from-cloud.webp" alt="The variety of buttons on the &quot;Instances&quot; page will help you to manage different entities, and assign them accordingly to the Edge instance. To assign a Device, click the &quot;Manage devices&quot; button." loading="lazy"><figcaption>The variety of buttons on the <b>"Instances"</b> page will help you to manage different <a href="/docs/user-guide/entities-and-relations/" target="_blank">entities</a>, and assign them accordingly to the <b>Edge instance</b>. To assign a <b>Device</b>, click the <b>"Manage devices"</b> button.</figcaption></figure><figure><img src="/images/edge/config/devices/1-assign-devices-from-cloud.webp" alt="On the &quot;Edge devices&quot; page, click the &quot;+&quot; icon and then select the Device(s) from the drop-down list in the pop-up window. Confirm the action by clicking the &quot;Assign&quot; button." loading="lazy"><figcaption>On the <b>"Edge devices"</b> page, click the <b>"+"</b> icon and then select the <b>Device(s)</b> from the drop-down list in the pop-up window. Confirm the action by clicking the <b>"Assign"</b> button.</figcaption></figure><figure><img src="/images/edge/config/devices/2-confirm-on-edge.webp" alt="To confirm that the Device has been assigned to the Edge instance, log in to your Edge instance and go to the  Entities > Devices section." loading="lazy"><figcaption>To confirm that the <b>Device</b> has been assigned to the <b>Edge instance</b>, log in to your <b>Edge instance</b> and go to the  <b>Entities > Devices</b> section.</figcaption></figure></div>


## Next Steps
