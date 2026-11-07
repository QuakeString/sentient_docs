+++
title = "Loriot integration"
description = "Loriot integration guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/loriot.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

[Loriot](https://loriot.io/) is LoRaWAN network designed for connecting your devices using LoRaWAN stack. After integrating LORIOT with the
SENTIENT, you can connect, communicate, process and visualize data from devices in the SENTIENT IoT platform.

## Register an account on Loriot

Here&#39;s how to get started with Loriot:

- Visit the [Loriot](https://loriot.io/) website.
- Choose a service package — for example, select the **Community Public Network Server**.
- Pick your preferred region and country.
- Complete the registration process and log in to your Loriot account.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/create-loriot-account-1.webp" alt="Visit the Loriot website. Choose a service package — for example, select the Community Public Network Server." loading="lazy"><figcaption>Visit the Loriot website. Choose a service package — for example, select the <b>Community Public Network Server</b>.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/create-loriot-account-2.webp" alt="Pick your preferred region and country." loading="lazy"><figcaption>Pick your preferred region and country.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/create-loriot-account-3.webp" alt="Complete the registration process." loading="lazy"><figcaption>Complete the registration process.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/create-loriot-account-4.webp" alt="Log in to your Loriot account." loading="lazy"><figcaption>Log in to your Loriot account.</figcaption></figure></div>


*&#42; The Loriot interface may change in the future.*

## Create Loriot integration

You will need to have access to SENTIENT Professional Edition. The easiest way is to use [SENTIENT Cloud](https://sentient.invenia.in/installations/choose-region/) server.
The alternative option is to install SENTIENT using [installation guide](/docs/installation/).

<br>
Let's move on to setting up the integration between the SENTIENT platform and Loriot.

**1. Basic settings**.

- Sign in to your SENTIENT account.
- Navigate to the "**Integrations**" page under the "**Integrations center**" section. Click "**plus**" button to add a new integration.
- From the list, select the integration type "**Loriot**".
- If you'd like to monitor events and troubleshoot, enable [debug mode](/docs/user-guide/integrations/#debug-mode).

<b><font size="3">Debug mode</font></b>

Enabling debug mode allows you to track events, states, and potential errors related to the execution of integrations. This greatly simplifies development and troubleshooting.


<div class="st-callout info">


**Note:** Debug mode can quickly increase disk usage because all debug events are stored in the database.
Starting from **SENTIENT 3.9**, the platform stores the full set of debug events only during the first **15 minutes** after the integrations is created; afterward, only error events are retained.


</div>


Debug mode settings can be combined or disabled entirely.

- Click "**Next**".

![image](/images/user-guide/integrations/loriot/loriot-add-integration-1-pe.webp)

<br>

**2. Uplink data converter**. 

Uplink is necessary in order to convert the incoming data from the device into the required format for displaying them in SENTIENT.

Starting from **SENTIENT 4.0**, we have simplified the process of writing converters for Loriot integration. You can now easily choose where the message fields from the integration should go (attributes or telemetry) without manually defining this in the decoder function.

> **Note**: Converters created before the release of SENTIENT 4.0 will still be available and will continue to function properly.

Let's review sample uplink message from Loriot:

```
{
     "cmd"  : "rx",
     "EUI"  : "BE7A000000000552",
     "ts"   : 1470850675433,
     "ack"  : false,
     "fcnt" : 1,
     "port" : 1,
     "data" : "2A3F",
     "freq" : 868500000,
     "dr"   : "SF12 BW125 4/5",
     "rssi" : -130,
     "snr"  : 1.2
 }
```
As you can see the unique device id arrives in the "**EUI**" field. We will use it as a device name in SENTIENT. 

Device data is encoded in the "**data**" field. The encoded data here is:

```
"data": "2A3F"
```

Let's convert them into temperature and humidity values.

**2A** is the value for **temperature.** In decoded form it will be **42**

**3F** is the value for **humidity.** In decoded form it will be **63**

<br>
Let's return to configuring the integration:

- Enter a name for the converter. It must be unique.
- To view the events, enable [debug mode](/docs/user-guide/integrations/#debug-mode).
- In the "**Main decoding configuration**" section
  - Select the entity type (**Device** or **Asset**) that will be created as a result of the integration, and specify the entity name. The **$eui** pattern will dynamically fetch the device&#39;s unique identifier from the Loriot message.
  > **Example**: If the entity name is set as Device $eui, and the incoming message contains: **"EUI": "BE7A000000000552"**, the converter will replace $eui with "BE7A000000000552". The final device name will be: "Device BE7A000000000552".
  - Use the existing script for parsing and transforming data, or provide your own custom script.

![image](/images/user-guide/integrations/loriot/loriot-add-integration-2-1-pe.webp)

- **Advanced decoding parameters**" section: 
  - The **Device profile**, **Device label**, **Customer name**, and **Device group name** fields are not mandatory, and you can also use the $ pattern to populate them dynamically.
  - In the **Attributes** and **Telemetry** sections specify the keys that should be interpreted as attributes and telemetry, respectively.
  - In the **Update only keys list** section, define keys whose values will be saved to the database only if they have changed from the previous incoming message.This applies to both Attributes and Telemetry, helping optimize data storage.
- Once the uplink converter is set up, click "**Next**".

![image](/images/user-guide/integrations/loriot/loriot-add-integration-2-2-pe.webp)

<br>

**3. Downlink data converter**.

At the step of adding a downlink converter, you can also select a previously created or create a new downlink converter. But for now, leave the "**Downlink data converter**" field empty. Click "**Skip**".

![image](/images/user-guide/integrations/loriot/loriot-add-integration-3-pe.webp)

<br>

**4. Connection**.

In order for data to be transferred from Loriot to SENTIENT, you need to configure an **Output** for your Loriot application. You can do this manually (recommended) or SENTIENT Integration can do this for you (you will need to specify login and password from your Loriot account for us to be able to automatically provision the output).

We can create the **Output** by either specifying the "**HTTP endpoint URL**" of the integration directly in the Loriot account or by enabling the "**Create Loriot Application output**" option in SENTIENT and providing your Loriot credentials there.


<div class="st-tabs">

<div class="st-tab" data-label="Use Loriot accountRecommended">


In Loriot UI:


1. Go to the "<b>Applications</b>" page and click on the application.

1. Go to the "<b>Output</b>" page.

1. Click on the "<b>Add new output</b>" button.

1. Select the output type as "<b>HTTP Push</b>" and enter the "<b>HTTP endpoint URL</b>" taken from the integration. Then, click "<b>Add output</b>" button.

1. Output created successfully.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot-http-push-1.webp" alt="Go to the &quot;Applications&quot; page and click on the application." loading="lazy"><figcaption>Go to the "<b>Applications</b>" page and click on the application.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot-http-push-2.webp" alt="Go to the &quot;Output&quot; page." loading="lazy"><figcaption>Go to the "<b>Output</b>" page.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot-http-push-3.webp" alt="Click on the &quot;Add new output&quot; button." loading="lazy"><figcaption>Click on the "<b>Add new output</b>" button.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot-http-push-4.webp" alt="Select the output type as &quot;HTTP Push&quot; and enter the &quot;HTTP endpoint URL&quot; taken from the integration. Then, click &quot;Add output&quot; button." loading="lazy"><figcaption>Select the output type as "<b>HTTP Push</b>" and enter the "<b>HTTP endpoint URL</b>" taken from the integration. Then, click "<b>Add output</b>" button.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot-http-push-5.webp" alt="Output created successfully." loading="lazy"><figcaption>Output created successfully.</figcaption></figure></div>


<br>
In SENTIENT UI: 
- Click "Add" to confirm creating integration.

![image](/images/user-guide/integrations/loriot/loriot-add-integration-4-1-pe.webp)

</div>

<div class="st-tab" data-label="Create Loriot Application output">

- Turn on the "**Create Loriot Application output**" option. 
- Fill in the "**Server**" and "**Application ID**" fields.
- Select the "**Basic**" credential type and enter your Loriot account credentials.
- Click "Add" to confirm creating integration.

![image](/images/user-guide/integrations/loriot/loriot-add-integration-4-2-pe.webp)

<br>
You can find the values for "**Server**" and "**Application ID**" in the Loriot UI:

**Server**:


1. Open the Loriot UI. The URL contains the server name that we selected during the registration process. This server needs to be specified in the integration settings.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot-server.webp" alt="Open the Loriot UI. The URL contains the server name that we selected during the registration process. This server needs to be specified in the integration settings." loading="lazy"><figcaption>Open the Loriot UI. The URL contains the server name that we selected during the registration process. This server needs to be specified in the integration settings.</figcaption></figure></div>


<br>

**Application ID**:


1. Locate the <b>Application ID</b> associated with your project. This value needs to be specified in the integration settings.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot-application-id.webp" alt="Locate the Application ID associated with your project. This value needs to be specified in the integration settings." loading="lazy"><figcaption>Locate the <b>Application ID</b> associated with your project. This value needs to be specified in the integration settings.</figcaption></figure></div>


</div>

</div>


<br>

**Enable security option**

If necessary, you can specify additional parameters, without which the data will not be included in the integration.

To do this, turn on the "<b>Enable security</b>" option. Click "<b>Add</b>" and enter an arbitrary value for the "<b>Header</b>" and "<b>Value</b>" fields.  Then, save the changes.

Also need to specify this credentials in Loriot UI.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/enable-security-1-pe.webp" alt="To do this, turn on the &quot;Enable security&quot; option. Click &quot;Add&quot; and enter an arbitrary value for the &quot;Header&quot; and &quot;Value&quot; fields. Then, save the changes." loading="lazy"><figcaption>To do this, turn on the "<b>Enable security</b>" option. Click "<b>Add</b>" and enter an arbitrary value for the "<b>Header</b>" and "<b>Value</b>" fields. Then, save the changes.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/enable-security-2-pe.webp" alt="Also need to specify this credentials in Loriot UI." loading="lazy"><figcaption>Also need to specify this credentials in Loriot UI.</figcaption></figure></div>


<br>
Once the Headers filter has been configured, it will also need to be specified in the uplink message in the format:

```
-H "$HEADER:$VALUE"
```


Example:

```
-H "authorization:secret"
```

## Send Uplink message

It may be useful to "emulate" the message from device using console instead of the Loriot server. To send an uplink message, you need a **HTTP endpoint URL** from the integration. 

Use this command to send message. Replace **$HTTP_ENDPOINT_URL** with corresponding values. 

```bash
curl -v -X POST -d "{\"EUI\":\"BE7A000000000552\",\"data\":\"2A3F\",\"port\":1,\"cmd\":\"rx\",\"dr\":\"SF12 BW125 4/5\",\"snr\":1.2,\"ack\":\"false\",\"freq\":868500000,\"fcnt\":1,\"rssi\":-130,\"ts\":1613745998000}" $HTTP_ENDPOINT_URL -H "Content-Type:application/json"
```


With the **enable security** option: replace **$HTTP_ENDPOINT_URL** and **$HEADER:$VALUE** with corresponding values. 

```bash
curl -v -X POST -d "{\"EUI\":\"BE7A000000000552\",\"data\":\"2A3F\",\"port\":1,\"cmd\":\"rx\",\"dr\":\"SF12 BW125 4/5\",\"snr\":1.2,\"ack\":\"false\",\"freq\":868500000,\"fcnt\":1,\"rssi\":-130,\"ts\":1613745998000}" $HTTP_ENDPOINT_URL "Content-Type:application/json" -H "$HEADER:$VALUE"
```


To find the "**HTTP endpoint URL**", go to the "Integrations" page in SENTIENT and click on the Loriot integration to open its details. There, you will find the "<b>HTTP endpoint URL</b>".


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot-copy-http-endpoint-pe.webp" alt="Go to the &quot;Integrations&quot; page in SENTIENT. Find your Loriot integration and click on it. There you can find the &quot;HTTP endpoint URL&quot;." loading="lazy"><figcaption>Go to the "Integrations" page in SENTIENT. Find your Loriot integration and click on it. There you can find the "HTTP endpoint URL".</figcaption></figure></div>


<br>

The created device with data can be seen in the "**"Devices**" page of the "**Entities**" section.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot-device-attributes-1-pe.webp" alt="The created device and its data can be found on the &quot;Devices&quot; page in the &quot;Entities&quot; section. On the &quot;Attributes&quot; tab, you will find the attributes sent by the device to SENTIENT." loading="lazy"><figcaption>The created device and its data can be found on the "Devices" page in the "Entities" section. On the "Attributes" tab, you will find the attributes sent by the device to SENTIENT.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot-device-attributes-2-pe.webp" alt="On the &quot;Latest telemetry&quot; tab, you will find the telemetry data transmitted by the device to SENTIENT." loading="lazy"><figcaption>On the "Latest telemetry" tab, you will find the telemetry data transmitted by the device to SENTIENT.</figcaption></figure></div>


<br>

The data can be viewed in the Uplink converter. In the "**In**", "**Out**" and "**Metadata**" blocks of the "**Events**" tab:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot-uplink-converter-events-1-pe.webp" alt="You can view the data in the Uplink converter under the &quot;Events&quot; tab, within the &quot;In&quot;, &quot;Out&quot;, and &quot;Metadata&quot; blocks." loading="lazy"><figcaption>You can view the data in the Uplink converter under the "<b>Events</b>" tab, within the "<b>In</b>", "<b>Out</b>", and "<b>Metadata</b>" blocks.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot-uplink-converter-events-2-pe.webp" alt="&quot;Input&quot; block." loading="lazy"><figcaption>"Input" block.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot-uplink-converter-events-3-pe.webp" alt="&quot;Output&quot; block." loading="lazy"><figcaption>"Output" block.</figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot-uplink-converter-events-4-pe.webp" alt="&quot;Metadata&quot; block." loading="lazy"><figcaption>"Metadata" block.</figcaption></figure></div>


## Advanced Usage: Create Downlink Converter

Create Downlink in **Data converters**. To see events - enable [debug mode](/docs/user-guide/integrations/#debug-mode).

> One can use either [TBEL](/docs/user-guide/rhai/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/rhai/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

You can customize the downlink according to your configuration. Let's consider an example where we send an attribute update message. So we should change code in the downlink encoder function under
line `//downlink data input`

```
data: msg.firmware
```


Also, indicate the required parameters in the metadata:

```
metadata: {
  "EUI": "$Device_EUI",
  "port": 1
}
```


ㅤㅤ&#42;**EUI** is device EUI and is taken from the device in LORIOT.

ㅤㅤ&#42; **port** can be from 1 to 223.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot_devices.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot_device_eui.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Example for downlink converter:

```javascript
// Encode downlink data from incoming Rule Engine message
// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter
// Result object with encoded downlink payload
var result = {
    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "TEXT",
    // downlink data
    data: msg.firmware,
    // Optional metadata object presented in key/value format
    metadata: {
            "EUI": "BE7A000000000552",
            "port": 1
    }
};
return result;

``` 


<br>
In **SENTIENT 4.0**, an option has been added to the Loriot downlink functionality, allowing users to avoid double hexadecimal encoding.
If your data is already in hexadecimal format, you can add the following metadata property to your message:

```
"isHexEncoded": "true"
```


With this property enabled, the downlink message will be sent to Loriot without double hexadecimal encoding.

Example for downlink converter without double hexadecimal encoding:

```javascript
// Encode downlink data from incoming Rule Engine message
// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter
// Result object with encoded downlink payload
var result = {
    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "TEXT",
    // downlink data
    data: "B104",
    // Optional metadata object presented in key/value format
    metadata: {
        "EUI": "BE7A000000000552",
        "port": 1, 
        "isHexEncoded": "true"
    }
};
return result;
``` 


Add a converter to the integration. You can do this at the stage of creating an integration or editing it.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot-downlink-converters-1-tbel-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


</div>

<div class="st-tab" data-label="JavaScript">

You can customize the downlink according to your configuration. Let's consider an example where we send an attribute update message. So we should change code in the downlink encoder function under
line `//downlink data input`

```
data: msg.firmware
```


Also, indicate the required parameters in the metadata:

```
metadata: {
  "EUI": "$Device_EUI",
  "port": 1
}
```


ㅤㅤ&#42;**EUI** is device EUI and is taken from the device in LORIOT.

ㅤㅤ&#42; **port** can be from 1 to 223.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot_devices.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot_device_eui.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Example for downlink converter:

```javascript
// Encode downlink data from incoming Rule Engine message
// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter
// Result object with encoded downlink payload
var result = {
    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "TEXT",
    // downlink data
    data: msg.firmware,
    // Optional metadata object presented in key/value format
    metadata: {
            "EUI": "BE7A000000000552",
            "port": 1
    }
};
return result;
``` 


<br>
In **SENTIENT 4.0**, an option has been added to the Loriot downlink functionality, allowing users to avoid double hexadecimal encoding.
If your data is already in hexadecimal format, you can add the following metadata property to your message:

```
"isHexEncoded": "true"
```


With this property enabled, the downlink message will be sent to Loriot without double hexadecimal encoding.

Example for downlink converter without double hexadecimal encoding:

```javascript
// Encode downlink data from incoming Rule Engine message
// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter
// Result object with encoded downlink payload
var result = {
    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "TEXT",
    // downlink data
    data: "B104",
    // Optional metadata object presented in key/value format
    metadata: {
        "EUI": "BE7A000000000552",
        "port": 1, 
        "isHexEncoded": "true"
    }
};
return result;
``` 


Add a converter to the integration. You can do this at the stage of creating an integration or editing it.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot-downlink-converters-1-java-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


</div>

</div>


To send Downlink, enable the **Send downlink** option in the integration.
Once we enable the “Send downlink” option, specify the Server, Application ID, Application Access Token in the fields:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/sentient_add_integration_send_downlink.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


To get this data - go to your account in LORIOT.

Data to fill in the **Server** field:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot-server.webp" alt="Open the Loriot UI. The URL contains the server name that we selected during the registration process. This server needs to be specified in the integration settings." loading="lazy"><figcaption>Open the Loriot UI. The URL contains the server name that we selected during the registration process. This server needs to be specified in the integration settings.</figcaption></figure></div>


Data to fill in the **Application ID** field:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot-application-id.webp" alt="Locate the Application ID associated with your project. This value needs to be specified in the integration settings." loading="lazy"><figcaption>Locate the <b>Application ID</b> associated with your project. This value needs to be specified in the integration settings.</figcaption></figure></div>


After that, go to Application and go to the **Access Tokens** section. Find the token that will be specified in the integration.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot_access_tokens.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot_authentication_tokens.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/loriot_and_sentient_integration_application_access_token.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


We can send a message to the device from Rule chain using the rule node. For our example, we create the **integration downlink** node and set the ***“Attributes updated”*** link to it. When changes are made to the attribute, the downlink message will be sent to the integration.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/sentient_rule_chain_integration_downlink.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


We go to the **Device group** section in the **All** folder, to see this with an example. We have indicated the firmware of the device in the **Shared attributes.** Now we edit it by clicking on the “pencil” icon. Then we make changes to the attribute (change the firmware from 01052020.v1.1 to 01052020.v1.2) and save the data.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/sentient_devices_all_shared_attributes.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/loriot/sentient_devices_all_shared_attributes_update.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Received data and data that was sent can be viewed in the downlink converter.In the **“In”** block of the **Events** tab, we see what data entered:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/sentient_downlink_converter_events_in.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


The **“Out”** field displays messages to device:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/sentient_downlink_converter_events_out.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


It is possible to check that messages have reached LORIOT on the **Devices** -> **LoRaWAN Parameters** page at the very bottom in the **Downlink Queue** field.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/loriot/loriot_devices_downlink_queue.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Next steps
