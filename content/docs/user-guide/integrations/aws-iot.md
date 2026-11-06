+++
title = "AWS IoT Integration"
description = "AWS IoT Integration Guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/aws-iot.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only [**Professional Edition**](/products/sentient-pe/) supports **Platform Integrations** feature.<br>
Use [**SENTIENT Cloud**](/installations/choose-region/) or [**install**](/docs/user-guide/install/pe/installation-options/) your own platform instance.


</div>

## Overview

AWS IoT Integration allows to stream data from AWS IoT Backend to SENTIENT and converts device payloads 
to the SENTIENT format. AWS IoT will be primarily responsible for receiving all messages (as a broker - 
messaging server), filtering them, deciding who is interested, and then sending the message to all 
subscribers, in our case of integration.

<object width="100%" style="max-width: max-content;" data="/images/user-guide/integrations/aws-iot-integration.svg"></object>

## AWS IOT

You should already have an [AWS account](https://aws.amazon.com/iot/) prepared, on which 
perform a few settings. To establish a correct and secure connection between the service and SENTIENT, you need to create Policies, devices, and certificates for them.

### Create Policy

A policy is an object in AWS that, when associated with an entity or resource, defines their permissions. 
Permissions in the policies determine whether the request is allowed or denied. Most policies are stored in 
AWS as JSON documents.

To add a new policy, choose **Security** - **Policies** in the main menu, and select the **Create Policy** button.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/create_policies_0.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


You will be redirected to the policy creation page, where you must specify the **Policy Name** and switch to **JSON** type.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/create_policies_1.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


In the field for the **Policy document**, you need to paste the code below with your unique **profile ID**.


<div class="st-callout info"><p class="st-callout-title">Importantly:</p>


Be sure to replace **YOUR_REGION**  and **YOUR_AWS_ID** with your region and account ID accordingly, <br>
(for example region and id "<strong><h style="color:DarkOrange;">eu-west-1:111197721064</h></strong>").


</div>


**For example of policy document:**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Publish",
        "iot:Receive"
      ],
      "Resource": [
        "arn:aws:iot:YOUR_REGION:YOUR_AWS_ID:topic/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "iot:Subscribe"
      ],
      "Resource": [
        "arn:aws:iot:YOUR_REGION:YOUR_AWS_ID:topicfilter/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "iot:Connect"
      ],
      "Resource": [
        "arn:aws:iot:YOUR_REGION:YOUR_AWS_ID:client/*"
      ]
    }
  ]
}
```


Your region is listed in the URL when you are signed in to your AWS IoT account. <br> For example: **https://<h style="color:orange;">eu-west-1</h>.console.aws.amazaon.com**


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/create_policies_2.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


After that, click the **Create** button. The policy will be added to the list, and you will receive the **Successfully created policy tb_policy** message.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/create_policies_3.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Create Things and Certificates
A Thing is a digital representation of a physical device or logical entity in AWS IoT.

You can create a conditional device in several steps, but for it need to go to the appropriate section. 
On the left, choose the **All devices** category - then **Things** item. This page will display
all your devices if you don't have them yet. At the top right, select the **Create thing** button to proceed 
to adding a device.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/add_device_0.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Consider the example of adding a single device, select the corresponding option the **Create 
single thing**, and then **Next** button.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/add_device_1.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


In the first stage, we will set the **Name** for the device, and at your discretion, additional parameters. 
Then press the **Next** button to move to the following step.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/add_device_2.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


At this stage, select the **Auto-generate a new certificate**. Certificates and keys will be available 
for download after confirming the addition of the device, so just click the next button.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/add_device_3.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


At the last stage, select your previously added policy and confirm the creation of a thing (device) 
with the **Create thing** button.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/add_device_4.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Upon completion, you will see an additional window with the possibility to download certificates and keys.

The list of files that are required to configure the integration:
- Device certificate (_*.pem.crt_)
- Private key (_*-private.pem.key_)
- Root CA certificate (_*.pem_)

AWS additionally requires you to save your **Public key file** for yourself, so please download that as well.

After saving the required, click the **Done**.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/save_certificates.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## SENTIENT setup

### Create Uplink Converter

Before creating the integration, you need to create an Uplink converter in Data converters. Uplink is
necessary in order to convert the incoming data from the device into the required format for displaying
them in SENTIENT. Click on the “plus” and on “Create new converter”. To view the events, enable Debug.
In the function decoder field, specify a script, for it copy the example Uplink converter, or
use own configuration to parse and transform data.

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

**Example for the Uplink converter:**

```ruby
// decode payload to JSON
var data = decodeToJson(payload);
var topicParts = metadata.topic.split("/");
var deviceType = topicParts[0];
var deviceName = topicParts[1];
// Result object with device attributes/telemetry data
var result = {
   deviceName: deviceName,
   deviceType: deviceType,
   attributes: {
       state: data.val0,
   },
   telemetry: {
       temperature: data.val1,
       fan_ins: data.val2,
       fan_out: data.val3,
   }
};

return result;
```


![image](/images/user-guide/integrations/aws-iot/aws-iot-uplink-converter-tbel-pe.webp)

</div>

<div class="st-tab" data-label="JavaScript">

**Example for the Uplink converter:**

```ruby
// decode payload to JSON
var payloadStr = decodeToString(payload);
var data = JSON.parse(payloadStr);
var topicParts = metadata.topic.split("/");
var deviceType = topicParts[0];
var deviceName = topicParts[1];
// Result object with device attributes/telemetry data
var result = {
   deviceName: deviceName,
   deviceType: deviceType,
   attributes: {
       state: data.val0,
   },
   telemetry: {
       temperature: data.val1,
       fan_ins: data.val2,
       fan_out: data.val3,
   }
};
/** Helper functions **/

