+++
title = "Platform Integrations"
description = "Platform Integrations Documentation"

aliases = ["/docs/user-guide/integrations/ibm-watson-iot/"]
[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/index.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

SENTIENT Platform integrations feature was designed for two primary use cases / deployment options:

- Connect existing NB IoT, LoRaWAN, SigFox and other devices with specific payload formats directly to SENTIENT platform.
- Stream data from devices connected to existing IoT Platforms to enable real-time interactive dashboards and efficient data processing.
  
Both use cases have few things in common. There is a server-side component in the deployment topology that prevents direct access to device and provides set of APIs to interact with the device in the field instead.
The payload format of the device is not well-defined. Often two devices that have similar sensors have different payload formats depending on a vendor or even software version.  

The job of SENTIENT Integration is to provide secure and reliable API bridge between core platform features (telemetry collection, attributes and RPC calls) and specific third-party platform APIs.    

## How it works?

At the moment SENTIENT supports various integration protocols. Most popular are HTTP, MQTT and OPC-UA. 
Platform also support integration with specific LoRaWAN Network servers, Sigfox backend, various NB IoT devices using raw UDP and TCP integrations. 
AWS IoT, IBM Watson and Azure Event Hub allows to subscribe to the data feed from devices via MQTT or AMQP.

![image](/images/user-guide/integrations/overview/create-integration-1.webp)

The list of platform integrations is constantly growing, however, the general integration concepts are the same and explained below.  

Once message arrives from External Platform to SENTIENT it passes validation according to platform specific payload format and security rules. 
Once message is validated SENTIENT Integration invokes assigned [**Uplink data converter**](#uplink-data-converter) to extract sub-set of meaningful information out of the incoming message.
The message is basically transformed from device and platform specific payload to the format that SENTIENT uses.

Since TB PE v2.0, Rule Engine is also able to push Downlink messages to the integrations. The example of such message may be:
 
 - notification about [shared attribute](/docs/user-guide/attributes/#device-specific-attribute-types) (configuration) update;
 - notification about [oneway RPC call](/docs/user-guide/rpc/#server-side-rpc-api) to trigger some action on the device;
 - any custom message from the rule engine.
 
The most common use cases are:
 
 - changing data upload frequency based on shared attribute value change
 - triggering firmware update procedure based on shared attribute value change
 - changing device state based on rpc call;    
 
Once message is pushed by the rule engine, SENTIENT invokes assigned [**Downlink data converter**](#downlink-data-converter) and transforms the rule engine message to the specific data format that is used by the Integration.

<br>

<object width="100%" data="/images/user-guide/integrations/integrations-overview.svg"></object>
 
## Uplink data converter

The primary function of the Uplink data converter is to parse the payload of incoming messages from devices (e.g., MQTT, HTTP, CoAP, or other protocols) and convert it into a format that SENTIENT can process.

Starting from SENTIENT version 4.0, we have simplified the process of writing converters for certain integrations that receive payload messages with the same structure.
You can now easily choose where the message fields from the integration should go (attributes or telemetry) without manually defining this in the decoder function.

This feature applies to uplink converters for the following integrations:

- [ChirpStack](/docs/user-guide/integrations/chirpstack/)
- [Loriot](/docs/user-guide/integrations/loriot/)
- [The Things Stack Community](/docs/user-guide/integrations/ttn/)
- [The Things Stack Industries](/docs/user-guide/integrations/tti/)
- **ThingPark**
- **ThingPark Enterprise**

> Converters created before the release of SENTIENT 4.0 will still be available and will continue to function properly.

### Generic Uplink data converter

To create a generic Uplink data converter suitable for all integration types, follow these steps:

- Navigate to the "**Data converters**" section in the "**Integration center**", click the "**plus**" icon button, and In the dropdown menu, select "**Create new converter**".
- In the new window:
  - Make sure the converter type selector is set to "**Uplink**".
  - Select the **integration type** where this converter will be used (e.g., [MQTT](/docs/user-guide/integrations/mqtt/), [OPC-UA](/docs/user-guide/integrations/opc-ua/), etc.), or leave it set to "All" if it will be used across multiple integrations.
  - Enter a name for the converter.
  - (Optional) Enable **Debug mode** if you need to troubleshoot the converter during development or testing.


<b><font size="3">Debug mode</font></b>

Enabling debug mode allows you to track events, states, and potential errors related to the execution of uplink converter. This greatly simplifies development and troubleshooting.


<div class="st-callout info">


**Note:** Debug mode can quickly increase disk usage because all debug events are stored in the database.
Starting from **SENTIENT 3.9**, the platform stores the full set of debug events only during the first **15 minutes** after the uplink converter is created; afterward, only error events are retained.


</div>


Debug mode settings can be combined or disabled entirely.

- In the **Main decoding configuration** section, define the decoding logic: use the provided default script or enter your custom script to parse and transform the incoming data.

> One can use either [TBEL](/docs/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.

![image](/images/user-guide/integrations/overview/adding-uplink-converter-1.webp)

- Configure **advanced decoding parameters**:
  - To prevent unnecessary updates for telemetry or attribute values, you can use the "**Update only keys list**" field. Keys specified in this list will only be updated if their values have changed compared to the previous ones. If a listed key appears in the converted message but its value remains the same, the update will be skipped.
  > **Please note** that in a cluster setup, values, associated with keys specified in the "Update only keys list" field may be updated more than once if a message is received by a different integration executor nodes. The same behavior is expected if the converter configuration has been updated.  
- Once everything is set up, click the "**Add**" button to create and save the new converter.

![image](/images/user-guide/integrations/overview/adding-uplink-converter-2.webp)

### Typed Uplink data converter

The typed Uplink data converter is designed for use with a specific integration type.
To create the Uplink data converter for an integration that supports the **new uplink converter functionality** ([ChirpStack](/docs/user-guide/integrations/chirpstack/), [Loriot](/docs/user-guide/integrations/loriot/), [The Things Stack Community](/docs/user-guide/integrations/ttn/), [The Things Stack Industries](/docs/user-guide/integrations/tti/), ThingPark, ThingPark Enterprise), follow these steps:

- The "**Integration type**" field lists all supported integrations. For this example, I&#39;ll use [Loriot](/docs/user-guide/integrations/loriot/).
- Specify a name for the converter.
- Go to the "**Main decoding configuration**" section: 
  - Select the entity type (**Device** or **Asset**) that will be created as a result of the integration, and specify the entity name.
  > The Entity name field is mandatory, so it cannot be left empty. By default, the entity name follows the pattern **Device $eui** (or **Asset $eui**). Here you need to underline the pattern **$** in the device name. As you type **$**, a list of available keys from the Loriot message will appear. This list is standardized and does not depend on the specific message content. The **$eui** pattern will dynamically fetch the device&#39;s unique identifier from the Loriot message.
- In the **Main decoding configuration** section, define the decoding logic: use the provided default script or enter your custom script to parse and transform the incoming data.

> One can use either [TBEL](/docs/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.

![image](/images/user-guide/integrations/overview/uplink-converter-20-1.webp)

- Configure **advanced decoding parameters**:
  - The **Device profile**, **Device label**, **Customer name**, and **Device group name** fields are not mandatory, and you can also use the **$** pattern to populate them dynamically.
  If the Device profile field is left empty, the device profile will be set to "default".
  - In the **Attributes** and **Telemetry** sections specify the keys that should be interpreted as attributes and telemetry, respectively.
  If a specified key is not present in the incoming message, it will be ignored by the converter.
  - To prevent unnecessary updates for telemetry or attribute values, you can use the "**Update only keys list**" field. Keys specified in this list will only be updated if their values have changed compared to the previous ones. If a listed key appears in the converted message but its value remains the same, the update will be skipped.
  > **Please note** that in a cluster setup, values, associated with keys specified in the "Update only keys list" field may be updated more than once if a message is received by a different integration executor nodes. The same behavior is expected if the converter configuration has been updated.
- Once everything is set up, click the "**Add**" button to create and save the new converter.

![image](/images/user-guide/integrations/overview/uplink-converter-20-2.webp)

### Test decoder function

When creating the Uplink data converter, you can validate the decoding logic used to process incoming device data.
To get started, click the "**Test payload decoder**" button. 
This allows you to simulate how your converter will handle real payloads and fine-tune your decoding function accordingly.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/overview/test-payload-decoder-1.webp" alt="Click the &quot;**Test payload decoder**&quot; button to validate the decoding logic used to process incoming device data." loading="lazy"><figcaption>Click the "**Test payload decoder**" button to validate the decoding logic used to process incoming device data.</figcaption></figure><figure><img src="/images/user-guide/integrations/overview/test-payload-decoder-2.webp" alt="Test decoder function window." loading="lazy"><figcaption>Test decoder function window.</figcaption></figure></div>


#### Payload

The **Payload** - this represents the encoded input data received from your device. 

> Note: Each supported integration has a pre-filled sample payload. You can use this as a starting point, or modify it to match the specific message format used by your integration.

The format can vary depending on the integration type and may be:
- **JSON**
- **TEXT**
- **Binary (Base64)**
  > For the **Binary (Base64) payload content type**, the payload is automatically decoded into a byte array, so there&#39;s no need to decode it manually in your script.

You can access the payload in your decoder script using the *payload* keyword.

#### Metadata

The **Metadata** is a key-value map that contains special fields provided by the integration.
You can reference these values in your decoder script using the metadata keyword.

Additionally, you can configure custom metadata parameters for each integration in its settings.
For example, you may define a metadata parameter such as deviceType and then use it in your script to automatically assign the appropriate device type when new devices are created.

#### Converter output

The **Converter output** displays the result in JSON format returned by your decoder function. This includes device value arrays (such as telemetry or attributes) and may also contain timestamps in telemetry values.
This allows you to compare and verify how the decoded data is ultimately interpreted and processed by SENTIENT.

> The only mandatory parameters in the output JSON are **deviceName** and **deviceType**.


<div class="st-callout info">


**NOTE**: Starting version 2.4.2, SENTIENT also supports **assetName** and **assetType** instead of deviceName and deviceType.


</div>


<div class="st-callout info">


**NOTE**: Starting version 2.4.2, SENTIENT also support optional **customerName** and **groupName**.
Those parameters will cause SENTIENT to automatically create customer and/or entity group and assign those entities to the customer and/or group.


</div>


Example of converter output data:

```json
{
  "entityType": "DEVICE",
  "name": "Device 1000000000000001",
  "profile": "default",
  "telemetry": [{
    "ts": 1684478801936,
    "values": {
      "battery": 95,
      "temperature": 36.6,
      "saturation": 99
    }
  }, {
    "rssi": -21,
    "data": "01755e030001040001",
    "battery": 94,
    "snr": 10,
    "fСnt": 2
  }],
  "attributes": {
    "serialNumber": "SN-12345678",
    "fPort": 85,
    "dr": "SF9 BW125 4/5",
    "frequency": 867500000,
    "eui": 1000000000000001
  }
}
```

## Downlink data converter

The main function of **downlink data converter** is to transform the incoming rule engine message and its metadata to the format that is used by corresponding Integration.


<div class="st-callout info">


**NOTE**: A Downlink Converter is generally optional. It is required only if your integration needs SENTIENT to send outgoing messages, such as RPCs, attribute updates, or other commands. If your integration only involves receiving data without initiating outbound communication, you can skip creating a Downlink Converter.


</div>


To create the Downlink data converter, follow these steps:
- Navigate to the "**Data converters**" section in the "**Integration center**", click the "**plus**" icon button, and In the dropdown menu, select "**Create new converter**".
- In the new window:
  - Switch the converter type selector to "**Downlink**".
  - Select the **integration type** where this converter will be used (e.g., [MQTT](/docs/user-guide/integrations/mqtt/), [OPC-UA](/docs/user-guide/integrations/opc-ua/), etc.), or leave it set to "All" if it will be used across multiple integrations.
  - Enter a name for the converter.
  - (Optional) Enable **Debug mode** if you need to troubleshoot the converter during development or testing.


<b><font size="3">Debug mode</font></b>

Enabling debug mode allows you to track events, states, and potential errors related to the execution of downlink converter. This greatly simplifies development and troubleshooting.


<div class="st-callout info">


**Note:** Debug mode can quickly increase disk usage because all debug events are stored in the database.
Starting from **SENTIENT 3.9**, the platform stores the full set of debug events only during the first **15 minutes** after the downlink converter is created; afterward, only error events are retained.


</div>


Debug mode settings can be combined or disabled entirely.

- In the **Main encoding configuration** section, define the decoding logic: enter **script** for parsing and transforming the output data.

> One can use either [TBEL](/docs/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.

- Click the "**Add**" button to create and save your new converter.

![image](/images/user-guide/integrations/overview/add-downlink-converter.webp)

<br>
Downlink Converter is basically a user defined function with the following signature:

```javascript
function encoder(msg, metadata, msgType, integrationMetadata);
```

where

ㅤ**&#42; msg** - JSON with rule engine msg<br>
ㅤ**&#42; metadata** - list of key-value pairs with additional data about the message (produced by the rule engine)<br>
ㅤ**&#42; msgType** - Rule Engine message type. See [predefined message types](/docs/user-guide/rule-engine-2-0/overview/#predefined-message-types) for more details<br>
ㅤ**&#42; integrationMetadata** - key-value map with some integration specific fields. You can configure additional metadata for each integration in the integration details
  
### Converter output

Converter output should be a valid JSON document with the following structure:

```json
{
    "contentType": "JSON",
    "data": "{\"tempFreq\":60,\"firmwareVersion\":\"1.2.3\"}",
    "metadata": {
        "topic": "temp-sensor/sensorA/upload"
    }
}
```

where

ㅤ**&#42; contentType** - JSON, TEXT or BINARY (Base64 string) and is specific to your Integration type<br>
ㅤ**&#42; data** - data string according to the content type<br>
ㅤ**&#42; metadata** - list of key-value pairs with additional data about the message. For example, topic to use for MQTT integration, etc.

### Synchronous vs asynchronous downlinks

Most of the integrations are able to process downlink messages to devices asynchronously.
For example, each message pushed by the rule engine to MQTT based integration is immediately pushed to the corresponding external MQTT broker.

However, some integrations, like SigFox or generic HTTP integration are not able to push message asynchroniously.
These integrations, due to the nature of underlying HTTP protocol, are only able to push downlink information synchronously in reply to uplink message request.
In this case, the last downlink message originated by rule engine will be stored in the queue until the new uplink message arrives for particular device.

### Example

Let&#39;s assume an example where temperature and humidity upload frequency attributes are updated via SENTIENT REST API and 
you would like to push this update to an external MQTT broker (TTN, Mosquitto, AWS IoT, etc.). 
You may also want to include the "firmwareVersion" attribute value that was configured long time ago and is not present in this particular request.
The topic to push the update should contain the device name.

> One can use either [TBEL](/docs/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

![image](/images/user-guide/integrations/downlink-converter-example-tbel.webp)


The full source code of TBEL function used in converter:

```bash
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

data.firmwareVersion = metadata['ss_firmwareVersion'];

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


</div>

<div class="st-tab" data-label="JavaScript">

![image](/images/user-guide/integrations/downlink-converter-example-java.webp)


The full source code of javascript function used in converter:

```bash
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

data.firmwareVersion = metadata['ss_firmwareVersion'];

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


</div>

</div>


In order to invoke the downlink processing by the integration, tenant administrator should configure the rule chain similar to the one below:

![image](/images/user-guide/integrations/downlink-rule-chain-example-pe.webp)

The full rule chain configuration is available [**here**](/docs/user-guide/resources/downlink-example-rule-chain.json).

## Converters library

SENTIENT Converters library is a built-in collection of ready-to-use uplink decoder functions for over 100 devices, supporting six popular LoRaWAN network servers.   
It significantly simplifies integration setup with various sensors and vendors.

Currently, the converters library is supported by the following integrations: [ChirpStack](/docs/user-guide/integrations/chirpstack/), [Loriot](/docs/user-guide/integrations/loriot/), [The Things Stack Community](/docs/user-guide/integrations/ttn/), [The Things Stack Industries](/docs/user-guide/integrations/tti/), **ThingPark**, and **ThingPark Enterprise**.   
In the future, the list of integrations that support the converters library will be expanded.

To access the Converters library:

- Navigate to the "**Integrations**" page under the "**Integrations center**" section. Click the "**plus**" icon button to start creating a new integration.
  - Select one of the integrations that currently support the Converters library. 
  - Click "**Next**" to proceed.
- In the "**Uplink data converter**" tab:
  - Switch to the "**Library**" option.
  - From the dropdown menu, choose the **device vendor**.
  - Then select the specific **sensor model** you are using. The corresponding decoder function will be automatically loaded into the editor.
  - If needed, configure advanced decoding options.
  - Click "**Next**".
- Continue the process to finalize the integration setup.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/overview/converters-library-1.webp" alt="Navigate to the &quot;**Integrations**&quot; page under the &quot;**Integrations center**&quot; section. Click the &quot;**plus**&quot; icon button to start creating a new integration. Select one of the integrations that currently support the converters library. Click &quot;**Next**&quot; to proceed." loading="lazy"><figcaption>Navigate to the "**Integrations**" page under the "**Integrations center**" section. Click the "**plus**" icon button to start creating a new integration. Select one of the integrations that currently support the converters library. Click "**Next**" to proceed.</figcaption></figure><figure><img src="/images/user-guide/integrations/overview/converters-library-2.webp" alt="Switch to the &quot;**Library**&quot; option. From the dropdown menu, choose the **device vendor**. Then select the specific **sensor model** you are using. The corresponding decoder function will be automatically loaded into the editor." loading="lazy"><figcaption>Switch to the "**Library**" option. From the dropdown menu, choose the **device vendor**. Then select the specific **sensor model** you are using. The corresponding decoder function will be automatically loaded into the editor.</figcaption></figure><figure><img src="/images/user-guide/integrations/overview/converters-library-3.webp" alt="If needed, configure advanced decoding options. Click &quot;**Next**&quot;. Continue the process to finalize the integration setup." loading="lazy"><figcaption>If needed, configure advanced decoding options. Click "**Next**". Continue the process to finalize the integration setup.</figcaption></figure></div>


The Converters library is open-source and actively maintained by the SENTIENT team. It is hosted on GitHub at the [following link](https://github.com/sentient/data-converters).


<br>**Using a custom converters repository**

You can [configure](/docs/user-guide/install/pe/how-to-change-config/) SENTIENT to use your own repository with personalized decoders for your specific devices instead of using the default converters library.

Set new environment variables in SENTIENT configuration file to define your custom repository and branch:

```
export TB_INTEGRATIONS_CONVERTERS_LIBRARY_REPO_URL=https://github.com/my-github-account/my-repo-name.git
export TB_INTEGRATIONS_CONVERTERS_LIBRARY_REPO_BRANCH=my-branch
```

where

ㅤ**&#42; TB_INTEGRATIONS_CONVERTERS_LIBRARY_REPO_URL** – URL of your GitHub (or other Git-based) repository<br>
ㅤ**&#42; TB_INTEGRATIONS_CONVERTERS_LIBRARY_REPO_BRANCH** – The branch name you want SENTIENT to pull the converters from (e.g., main, develop, or any custom branch name)

![image](/images/user-guide/integrations/overview/terminal-custom-repo-converters-library.webp)

Once configured, SENTIENT will pull device decoder functions directly from your custom Git repository.


## Debug mode

**Debug mode** is extremely useful for development and troubleshooting.
However, having it on all the time can significantly increase the disk space used by the database since all the debug data is stored there.
Therefore, starting from version 3.9, SENTIENT stores all debug events only during the first 15 minutes. After that, only failure events are retained.
These settings can be combined or completely disabled.

## Deployment options

SENTIENT Integration has two deployment options: embedded and remote. See details and architecture diagrams below.

### Embedded integrations

Embedded integration is running in the main SENTIENT server process. Basically it is part of a monolith deployment scenario.

Pros:
* simplifies deployment of new integration (just few clicks on SENTIENT UI);
* minimize latency for message delivery;

Cons:
* consume resources allocated to main SENTIENT process: network connections, OS threads and CPU cycles;
* low level of isolation;
* can&#39;t access local MQTT brokers or OPC-UA servers if SENTIENT is deployed in the cloud.

<object width="100%" data="/images/user-guide/integrations/embeded-integrations-overview.svg"></object>

### Remote integrations

Remote integration become available since SENTIENT Professional Edition v2.4.1 and enables new deployment scenario.
One can install remote integration in the local network and stream data to the cloud.

Let&#39;s assume you have local MQTT broker or OPC-UA server deployed on-premises.
Those brokers and/or servers don&#39;t have dedicated external IP address, so SENTIENT instance in the cloud can&#39;t connect to them directly.
However, you can install remote integration close to this server, in the same local network.
This integration will connect to the broker/server, pull the data and store it in the local file system.
Remote integration will stream the data to the SENTIENT instance deployed in the cloud once the internet connection is available.

Pros:
* enables integration with servers deployed in the local network;
* isolates the integration process from main SENTIENT process;

Cons:
* requires installation of a separate package;

Learn how to configure integration to run remotely using [this guide](/docs/user-guide/integrations/remote-integrations).

<object width="100%" data="/images/user-guide/integrations/remote-integrations-overview.svg"></object>

## Platform Integrations vs IoT Gateway

Experienced SENTIENT users may notice that functionality of Integrations feature partially overlap with functionality of [IoT Gateway](/docs/iot-gateway/what-is-iot-gateway/).
However, there are key differences between these two systems/features:

  - IoT Gateway is designed for local network deployments, Integrations are designed for server-to-server integrations.
  - IoT Gateway is designed to support < 1000 devices, while Integrations are designed for high throughput, scalability and cluster deployments as part of SENTIENT server.
  - Gateway recompilation and restart is required to add custom payload decoder while Integration Converter is a JS function that may be modified in real time. 
  
As you can see, both systems are important and applicable in different use cases.

## Feature Roadmap

### Usage statistics
 
We plan to log statistics for amount of messages processed by each integration with possible limitations of messages processed on a tenant / system levels.

### More integrations and protocols

We plan to provide specific integrations for different platforms, and also for different communication protocols, like gRPC.

### More data converters

We plan to collect and maintain data converters for most popular devices on the market to simplify integration path even more. 
Please note that you can share your converters with community and send them to us to make part of official SENTIENT distributive.   

Contact us to suggest missing feature for your use case.

## See also

Explore guides and video tutorials related to specific integrations:

 - [HTTP](/docs/user-guide/integrations/http/)
 - [MQTT](/docs/user-guide/integrations/mqtt/)
 - [AWS IoT](/docs/user-guide/integrations/aws-iot/)
 - [AWS Kinesis](/docs/user-guide/integrations/aws-kinesis/)
 - [IBM Watson IoT](/docs/user-guide/integrations/ibm-watson-iot/)
 - [Azure Event Hub](/docs/user-guide/integrations/azure-event-hub/)
 - [Azure IoT Hub](/docs/user-guide/integrations/azure-iot-hub/)
 - [Actility ThingPark](/docs/user-guide/integrations/thingpark/)
 - [TheThingsIndustries](/docs/user-guide/integrations/tti/)
 - [SigFox](/docs/user-guide/integrations/sigfox/)
 - [OceanConnect](/docs/user-guide/integrations/ocean-connect/)
 - [TheThingsStack](/docs/user-guide/integrations/ttn/)
 - [OPC-UA](/docs/user-guide/integrations/opc-ua/)
 - [TCP](/docs/user-guide/integrations/tcp/)
 - [UDP](/docs/user-guide/integrations/udp/)
 - [Custom](/docs/user-guide/integrations/custom/)
 - [LORIOT](/docs/user-guide/integrations/loriot/)
 - [Kafka](/docs/user-guide/integrations/kafka/)
 - [ChirpStack](/docs/user-guide/integrations/chirpstack/)
 - [CoAP](/docs/user-guide/integrations/coap/)

## Video tutorial

See the video tutorial below for step-by-step instructions on how to set up an Uplink data converter.

<br>
<div id="video">  
    <div id="video_wrapper">
        <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/CojStpYCTGI" frameborder="0" allowfullscreen></iframe>
    </div>
</div>


## Next steps
