+++
title = "Socket Connector Configuration"
description = "Socket API support for SENTIENT IoT Gateway"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/config/socket.md"
+++
This guide will help you get familiar with Socket Connector configuration for SENTIENT IoT Gateway. 
Use the [general configuration guide](/docs/iot-gateway/configuration/) to enable this connector. 
A Socket connector runs a server on the local machine to which other devices can connect. This connector is useful 
when you have devices that can send data over TCP or UDP protocols. 

We will describe the connector configuration file below.


<div class="st-callout info">


**Please note:**
If you are new to IoT Gateway, use the "Basic" configuration mode. If you are familiar with configuring IoT Gateway, you can use the "Advanced" configuration mode.


</div>


## Connector configuration

Connector configuration is a UI form that contains information on how to connect to an external server, how to process
the data and other service features. Let’s review the format of the configuration file using the example below.
Let’s take a comprehensive look at all the available settings. We will go through each option in detail to ensure 
that we thoroughly understand their functions and implications. By doing so, we can make well-informed decisions about 
which settings will best suit our needs and preferences.

## Section "General"

This configuration section contains general connector settings, such as:

- **Name** - connector name used for logs and saving to persistent devices;
- Logs configuration:
  - **Enable remote logging** - enables remote logging for the connector;
  - **Logging level** - logging level for local and remote logs: INFO, DEBUG, WARNING, ERROR, CRITICAL, NONE;
- **Send data only on change** - sends data only it has changed since the last check, otherwise – data will be sent after every check;
- **Report strategy** - strategy for sending data to SENTIENT:
  - **Report period** - period for sending data to SENTIENT in milliseconds;
  - **Type** - type of the report strategy:
    - **On report period** - sends data to SENTIENT after the report period;
    - **On value change** - sends data to SENTIENT when the value changes;
    - **On value change or report period** - sends data to SENTIENT when the value changes or report period;
    - **On received** - sends data to SENTIENT after receiving data from the device (default strategy).


<div class="st-callout info">


Additional information about the report strategy can be found [here](/docs/iot-gateway/features-overview/report-strategy).


</div>


![image](/images/gateway/socket-connector/socket-general-basic-section-1-ce.webp)


<div class="st-callout info">


The settings are the same for both the basic and advanced configurations.


</div>


## Section "Socket"

The “Socket” section is used for configuring local socket settings.


<div class="st-tabs">

<div class="st-tab" data-label="Basic">

This configuration section contains settings of the socket, such as:

- **Connection type** - socket type, can either be TCP or UDP;
- **Address** - connector bound address;
- **Port** - connector bound port;
- **Buffer size** - size of received data block buffer.

![image](/images/gateway/socket-connector/socket-basic-section-1-ce.webp)


</div>

<div class="st-tab" data-label="Advanced">

This configuration section contains settings of the socket, such as:

| **Parameter** | **Default value**         | **Description**                       |
|:--------------|:--------------------------|---------------------------------------|
| name          | **TCP Connector Example** | Connector name                        |
| type          | **TCP**                   | Socket type, can either be TCP or UDP |
| address       | **127.0.0.1**             | Connector bound address               |
| port          | **50000**                 | Connector bound port                  |
| bufferSize    | **1024**                  | Size of received data block buffer    |
| ---           |                           |                                       |

Configuration section will look like this:

```json
{
  "type": "TCP",
  "address": "127.0.0.1",
  "port": 50000,
  "bufferSize": 1024,
  ...
}
```

![image](/images/gateway/socket-connector/socket-advanced-configuration-section-1-ce.webp)


</div>

</div>


## Section "Devices"

This configuration section contains an array of objects that contains clients that can be connected to the connector\'s 
socket and send the data to it. Any connection not included in this array will be rejected by the connector.

### Subsection "Device"


<div class="st-tabs">

<div class="st-tab" data-label="Basic">

To add a new device, click the "plus" icon:

![image](/images/gateway/socket-connector/socket-device-subsection-basic-1-ce.webp)

In the opened modal window provide the following fields: 
- **Address filter** - used to filter the allowed IP addresses to connect to the connector.
- **Device name** - name for the device in SENTIENT. 
- **Device profile** - device profile for SENTIENT, by default this parameter is absent, but you can add it.
- **Encoding** - encoding used when writing string data to storage.

![image](/images/gateway/socket-connector/socket-device-subsection-basic-2-ce.webp)


</div>

<div class="st-tab" data-label="Advanced">

