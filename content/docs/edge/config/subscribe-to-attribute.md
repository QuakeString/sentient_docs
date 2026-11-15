+++
title = "Bidirectional Attribute Subscription And Update with Post-Processing"
description = "Bidirectional Attribute Subscription And Update with Post-Processing"

[extra]
status = "imported"
checked = ""
source = "docs/edge/config/subscribe-to-attribute.md"
+++
## Overview

In SENTIENT, **device attributes** are key-value pairs associated with devices. They are used to store configuration settings, metadata, or other relevant information. 

Subscribing to device attributes enables clients to receive updates when these attributes change. The subscription methods vary based on the attribute type and the communication protocol used.

Attributes are categorized into three types:
* **Server-side Attributes:** Set and used exclusively by the server. Can be configured via User Interface (UI) or REST API.
* **Shared Attributes:** Devices can subscribe to updates to receive real-time notifications when the server modifies them. Can be configured via UI or REST API.
* **Client-side Attributes:** Set by the device and stored on the server. Can only be read via UI or REST API.

For more detailed information and examples, please refer to the SENTIENT documentation on [Working with IoT Device Attributes](/docs/user-guide/attributes/).

The following guide explains real-time, bidirectional communication between your device and the **SENTIENT Cloud** via **SENTIENT Edge**.

## Prerequisites

* The **SENTIENT Cloud** or locally hosted [Server](/docs/user-guide/install/installation-options/).
* The installed **SENTIENT Edge** with network access.
* A **Device** capable of connecting to **SENTIENT Edge** via [MQTT](/docs/reference/mqtt-api/), [HTTP](/docs/reference/http-api/), or [CoAP](/docs/reference/coap-api/).

## Step 1. Configure a Rule Chain for the Edge

To automatically route messages (data or attributes) from the device to the **SENTIENT Cloud**, configure the rule chain for the **SENTIENT Edge**:


1. Log in to the <b>SENTIENT Cloud</b> and go to the <b>Edge management > Rule chain templates</b> section and click on the <b>Rule chain</b> assigned to your <b>Edge instance.</b><ul><li>If you are using <b>Edge 4.0</b> or later, stay in your <b>Edge</b> instance and go to the <b>Rule chains</b> section. To edit a rule chain, click the appropriate <b>Rule Chain</b>.</li></ul>

1. On the <b>Rule Chain</b> edit page, in the Node search bar find the <b>"push to cloud"</b> node. It pushes messages from Edge to Cloud. Drag and drop the node onto the <b>Rule Chain</b> sheet. Then, in the <b>"Add rule node"</b> pop-up window enter the node title and select the <b>"Client attributes"</b> option in the <b>"Entity attributes scope"</b> field. Click the <b>"Add"</b> button to proceed.

1. Connect the <b>“save attributes”</b> and <b>“save time series”</b> nodes to the <b>"push to cloud"</b> node and set the <b>"Success"</b> link label. Click the <b>“Apply changes”</b> button on the <b>Rule Chain</b> sheet.


