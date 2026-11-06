+++
title = "The Things Stack Industries integration"
description = "The Things Stack Industries integration guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/tti.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only [**Professional Edition**](/products/sentient-pe/) supports **Platform Integrations** feature.<br>
Use [**SENTIENT Cloud**](/installations/choose-region/) or [**install**](/docs/user-guide/install/pe/installation-options/) your own platform instance.


</div>

## Overview
TheThingsIndustries is LoRaWAN network designed for connecting your devices using LoRaWAN stack. 
After integrating TheThingsIndustries with the SENTIENT, you can connect, communicate, process and visualize data from devices in the SENTIENT IoT platform.


## The Things Stack

### Register Application
The first step is to create an **application** in TheThingsIndustries console. Go to console by , open 
**Applications** section, press **add application** button and fill required fields.

- **Application ID** - sentient-integration

![image](/images/user-guide/integrations/tti/tti-create-app.webp)


### Payload Decoder
Our device submits data in binary format. We have 2 options where to decode this data:

- **TheThingsIndustries decoder** - data will be decoded before entering the SENTIENT
- **SENTIENT converters** - uplink/downlink converters will be used to decode data from binary format into JSON

In this tutorial, we will make an initial transformation into JSON with TTI decoder and then use SENTIENT converters for correct data processing.
In real life scenario, it is up to you where to decode/encode data, because it is possible to do this on any side.

After application registered in TTI, go to **Payload formatters**, **Uplink** select decoder function. We will take the first byte as a temperature value from a device 
and transform it into JSON.

Decode Function <figure class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">function</span> <span class="nx">Decoder</span><span class="p">(</span><span class="nx">bytes</span><span class="p">,</span> <span class="nx">port</span><span class="p">)</span> <span class="p">{</span>
  <span class="kd">var</span> <span class="nx">decoded</span> <span class="o">=</span> <span class="p">{</span><span class="na">temperature</span><span class="p">:</span> <span class="nx">bytes</span><span class="p">[</span><span class="mi">0</span><span class="p">]};</span>
  <span class="k">return</span> <span class="nx">decoded</span><span class="p">;</span>
<span class="p">}</span></code></pre></figure>
 
Output json:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
  </span><span class="nl">"temperature"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

![image](/images/user-guide/integrations/tti/tti-create-decoder.webp)

Press **Save payload function**

### Device Registration in TheThingsIndustries

Next step is a Device creation in the TTI. Open **End devices** page and press **Add end device**

- Device ID - thermostat1.
- DevEUI - unique device identifier.
- Press **Network layer settings** button.

![image](/images/user-guide/integrations/tti/tti-create-device-1.webp)

- Select configuration for your device.

![image](/images/user-guide/integrations/tti/tti-create-device-2.webp)

- Press **Application layer settings** button.

Fill the **AppSKey** by generation button.

Press **Add end device** button.

## Integration with the SENTIENT

We need to create Integration on The Things Industries, to do this open **Integrations** - **MQTT** and press **Generate new API key**. 
Copy username and password we will need it later.

![image](/images/user-guide/integrations/tti/tti-integration.webp)

Now we can start configuring the SENTIENT.

### SENTIENT Uplink Data Converter

First, we need to create Uplink Data converter that will be used for receiving messaged from the TTI. The converter should transform incoming payload into the required message format.
Message must contains **deviceName** and **deviceType**. Those fields are used for submitting data to the correct device. If a device was not found then new device will be created.
Here is how payload from TheThingsIndustries will look like:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
  </span><span class="nl">"end_device_ids"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"device_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"thermostat1"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"application_ids"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"application_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"sentient-integration"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="nl">"dev_eui"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ABABABABABABABAA"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"join_eui"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0000000000000000"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"dev_addr"</span><span class="p">:</span><span class="w"> </span><span class="s2">"270000BC"</span><span class="w">
  </span><span class="p">},</span><span class="w">
  </span><span class="nl">"correlation_ids"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="s2">"as:up:01EFEBYDTA1X51TDGPKC1EYK6N"</span><span class="p">,</span><span class="w">
    </span><span class="s2">"gs:conn:01ED482WRPY2BABY4TYZV57RJG"</span><span class="p">,</span><span class="w">
    </span><span class="s2">"gs:uplink:01ED9B93M49J8P3FQXCGGCYTGX"</span><span class="p">,</span><span class="w">
    </span><span class="s2">"ns:uplink:01ED9B93MH00CTY41A6KF674E4"</span><span class="p">,</span><span class="w">
    </span><span class="s2">"rpc:/ttn.lorawan.v3.AppAs/SimulateUplink:01EFEBYDS9BGD5A9VVZ6GSNBAV"</span><span class="p">,</span><span class="w">
    </span><span class="s2">"rpc:/ttn.lorawan.v3.GsNs/HandleUplink:01ED9B93MH293RE2TR3F1WMHEG"</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"received_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-08-11T08:59:45.869225403Z"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"uplink_message"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"session_key_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"BXGsg614fdmYH7efd+fRvA=="</span><span class="p">,</span><span class="w">
    </span><span class="nl">"f_port"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w">
    </span><span class="nl">"f_cnt"</span><span class="p">:</span><span class="w"> </span><span class="mi">23787</span><span class="p">,</span><span class="w">
    </span><span class="nl">"frm_payload"</span><span class="p">:</span><span class="w"> </span><span class="s2">"AhJF8HTI3khf"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"decoded_payload"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"temperature"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="nl">"settings"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"data_rate"</span><span class="p">:</span><span class="w"> </span><span class="p">{}</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="nl">"received_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-08-11T10:08:31.505981496Z"</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

