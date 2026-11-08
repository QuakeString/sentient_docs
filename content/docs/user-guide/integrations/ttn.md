+++
title = "The Things Stack Community integration"
description = "The Things Stack Community integration guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/ttn.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

## Overview
TheThingsStack is LoRaWAN network designed for connecting your devices using LoRaWAN stack. 
After integrating TheThingsStack with Sentient, you can connect, communicate, process and visualize data from devices in the Sentient IoT platform.


## The Things Stack Community setup

### Register Application
The first step is to create an **application** in TheThingsStack console. Go to [console](https://console.thethingsnetwork.org/), open 
**Applications** section, press **add application** button and fill required fields.

- **Application ID** - sentient-connection

Handler registration - used to identify region where application will be registered. In our example it
will be *eu* region.

![image](/images/user-guide/integrations/ttn/ttn-add-application.webp)

### Payload Decoder
Our device submits data in binary format. We have 2 options where to decode this data:

- **TheThingsStack decoder** - data will be decoded before entering the Sentient
- **Sentient converters** - uplink/downlink converters will be used to decode data from binary format into JSON

In this tutorial, we will make an initial transformation into JSON with TTS decoder and then use Sentient converters for correct data processing.
In real life scenario, it is up to you where to decode/encode data, because it is possible to do this on any side.

Decode Function:
```ruby
function Decoder(bytes, port) {
  var decoded = {temperature: bytes[0]};
  return decoded;
}
```


![image](/images/user-guide/integrations/ttn/ttn-decoder.webp)

Press **Save payload function**

### Device Registration in TheThingsStack

Next step is a Device creation in the TTS. Open **Devices** page and press **register device**

- Device ID - thermostat_a
- Device EUI - press **generate** button for generating random identified
- AppEUI - you can fill with zero
- AppKey - press **generate** button for generating random identified


![image](/images/user-guide/integrations/ttn/ttn-add-device_0.webp)

![image](/images/user-guide/integrations/ttn/ttn-add-device_1.webp)

Press **Register** button.

### Payload formatter (optionally)

After device added in TTS, you can test your decoder and payload. Go to your device the **thermostat-a**, and select tab **payload_formatters**. We will take the first byte as a temperature value from a device
and transform it into JSON.

**Payload:**
```
  0F
```


**Output json:**
```json
{
  "temperature": 15
}
```

![image](/images/user-guide/integrations/ttn/payload_format.webp)

### Access key (API key)

Also, an access key will be needed to configure the integration, it can be generated in the API keys menu. It's important to save it.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/ttn/api_key_access_token_0.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/ttn/api_key_access_token_1.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/integrations/ttn/api_key_access_token_2.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Integration with Sentient
We made all required configurations in the TheThingsStack (register application, add decoder function and register device). Now we can start configuring Sentient.

### Sentient Uplink Data Converter

First, we need to create an Uplink Data Converter which will be used for receiving messages from the TTS. 
The converter should transform incoming payload into the required message format. Message must 
contain **deviceName** and **deviceType**. Those fields are used for submitting data to the correct device. 
If a device was not found a new device will be created.

Here is how payload from TheThingsStack will look like:
```json
{
  "end_device_ids": {
    "device_id": "thermostat-a",
    "application_ids": {
      "application_id": "sentient-connection"
    },
    "dev_eui": "70B3D57ED00550F2",
    "join_eui": "0000000000000000"
  },
  "correlation_ids": ["as:up:01GC9S4G55D3AJ2PG32TCAZ6H1", "rpc:/ttn.lorawan.v3.AppAs/SimulateUplink:48ff02a3-cc7d-4097-b301-1411dbae3ca2"],
  "received_at": "2022-09-06T16:11:35.461454886Z",
  "uplink_message": {
    "f_port": 1,
    "frm_payload": "Dw==",
    "decoded_payload": {
      "temperature": 15
    },
    "rx_metadata": [{
      "gateway_ids": {
        "gateway_id": "test"
      },
      "rssi": 42,
      "channel_rssi": 42,
      "snr": 4.2
    }],
    "settings": {
      "data_rate": {
        "lora": {
          "bandwidth": 125000,
          "spreading_factor": 7
        }
      }
    }
  },
  "simulated": true
}
```


We will take **device_id** and map it to the **deviceName** and **application_id** map to the **deviceType**. But you can use another mapping in your specific use cases. Also, we will take the value of the **temperature** field and use it as a device telemetry.

Go to **Data Converters** and create new **uplink** Converter with this function: 

```ruby
var data = decodeToJson(payload);
var deviceName = data.end_device_ids.device_id;
var deviceType = data.end_device_ids.application_ids.application_id;

var result = {
    deviceName: deviceName,
    deviceType: deviceType,
    telemetry: {
         temperature: data.uplink_message.decoded_payload.temperature
    }
};

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


![image](/images/user-guide/integrations/ttn/st-converter_0.webp)

![image](/images/user-guide/integrations/ttn/st-converter_1.webp)

### Sentient Downlink Data Converter
For sending Downlink messages from Sentient to the device inside TTS, we need to define a Downlink 
Converter. In general, the output from the Downlink Converter should have the following structure:
```json
{
  "downlinks": [{
    "f_port": 2,
    "frm_payload": "vu8=",
    "priority": "NORMAL"
  }]
}
```


- **contentType** - defines how data will be encoded {TEXT \| JSON \| BINARY}
- **data** - actual data that will be sent to the device in TTS. More details about API can be found in this [TTS API](https://www.thethingsnetwork.org/docs/applications/mqtt/api)
- **metadata** - in this object you should place correct devId value that will be used to identify target device in TTS

Go to **Data Converters** and create new **downlink** Converter with this function:

```ruby
var data = {
        downlinks: [{
            f_port: 2,
            confirmed: false,
            frm_payload: btoa(msg.version),
            priority: "NORMAL"
        }]
    };

var result = {
    contentType: "JSON",
    data: JSON.stringify(data),
    metadata: {
        devId: 'thermostat1'
    }

};
return result;
```


This converter will take the **version** field from the incoming message and add it as a payload field 
in the outbound message. The destination device is a **thermostat-a** device.

![image](/images/user-guide/integrations/ttn/st-downlink-converter.webp)

### TTS Integration

Next we will create the integration with TheThingsStack inside Sentient. Open **Integrations** section and add new Integration with type
**TheThingsStack**

- Name: **TheThingsStack Integration**
- Type: **The Things Stack Community**
- Uplink data converter: **TheThingsStack Uplink**
- Downlink data converter: **TheThingsStack Downlink**
- Region: **eu1** (region where your application was registered inside TTS)
- Application ID: **sentient-connection** (use **Application ID** from TTS)
- Access Key: use **Access Key** from TTS
- Use API v3: Set **Enable**

![image](/images/user-guide/integrations/ttn/st-integration_0.webp)

When adding the integration, you can test the connection between SENTIENT and TheThingsStack. For it, 
after all required configurations, click the **Check connection** button.

![image](/images/user-guide/integrations/ttn/st-integration_1.webp)

## Validation

### Validate Uplink Messages
Let's verify our integration. Go to the device **thermostat-a** page in TheThingsStack. Scroll to the **Simulate Uplink** section.
Our device will publish temperature **0F** (15). So enter **0F** into the payload field and press the **Send** button.

![image](/images/user-guide/integrations/ttn/ttn-send-payload.webp)

In Sentient go to **Device Group** -> **All** -> **thermostat-a** - here you can see that 

- a new device was registered in Sentient
- in the **Latest Telemetry** section you will see that the last submitted temperature equals 15.

![image](/images/user-guide/integrations/ttn/st-device-telemetry.webp)

### Validate Downlink Messages
For testing Downlink Messages, we will update our Root Rule Chain to send downlink message when a device attribute is changed.
Open and edit **Root Rule Chain**. Add **Integration Downlink** Action node and connect it with the **Message Type Switch** Node using the relation 
**Attributes Updated**

![image](/images/user-guide/integrations/ttn/st-add-rule-downlink.webp)

![image](/images/user-guide/integrations/ttn/st-route-to-downlink.webp)

Save Changes.

Go to **Device Group** -> **All** -> **thermostat_a** -> attributes section. We will add **Shared attribute** with the name **version** and
the value **v.0.11**

![image](/images/user-guide/integrations/ttn/st-add-version.webp)

By making this step, we triggered a downlink message to the device **thermostat-a** and this message should contain the versions field value. 
Open TTS Console, navigate to **st_platform** application, to the section **Data**. And we see that the Downlink message was received.

![image](/images/user-guide/integrations/ttn/ttn-downlink-verified.webp)

## See also
With this integration you can also configure Downlink converters and trigger required actions using Rule Engine nodes.

- [Integration Overview](/docs/user-guide/integrations/)
- [Uplink Converters](/docs/user-guide/integrations/#uplink-data-converter)
- [Downlink Converters](/docs/user-guide/integrations/#downlink-data-converter)
- [Rule Engine](/docs/user-guide/rule-engine-2-0/re-getting-started/)


## Next steps
