+++
title = "Azure Event Hub Integration"
description = "Azure Event Hub Integration Guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/azure-event-hub.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

## Overview

Azure Event Hub Integration allows to stream data from Azure Event Hub to SENTIENT and converts device payloads to the SENTIENT format.

{{ diagram(name="azure-event-hub-integration") }}
 
## Create IoT hub using the Azure portal.

First, sign in to the [Azure portal](https://portal.azure.com/).

### Create IoT Hub in Azure

For now, you need to create IoT hub. Here you will create devices and do some other operations. Let's do this step by step:

- In the Azure portal, click on the "**Create a resource**" button;
- In the search field, type "**IoT Hub**" and select the matching item from the list;
- Click "**Create**";
- On the configuration page, click "**Create new**", specify the resource group and IoT hub name, then click "**Review + create**";
- On the next page, click "**Create**";
- Wait for the deployment process to complete, and then click "**Go to resource**";


<div class="st-gallery"><figure><img src="/images/azure-event-hub/create_a_resource.webp" alt="In the Azure portal, click on the &quot;Create a resource&quot; button;" loading="lazy"><figcaption>In the Azure portal, click on the "Create a resource" button;</figcaption></figure><figure><img src="/images/azure-event-hub/select_iot_hub.webp" alt="In the search field, type &quot;IoT Hub&quot; and select the matching item from the list;" loading="lazy"><figcaption>In the search field, type "IoT Hub" and select the matching item from the list;</figcaption></figure><figure><img src="/images/azure-event-hub/create_iot_hub.webp" alt="Click &quot;Create&quot;;" loading="lazy"><figcaption>Click "Create";</figcaption></figure><figure><img src="/images/azure-event-hub/basics_iot_hub.webp" alt="On the configuration page, click &quot;Create new&quot;, specify the resource group and IoT hub name, then click &quot;Review + create&quot;;" loading="lazy"><figcaption>On the configuration page, click "Create new", specify the resource group and IoT hub name, then click "Review + create";</figcaption></figure><figure><img src="/images/azure-event-hub/create_basics_iot_hub.webp" alt="On the next page, click &quot;Create&quot;;" loading="lazy"><figcaption>On the next page, click "Create";</figcaption></figure><figure><img src="/images/azure-event-hub/deployment_is_in_progress.webp" alt="Wait for the deployment process to complete;" loading="lazy"><figcaption>Wait for the deployment process to complete;</figcaption></figure><figure><img src="/images/azure-event-hub/go_to_resource.webp" alt="Click &quot;Go to resource&quot;." loading="lazy"><figcaption>Click "Go to resource".</figcaption></figure></div>


### Create device in IoT Hub

After completing the first step, follow these instructions to create a new device:

- Navigate to the "**IoT devices**" page from the context menu;
- Click the "**+ New**" button;
- In the pop-up window, enter the "**Device ID**" and click "**Save**".

Great! You have successfully created your new device.


<div class="st-gallery"><figure><img src="/images/azure-event-hub/iot_devices.webp" alt="Navigate to the &quot;IoT devices&quot; page from the context menu;" loading="lazy"><figcaption>Navigate to the "IoT devices" page from the context menu;</figcaption></figure><figure><img src="/images/azure-event-hub/iot_devices_new.webp" alt="Click the &quot;+ New&quot; button;" loading="lazy"><figcaption>Click the "+ New" button;</figcaption></figure><figure><img src="/images/azure-event-hub/save_device_id.webp" alt="In the pop-up window, enter the &quot;Device ID&quot; and click &quot;Save&quot;;" loading="lazy"><figcaption>In the pop-up window, enter the "Device ID" and click "Save";</figcaption></figure><figure><img src="/images/azure-event-hub/your_devices.webp" alt="Great! You have successfully created your new device." loading="lazy"><figcaption>Great! You have successfully created your new device.</figcaption></figure></div>


## Add Azure Event Hub integration

**1. Basic settings**.

Go to the "**Integrations**" page of the "**Integrations center**" section. Click "**plus**" button to start adding new integration. Select type "**Azure Event Hub**" integration and click "**Next**";

![image](/images/user-guide/integrations/azure-event-hub/azure-event-hub-integration-setup-1-pe.webp)

<br>
**2. Uplink data converter**. 

Uplink is necessary in order to convert the incoming data from the device into the required format for displaying them in the SENTIENT.

In the function decoder field, specify a script to parse and transform data. For our example, use the default decoder function (or use your own configuration). Then, click "**Next**";

![image](/images/user-guide/integrations/azure-event-hub/azure-event-hub-integration-setup-2-pe.webp)

You can always change the decoder function after creating it.

<br>
**3. Downlink data converter**.

At the step of adding a downlink converter, you can also select a previously created or create a new downlink converter. But for now, leave the "Downlink data converter" field empty. Click "**Skip**";

![image](/images/user-guide/integrations/azure-event-hub/azure-event-hub-integration-setup-3-pe.webp)

<br>
**4. Connection**.

Retrieve the Event Hub-compatible Endpoint in the Azure portal:

- Navigate to the "**IoT Hub**" resource;
- Open the "**Built-in endpoints**" page from the context menu;
- Locate and copy the "**Event Hub-compatible endpoint**" value.

This value will be used to integrate with SENTIENT services.


<div class="st-gallery"><figure><img src="/images/azure-event-hub/built_in_endpoints.webp" alt="In the Azure portal, navigate to the &quot;IoT Hub&quot; resource, and open the &quot;Built-in endpoints&quot; page from the context menu;" loading="lazy"><figcaption>In the Azure portal, navigate to the "IoT Hub" resource, and open the "Built-in endpoints" page from the context menu;</figcaption></figure><figure><img src="/images/azure-event-hub/event_hub_compatible_endpoint.webp" alt="Copy and save the &quot;Event Hub-compatible endpoint&quot; value." loading="lazy"><figcaption>Copy and save the "Event Hub-compatible endpoint" value.</figcaption></figure></div>


<br>
To find the **container name**:

- In the Azure portal, click the "**Storage account**";
- Go to the "**Containers**" page of the "**Data storage**" section.

Here you will find the **container**. Save its name.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/azure-event-hub/container-1.webp" alt="In the Azure portal, click the &quot;Storage account&quot;;" loading="lazy"><figcaption>In the Azure portal, click the "Storage account";</figcaption></figure><figure><img src="/images/user-guide/integrations/azure-event-hub/container-2.webp" alt="Go to the &quot;Containers&quot; page of the &quot;Data storage&quot; section. Here you will find the container. Save its name." loading="lazy"><figcaption>Go to the "Containers" page of the "Data storage" section. Here you will find the container. Save its name.</figcaption></figure></div>


<br>
To find the storage <b>connection string</b> values, navigate to the "<b>Access keys</b>" page in the "<b>Security + networking</b>" section.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/azure-event-hub/storage-connection-string-1.webp" alt="To find the storage connection string values, navigate to the &quot;Access keys&quot; page in the &quot;Security + networking&quot; section." loading="lazy"><figcaption>To find the storage connection string values, navigate to the "Access keys" page in the "Security + networking" section.</figcaption></figure></div>


<br>
In SENTIENT:

- Paste in the "**Connection String**" field copied "**Event Hub-compatible endpoint**";
- Enable persistent checkpoints to resume processing from the last checkpoint after an integration restart, and fill in the fields "**Storage connection string**" and "**Container name**" with the appropriate values. Disable to always start from the latest event;
- [Optional] Click on "Check connection" button to check connection to check correctly copied connection string;
- Finally, click "**Add**" button to create the integration.

![image](/images/user-guide/integrations/azure-event-hub/azure-event-hub-integration-setup-4-pe.webp)

## Test it up!

For now, we ready to test our integration. To do this, follow these steps:

1) Go to the "<b>Rule chains</b>" page and select one of your rule chains. In the search nodes field, type &#39;gen&#39; to find the <b>generator</b> node in the menu. Drag it onto the canvas. In the pop-up window, specify the <b>name</b> of the generator, the <b>number of messages</b>, and the <b>generate function</b> (you can use our example). Finally, click "<b>Add</b>";


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/azure-event-hub/test-azure-event-hub-integration-1-pe.webp" alt="Go to the &quot;Rule chains&quot; page and select one of your rule chains. In the search nodes field, type &#39;gen&#39; to find the generator node in the menu. Drag it onto the canvas. In the pop-up window, specify the name of the generator, the number of messages, and the generate function (you can use our example). Finally, click &quot;Add&quot;;" loading="lazy"><figcaption>Go to the "<b>Rule chains</b>" page and select one of your rule chains. In the search nodes field, type &#39;gen&#39; to find the <b>generator</b> node in the menu. Drag it onto the canvas. In the pop-up window, specify the <b>name</b> of the generator, the <b>number of messages</b>, and the <b>generate function</b> (you can use our example). Finally, click "<b>Add</b>";</figcaption></figure></div>