We will take **device_id** and map it to the **deviceName** and **application_id** map to the **deviceType**. But you can use another mapping in your specific use cases.
Also, we will take the value of the **temperature** field and use it as a device telemetry. 

Go to **Data Converters** and create new **uplink** Converter with this function: <figure class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">data</span> <span class="o">=</span> <span class="nx">decodeToJson</span><span class="p">(</span><span class="nx">payload</span><span class="p">);</span>
<span class="kd">var</span> <span class="nx">deviceName</span> <span class="o">=</span> <span class="nx">data</span><span class="p">.</span><span class="nx">end_device_ids</span><span class="p">.</span><span class="nx">device_id</span><span class="p">;</span>
<span class="kd">var</span> <span class="nx">deviceType</span> <span class="o">=</span> <span class="nx">data</span><span class="p">.</span><span class="nx">end_device_ids</span><span class="p">.</span><span class="nx">application_ids</span><span class="p">.</span><span class="nx">application_id</span><span class="p">;</span>

<span class="kd">var</span> <span class="nx">result</span> <span class="o">=</span> <span class="p">{</span>
    <span class="na">deviceName</span><span class="p">:</span> <span class="nx">deviceName</span><span class="p">,</span>
    <span class="na">deviceType</span><span class="p">:</span> <span class="nx">deviceType</span><span class="p">,</span>
    <span class="na">telemetry</span><span class="p">:</span> <span class="p">{</span>
         <span class="na">temperature</span><span class="p">:</span> <span class="nx">data</span><span class="p">.</span><span class="nx">uplink_message</span><span class="p">.</span><span class="nx">decoded_payload</span><span class="p">.</span><span class="nx">temperature</span>
    <span class="p">}</span>
<span class="p">};</span>

<span class="kd">function</span> <span class="nx">decodeToString</span><span class="p">(</span><span class="nx">payload</span><span class="p">)</span> <span class="p">{</span>
    <span class="k">return</span> <span class="nb">String</span><span class="p">.</span><span class="nx">fromCharCode</span><span class="p">.</span><span class="nx">apply</span><span class="p">(</span><span class="nb">String</span><span class="p">,</span> <span class="nx">payload</span><span class="p">);</span>
<span class="p">}</span>

<span class="kd">function</span> <span class="nx">decodeToJson</span><span class="p">(</span><span class="nx">payload</span><span class="p">)</span> <span class="p">{</span>
    <span class="kd">var</span> <span class="nx">str</span> <span class="o">=</span> <span class="nx">decodeToString</span><span class="p">(</span><span class="nx">payload</span><span class="p">);</span>
    <span class="kd">var</span> <span class="nx">data</span> <span class="o">=</span> <span class="nx">JSON</span><span class="p">.</span><span class="nx">parse</span><span class="p">(</span><span class="nx">str</span><span class="p">);</span>
    <span class="k">return</span> <span class="nx">data</span><span class="p">;</span>
<span class="p">}</span>

<span class="k">return</span> <span class="nx">result</span><span class="p">;</span></code></pre></figure>

![image](/images/user-guide/integrations/tti/tb-uplink.webp)


### SENTIENT Downlink Data Converter
For sending Downlink messages from the SENTIENT to the device inside TTI, we need to define downlink Converter.
In general, output from Downlink converter should have the following structure:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
  </span><span class="nl">"downlinks"</span><span class="p">:</span><span class="w"> </span><span class="p">[{</span><span class="w">
    </span><span class="nl">"f_port"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w">
    </span><span class="nl">"frm_payload"</span><span class="p">:</span><span class="w"> </span><span class="s2">"vu8="</span><span class="p">,</span><span class="w">
    </span><span class="nl">"priority"</span><span class="p">:</span><span class="w"> </span><span class="s2">"NORMAL"</span><span class="w">
  </span><span class="p">}]</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

