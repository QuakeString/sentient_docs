+++
title = "ChirpStack Integration"
description = "ChirpStack Integration Guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/chirpstack.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only [**Professional Edition**](/products/sentient-pe/) supports **Platform Integrations** feature.<br>
Use [**SENTIENT Cloud**](/installations/choose-region/) or [**install**](/docs/user-guide/install/pe/installation-options/) your own platform instance.


</div>

The ChirpStack open-source LoRaWAN Network Server stack provides open-source components for LoRaWAN networks. After integrating ChirpStack with SENTIENT, you can connect, communicate, process and visualize data from devices in the SENTIENT IoT platform.

## Prerequisites

To receive data, you need to have a configured instance of the ChirpStack Network Server stack. In this guide, we’ll use a local instance installed via Docker compose.   
[Click here to learn how to install the ChirpStack Network Server using Docker Compose](https://www.chirpstack.io/project/guides/docker-compose/).

Additionally, you must connect your device to the network. You can find detailed instructions in the [official ChirpStack device connection guide](https://www.chirpstack.io/project/guides/connect-device/).

## Create ChirpStack integration

You will need to have access to SENTIENT Professional Edition. The easiest way is to use [SENTIENT Cloud](https://sentient.invenia.in/installations/choose-region/) server.
The alternative option is to install SENTIENT using [installation guide](/docs/user-guide/install/pe/installation-options/).

<br>
Let's move on to setting up the integration between the SENTIENT platform and ChirpStack.

**1. Basic settings**.

- Sign in to your SENTIENT account.
- Navigate to the "**Integrations**" page under the "**Integrations center**" section. Click "**plus**" button to add a new integration.
- From the list, select the integration type "**ChirpStack**".
- If you'd like to monitor events and troubleshoot, enable [debug mode](/docs/user-guide/integrations/#debug-mode).

<b><font size="3">Debug mode</font></b>

Enabling debug mode allows you to track events, states, and potential errors related to the execution of integrations. This greatly simplifies development and troubleshooting.


<div class="st-callout info">


**Note:** Debug mode can quickly increase disk usage because all debug events are stored in the database.
Starting from **SENTIENT 3.9**, the platform stores the full set of debug events only during the first **15 minutes** after the integrations is created; afterward, only error events are retained.


</div>


Debug mode settings can be combined or disabled entirely.

- Click "**Next**".

![image](/images/user-guide/integrations/chirpstack/chirpstack-integration-setup-1-pe.webp)

<br>

**2. Uplink data converter**. 

Uplink is necessary in order to convert the incoming data from the device into the required format for displaying them in SENTIENT.

Starting from **SENTIENT 4.0**, we have simplified the process of writing converters for Loriot integration. You can now easily choose where the message fields from the integration should go (attributes or telemetry) without manually defining this in the decoder function.

> **Note**: Converters created before the release of SENTIENT 4.0 will still be available and will continue to function properly.

- Enter a name for the converter. It must be unique.
- To view the events, enable [debug mode](/docs/user-guide/integrations/#debug-mode).
- In the "**Main decoding configuration**" section
    - Select the entity type (**Device** or **Asset**) that will be created as a result of the integration, and specify the entity name. The **$eui** pattern will dynamically fetch the device&#39;s unique identifier from the Loriot message.
    - Use the existing script for parsing and transforming data, or provide your own custom script.


<div class="st-callout info">


**Note:** The converter shown below will work **only with SENTIENT versions 3.9 and earlier**.


</div>


> One can use either [TBEL](/docs/pe/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/pe/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">


The script used in the example:

```javascript
var data = decodeToJson(payload);
var deviceName = data.deviceInfo.deviceName;
var deviceType = data.deviceInfo.deviceProfileName;
var groupName = 'IAQ devices';
// var customerName = 'Customer A';
// use assetName and assetType instead of deviceName and deviceType
// to automatically create assets instead of devices.
// var assetName = 'Asset A';
// var assetType = 'building';

// If you want to parse incoming data somehow, you can add your code to this function.
// input: bytes
// expected output:
//  {
//    "attributes": {"attributeKey": "attributeValue"},
//    "telemetry": {"telemetryKey": "telemetryValue"}
//  }
//
// In the example - bytes will be saved as HEX string and also parsed as light level, battery level and PIR sensor value.
//

function decodePayload(input) {
var output = { attributes:{}, telemetry: {} };
// --- Decoding code --- //

    output.telemetry.HEX_bytes = bytesToHex(input);

    // If the length of the input byte array is odd - we cannot parse it using the example below
    if (input.length > 0) {
        for (var i = 0; i < input.length; ) {
            var channel_id = input[i++];
            if (i < input.length) {
                var channel_type = input[i++];
                // BATTERY
                if (channel_id === 0x01 && channel_type === 0x75) {
                    output.telemetry.battery = input[i];
                    i += 1;
                }
                // PIR
                else if (channel_id === 0x03 && channel_type === 0x00) {
                    output.telemetry.pir = input[i] === 0 ? "normal" : "trigger";
                    i += 1;
                }
                // DAYLIGHT
                else if (channel_id === 0x04 && channel_type === 0x00) {
                    output.telemetry.daylight = input[i] === 0 ? "dark" : "light";
                    i += 1;
                }
            }
        }
    }

    // --- Decoding code --- //
    return output;
}

// --- attributes and telemetry objects ---
var telemetry = {};
var attributes = {};
// --- attributes and telemetry objects ---

// --- Timestamp parsing
var dateString = data.time;
var timestamp = -1;
if (dateString != null) {
  timestamp = new Date(dateString).getTime();
  if (timestamp == -1) {
    var secondsSeparatorIndex = dateString.lastIndexOf('.') + 1;
    var millisecondsEndIndex = dateString.lastIndexOf('+');
    if (millisecondsEndIndex == -1) {
      millisecondsEndIndex = dateString.lastIndexOf('Z');
    }
    if (millisecondsEndIndex == -1) {
      millisecondsEndIndex = dateString.lastIndexOf('-');
    }
    if (millisecondsEndIndex == -1) {
      if (dateString.length >= secondsSeparatorIndex + 3) {
        dateString = dateString.substring(0, secondsSeparatorIndex + 3);
      }
    } else {
      dateString = dateString.substring(0, secondsSeparatorIndex + 3) +
        dateString.substring(millisecondsEndIndex, dateString.length);
    }
    timestamp = new Date(dateString).getTime();
  }
}
// If we cannot parse timestamp - we will use the current timestamp
if (timestamp == -1) {
timestamp = Date.now();
}
// --- Timestamp parsing

// You can add some keys manually to attributes or telemetry
attributes.deduplicationId = data.deduplicationId;

// You can exclude some keys from the result
var excludeFromAttributesList = ["deviceName", "rxInfo", "confirmed", "data", "deduplicationId","time", "adr", "dr", "fCnt"];
var excludeFromTelemetryList = ["data", "deviceInfo", "txInfo", "devAddr", "adr", "time", "fPort", "region_common_name", "region_config_id", "deduplicationId"];

// Message parsing
// To avoid paths in the decoded objects we passing false value to function as "pathInKey" argument.
// Warning: pathInKey can cause already found fields to be overwritten with the last value found.

var telemetryData = toFlatMap(data, excludeFromTelemetryList, false);
var attributesData = toFlatMap(data, excludeFromAttributesList, false);

var uplinkDataList = [];

// Passing incoming bytes to decodePayload function, to get custom decoding
var customDecoding = decodePayload(base64ToBytes(data.data));

// Collecting data to result
if (customDecoding.?telemetry.size() > 0) {
  telemetry.putAll(customDecoding.telemetry);
}

if (customDecoding.?attributes.size() > 0) {
  attributes.putAll(customDecoding.attributes);
}

telemetry.putAll(telemetryData);
attributes.putAll(attributesData);

var result = {
    deviceName: deviceName,
    deviceType: deviceType,
    //  assetName: assetName,
    //  assetType: assetType,
    //  customerName: customerName,
    groupName: groupName,
    attributes: attributes,
    telemetry: {
    ts: timestamp,
    values: telemetry
    }
};

return result;
```


</div>

<div class="st-tab" data-label="JavaScript">


The script used in the example:

```javascript
// Decode an uplink message from a buffer
// payload - array of bytes
// metadata - key/value object

/** Decoder **/

// decode payload to string
var payloadStr = decodeToString(payload);

// decode payload to JSON
// var data = decodeToJson(payload);

var deviceName = 'Device A';
var deviceType = 'thermostat';
var customerName = 'Customer C';
var groupName = 'thermostat devices';
var manufacturer = 'Example corporation';
// use assetName and assetType instead of deviceName and deviceType
// to automatically create assets instead of devices.
// var assetName = 'Asset A';
// var assetType = 'building';

// Result object with device/asset attributes/telemetry data
var result = {
// Use deviceName and deviceType or assetName and assetType, but not both.
  deviceName: deviceName,
  deviceType: deviceType,
// assetName: assetName,
// assetType: assetType,
// customerName: customerName,
  groupName: groupName,
  attributes: {
    model: 'Model A',
    serialNumber: 'SN111',
    integrationName: metadata['integrationName'],
    manufacturer: manufacturer
  },
  telemetry: {
    temperature: 42,
    humidity: 80,
    rawData: payloadStr
  }
};

/** Helper functions **/

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


</div>

</div>


![image](/images/user-guide/integrations/chirpstack/chirpstack-integration-setup-2-1-pe.webp)

- **Advanced decoding parameters**" section:
    - The **Device profile**, **Device label**, **Customer name**, and **Device group name** fields are not mandatory, and you can also use the $ pattern to populate them dynamically.
    - In the **Attributes** and **Telemetry** sections specify the keys that should be interpreted as attributes and telemetry, respectively.
    - In the **Update only keys list** section, define keys whose values will be saved to the database only if they have changed from the previous incoming message.This applies to both Attributes and Telemetry, helping optimize data storage.
- Once the uplink converter is set up, click "**Next**".

![image](/images/user-guide/integrations/chirpstack/chirpstack-integration-setup-2-2-pe.webp)

<br>

**3. Downlink data converter**.

At the step of adding a downlink converter, you can also select a previously created or create a new downlink converter. But for now, leave the "Downlink data converter" field empty. Click "**Skip**";

![image](/images/user-guide/integrations/chirpstack/chirpstack-integration-setup-3-pe.webp)

<br>
**4. Connection**.

To complete adding integration, you need to:

- Specify your "Base URL";
- Note down "HTTP endpoint URL" we will use this value later;
- Specify "Application server URL" - address of application server or REST API service. Usually, with a standard installation, only the port is changed to 8090;
- Specify "Application server API Token" - taken from the application server. To get its we need to open ChirpStack application server UI, navigate to the "API keys" page from the left top menu and create new an API key.  


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/chirpstack-api-key-1.webp" alt="Go to the &quot;API keys&quot; page, and click &quot;Add API key&quot;;" loading="lazy"><figcaption>Go to the "API keys" page, and click "Add API key";</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/chirpstack-api-key-2.webp" alt="Enter API key name, and click &quot;Submit&quot;;" loading="lazy"><figcaption>Enter API key name, and click "Submit";</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/chirpstack-api-key-3.webp" alt="API key created. Copy API token." loading="lazy"><figcaption>API key created. Copy API token.</figcaption></figure></div>


Finally, click "Add" button to complete adding the ChirpStack integration.

![image](/images/user-guide/integrations/chirpstack/chirpstack-integration-setup-4-pe.webp)

## Configure integration on your ChirpStack application

In order for data to be transferred from ChirpStack to SENTIENT, you need to configure an integration in your ChirpStack application.

To create integration on ChirpStack Network server stack, we need to do the following steps:

- Go to the "Applications" page in the left menu of the ChirpStack Network server user interface, and click "Add application" button;
- Named it and click "Submit" button;
- Application created. Now, navigate to the "Integrations" tab;
- Find and add a HTTP integration by clicking "+" icon;
- Fill in the field with the "HTTP endpoint URL" previously copied from the ChirpStack integration in the SENTIENT. Then, click "Submit" button.

HTTP integration created.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/chirpstack-configure-integration-1.webp" alt="Go to the &quot;Applications&quot; page in the left menu of the ChirpStack Network server user interface, and click &quot;Add application&quot; button;" loading="lazy"><figcaption>Go to the "Applications" page in the left menu of the ChirpStack Network server user interface, and click "Add application" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/chirpstack-configure-integration-2.webp" alt="Named it and click &quot;Submit&quot; button;" loading="lazy"><figcaption>Named it and click "Submit" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/chirpstack-configure-integration-3.webp" alt="Application created. Now, navigate to the &quot;Integrations&quot; tab;" loading="lazy"><figcaption>Application created. Now, navigate to the "Integrations" tab;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/chirpstack-configure-integration-4.webp" alt="Find and add a &quot;HTTP&quot; integration by clicking &quot;+&quot; icon;" loading="lazy"><figcaption>Find and add a "HTTP" integration by clicking "+" icon;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/chirpstack-configure-integration-5.webp" alt="Fill in the field with the &quot;HTTP endpoint URL&quot; previously copied from the ChirpStack integration in the SENTIENT. Then, click &quot;Submit&quot; button;" loading="lazy"><figcaption>Fill in the field with the "HTTP endpoint URL" previously copied from the ChirpStack integration in the SENTIENT. Then, click "Submit" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/chirpstack-configure-integration-6.webp" alt="HTTP integration created." loading="lazy"><figcaption>HTTP integration created.</figcaption></figure></div>


## Processing uplink message

When your device sends an uplink message, a new device will appear in the SENTIENT user interface.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/device-created-1-pe.webp" alt="When your device sends an uplink message, a new device will appear in the SENTIENT user interface." loading="lazy"><figcaption>When your device sends an uplink message, a new device will appear in the SENTIENT user interface.</figcaption></figure></div>


You will receive an uplink event in the ChirpStack integration.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/integration-uplink-message-event-1.webp" alt="You will receive an uplink event in the ChirpStack integration." loading="lazy"><figcaption>You will receive an uplink event in the ChirpStack integration.</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/integration-uplink-message-event-2.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Received data can be viewed in the uplink converter. In the "In" and "Out" blocks of the "Events" tab:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/converter-event-1-pe.webp" alt="Received data can be viewed in the uplink converter. In the &quot;In&quot; and &quot;Out&quot; blocks of the &quot;Events&quot; tab;" loading="lazy"><figcaption>Received data can be viewed in the uplink converter. In the "In" and "Out" blocks of the "Events" tab;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/converter-event-2-pe.webp" alt="Incoming data to converter from ChirpStack" loading="lazy"><figcaption>Incoming data to converter from ChirpStack</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/converter-event-3-pe.webp" alt="Outgoing data from converter." loading="lazy"><figcaption>Outgoing data from converter.</figcaption></figure></div>


<br>
Use the [Dashboards](/docs/pe/user-guide/dashboards/) to work with data. Dashboards are a modern format for collecting and visualizing data sets. Visibility of data presentation is achieved through a variety of widgets.  
SENTIENT has examples of several types of dashboards that you can use. Learn more about **Solution templates** [here](/docs/pe/solution-templates/overview/).


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/http/http-solution-templates.webp" alt="Outgoing data from converter." loading="lazy"><figcaption>Outgoing data from converter.</figcaption></figure></div>


## Advanced usage: downlink

For sending downlink messages from the Sentient to the device, we need to define a downlink converter. You can customize the downlink according to your configuration.  

### Add downlink converter

Let's consider an example where we send an attribute update message. 

> One can use either [TBEL](/docs/pe/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/pe/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

You can use our example of downlink converter, or write your own according to your configuration:

```javascript
// Encode downlink data from incoming Rule Engine message

// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter

/** Encoder **/

// Result object with encoded downlink payload
var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "TEXT",

    // downlink data
    data: btoa(msg.downlink),

    // Optional metadata object presented in key/value format
    metadata: {
            DevEUI: metadata.cs_devEui,
            fPort: metadata.cs_fPort
    }

};

return result;
```


To add the downlink converter to the integration, follow this steps:


1. Go to the "Integrations" page, click ChirpStack integration to open its details, and enter integration editing mode by clicking the "pencil" icon;

1. Enter a name for the downlink data converter and click "Create new converter";

1. Paste the script to the encoder function section, and click "Add";

1. Apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/add-downlink-converter-1-pe.webp" alt="Go to the &quot;Integrations&quot; page, click ChirpStack integration to open its details, and enter integration editing mode by clicking the &quot;pencil&quot; icon;" loading="lazy"><figcaption>Go to the "Integrations" page, click ChirpStack integration to open its details, and enter integration editing mode by clicking the "pencil" icon;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/add-downlink-converter-2-pe.webp" alt="Enter a name for the downlink data converter and click &quot;Create new converter&quot;;" loading="lazy"><figcaption>Enter a name for the downlink data converter and click "Create new converter";</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/add-downlink-converter-tbel-3-pe.webp" alt="Paste the script to the encoder function section, and click &quot;Add&quot;;" loading="lazy"><figcaption>Paste the script to the encoder function section, and click "Add";</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/add-downlink-converter-4-pe.webp" alt="Apply changes." loading="lazy"><figcaption>Apply changes.</figcaption></figure></div>


</div>

<div class="st-tab" data-label="JavaScript">

You can use our example of downlink converter, or write your own according to your configuration:

```javascript
// Encode downlink data from incoming Rule Engine message

// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter

/** Encoder **/

// Result object with encoded downlink payload
var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "TEXT",

    // downlink data
    data: btoa(msg.downlink),

    // Optional metadata object presented in key/value format
    metadata: {
            DevEUI: metadata.cs_devEui,
            fPort: metadata.cs_fPort
    }

};

return result;
```


To add the downlink converter to the integration, follow this steps:


1. Go to the "Integrations" page, click ChirpStack integration to open its details, and enter integration editing mode by clicking the "pencil" icon;

1. Enter a name for the downlink data converter and click "Create new converter";

1. Paste the script to the encoder function section, and click "Add";

1. Apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/add-downlink-converter-1-pe.webp" alt="Go to the &quot;Integrations&quot; page, click ChirpStack integration to open its details, and enter integration editing mode by clicking the &quot;pencil&quot; icon;" loading="lazy"><figcaption>Go to the "Integrations" page, click ChirpStack integration to open its details, and enter integration editing mode by clicking the "pencil" icon;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/add-downlink-converter-2-pe.webp" alt="Enter a name for the downlink data converter and click &quot;Create new converter&quot;;" loading="lazy"><figcaption>Enter a name for the downlink data converter and click "Create new converter";</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/add-downlink-converter-java-3-pe.webp" alt="Paste the script to the encoder function section, and click &quot;Add&quot;;" loading="lazy"><figcaption>Paste the script to the encoder function section, and click "Add";</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/add-downlink-converter-4-pe.webp" alt="Apply changes." loading="lazy"><figcaption>Apply changes.</figcaption></figure></div>


</div>

</div>


You can add a downlink converter when creating or editing an integration.

### Modify Root Rule Chain

In order to send downlink, we'll use the rule chain to process shared attribute update. Let's import this rule chain:

- Download the [downlink_to_chirpstack.json](/docs/user-guide/integrations/resources/downlink_to_chirpstack.json) file;
- Go to the "Rule Chains" page. To import this JSON file, click the "+" icon in the upper right corner of the screen and select "Import rule chain";
- Drag the downloaded JSON file into the import rule chain window. Click "Import";
- The "Downlink to Chirpstack" rule chain will open. Double-click on the "integration downlink" node, specify ChirpStack integration in the "Integration" field and save changes;
- Save rule chain by pressing on checkmark.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/import-downlink-rule-chain-1.webp" alt="Go to the &quot;Rule Chains&quot; page. To import this JSON file, click the + icon in the upper right corner of the screen and select &quot;Import rule chain&quot;. Drag the downloaded JSON file into the import rule chain window. Click &quot;Import&quot;;" loading="lazy"><figcaption>Go to the "Rule Chains" page. To import this JSON file, click the + icon in the upper right corner of the screen and select "Import rule chain". Drag the downloaded JSON file into the import rule chain window. Click "Import";</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/import-downlink-rule-chain-2.webp" alt="The &quot;Downlink to Chirpstack&quot; rule chain will open. Double-click on the &quot;integration downlink&quot; node;" loading="lazy"><figcaption>The "Downlink to Chirpstack" rule chain will open. Double-click on the "integration downlink" node;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/import-downlink-rule-chain-4.webp" alt="Specify ChirpStack integration in the &quot;Integration&quot; field;" loading="lazy"><figcaption>Specify ChirpStack integration in the "Integration" field;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/import-downlink-rule-chain-5.webp" alt="Save rule chain by pressing on checkmark." loading="lazy"><figcaption>Save rule chain by pressing on checkmark.</figcaption></figure></div>


Now you need to configure the **Root Rule Chain**:


1. Open the "Root Rule Chain", and find a "check relation presence" node;

1. Drag it to the rule chain. Name it "Check relation to ChirpStack integration", select the direction - "To originator", specify "ManagedByOriginator" relation type. Specify ChirpStack integration and click "Add";

1. Tap on a right grey circle of "message type switch" node and drag this circle to the left side of "check relation presence" node. Here, add the "Attributes Updated" link, and click "Add";

1. Find a "rule chain" node;

1. Drag it to the rule chain. Name it "Downlink to Chirpstack", specify "Downlink to Chirpstack" rule chain, and click "Add";

1. Tap on the right grey circle of the "check relation presence" node and drag this circle to left side of “rule chain” node. Here, select the "True" link, and click "Add". Finally, save Root Rule Chain.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/edit-root-rule-chain-1.webp" alt="Open the &quot;Root Rule Chain&quot;, and find a &quot;check relation presence&quot; node;" loading="lazy"><figcaption>Open the "Root Rule Chain", and find a "check relation presence" node;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/edit-root-rule-chain-2.webp" alt="Drag it to the rule chain. Name it &quot;Check relation to ChirpStack integration&quot;, select the direction - &quot;To originator&quot;, specify &quot;ManagedByOriginator&quot; relation type. Specify ChirpStack integration and click &quot;Add&quot;;" loading="lazy"><figcaption>Drag it to the rule chain. Name it "Check relation to ChirpStack integration", select the direction - "To originator", specify "ManagedByOriginator" relation type. Specify ChirpStack integration and click "Add";</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/edit-root-rule-chain-3.webp" alt="Tap on a right grey circle of &quot;message type switch&quot; node and drag this circle to the left side of &quot;check relation presence&quot; node. Here, add the &quot;Attributes Updated&quot; link, and click &quot;Add&quot;;" loading="lazy"><figcaption>Tap on a right grey circle of "message type switch" node and drag this circle to the left side of "check relation presence" node. Here, add the "Attributes Updated" link, and click "Add";</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/edit-root-rule-chain-4.webp" alt="Find a &quot;rule chain&quot; node;" loading="lazy"><figcaption>Find a "rule chain" node;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/edit-root-rule-chain-5.webp" alt="Drag it to the rule chain. Name it &quot;Downlink to Chirpstack&quot;, specify &quot;Downlink to Chirpstack&quot; rule chain, and click &quot;Add&quot;;" loading="lazy"><figcaption>Drag it to the rule chain. Name it "Downlink to Chirpstack", specify "Downlink to Chirpstack" rule chain, and click "Add";</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/edit-root-rule-chain-6.webp" alt="Tap on the right grey circle of the &quot;check relation presence&quot; node and drag this circle to left side of “rule chain” node. Here, select the &quot;True&quot; link, and click &quot;Add&quot;. Finally, save Root Rule Chain." loading="lazy"><figcaption>Tap on the right grey circle of the "check relation presence" node and drag this circle to left side of “rule chain” node. Here, select the "True" link, and click "Add". Finally, save Root Rule Chain.</figcaption></figure></div>


### Test downlink

A downlink message will be sent to the integration when an attribute is added or modified.

To see this with an example, we go to the "Devices" page. Select your device and navigate to the "Attributes" tab. 
Select "Shared attributes" and click on the "plus" icon to add new attribute. Then enter the attribute name and its value (for example, the key name is 'downlink', value: '01040203') and click "Add".


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/add-shared-attribute-1.webp" alt="Go to the &quot;Devices&quot; page. Select your device and navigate to the &quot;Attributes&quot; tab. Select &quot;Shared attributes&quot; and click on the &quot;plus&quot; icon to add new attribute. Then enter the attribute name and its value (for example, the key name is &#39;downlink&#39;, value: &#39;01040203&#39;) and click &quot;Add&quot;." loading="lazy"><figcaption>Go to the "Devices" page. Select your device and navigate to the "Attributes" tab. Select "Shared attributes" and click on the "plus" icon to add new attribute. Then enter the attribute name and its value (for example, the key name is &#39;downlink&#39;, value: &#39;01040203&#39;) and click "Add".</figcaption></figure></div>


Received data and data that was sent can be viewed in the downlink converter. In the "In" block of the "Events" tab, we see what data entered and the "Out" field displays messages to device:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/chirpstack/downlink-event-1.webp" alt="Received data can be viewed in the downlink converter. In the &quot;In&quot; and &quot;Out&quot; blocks of the &quot;Events&quot; tab;" loading="lazy"><figcaption>Received data can be viewed in the downlink converter. In the "In" and "Out" blocks of the "Events" tab;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/downlink-event-2.webp" alt="Input data to downlink converter;" loading="lazy"><figcaption>Input data to downlink converter;</figcaption></figure><figure><img src="/images/user-guide/integrations/chirpstack/downlink-event-3.webp" alt="Output data from downlink converter." loading="lazy"><figcaption>Output data from downlink converter.</figcaption></figure></div>


## Next steps
