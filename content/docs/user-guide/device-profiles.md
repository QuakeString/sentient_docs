+++
title = "Device profiles"
description = "IoT device profiles"
aliases = ["/docs/user-guide/ui/device-profiles"]

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/device-profiles.md"
+++
<table style="width:auto">
   <thead>
     <tr>
	 <td style="text-align: center"><strong><em>Available since TB Version 3.2</em></strong></td>
     </tr>
   </thead>
</table> 


Device profiles in SENTIENT allows an administrator to define and centrally manage common settings for multiple devices at once.   
This greatly simplifies the management of a large number of similar devices, making it especially valuable in IoT solutions where numerous devices share identical configurations and behaviors.

Typical device profile settings include:
- Setting a default [rule chain](#default-rule-chain).
- Configuring message [queue](#queue) for efficient message handling.
- Defining **firmware** and **software** versions to be distributed automatically to devices.
- Configuring [transport protocols](#transport-configuration) used for device communication.
- Defining and managing [alarm rules](/docs/user-guide/alarm-rules/).
- Setting the [provision strategy](/docs/user-guide/device-provisioning/).

## Create device profile

To create a new device profile:
- Go to the "**Device profiles**" page in the "Profiles" section.
- Click the "**+**" icon in the upper-right corner and select "**Create new device profile**" from the dropdown menu.
- Only the **Name** field is required; all other settings are optional.
- Click "**Add**" to create the device profile.


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/create-device-profile-1-ce.webp" alt="Go to the &quot;Device profiles&quot; page in the &quot;Profiles&quot; section. Click the &quot;+&quot; icon in the upper-right corner and select &quot;Create new device profile&quot; from the dropdown menu." loading="lazy"><figcaption>Go to the "<b>Device profiles</b>" page in the "<b>Profiles</b>" section. Click the "<b>+</b>" icon in the upper-right corner and select "<b>Create new device profile</b>" from the dropdown menu.</figcaption></figure><figure><img src="/images/user-guide/device-profile/create-device-profile-2-ce.webp" alt="Only the Name field is required; all other settings are optional. Click &quot;Add&quot; to create the device profile." loading="lazy"><figcaption>Only the <b>Name</b> field is required; all other settings are optional. Click "<b>Add</b>" to create the device profile.</figcaption></figure></div>


## Main device profile configuration

### Default rule chain

The Default [Rule Chain](/docs/user-guide/rule-engine-2-0/overview/#rule-chain) processes all incoming messages and events from any device. As the number of device types grows, the default rule chain can become complex and difficult to manage. 
Often, users create their own root rule chains to route messages to specialized rule chains based on device type.

To simplify this process, you can assign separate rule chains to individual device profiles. 
This allows you to centrally and flexibly manage telemetry processing, device state (active/inactive), and device lifecycle events (creation, update, deletion).


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/device-profile-rule-chain-1-ce.webp" alt="You can simplify the processing of incoming messages and events from any device by assigning separate rule chains to device profiles based on device type, instead of using the default rule chain." loading="lazy"><figcaption>You can simplify the processing of incoming messages and events from any device by assigning separate rule chains to device profiles based on device type, instead of using the default rule chain.</figcaption></figure></div>


### Queue

By default, the **main** [queue](/docs/user-guide/rule-engine-2-5/queues/) will be used to store all incoming messages and events from any device.
The transport layer will submit messages to this queue and Rule Engine will poll the queue for new messages.
However, for multiple use cases, you might want to use different queues for different devices. 
For example, you might want to isolate data processing for Fire Alarm/Smoke Detector sensors and other devices.
This way, even if your system has a peak load produced by millions of water meters, whenever the Fire Alarm is reported, it will be processed without delay.
Separation of the queues also allows you to customize different [submit](/docs/user-guide/rule-engine-2-5/queues/#submit-settings) and [processing](/docs/user-guide/rule-engine-2-5/queues/#retries-processing-settings) strategies.

> **Please note:** if you choose to use a custom queue, you should configure it with the **system administrator** before you using it.


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/device-profile-queue-1-ce.webp" alt="Using separate queues for different device types allows isolated and prioritized processing, ensuring critical events like fire alarms are handled promptly despite high system load." loading="lazy"><figcaption>Using separate queues for different device types allows isolated and prioritized processing, ensuring critical events like fire alarms are handled promptly despite high system load.</figcaption></figure></div>


## Transport configuration

The current version of SENTIENT platform supports the following transport types: 
- [Default](#default-transport-type) - standard HTTP transport suitable for basic device interactions with SENTIENT. Easy to configure, but less efficient for a large number of devices or frequent updates.
- [MQTT](#mqtt-transport-type) -  lightweight, bidirectional protocol specifically optimized for IoT devices, providing efficient telemetry delivery, high throughput, and resource efficiency.
- [CoAP](#coap-transport-type) - lightweight IoT protocol ideal for resource-constrained devices operating in low-bandwidth networks.
- [LWM2M](/docs/reference/lwm2m-api/#step-2-define-lwm2m-device-profile) - standardized IoT protocol designed for efficient management of resource-constrained devices, enabling centralized configuration management, firmware updates, and device monitoring.
- [SNMP](/docs/reference/snmp-api/#device-profile-configuring) - widely used protocol for managing network devices like routers, switches, servers, enabling collection and analysis of device health information.


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/device-profile-transport-1-ce.webp" alt="The current version of SENTIENT platform supports the following transport types: Default, MQTT, CoAP, LWM2M, SNMP." loading="lazy"><figcaption>The current version of SENTIENT platform supports the following transport types: <b>Default, MQTT, CoAP, LWM2M, SNMP</b>.</figcaption></figure></div>


### Default transport type

The **Default** transport type is designed to ensure compatibility with earlier versions of the platform.
Devices using this type can connect through SENTIENT&#39;s standard APIs: [MQTT](/docs/reference/mqtt-api/), [HTTP](/docs/reference/http-api/), and [CoAP](/docs/reference/coap-api/).
It requires no special configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/default-transport-type-1-ce.webp" alt="The Default transport type is designed to ensure compatibility with earlier versions of the platform. Devices using this type can connect through SENTIENT&#39;s standard APIs: MQTT, HTTP, and CoAP. It requires no special configuration." loading="lazy"><figcaption>The <b>Default</b> transport type is designed to ensure compatibility with earlier versions of the platform. Devices using this type can connect through SENTIENT&#39;s standard APIs: <b>MQTT</b>, <b>HTTP</b>, and <b>CoAP</b>. It requires no special configuration.</figcaption></figure></div>


### MQTT transport type

The **MQTT** transport type allows for flexible communication setup with devices using the MQTT protocol.
You can define custom **MQTT topic filters** for sending telemetry and updating attributes by using SENTIENT&#39;s [telemetry upload API](/docs/reference/mqtt-api/#telemetry-upload-api) and [attribute update API](/docs/reference/mqtt-api/#publish-attribute-update-to-the-server).

The MQTT transport type has the following settings:

<br><b><font size="4">MQTT device topic filters</font></b>

Custom MQTT topic filters support **single-level (`+`)** and **multi-level (`#`) wildcards**, making it possible to connect to almost any **MQTT-based device** that sends payloads in **JSON** or **Protobuf** format.


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/mqtt-device-topic-filters-1-ce.webp" alt="Custom MQTT topic filters support single-level (+) and multi-level (#) wildcards, making it possible to connect to almost any MQTT-based device that sends payloads in JSON or Protobuf format." loading="lazy"><figcaption>Custom MQTT topic filters support <b>single-level (+)</b> and <b>multi-level (#) wildcards</b>, making it possible to connect to almost any <b>MQTT-based device</b> that sends payloads in <b>JSON</b> or <b>Protobuf</b> format.</figcaption></figure></div>


<br>
Let&#39;s look at an example where we use custom MQTT topic filters to publish time-series data using "MQTT Basic" device credentials:

- Specify custom MQTT topic filters in the device profile. For example:
  - Telemetry topic filter: `/telemetry`
  - Attributes topic filter: `/attributes`
- Configure MQTT basic credentials for your device:
  - Client ID: `c1`
  - Username: `t1`
  - Password: `secret`

Publish time-series data using the following command:


> Don&#39;t forget to replace `$SENTIENT_HOST_NAME` with your actual host name.

```bash
mosquitto_pub -h $SENTIENT_HOST_NAME -t /telemetry -i "c1" -u "t1" -P "secret" -m "{humidity:10.3}"
```


Transmitted data will be displayed in the "**Latest telemetry**" tab of the device.


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/mqtt-transport-example-1-ce.webp" alt="Specify custom MQTT device topic filters in the device profile." loading="lazy"><figcaption>Specify custom <b>MQTT device topic filters</b> in the device profile.</figcaption></figure><figure><img src="/images/user-guide/device-profile/mqtt-transport-example-2-ce.webp" alt="Click the &quot;Manage credentials&quot; button in your device details." loading="lazy"><figcaption>Click the "<b>Manage credentials</b>" button in your device details.</figcaption></figure><figure><img src="/images/user-guide/device-profile/mqtt-transport-example-3-ce.webp" alt="Provide basic MQTT credentials for your device with the client id &#39;c1&#39;, username &#39;t1&#39; and password &#39;secret&#39;." loading="lazy"><figcaption><b>Provide basic MQTT credentials</b> for your device with the client id &#39;c1&#39;, username &#39;t1&#39; and password &#39;secret&#39;.</figcaption></figure><figure><img src="/images/user-guide/device-profile/mqtt-transport-example-4-ce.webp" alt="Use Terminal to publish time-series data. Transmitted data will be displayed in the &quot;Latest telemetry&quot; tab of the device." loading="lazy"><figcaption>Use <b>Terminal</b> to publish time-series data. Transmitted data will be displayed in the <b>"Latest telemetry" tab</b> of the device.</figcaption></figure></div>


<br>
If you use the standard MQTT device topic filters configuration, you can publish time series and attributes using the commands below.

> Don&#39;t forget to replace `$SENTIENT_HOST_NAME` with your actual host name.

Command for publish **timeseries data**:


```bash
mosquitto_pub -h $SENTIENT_HOST_NAME -t v1/devices/me/telemetry -i "c1" -u "t1" -P "secret" -m "{humidity:10.3}"
```


Command for update **attributes**:

```bash
mosquitto_pub -h $SENTIENT_HOST_NAME -t v1/devices/me/attributes -i "c1" -u "t1" -P "secret" -m "{"firmwareVersion": "1.3"}"
```


<br><b><font size="4">MQTT device payload</font></b>

- **JSON**. By default, SENTIENT expects devices to send data in JSON format. However, it is also possible to transmit data using [Protocol Buffers](https://developers.google.com/protocol-buffers) (Protobuf).
- **Protocol Buffers (Protobuf)** is a language- and a platform-neutral way of serializing structured data. It is convenient to minimize the size of transmitted data.   
The current version of the SENTIENT platform supports customizable proto schemas for [telemetry upload](/docs/reference/mqtt-api/#telemetry-upload-api) and [attribute upload](/docs/reference/mqtt-api/#publish-attribute-update-to-the-server) and implemented the ability to define a schema for downlink messages (RPC calls). 
> SENTIENT parses the protobuf structures dynamically, that is why, it does not support some protobuf features like OneOf, extensions and maps, yet.


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/mqtt-device-payload-1-ce.webp" alt="Go to the &quot;Device profiles&quot; page in the &quot;Profiles&quot; section. Click the &quot;+&quot; icon in the upper-right corner and select &quot;Create new device profile&quot; from the dropdown menu." loading="lazy"><figcaption>Go to the "Device profiles" page in the "Profiles" section. Click the "+" icon in the upper-right corner and select "Create new device profile" from the dropdown menu.</figcaption></figure><figure><img src="/images/user-guide/device-profile/mqtt-device-payload-2-ce.webp" alt="Go to the &quot;Device profiles&quot; page in the &quot;Profiles&quot; section. Click the &quot;+&quot; icon in the upper-right corner and select &quot;Create new device profile&quot; from the dropdown menu." loading="lazy"><figcaption>Go to the "Device profiles" page in the "Profiles" section. Click the "+" icon in the upper-right corner and select "Create new device profile" from the dropdown menu.</figcaption></figure></div>


- **Compatibility with other payload formats** option.   
When compatibility mode is enabled, SENTIENT will default to using a Protobuf payload format. If parsing the Protobuf payload fails, SENTIENT will automatically attempt to use the JSON payload format. This feature is particularly useful for ensuring backward compatibility during firmware updates. For example, an initial firmware release might use JSON, while a new release switches to Protobuf. During firmware updates across multiple devices, supporting both formats simultaneously is essential.   
> It is important to note that enabling compatibility mode can introduce slight performance degradation. Therefore, it is recommended to disable compatibility mode once all devices have been successfully updated.


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/mqtt-device-payload-3-ce.webp" alt="Go to the &quot;Device profiles&quot; page in the &quot;Profiles&quot; section. Click the &quot;+&quot; icon in the upper-right corner and select &quot;Create new device profile&quot; from the dropdown menu." loading="lazy"><figcaption>Go to the "Device profiles" page in the "Profiles" section. Click the "+" icon in the upper-right corner and select "Create new device profile" from the dropdown menu.</figcaption></figure></div>


### CoAP transport type

**CoAP (Constrained Application Protocol)** is a lightweight IoT protocol specifically designed for resource-constrained devices operating in low-bandwidth networks.

<b><font size="3">CoAP device type:</font></b>

- **Default**. The default CoAP device type uses a JSON payload. This supports basic [CoAP APIs](/docs/reference/coap-api/) similar to the [default transport type](#default-transport-type).    
You can also configure devices to transmit data using [Protocol Buffers](https://developers.google.com/protocol-buffers) (Protobuf) by changing the **CoAP device payload** setting to **Protobuf**.

    - **Protocol Buffers (Protobuf)** is a language- and platform-neutral method of serializing structured data, designed primarily to reduce the size of transmitted data.   
  The current version of the SENTIENT platform supports customizable proto schemas for [telemetry upload](/docs/reference/coap-api/#telemetry-upload-api) and [attribute upload](/docs/reference/coap-api/#publish-attribute-update-to-the-server) and implemented the ability to define a schema for downlink messages (RPC calls).
  SENTIENT parses the protobuf structures dynamically, that is why, it does not support some protobuf features like OneOf, extensions and maps, yet.


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/coap-default-1-ce.webp" alt="The default CoAP device type uses a JSON payload. This supports basic CoAP APIs similar to the default transport type. You can also configure devices to transmit data using Protocol Buffers (Protobuf) by changing the CoAP device payload setting to Protobuf." loading="lazy"><figcaption>The default CoAP device type uses a JSON payload. This supports basic CoAP APIs similar to the default transport type. You can also configure devices to transmit data using Protocol Buffers (Protobuf) by changing the CoAP device payload setting to Protobuf.</figcaption></figure><figure><img src="/images/user-guide/device-profile/coap-default-2-ce.webp" alt="Protocol Buffers (Protobuf) is a language- and platform-neutral method of serializing structured data, designed primarily to reduce the size of transmitted data." loading="lazy"><figcaption>Protocol Buffers (Protobuf) is a language- and platform-neutral method of serializing structured data, designed primarily to reduce the size of transmitted data.</figcaption></figure></div>


- **Efento NB-IoT** devices are wireless sensors that use NB-IoT technology for energy-efficient transmission of telemetry data (e.g., temperature, humidity, pressure, open/close, leakage, and more). 
You can integrate them with SENTIENT using the built-in CoAP transport, which receives messages from the devices, decodes them using Protobuf, and stores telemetry data on the platform.
This data becomes instantly available for viewing, charting, dashboarding, alarm setup, and automation.
> Requires Efento devices with FW version: 06.02+. 


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/coap-efento-nb-iot1-ce.webp" alt="Efento NB-IoT devices are wireless sensors that use NB-IoT technology for energy-efficient transmission of telemetry data (e.g., temperature, humidity, pressure, open/close, leakage, and more). You can integrate them with SENTIENT using the built-in CoAP transport, which receives messages from the devices, decodes them using Protobuf, and stores telemetry data on the platform. This data becomes instantly available for viewing, charting, dashboarding, alarm setup, and automation." loading="lazy"><figcaption>Efento NB-IoT devices are wireless sensors that use NB-IoT technology for energy-efficient transmission of telemetry data (e.g., temperature, humidity, pressure, open/close, leakage, and more). You can integrate them with SENTIENT using the built-in CoAP transport, which receives messages from the devices, decodes them using Protobuf, and stores telemetry data on the platform. This data becomes instantly available for viewing, charting, dashboarding, alarm setup, and automation.</figcaption></figure></div>


<br><b><font size="3">Power Saving Mode</font></b>

The platform supports the following power-saving mechanisms for optimized device operation:
- Power Saving Mode (PSM)
- Discontinuous Reception (DRX)
- Extended Discontinuous Reception (eDRX)


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/power-saving-mode-1-ce.webp" alt="The platform supports the following power-saving mechanisms for optimized device operation: Power Saving Mode (PSM), Discontinuous Reception (DRX), Extended Discontinuous Reception (eDRX)." loading="lazy"><figcaption>The platform supports the following power-saving mechanisms for optimized device operation: Power Saving Mode (PSM), Discontinuous Reception (DRX), Extended Discontinuous Reception (eDRX).</figcaption></figure></div>


### LWM2M transport type

**LwM2M** is a standardized IoT protocol designed for efficient management of resource-constrained devices. It enables centralized configuration, remote firmware updates, and real-time device monitoring.

To configure an **LwM2M device profile**, specify the following parameters:
- **Define the objects** you want to observe or interact with
- **Set the observe strategy** to determine how the platform monitors object changes
- **Configure how SENTIENT processes LwM2M object data**, including telemetry, attributes, and key parameters

Learn more about configuring the LwM2M transport at [this link](/docs/reference/lwm2m-api/).


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/lwm2m-transport-type-1-ce.webp" alt="LwM2M is a standardized IoT protocol designed for efficient management of resource-constrained devices. It enables centralized configuration, remote firmware updates, and real-time device monitoring." loading="lazy"><figcaption>LwM2M is a standardized IoT protocol designed for efficient management of resource-constrained devices. It enables centralized configuration, remote firmware updates, and real-time device monitoring.</figcaption></figure></div>


### SNMP transport type

**SNMP** is a widely used protocol for managing network devices such as routers, switches, and servers. It enables the collection and analysis of device status and performance data.

To configure an **SNMP device profile**, specify the following parameters:
- **Request timeout** — how long (in milliseconds) the system waits before retrying or marking the request as failed
- **Retry count** — how many times the system will attempt the request before giving up
- **Communication configuration** — define how the device communicates with SENTIENT over SNMP

Learn more about configuring the SNMP transport at [this link](/docs/reference/snmp-api/).


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/snmp-transport-type-1-ce.webp" alt="SNMP is a widely used protocol for managing network devices such as routers, switches, and servers. It enables the collection and analysis of device status and performance data." loading="lazy"><figcaption>SNMP is a widely used protocol for managing network devices such as routers, switches, and servers. It enables the collection and analysis of device status and performance data.</figcaption></figure></div>


## Device profile details

Clicking a device profile opens a details window where you can access and manage all aspects of that profile.


<div class="st-gallery"><figure><img src="/images/user-guide/device-profile/device-profile-details-page-1-ce.webp" alt="Clicking a device profile opens a details window where you can access and manage all aspects of that profile." loading="lazy"><figcaption>Clicking a device profile opens a <b>details window</b> where you can access and manage all aspects of that profile.</figcaption></figure></div>


<b><font size="3">Details</font></b>   
This tab contains the core configuration of the device profile — general settings that define how devices of this type behave. Here you can configure the profile name, default dashboard, default rule chain, firmware/OS information, and other high-level parameters. These settings apply to all devices assigned to this profile.

<b><font size="3">Transport Configuration</font></b>   
Defines how devices communicate with the platform. This tab includes transport-specific settings for MQTT, HTTP, CoAP, LwM2M, or SNMP, depending on the selected transport type.

Here you can configure:
- authentication strategy
- payload formats (JSON, Protobuf, custom)
- topic/endpoint settings
- request/response parameters
- device-side and server-side transport behavior

Transport configuration ensures consistent connectivity rules for all devices under this profile.

<b><font size="3">Calculated fields</font></b>   
Displays fields whose values are automatically computed using formulas based on device attributes or telemetry. These fields allow generating derived metrics without modifying device firmware. Calculated fields defined at the profile level apply to all devices using this profile. Learn more about Calculated fields [here](/docs/user-guide/calculated-fields/).

<b><font size="3">Alarm rules</font></b>   
Contains alarm rules associated with the device profile. These rules define when and how alarms should be generated across all devices in this profile, including:
- trigger conditions 
- severity levels 
- alarm propagation and clearing logic 
- optional actions (notifications, integrations, workflows)

Centralized alarm rules simplify management and ensure consistent monitoring across device groups. 

Learn more about configuring alarm rules [here](/docs/user-guide/alarm-rules/).

<b><font size="3">Device provisioning</font></b>    
Defines how devices assigned to this profile are created and authenticated. This section may include:
- provisioning strategies (HTTP, MQTT, CoAP)
- secret keys and token generation rules
- provisioning templates
- auto-registration behavior

These settings streamline automated onboarding of new devices.

See separate documentation [page](/docs/user-guide/device-provisioning/) for more details.

<b><font size="3">Audit Log</font></b>   
Displays records of all user actions performed on this device profile — changes to configuration, rules, provisioning settings, and more. Useful for troubleshooting, compliance, and tracking modifications over time.

<b><font size="3">Version control</font></b>   
Enables exporting, committing, and restoring the device profile configuration via the Git-based [version control](/docs/user-guide/version-control/) service. Supports backup, collaboration, and rollback to previous profile versions.

<hr>

## Next steps


<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please [contact us](/docs/contact-us/).