<div class="st-gallery"><figure><img src="/images/edge/config/subscribe-to-attribute/1-rule-chain-templates.webp" alt="Log in to the SENTIENT Cloud and go to the Edge management > Rule chain templates section and click on the Rule chain assigned to your Edge instance.If you are using Edge 4.0 or later, stay in your Edge instance and go to the Rule chains section. To edit a rule chain, click the appropriate Rule Chain." loading="lazy"><figcaption>Log in to the <b>SENTIENT Cloud</b> and go to the <b>Edge management > Rule chain templates</b> section and click on the <b>Rule chain</b> assigned to your <b>Edge instance.</b><ul><li>If you are using <b>Edge 4.0</b> or later, stay in your <b>Edge</b> instance and go to the <b>Rule chains</b> section. To edit a rule chain, click the appropriate <b>Rule Chain</b>.</li></ul></figcaption></figure><figure><img src="/images/edge/config/subscribe-to-attribute/2-add-push-to-cloud.webp" alt="On the Rule Chain edit page, in the Node search bar find the &quot;push to cloud&quot; node. It pushes messages from Edge to Cloud. Drag and drop the node onto the Rule Chain sheet. Then, in the &quot;Add rule node&quot; pop-up window enter the node title and select the &quot;Client attributes&quot; option in the &quot;Entity attributes scope&quot; field. Click the &quot;Add&quot; button to proceed." loading="lazy"><figcaption>On the <b>Rule Chain</b> edit page, in the Node search bar find the <b>"push to cloud"</b> node. It pushes messages from Edge to Cloud. Drag and drop the node onto the <b>Rule Chain</b> sheet. Then, in the <b>"Add rule node"</b> pop-up window enter the node title and select the <b>"Client attributes"</b> option in the <b>"Entity attributes scope"</b> field. Click the <b>"Add"</b> button to proceed.</figcaption></figure><figure><img src="/images/edge/config/subscribe-to-attribute/3-save.webp" alt="Connect the “save attributes” and “save time series” nodes to the &quot;push to cloud&quot; node and set the &quot;Success&quot; link label. Click the “Apply changes” button on the Rule Chain sheet." loading="lazy"><figcaption>Connect the <b>“save attributes”</b> and <b>“save time series”</b> nodes to the <b>"push to cloud"</b> node and set the <b>"Success"</b> link label. Click the <b>“Apply changes”</b> button on the <b>Rule Chain</b> sheet.</figcaption></figure></div>


## Step 2. Configure a Rule Chain for the Cloud

To send back some attributes update message to the Edge, modify root rule chain on the cloud. Once the attribute update message will arrive to the edge you should see this message on the device.


1. Go to the <b>Rule Chains</b> section, to modify the <b>Rule Chain.</b>

1. On the <b>Rule Chain</b> edit page, in the Node search bar find the <b>"script"</b> node. It allows modification of message payload, metadata or message type with JavaScript. Drag and drop the node onto the <b>Rule Chain</b> sheet. Then, in the <b>"Add rule node: script"</b> pop-up window enter the node title and enter the script below. Click the <b>"Add"</b> button to proceed.

1. On the <b>Rule Chain</b> edit page, in the Node search bar find the <b>"push to edge"</b> node. It pushes messages from Cloud to Edge. Drag and drop the node onto the <b>Rule Chain</b> sheet. Then, in the <b>"Add rule node"</b> pop-up window enter the node title and select the <b>"Shared attributes"</b> option in the <b>"Entity attributes scope"</b> field. Click the <b>"Add"</b> button to proceed.

1. Connect the <b>“save attributes”</b> and <b>“save time series”</b> nodes to the <b>"push to edge"</b> node and set the <b>"Success"</b> link label. Click the <b>“Apply changes”</b> button on the <b>Rule Chain</b> sheet.


