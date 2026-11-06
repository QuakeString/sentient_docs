+++
title = "Devices"
description = "SENTIENT IoT Device management"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/devices.md"
+++
**Devices** are fundamental IoT entities in SENTIENT that can **generate telemetry data** (such as temperature, humidity, GPS coordinates, etc.) and **transmit** it to the SENTIENT platform, as well as respond to Remote Procedure Call (RPC) commands.
Devices can be either physical (e.g., sensors, controllers, trackers) or virtual (e.g., emulators) network-connected objects that are capable of:
- **Generating telemetry data** — send measured data such as temperature, humidity, or location.
- **Transmitting data to the SENTIENT platform** via [supported protocols](/docs/reference/protocols/) (MQTT, HTTP, CoAP, etc.).
- **Responding to RPC commands** — receiving and executing on remote procedure calls sent from the platform.

Each device:
- is stored as a separate **entity**.
- has a device profile that defines type, transport settings, firmware, alarm rules, etc.
- can be assigned an [owner](/docs/user-guide/ui/devices/#manage-owner-and-groups).
- supports both [attributes](/docs/user-guide/attributes/) (static or semi-static properties) and [telemetry](/docs/user-guide/telemetry/) (time-series data).

> SENTIENT supports device management functions via both the web UI and the [REST API](/docs/reference/rest-api/).

<b><font size="4">Practical video course 🎥</font></b>

Explore a hands-on video course that provides detailed explanations on how to create and manage devices in SENTIENT.

> The course includes practical examples to help you better understand how to work with dashboards, resources, and devices, including their configuration and real-world usage.


<div id="video">  
    <div id="video_wrapper">
        <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/65SoFceFDBE" frameborder="0" allowfullscreen></iframe>
    </div>
</div>

<hr>

## How to add, edit, and delete device

Tenant administrators and users with appropriate permissions can create, edit, or delete devices in SENTIENT.

### Adding new device

To add a new device:
- Navigate to **Entities** &#10230; **Devices**. 
- Click the "**+**" icon in the upper-right corner and select "**Add new device**" from drop-down menu.
- In the device creation form, fill in the required fields:
  - **Name** – a unique name for the device.
  - **[Device profile](/docs/user-guide/device-profiles/)** – by default, the profile is set to "**default**", but you can choose a different profile if needed.
- Optional fields such as **Label** or **Description** can be filled in if needed.
- Click "**Add**".

Device successfully created and is now available in the list.

A window will immediately open where you can [check the device's connection to SENTIENT platform](#check-connectivity).
This step is optional. For now, let's close this window and return to the connection check in more detail later.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-1-ce.webp" alt="Login to your SENTIENT instance. Navigate to &quot;Entities&quot; &#8702; &quot;Devices&quot;." loading="lazy"><figcaption>Login to your SENTIENT instance. Navigate to "<b>Entities</b>" &#8702; "<b>Devices</b>".</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-2-ce.webp" alt="Click the &quot;+&quot; icon in the upper-right corner and select &quot;Add new device&quot; from drop-down menu." loading="lazy"><figcaption>Click the "<b>+</b>" icon in the upper-right corner and select "<b>Add new device</b>" from drop-down menu.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-3-ce.webp" alt="In the device creation form, fill in the required fields: Name – a unique name for the device; Device profile – by default, the profile is set to &quot;default&quot;, but you can choose a different profile if needed. Click &quot;Add&quot;." loading="lazy"><figcaption>In the device creation form, fill in the required fields: <b>Name</b> – a unique name for the device; <b>Device profile</b> – by default, the profile is set to "<b>default</b>", but you can choose a different profile if needed. Click "<b>Add</b>".</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-4-ce.webp" alt="A window will immediately open where you can check the device&#39;s connection to SENTIENT platform. This step is optional. For now, let&#39;s close this window and return to the connection check in more detail later." loading="lazy"><figcaption>A window will immediately open where you can check the device&#39;s connection to SENTIENT platform. This step is optional. For now, let&#39;s close this window and return to the connection check in more detail later.</figcaption></figure><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-5-ce.webp" alt="Device successfully created and is now available in the list." loading="lazy"><figcaption>Device successfully created and is now available in the list.</figcaption></figure></div>


You&#39;ll also receive a [notification](/docs/user-guide/notifications/) (bell icon) indicating the device was added.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-ce/hello-world-1-1-provision-device-6-ce.webp" alt="You&#39;ll also receive a notification (bell icon) indicating the device was added." loading="lazy"><figcaption>You&#39;ll also receive a notification (bell icon) indicating the device was added.</figcaption></figure></div>


<hr>


### Edit device

You can change the device name, its device profile, label, assign the firmware and software.
To edit the device, you need to:


1. In the devices list, locate and click on the desired asset, then click the "<b>pencil</b>" (✏️ <b>Edit</b>) icon on the right to open the edit form.

1. Make the necessary changes and click the "<b>Apply changes</b>" button to save them.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/devices/ce/device-details-1-ce.webp" alt="In the devices list, locate and click on the desired asset, then click the &quot;pencil&quot; (✏️ Edit) icon on the right to open the edit form." loading="lazy"><figcaption>In the devices list, locate and click on the desired asset, then click the "<b>pencil</b>" (✏️ <b>Edit</b>) icon on the right to open the edit form.</figcaption></figure><figure><img src="/images/user-guide/ui/devices/ce/device-details-2-ce.webp" alt="Make the necessary changes and click the &quot;Apply changes&quot; button to save them." loading="lazy"><figcaption>Make the necessary changes and click the "<b>Apply changes</b>" button to save them.</figcaption></figure></div>


<hr>

### Delete device

You can delete a device using one of the following ways:

First way:


1. Click on the "<b>trash can</b>" icon can opposite the device&#39;s name you want to delete.

1. Confirm deleting the device in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/devices/ce/device-delete-1-ce.webp" alt="Click on the &quot;trash can&quot; icon can opposite the device&#39;s name you want to delete." loading="lazy"><figcaption>Click on the "<b>trash can</b>" icon can opposite the device&#39;s name you want to delete.</figcaption></figure><figure><img src="/images/user-guide/ui/devices/ce/device-delete-2-ce.webp" alt="Confirm deleting the device in the dialog box." loading="lazy"><figcaption>Confirm deleting the device in the dialog box.</figcaption></figure></div>


Second way:


1. Click on the device that you want to delete. In the device details window, click the "<b>Delete device</b>" button;

1. Confirm deleting the device in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/devices/ce/device-delete-3-ce.webp" alt="Click on the device that you want to delete. In the device details window, click the &quot;Delete device&quot; button;" loading="lazy"><figcaption>Click on the device that you want to delete. In the device details window, click the "<b>Delete device</b>" button;</figcaption></figure><figure><img src="/images/user-guide/ui/devices/ce/device-delete-4-ce.webp" alt="Confirm deleting the device in the dialog box." loading="lazy"><figcaption>Confirm deleting the device in the dialog box.</figcaption></figure></div>


## Check connectivity

**Check connectivity** is a built-in feature that provides ready-to-use commands for testing device connectivity to SENTIENT using different communication protocols. It allows you to quickly verify network access, validate credentials, and confirm that incoming telemetry is processed correctly.

Using this feature, you can publish test telemetry data (for example, a temperature value of 25) and immediately ensure that the device is able to communicate with the platform.

**To verify device connectivity:**
1. Click on device to open its details page. 
2. Click **Check connectivity**. 
3. Select the [communication protocol](/docs/reference/protocols/) ([MQTT](/docs/reference/mqtt-api), [HTTP](/docs/reference/http-api), etc.) and your operating system. 
4. Copy the generated command and execute it in a terminal.

If the connection is successful:
- The device status changes from **Inactive** to **Active**.
- Telemetry data appears on the **Latest telemetry** tab.


<div class="st-callout info">


For guidance on connecting devices based on your technology stack, see the available [connection guides](/docs/guides/#AnchorIDGettingStartedGuides).<br>
For advanced protocols and API options, refer to the [SENTIENT API reference](/docs/reference/protocols/).


</div>


<div class="st-gallery"><figure><img src="/images/user-guide/ui/devices/ce/check-connectivity-1-ce.webp" alt="Open the &quot;Device details&quot; window and click &quot;Check connectivity&quot;" loading="lazy"><figcaption>Open the "<b>Device details</b>" window and click "<b>Check connectivity</b>"</figcaption></figure><figure><img src="/images/user-guide/ui/devices/ce/check-connectivity-2-ce.webp" alt="Select the communication protocol (MQTT, HTTP, etc.) and your operating system, then copy the command." loading="lazy"><figcaption>Select the communication protocol (MQTT, HTTP, etc.) and your operating system, then copy the command.</figcaption></figure><figure><img src="/images/user-guide/ui/devices/ce/check-connectivity-3-ce.webp" alt="Run copied command in a Terminal. The device state should be changed from &quot;Inactive&quot; to &quot;Active&quot; and you should see the published &quot;temperature&quot; readings." loading="lazy"><figcaption>Run copied command in a <b>Terminal</b>. The device state should be changed from "Inactive" to "Active" and you should see the published "temperature" readings.</figcaption></figure></div>


<hr>

## Manage device credentials

Supported credential types:

- [Access Token](/docs/user-guide/access-token/) (default).
- [X.509](/docs/user-guide/certificates/) certificate.
- [MQTT Basic](/docs/user-guide/basic-mqtt/).

To change or manage credentials:


1. Open "<b>Device details</b>" window and click the "<b>Manage credentials</b>" button;

1. Select the desired credential type and generate or enter required fields. Click "<b>Save</b>".


<div class="st-gallery"><figure><img src="/images/user-guide/ui/devices/ce/manage-device-credentials-1-ce.webp" alt="Open &quot;Device details&quot; window and click the &quot;Manage credentials&quot; button;" loading="lazy"><figcaption>Open "<b>Device details</b>" window and click the "<b>Manage credentials</b>" button;</figcaption></figure><figure><img src="/images/user-guide/ui/devices/ce/manage-device-credentials-2-ce.webp" alt="Select the desired credential type and generate or enter required fields. Click &quot;Save&quot;." loading="lazy"><figcaption>Select the desired credential type and generate or enter required fields. Click "<b>Save</b>".</figcaption></figure></div>


<hr>


## Make device public

You can make a device public so that all its data is accessible to everyone. This is ideal for creating public demo dashboards that require access to device data or for open data use cases.


1. Open "Device details" window and click the "Make device public" button;

1. Confirm the action in the dialog box;


<div class="st-gallery"><figure><img src="/images/user-guide/ui/devices/ce/make-device-public-1-ce.webp" alt="Open &quot;Device details&quot; window and click the &quot;Make device public&quot; button;" loading="lazy"><figcaption>Open "Device details" window and click the "Make device public" button;</figcaption></figure><figure><img src="/images/user-guide/ui/devices/ce/make-device-public-2-ce.webp" alt="Confirm the action in the dialog box;" loading="lazy"><figcaption>Confirm the action in the dialog box;</figcaption></figure></div>


To make the device private again, follow these steps:


1. Open "Device details" window and click the "Make device private" button;

1. Confirm the action in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/devices/ce/make-device-public-4-ce.webp" alt="Open &quot;Device details&quot; window and click the &quot;Make device private&quot; button;" loading="lazy"><figcaption>Open "Device details" window and click the "Make device private" button;</figcaption></figure><figure><img src="/images/user-guide/ui/devices/ce/make-device-public-5-ce.webp" alt="Confirm the action in the dialog box." loading="lazy"><figcaption>Confirm the action in the dialog box.</figcaption></figure></div>


> Once the device is made private, it will no longer be publicly accessible, and any **public [dashboards](/docs/user-guide/dashboards/)** referencing it will lose access to its data.

<hr>

## Assign device to customer

You can assign the device to a specific [customer](/docs/user-guide/ui/customers/). This ensures that only users associated with that customer will have access to the device and its data.

> This step is crucial for ensuring data [access control](/docs/administration/roles/). Each customer user will only see their own devices and will not have access to devices or data assigned to other customers.


1. Open "Device details" window and click the "Assign device to customer" button;

1. Select the customer to assign the device. Then click "Assign";

1. The device is assigned to the selected customer.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/devices/ce/assign-device-to-customer-1-ce.webp" alt="Open &quot;Device details&quot; window and click the &quot;Assign device to customer&quot; button;" loading="lazy"><figcaption>Open "Device details" window and click the "Assign device to customer" button;</figcaption></figure><figure><img src="/images/user-guide/ui/devices/ce/assign-device-to-customer-2-ce.webp" alt="Select the customer to assign the device. Then click &quot;Assign&quot;;" loading="lazy"><figcaption>Select the customer to assign the device. Then click "Assign";</figcaption></figure><figure><img src="/images/user-guide/ui/devices/ce/assign-device-to-customer-3-ce.webp" alt="The device is assigned to the selected customer." loading="lazy"><figcaption>The device is assigned to the selected customer.</figcaption></figure></div>


In the SENTIENT Professional Edition (PE), you can assign devices using the [“Manage owner and groups”](https://sentient.invenia.in/docs/pe/user-guide/ui/devices/#manage-device-owner-and-groups) button in the device details. This allows you to not only assign ownership but also manage group memberships at the same time.


<hr>


## Device details

Clicking on the device opens a window where you can access and manage various aspects of that device.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/devices/ce/device-details-page-1-ce.webp" alt="Click on the target device to open its details window." loading="lazy"><figcaption>Click on the target device to open its <b>details window</b>.</figcaption></figure></div>


<b><font size="3">Copy device ID</font></b>   
Allows you to quickly retrieve the device&#39;s unique UUID. Click Copy device Id to copy it to your clipboard. The ID is used in API calls, integrations, and scripts.

<b><font size="3">Copy device credentials</font></b>   
Depending on the authentication type, you can copy:
- **Access Token**
- **MQTT Credentials**

Click the corresponding button to instantly obtain the credentials required for connecting the device to SENTIENT.

<b><font size="3">Attributes</font></b>   

This tab displays client, server, and shared [attributes](/docs/user-guide/attributes/) — static or semi-static key-value pairs associated with the device. Typical examples include serial number, model, and firmware version.

<b><font size="3">Latest telemetry</font></b>   

Shows the [latest telemetry](/docs/user-guide/telemetry/) values sent by the device, including sensor readings, status updates, and other real-time parameters.
- **Adding telemetry:** Click the "**+**" icon, enter the key name, value type, and value.
- **Deleting telemetry:** Click the trash icon, choose the deletion mode (all data, latest value, all except latest, or by time period), and confirm the action.

<b><font size="3">Calculated fields</font></b>   
Displays fields whose values are computed from existing attributes or telemetry using formulas. This allows you to define derived parameters without modifying the device firmware. Learn more about Calculated fields [here](/docs/user-guide/calculated-fields/).

<b><font size="3">Alarm rules</font></b>   
Contains the rules that define how alarms are generated for the device. You can review conditions, thresholds, triggers, and configured alarm actions. Learn more about configuring alarm rules [here](/docs/user-guide/alarm-rules/).

<b><font size="3">Alarms</font></b>    
Shows all active and historical [alarms](/docs/user-guide/alarms/) related to the device. Helps monitor device health, track warnings, and identify critical events.

<b><font size="3">Events</font></b>   
Displays system events associated with the device, including logs, warnings, errors, and other lifecycle-related records. Useful for diagnostics and activity tracking.

<b><font size="3">Relations</font></b>   
Shows all directed [relations](/docs/user-guide/entities-and-relations/#relations) between this device and other entities, such as assets, devices, dashboards, and rule chains. Provides context on how the device fits into the overall system.

<b><font size="3">Audit logs</font></b>   
Provides a record of user actions related to the device — creation, updates, configuration changes, and deletions. Useful for security auditing and traceability.

<b><font size="3">Version control</font></b>   
Enables exporting and restoring SENTIENT entities using the built-in Git-based [version control](/docs/user-guide/version-control/) service. Supports backup, collaboration, and configuration version management.

<hr>

## Next steps


<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please contact us.
