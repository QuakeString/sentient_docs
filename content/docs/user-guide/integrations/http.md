+++
title = "HTTP Integration"
description = "HTTP integration guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/http.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

## Overview

HTTP Integration allows converting existing protocols and payload formats to SENTIENT message format and is useful in several deployment scenarios: 

 - stream device and/or asset data from external system, IoT platform or connectivity provider back-end.
 - stream device and/or asset data from your custom application running in the cloud.
 - connect the existing device with custom HTTP based protocol to SENTIENT.

<object width="100%" style="max-width: max-content;" data="/images/user-guide/integrations/http-integration.svg"></object>

## Create Uplink Converter

Before creating the integration, you need to create an Uplink converter in Data converters. Uplink is necessary in order to convert the incoming data from the device into the required format for displaying them in SENTIENT. 
Click on the “plus” and on “Create new converter”. To view the events, enable Debug. 
In the function decoder field, specify a script to parse and transform data.

<b><font size="3">Debug mode</font></b>

Enabling debug mode allows you to track events, states, and potential errors related to the execution of integrations. This greatly simplifies development and troubleshooting.


<div class="st-callout info">


**Note:** Debug mode can quickly increase disk usage because all debug events are stored in the database.
Starting from **SENTIENT 3.9**, the platform stores the full set of debug events only during the first **15 minutes** after the integrations is created; afterward, only error events are retained.


</div>


Debug mode settings can be combined or disabled entirely.

