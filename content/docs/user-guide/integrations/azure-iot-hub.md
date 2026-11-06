+++
title = "Azure IoT Hub Integration"
description = "Azure IoT Hub Integration Guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/azure-iot-hub.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

## Overview

Azure IoT Hub Integration allows to stream data from AWS IoT Backend to SENTIENT and converts device payloads to the SENTIENT format.

  <object width="80%" data="/images/user-guide/integrations/azure/iot-hub-integration.svg"></object>

## Create and configure Azure IoT Hub account

- [Create an IoT hub](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal#create-an-iot-hub).
- [Register a new device in the IoT hub](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-create-through-portal#register-a-new-device-in-the-iot-hub).

## Integration with the Sentient
We have done all necessary steps on the Azure IoT Hub side. Now we can start configuring the Sentient.

### Sentient Uplink Data Converter

First, we need to create Uplink Data converter that will be used for converting messages received from the Azure IoT Hub. The converter should transform incoming payload into the required message format.
Message must contains **deviceName** and **deviceType**. Those fields are used for submitting data to the correct device. If a device was not found then new device will be created.
Here is how demo payload from the Azure IoT Hub will look like:
<figure class="highlight"><pre><code class="language-json" data-lang="json"><span class="p">{</span><span class="w">
    </span><span class="nl">"devName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"T1"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"msg"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"temp"</span><span class="p">:</span><span class="w"> </span><span class="mi">42</span><span class="p">,</span><span class="w">
        </span><span class="nl">"humidity"</span><span class="p">:</span><span class="w"> </span><span class="mi">77</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span></code></pre></figure>

We will take **devName** and map it to the **deviceName**. But you can use another mapping in your specific use cases.
Also, we will take the value of the **temperature** and **humidity** fields and use it as a device telemetry. 

Go to **Data Converters** and create new **uplink** Converter with this function: 
<figure class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">data</span> <span class="o">=</span> <span class="nx">decodeToJson</span><span class="p">(</span><span class="nx">payload</span><span class="p">);</span>
<span class="kd">var</span> <span class="nx">deviceName</span> <span class="o">=</span> <span class="nx">data</span><span class="p">.</span><span class="nx">devName</span><span class="p">;</span>
<span class="kd">var</span> <span class="nx">deviceType</span> <span class="o">=</span> <span class="dl">'</span><span class="s1">thermostat</span><span class="dl">'</span><span class="p">;</span>

<span class="kd">var</span> <span class="nx">result</span> <span class="o">=</span> <span class="p">{</span>
   <span class="na">deviceName</span><span class="p">:</span> <span class="nx">deviceName</span><span class="p">,</span>
   <span class="na">deviceType</span><span class="p">:</span> <span class="nx">deviceType</span><span class="p">,</span>
   <span class="na">telemetry</span><span class="p">:</span> <span class="p">{</span>
       <span class="na">temperature</span><span class="p">:</span> <span class="nx">data</span><span class="p">.</span><span class="nx">msg</span><span class="p">.</span><span class="nx">temp</span><span class="p">,</span>
       <span class="na">humidity</span><span class="p">:</span> <span class="nx">data</span><span class="p">.</span><span class="nx">msg</span><span class="p">.</span><span class="nx">humidity</span>
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

![image](/images/user-guide/integrations/azure/iot-hub-converter.webp)

### Azure IoT Hub Integration

Next we will create Integration with Azure IoT Hub inside the Sentient. Open **Integrations** section and add new Integration with type
**Azure IoT Hub**

- Name: IoT Hub
- Type: Azure IoT Hub
- Uplink data converter: Thermostat Converter
- Hostname: **AZURE_IOT_HUB_HOSTNAME**
- Device ID: T1
- Credentials: Shared Access Signature
- SAS Key: **DEVICE_SAS_KEY**
- Topic filter: devices/T1/messages/devicebound/#

![image](/images/user-guide/integrations/azure/iot-hub-add-integration.webp)

- **Topic** - for more information about IoT Hub topic use [link](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support#receiving-cloud-to-device-messages).
- **Credentials** - Azure IoT Hub connection credentials. Can be either *Shared Access Signature* or *PEM*.

Different Authentication credentials are supported for Azure IoT Hub:

- Shared Access Signature - SAS Key is used for Authentication
- PEM - PEM certificates are used for Authentication

If **Shared Access Signature** credentials type is selected, the following configuration should be provided:
- SAS Key - it is key from your device in [Azure IoT Hub](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-authenticate-downstream-device#symmetric-key-authentication)
- CA certificate file, by default used Baltimore certificate. More about certificates [here](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support#tlsssl-configuration)

If **PEM** credentials type is selected, the following configuration should be provided:

- CA certificate file, by default used Baltimore certificate. More about certificates [here](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support#tlsssl-configuration)
- Certificate file
- Private key file
- Private key password

[X.509 CA-signed authentication](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-authenticate-downstream-device#x509-ca-signed-authentication)

[CACertificates instruction](https://github.com/Azure/azure-iot-sdk-c/tree/master/tools/CACertificates)

## Validation

### Validate Uplink Messages
Lets verify our integration. First, lets put message into uplink stream, so Sentient will fetch this message. 

Open page with your Device and go to **Message to Device**.

Send test message to device.

![image](/images/user-guide/integrations/azure/iot-hub-send-test-msg.webp)


Go to **Device Group** -> **All** -> **T1** - you can see that 

- new device was registered in the sentient
- In the **Latest Telemetry** section you will see that last submitted temperature = 42 and humidity = 77.

![image](/images/user-guide/integrations/azure/iot-hub-validate-telemetry.webp)

## Next steps