- **contentType** - defines how data will be encoded {TEXT \| JSON \| BINARY}
- **data** - actual data that will be sent to the device in TTI. More details about API can be found in this [TTI API](https://enterprise.thethingsstack.io/integrations/mqtt/)
- **metadata** - in this object you should place correct **devId** (device id) value that will be used to identify target device in TTI

Go to **Data Converters** and create new **downlink** Converter with this function: <figure class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">data</span> <span class="o">=</span> <span class="p">{</span>
        <span class="na">downlinks</span><span class="p">:</span> <span class="p">[{</span>
            <span class="na">f_port</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
            <span class="na">confirmed</span><span class="p">:</span> <span class="kc">false</span><span class="p">,</span>
            <span class="na">frm_payload</span><span class="p">:</span> <span class="nx">btoa</span><span class="p">(</span><span class="nx">msg</span><span class="p">.</span><span class="nx">version</span><span class="p">),</span>
            <span class="na">priority</span><span class="p">:</span> <span class="dl">"</span><span class="s2">NORMAL</span><span class="dl">"</span>
        <span class="p">}]</span>
    <span class="p">};</span>

<span class="kd">var</span> <span class="nx">result</span> <span class="o">=</span> <span class="p">{</span>
    <span class="na">contentType</span><span class="p">:</span> <span class="dl">"</span><span class="s2">JSON</span><span class="dl">"</span><span class="p">,</span>
    <span class="na">data</span><span class="p">:</span> <span class="nx">JSON</span><span class="p">.</span><span class="nx">stringify</span><span class="p">(</span><span class="nx">data</span><span class="p">),</span>
    <span class="na">metadata</span><span class="p">:</span> <span class="p">{</span>
        <span class="na">devId</span><span class="p">:</span> <span class="dl">'</span><span class="s1">thermostat1</span><span class="dl">'</span>
    <span class="p">}</span>

<span class="p">};</span>
<span class="k">return</span> <span class="nx">result</span><span class="p">;</span></code></pre></figure>

This converter will take **version** field from the incoming message and add it is a payload field in the outbound message. Destination device is a **thermostat1** device.

![image](/images/user-guide/integrations/tti/tb-downlink.webp)

### TTI Integration

Next we will create Integration with TheThingsIndustries inside the SENTIENT. Open **Integrations** section and add new Integration with type
**TheThingsIndustries**

- **Name**: *TTI Integration*
- **Type**: *TheThingsIndustries*
- **Uplink** data converter: *TTI Uplink*
- **Downlink** data converter: *TTI Downlink*
- **Region**: *eu1* (region where your application was registered inside TTI)
- **Username**: *sentient-integration@sentient* (use ***Username*** from TTI integration)
- **Password**: use ***Password*** from TTI integration

![image](/images/user-guide/integrations/tti/tb-integration-1.webp)  

![image](/images/user-guide/integrations/tti/tb-integration-2.webp)  

## Validation

### Validate Uplink Messages
Lets verify our integration. 

When device sends data, we can check it in the SENTIENT, to do this:

Go to **Device Group** -> **All** -> **thermostat1** - you can see that 

- new device was registered in the Sentient with name "thermostat1"
- In the **Latest Telemetry** section you will see that last submitted temperature = 2.

![image](/images/user-guide/integrations/tti/tb-device-telemetry.webp)

### Validate Downlink Messages
For testing Downlink Messages, we will update our Root Rule Chain to send downlink message when device attribute is changed.
Open and edit **Root Rule Chain**. Add **Integration Downlink** Action node and connect it with the **Message Type Switch** Node using relation 
**Attributes Updated**
 
![image](/images/user-guide/integrations/tti/tb-add-rule-downlink.webp)

![image](/images/user-guide/integrations/tti/tb-route-to-downlink.webp)

Save Changes.

Go to **Device Group** -> **All** -> **thermostat1** -> attributes section. We will add **Shared attribute** with name **version** and
value **v.0.11** 

![image](/images/user-guide/integrations/tti/tb-add-version.webp)

By making this step, we triggered downlink message to the device **thermostat1** and this message should contains version field value.  
Open TTI Console, navigate to **sentient-integration** application, to the section **Data**.  
And we see that Downlink message was received (It is displayed as bytes **76 2E 30 2E 31 31**).  

![image](/images/user-guide/integrations/tti/ttn-downlink-verified.webp)

## See also
With this integration you can also configure Downlink converters and trigger required actions using Rule Engine nodes.

- [Integration Overview](/docs/user-guide/integrations/)
- [Uplink Converters](/docs/user-guide/integrations/#uplink-data-converter)
- [Downlink Converters](/docs/user-guide/integrations/#downlink-data-converter)
- [Rule Engine](/docs/pe/user-guide/rule-engine-2-0/re-getting-started/)


## Next steps