```javascript
var msg = {
    "devName": "ST-D-01",
    "msg": {
        "temp": 42,
        "humidity": 77
    }
};
var metadata = { data: 40 };
var msgType = "POST_TELEMETRY_REQUEST";

return { msg: msg, metadata: metadata, msgType: msgType };
```


2) Now, find the device&#39;s <b>Primary key</b>. Go to the Azure portal, navigate to the <b>IoT devices</b> tab, select your device, and locate the "<b>Primary key</b>" field. Copy and save it for later use;


<div class="st-gallery"><figure><img src="/images/azure-event-hub/your_devices.webp" alt="Now, find the device&#39;s Primary key. Go to the Azure portal, navigate to the IoT devices tab, and select your device;" loading="lazy"><figcaption>Now, find the device&#39;s <b>Primary key</b>. Go to the Azure portal, navigate to the <b>IoT devices</b> tab, and select your device;</figcaption></figure><figure><img src="/images/azure-event-hub/primary_key.webp" alt="Locate the &quot;Primary key&quot; field. Copy and save it for later use." loading="lazy"><figcaption>Locate the "<b>Primary key</b>" field. Copy and save it for later use.</figcaption></figure></div>


3) Return to your SENTIENT instance. We need to find another rule node. Type &#39;iot&#39; in the search nodes field and select the <b>azure iot hub</b> node. Drag it onto the canvas. In the pop-up window, specify the <b>node name</b>, replace <b>&#60;device_id&#62;</b> in the <b>Topic</b> with your Device Name, and enter the <b>Hostname</b> by retrieving it from the "<b>IoT Hub</b>" resource in the Azure portal. Enter the Device Name as the <b>Device ID</b> and add the <b>SAS Key</b> (<b>Primary Key</b>) that we previously copied from the device credentials. If you need to monitor events, enable Debug mode;


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/azure-event-hub/test-azure-event-hub-integration-2-pe.webp" alt="Return to your SENTIENT instance. We need to find another rule node. Type &#39;iot&#39; in the search nodes field and select the azure iot hub node. Drag it onto the canvas. In the pop-up window, specify the node name, replace &#60;device_id&#62; in the Topic with your Device Name, and enter the Hostname by retrieving it from the &quot;IoT Hub&quot; resource in the Azure portal. Enter the Device Name as the Device ID and add the SAS Key (Primary Key) that we previously copied from the device credentials. If you need to monitor events, enable Debug mode;" loading="lazy"><figcaption>Return to your SENTIENT instance. We need to find another rule node. Type &#39;iot&#39; in the search nodes field and select the <b>azure iot hub</b> node. Drag it onto the canvas. In the pop-up window, specify the <b>node name</b>, replace <b>&#60;device_id&#62;</b> in the <b>Topic</b> with your Device Name, and enter the <b>Hostname</b> by retrieving it from the "<b>IoT Hub</b>" resource in the Azure portal. Enter the Device Name as the <b>Device ID</b> and add the <b>SAS Key</b> (<b>Primary Key</b>) that we previously copied from the device credentials. If you need to monitor events, enable Debug mode;</figcaption></figure></div>