<div class="st-gallery"><figure><img src="/images/edge/config/subscribe-to-attribute/4-rule-chain.webp" alt="Go to the Rule Chains section, to modify the Rule Chain." loading="lazy"><figcaption>Go to the <b>Rule Chains</b> section, to modify the <b>Rule Chain.</b></figcaption></figure><figure><img src="/images/edge/config/subscribe-to-attribute/5-add-script.webp" alt="On the Rule Chain edit page, in the Node search bar find the &quot;script&quot; node. It allows modification of message payload, metadata or message type with JavaScript. Drag and drop the node onto the Rule Chain sheet. Then, in the &quot;Add rule node: script&quot; pop-up window enter the node title and enter the script below. Click the &quot;Add&quot; button to proceed." loading="lazy"><figcaption>On the <b>Rule Chain</b> edit page, in the Node search bar find the <b>"script"</b> node. It allows modification of message payload, metadata or message type with JavaScript. Drag and drop the node onto the <b>Rule Chain</b> sheet. Then, in the <b>"Add rule node: script"</b> pop-up window enter the node title and enter the script below. Click the <b>"Add"</b> button to proceed.</figcaption></figure><figure><img src="/images/edge/config/subscribe-to-attribute/5-add-push-to-edge.webp" alt="On the Rule Chain edit page, in the Node search bar find the &quot;push to edge&quot; node. It pushes messages from Cloud to Edge. Drag and drop the node onto the Rule Chain sheet. Then, in the &quot;Add rule node&quot; pop-up window enter the node title and select the &quot;Shared attributes&quot; option in the &quot;Entity attributes scope&quot; field. Click the &quot;Add&quot; button to proceed." loading="lazy"><figcaption>On the <b>Rule Chain</b> edit page, in the Node search bar find the <b>"push to edge"</b> node. It pushes messages from Cloud to Edge. Drag and drop the node onto the <b>Rule Chain</b> sheet. Then, in the <b>"Add rule node"</b> pop-up window enter the node title and select the <b>"Shared attributes"</b> option in the <b>"Entity attributes scope"</b> field. Click the <b>"Add"</b> button to proceed.</figcaption></figure><figure><img src="/images/edge/config/subscribe-to-attribute/6-save.webp" alt="Connect the “save attributes” and “save time series” nodes to the &quot;push to edge&quot; node and set the &quot;Success&quot; link label. Click the “Apply changes” button on the Rule Chain sheet." loading="lazy"><figcaption>Connect the <b>“save attributes”</b> and <b>“save time series”</b> nodes to the <b>"push to edge"</b> node and set the <b>"Success"</b> link label. Click the <b>“Apply changes”</b> button on the <b>Rule Chain</b> sheet.</figcaption></figure></div>


To rewrite and return received data back to Edge, add the following script into the **"script"** node:
```bash
// POST PROCESSING LOGIC
msg = {"attribute1_result": "value1_result"};
metadata = {};

return {msg: msg, metadata: metadata, msgType: msgType};
```


## Step 3. Subscribe to Device Attributes Change And Publish Device Attributes Message

The procedure for subscribing to the **Device Attribute Changes** and subsequently publishing the **Device Attributes Message** depends on the protocol used. There are  the most commonly used protocols for basic telemetry and attribute updates in IoT applications:


<div class="st-tabs">

<div class="st-tab" data-label="MQTT">

**MQTT** is a lightweight protocol commonly used for IoT communication. 