| **Parameter** | **Default value**  | **Description**                                                                                                    |
|:--------------|:-------------------|--------------------------------------------------------------------------------------------------------------------|
| addressFilter | *.*                | Used to filter the allowed IP addresses to connect to the connector.                                               |
| deviceName    | **Device Example** | Name for the device in SENTIENT.                                                                                |
| deviceType    | **default**        | Device type for SENTIENT, by default this parameter is absent, but you can add it.                              |
| encoding      | **utf-8**          | Encoding used when writing string data to storage.                                                                 |
| ---           |                    |                                                                                                                    |

Example:
```json
{
  "address": "127.0.0.1:50001",
  "deviceName": "Device Example",
  "deviceType": "default",
  "encoding": "utf-8",
  ...
```

![image](/images/gateway/socket-connector/socket-subsection-device-advanced-1-ce.webp)


</div>

</div>


Let’s review more examples of IP addresses filtering:

For example, we have a device that has the following IP address: 192.168.0.120:5001. Now, let's look at configuration examples 
of the field to allow connections with different IP address variants:

1. Only one device with a specified IP address and port can connect:

   **Address filter:** 192.168.0.120:5001
2. Allow any devices with any IP address, but only port 5001:

   **Address filter:** *:5001
3. Allow all devices that have the IP address 192.168.0.120 with any port:

   **Address filter:** 192.168.0.120:*
4. Allow all devices with any IP address and any port:

   **Address filter:** *:*

#### Subsection "Time series" and "Attributes"

This configuration section includes the parameters for handling incoming data.


<div class="st-tabs">

<div class="st-tab" data-label="Basic">

This converter is designed for binary payloads. It directly interprets binary data to retrieve attributes and 
time series, using specific byte positions for data extraction.

To add new time series or attribute key, follow these steps:


1. Click “**pencil**” icon of the “**Attributes**” section to add new attribute key;

1. Click on "**Add attribute**" in the opened window;

1. Enter the **key name** and fill in the **byte positions**. Click “**Apply**”;

1. Now click on the “**pencil**” icon of the “**Time series**” section to add new time series key;

1. Click on "**Add time series**" in the opened window;

1. Enter the **key name**, fill in the **byte positions** and click “**Apply**”.


<div class="st-gallery"><figure><img src="/images/gateway/socket-connector/socket-adding-device-1-ce.webp" alt="Click “**pencil**” icon of the “**Attributes**” section to add new attribute key;" loading="lazy"><figcaption>Click “**pencil**” icon of the “**Attributes**” section to add new attribute key;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-2-ce.webp" alt="Click on &quot;**Add attribute**&quot; in the opened window;" loading="lazy"><figcaption>Click on "**Add attribute**" in the opened window;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-4-ce.webp" alt="Enter the **key name** and fill in the **byte positions**. Click “**Apply**”;" loading="lazy"><figcaption>Enter the **key name** and fill in the **byte positions**. Click “**Apply**”;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-5-ce.webp" alt="Now click on the “**pencil**” icon of the “**Time series**” section to add new time series key;" loading="lazy"><figcaption>Now click on the “**pencil**” icon of the “**Time series**” section to add new time series key;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-6-ce.webp" alt="Click on &quot;**Add time series**&quot; in the opened window;" loading="lazy"><figcaption>Click on "**Add time series**" in the opened window;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-7-ce.webp" alt="Enter the **key name**, fill in the **byte positions** and click “**Apply**”." loading="lazy"><figcaption>Enter the **key name**, fill in the **byte positions** and click “**Apply**”.</figcaption></figure></div>


You can enable a specific report strategy for each time series or attribute. This strategy defines how often  
data is sent to the SENTIENT server. The following strategies are available:

- **On report period** - sends data to SENTIENT after the report period;
- **On value change** - sends data to SENTIENT when the value changes;
- **On value change or report period** - sends data to SENTIENT when the value changes or report period;
- **On received** - sends data to SENTIENT after receiving data from the device (default strategy).

![image](/images/gateway/socket-connector/socket-adding-device-9-ce.webp)


<div class="st-callout info">


Additional information about the report strategy can be found [here](/docs/iot-gateway/features-overview/report-strategy).


</div>


</div>

<div class="st-tab" data-label="Advanced">

This converter is designed for binary payloads. It directly interprets binary data to retrieve attributes and 
time series, using specific byte positions for data extraction.