4) Connect the <b>generator</b> to the <b>azure iot hub</b>. Tap on the right grey circle of "<b>generator</b>" node and drag this circle to the left side of the <b>azure iot hub</b> node. Select the "<b>Success</b>" link and click "<b>Add</b>". <b>Save</b> the rule chain, and go to the integration;


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/azure-event-hub/test-azure-event-hub-integration-3-pe.webp" alt="Connect the generator to the azure iot hub. Tap on the right grey circle of &quot;generator&quot; node and drag this circle to the left side of the azure iot hub node. Select the &quot;Success&quot; link and click &quot;Add&quot;. Save the rule chain, and go to the integration;" loading="lazy"><figcaption>Connect the <b>generator</b> to the <b>azure iot hub</b>. Tap on the right grey circle of "<b>generator</b>" node and drag this circle to the left side of the <b>azure iot hub</b> node. Select the "<b>Success</b>" link and click "<b>Add</b>". <b>Save</b> the rule chain, and go to the integration;</figcaption></figure></div>


Go to the "<b>Integrations</b>" page and select your <b>Azure Event Hub integration</b>. If you see a message of type "Uplink" in the "Events" section of your integration, everything is working correctly.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/azure-event-hub/test-azure-event-hub-integration-4-pe.webp" alt="Go to the &quot;Integrations&quot; page and select your Azure Event Hub integration. If you see a message of type &quot;Uplink&quot; in the &quot;Events&quot; section of your integration, everything is working correctly." loading="lazy"><figcaption>Go to the "<b>Integrations</b>" page and select your <b>Azure Event Hub integration</b>. If you see a message of type "Uplink" in the "Events" section of your integration, everything is working correctly.</figcaption></figure></div>