> One can use either [TBEL](/docs/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">


![image](/images/user-guide/integrations/http/http-create-data-converters-1-tbel-pe.webp)


**Example for the Uplink converter:**

```ruby
// Decode an uplink message from a buffer
// payload - array of bytes
// metadata - key/value object

/** Decoder **/
 
// decode payload to string
// var payloadStr = decodeToString(payload);

// decode payload to JSON
var data = decodeToJson(payload);

var deviceName = data.deviceName;
var deviceType = data.deviceType;

// Result object with device attributes/telemetry data
var result = {
   deviceName: deviceName,
   deviceType: deviceType,
   attributes: {
       model: data.model,
       serialNumber: data.param2,
   },
   telemetry: {
       temperature: data.temperature
   }
};

/** Helper functions 'decodeToString' and 'decodeToJson' are already built-in **/

return result;
```


You can change the decoder function while creating the converter or after creating it. If the converter has already been created, then click on the “pencil” icon to edit it.
Copy the configuration example for the converter (or your own configuration) and insert it into the decoder function. Save changes by clicking on the “checkmark” icon.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/http/http-create-data-converters-2-tbel-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/http/http-create-data-converters-3-tbel-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/http/http-create-data-converters-4-tbel-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


</div>

<div class="st-tab" data-label="JavaScript">


![image](/images/user-guide/integrations/http/http-create-data-converters-1-java-pe.webp)


**Example for the Uplink converter:**

```ruby
// Decode an uplink message from a buffer
// payload - array of bytes
// metadata - key/value object

/** Decoder **/

// decode payload to string
// var payloadStr = decodeToString(payload);

// decode payload to JSON
var data = decodeToJson(payload);

var deviceName = data.deviceName;
var deviceType = data.deviceType;

// Result object with device attributes/telemetry data
var result = {
   deviceName: deviceName,
   deviceType: deviceType,
   attributes: {
       model: data.model,
       serialNumber: data.param2,
   },
   telemetry: {
       temperature: data.temperature
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


You can change the decoder function while creating the converter or after creating it. If the converter has already been created, then click on the “pencil” icon to edit it.
Copy the configuration example for the converter (or your own configuration) and insert it into the decoder function. Save changes by clicking on the “checkmark” icon.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/http/http-create-data-converters-2-java-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/http/http-create-data-converters-3-java-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/http/http-create-data-converters-4-java-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


</div>

</div>


Now that the Uplink converter has been created, it is possible to create an integration.

## Create integration

- Go to the "**Integrations center**" section -> "**Integrations**" page and click "plus" button to create new integration. Name it "**HTTP Integration**", select type '**HTTP**'. Click "Next";


![image](/images/user-guide/integrations/http/http-add-integration-1-pe.webp)


- At this step, you can select a previously created or create a new upnlink converter right in this window. Select the previously created "**HTTP Uplink Converter**". Click "Next";


![image](/images/user-guide/integrations/http/http-add-integration-2-pe.webp)


- At the step of adding a downlink converter, you can also select a previously created or create a new downlink converter. But for now, leave the "Downlink data converter" field empty. Click "Skip";


![image](/images/user-guide/integrations/http/http-add-integration-3-pe.webp)


 - At this step, specify your '**Base URL**';
 - Please note down '**HTTP endpoint URL**' we will use this value later;
 - In '**Advanced settings**' enable "**Replace response status from 'No-Content' to 'OK'**";
 - Click "Add" button to save the Integration.


![image](/images/user-guide/integrations/http/http-add-integration-4-pe.webp)


## Send uplink message

To send an uplink message, you need the previously copied '**HTTP endpoint URL**' from the integration.

Use this command to send the message. Don't forget to replace `$DEVICE_NAME`, `$DEVICE_TYPE` and `$YOUR_HTTP_ENDPOINT_URL` with corresponding values.

```ruby
curl -v -X POST -d "{\"deviceName\":\"$DEVICE_NAME\",\"deviceType\":\"$DEVICE_TYPE\",\"temperature\":33,\"model\":\"test\"}" $YOUR_HTTP_ENDPOINT_URL -H "Content-Type:application/json"
```


![image](/images/user-guide/integrations/http/http-send-uplink-message-1-pe.webp)


<br>
Go to the "**Events**" tab in your HTTP integration. If you have done everything correctly, you should see one event with the status 'OK'.


![image](/images/user-guide/integrations/http/http-send-uplink-message-3-pe.webp)


<br>
When you sent the message, a new device was created. You should receive a notification about it. To view notification, click on the bell icon in the upper right corner of the screen. 
The notification will contain an action button by clicking which you can go to the details of the new device. Click this button.

![image](/images/user-guide/integrations/http/http-device-2-pe.webp)

<br>
Here you will see information about the new device. As well as the telemetry which we sent from the device to the SENTIENT.

![image](/images/user-guide/integrations/http/http-device-1-pe.webp)

<br>
Learn more about **notifications** and how to configure them [here](/docs/user-guide/notifications/).


<div class="st-callout info">


**NOTE**
<br>
If the "Allow create devices or assets" checkbox is unchecked, when sending a message to the SENTIENT with any parameters of the device (or asset), if such a device (asset) does not exist, then device (asset) will not be created.


</div>


Also, sent and received data can be viewed in the Uplink converter. In the 'In' and 'Out' blocks of the "**Events**" tab.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/http/http-received-data-1-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/http/http-received-data-2-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/http/http-received-data-3-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<br>
Use the [Dashboards](/docs/user-guide/dashboards/) to work with data. Dashboards are a modern format for collecting and visualizing data sets. Visibility of data presentation is achieved through a variety of widgets.  
SENTIENT has examples of several types of dashboards that you can use. Learn more about **Solution templates** [here](/docs/solution-hub/).


![image](/images/user-guide/integrations/http/http-solution-templates.webp)


### Enable security option

If necessary, you can specify additional parameters, without which the data will not be included in the integration.
To do this, check the Enable security checkbox and click on the Headers filter. Specify an arbitrary value and save the changes.


![image](/images/user-guide/integrations/http/http-enable-security-1-pe.webp)


Once the Headers filter has been configured, it will also need to be specified in the uplink message as follows:

```ruby
-H "test-header:secret"
```

Use this command to send the message with enable security option. Don't forget to replace `$DEVICE_NAME`, `$DEVICE_TYPE`, `$YOUR_HTTP_ENDPOINT_URL` and `$VALUE` with corresponding values.

```ruby
curl -v -X POST -d "{\"deviceName\":\"$DEVICE_NAME\",\"deviceType\":\"$DEVICE_TYPE\",\"temperature\":33,\"model\":\"test\"}" $YOUR_HTTP_ENDPOINT_URL -H "Content-Type:application/json" -H "$VALUE"
```


![image](/images/user-guide/integrations/http/http-enable-security-2-pe.webp)


## Downlink Converter

Create downlink converter in the "**Data converters**" page. To see events enable 'Debug mode'.

> One can use either [TBEL](/docs/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="tb-content-toggle" id="httpdownlinkconverterconfig">
    <div class="panel panel-default">
        <div class="panel-heading">
            
            
            
            
            <a class="content-toggle-button" data-target="#accessToken">
                <div class="content-toggle-button-text">
                    TBEL<small>Recommended</small>
                </div>
            </a>
            
            
            
            
            <a class="content-toggle-button" data-target="#anonymous">
                <div class="content-toggle-button-text">
                    JavaScript<small></small>
                </div>
            </a>
            
        </div>
        
        
        
        
        
        <div id="accessToken" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


![image](/images/user-guide/integrations/http/http-create-downlink-tbel-1-pe.webp)


<br>
Add a converter to the integration. You can customize a downlink according to your configuration.
Let’s consider an example where we send an attribute update message. So we should change code in the downlink encoder function under line **//downlink data** input:

```ruby
data: JSON.stringify(msg)
```

where **msg** is the message that we receive and send back to the device.


![image](/images/user-guide/integrations/http/http-create-downlink-tbel-2-pe.webp)


<br>
An example of downlink converter:

```ruby
// Encode downlink data from incoming Rule Engine message

// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter

var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",

    // downlink data
    data: JSON.stringify(msg),

    // Optional metadata object presented in key/value format
    metadata: {
    }
};