function decodeToString(payload) {
    return String.fromCharCode.apply(String, payload);
}
function decodeToJson(payload) {
   // covert payload to string and then parse string to JSON
   return JSON.parse(decodeToString(payload));
}
return result;
```


![image](/images/user-guide/integrations/aws-iot/aws-iot-uplink-converter-java-pe.webp)


</div>

</div>


You can change the decoder function while creating the converter or after creating it. If the converter
has already been created, then click on the “pencil” icon to edit it.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/edit_converter_0.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/aws-iot/edit_converter_1.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/aws-iot/edit_converter_2.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Create Integration

- Go to **Integrations** section and click **Add new integration** button. Name it **"AWS IoT Integration"**, select type **AWS IoT**.

![image](/images/user-guide/integrations/aws-iot/aws-iot-add-integration-1-pe.webp)


<div class="st-callout info">


Note that if the “Allow create devices or assets” checkbox is unchecked, when sending a message to sentient
with any parameters of the device (or asset), if such a device (asset) does not exist, then device (asset) will not be created.


</div>


- The next steps is to add the recently created **Uplink** converter.

![image](/images/user-guide/integrations/aws-iot/aws-iot-add-integration-2-pe.webp)

- For now, leave the "Downlink data converter" field blank.

![image](/images/user-guide/integrations/aws-iot/aws-iot-add-integration-3-pe.webp)

- Enter AWS IoT Endpoint. You can find it in your [AWS account](https://aws.amazon.com/iot/) if you go to **Settings** - **Device data endpoint**. 


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/aws_endpoint_0.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/aws-iot/aws_endpoint_1.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- Download the previously generated certificates and key.

![image](/images/user-guide/integrations/aws-iot/aws-iot-add-integration-4-pe.webp)

- Add a Topic Filter **tb/aws/iot/#**. You can also select QoS level. We use QoS level 0 (At most once) by default.
- Click **Add** to create an integration.

![image](/images/user-guide/integrations/aws-iot/aws-iot-add-integration-5-pe.webp)

### Send Uplink message

To send a test message, use the additional functionality of AWS IoT, the MQTT test client.
In the main menu, go to **MQTT test client**, then select the **Publish to a topic** tab.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/send_uplink_0.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


**Example of topic:**
```
tb/aws/iot/sensors/freezer-432
```


**Example of payload:**
```ruby
{
    "val0": "loaded",
    "val1": -18,
    "val2": 1785,
    "val3": 548
}
```


To check if the message has arrived at AWS IoT integration open the events tab of integration.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/send_uplink_1.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/aws-iot/send_uplink_2.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Advanced usage: Create Downlink Converter

Let's look at a simple example to test a connection and send a message. For it need to create a downlink
Data converter. Then set the converter and topic in the AWS IoT integration.

> One can use either [TBEL](/docs/pe/user-guide/tbel/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/pe/user-guide/tbel/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/create-downlink-converter-tbel-1-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/aws-iot/downlink_1.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/aws-iot/downlink_1(2).png" alt="" loading="lazy"><figcaption></figcaption></figure></div>


An example of downlink converter:

```ruby
// Encode downlink data from incoming Rule Engine message

// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter

/** Encoder **/
var data = {};

// Process data from incoming message and metadata
data.v0 = msg.state;
data.m0 = "att_upd_success";
data.devSerialNumber = metadata['ss_serialNumber'];

// Result object with encoded downlink payload
var result = {
    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",
    // downlink data
    data: JSON.stringify(data),
    // Optional metadata object presented in key/value format
    metadata: {
            type: "sensors/device/upload"
    }
};
return result;
```


</div>

<div class="st-tab" data-label="JavaScript">


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/create-downlink-converter-java-1-pe.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/aws-iot/downlink_1.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/aws-iot/downlink_1(2).png" alt="" loading="lazy"><figcaption></figcaption></figure></div>


An example of downlink converter:

```ruby
// Encode downlink data from incoming Rule Engine message

// msg - JSON message payload downlink message json
// msgType - type of message, for ex. 'ATTRIBUTES_UPDATED', 'POST_TELEMETRY_REQUEST', etc.
// metadata - list of key-value pairs with additional data about the message
// integrationMetadata - list of key-value pairs with additional data defined in Integration executing this converter

/** Encoder **/
var data = {};

// Process data from incoming message and metadata
data.v0 = msg.state;
data.m0 = "att_upd_success";
data.devSerialNumber = metadata['ss_serialNumber'];

// Result object with encoded downlink payload
var result = {
    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",
    // downlink data
    data: JSON.stringify(data),
    // Optional metadata object presented in key/value format
    metadata: {
            type: "sensors/device/upload"
    }
};
return result;
```


</div>

</div>


Next, configure the conditions under which a message will be sent through the AWS IoT Downlink integration.
To do this, you need to open the Rule Chain used for the device (in our case, the default Root Rule Chain), then add an [integration downlink node](https://sentient.invenia.in/docs/user-guide/rule-engine-2-0/nodes/action/integration-downlink/), for link condition set the Attributes Updated.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/downlink_2.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/aws-iot/downlink_3.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


To subscribe to a topic for receive messages from Sentient, use the **AWS MQTT test client**.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/downlink_4.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Now you can update the device attribute. To do this, open **Device**, **Attributes** tab, and choose 
**Shared Attributes**, then select any attribute, or add a new one to update it.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/downlink_5.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


The result can be tracked on AWS page where you subscribed to the topic:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/aws-iot/downlink_6.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Video tutorial

See video tutorial below for step-by-step instruction how to setup AWS IoT Integration (Outdated interface).

<br>
<div id="video">  
 <div id="video_wrapper">
     <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/udkuOUrNzWk" frameborder="0" allowfullscreen></iframe>
 </div>
</div>

## Next steps
