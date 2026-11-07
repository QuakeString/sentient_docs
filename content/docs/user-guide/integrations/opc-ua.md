+++
title = "OPC-UA Integration"
description = "OPC-UA Integration Guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/opc-ua.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

OPC UA Integration allows you to stream data from the OPC UA server to SENTIENT and converts the device payloads to the SENTIENT format.

<object width="100%" style="max-width: max-content;" data="/images/user-guide/integrations/opc-ua-integration.svg"></object>

## OPC-UA integration tutorial

In this tutorial, we will configure the integration between SENTIENT and OPC-UA to get the Airconditioners data from the [OPC UA C++ Demo Server](https://www.unified-automation.com/downloads/opc-ua-servers.html) and allow the user to switch on/off any Airconditioner using the integration downlink feature.

## Prerequisites

- Download and install the [OPC UA C++ Demo Server](https://www.unified-automation.com/downloads/opc-ua-servers.html).
> **Note:** This server currently supports Windows only.

- **Launch the UA Admin Dialog** after installation.
- Make sure the **hostname/IP address** and **port** are configured correctly.   
You&#39;ll need these details to set up the OPC-UA integration in SENTIENT.

![image](/images/user-guide/integrations/opc-ua/opc-ua-server-config.webp)

- **Launch the UaCPPServer**.   
A console window will appear displaying the server&#39;s endpoint URLs

![image](/images/user-guide/integrations/opc-ua/opc-ua-server-config-2.webp)

## SENTIENT setup

### Uplink data converter

First, we need to create the Uplink Data converter that will be used for receiving the messages from the OPC UA server. The converter should transform the incoming payload into the required message format.
The message must contain the *deviceName* and *deviceType*. These fields are used to submit the data to the correct device. If a device cannot not be found, a new device will be created.
Here is how the payload from the OPC UA integration will look like:

Payload:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
    </span><span class="nl">"temperature"</span><span class="p">:</span><span class="w"> </span><span class="s2">"72.15819999999641"</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

Metadata:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
    </span><span class="nl">"opcUaNode_namespaceIndex"</span><span class="p">:</span><span class="w"> </span><span class="s2">"3"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"opcUaNode_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"AirConditioner_1"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"integrationName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"OPC-UA Airconditioners"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"opcUaNode_identifier"</span><span class="p">:</span><span class="w"> </span><span class="s2">"AirConditioner_1"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"opcUaNode_fqn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Objects.BuildingAutomation.AirConditioner_1"</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

We will take the *opcUaNode_name* metadata value and map it to the *deviceName* and set the *deviceType* as *airconditioner*.

However, you can use another mapping in your specific use cases.

Also, we will retrieve the values of the *temperature*, *humidity* and *powerConsumption* fields and use them as device telemetries.

Go to the **Data converters** page of the **"Integrations center"** section, and create a new uplink converter.
To view the events, enable Debug. In the function decoder field, specify a script to parse and transform data.

<b><font size="3">Debug mode</font></b>

Enabling debug mode allows you to track events, states, and potential errors related to the execution of integrations. This greatly simplifies development and troubleshooting.


<div class="st-callout info">


**Note:** Debug mode can quickly increase disk usage because all debug events are stored in the database.
Starting from **SENTIENT 3.9**, the platform stores the full set of debug events only during the first **15 minutes** after the integrations is created; afterward, only error events are retained.


</div>


Debug mode settings can be combined or disabled entirely.

> One can use either [TBEL](/docs/user-guide/rhai/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/rhai/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

Use this function:

```ruby
var data = decodeToJson(payload);
var deviceName = metadata['opcUaNode_name'];
var namespaceIndex = metadata['opcUaNode_namespaceIndex'];
var deviceType = 'airconditioner';

var result = {
   deviceName: deviceName,
   deviceType: deviceType,
   telemetry: {
   },
   attributes: {
       namespaceIndex: namespaceIndex
   }
};

if (data.temperature != null) {
    result.telemetry.temperature = toFixed(data.temperature, 2);
}

if (data.humidity != null) {
   result.telemetry.humidity = toFixed(data.humidity, 2);
}

if (data.powerConsumption != null) {
   result.telemetry.powerConsumption = toFixed(data.powerConsumption, 2);
}

if (data.state != null) {
   result.attributes.state = data.state == '1' ? true : false;
}

/** Helper functions 'decodeToString' and 'decodeToJson' are already built-in **/

return result;
```


![image](/images/user-guide/integrations/opc-ua/opc-ua-uplink-converter-tbel.webp)

</div>

<div class="st-tab" data-label="JavaScript">

Use this function:

```ruby
var data = decodeToJson(payload);
var deviceName = metadata['opcUaNode_name'];
var deviceType = 'airconditioner';

var result = {
   deviceName: deviceName,
   deviceType: deviceType,
   telemetry: {
   },
   attributes: {
   }
};

if (data.temperature) {
    result.telemetry.temperature = Number(Number(data.temperature).toFixed(2));
}

if (data.humidity) {
    result.telemetry.humidity = Number(Number(data.humidity).toFixed(2));
}

if (data.powerConsumption) {
    result.telemetry.powerConsumption = Number(Number(data.powerConsumption).toFixed(2));
}

if (data.state !== undefined) {
    result.attributes.state = data.state === '1' ? true : false;
}

function decodeToString(payload) {
   return String.fromCharCode.apply(String, payload);
}

function decodeToJson(payload) {
   var str = decodeToString(payload);
   var data = JSON.parse(str);
   return data;
}

return result;
```


![image](/images/user-guide/integrations/opc-ua/opc-ua-uplink-converter-java.webp)

</div>

</div>


### Downlink data converter

For sending Downlink messages from the Sentient to the OPC UA node, we need to define a
downlink Converter.

In general, the output from a Downlink converter should have the following structure:

<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">[{</span><span class="w">
    </span><span class="nl">"contentType"</span><span class="p">:</span><span class="w"> </span><span class="s2">"JSON"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"{</span><span class="se">\"</span><span class="s2">writeValues</span><span class="se">\"</span><span class="s2">:[],</span><span class="se">\"</span><span class="s2">callMethods</span><span class="se">\"</span><span class="s2">:[{</span><span class="se">\"</span><span class="s2">objectId</span><span class="se">\"</span><span class="s2">:</span><span class="se">\"</span><span class="s2">ns=3;s=AirConditioner_1</span><span class="se">\"</span><span class="s2">,</span><span class="se">\"</span><span class="s2">methodId</span><span class="se">\"</span><span class="s2">:</span><span class="se">\"</span><span class="s2">ns=3;s=AirConditioner_1.Stop</span><span class="se">\"</span><span class="s2">,</span><span class="se">\"</span><span class="s2">args</span><span class="se">\"</span><span class="s2">:[]}]}"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"metadata"</span><span class="p">:</span><span class="w"> </span><span class="p">{}</span><span class="w">
</span><span class="p">}]</span></code></pre></figure>

- *contentType* - defines how data will be encoded {TEXT \| JSON \| BINARY}. In case of OPC UA Integration, JSON is used by default.
- *data* - the actual data that will be processed by OPC UA Integration and sent to the target OPC UA nodes:
    - *writeValues* - array of write values methods:
        - *nodeId* - target node in [OPC UA NodeId format](https://documentation.unified-automation.com/uasdkhp/1.4.1/html/_l2_ua_node_ids.html) (`ns=<namespaceIndex>;<identifiertype>=<identifier>`)
        - *value* - value to write
    - *callMethods* - array of call methods:
        - *objectId* - target object in [OPC UA NodeId format](https://documentation.unified-automation.com/uasdkhp/1.4.1/html/_l2_ua_node_ids.html)
        - *methodId* - target method in [OPC UA NodeId format](https://documentation.unified-automation.com/uasdkhp/1.4.1/html/_l2_ua_node_ids.html)
        - *args* - array of method input values
- *metadata* - not used in case of OPC UA Integration and can be empty.

<br>
Go to the **Integrations center** section -> **Data converters** page and create a new downlink converter.

> One can use either [TBEL](/docs/user-guide/rhai/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/rhai/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="st-tabs">

<div class="st-tab" data-label="TBELRecommended">

Use this function:

```ruby
var data = {
    writeValues: [],
    callMethods: []
};

if (msgType === 'RPC_CALL_FROM_SERVER_TO_DEVICE') {
    if (msg.method === 'setState') {
        var targetMethod = msg.params === 'true' ? 'Start' : 'Stop';
        var writeValue = {
              nodeId: 'ns=' + metadata['cs_namespaceIndex'] +';s=' + metadata['deviceName'],
              value: msg.params
        };
        data.writeValues.push(writeValue);
        var callMethod = {
              objectId: 'ns=' + metadata['cs_namespaceIndex'] +';s=' + metadata['deviceName'],
              methodId: 'ns=' + metadata['cs_namespaceIndex'] +';s=' + metadata['deviceName']+'.'+targetMethod,
              args: []
        };
        data.callMethods.push(callMethod);
    }
}

var result = {
    contentType: "JSON",
    data: JSON.stringify(data),
    metadata: {}
};

return result;
```


![image](/images/user-guide/integrations/opc-ua/opc-ua-downlink-converter-tbel.webp)

</div>

<div class="st-tab" data-label="JavaScript">

Use this function:

```ruby
var data = {
    writeValues: [],
    callMethods: []
};

if (msgType === 'RPC_CALL_FROM_SERVER_TO_DEVICE') {
    if (msg.method === 'setState') {
        var targetMethod = msg.params === 'true' ? 'Start' : 'Stop';
        var writeValue = {
              nodeId: 'ns=' + metadata['cs_namespaceIndex'] +';s=' + metadata['deviceName'],
              value: msg.params
        };
        data.writeValues.push(writeValue);
        var callMethod = {
              objectId: 'ns=' + metadata['cs_namespaceIndex'] +';s=' + metadata['deviceName'],
              methodId: 'ns=' + metadata['cs_namespaceIndex'] +';s=' + metadata['deviceName']+'.'+targetMethod,
              args: []
        };
        data.callMethods.push(callMethod);
    }
}

var result = {
    contentType: "JSON",
    data: JSON.stringify(data),
    metadata: {}
};

return result;
```


![image](/images/user-guide/integrations/opc-ua/opc-ua-downlink-converter-java.webp)

</div>

</div>


This converter will process the RPC command to the device using the method *setState*
and a boolean *params* value to call the 'Start' or 'Stop' method of the airconditioner.

Destination node is detected using the *deviceName* field of the incoming message metadata.

### OPC-UA integration

 - Open the "**Integrations center**" section -> "**Integrations**" page and click `+` icon to create new integration.
 - From the list of available types, select "**OPC-UA**" as the integration type.

![image](/images/user-guide/integrations/opc-ua/opc-ua-create-integration-1.webp)

 - The next steps is to add the recently created uplink and downlink converters.

![image](/images/user-guide/integrations/opc-ua/opc-ua-create-integration-2.webp)

![image](/images/user-guide/integrations/opc-ua/opc-ua-create-integration-3.webp)

- Specify host: **hostname/IP** (see [Prerequisites](#prerequisites));
- Specify port: **port** (see [Prerequisites](#prerequisites));
- Security: **None** (can be *Basic128Rsa15* / *Basic256* / *Basic256Sha256* / *None*);
- Identity: **Anonymous** (can be *Anonymous* / *Username*).

![image](/images/user-guide/integrations/opc-ua/opc-ua-create-integration-4.webp)

- Mapping:
     - MappingType: **Fully Qualified Name** (can be *Fully Qualified Name* / *ID*);
     - Specify Device Node Pattern: **Objects\\.BuildingAutomation\\.AirConditioner_\d+$** 
  
  (regular expression used to match scanned OPC UA Node FQNs/IDs to device name. 
  In this sample, path on OPC UA Explorer is `Objects\.BuildingAutomation\.AirConditioner_X`, where X is a number from 1 to N. 
  That's why we use `Objects\.BuildingAutomation\.AirConditioner_\d+$` as regular expression, because `\d+` means any number from 1 to *N*, and `$` means the end of the string);
     - Subscription tags (list of node tags (**Path**) to subscribe with mappings to keys (**Key**) used in the output message):
        - *state* - State;
        - *temperature* - Temperature;
        - *humidity* - Humidity;
        - *powerConsumption* - PowerConsumption.
- Click "**Add**".

![image](/images/user-guide/integrations/opc-ua/opc-ua-create-integration-5.webp)

The OPC-UA integration has been added. 

The [OPC-UA server](#prerequisites) simulates sending telemetry from devices to SENTIENT. If you have done everything correctly, 10 new devices should appear on the "**Devices**" page as a result of the integration. Please make sure of this.

![image](/images/user-guide/integrations/opc-ua/opc-ua-devices-1.webp)

Open the details of any airconditioner and navigate to the "**Latest telemetry**" tab.
You will see that telemetry values are frequently updated.

![image](/images/user-guide/integrations/opc-ua/opc-ua-devices-2.webp)

### Airconditioners Rule Chain

To demonstrate OPC-UA integration and Rule Engine capabilities, we will create a separate rule chain to process the uplink and downlink messages related to the OPC-UA integration.

Let's create the **Airconditioners** rule chain.

 - Download the [airconditioners.json](/docs/user-guide/resources/airconditioners.json) file;
 - Go to the "**Rule Chains**" page. To import this JSON file, click the `+` icon in the upper right corner of the screen and select "**Import rule chain**";
 - Drag and drop downloaded JSON file to the **Import rule chain** window. Click "**Import**";
 - The "**Airconditioners**" rule chain will open. Double-click on the "**integration downlink**" node and specify **OPC-UA Integration** in the integration field;
 - Apply all changes.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/opc-ua/opc-ua-rule-chain-1.webp" alt="Download the airconditioners.json file. Go to the &quot;Rule Chains&quot; page. To import this JSON file, click the &quot;+&quot; icon in the upper right corner of the screen and select the &quot;Import rule chain&quot;;" loading="lazy"><figcaption>Download the airconditioners.json file. Go to the "Rule Chains" page. To import this JSON file, click the "+" icon in the upper right corner of the screen and select the "Import rule chain";</figcaption></figure><figure><img src="/images/user-guide/integrations/opc-ua/opc-ua-rule-chain-2.webp" alt="Double-click on the &quot;integration downlink&quot; node;" loading="lazy"><figcaption>Double-click on the "integration downlink" node;</figcaption></figure><figure><img src="/images/user-guide/integrations/opc-ua/opc-ua-rule-chain-3.webp" alt="Specify &quot;OPC-UA Integration&quot; in the integration field;" loading="lazy"><figcaption>Specify "OPC-UA Integration" in the integration field;</figcaption></figure><figure><img src="/images/user-guide/integrations/opc-ua/opc-ua-rule-chain-4.webp" alt="Apply all changes." loading="lazy"><figcaption>Apply all changes.</figcaption></figure></div>


 - Open and edit the **Root Rule Chain**;
 - Find a **rule chain** node, drag and drop it to the rule chain. Name it Airconditioners, specify **Airconditioners** rule chain and click "**Add**";
 - Tap on a right grey circle of "**message type switch**" node and drag this circle to left side of "**rule chain**" node. Here, select "**Attributes Updated**", "**Post telemetry**", and "**RPC Request to Device**";
 - Click "**Add**" and save rule chain.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/opc-ua/opc-ua-rule-chain-5.webp" alt="Open the &quot;Root Rule Chain&quot;;" loading="lazy"><figcaption>Open the "Root Rule Chain";</figcaption></figure><figure><img src="/images/user-guide/integrations/opc-ua/opc-ua-rule-chain-7.webp" alt="Add a &quot;rule chain&quot; node. Name it &quot;Airconditioners&quot;, choose our &quot;Airconditioners&quot; rule chain and click &quot;Add&quot;;" loading="lazy"><figcaption>Add a "rule chain" node. Name it "Airconditioners", choose our "Airconditioners" rule chain and click "Add";</figcaption></figure><figure><img src="/images/user-guide/integrations/opc-ua/opc-ua-rule-chain-8.webp" alt="Tap on a right grey circle of &quot;message type switch&quot; node and drag this circle to left side of &quot;rule chain&quot; node. Here, select &quot;Attributes Updated&quot;, &quot;Post telemetry&quot; and &quot;RPC Request to Device&quot;. Then tap &quot;Add&quot; and save rule chain." loading="lazy"><figcaption>Tap on a right grey circle of "message type switch" node and drag this circle to left side of "rule chain" node. Here, select "Attributes Updated", "Post telemetry" and "RPC Request to Device". Then tap "Add" and save rule chain.</figcaption></figure></div>


### Airconditioners dashboard

To visualize the Airconditioners data and test RPC commands, we will create the **Airconditioners** dashboard.

- Download the [airconditioners_dashboard.json](/docs/user-guide/resources/airconditioners_dashboard.json) file;
- Go to the "**Dashboards**" page;
- To import this JSON file, click the `+` icon in the upper right corner of the screen and select "**Import dashboard**";
- Drag and drop downloaded JSON file to the **Import dashboard** window. Click "Import".

![image](/images/user-guide/integrations/opc-ua/opc-ua-dashboard-1.webp)

 - Open the **Airconditioners** dashboard;
 - You will see the telemetry till the last minute from all the 10 airconditioners;
 - Open any Airconditioner details page by clicking on the details button in the Entities widget;

![image](/images/user-guide/integrations/opc-ua/opc-ua-dashboard-2.webp)

 - You will find the Airconditioner status light green. Try to switch off the airconditioner by clicking on the **On/Off Round switch**;

![image](/images/user-guide/integrations/opc-ua/opc-ua-dashboard-4.webp)

 - The Airconditioner status light will turn into grey, the temperature will start rising, the humidity will start increasing and the power consumption will stop.

![image](/images/user-guide/integrations/opc-ua/opc-ua-dashboard-5.webp)

## Video tutorial

See video tutorial below for step-by-step instruction how to setup OPC-UA Integration.

<br>
<div id="video">  
    <div id="video_wrapper">
        <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/KK0gXGXFQ0E" frameborder="0" allowfullscreen></iframe>
    </div>
</div> 

<br>

## See also

- [Integration Overview](/docs/user-guide/integrations/)
- [Uplink Converters](/docs/user-guide/integrations/#uplink-data-converter)
- [DownLink Converters](/docs/user-guide/integrations/#downlink-data-converter)
- [Rule Engine](/docs/user-guide/rule-engine-2-0/re-getting-started/)

  
## Next steps
