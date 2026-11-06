+++
title = "Abeeway Micro Tracker and Abeeway Industrial Tracker telemetry upload"
description = "Abeeway Micro Tracker and Abeeway Industrial Tracker upload"

[extra]
status = "imported"
checked = ""
source = "docs/samples/abeeway/tracker.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only [**Professional Edition**](/products/sentient-pe/) supports **Platform Integrations** feature.<br>
Use [**SENTIENT Cloud**](/installations/choose-region/) or [**install**](/docs/user-guide/install/pe/installation-options/) your own platform instance.


</div>


This guide provides step-by-step instructions for connecting the Abeeway Micro Tracker and Abeeway Industrial Tracker to SENTIENT Professional Edition (PE).
The connection is through the IoT network in the new global standard LoRaWAN and ThingPark Wireless OSS intelligent logger (Actility).
In this guide, we will use the free SENTIENT Professional Edition demo server [sentient.cloud](https://sentient.cloud/signup) in this guide.
This guide will be useful to anyone who wants to connect their trackers manufactured by Abeeway or another industrial IoT application to the LoRaWAN network.

![image](/images/samples/abeeway/actility_dashboard_example.webp)

## Prerequisites

We assume:
- You are registered on the Actility [website](https://www.actility.com/).
- You have at least one Abeeway Micro Tracker or Abeeway Industrial Tracker that is already connected  with ACTILITY THINGPARK IoT NETWORK and is active.
- We also assume you already have a SENTIENT Professional Edition server or free demo account.
Otherwise, you can register for a 30-days free demo account here: [sentient.cloud](https://sentient.cloud/signup).
We expect you to have at least a basic knowledge about SENTIENT, so we do recommend to complete the [Getting Started](/docs/getting-started-guides/helloworld) guide.


## Integration overview

SENTIENT Platform Integrations feature allows to push data from various platforms and connectivity solutions to SENTIENT.
We will use platform ThingPark Wireless company Actility to consume data from LoRaWAN networks and automatically register devices in SENTIENT.
Besides configuring the integration, we will also set SENTIENT up to decode incoming data, store it in the database, visualize on the dashboard and generate alarms based on configurable thresholds.

## Step 1. Checking the registration for the platform ThingPark Wireless company Actility

- Registration and condition of devices

Few things to notice:

The <b>DevEUI</b> from the incoming message will become the Device <b>Name</b> in SENTIENT;

SENTIENT will automatically create device with type “tracker” and name equal to <b>DevEUI</b>;

Therefore, when creating a new device, in the <b>Name</b> field, enter the value <b>DevEUI</b>: from the Device Information (ThingPark Wireless OSS intelligent logger (Actility)) section

<details>
    <summary>
        <font color="#006400"><i><b>An example of a device registered to the platform ThingPark Wireless company Actility</b></i></font> (<b>click to open expanded view</b>)
    </summary>
    <ul>
        <p>
            <font color="#00008b"><b>The device must be <font color="#32cd32">active!!!</font> </b>In the example, DevUi = </font><font color="red">"20635F010800105C"</font>
        </p>
        <p>
            <font color="#00008b"><b>The device must be attached to the application.</b>In our example: to Application </font><font color="red">"NoAS21"</font>
         </p>
        <details>
             <summary>
                 <font color="#228b22"><b>Photo of the example of a device registered to the platform ThingPark Wireless company Actility</b></font>  (<b>click to open expanded view</b>)
             </summary>
            <img src="/images/samples/abeeway/actility_device.webp" alt="Actility device example">
        </details>
    </ul>
</details>

## Step 2. Creation UpLink and DownLink DATA Converters
In order to create an [Integration](/docs/user-guide/integrations), we should create the [Uplink Data Converter](/docs/user-guide/integrations/#uplink-data-converter) and the [Downlink Data Converter](/docs/user-guide/integrations/#downlink-data-converter) first. 
The converters will decode incoming telemetry payload data from global standard LoRaWAN that contains in encoded hex string to human readable, simplified SENTIENT data format.

<details>
    <summary>
        <font color="#006400"><i><b>Screenshot of how to create Uplink converter</b></i></font> (<b>click to open expanded view</b>)
    </summary>
    <img src="/images/samples/abeeway/add_uplink_decoder.webp" alt="Add uplink decoder dialog">
</details>

<details>
    <summary>
        <font color="#006400"><i><b>Screenshot of how to create Downlink converter</b></i></font> (<b>click to open expanded view</b>)
    </summary>
    <img src="/images/samples/abeeway/add_downlink_decoder.webp" alt="Add downlink decoder dialog">
</details>

## Step 3. Uplink Data Converter configuration

When creating an Uplink Converter, a default decoder is added to the Decoder section.

After creating the Uplink Converter to the Decoder section, you need to update the Decoder code to [the following code](/images/samples/abeeway/upLinkDecoder.txt).

<b>It is necessary to edit the Uplink decoder</b>


<p></p> <p></p>
<details>
    <summary>
        <font color="#006400"><i><b>Open Uplink Converter, editor mode, click "test decoder function" and replace the default code with a new code:</b></i></font> <br> (<b>click to open expanded view</b>)
    </summary>
   <ul>
        <details>
            <summary>
            <font color="#228b22"><b>Screenshot of editing the UpLink decoder</b></font> (<b>click to open expanded view</b>)
            </summary>
            <img src="/images/samples/abeeway/uplink_decoder.webp" alt="Uplink decoder properties screen">
        </details>
        <details>
            <summary>
             <font color="#228b22"><b>Input data from ThingPark Wireless OSS intelligent logger (Actility) Platform looks like this:</b></font> (<b>click to open expanded view</b>)
            </summary>
            <ul>
                <details>
                <summary>
                  <font color="#32cd32"><b>JSON: input data from ThingPark Wireless OSS intelligent logger (Actility) Platform looks like this:</b></font>  <br>(<b>click to open expanded view</b>)
                </summary>
                 <figure class="highlight"><pre><code class="language-bash" data-lang="bash">                 <span class="o">{</span>
                     <span class="s2">"DevEUI_uplink"</span>: <span class="o">{</span>
                         <span class="s2">"Time"</span>: <span class="s2">"2019-11-06T09:54:46.342+01:00"</span>,
                         <span class="s2">"DevEUI"</span>: <span class="s2">"20635F00C5000660"</span>,
                         <span class="s2">"FPort"</span>: 17,
                         <span class="s2">"FCntUp"</span>: 1796,
                         <span class="s2">"ADRbit"</span>: 1,
                         <span class="s2">"MType"</span>: 2,
                         <span class="s2">"FCntDn"</span>: 94,
                         <span class="s2">"payload_hex"</span>: <span class="s2">"0500997d3040"</span>,
                         <span class="s2">"mic_hex"</span>: <span class="s2">"304d48f9"</span>,
                         <span class="s2">"Lrcid"</span>: <span class="s2">"00000211"</span>,
                         <span class="s2">"LrrRSSI"</span>: <span class="nt">-63</span>.0,
                         <span class="s2">"LrrSNR"</span>: 7.5,
                         <span class="s2">"SpFact"</span>: 7,
                         <span class="s2">"SubBand"</span>: <span class="s2">"G1"</span>,
                         <span class="s2">"Channel"</span>: <span class="s2">"LC2"</span>,
                         <span class="s2">"DevLrrCnt"</span>: 1,
                         <span class="s2">"Lrrid"</span>: <span class="s2">"10000329"</span>,
                         <span class="s2">"Late"</span>: 0,
                         <span class="s2">"Lrrs"</span>: <span class="o">{</span>
                             <span class="s2">"Lrr"</span>: <span class="o">[{</span>
                                 <span class="s2">"Lrrid"</span>: <span class="s2">"10000329"</span>,
                                 <span class="s2">"Chain"</span>: 0,
                                 <span class="s2">"LrrRSSI"</span>: <span class="nt">-63</span>.0,
                                 <span class="s2">"LrrSNR"</span>: 7.5,
                                 <span class="s2">"LrrESP"</span>: <span class="nt">-63</span>.710819
                             <span class="o">}]</span>
                         <span class="o">}</span>,
                         <span class="s2">"CustomerID"</span>: <span class="s2">"100038328"</span>,
                         <span class="s2">"CustomerData"</span>: <span class="o">{</span>
                             <span class="s2">"alr"</span>: <span class="o">{</span>
                                 <span class="s2">"pro"</span>: <span class="s2">"ABEE/APY"</span>,
                                 <span class="s2">"ver"</span>: <span class="s2">"1"</span>
                             <span class="o">}</span>
                         <span class="o">}</span>,
                         <span class="s2">"ModelCfg"</span>: <span class="s2">"0"</span>,
                         <span class="s2">"InstantPER"</span>: 0.0,
                         <span class="s2">"MeanPER"</span>: 0.001706,
                         <span class="s2">"DevAddr"</span>: <span class="s2">"05C1704A"</span>,
                         <span class="s2">"TxPower"</span>: 9.5,
                         <span class="s2">"NbTrans"</span>: 1
                     <span class="o">}</span>
                 <span class="o">}</span>
                 </code></pre></figure>
                </details>
                <details>
                 <summary>
                     <font color="#32cd32"><b>Screenshot of the input data from ThingPark Wireless OSS intelligent logger (Actility) Platform looks like this:</b></font>  <br>(<b>click to open expanded view</b>)
                 </summary>
                 <img src="/images/samples/abeeway/uplink_decoder_input.webp" alt="Uplink decoder input dialog">
                </details>
            </ul>
        </details>
        <details>
            <summary>
             <font color="#228b22"><b>Output data after decoding will look like this:</b></font> (<b>click to open expanded view</b>)
            </summary>
            <ul>
                <details>
                    <summary>
                    <font color="#32cd32"><b>JSON: output data from ThingPark Wireless OSS intelligent logger (Actility) Platform looks like this:</b></font>  <br>(<b>click to open expanded view</b>)
                    </summary>
                    <figure class="highlight"><pre><code class="language-bash" data-lang="bash">                    <span class="o">{</span>
                     <span class="s2">"deviceName"</span>: <span class="s2">"20635F00C5000660"</span>,
                     <span class="s2">"deviceType"</span>: <span class="s2">"Abeeway Micro/Industrial Tracker"</span>,
                     <span class="s2">"telemetry"</span>: <span class="o">{</span>
                         <span class="s2">"ts"</span>: 1573030486342,
                         <span class="s2">"values"</span>: <span class="o">{</span>
                             <span class="s2">"batteryVoltage"</span>: 8.388,
                             <span class="s2">"temperature"</span>: 18.5,
                             <span class="s2">"ph_type"</span>: <span class="s2">"Heartbeat message"</span>,
                             <span class="s2">"ph_status"</span>: <span class="s2">"Standby"</span>,
                             <span class="s2">"ph_alert_SOS_bit4"</span>: 0,
                             <span class="s2">"ph_tracking/idle_state_bit3"</span>: 0,
                             <span class="s2">"ph_tracker_is_moving_bit2"</span>: 0,
                             <span class="s2">"ph_periodic_position_message_bit1"</span>: 0,
                             <span class="s2">"ph_POD_message_bit0"</span>: 0,
                             <span class="s2">"m_type"</span>: <span class="s2">"Unconfirmed Data Up"</span>,
                             <span class="s2">"m_port"</span>: 17,
                             <span class="s2">"m_customerID"</span>: <span class="s2">"100038328"</span>,
                             <span class="s2">"m_LrrRSSI"</span>: <span class="nt">-63</span>,
                             <span class="s2">"m_LrrSNR"</span>: 7.5,
                             <span class="s2">"m_Lrrid"</span>: <span class="s2">"10000329"</span>,
                             <span class="s2">"ack"</span>: 3
                         <span class="o">}</span>,
                         <span class="s2">"last_reset_cause"</span>: 64
                     <span class="o">}</span>
                    <span class="o">}</span>
                    </code></pre></figure>
                </details> 
                <details>
                  <summary>
                  <font color="#32cd32"><b>Screenshot: output data from ThingPark Wireless OSS intelligent logger (Actility) Platform looks like this:</b></font>  <br>(<b>click to open expanded view</b>)
                  </summary>
                  <img src="/images/samples/abeeway/uplink_decoder_output.webp" alt="Uplink decoder output dialog">
                </details>
                <details>
                    <summary>
                    <font color="#32cd32"><b>Payload_hex: example to decoder</b></font>  <br>(<b>click to open expanded view</b>)
                    </summary>
                    <b>Common message header</b>
                    <table style="width: 75%">
                    <thead>
                        <tr>
                            <td><b>Byte 0</b></td>
                            <td><b>Byte 1</b></td>
                            <td><b>Byte 2</b></td>
                            <td><b>Byte 3</b></td>
                            <td><b>Byte 4</b></td>
                            <td><b>Data Variable</b></td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Type</td>
                            <td>Status</td>
                            <td>Battery</td>
                            <td>Temperature</td>
                            <td>Ack/opt</td>
                            <td>Data</td>
                        </tr>
                     </tbody>
                    </table>
                    <i>"payload_hex": <font color="#cd5c5c"><b>"0500997d3040"</b></font></i>
                    <table style="width: 75%">
                    <thead>
                        <tr>
                            <td><b>Field</b></td>
                            <td><b>First Byte</b></td>
                            <td><b>Byte length</b></td>
                            <td><b>Value</b></td>
                            <td><b>Description</b></td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Type</td>
                            <td>0</td>
                            <td>1</td>
                            <td>0x05</td>
                            <td>Heartbeat message</td>
                        </tr>
                         <tr>
                            <td>Status</td>
                            <td>1</td>
                            <td>1</td>
                            <td>0x00</td>
                            <td>Standby</td>
                         </tr>
                         <tr>
                            <td>Battery</td>
                            <td>2</td>
                            <td>1</td>
                            <td>0x99</td>
                            <td>8.388</td>
                         </tr>
                         <tr>
                            <td>Temperature</td>
                            <td>3</td>
                            <td>1</td>
                            <td>0x7d</td>
                            <td>18.5</td>
                         </tr>
                         <tr>
                            <td>Ack/opt</td>
                            <td>4</td>
                            <td>1</td>
                            <td>0x30</td>
                            <td>3/Optional data (depending on message type. Currently used only for position messages)</td>
                         </tr>
                         <tr>
                            <td>Data</td>
                            <td>5</td>
                            <td>1-22</td>
                            <td>0x40</td>
                            <td>last_reset_cause</td>
                        </tr>
                     </tbody>
                    </table>
                </details>
                <details>
                        <summary>
                            <font color="#32cd32"><b>Info: The tracker supports different types of uplink messages, that are described in following sections:</b></font>
                        </summary>
                        <ul>
                        <li>This section describes the payload messages supported by the tracke</li>
                        <li>Unless otherwise specified, all values are transmitted in network byte order (MSB first).</li>
                          <li>Each message is composed by:
                           <ul>
                             <li>A common header</li>
                             <li>A specific data part</li>
                             </ul>
                          </li>
                        </ul>
                        <table style="width: 75%">
                           <thead>
                               <tr>
                                   <td><b>Message type</b></td>
                                   <td><b>Id</b></td>
                                   <td><b>Content</b></td>
                                </tr>
                           </thead>
                           <tbody>
                              <tr>
                                  <td>Frame pending</td>
                                  <td>0x00</td>
                                  <td>This uplink message is sent to trigger the sending. (and speed up the configuration of the tracker) if downlink messages are available on gateway and no other uplink message is on the queue</td>
                              </tr>
                              <tr>
                                  <td>Position message</td>
                                  <td>0x03</td>
                                  <td>GPS, low power GPS, WIFI or BLE position data</td>
                              </tr>
                              <tr>
                                  <td>Energy status message</td>
                                  <td>0x04</td>
                                  <td>Used by the server to estimate the battery level. Contain information related to the power consumption</td>
                              </tr>
                              <tr>
                                  <td>Heartbeat message</td>
                                  <td>0x05</td>
                                  <td>Notify the server the tracker is operational and under LoRa coverage</td>
                              </tr>
                              <tr>
                                  <td>Activity Status message (1)</td>
                                  <td>0x07</td>
                                  <td>Reports the activity counter. Used only by the activity tracking operating mode</td>
                              </tr>
                              <tr>
                                  <td>Configuration message (1)</td>
                                  <td>0x07</td>
                                  <td>Reports the partial or whole configuration of the trackers</td>
                              </tr>
                              <tr>
                                  <td>Shutdown message </td>
                                  <td>0x09</td>
                                  <td>Sent when the tracker is set off</td>
                              </tr>
                              <tr>
                                  <td>Geolocation start message (2)</td>
                                  <td>0x0A</td>
                                  <td>Sent when the tracker starts a geolocation</td>
                              </tr>
                              <tr>
                                  <td>Debug message</td>
                                  <td>0xFF</td>
                                  <td>Internal use only</td>
                              </tr>
                            </tbody>
                        </table>
                        Note:
                        <ul>
                        <li>(1) Activity status message and configuration message share the same identifier. They are differentiated by another field.</li>
                        <li>(2) Only available on FW 1.7-3. Configurable via the config_flag parameter</li>
                        </ul>
                    </details>
                </ul>
         </details>
    </ul>
</details>

Alternatively, you can import it from this [file](/docs/user-guide/resources/actility/uplink_actility_converter.json) 
<details>
    <summary>
        <font color="#006400"><i><b>the following way: Go to Data Converters -> Add new Data Converter -> Import Converter </b></i></font> (<b>click to open expanded view</b>)
    </summary>
    <img src="/images/user-guide/rule-engine-2-0/tutorials/mqtt-downlink/import_new_converter.webp" alt="Import new converter screen">
</details>


## Step 4. Downlink Data Converter configuration
When creating an Downlink Converter, a default decoder is added to the Decoder section.<br>
After creating the Downlink Converter to the Decoder section, you need to update the Decoder code to [the following code](/images/samples/abeeway/downlinkDecoder.txt). <br>

<b>It is necessary to edit the Downlink decoder</b>

Open Downlink Converter, editor mode, click "test decoder function" and replace the default code with a new code:

   <ul>
        <details>
            <summary>
            <font color="#228b22"><b>Screenshot edit the DownLink decoder</b></font> (<b>click to open expanded view</b>)
            </summary>
            <img src="/images/samples/abeeway/downlink_decoder.webp" alt="Downlink decoder properties screen">
        </details>
        <details>
            <summary>
             <font color="#228b22"><b>JSON: output data after DownLink Data Converter looks like this:</b></font>  <br>(<b>click to open expanded view</b>)
             </summary>
             <figure class="highlight"><pre><code class="language-bash" data-lang="bash">             <span class="o">{</span>
                 <span class="o">{</span>
                    /<span class="k">**</span> Encoder <span class="k">**</span>/
                    var data <span class="o">=</span> <span class="o">{}</span><span class="p">;</span>
                    // Process data from incoming message and metadata
                    data.payload <span class="o">=</span> msg.sentPayloadHex<span class="p">;</span>
                    data.DevEUI <span class="o">=</span> metadata[<span class="s1">'DevEUI'</span><span class="o">]</span><span class="p">;</span>
                    data.deviceType <span class="o">=</span> metadata[<span class="s1">'deviceType'</span><span class="o">]</span><span class="p">;</span>
                    data.ContentType <span class="o">=</span> <span class="s2">"application/json"</span><span class="p">;</span>
                    data.Accept <span class="o">=</span> <span class="s2">"application/json"</span><span class="p">;</span>
                    data.urlPrefix <span class="o">=</span> <span class="s2">"/core/latest/api/devices/"</span><span class="p">;</span>
                    data.urlSufix <span class="o">=</span> <span class="s2">"/downlinkMessages"</span><span class="p">;</span>
                    data.urlSufixToken <span class="o">=</span> <span class="s2">"/admin/latest/api/oauth/token"</span><span class="p">;</span>
                    data.firstParamToken <span class="o">=</span> <span class="s2">"client_credentials"</span><span class="p">;</span>
                    data.urlSufixGetDevices <span class="o">=</span> <span class="s2">"/core/latest/api/devices"</span><span class="p">;</span>
                    // Result object with encoded downlink payload
                    var result <span class="o">=</span> <span class="o">{</span>
                        // downlink data content <span class="nb">type</span>: JSON, TEXT or BINARY <span class="o">(</span><span class="nb">base64 </span>format<span class="o">)</span>
                        contentType: <span class="s2">"JSON"</span>,
                        // downlink data
                        data: JSON.stringify<span class="o">(</span>data<span class="o">)</span>,
                        msg: msg,
                        metadata:  metadata
                    <span class="o">}</span><span class="p">;</span>
                    <span class="k">return </span>result<span class="p">;</span>
                 <span class="o">}</span>
             <span class="o">}</span>
             </code></pre></figure>
         </details>
    </ul>


Alternatively, you can import it from this [file](/docs/user-guide/resources/actility/downlink_actility_converter.json)
<details>
    <summary>
        <font color="#006400"><i><b>the following way: Go to Data Converters -> Add new Data Converter -> Import Converter </b></i></font> (<b>click to open expanded view</b>)
    </summary>
    <img src="/images/user-guide/rule-engine-2-0/tutorials/mqtt-downlink/import_new_converter.webp" alt="Import new converter screen">
</details>

## Step 5. Integration configuration
<details>
    <summary>
        <font color="#006400"><i><b>Screenshot of creating integration on the SENTIENT platform</b></i></font> <br> (<b>click to open expanded view</b>)
    </summary> 
    <img src="/images/samples/abeeway/create_integration.webp" alt="Create integration dialog">
</details>
<b><font color="red">WARNING !!!</font> After creation of the Integration...</b>
<ul>
    <li>check of the <b>base URL,</b></li>
    <li>check <b>downLink URL</b> in order to:</li>
    <ol>
        <li>copy <b>downLink URL</b> - the HTTP Endpoint URL from the integration window (Example: https://thingparkenterprise.eu.actility.com/thingpark/dx/core/latest/api/devices)</li>
        <li>paste this <b>downLink URL</b> to the URL of the Application server Actility where the device data is sent to and received from.</li>
    </ol>
</ul>

<details>
    <summary>
        <font color="#006400"><i><b>Screenshot of page ThingPark Wireless OSS intelligent logger (Actility),</b> where you need to copy the <b>downLink URL</b></i></font> <br> (<b>click to open expanded view</b>)
    </summary>
    <img src="/images/samples/abeeway/actility_application.webp" alt="Adding credentials in Actility application">
</details>


## Step 6. Verifying devices connectivity after the creation and configuration of the Integration.
After creating and configuring the integration and connecting it to platform ThingPark Wireless company Actility, SENTIENT will begin receiving the first reports of the telemetry from your devices.
<details>
   <summary>
       <font color="#006400"><i><b>Screenshot of receiving the first reports of the telemetry</b></i></font> (<b>click to open expanded view</b>)
   </summary>
   <img src="/images/samples/abeeway/after_integr_mesag.webp" alt="After integr mesage screen">
</details>
On the basis of these first messages SENTIENT system will automatically create devices with type  and name  under which devices were registered in the ThingPark Actility Enterprise.
<details>
   <summary>
       <font color="#006400"><i><b>Screenshot of how SENTIENT system will automatically create devices</b></i></font> (<b>click to open expanded view</b>)
   </summary>
   <img src="/images/samples/abeeway/after_integr_dev.webp" alt="After integr dev screen">
</details>
That's why after creating and configuring the integration and before starting the Dashboard setup you need to check that all your devices are detected and visible in SENTIENT.

## Step 7. Creation  and  configuration of the Dashboard
<details>
   <summary>
       <font color="#006400"><i><b>Screenshot of the Dashboard after finishing its creation</b></i></font> (<b>click to open expanded view</b>)
   </summary>
   <img src="/images/samples/abeeway/actility_dashboard_example.webp" alt="Actility dashboard example screen">
</details>

[Example:  Dashboard in json format](/images/samples/abeeway/actility_dashboard.json)

<b>- Creation of the Dashboard<b>
<details>
   <summary>
       <font color="#006400"><i><b>Screenshot of the creation of the Dashboard</b></i></font> (<b>click to open expanded view</b>)
   </summary>
   <img src="/images/samples/abeeway/dashboard_create_01.webp" alt="Dashboard creating step 01 dialog">
</details>
<ol>
     <li>Open Dashboard and add to: <br> alias (List abeeways): filter_type: Entity_list, type: Device, device_names: DevEUI_1_, DevEUI_2_, DevEUI_3_...</li>
    <details>
        <summary>
            <font color="#006400"><i><b>Screenshot: open Dashboard and add to: alias (List abeeways): filter_type: Entity_list, type: Device, device_names: DevEUI_1_, DevEUI_2_, DevEUI_3_...</b></i></font> <br> (<b>click to open expanded view</b>)
        </summary>
        <img src="/images/samples/abeeway/alias_create.webp" alt="Alias creating dialog">
    </details>
    <li>Open Dashboard and add to: alias (DigEntityFrom): type: Entity from dashboard state, type: Device</li>
    <details>
        <summary>
            <font color="#006400"><i><b>Screenshot: open Dashboard and add to: alias (DigEntityFrom): type: Entity from dashboard state, type: Device</b></i></font> <br> (<b>click to open expanded view</b>)
        </summary>
        <img src="/images/samples/abeeway/alias_create_entityFromDashboard.webp" alt="Alias create entity From Dashboard dialog">
    </details>
</ol>

<b>- Add to the Dashboard new widgets:</b>
<ol>
    <li> widget number 1: </li>
    <ul>
        <li>Current_bundle: Cards -> latest_values -> Entities: </li>
        <li>Datasources: type: Entity, parameters: List abeeways </li>
        <details>
             <summary>
                 <font color="#006400"><i><b>Screenshot of creation of the widget number 1</b></i></font> (<b>click to open expanded view</b>)
             </summary> 
             <img src="/images/samples/abeeway/widget_create_cards.webp" alt="Widget create cards screen">
         </details>
        <li> Action: action sources: on row click, Name: ${entityName}, type: Update_current_dashboard_state, Set_entity_from_widget </li>
         <details>
              <summary>
                  <font color="#006400"><i><b>Screenshot of widget settings - action sources: on row click to widget number 1</b></i></font> (<b>click to open expanded view</b>)
              </summary> 
              <img src="/images/samples/abeeway/widget_create_cards_action.webp" alt="Widget create cards action dialog">
          </details>
    </ul>
    <li> widget number 2: </li>
    <ul>
        <li>Current_bundle: Charts -> time_series: Timeseries_Float:</li>
        <details>
           <summary>
               <font color="#006400"><i><b>Screenshot of creation of the widget number 2</b></i></font> (<b>click to open expanded view</b>)
           </summary>
           <img src="/images/samples/abeeway/widget_create_charts_timeseriesFloat.webp" alt="Widget create charts timeseries Float screen">
        </details>
        <li>Data_Source: type: Entity, parameters: List_abeeways, key:temperature, label: ${entityLabel}</li>
        <details>
            <summary>
                <font color="#006400"><i><b>Screenshot of adding datasource to widget number 2 (part 1)</b></i></font> (<b>click to open expanded view</b>)
            </summary>
            <img src="/images/samples/abeeway/widget_create_charts.webp" alt="Widget create charts screen">
        </details>
        <details>
           <summary>
               <font color="#006400"><i><b>Screenshot of adding datasource to widget number 2 (part 2)</b></i></font> (<b>click to open expanded view</b>)
           </summary>
           <img src="/images/samples/abeeway/widget_create_charts_entityLabel.webp" alt="Widget create charts entity Label dialog">
        </details>  ![image](/images/samples/abeeway/Actility Dashboard_Example.png)
    </ul>
    <li> widget number 3: </li>
    <ul>
        <li>Current_bundle: Digital_guages</li>
        <details>
           <summary>
               <font color="#006400"><i><b>Screenshot of creation of the widget number 3</b></i></font> (<b>click to open expanded view</b>)
           </summary>
           <img src="/images/samples/abeeway/widget_create_difital_guages.webp" alt="Widget create difital guages screen">
        </details>
        <li>Data_Source: type: Entity, parameters: DigEntityFrom, key:temperature, label: temperature</li>
         <details>
            <summary>
                <font color="#006400"><i><b>Screenshot of adding datasource to widget number 3</b></i></font> <b>click to open expanded view</b>)
            </summary>
            <img src="/images/samples/abeeway/widget_create_difital.webp" alt="Widget create difital scren">
         </details>
    </ul>
    <li> widget number 4: </li>
    <ul>
        <li>Current_bundle: Cards ->Timeseries</li>
        <details>
           <summary>
               <font color="#006400"><i><b>Screenshot of creation widget number 4</b></i></font> (<b>click to open expanded view</b>)
           </summary>
           <img src="/images/samples/abeeway/widget_create_cards_Timeseries.webp" alt="Widget create cards Timeseries screen">
        </details>
        <li>Data_Source: type: Entity, parameters: DigEntityFrom</li>
            <ul>
                <li>keys:temperature, label: temperature</li>>
                <li>keys:batteryVoltage, label: batteryVoltage ...</li>>
            </ul>
        </li>
        <details>
         <summary>
             <font color="#006400"><i><b>Screenshot of adding datasource to widget number 4</b></i></font> (<b>click to open expanded view</b>)
         </summary> 
         <img src="/images/samples/abeeway/widget_create_cards_with_value.webp" alt="Widget create cards with value screen">
        </details>
    </ul>
    <li> widget number 5: </li>
    <ul>
        <li>Current_bundle: Input widgets ->Update Multiple Attributes</li>
        <details>
           <summary>
               <font color="#006400"><i><b>Screenshot of creation of the widget number 5</b></i></font> (<b>click to open expanded view</b>)
           </summary>
           <img src="/images/samples/abeeway/widget_create_input.webp" alt="Widget create input screen">
        </details>
        <li>Data_Source: type: Entity, parameters: DigEntityFrom</li>
            <ul>
                <li>keys:sentPayloadHex, label: ${entityLabel}</li>
            </ul>
        </li>
        <details>
         <summary>
             <font color="#006400"><i><b>Screenshot of adding datasource to the widget number 5</b></i></font> (<b>click to open expanded view</b>)
         </summary>
         <img src="/images/samples/abeeway/widget_create_input_with_value.webp" alt="Widget create input with value dialog">
        </details>
    </ul>
</ol>


-<b><i>Note</i></b>:
<ul>
    <li>Widgets Number 1 and Number 2 with alias <b>Entity_list.Device</b>.</li>
    <li>Widgets Number 3 and Number 4 with alias <b>DigEntityFrom</b>.</li>
</ul>

## Step 8: Post telemetry and verify the Integration configuration
<details>
    <summary>
        <font color="#006400"><i><b>Screenshot of Integration settings change log see here</b></i></font> (<b>click to open expanded view</b>)
    </summary>
    <img src="/images/samples/abeeway/integration_latest_telemetry.webp" alt="Integration latest telemetry screen">
</details>
<details>
    <summary>
        <font color="#006400"><i><b>Screenshot of a log of incoming messages from from ThingPark Wireless OSS intelligent logger (Actility) Platform:</b></i></font> <br> (<b>click to open expanded view</b>)
    </summary>
    <img src="/images/samples/abeeway/integration_events.webp" alt="Integration events dialog">
</details>
If your devices are active and you do everything correctly when you connect the ThingPark Wireless OSS intelligent <br> logger (Actility) Platform, then you will see incoming messages on the dashboard you created.
<details>
    <summary>
        <font color="#006400"><i><b>Screenshot of incoming messages to the dashboard you created</b></i></font> (<b>click to open expanded view</b>)
    </summary>
    <img src="/images/samples/abeeway/actility_dashboard_example.webp" alt="Actility dashboard example screen">
</details>


## Step 9: Configuration the Root Rule Chain (Root)

After adding widget number 5, it must be associated with the downlink decoder.<br>
To do this, go to the "Rule Chain" tab and open the "Root Rule Chain".<br>
<details>
 <summary>
     <font color="#006400"><i><b>Screenshot of configuration of the Root Rule Chain for the  message to be sent to device</b></i></font> (<b>click to open expanded view</b>)
 </summary>
 <img src="/images/samples/abeeway/rule_chain.webp" alt="Rule chain example screen">
</details> <br>
Editing the "Root Rule Chain":
<ul>
    <li>To get the original name of the device via metadata After "Message Type Switch" add Enrichment node: "originator fields" with the name "Fetch Name and Type":</li>
        <ul>
        <li>name: deviceName</li>
        <li>type: deviceType</li>
        <li>The relationship between "Message Type Switch" and "Fetch Name and Type":</li>
            <ul>
                <li>"Rule node link details": "Attributes Update"</li>
            </ul>
        </ul>
    <details>
     <summary>
         <font color="#006400"><i><b>Screenshot of the created Enrichment node: "originator fields"</b></i></font> (<b>click to open expanded view</b>)
     </summary>
     <img src="/images/samples/abeeway/create_incrichment_originator_fields.webp" alt="Create encrichment originator fields screen">
    </details>
    <li>To receive downlink data by a decoder and transmit decoded data to "Action - rpc call request":</li>
        <ul>
        <li>between "Fetch Name and Type" and "Action - rpc call request"</li>
            <ul>
                <li>add: Action: "integration downlink": name: Actility_DownLink, integration: Test_ThigPark</li>
                    <details>
                     <summary>
                         <font color="#006400"><i><b>Screenshot of the created Action: "integration downlink"</b></i></font> (<b>click to open expanded view</b>)
                     </summary>
                     <img src="/images/samples/abeeway/create_action _integration_downlink.png" alt="Create action integration downlink screen">
                    </details>
            </ul>
        <li>The relationship between "Fetch Name and Type" and "Actility_DownLink":</li>
            <ul>
                <li>"Rule node link details": "Success"</li>
             </ul>
        <li>The relationship between "Actility_DownLink" and "Action - rpc call request":</li>
            <ul>
                <li>"Rule node link details": "Success"</li>
            </ul>
        </ul>
</ul>

## Step 10: Create and Sent Downlink messages

Before sending a message:
- you must create a heading in which the type of request is determined (information about the configuration, or about the status of the device, or about the new configuration)<br>
and also the content of the data itself (a detailed description of the data).

<details>
    <summary>
         <font color="#006400"><i><b>Information to create Downlink messages</b></i></font> (<b>click to open expanded view</b>)
    </summary>
     <ul>
        <li>These messages are sent from the server to the tracker through the LoRa network. They are used to either
        configure or manage the tracker. Each message contains a header including: </li>
        <ul>
            <li> A message type </li>
            <li> An acknowledgement token</li>
        </ul>
        <details>
            <summary>
             <font color="#228b22"><i><b>The remainder of the message depends on the message type described in the following table.</b></i></font> <br> (<b>click to open expanded view</b>)
            </summary>
            <table style="width: 50%">
              <thead>
                  <tr>
                      <td><b>Message type</b></td>
                      <td><b>ID</b></td>
                      <td><b>Description</b></td>
                  </tr>
              </thead>
              <tbody>
                  <tr>
                      <td>POD</td>
                      <td>0x01</td>
                      <td>Position on demand</td>
                  </tr>
                  <tr>
                      <td>Set Mode</td>
                      <td>0x02</td>
                      <td>hange the tracker operational mode</td>
                  </tr>
                  <tr>
                      <td>Request configuration</td>
                      <td>0x03</td>
                      <td>Request the actual configuration of the tracker</td>
                  </tr>
                  <tr>
                      <td>Start SOS mode</td>
                      <td>0x04</td>
                      <td>Turn on SOS mode</td>
                  </tr>
                  <tr>
                      <td>Stop SOS mode</td>
                      <td>0x05</td>
                      <td>Turn off SOS mode</td>
                  </tr>
                  <tr>Enrichment: "originator fields"
                      <td>Set Param</td>
                      <td>0x0B</td>
                      <td>Modify parameter(s)</td>
                  </tr>
                  <tr>
                      <td>Debug command</td>
                      <td>0xFF</td>
                      <td>Remove BLE bonding. Reset the tracker</td>
                  </tr>
                </tbody>
            </table>
        </details>
        - Create request: Position on demand
        [JSON: Create request "Position on demand"](/images/samples/abeeway/payloadHex_0102.json)
        <details>
            <summary>
             <font color="#228b22"><i><b>Create request: Position on demand</b></i></font> (<b>click to open expanded view</b>)
            </summary> 
            <ul>
                <details>
                    <summary>
                    <font color="##228b22"><i><b>Create request: Position on demand -> Mode: operating modes. Acceptable values are:</b></i></font> (<b>click to open expanded view</b>)
                    </summary> 
                    <table style="width: 40%">
                      <thead>
                          <tr>
                              <td><b>Mode</b></td>
                              <td><b>Value</b></td>
                          </tr>
                      </thead>
                      <tbody>
                          <tr>
                              <td>Standby</td>
                              <td>0</td>
                          </tr>
                          <tr>
                              <td>Motion tracking</td>
                              <td>1</td>
                          </tr>
                          <tr>
                              <td>Permanent tracking</td>
                              <td>2</td>
                          </tr>
                          <tr>
                              <td>Motion start/end tracking</td>
                              <td>3</td>
                          </tr>
                          <tr>
                              <td>Activity tracking</td>
                              <td>4</td>
                          </tr>
                          <tr>
                              <td>Off mode</td>
                              <td>5</td>
                          </tr>
                       </tbody>
                    </table>
                 </details>
                 <ul>
                    <li>Operational mode configuration</li>
                    <figure class="highlight"><pre><code class="language-bash" data-lang="bash">                    <span class="o">{</span>...
                          payloadHex: <span class="s2">"0203"</span>, ...
                    <span class="o">}</span>
                    </code></pre></figure>
                    <li>Request device configuration</li>
                    <figure class="highlight"><pre><code class="language-bash" data-lang="bash">                    <span class="o">{</span>...
                        payloadHex: <span class="s2">"030605090C01"</span>, ...
                        <span class="k">*</span> <span class="s2">"05"</span> - geoloc_sensor,
                        <span class="k">*</span> <span class="s2">"09"</span> - gps_timeout,
                        <span class="k">*</span> <span class="s2">"0C"</span> - gps_convergence,
                        <span class="k">*</span> <span class="s2">"01"</span> - lora_period,
                        Special parameter Id:
                        <span class="k">*</span> <span class="s2">"0xFD"</span>: get the BLE version.
                        <span class="k">*</span> <span class="s2">"0xFE"</span>: get the firmware version.
                    <span class="o">}</span>
                    </code></pre></figure>
                    <li>Parameters configuration</li>
                    <figure class="highlight"><pre><code class="language-bash" data-lang="bash">                    <span class="o">{</span>...
                          payloadHex: <span class="s2">"0B 0A 0C00000078 1100000E10"</span>, ...
                         <span class="k">*</span> <span class="s2">"0C00000078"</span> - 0C - gps_convergence, 0x78 - value <span class="o">(</span>sec<span class="o">)</span>,
                         <span class="k">*</span> 1100000E10 - 11 - gps_standby_timeout. 0xE10 - value <span class="o">(</span>sec<span class="o">)</span><span class="nb">.</span>
                    <span class="o">}</span>
                    </code></pre></figure>
                </ul>
            </ul>
        </details>
    </ul>
</details>
<details>
    <summary>
         <font color="#006400"><i><b>Sending Downlink messages</b></i></font> (<b>click to open expanded view</b>)
    </summary>
    <ul>
        <li>Messages to devices are sent from widget number 5:</li>
        <details>
             <summary>
                 <font color="#228b22"><i><b>Screenshot of the sent message from widget number 5</b></i></font> (<b>click to open expanded view</b>)
             </summary>
             <img src="/images/samples/abeeway/sent_message.webp" alt="Sent message screen">
        </details>
        <details>
            <summary>
                 <font color="#228b22"><i><b>Example of the creation message</b></i></font> (<b>click to open expanded view</b>)
            </summary>
              <figure class="highlight"><pre><code class="language-bash" data-lang="bash">                <span class="o">{</span>...
                      payloadHex: <span class="s2">"03020001020305"</span>,
                ...<span class="o">}</span>
                </code></pre></figure>
                <figure class="highlight"><pre><code class="language-bash" data-lang="bash">                <span class="o">{</span>...
                    Byte 0 Byte 1 Byte 2-21
                    <span class="s2">"0x03"</span> <span class="s2">"ACK"</span> Byte <span class="s2">"2-21"</span> Parameter ID list <span class="o">(</span>optional<span class="o">)</span>
                    Special parameter Id:
                    ➢ 0xFD: get the BLE version.
                    ➢ 0xFE: get the firmware version.
                    Byte 2-21 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12
                    13 fd fe
                    00 01 02 03 05 06 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 fe
                ...<span class="o">}</span>
                </code></pre></figure>
        </details>
        <details>
          <summary>
              <font color="#228b22"><i><b>Screenshot of receiving / sending messages to the device ThingPark Wireless OSS intelligent logger (Actility)</b></i></font> (<b>click to open expanded view</b>)
          </summary>
          <img src="/images/samples/abeeway/receiving_message_actility.webp" alt="Receiving message actility screen">
         </details>
        <details>
          <summary>
              <font color="#228b22"><i><b>Screenshot of receiving messages from the device ThingPark Wireless OSS intelligent logger (Actility)</b></i></font> (<b>click to open expanded view</b>)
          </summary>
          <img src="/images/samples/abeeway/receiving_actility_from_dev.webp" alt="Receiving actility from dev screen">
         </details>
        <details>
          <summary>
              <font color="#228b22"><i><b>Screenshot of receiving confirmation from the ThingPark Wireless to SENTIENTabout sending a message to the device</b></i></font> (<b>click to open expanded view</b>)
          </summary>
          <img src="/images/samples/abeeway/receiving_confirmation_singboard.webp" alt="Receiving confirmation thingboard dialog">
         </details>
        <details>
          <summary>
              <font color="#228b22"><i><b>Screenshot of decoding device response by Sentient  UpLink decoder</b></i></font> (<b>click to open expanded view</b>)
          </summary>
          <img src="/images/samples/abeeway/decoding_device_response.webp" alt="Decoding device response dialog">
         </details>
    </ul>

</details>

## Next steps


- [Getting started guides](/docs/pe/guides/#AnchorIDGettingStartedGuides) - These guides provide quick overview of main SENTIENT features. Designed to be completed in 15-30 minutes.
- [Installation guides](/docs/user-guide/install/pe/installation-options/) - Learn how to set up SENTIENT on various available operating systems.
- [Connect your device](/docs/pe/guides/#AnchorIDConnectYourDevice) - Learn how to connect devices based on your connectivity technology or solution.
- [Data visualization](/docs/pe/guides/#AnchorIDDataVisualization) - These guides contain instructions on how to configure complex SENTIENT dashboards.
- [Data processing & actions](/docs/pe/guides/#AnchorIDDataProcessing) - Learn how to use SENTIENT Rule Engine.
- [IoT Data analytics](/docs/pe/guides/#AnchorIDDataAnalytics) - Learn how to use rule engine to perform basic analytics tasks.
- [Advanced features](/docs/pe/guides/#AnchorIDAdvancedFeatures) - Learn about advanced SENTIENT features.