return result;
```


                </td></tr></table>
            </div>
        </div>
        
        
        
        
        
        <div id="anonymous" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


![image](/images/user-guide/integrations/http/http-create-downlink-java-1-pe.webp)


<br>
Add a converter to the integration. You can customize a downlink according to your configuration.
Let’s consider an example where we send an attribute update message. So we should change code in the downlink encoder function under line **//downlink data** input:

```ruby
data: JSON.stringify(msg)
```

where **msg** is the message that we receive and send back to the device.


![image](/images/user-guide/integrations/http/http-create-downlink-java-2-pe.webp)


<br>
An example of downlink converter:

```ruby
// Encode downlink data from incoming Rule Engine message

// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter

var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",

    // downlink data
    data: JSON.stringify(msg),

    // Optional metadata object presented in key/value format
    metadata: {
    }
};

return result;
```


                </td></tr></table>
            </div>
        </div>
        
    </div>
</div>


Now you need to add the created downlink converter to the integration.


![image](/images/user-guide/integrations/http/http-add-downlink-converter-1-pe.webp)


<br>
To be able to send downlink over integration we need to modify a "**Root Rule chain**":

- Go to the "**Rule chains**" page and click on the "**Root Rule Chain**" to open it;
- Create an '**integration downlink**' node. Specify your integration in its settings;


![image](/images/user-guide/integrations/http/http-downlink-rule-chain-1-pe.webp)


- Set the "**Attributes updated**" and "**Post attributes**" links from the '**message type switch**' node to the '**integration downlink**' node. Apply changes.


![image](/images/user-guide/integrations/http/http-downlink-rule-chain-2-pe.webp)


<br>
When the attribute is created or changes are made to the attribute, the downlink message will be sent to the integration.

To see this with an example, we go to the "**Devices**" page. Select your device and navigate to the "**Attributes**" tab. Select **Shared attributes** and click on the "plus" icon to create new attribute.
Then set the attribute name, its value (for example, the key name is 'firmware', value: '01052020.v1.1') and save the data.


![image](/images/user-guide/integrations/http/http-downlink-add-attribute-1-pe.webp)


<br>
Send the uplink message again. We will receive a response from the SENTIENT in the terminal:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/http/http-downlink-responce-2-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/http/http-downlink-responce-1-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Received data and data that was sent can be viewed in the downlink converter. In the "In" block of the Events tab, we see what data entered and in the "Out" field, the message sent to the device is displayed:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/http/http-downlink-message-1-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/http/http-downlink-message-2-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/http/http-downlink-message-3-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Next steps