To facilitate communication with **SENTIENT Edge** using **MQTT**, we recommend installing the [MQTT Broker](/docs/reference/mqtt-api/?connectdevice=mqtt-linux#mqtt-connect). This allows the device to **publish** telemetry or attribute messages and **subscribe** to topics for attribute updates.

#### Subscribe to the Changes in Shared Device Attributes

To subscribe to shared device attribute changes, send the SUBSCRIBE message:
```bash
mosquitto_sub -d -h $SENTIENT_HOST_NAME -t "v1/devices/me/attributes" -u "$ACCESS_TOKEN"
```


* **v1/devices/me/attributes:** This is a topic on SENTIENT Edge. It allows the device to listen for any updates related to its attributes from the cloud.
* Replace the **$SENTIENT_HOST_NAME** with the actual hostname or IP address of your SENTIENT Edge instance. 
    


  


1. Replace the **$ACCESS_TOKEN** with the actual access token of the device. To find the device access token, go to the **Entities > Devices** section and click on the device. On the **"Device details"** page, you can copy the token by clicking the **"Copy access token"** button.


<div class="st-gallery"><figure><img src="/images/edge/config/subscribe-to-attribute/9-copy-access-token.webp" alt="Replace the **$ACCESS_TOKEN** with the actual access token of the device. To find the device access token, go to the **Entities > Devices** section and click on the device. On the **&quot;Device details&quot;** page, you can copy the token by clicking the **&quot;Copy access token&quot;** button." loading="lazy"><figcaption>Replace the **$ACCESS_TOKEN** with the actual access token of the device. To find the device access token, go to the **Entities > Devices** section and click on the device. On the **"Device details"** page, you can copy the token by clicking the **"Copy access token"** button.</figcaption></figure></div>


#### Publish Time-Series or Attribute Message.

To publish client-side device attributes to the **SENTIENT Edge**, send a PUBLISH message. 

You can publish the telemetry data:

```bash
mosquitto_pub -d -h $SENTIENT_HOST_NAME -t "v1/devices/me/attributes" -u "$ACCESS_TOKEN" -m "{"attribute1": "value1", "attribute2": true}"
```


* **v1/devices/me/attributes:** The topic to which the telemetry data is published.
* **$SENTIENT_HOST_NAME:** The actual hostname or IP address of your SENTIENT Edge instance
* **$ACCESS_TOKEN:** The actual access token of the device.
* **{"attribute1": "value1", "attribute2": true}** The telemetry data.

You can also publish client-side attributes update using data from [**new-attributes-values.json**](/docs/reference/resources/new-attributes-values.json) file:

```bash
mosquitto_pub -d -h $SENTIENT_HOST_NAME -t "v1/devices/me/attributes" -u "$ACCESS_TOKEN" -f "new-attributes-values.json"
```


</div>

<div class="st-tab" data-label="HTTP">

**HTTP** is a general-purpose network protocol that can be used in IoT applications. HTTP protocol is TCP based and uses request-response model.

#### Subscribe to the Changes in Shared Device Attributes

To subscribe to changes in shared device attributes, send a GET request to the following URL, with an optional 'timeout' parameter:

```bash
http(s)://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes/updates
```


* **/attributes/updates** The endpoint that is used to fetch the updates of device attributes.
* Replace the **$SENTIENT_HOST_NAME** with the actual hostname or IP address of your SENTIENT Edge instance.


  


1. Replace the **$ACCESS_TOKEN** with the actual access token of the device. To find the device access token, go to the **Entities > Devices** section and click on the device. On the **"Device details"** page, you can copy the token by clicking the **"Copy access token"** button.


<div class="st-gallery"><figure><img src="/images/edge/config/subscribe-to-attribute/9-copy-access-token.webp" alt="Replace the **$ACCESS_TOKEN** with the actual access token of the device. To find the device access token, go to the **Entities > Devices** section and click on the device. On the **&quot;Device details&quot;** page, you can copy the token by clicking the **&quot;Copy access token&quot;** button." loading="lazy"><figcaption>Replace the **$ACCESS_TOKEN** with the actual access token of the device. To find the device access token, go to the **Entities > Devices** section and click on the device. On the **"Device details"** page, you can copy the token by clicking the **"Copy access token"** button.</figcaption></figure></div>


Execute the command:
```bash
curl -v -X GET http(s)://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes/updates?timeout=20000
```


* **timeout=20000** The server will keep the connection open for 20 seconds. If a **shared attribute** for the device is updated within this timeout period, the server will respond immediately with the update.

#### Publish Time-Series or Attribute Message.

To publish client-side device attributes to the **SENTIENT Edge**, send a POST request to the following URL:

```bash
http(s)://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes
```


* **$SENTIENT_HOST_NAME:** The actual hostname or IP address of your SENTIENT Edge instance
* **$ACCESS_TOKEN:** The actual access token of the device.

Publish client-side attributes update

```bash
curl -v -X POST --data "{"attribute1": "value1", "attribute2":true, "attribute3": 43.0}" https:/$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes --header "Content-Type:application/json"
```

You can also publish client-side attributes update using data from [**new-attributes-values.json**](/docs/reference/resources/new-attributes-values.json) file:

```bash
curl -v -X POST -d @new-attributes-values.json https://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes --header "Content-Type:application/json"
```


</div>

<div class="st-tab" data-label="CoAP">

**CoAP** is a light-weight IoT protocol for constrained devices. **CoAP** protocol is UDP based, but similar to HTTP it uses request-response model. 
#### Subscribe to the Changes in Shared Device Attributes

To subscribe to changes in shared device attributes, send a GET request to the following URL:

```bash
coap://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes
```


* Replace the **$SENTIENT_HOST_NAME** with the actual hostname or IP address of your SENTIENT Edge instance.


  


1. Replace the **$ACCESS_TOKEN** with the actual access token of the device. To find the device access token, go to the **Entities > Devices** section and click on the device. On the **"Device details"** page, you can copy the token by clicking the **"Copy access token"** button.


<div class="st-gallery"><figure><img src="/images/edge/config/subscribe-to-attribute/9-copy-access-token.webp" alt="Replace the **$ACCESS_TOKEN** with the actual access token of the device. To find the device access token, go to the **Entities > Devices** section and click on the device. On the **&quot;Device details&quot;** page, you can copy the token by clicking the **&quot;Copy access token&quot;** button." loading="lazy"><figcaption>Replace the **$ACCESS_TOKEN** with the actual access token of the device. To find the device access token, go to the **Entities > Devices** section and click on the device. On the **"Device details"** page, you can copy the token by clicking the **"Copy access token"** button.</figcaption></figure></div>


Execute the command:
```bash
coap get -o coap://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes
```


Once shared attribute will be changed by one of the server-side components (REST API or Rule Chain) the client will receive the update.

#### Publish Time-Series or Attribute Message.

To publish client-side device attributes to the **SENTIENT Edge**, send a POST request to the following URL:

```bash
coap://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes
```


* **$SENTIENT_HOST_NAME:** The actual hostname or IP address of your SENTIENT Edge instance
* **$ACCESS_TOKEN:** The actual access token of the device.

Publish client-side attributes update using data from [**new-attributes-values.json**](/docs/reference/resources/new-attributes-values.json) file:

```bash
cat new-attributes-values.json | coap post coap://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes
```


</div>

</div>


## Step 4. Confirm the Results

Confirm the received and pushed attributes:


1. Once you have subscribed to attribute updates, you will receive updates as the attributes change. We have used the <b>MQTT protocol</b> as an example. The updates were received after new attributes were published.


<div class="st-gallery"><figure><img src="/images/edge/config/subscribe-to-attribute/10-subscribe-post-update-attributes-mqtt.webp" alt="Once you have subscribed to attribute updates, you will receive updates as the attributes change. We have used the MQTT protocol as an example. The updates were received after new attributes were published." loading="lazy"><figcaption>Once you have subscribed to attribute updates, you will receive updates as the attributes change. We have used the <b>MQTT protocol</b> as an example. The updates were received after new attributes were published.</figcaption></figure></div>


1. To confirm if the <b>client-side attributes</b> are received, go to the <b>Entities > Devices</b> section of your <b>Edge</b> and click on the <b>device</b>. On the <b>"Device details"</b> page, select the <b>"Attributes"</b> tab and select the <b>"Client attributes"</b> option in the <b>"Entity attributes scope"</b> drop-down menu.


<div class="st-gallery"><figure><img src="/images/edge/config/subscribe-to-attribute/7-confirm-on-device-1.webp" alt="To confirm if the client-side attributes are received, go to the Entities > Devices section of your Edge and click on the device. On the &quot;Device details&quot; page, select the &quot;Attributes&quot; tab and select the &quot;Client attributes&quot; option in the &quot;Entity attributes scope&quot; drop-down menu." loading="lazy"><figcaption>To confirm if the <b>client-side attributes</b> are received, go to the <b>Entities > Devices</b> section of your <b>Edge</b> and click on the <b>device</b>. On the <b>"Device details"</b> page, select the <b>"Attributes"</b> tab and select the <b>"Client attributes"</b> option in the <b>"Entity attributes scope"</b> drop-down menu.</figcaption></figure></div>


1. To confirm if the attributes message is received and pushed to Cloud, go to the <b>Rule chains</b> section of your Edge instance and click on the <b>Rule chain</b>. Click on the <b>"push to cloud"</b> node.

1. On the <b>"Push to cloud"</b> page, select the <b>"Events"</b> tab. If you have debug mode enabled, select the <b>"Debug"</b> option in the <b>"Event type"</b> drop-down menu. You should see the new records - <b>"IN"</b> and <b>"OUT"</b>, where the <b>"IN"</b> record defines the attributes received from the device, and the <b>"OUT"</b> record defines the attributes message pushed to the <b>Cloud</b>.


<div class="st-gallery"><figure><img src="/images/edge/config/subscribe-to-attribute/8-confirm-on-edge-node-1.webp" alt="To confirm if the attributes message is received and pushed to Cloud, go to the Rule chains section of your Edge instance and click on the Rule chain. Click on the &quot;push to cloud&quot; node." loading="lazy"><figcaption>To confirm if the attributes message is received and pushed to Cloud, go to the <b>Rule chains</b> section of your Edge instance and click on the <b>Rule chain</b>. Click on the <b>"push to cloud"</b> node.</figcaption></figure><figure><img src="/images/edge/config/subscribe-to-attribute/8-confirm-on-edge-node-2.webp" alt="On the &quot;Push to cloud&quot; page, select the &quot;Events&quot; tab. If you have debug mode enabled, select the &quot;Debug&quot; option in the &quot;Event type&quot; drop-down menu. You should see the new records - &quot;IN&quot; and &quot;OUT&quot;, where the &quot;IN&quot; record defines the attributes received from the device, and the &quot;OUT&quot; record defines the attributes message pushed to the Cloud." loading="lazy"><figcaption>On the <b>"Push to cloud"</b> page, select the <b>"Events"</b> tab. If you have debug mode enabled, select the <b>"Debug"</b> option in the <b>"Event type"</b> drop-down menu. You should see the new records - <b>"IN"</b> and <b>"OUT"</b>, where the <b>"IN"</b> record defines the attributes received from the device, and the <b>"OUT"</b> record defines the attributes message pushed to the <b>Cloud</b>.</figcaption></figure></div>


1. To confirm if the attributes message is received on the Cloud and pushed back to the Edge, go to the <b>Rule chains</b> section of your Cloud and click on the <b>Rule chain</b>. Click twice on the <b>"push to edge"</b> node.

1. On the <b>"Push to edge"</b> page, select the <b>"Events"</b> tab. If you have debug mode enabled, select the <b>"Debug"</b> option from the <b>"Event type"</b> drop-down menu. You should see two new records - <b>"IN"</b> and <b>"OUT"</b>, where the <b>"IN"</b> record defines the attributes received from Edge, and the <b>"OUT"</b> record defines the attributes message pushed back to <b>Edge</b>.


<div class="st-gallery"><figure><img src="/images/edge/config/subscribe-to-attribute/9-confirm-on-cloud-node-1.webp" alt="To confirm if the attributes message is received on the Cloud and pushed back to the Edge, go to the Rule chains section of your Cloud and click on the Rule chain. Click twice on the &quot;push to edge&quot; node." loading="lazy"><figcaption>To confirm if the attributes message is received on the Cloud and pushed back to the Edge, go to the <b>Rule chains</b> section of your Cloud and click on the <b>Rule chain</b>. Click twice on the <b>"push to edge"</b> node.</figcaption></figure><figure><img src="/images/edge/config/subscribe-to-attribute/9-confirm-on-cloud-node-2.webp" alt="On the &quot;Push to edge&quot; page, select the &quot;Events&quot; tab. If you have debug mode enabled, select the &quot;Debug&quot; option from the &quot;Event type&quot; drop-down menu. You should see two new records - &quot;IN&quot; and &quot;OUT&quot;, where the &quot;IN&quot; record defines the attributes received from Edge, and the &quot;OUT&quot; record defines the attributes message pushed back to Edge." loading="lazy"><figcaption>On the <b>"Push to edge"</b> page, select the <b>"Events"</b> tab. If you have debug mode enabled, select the <b>"Debug"</b> option from the <b>"Event type"</b> drop-down menu. You should see two new records - <b>"IN"</b> and <b>"OUT"</b>, where the <b>"IN"</b> record defines the attributes received from Edge, and the <b>"OUT"</b> record defines the attributes message pushed back to <b>Edge</b>.</figcaption></figure></div>


## Next Steps