## Advanced usage: create Downlink converter

Downlink uses for send a message to device. For example information that message from device have been received.

1) At first, lets find **IoT Hub name**:

- Open the [Azure portal](https://portal.azure.com/) and navigate to the "**IoT Hub**" resource;
- Go to the "**Built-in endpoints**" page from the context menu;
- Find and copy the value of "**Event Hub-compatible name**" — this represents the **IoT Hub name**.
 


<div class="st-gallery"><figure><img src="/images/azure-event-hub/event_hub_compatible_name.webp" alt="Open the Azure portal and navigate to the &quot;IoT Hub&quot; resource. Go to the &quot;Built-in endpoints&quot; page from the context menu. Find and copy the value of &quot;Event Hub-compatible name&quot; — this represents the IoT Hub name." loading="lazy"><figcaption>Open the Azure portal and navigate to the "IoT Hub" resource. Go to the "Built-in endpoints" page from the context menu. Find and copy the value of "Event Hub-compatible name" — this represents the IoT Hub name.</figcaption></figure></div>


<br>
2) To add the Downlink data converter to the Azure Event Hub integration, follow these steps:

- Navigate to the "**Integrations**" page, select the **Azure Event Hub** integration to open its details, and click the "**pencil**" icon to enter editing mode;
- Provide a name for the downlink data converter and click "**Create new converter**";
- Paste the required script into the **Encoder function** section. Click "Add";
- In the **advanced settings**, add the "**IoT Hub name**" in the corresponding field;
- Click "**Apply changes**" to save the configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/azure-event-hub/adding-azure-event-hub-downlink-converter-1-pe.webp" alt="Navigate to the &quot;Integrations&quot; page, select the Azure Event Hub integration to open its details, and click the &quot;pencil&quot; icon to enter editing mode;" loading="lazy"><figcaption>Navigate to the "Integrations" page, select the Azure Event Hub integration to open its details, and click the "pencil" icon to enter editing mode;</figcaption></figure><figure><img src="/images/user-guide/integrations/azure-event-hub/adding-azure-event-hub-downlink-converter-2-pe.webp" alt="Provide a name for the downlink data converter and click &quot;Create new converter&quot;;" loading="lazy"><figcaption>Provide a name for the downlink data converter and click "Create new converter";</figcaption></figure><figure><img src="/images/user-guide/integrations/azure-event-hub/adding-azure-event-hub-downlink-converter-3-pe.webp" alt="Paste the required script into the Encoder function section. Click &quot;Add&quot;;" loading="lazy"><figcaption>Paste the required script into the Encoder function section. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/integrations/azure-event-hub/adding-azure-event-hub-downlink-converter-4-pe.webp" alt="In the advanced settings, add the &quot;IoT Hub name&quot; in the corresponding field. Click &quot;Apply changes&quot; to save the configuration." loading="lazy"><figcaption>In the advanced settings, add the "IoT Hub name" in the corresponding field. Click "Apply changes" to save the configuration.</figcaption></figure></div>


