+++
title = "MQTT Gateway API Reference"
description = "Supported MQTT Gateway API Reference for IoT Devices"

[extra]
status = "imported"
checked = ""
source = "docs/edge/reference/gateway-mqtt-api.md"
+++
A Gateway in SENTIENT is a special type of device that acts as a bridge between external devices and the platform. 
It maintains a single MQTT connection to SENTIENT while proxying data for multiple physical devices connected behind it.

The gateway itself is also a standard SENTIENT device. It can use the [MQTT Device API](/docs/edge/reference/mqtt-api/) to:
- Publish its own telemetry and attributes
- Receive configuration updates
- Execute RPC commands

In addition, this API defines gateway-specific MQTT topics and payload formats and is used by the open-source [SENTIENT IoT Gateway](/docs/iot-gateway/what-is-iot-gateway/).


<div class="st-callout info">


For device-level MQTT details (authentication, QoS, payload format, etc.), refer to the [MQTT Device API](/docs/edge/reference/mqtt-api/).


</div>


<hr>

## Client libraries setup

Many MQTT client libraries are available for different platforms and languages.

The examples in this guide use:   
&#8194;**&#8226;**&#8194;**Mosquitto** (command-line tools)   
&#8194;**&#8226;**&#8194;**MQTT.js** (JavaScript)

Use the instructions below to install the following command-line utilities:   
&#8194;**&#8226;**&#8194;<span class="code-light">mosquitto_pub</span>   
&#8194;**&#8226;**&#8194;<span class="code-light">mosquitto_sub</span>

Select your operating system to continue with the installation steps:


<div class="st-content-toggle" id="connectdevice">
    <div class="panel panel-default">
        <div class="panel-heading">
            
            
            
            
            <a class="content-toggle-button" data-target="#mqtt-linux">
                <div class="content-toggle-button-text">
                    MQTT<small>Linux or macOS</small>
                </div>
            </a>
            
            
            
            
            <a class="content-toggle-button" data-target="#mqtt-windows">
                <div class="content-toggle-button-text">
                    MQTT<small>Windows</small>
                </div>
            </a>
            
        </div>
        
        
        
        
        
        <div id="mqtt-linux" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


**Install mqtt client for Ubuntu**:

```bash
sudo apt-get install mosquitto-clients
```


**Install cURL for macOS**:

```bash
brew install mosquitto-clients
```


                </td></tr></table>
            </div>
        </div>
        
        
        
        
        
        <div id="mqtt-windows" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


Use the instructions listed below to download, install, setup and run mosquitto_pub in Windows:

1. Download and Install Eclipse Mosquitto. Visit [Mosquitto's official download page](https://mosquitto.org/download/) and choose the appropriate Windows installer (32-bit or 64-bit depending on your system).
2. Once downloaded, run the installer and follow the instructions. This will install Mosquitto on your Windows machine. By default, Mosquitto is installed in 'C:\Program Files\mosquitto';
3. Update the System&#39;s "Path" variable. The executables 'mosquitto_pub.exe' and 'mosquitto_sub.exe' are located in the directory where you installed the Mosquitto. You need to add this directory to your system's "Path" environment variable so that Windows can find these executables regardless of the current directory.

To add the Mosquitto directory to the "Path" variable, follow these steps: 


1. Press the Win + X, then select "System". Then click on the "System" page;

1. Navigate to the "About" section, then click "Advanced system settings";

1. In the "System Properties" pop-up window, click "Environment Variables" button on the "Advanced" tab;

1. In the "Environment Variables" pop-up window, select the "Path", then click on the "Edit" button;

1. In the "Edit environment variable" pop-up window click on the "New" button and add the path to the directory containing &#39;mosquitto_pub.exe&#39; and &#39;mosquitto_sub.exe&#39; (&#39;C:\Program Files\mosquitto&#39; by default). Click "OK" button;

1. Click "OK" button to save changes in the environment variables;

1. Finally, click "OK" button to apply all changes in the system properties.


<div class="st-gallery"><figure><img src="/images/helloworld/getting-started-pe/mosquitto-windows-1.webp" alt="Press the Win + X, then select &quot;System&quot;. Then click on the &quot;System&quot; page;" loading="lazy"><figcaption>Press the Win + X, then select "System". Then click on the "System" page;</figcaption></figure><figure><img src="/images/helloworld/getting-started-pe/mosquitto-windows-2.webp" alt="Navigate to the &quot;About&quot; section, then click &quot;Advanced system settings&quot;;" loading="lazy"><figcaption>Navigate to the "About" section, then click "Advanced system settings";</figcaption></figure><figure><img src="/images/helloworld/getting-started-pe/mosquitto-windows-3.webp" alt="In the &quot;System Properties&quot; pop-up window, click &quot;Environment Variables&quot; button on the &quot;Advanced&quot; tab;" loading="lazy"><figcaption>In the "System Properties" pop-up window, click "Environment Variables" button on the "Advanced" tab;</figcaption></figure><figure><img src="/images/helloworld/getting-started-pe/mosquitto-windows-4.webp" alt="In the &quot;Environment Variables&quot; pop-up window, select the &quot;Path&quot;, then click on the &quot;Edit&quot; button;" loading="lazy"><figcaption>In the "Environment Variables" pop-up window, select the "Path", then click on the "Edit" button;</figcaption></figure><figure><img src="/images/helloworld/getting-started-pe/mosquitto-windows-5.webp" alt="In the &quot;Edit environment variable&quot; pop-up window click on the &quot;New&quot; button and add the path to the directory containing &#39;mosquitto_pub.exe&#39; and &#39;mosquitto_sub.exe&#39; (&#39;C:\Program Files\mosquitto&#39; by default). Click &quot;OK&quot; button;" loading="lazy"><figcaption>In the "Edit environment variable" pop-up window click on the "New" button and add the path to the directory containing &#39;mosquitto_pub.exe&#39; and &#39;mosquitto_sub.exe&#39; (&#39;C:\Program Files\mosquitto&#39; by default). Click "OK" button;</figcaption></figure><figure><img src="/images/helloworld/getting-started-pe/mosquitto-windows-6.webp" alt="Click &quot;OK&quot; button to save changes in the environment variables;" loading="lazy"><figcaption>Click "OK" button to save changes in the environment variables;</figcaption></figure><figure><img src="/images/helloworld/getting-started-pe/mosquitto-windows-7.webp" alt="Finally, click &quot;OK&quot; button to apply all changes in the system properties." loading="lazy"><figcaption>Finally, click "OK" button to apply all changes in the system properties.</figcaption></figure></div>


                </td></tr></table>
            </div>
        </div>
        
    </div>
</div>


<hr>

## Device connect API

Use this API to inform SENTIENT that a device behind the Gateway is now connected and ready to exchange data.

**Topic:**

```bash
v1/gateway/connect
```


**Payload:**

```bash
{"device": "Device A", "type": "Sensor A"}
```

- **device** - required. The device name in SENTIENT.
- **type** – optional. Name of the device profile. If omitted, the `default` device profile is used.

**Behavior:**

- If a device with the given name does not exist, SENTIENT creates it automatically.
- If the device profile name is provided and the profile does not exist, SENTIENT creates it automatically.
- Once connected, SENTIENT routes the following events for this device through the Gateway:
  - Updates to shared attributes.
  - RPC commands.


<div class="st-callout info">


**Only for MQTT v.5**

It is recommended to wait for the PUBACK response to ensure that the device connection was successful.
If something goes wrong during the connection, for example, the device limit is exceeded, the PUBACK will return with 
the corresponding [status code](/docs/reference/mqtt-v5-errors-code/).


</div>


**Examples**


> ⚠️ In all examples on this page, the hostname refers to a **local** SENTIENT Edge installation.   
If your SENTIENT Edge instance is deployed on a different host, replace <code>localhost</code> with the appropriate hostname or IP address.


> Don&#39;t forget to replace <code>$ACCESS_TOKEN</code> with your gateway device access token.

**Example 1.** Connect a device.

In order to inform SENTIENT that device is connected to the Gateway, one needs to publish following message:

```bash
mosquitto_pub -h "localhost" -t "v1/gateway/connect" -u "$ACCESS_TOKEN" -m '{"device": "Device A"}'
```


**Example 2.** Connect a device with a specific device profile.

In order to inform SENTIENT that device is connected to the Gateway with a specific device profile, one needs to 
publish following message:

```bash
mosquitto_pub -h "localhost" -t "v1/gateway/connect" -u "$ACCESS_TOKEN" -m '{"device": "Device A", "type": "Sensor A"}'
```


<hr>

## Device disconnect API

Use this API to inform SENTIENT that a device behind the Gateway is no longer active.

**Topic:**

```bash
v1/gateway/disconnect
```


**Payload:**

```bash
{"device": "Device A"}
```


**Behavior:**

- If the device with the given name does not exist, SENTIENT ignores the message.
- After processing this message, SENTIENT stops sending attribute and RPC updates for that device to the Gateway.


<div class="st-callout info">


**Only for MQTT v.5**

If something goes wrong during the disconnecting, the PUBACK will return with the corresponding [status code](/docs/reference/mqtt-v5-errors-code/).


</div>


**Example**

> ⚠️ Replace <code>$ACCESS_TOKEN</code> with your gateway device access token.

Also, make sure that the device is connected before disconnecting it.

In order to inform SENTIENT that device is disconnected from the Gateway, one needs to publish following message:

```bash
mosquitto_pub -h "localhost" -t "v1/gateway/disconnect" -u "$ACCESS_TOKEN" -m '{"device": "Device A"}'
```


<hr>

## Attributes API

SENTIENT attributes API allows devices to:


- Upload [client-side](/docs/user-guide/attributes/#attribute-types) device attributes to the server.
- Request [client-side](/docs/user-guide/attributes/#attribute-types) and [shared](/docs/user-guide/attributes/#attribute-types) device attributes from SENTIENT platform.
- Subscribe to [shared](/docs/user-guide/attributes/#attribute-types) device attributes from SENTIENT platform.


<hr>

### Publish attribute to SENTIENT

Use this topic to publish client-side device attributes to SENTIENT platform. All attributes in the payload 
are stored as client-side attributes for the corresponding devices.

**Topic:**

```bash
v1/gateway/attributes
```


**Payload:**

```json
{
  "Device A": {
    "attribute1": "value1",
    "attribute2": 42
  },
  "Device B": {
    "attribute1": "value1",
    "attribute2": 42
  }
}
```


**Behavior:**

- If the device with the given name does not exist, SENTIENT creates it automatically with `default` profile name.
- If the attribute does not exist, it is created.
- If the attribute already exists, its value is updated.


<div class="st-callout info">


**Only for MQTT v.5**

If something goes wrong during the publishing, the PUBACK will return with the corresponding [status code](/docs/reference/mqtt-v5-errors-code/).


</div>


**Example**

> ⚠️ Replace <code>$ACCESS_TOKEN</code> with your gateway device access token.

In order to publish client-side device attributes to SENTIENT platform, one needs to publish following message:

```bash
mosquitto_pub -h "localhost" -t "v1/gateway/attributes" -u "$ACCESS_TOKEN" -m '{"Device A": { "fw_version": "1.0", "battery": 87 }}'
```


<hr>

### Request attribute values from SENTIENT

Use this API to request client-side or shared device attributes from SENTIENT platform. Make attention that you 
need to subscribe to the response topic first in order to receive the response.

**Subscribe topic:**

```bash
v1/gateway/attributes/response
```


**Publish topic:**

```bash
v1/gateway/attributes/request
```


**Payload:**

```json
{
  "id": "$request_id",
  "device": "Device A",
  "client": ["key1", "key2"],
  "shared": ["key3", "key4"]
}
```


Fields:
- **id** – required. Your integer request identifier.
- **device** – required. The device name in SENTIENT.
- **client** – optional. An array of client-side attribute keys to request.
- **shared** – optional. An array of shared attribute keys to request.

<hr>

### Subscribe to attribute updates from SENTIENT

Use this topic to subscribe to shared device attribute changes. Take attention that you need to subscribe to the topic 
first in order to receive updates.

**Subscribe topic:**

```bash
v1/gateway/attributes
```


**Response message format:**

```json
{
  "device": "Device A",
  "data": {
    "attribute1": "value1",
    "attribute2": 42
  }
}
```


Fields:
- **device** – the device name in SENTIENT.
- **data** – map of updated shared attributes.

<hr>

## Telemetry upload API

Use this API to publish telemetry for one or more devices in a single MQTT message.

**Topic:**

```bash
v1/gateway/telemetry
```


**Payload:**

```json
{
  "Device A": [
    {
      "ts": 1483228800000,
      "values": {
        "temperature": 42,
        "humidity": 80
      }
    },
    {
      "ts": 1483228801000,
      "values": {
        "temperature": 43,
        "humidity": 82
      }
    }
  ],
  "Device B": [
    {
      "ts": 1483228800000,
      "values": {
        "temperature": 42,
        "humidity": 80
      }
    }
  ]
}
```


Fields:
- **device** – required. The device name in SENTIENT.
- **ts** – Optional. Unix timestamp in milliseconds.
- **values** – required. Key-value map of telemetry fields (e.g., temperature, humidity).

**Behavior:**

- If the device with the given name does not exist, SENTIENT creates it automatically with `default` profile name.
- If the telemetry keys do not exist, they are created.
- Telemetry data is stored with the provided timestamps.


<div class="st-callout info">


**Only for MQTT v.5**

If something goes wrong during the publishing, the PUBACK will return with the corresponding [status code](/docs/reference/mqtt-v5-errors-code/).


</div>


**Example**

> ⚠️ Replace <code>$ACCESS_TOKEN</code> with your gateway device access token.

In order to publish device telemetry to SENTIENT platform, one needs to publish following message:

```bash
mosquitto_pub -h "localhost" -t "v1/gateway/telemetry" -u "$ACCESS_TOKEN" -m '{"Device A": [{"ts": 1700000000000, "values": {"temperature": 23.5, "humidity": 61 }}]}'
```


<hr>

## RPC API

### Server-side RPC

Use this API to receive and respond to RPC commands from SENTIENT for devices behind the Gateway.

**Subscribe topic:**

```bash
v1/gateway/rpc
```


**Request message format:**

```bash
{"device": "Device A", "data": {"id": $request_id, "method": "toggle_gpio", "params": {"pin": 1}}}
```


**Response topic:**

```bash
v1/gateway/rpc
```


**Response message format:**

```bash
{"device": "Device A", "id": $request_id, "data": {"success": true}}
```


Fields:
- **device** – the device name in SENTIENT.
- **id** – your integer request identifier.
- **data** – response payload.

You need to subscribe to the request topic first in order to receive RPC commands. After processing the RPC command, 
you can publish the response message to the response topic.


<div class="st-callout info">


Make sure that device is connected via the Gateway to receive RPC commands for it.

Make attention that the **id** in the response message should match the **id** from the request message.


</div>


<hr>

## Claiming devices API

SENTIENT supports a claiming mechanism that allows end users to take ownership of pre-provisioned devices. For 
conceptual details, see [Claiming devices](/docs/user-guide/claiming-devices/) guide.

**Topic:**

```bash
v1/gateway/claim
```


**Payload:**

```json
{
  "Device A": {
    "secretKey": "value_A",
    "durationMs": 60000
  },
  "Device B": {
    "secretKey": "value_B",
    "durationMs": 60000
  }
}
```


Per-device parameters:
- **secretKey** – optional. The secret key assigned to the device for claiming. If omitted, an empty string is used.
- **durationMs** – optional. Claiming duration in milliseconds. If omitted, the system parameter 
**device.claim.duration** is used (in the file **/etc/sentient/conf/sentient.yml**).

**Example**

> ⚠️ Replace <code>$ACCESS_TOKEN</code> with your gateway device access token.

Also, make sure that the device is connected before testing claiming.

In order to inform SENTIENT platform to start claiming process for devices, one needs to publish following message:

```bash
mosquitto_pub -h "localhost" -t "v1/gateway/claim" -u "$ACCESS_TOKEN" -m '{"Device A": {"secretKey": "mySecret", "durationMs": 60000}}'
```


<hr>

## Protocol customization

MQTT transport can be fully customized for specific use-case by changing the corresponding [module](https://github.com/sentient/sentient/tree/master/transport/mqtt).

<hr>

## Next steps
