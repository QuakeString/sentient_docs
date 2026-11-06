+++
title = "MQTT Device API Reference"
description = "Supported MQTT API Reference for IoT Devices"

[extra]
status = "imported"
checked = ""
source = "docs/reference/mqtt-api.md"
+++
[MQTT](https://en.wikipedia.org/wiki/MQTT) is a lightweight publish/subscribe messaging protocol,probably making it the most suitable for various IoT devices. 

SENTIENT server nodes acts as an MQTT broker and supports:   
&#8194;**&#8226;**&#8194;QoS 0 (at most once)   
&#8194;**&#8226;**&#8194;QoS 1 (at least once)   
&#8194;**&#8226;**&#8194;Configurable MQTT topics via [Device profiles](/docs/user-guide/device-profiles/#mqtt-device-topic-filters)

Learn more about MQTT at [mqtt.org](https://mqtt.org/).

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


<div class="tb-content-toggle" id="connectdevice">
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

## Authentication methods

SENTIENT supports multiple authentication mechanisms to secure MQTT connections.

**Supported methods**:
- [Access token](/docs/user-guide/access-token/). Uses a unique **device access token** as the MQTT **username** in the <span class="code-light">CONNECT</span> packet.   
  This method provides a simple and secure way to authenticate devices without requiring certificates or additional credentials.
- [X.509 certificates](/docs/user-guide/certificates/). Uses digital certificates to authenticate devices and establish secure communication based on **public key infrastructure (PKI)**.
- [Basic MQTT credentials](/docs/user-guide/basic-mqtt/) Uses authentication data—a combination of the optional client ID, username, and password—sent in the MQTT <span class="code-light">CONNECT</span> packet. 

Topic names and payload formats for MQTT communication are configured via the **Device profile**. For more details, see [here](/docs/user-guide/device-profiles/#mqtt-transport-type).

> The examples in this guide use **access token–based authentication**.

<hr>

## Publish a test telemetry message

Use the following command to publish test telemetry data.


 

> ⚠️ **Don&#39;t forget to replace:**   
> &#8194;&#8226;&#8194;<code>$SENTIENT_HOST_NAME</code> with your SENTIENT hostname or IP address.   
> &#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

```bash
mosquitto_pub -d -q 1 -h "$SENTIENT_HOST_NAME" -p "1883" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -m {"temperature":25}
```


**Example**   
In this example, <code>$SENTIENT_HOST_NAME</code> refers to your <code>local</code> SENTIENT installation, and <code>$ACCESS_TOKEN</code> is set to <code>ABC123</code>.

```bash
mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "ABC123" -m {"temperature":25}
```


A successful telemetry publish produces output similar to the following:

```
Client mosqpub|xxx sending CONNECT
Client mosqpub|xxx received CONNACK
Client mosqpub|xxx sending PUBLISH (d0, q1, r0, m1, 'v1/devices/me/telemetry', ... (16 bytes))
Client mosqpub|xxx received PUBACK (Mid: 1)
Client mosqpub|xxx sending DISCONNECT
```

<b><font size="3">Possible MQTT connection responses</font></b>

During the connection process, the MQTT broker may return the following response codes:

* **0x00 Connected** - Successfully connected to SENTIENT MQTT server.
* **0x04 Connection Refused, bad username or password** - Username is empty.
* **0x05 Connection Refused, not authorized** - Username contains invalid access token.

<hr>

## Key-value format

By default, SENTIENT supports key-value content in JSON. Key is always a string, while value can be either string, boolean, double, long or JSON.
For example:

```json
{
 "stringKey":"value1", 
 "booleanKey":true, 
 "doubleKey":42.0, 
 "longKey":73, 
 "jsonKey": {
    "someNumber": 42,
    "someArray": [1,2,3],
    "someNestedObject": {"key": "value"}
 }
}
```


However, it is also possible to send data via [Protocol Buffers](https://developers.google.com/protocol-buffers).
Please refer to the [MQTT transport type](/docs/user-guide/device-profiles/#mqtt-transport-type) configuration section in device profile article for more details.

Using custom binary format or some serialization framework is also possible. See [protocol customization](#protocol-customization) for more details.

<hr>

## Telemetry upload API

In order to publish telemetry data to SENTIENT server node, send PUBLISH message to the following topic:
 
```bash
v1/devices/me/telemetry
```

The simplest supported data formats are:

```json
{"key1":"value1", "key2":"value2"}
```

or

```json
[{"key1":"value1"}, {"key2":"value2"}]
```


<div class="st-callout info">


**Please note** that in this case, the server-side timestamp will be assigned to uploaded data!


</div>


In case your device is able to get the client-side timestamp, you can use following format:

```json
{"ts":1451649600512, "values":{"key1":"value1", "key2":"value2"}}
```

Where **1451649600512** is a [unix timestamp](https://en.wikipedia.org/wiki/Unix_time) with milliseconds precision. For example, the value '1451649600512' corresponds to 'Fri, 01 Jan 2016 12:00:00.512 GMT'

<br><b><font size="3">Examples</font></b>   
Below are the examples of commands for publishing different types of telemetry data.

> ⚠️ Don&#39;t forget to replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_HOST_NAME</code> with your SENTIENT hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

**Example 1**.   
Publish data as an object without timestamp (server-side timestamp will be used). 

Execute the command:


<div class="st-tabs">

<div class="st-tab" data-label="Mosquitto">


```bash
mosquitto_pub -d -q 1 -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -m "{"temperature":42}"
```


</div>

<div class="st-tab" data-label="MQTT.js">


```bash
mqtt pub -v -q 1 -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/telemetry" -u '$ACCESS_TOKEN' -m "{"temperature":42}"
```


</div>

</div>


Telemetry data:

```json
{"temperature":42}
```

**Example 2**.   
Publish data as an object without timestamp (server-side timestamp will be used) using data from [telemetry-data-as-object.json](/docs/reference/resources/telemetry-data-as-object.json) file.

Execute the command:


<div class="st-tabs">

<div class="st-tab" data-label="Mosquitto">


```bash
mosquitto_pub -d -q 1 -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -f "telemetry-data-as-object.json"
```


</div>

<div class="st-tab" data-label="MQTT.js">


```bash
cat telemetry-data-as-object.json | mqtt pub -v -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/telemetry" -u '$ACCESS_TOKEN' -s -m ""
```


</div>

</div>


The content of the JSON file:

```json
{
  "stringKey": "value1",
  "booleanKey": true,
  "doubleKey": 42.0,
  "longKey": 73,
  "jsonKey": {
    "someNumber": 42,
    "someArray": [1,2,3],
    "someNestedObject": {"key": "value"}
  }
}
```

**Example 3**.   
Publish data as an array of objects without timestamp (server-side timestamp will be used) using data from [telemetry-data-as-array.json](/docs/reference/resources/telemetry-data-as-array.json) file.

Execute the command:


<div class="st-tabs">

<div class="st-tab" data-label="Mosquitto">


```bash
mosquitto_pub -d -q 1 -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -f "telemetry-data-as-array.json"
```


</div>

<div class="st-tab" data-label="MQTT.js">


```bash
cat telemetry-data-as-array.json | mqtt pub -v -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/telemetry" -u '$ACCESS_TOKEN' -s -m ""
```


</div>

</div>


The content of the JSON file:

```json
[{"key1":"value1"}, {"key2":true}]
```

**Example 4**.   
Publish data as an object with timestamp (telemetry timestamp will be used) using data from [telemetry-data-with-ts.json](/docs/reference/resources/telemetry-data-with-ts.json) file.

Execute the command:


<div class="st-tabs">

<div class="st-tab" data-label="Mosquitto">


```bash
mosquitto_pub -d -q 1 -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -f "telemetry-data-with-ts.json"
```


</div>

<div class="st-tab" data-label="MQTT.js">


```bash
cat telemetry-data-with-ts.json | mqtt pub -v -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/telemetry" -u '$ACCESS_TOKEN' -s -m ""
```


</div>

</div>


The content of the JSON file:

```json
{
  "ts": 1451649600512,
  "values": {
    "stringKey": "value1",
    "booleanKey": true,
    "doubleKey": 42.0,
    "longKey": 73,
    "jsonKey": {
      "someNumber": 42,
      "someArray": [1, 2, 3],
      "someNestedObject": {
        "key": "value"
      }
    }
  }
}
```

<hr>

## Attributes API

SENTIENT attributes API allows devices to

* Upload [client-side](/docs/user-guide/attributes/#attribute-types) device attributes to the server.
* Request [client-side](/docs/user-guide/attributes/#attribute-types) and [shared](/docs/user-guide/attributes/#attribute-types) device attributes from the server.
* Subscribe to [shared](/docs/user-guide/attributes/#attribute-types) device attributes from the server.

<hr>

### Publish attribute update to the server

In order to publish client-side device attributes to SENTIENT server node, send PUBLISH message to the following topic:

```bash
v1/devices/me/attributes
```


<b><font size="3">Examples</font></b>   
Below are the examples of how to publish client-side device attributes.

> ⚠️ Don&#39;t forget to replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_HOST_NAME</code> with your SENTIENT hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

**Example 1**.   
Publish client-side attributes update.

Telemetry data:

```json
{"attribute1": "value1", "attribute2": true}
```


Execute the command:


```bash
mosquitto_pub -d -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/attributes" -u "$ACCESS_TOKEN" -m "{"attribute1": "value1", "attribute2": true}"
```


**Example 2**.   
Publish client-side attributes update using data from [new-attributes-values.json](/docs/reference/resources/new-attributes-values.json) file.

The content of the **"new-attributes-values.json"** file:

```json
{
  "attribute1": "value1",
  "attribute2": true,
  "attribute3": 42.0,
  "attribute4": 73,
  "attribute5": {
    "someNumber": 42,
    "someArray": [1,2,3],
    "someNestedObject": {"key": "value"}
  }
}
```

Execute the command:


<div class="st-tabs">

<div class="st-tab" data-label="Mosquitto">


```bash
mosquitto_pub -d -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/attributes" -u "$ACCESS_TOKEN" -f "new-attributes-values.json"
```


</div>

<div class="st-tab" data-label="MQTT.js">


```bash
cat new-attributes-values.json | mqtt pub -d -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/attributes" -u '$ACCESS_TOKEN' -s -m ""
```


</div>

</div>


<hr>

### Request attribute values from the server

In order to request client-side or shared device attributes to SENTIENT server node, send PUBLISH message to the following topic:

```bash
v1/devices/me/attributes/request/$request_id
```


where **$request_id** is your integer request identifier.
Before sending PUBLISH message with the request, client needs to subscribe to 

```bash
v1/devices/me/attributes/response/+
```

<br><b><font size="3">Example</font></b>   
The following example is written in javascript and is based on mqtt.js. 
Pure command-line examples are not available because subscribe and publish need to happen in the same mqtt session.

**1.** Save the [mqtt-js-attributes-request.js](/docs/reference/resources/mqtt-js-attributes-request.js) file to your PC.


> ⚠️ In this example, the hostname refers to a **local SENTIENT installation**.   
> If your SENTIENT instance is deployed on a different host, make sure to replace <code>localhost</code> with the appropriate hostname or IP address.


<div class="st-tabs">

<div class="st-tab" data-label="The content of the "mqtt-js-attributes-request.js" file:">


```javascript
var mqtt = require('mqtt')
var client = mqtt.connect('mqtt://localhost', {
    username: process.env.TOKEN
})

client.on('connect', function () {
    console.log('connected')
    client.subscribe('v1/devices/me/attributes/response/+')
    client.publish('v1/devices/me/attributes/request/1', '{"clientKeys":"attribute1,attribute2", "sharedKeys":"shared1,shared2"}')
})

client.on('message', function (topic, message) {
    console.log('response.topic: ' + topic)
    console.log('response.body: ' + message.toString())
    client.end()
})
```


</div>

</div>


**2.** Execute the command.

> ⚠️ Replace <code>$ACCESS_TOKEN</code> with your device&#39;s access token.

```bash
export TOKEN=$ACCESS_TOKEN
node mqtt-js-attributes-request.js
```


Result:

```
{"client":{"attribute1":"value1","attribute2":true}}
```


<div class="st-callout info">


**Please note**, the intersection of client-side and shared device attribute keys is a bad practice! 
However, it is still possible to have same keys for client, shared or even server-side attributes.


</div>


<hr>

### Subscribe to attribute updates from the server

In order to subscribe to shared device attribute changes, send SUBSCRIBE message to the following topic:

```bash
v1/devices/me/attributes
```


When a shared attribute is changed by one of the server-side components (such as the REST API or the Rule Chain), the client will receive the following update: 

```json
{"key1":"value1"}
```

> ⚠️ Don&#39;t forget to replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_HOST_NAME</code> with your SENTIENT hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

Execute the command:


<div class="st-tabs">

<div class="st-tab" data-label="Mosquitto">


```bash
mosquitto_sub -d -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/attributes" -u "$ACCESS_TOKEN"
```


</div>

<div class="st-tab" data-label="MQTT.js">


```bash
mqtt sub -v -h "$SENTIENT_HOST_NAME" -t "v1/devices/me/attributes" -u '$ACCESS_TOKEN'
```


</div>

</div>


<hr>

## JSON value support

We have added support of JSON data structures to telemetry and attributes API to simplify work with device configuration.
JSON support allows you to both upload from the device, and push nested objects to the device.
You can store one configuration JSON as a shared attribute and push it to the device. You can also process the JSON data in the rule engine and raise alarms, etc.

Therefore, this improvement minimizes the number of Database operations when SENTIENT stores the data.
For example, “temperature” and “humidity” would be stored as separate rows in SQL or NoSQL databases in order to efficiently aggregate this data for visualization.
Since there is no need to aggregate JSON data, we can store all the content as one row instead of separate rows for each configuration item.
In some of our environments, it is possible to decrease the number of database operations more than 10 times by aggregating multiple parameters within one JSON.

Learn more about JSON value support with the [video](https://www.youtube.com/watch?v=ErV5Krwhak0&ab_channel=SENTIENT).

<hr>

## RPC API

### Server-side RPC

In order to subscribe to RPC commands from the server, send SUBSCRIBE message to the following topic:

```bash
v1/devices/me/rpc/request/+
```


Once subscribed, the client will receive individual commands as a PUBLISH message to the corresponding topic:

```bash
v1/devices/me/rpc/request/$request_id
```

where **$request_id** is an integer request identifier.

The client should publish the response to the following topic:

```bash
v1/devices/me/rpc/response/$request_id
```

<br><b><font size="3">Example</font></b>   
The following example is written in javascript and is based on mqtt.js. 
Pure command-line examples are not available because subscribe and publish need to happen in the same mqtt session.


**1.** Save the [mqtt-js-rpc-from-server.js](/docs/reference/resources/mqtt-js-rpc-from-server.js) file to your PC.

> ⚠️ In this example, the hostname refers to a **local SENTIENT installation**.   
> If your SENTIENT instance is deployed on a different host, make sure to replace <code>localhost</code> with the appropriate hostname or IP address.


  


<div class="st-tabs">

<div class="st-tab" data-label="The content of the "mqtt-js-rpc-from-server.js" file">


```javascript
var mqtt = require('mqtt');
var client = mqtt.connect('mqtt://localhost', {
    username: process.env.TOKEN
});

client.on('connect', function () {
    console.log('connected');
    client.subscribe('v1/devices/me/rpc/request/+')
});

client.on('message', function (topic, message) {
    console.log('request.topic: ' + topic);
    console.log('request.body: ' + message.toString());
    var requestId = topic.slice('v1/devices/me/rpc/request/'.length);
    //client acts as an echo service
    client.publish('v1/devices/me/rpc/response/' + requestId, message);
});
```


</div>

</div>


**2.** Now, follow these steps:
- Use **RPC debug terminal** widget in your SENTIENT instance;
- Execute the command to subscribe to RPC commands from the server using the command below. 

> ⚠️ Replace <code>$ACCESS_TOKEN</code> with your device&#39;s access token.

```bash
export TOKEN=$ACCESS_TOKEN
node mqtt-js-rpc-from-server.js
```


- Send an RPC request "connect" to the device using **RPC debug terminal** widget;
- You should receive a response from the device.


<div class="st-gallery"><figure><img src="/images/reference/device-connectivity-apis/server-side-rpc-mqtt-1-ce.webp" alt="Use RPC debug terminal widget in your SENTIENT instance" loading="lazy"><figcaption>Use RPC debug terminal widget in your SENTIENT instance</figcaption></figure><figure><img src="/images/reference/device-connectivity-apis/server-side-rpc-mqtt-2-ce.webp" alt="Subscribe to RPC commands from the server" loading="lazy"><figcaption>Subscribe to RPC commands from the server</figcaption></figure><figure><img src="/images/reference/device-connectivity-apis/server-side-rpc-mqtt-3-ce.webp" alt="Send an RPC request &quot;connect&quot; to the device using RPC debug terminal widget" loading="lazy"><figcaption>Send an RPC request "connect" to the device using RPC debug terminal widget</figcaption></figure><figure><img src="/images/reference/device-connectivity-apis/server-side-rpc-mqtt-4-ce.webp" alt="You should receive a response from the device" loading="lazy"><figcaption>You should receive a response from the device</figcaption></figure></div>


In case your MQTT device is a gateway, SENTIENT will send a server-side RPC (notification) about changes on provisioned device entities.  
Your MQTT gateway device will receive a service RPC about removal or renaming of device to [properly resolve such events](/docs/iot-gateway/how-device-removing-renaming-works/). 

<hr>

### Client-side RPC

In order to send RPC commands to server, send PUBLISH message to the following topic:

```bash
v1/devices/me/rpc/request/$REQUEST_ID
```


> Where <code>$REQUEST_ID</code> is an integer request identifier.

The response from server will be published to the following topic:

```bash
v1/devices/me/rpc/response/$request_id
```

<br><b><font size="3">Example</font></b>   
The following example is written in javascript and is based on mqtt.js. 
Pure command-line examples are not available because subscribe and publish need to happen in the same mqtt session.


**1.** Save the [mqtt-js-rpc-from-client.js](/docs/reference/resources/mqtt-js-rpc-from-client.js) file to your PC. 

> ⚠️ In this example, the hostname refers to a **local SENTIENT installation**.   
> If your SENTIENT instance is deployed on a different host, make sure to replace <code>localhost</code> with the appropriate hostname or IP address.


<div class="st-tabs">

<div class="st-tab" data-label="The content of the "mqtt-js-rpc-from-client.js" file">


```javascript
var mqtt = require('mqtt');
var client = mqtt.connect('mqtt://localhost', {
    username: process.env.TOKEN
});

client.on('connect', function () {
    console.log('connected');
    client.subscribe('v1/devices/me/rpc/response/+');
    var requestId = 1;
    var request = {
        "method": "getCurrentTime",
        "params": {}
    };
    client.publish('v1/devices/me/rpc/request/' + requestId, JSON.stringify(request));
});

client.on('message', function (topic, message) {
    console.log('response.topic: ' + topic);
    console.log('response.body: ' + message.toString());
});
```


</div>

</div>


**2.** Now, follow these steps:
- In the **Root Rule Chain** add two nodes: [transformation script](/docs/user-guide/rule-engine-2-0/nodes/transformation/script) and [rpc call reply](/docs/user-guide/rule-engine-2-0/nodes/action/rpc-call-reply). Connect them to "[Log RPC from Device](/docs/user-guide/rule-engine-2-0/nodes/action/log)" action node with "**Success**" link.
- In the **script** node enter the function:

```bash
return {msg: {time: new Date()}, metadata: metadata, msgType: msgType};
```


- Send request to the server.

> ⚠️ Replace <code>$ACCESS_TOKEN</code> with your device&#39;s access token.

```bash
export TOKEN=$ACCESS_TOKEN
node mqtt-js-rpc-from-client.js
```


You should receive a response from the server:

```bash
{"time":"Thursday, February 5, 2026, 9:08:22 AM Coordinated Universal Time"}
```


<div class="st-gallery"><figure><img src="/images/reference/device-connectivity-apis/client-side-rpc-1-ce.webp" alt="Add two nodes to the Rule Chain: &quot;script&quot; and &quot;rpc call reply&quot;" loading="lazy"><figcaption>Add two nodes to the Rule Chain: "script" and "rpc call reply"</figcaption></figure><figure><img src="/images/reference/device-connectivity-apis/client-side-rpc-2-ce.webp" alt="In the script node enter the function: return {msg: {time:String(new Date())}, metadata: metadata, msgType: msgType};" loading="lazy"><figcaption>In the script node enter the function: return {msg: {time:String(new Date())}, metadata: metadata, msgType: msgType};</figcaption></figure><figure><img src="/images/reference/device-connectivity-apis/client-side-rpc-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/reference/device-connectivity-apis/client-side-rpc-mqtt-4-ce.webp" alt="Send request to the server" loading="lazy"><figcaption>Send request to the server</figcaption></figure><figure><img src="/images/reference/device-connectivity-apis/client-side-rpc-mqtt-5-ce.webp" alt="You should receive a response from the server" loading="lazy"><figcaption>You should receive a response from the server</figcaption></figure></div>


<hr>

### Get session limits RPC

The **getSessionLimits** RPC method allows device manufacturers and developers to retrieve the **MQTT transport limits** enforced by SENTIENT server.

Understanding these limits helps ensure that devices operate within supported parameters and prevents issues such as **message rejection, throttling**, or **connection loss**.

<b><font size="3">Request format</font></b>   
To request session limits, the device sends the following RPC request:

```json
{
  "method": "getSessionLimits",
  "params": {}
}
```

<b><font size="3">Response format</font></b>   
After processing the request, SENTIENT returns the session limits in the RPC response using the following format:

```json
{
  "maxPayloadSize": 65536,
  "maxInflightMessages": 100,
  "rateLimits": {
    "messages": "200:1,6000:60,14000:3600",
    "telemetryMessages": "100:1,3000:60,7000:3600",
    "telemetryDataPoints": "200:1,6000:60,14000:3600"
  }
}
```

<b><font size="3">Response fields description</font></b>   
- **maxPayloadSize** - the maximum allowable size for an MQTT message payload, expressed in bytes.  
- **maxInflightMessages** -  the maximum number of MQTT messages that can be sent but remain unacknowledged (in-flight) at any given time.
- **rateLimits** - A nested object defining rate limits for different message categories:
  - **messages** - the overall message rate limit.
  - **telemetryMessages** - the maximum number of telemetry messages that can be sent.
  - **telemetryDataPoints** - the number of telemetry data points a device can send.  

<b><font size="3">Rate Limit Format Explanation</font></b>   
A rate limit value such as:

```
200:1,6000:60,14000:3600
```

- **200:1** — up to 200 messages per second
- **6000:60** — up to 6,000 messages per 60 seconds (1 minute)
- **14000:3600** — up to 14,000 messages per 3,600 seconds (1 hour)

These limits are enforced simultaneously.

<b><font size="4">Gateway-specific session limits</font></b>   
If the device is a **gateway**, the response includes additional limits that apply to devices connected **through the gateway**.

<b><font size="3">Gateway response format</font></b>   

```json
{
  "maxPayloadSize": 65536,
  "maxInflightMessages": 100,
  "rateLimits": {
    "messages": "200:1,6000:60,14000:3600",
    "telemetryMessages": "100:1,3000:60,7000:3600",
    "telemetryDataPoints": "200:1,6000:60,14000:3600"
  },
  "gatewayRateLimits": {
    "messages": "200:1,6000:60,14000:3600",
    "telemetryMessages": "100:1,3000:60,7000:3600",
    "telemetryDataPoints": "200:1,6000:60,14000:3600"
  }
}
```

<b><font size="3">Gateway rate limits description</font></b>   
- **rateLimits** - rate limits that apply to the gateway device itself.
- **gatewayRateLimits** - rate limits that apply to individual devices connected through the gateway.

These limits help control load and ensure stable operation when multiple devices communicate through a single gateway connection.

<hr>

## Claiming devices

The Device Claiming feature allows end users to securely associate a device with their account after the device has been deployed and connected to SENTIENT.
For a detailed explanation of the device claiming workflow and supported scenarios, refer to the [Claiming devices](/docs/user-guide/claiming-devices) documentation.

In order to initiate claiming device, send PUBLISH message to the following topic:

```bash
v1/devices/me/claim
```


The supported data format is:

```json
{"secretKey":"value", "durationMs":60000}
```


<div class="st-callout info">


**Please note** that the above fields are optional. In case the **secretKey** is not specified, the empty string as a default value is used.
In case the **durationMs** is not specified, the system parameter **device.claim.duration** is used (in the file **/etc/sentient/conf/sentient.yml**).


</div>


<hr>

## Device provisioning

Device provisioning allows devices to be registered dynamically without manual creation in the SENTIENT UI.
For a detailed explanation of the provisioning process and supported scenarios, refer to the [Device provisioning](/docs/user-guide/device-provisioning) documentation.

**Provisioning request**   
To initiate device provisioning, send Provisioning request to the following topic:

```bash
/provision
```


Also, you should set **username** or **clientId** to *provision*.

**Request Payload**   
The provisioning request must use the following JSON format:

```json
{
  "deviceName": "DEVICE_NAME",
  "provisionDeviceKey": "u7piawkboq8v32dmcmpp",
  "provisionDeviceSecret": "jpmwdn8ptlswmf4m29bw"
}
```

**Payload fields**
- **deviceName** — the name of the device to be provisioned.
- **provisionDeviceKey** — the provisioning key configured in SENTIENT.
- **provisionDeviceSecret** — the provisioning secret associated with the provisioning key.

If the provided credentials are valid, SENTIENT automatically creates the device (if it does not already exist) and returns the device credentials, allowing the device to start communicating with the platform.

<hr>

## Firmware API

When SENTIENT initiates an MQTT device firmware update, it sets the fw_title, fw_version, fw_checksum, fw_checksum_algorithm shared attributes.
To receive the shared attribute updates, the device has to subscribe to 

```bash
v1/devices/me/attributes/response/+
```


Where

**+** is the Wildcard character.

When the MQTT device receives updates for fw_title and fw_version shared attributes, it has to send PUBLISH message to

```bash
v2/fw/request/${requestId}/chunk/${chunkIndex} 
```


Where

**${requestId}** - number corresponding to the number of firmware updates. The ${requestId} has to be different for each firmware update.  
**${chunkIndex}** - number corresponding to the index of firmware chunks. The ${chunkID} are counted from 0. The device must increment the chunk index for each request until the received chunk size is zero.  
And the MQTT payload should be the size of the firmware chunk in bytes.

For each new firmware update, you need to change the request ID and subscribe to 

```bash
v2/fw/response/+/chunk/+
```


Where

**+** is the Wildcard character.

<hr>

## Protocol customization

MQTT transport can be fully customized for specific use-case by changing the corresponding [module](https://github.com/sentient/sentient/tree/master/transport/mqtt).

<hr>

## Next steps