| **Parameter** | **Default value** | **Description**                                                                                                      |
|:--------------|:------------------|----------------------------------------------------------------------------------------------------------------------|
| telemetry     |                   | This subsection contains parameters of the incoming message, that will be interpreted as telemetry for the device.   |
| ... key       | **temp**          | Name for telemetry in SENTIENT.                                                                                   |
| ... byteFrom  | **0**             | Used to slice received data from the specific index.                                                                 |
| ... byteTo    | **-1**            | Used to slice received data to the specific index.                                                                   |
| attributes    |                   | This subsection contains parameters of the incoming requests, that will be interpreted as attributes for the device. |
| ... key       | **hum**           | Name for attribute in SENTIENT.                                                                                   |
| ... byteFrom  | **2**             | Used to slice received data from the specific index.                                                                 |
| ... byteTo    | **4**             | Used to slice received data to the specific index.                                                                   |
| ---           |                   |                                                                                                                      |

The attributes section uses the same parameters as the telemetry section.

Example:
```json
{
  "address": "127.0.0.1:50001",
  "deviceName": "Device Example",
  "deviceType": "default",
  "encoding": "utf-8",
  "telemetry": [
    {
      "key": "temp",
      "byteFrom": 0,
      "byteTo": -1
    },
    {
      "key": "hum",
      "byteFrom": 0,
      "byteTo": 2
    }
  ],
  "attributes": [
    {
      "key": "name",
      "byteFrom": 0,
      "byteTo": -1
    },
    {
      "key": "num",
      "byteFrom": 2,
      "byteTo": 4
    }
  ]
}
```


<div class="st-gallery"><figure><img src="/images/gateway/socket-connector/socket-subsection-time-series-advanced-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-subsection-attributes-advanced-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


</div>

</div>


#### Subsection "Attribute request"

This configuration section is optional.

In order to request client-side or shared device attributes to SENTIENT server node, Gateway allows 
sending attribute requests.


<div class="st-tabs">

<div class="st-tab" data-label="Basic">

In order to add new attribute request, use the following steps:


1. Click “**pencil**” icon of the “**Attribute requests**” section to add new attribute request;

1. Click on "**Add attribute request**" in the opened window;

1. Select the request type, enter request expression, and attribute name expression. Click “**Apply**”.


<div class="st-gallery"><figure><img src="/images/gateway/socket-connector/socket-adding-device-10-ce.webp" alt="Click “**pencil**” icon of the “**Attribute requests**” section to add new attribute request;" loading="lazy"><figcaption>Click “**pencil**” icon of the “**Attribute requests**” section to add new attribute request;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-11-ce.webp" alt="Click on &quot;**Add attribute request**&quot; in the opened window;" loading="lazy"><figcaption>Click on "**Add attribute request**" in the opened window;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-12-ce.webp" alt="Select the request type, enter request expression, and attribute name expression. Click “**Apply**”." loading="lazy"><figcaption>Select the request type, enter request expression, and attribute name expression. Click “**Apply**”.</figcaption></figure></div>


</div>

<div class="st-tab" data-label="Advanced">

| **Parameter**           | **Default value** | **Description**                                                                                        |
|:------------------------|:------------------|--------------------------------------------------------------------------------------------------------|
| type                    | **shared**        | The type of requested attribute, can be either “shared” or “client”.                                   |
| requestExpression       | **${[0:3]==atr}** | The expression that is used to determine if the request from the device is "Attribute Request" or not. |
| attributeNameExpression | **[3:]**          | The expression that is used to get the name of the requested attribute from the received data.         |
| ---                     |                   |                                                                                                        |

Configuration of this subsection looks like this:

```json
"attributeRequests": [
  {
    "type": "shared",
    "requestExpression": "${[0:3]==atr}",
    "attributeNameExpression": "[3:]"
  }
]
```

Additionally, you can request multiple attributes at once. Simply add one more slice expression to 
attributeNameExpression parameter. For example, if we want to request two shared attributes in a single request, our config 
will look like this:

```json
"attributeRequests": [
  {
    "type": "shared",
    "requestExpression": "${[0:3]==atr}",
    "attributeNameExpression": "[4:19][20:]"
  }
]
```

This means that we have to send the following message to request two shared attributes:
`atr sharedAttribute sharedAttribute1`

![image](/images/gateway/socket-connector/socket-subsection-attribute-request-advanced-1-ce.webp)


</div>

</div>


#### Subsection "Attribute update"

This configuration section is optional. 

SENTIENT allows the provisioning of device attributes and fetches some of them from 
the device application. You can treat this as a remote configuration for devices, enabling them to request 
shared attributes from SENTIENT. See [user guide](/docs/user-guide/attributes/) for more details.


<div class="st-tabs">

<div class="st-tab" data-label="Basic">

In order to add new attribute update, follow these steps:


1. Click “**pencil**” icon of the “**Attribute updates**” section to add new attribute update;

1. Click on "**Add attribute update**" in the opened window;

