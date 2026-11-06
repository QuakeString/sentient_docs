+++
title = "MQTT Integration"
description = "MQTT Integration guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/mqtt.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only [**Professional Edition**](/products/sentient-pe/) supports **Platform Integrations** feature.<br>
Use [**SENTIENT Cloud**](/installations/choose-region/) or [**install**](/docs/user-guide/install/pe/installation-options/) your own platform instance.


</div>

MQTT Integration allows to connect to external MQTT brokers, subscribe to data streams from those brokers and convert any type of payload from your devices to SENTIENT message format. Its typical use is whenever your devices are already connected to external MQTT broker or any other IoT platform or connectivity provider with MQTT based back-end. 

Please review the integration diagram to learn more. 

<object width="100%" style="max-width: max-content;" data="/images/user-guide/integrations/mqtt-integration.svg"></object>

SENTIENT MQTT Integration acts as an MQTT client. It subscribes to topics and converts the data into telemetry and attribute updates. In case of downlink message, MQTT integration converts it to the device-suitable format and pushes to external MQTT broker. 
Pay attention: MQTT broker should be either co-located with SENTIENT instance or deployed in the cloud and have a valid DNS name or static IP address. SENTIENT instance that is running in the cloud can’t connect to the MQTT broker deployed in local area network.

## MQTT Integration Configuration

In this tutorial, we will configure MQTT Integration to provide devices connection to the Platform and ability to send RPC commands to devices.

### Prerequisites

In this tutorial, we will use:


- The instance of [SENTIENT Professional Edition](https://sentient.invenia.in/docs/user-guide/install/pe/installation-options/) installed locally;
  
  
 - MQTT broker, accessible by SENTIENT Professional Edition instance — broker.hivemq.com (port 1883);
 - mosquitto_pub and mosquitto_sub MQTT clients to send and receive messages;   
 - an advanced [device simulator](/docs/user-guide/integrations/resources/mqtt-client.py) for RPC simulation example.

Let's assume that we have a sensor which is sending current temperature readings.
Our sensor device *SN-001* publishes it's temperature readings to '**tb/mqtt-integration-tutorial/sensors/SN-001/temperature**' and it is subscribed to '**tb/mqtt-integration-tutorial/sensors/SN-001/rx**' to receive RPC calls.

### SENTIENT setup

Before setting up an MQTT integration, you need to create uplink and downlink converters.

Uplink converter is a script for parsing and transforming the data received by MQTT integration.

Downlink converter parses and transforms the data sent from SENTIENT to the format that is consumed by existing device(s).

#### Uplink Converter

The purpose of the decoder function is to parse the incoming data and metadata to a format that SENTIENT can consume.
*deviceName* and *deviceType* are required, while *attributes* and *telemetry* are optional.
*Attributes* and *telemetry* are flat key-value objects. Nested objects are not supported.

To create an uplink converter go to the **Integrations center** -> **Data converters** page and click "plus" button.
Name it "**MQTT Uplink Converter**" and select type **Uplink**. Use **debug mode** for now.

<b><font size="3">Debug mode</font></b>

Enabling debug mode allows you to track events, states, and potential errors related to the execution of integrations. This greatly simplifies development and troubleshooting.


<div class="st-callout info">


**Note:** Debug mode can quickly increase disk usage because all debug events are stored in the database.
Starting from **SENTIENT 3.9**, the platform stores the full set of debug events only during the first **15 minutes** after the integrations is created; afterward, only error events are retained.


</div>


Debug mode settings can be combined or disabled entirely.

> One can use either [TBEL](/docs/pe/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/pe/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

Now copy & paste the following script to the Decoder function section:

```javascript
/** Decoder **/

// decode payload to string
var payloadStr = decodeToString(payload);
var data = JSON.parse(payloadStr);

var deviceName =  metadata.topic.split("/")[3];
// decode payload to JSON
var deviceType = 'sensor';

// Result object with device attributes/telemetry data
var result = {
    deviceName: deviceName,
    deviceType: deviceType,
    attributes: {
        integrationName: metadata['integrationName'],
    },
    telemetry: {
        temperature: data.value,
    }
};

/** Helper functions 'decodeToString' and 'decodeToJson' are already built-in **/

return result;
``` 


![image](/images/user-guide/integrations/mqtt/mqtt-integration-add-uplink-converter-tbel-1-pe.webp)

</div>

<div class="st-tab" data-label="JavaScript">

Now copy & paste the following script to the Decoder function section:

```javascript
/** Decoder **/

// decode payload to string
var payloadStr = decodeToString(payload);
var data = JSON.parse(payloadStr);

var deviceName =  metadata.topic.split("/")[3];
// decode payload to JSON
var deviceType = 'sensor';

// Result object with device attributes/telemetry data
var result = {
    deviceName: deviceName,
    deviceType: deviceType,
    attributes: {
        integrationName: metadata['integrationName'],
    },
    telemetry: {
        temperature: data.value,
    }
};

/** Helper functions **/

function decodeToString(payload) {
    return String.fromCharCode.apply(String, payload);
}

function decodeToJson(payload) {
    // convert payload to string.
    var str = decodeToString(payload);

    // parse string to JSON
    var data = JSON.parse(str);
    return data;
}

return result;
``` 


![image](/images/user-guide/integrations/mqtt/mqtt-integration-add-uplink-converter-java-1-pe.webp)

</div>

</div>


#### Downlink Converter

The Downlink converter transforming outgoing RPC message and then the Integration sends it to external MQTT broker.


<div class="st-callout info">


**NOTE:**
<br>
Even if you won't send downlink RPC, you still need to create a dummy Downlink converter.


</div>


Create another converter with the name "**MQTT Downlink Converter**" and type **Downlink**. Leave the default script and click **Add**.     

> One can use either [TBEL](/docs/pe/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/pe/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

Now copy & paste the following script to the Encoder function section:

```javascript
// Encode downlink data from incoming Rule Engine message

// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter

/** Encoder **/

var data = {};

// Process data from incoming message and metadata

data.tempFreq = msg.temperatureUploadFrequency;
data.humFreq = msg.humidityUploadFrequency;

data.devSerialNumber = metadata['ss_serialNumber'];

// Result object with encoded downlink payload
var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",

    // downlink data
    data: JSON.stringify(data),

    // Optional metadata object presented in key/value format
    metadata: {
        topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'
    }

};

return result;

``` 


![image](/images/user-guide/integrations/mqtt/mqtt-integration-add-downlink-converter-tbel-1-pe.webp)

</div>

<div class="st-tab" data-label="JavaScript">

Now copy & paste the following script to the Encoder function section:

```javascript
// Encode downlink data from incoming Rule Engine message

// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter

/** Encoder **/

var data = {};

// Process data from incoming message and metadata

data.tempFreq = msg.temperatureUploadFrequency;
data.humFreq = msg.humidityUploadFrequency;

data.devSerialNumber = metadata['ss_serialNumber'];

// Result object with encoded downlink payload
var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",

    // downlink data
    data: JSON.stringify(data),

    // Optional metadata object presented in key/value format
    metadata: {
        topic: metadata['deviceType']+'/'+metadata['deviceName']+'/upload'
    }

};

return result;

``` 


![image](/images/user-guide/integrations/mqtt/mqtt-integration-add-downlink-converter-java-1-pe.webp)

</div>

</div>


#### MQTT Integration Setup

- Go to the **Integrations center** -> **Integrations** page and click "plus" icon to add a new integration. Name it "**MQTT Integration**", select type **MQTT**;

![image](/images/user-guide/integrations/mqtt/mqtt-integration-add-integration-1-pe.webp)

- The next steps is to add the recently created **uplink** and **downlink** converters;

![image](/images/user-guide/integrations/mqtt/mqtt-integration-add-integration-2-pe.webp)

![image](/images/user-guide/integrations/mqtt/mqtt-integration-add-integration-3-pe.webp)

- Specify **host**: **broker.hivemq.com** and **port**: **1883** at the connection step;
- Add a **topic filter**:

```bash
tb/mqtt-integration-tutorial/sensors/+/temperature
```


 - You can also select an MQTT **QoS** level. We use MQTT QoS level 0 (At most once) by default;

![image](/images/user-guide/integrations/mqtt/mqtt-integration-add-integration-4-pe.webp)

- Go to the **advanced settings**. It is better to uncheck the **Clean session** parameter. Many brokers do not support sticky sessions, so will silently close the connection if you try to connect with this option enabled;
- Let's leave the **Downlink topic pattern** by default, meaning that the Integration will take the metadata.topic and use it as the downlink topic;

![image](/images/user-guide/integrations/mqtt/mqtt-integration-add-integration-5-pe.webp)

- [Optional] Click on **Check connection** button to check connection to your Service Bus topic. Click **Add** button to create the integration.

![image](/images/user-guide/integrations/mqtt/mqtt-integration-add-integration-6-pe.webp)

#### Send Uplink message

Now let's simulate the device sending a temperature reading to the integration. 

Use terminal for will send a message with temperature readings in a simple format: *`{"value":25.1}`*:

```bash
mosquitto_pub -h broker.hivemq.com -p 1883 -t "tb/mqtt-integration-tutorial/sensors/SN-001/temperature" -m '{"value":25.1}'
```


![image](/images/user-guide/integrations/mqtt/mqtt-integration-send-uplink-message-1.webp)


After you sent uplink message a new device was created. You should receive a notification about it. 
To view notification click on the bell icon in the upper right corner of the screen. 
The notification will contain link to created device. Go to this device.

![image](/images/user-guide/integrations/mqtt/mqtt-integration-go-to-devices-1-pe.webp)

Here you will see information about the new device. As well as the telemetry which we sent to the device.

![image](/images/user-guide/integrations/mqtt/mqtt-integration-go-to-devices-2-pe.webp)

Learn more about *notifications* and how to configure them [here](/docs/pe/user-guide/notifications/).


Go back to your **Integrations** page and navigate to the **Events** tab. There you'll see the message consumed by the **MQTT Integration**.


![image](/images/user-guide/integrations/mqtt/mqtt-integration-events-1-pe.webp)


On **Events** tab of your **MQTT Uplink Converter** there will be "*In*", "*Out*", and "*Metadata*" columns. 
The "*In*" and "*Metadata*" are the input for the data converter, and "*Out*" is the result.


![image](/images/user-guide/integrations/mqtt/mqtt-integration-converter-events-1-pe.webp)


<br>
**Summary:** the Uplink Data Converter defines provisioning of device and interpreting the input data. 
In our example we capture the device name from the topic (SN-001), set the default device type (sensor) and populate a telemetry value to it. 
In more complex cases you can write a script that will take this data from any part of data or metadata.

### Send One-Way RPC to Device

This section describes how to send a one-way RPC request to the device using Control Widgets.

- Go to the **Dashboards** page and create a new dashboard named **MQTT RPC**. Open the dashboard add an alias by clicking on **Entity aliases** icon;
- Name the alias (**Sensor**, for example), select filter type **Single Entity**, type **Device** and choose our **SN-001** sensor. Press **Add** and then **Save**;
- Now add a new widget, select the **Control Widgets** bundle from drop down menu and select the **Knob Control** widget;
- On the **Data** field select created alias (**Sensor**). Set **Number of digits after floating point** to 0;
- Go to **Advanced** tab and set **Minimum value** to 15 and **Maximum value** to 45. Leave the rest by default. Click **Add** to create widget;
- Save changes.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-new-dashboard-1-pe.webp" alt="Go to Dashboards page and create a new dashboard named MQTT RPC. Open this dashboard;" loading="lazy"><figcaption>Go to Dashboards page and create a new dashboard named MQTT RPC. Open this dashboard;</figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-new-dashboard-2-pe.webp" alt="Add an alias by clicking on Entity Aliases icon on the top-right. Name the alias (Sensor, for example), select filter type &quot;Single Entity&quot;, type &quot;Device&quot; and choose our SN-001 sensor. Press Add and then Save;" loading="lazy"><figcaption>Add an alias by clicking on Entity Aliases icon on the top-right. Name the alias (Sensor, for example), select filter type "Single Entity", type "Device" and choose our SN-001 sensor. Press Add and then Save;</figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-new-dashboard-4-pe.webp" alt="Now Add New Widget;" loading="lazy"><figcaption>Now Add New Widget;</figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-new-dashboard-5-pe.webp" alt="Select Control Widgets from drop down menu;" loading="lazy"><figcaption>Select Control Widgets from drop down menu;</figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-new-dashboard-6-pe.webp" alt="Select Knob Control widget;" loading="lazy"><figcaption>Select Knob Control widget;</figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-new-dashboard-7-pe.webp" alt="On the Data field select created alias (Sensor). Set Number of digits after floating point to 0;" loading="lazy"><figcaption>On the Data field select created alias (Sensor). Set Number of digits after floating point to 0;</figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-new-dashboard-8-pe.webp" alt="Go to Advanced tab and set Minimum value to 15 and Maximum value to 45. Leave the rest by default. Click Add to create widget;" loading="lazy"><figcaption>Go to Advanced tab and set Minimum value to 15 and Maximum value to 45. Leave the rest by default. Click Add to create widget;</figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-new-dashboard-9-pe.webp" alt="Save the changes to the dashboard." loading="lazy"><figcaption>Save the changes to the dashboard.</figcaption></figure></div>


Now go to the **Rule Chains** page and open **Root Rule Chain**. Double-click on **message type switch** node and enable the **Debug mode** on it. 


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-edit-message-type-switch-1-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-edit-message-type-switch-2-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-create-edit-message-type-switch-3-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Now go back to your dashboard and turn knob a couple of times. 


![image](/images/user-guide/integrations/mqtt/mqtt-integration-turn-knob-1-pe.webp)


In the **message type switch** node on the **Events** tab you should then see incoming messages with the message type *RPC_CALL_FROM_SERVER_TO_DEVICE* and relation type *RPC Request to Device*. You can check out what data and metadata was sent by the Knob Control to the Rule Engine.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-incoming-messages-2-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-incoming-messages-3-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


To make sensor performing this command you need **RPC Request to Device** type messages to be forwarded to the downlink data converter.
In the Root Rule Chain editor find the **integration downlink** node, drag and drop it to the rule chain. Name it **MQTT Integration Downlink**, select our **MQTT Integration** and click **Add**.
Drag a connection from Message Type Switch node to MQTT Integration Downlink node with label "RPC Request to Device" and click add.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-integration-downlink-node-1-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-integration-downlink-node-2-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/mqtt/mqtt-integration-integration-downlink-node-3-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Go to the **Data converters** page, open your "**MQTT Downlink Converter**" and replace the default script with this one:


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

```js
/** Encoder **/

var value = parseInt(msg.params.replaceAll("[\"]",""));
var data = {value: value};
// Result object with encoded downlink payload
var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",

    // downlink data
    data: JSON.stringify(data),

    // Optional metadata object presented in key/value format
    metadata: {
        topic: 'tb/mqtt-integration-tutorial/sensors/'+metadata['deviceName']+'/rx'
    }

};

return result;
```


![image](/images/user-guide/integrations/mqtt/mqtt-integration-edit-downlink-converter-tbel-1-pe.webp)

</div>

<div class="st-tab" data-label="JavaScript">

```js
/** Encoder **/

var value = parseInt(msg.params.replace(/"/g,""));
var data = {value: value};
// Result object with encoded downlink payload
var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",

    // downlink data
    data: JSON.stringify(data),

    // Optional metadata object presented in key/value format
    metadata: {
        topic: 'tb/mqtt-integration-tutorial/sensors/'+metadata['deviceName']+'/rx'
    }

};

return result;
```


![image](/images/user-guide/integrations/mqtt/mqtt-integration-edit-downlink-converter-java-1-pe.webp)

</div>

</div>


The script above removes quotes from *msg.params* value, which comes as quoted string, and parses it to integer. Then it builds a result object which is passed to the Integration.
The result object structure should be followed: the data (the message payload sent to the external MQTT broker as-is) and the metadata (is used by Integrationin). As mentioned: the Integration downlink topic is configured to **${topic}**, which means that the integration will take the metadata.topic and use it as the downlink topic.

Open the terminal window and execute the following command:

```bash
mosquitto_sub -h broker.hivemq.com -p 1883 -t "tb/mqtt-integration-tutorial/sensors/+/rx"
```


![image](/images/user-guide/integrations/mqtt/mqtt-integration-execute-command.webp)

Go to the dashboard and turn the wheel again. In your terminal window you should receive series of the incoming messages sent by thew knob control widget:
```bash
{"value":33}
{"value":42}
```


![image](/images/user-guide/integrations/mqtt/mqtt-integration-turn-the-wheel-1-pe.webp)

![image](/images/user-guide/integrations/mqtt/mqtt-integration-turn-the-wheel-2-pe.webp)


### Simulating of Two-Way RPC 

Now try to simulate sending an RPC request to the device with recieving a response.

First you should modify converters to send downlink messages to '**tb/mqtt-integration-tutorial/sensors/+/rx/twoway**' topic and receive device responses on 
**tb/mqtt-integration-tutorial/sensors/+/rx/response**' topic.

Change downlink converter code to send messages to '**tb/mqtt-integration-tutorial/sensors/+/rx/twoway**' topic. Go to the "**MQTT Downlink Converter**" and change the code on line 16 to

```bash
topic: 'tb/mqtt-integration-tutorial/sensors/'+metadata['deviceName']+'/rx/twoway'
```


Or just paste the following code in the encoder window:


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

```js
/** Encoder **/

var value = parseInt(msg.params.replaceAll("[\"]",""));
var data = {value: value};
// Result object with encoded downlink payload
var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",

    // downlink data
    data: JSON.stringify(data),

    // Optional metadata object presented in key/value format
    metadata: {
        topic: 'tb/mqtt-integration-tutorial/sensors/'+metadata['deviceName']+'/rx/twoway'
    }

};

return result;
```


![image](/images/user-guide/integrations/mqtt/mqtt-rpc-edit-downlink-tbel-3-pe.webp)

</div>

<div class="st-tab" data-label="JavaScript">

```js
/** Encoder **/

var value = parseInt(msg.params.replace(/"/g,""));
var data = {value: value};
// Result object with encoded downlink payload
var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",

    // downlink data
    data: JSON.stringify(data),

    // Optional metadata object presented in key/value format
    metadata: {
        topic: 'tb/mqtt-integration-tutorial/sensors/'+metadata['deviceName']+'/rx/twoway'
    }

};

return result;
```


![image](/images/user-guide/integrations/mqtt/mqtt-rpc-edit-downlink-java-3-pe.webp)

</div>

</div>


Then prepare the uplink converter to receive the response messages. Go to the "**MQTT Uplink Converter**" and paste the following code in the decoder window:


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

```js
/** Decoder **/

// decode payload to string
var payloadStr = decodeToString(payload);
var data = JSON.parse(payloadStr);
var deviceName =  metadata.topic.split("/")[3];
// decode payload to JSON
var deviceType = 'sensor';

// Result object with device attributes/telemetry data
var telemetry;
if (metadata.topic.endsWith('/temperature')) {
    // Transform the incoming data as before
    telemetry = getTemperatureTelemetry(data);
} else if (metadata.topic.endsWith('/rx/response')) {
    // Get the input value as is
    telemetry = data;
}

var result = {
    deviceName: deviceName,
    deviceType: deviceType,
    attributes: {
        integrationName: metadata['integrationName'],
    },
    telemetry: telemetry
};

/** Helper functions 'decodeToString' and 'decodeToJson' are already built-in **/

return result;
```


![image](/images/user-guide/integrations/mqtt/mqtt-rpc-edit-uplink-tbel-3-pe.webp)

</div>

<div class="st-tab" data-label="JavaScript">

```js
/** Decoder **/

// decode payload to string
var payloadStr = decodeToString(payload);
var data = JSON.parse(payloadStr);
var deviceName =  metadata.topic.split("/")[3];
// decode payload to JSON
var deviceType = 'sensor';

// Result object with device attributes/telemetry data
var telemetry;
if (metadata.topic.endsWith('/temperature')) {
    // Transform the incoming data as before
    telemetry = getTemperatureTelemetry(data);
} else if (metadata.topic.endsWith('/rx/response')) {
    // Get the input value as is
    telemetry = data;
}

var result = {
    deviceName: deviceName,
    deviceType: deviceType,
    attributes: {
        integrationName: metadata['integrationName'],
    },
    telemetry: telemetry
};

/** Helper functions **/

function getTemperatureTelemetry(data) {
    return {temperature: data.value}
}

function decodeToString(payload) {
    return String.fromCharCode.apply(String, payload);
}

function decodeToJson(payload) {
    // covert payload to string.
    var str = decodeToString(payload);

    // parse string to JSON
    var data = JSON.parse(str);
    return data;
}

return result;
```


![image](/images/user-guide/integrations/mqtt/mqtt-rpc-edit-uplink-java-3-pe.webp)

</div>

</div>


The script above is slightly different from what we had initially. It distinguishes between Post Telemetry requests and RPC call Responses, thus publishing different kind of output to Rule Engine.

You also must add a topic filter in your integration to receive the RPC response messages: **MQTT Integration** -> **Topic filters** -> **Add topic filter**. 
Add this topic with the default **QoS** level:

```bash
tb/mqtt-integration-tutorial/sensors/+/rx/response
```


Apply changes.


![image](/images/user-guide/integrations/mqtt/mqtt-rpc-edit-integration-1-pe.webp)


Now run device emulator. Notice, the **mosquitto_pub** and **mosquitto_sub** is not suffice, so please launch an [advanced simulator](/docs/user-guide/integrations/resources/mqtt-client.py):

```js
python mqtt-client.py
```


![image](/images/user-guide/integrations/mqtt/mqtt-rpc-send-message-2.webp)

Try to turn the knob wheel on a dashboard. In the terminal window you should have an output similar to :

```bash
Incoming message
Topic: tb/mqtt-integration-tutorial/sensors/SN-001/rx/twoway
Message: {"value":40}
This is a Two-way RPC call. Going to reply now!
Sending a response message: {"rpcReceived":"OK"}
```


![image](/images/user-guide/integrations/mqtt/mqtt-rpc-turn-the-wheel-1-pe.webp)


Go to the **Devices** page and find *rpcReceived* telemetry value is "*OK*" on the **Latest telemetry** tab of your SN-001 device.


![image](/images/user-guide/integrations/mqtt/mqtt-rpc-device-1-pe.webp)


### MQTT retransmission mechanism

The MQTT integration uses SENTIENT's internal MQTT client.


SENTIENT's internal MQTT client includes a retransmission mechanism designed to improve reliability for message types that require acknowledgment.  
This mechanism applies specifically to the following MQTT message types:
- **PUBLISH** (only for QoS 1 or 2)
- **SUBSCRIBE**
- **UNSUBSCRIBE**
- **PUBREL** (only for QoS 2)

When one of these messages is sent, the client waits for an acknowledgment within a configurable delay period.  
If no acknowledgment is received, the message is retransmitted. The delay between retransmissions follows an **exponential backoff** strategy, starting from an initial delay and doubling with each attempt.  
A **jitter factor** introduces random variance into the delay to help prevent synchronized retries.

For example, if the retransmission configuration is set to **three attempts**, with an **initial delay of 5,000 ms** and a **jitter factor of 0.15**, the retransmission attempts would be scheduled at approximately **5,000 ms**, **10,000 ms**, and **20,000 ms**, each adjusted by ±15% jitter.  
If no acknowledgment is received after the final attempt, the system waits through the next scheduled delay—based on exponential backoff with jitter—before finally considering the message **undeliverable and dropping it**.


You can configure retransmission parameters globally in the `sentient.yml` file. These settings affect **all MQTT clients** on the platform:

```yaml
mqtt:
  client:
    retransmission:
      max_attempts: "${TB_MQTT_CLIENT_RETRANSMISSION_MAX_ATTEMPTS:3}"
      initial_delay_millis: "${TB_MQTT_CLIENT_RETRANSMISSION_INITIAL_DELAY_MILLIS:5000}"
      jitter_factor: "${TB_MQTT_CLIENT_RETRANSMISSION_JITTER_FACTOR:0.15}"
```


When the MQTT message is dropped, the corresponding rule engine message is routed via **Failure** chain with the appropriate exception message.

## Video tutorials

### Setting up MQTT Integration

This video is a step-by-step tutorial on setting up of MQTT Integration.

<br>
<div id="video">  
 <div id="video_wrapper">
     <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/BeN5bsDQbdo" frameborder="0" allowfullscreen></iframe>
 </div>
</div> 

### Configure RPC request to the device

For your convenience you may follow this video to configure RPC request to device and receive simulated response via MQTT Integration.

<br>
<div id="video">  
 <div id="video_wrapper">
     <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/A_jCXQj_LXs" frameborder="0" allowfullscreen></iframe>
 </div>
</div> 

## Next steps