The Downlink converter used in this example:

```javascript
var result = {

    contentType: "JSON",

    data: JSON.stringify(msg),

    metadata: {
            deviceId: 'ST-D-01'
    }

};

return result;
```


<div class="st-callout info">


**NOTE** If you used another name of device (not ST-D-01) you have to specify in the Downlink converter your device name for **deviceId** field.


</div>


**Ok, downlink converter ready, integration ready, Let's test it:**

1) After test of uplink, integration have created the device inside SENTIENT, and we need to know for which Rule Chain it connected.
Just go to the Device groups in SENTIENT menu choose **All** and find the device with the name that we have used in the uplink.


<div class="st-gallery"><figure><img src="/images/azure-event-hub/device_groups_all_device profile.png" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/azure-event-hub/device_profiles_rule_chain.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


2) Find the name of necessary rule chain in "Rule Chains" pages of SENTIENT menu. 

3) In the "Search nodes" field type 'down' and choose in the menu **integration downlink** node, drag it to the canvas. In pop-up you need to specify the name of rule node and choose our integration.

4) Click on left gray circle of **message type switch** node and drag it to gray circle of our "downlink" node. Here choose **Attributes update** and click "Add".


<div class="st-gallery"><figure><img src="/images/azure-event-hub/add_rule_node_integration_downlink.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/azure-event-hub/rule_chain_attributes_updated_and_downlink.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


5) Great. Save Canvas and let's go to "Device groups" -> "All" and choose our device. Switch to **Attributes** in 'Entity attributes scope' list choose **Shared attributes**. 
   Tap on 'plus' to create new. Specify in pop-up the key of attribute, type of value and some value.

6) Tap "Add" and go to the Integration to check the result of downlink.


<div class="st-gallery"><figure><img src="/images/azure-event-hub/add_shared_attributes.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/azure-event-hub/integrations_events_downlink.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


How you can see, we have a message that Downlink successfully received by Integration and sent to Azure Event Hub.
To check it in Azure IoT Hub we need to go to Azure Portal, choose **IoT devices** menu tab and see **Cloud to Device Message Count** number. 


<div class="st-gallery"><figure><img src="/images/azure-event-hub/azure_cloud_to_device_message_count.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Advanced usage: Check Downlink using Azure IoT Hub integration

There is a simple explanation how to see your downlinks in Azure IoT Hub Integration.
Just look this images to understand how we make simple downlink check for Azure Event Hub


<div class="st-gallery"><figure><img src="/images/azure-event-hub/iot_integration_first.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/azure-event-hub/iot_integration_second.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/azure-event-hub/uplink_received.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/azure-event-hub/uplink_message.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


You can familiarize with Azure Iot Hub using next Link: [Azure IoT Hub Integration](/docs/user-guide/integrations/azure-iot-hub).

## Conclusion

That's it! Good luck in configuring of you IoT devices and dashboards!

## Next steps