1. Select encoding and fill in "**Attribute on platform**" field. Click “**Apply**”.


<div class="st-gallery"><figure><img src="/images/gateway/socket-connector/socket-adding-device-13-ce.webp" alt="Click “**pencil**” icon of the “**Attribute updates**” section to add new attribute update;" loading="lazy"><figcaption>Click “**pencil**” icon of the “**Attribute updates**” section to add new attribute update;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-14-ce.webp" alt="Click on &quot;**Add attribute update**&quot; in the opened window;" loading="lazy"><figcaption>Click on "**Add attribute update**" in the opened window;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-15-ce.webp" alt="Select encoding and fill in &quot;**Attribute on platform**&quot; field. Click “**Apply**”." loading="lazy"><figcaption>Select encoding and fill in "**Attribute on platform**" field. Click “**Apply**”.</figcaption></figure></div>


</div>

<div class="st-tab" data-label="Advanced">

The “attributeUpdates” configuration allows you to set up the format of the corresponding attribute data that will be 
sent to the server.

| **Parameter**          | **Default value** | **Description**                                             |
|:-----------------------|:------------------|-------------------------------------------------------------|
| encoding               | **utf-16**        | Encoding used when writing received string data to storage. |
| attributeOnSENTIENT | **sharedName**    | Shared attribute name                                       |
| ---                    |                   |                                                             |

This subsection in configuration file looks like this:

```json
"attributeUpdates": [
  {
    "encoding": "utf-16",
    "attributeOnSENTIENT": "sharedName"
  }
]
```

![image](/images/gateway/socket-connector/socket-subsection-attribute-updates-advanced-1-ce.webp)


</div>

</div>


#### Subsection "RPC methods"

This configuration section is optional. 

SENTIENT allows sending RPC commands to devices connected directly to SENTIENT or via Gateway.


<div class="st-tabs">

<div class="st-tab" data-label="Basic">

In order to add new RPC method, follow these steps:


1. Click “**pencil**” icon of the “**RPC methods**” section to add new RPC;

1. Click on "**Add method**" in the opened window;

1. Fill in "**Method name**" field, select **encoding** and check/uncheck "**With Response**" field. Click “**Apply**”.


<div class="st-gallery"><figure><img src="/images/gateway/socket-connector/socket-adding-device-16-ce.webp" alt="Click “**pencil**” icon of the “**RPC methods**” section to add new RPC;" loading="lazy"><figcaption>Click “**pencil**” icon of the “**RPC methods**” section to add new RPC;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-17-ce.webp" alt="Click on &quot;**Add method**&quot; in the opened window;" loading="lazy"><figcaption>Click on "**Add method**" in the opened window;</figcaption></figure><figure><img src="/images/gateway/socket-connector/socket-adding-device-18-ce.webp" alt="Fill in &quot;**Method name**&quot; field, select **encoding** and check/uncheck &quot;**With Response**&quot; field. Click “**Apply**”." loading="lazy"><figcaption>Fill in "**Method name**" field, select **encoding** and check/uncheck "**With Response**" field. Click “**Apply**”.</figcaption></figure></div>


</div>

<div class="st-tab" data-label="Advanced">

Configuration, provided in this section is used for sending RPC requests from SENTIENT to the device.

| **Parameter**    | **Default value** | **Description**                                                             |
|:-----------------|:------------------|-----------------------------------------------------------------------------|
| methodRPC        | **rpcMethod1**    | RPC method name.                                                            |
| withResponse     | **true**          | Boolean value that determines whether to send response back to SENTIENT. |
| methodProcessing | **write**         | Type of operation.                                                          |
| encoding         | **utf-8**         | Encoding used when writing received string data to storage.                 |
| ---              |                   |                                                                             |

This subsection in configuration file looks like this:

```json
"serverSideRpc": [
  {
    "methodRPC": "rpcMethod1",
    "withResponse": true,
    "methodProcessing": "write",
    "encoding": "utf-8"
  }
]
```

![image](/images/gateway/socket-connector/socket-subsection-rpc-methods-advanced-1-ce.webp)


</div>

</div>


Also, every telemetry and attribute parameter has a built-in SET RPC method out of the box, eliminating the need for 
manual configuration. To use them, make sure you set all the required parameters (in the case of Socket Connector, 
these are the following:
**withResponse**, **methodProcessing**, **encoding**). 
See [the guide](/docs/iot-gateway/guides/how-to-use-get-set-rpc-methods).

## Next steps

Explore guides related to main SENTIENT features:

 - [Data Visualization](/docs/user-guide/dashboards/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine-2-0/overview/) - how to use rule engine to analyze data from devices.
