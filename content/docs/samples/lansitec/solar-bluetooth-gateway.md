+++
title = "Solar Bluetooth Gateway"
description = "Solar Bluetooth Gateway"

[extra]
status = "imported"
checked = ""
source = "docs/samples/lansitec/solar-bluetooth-gateway.md"
+++
<img src="/images/samples/lansitec/solar-bluetooth-gateway.webp" alt="LoRaWAN Solar Bluetooth Gateway" style="float: left; max-width: 200px; max-height: 200px; margin: 0px 10px 0px 0px" />[**Solar Bluetooth Gateway**](https://www.lansitec.com/products/lorawan-solar-bluetooth-gateway/) is designed based on LoRaWAN and Bluetooth 5.0 technology. It receives nearby [**Bluetooth beacon**](https://www.lansitec.com/products/bluetooth-beacon/) messages, and then transmit to a LoRaWAN gateways through LoRaWAN after restructure the data. It is powered with robust solar film and a 5300mAh rechargeable battery.

<br><br><br><br>

## Prerequisites

To continue with this guide we will need the following:

- [Solar Bluetooth Gateway](https://www.lansitec.com/products/lorawan-solar-bluetooth-gateway/)
- [LoRaWAN Gateway](https://www.lansitec.com/products/outdoor-lorawan-gateway/)
- [Bluetooth beacon](https://www.lansitec.com/products/bluetooth-beacon/)
- [Network Server account](https://www.chirpstack.io/)
- [SENTIENT account](https://sentient.invenia.in/installations/choose-region/)

## Configuration

To create integration with the network server Chirpstack

### Add a LoRaWAN Gateway on Chirpstack

First, we need to add a LoRaWAN gateway on the [Chirpstack](https://chirpstack.io/).

Step to add a gateway:


1. Log in to Chirpstack server. Go to the **Gateways** page and click the **Add gateway** button.

1. Enter the **Name**, **Gateway ID** (found in the gateway control panel), then scroll down and click the **Submit** button.

1. Once added, you can view the gateway&#39;s status under the **Gateways** tab.


<div class="st-gallery"><figure><img src="/images/samples/lansitec/gateway-1.webp" alt="Log in to Chirpstack server. Go to the **Gateways** page and click the **Add gateway** button." loading="lazy"><figcaption>Log in to Chirpstack server. Go to the **Gateways** page and click the **Add gateway** button.</figcaption></figure><figure><img src="/images/samples/lansitec/gateway-2.webp" alt="Enter the **Name**, **Gateway ID** (found in the gateway control panel), then scroll down and click the **Submit** button." loading="lazy"><figcaption>Enter the **Name**, **Gateway ID** (found in the gateway control panel), then scroll down and click the **Submit** button.</figcaption></figure><figure><img src="/images/samples/lansitec/gateway-3.webp" alt="Once added, you can view the gateway&#39;s status under the **Gateways** tab." loading="lazy"><figcaption>Once added, you can view the gateway&#39;s status under the **Gateways** tab.</figcaption></figure></div>


### Configure the LoRaWAN Gateway to send data

To connect the gateway and transmit data to ChirpStack, follow these steps:


1. Open the gateway control panel. Go to the **Network Settings** page and set the Mode to **Packet Forwarder**. Enter your server address in the **Server Address** field (e.g., **192.168.31.11** in our case), then click **Save & Apply** button.

1. Verify the gateway&#39;s status on ChirpStack, it should now appear online.


<div class="st-gallery"><figure><img src="/images/samples/lansitec/rak-1.webp" alt="Open the gateway control panel. Go to the **Network Settings** page and set the Mode to **Packet Forwarder**. Enter your server address in the **Server Address** field (e.g., **192.168.31.11** in our case), then click **Save & Apply** button." loading="lazy"><figcaption>Open the gateway control panel. Go to the **Network Settings** page and set the Mode to **Packet Forwarder**. Enter your server address in the **Server Address** field (e.g., **192.168.31.11** in our case), then click **Save & Apply** button.</figcaption></figure><figure><img src="/images/samples/lansitec/rak-2.webp" alt="Verify the gateway&#39;s status on ChirpStack, it should now appear online." loading="lazy"><figcaption>Verify the gateway&#39;s status on ChirpStack, it should now appear online.</figcaption></figure></div>


### Add a device profile on Chirpstack


1. In Chirpstack UI, go to the **Device Profiles** page and click **Add device profile** button.

1. Fill in the required fields.

1. Navigate to the **Codec** tab, select "JavaScript functions”, paste the **Solar Bluetooth Gateway decoder**, and click **Submit**.


<div class="st-gallery"><figure><img src="/images/samples/lansitec/device-profiles-1.webp" alt="In Chirpstack UI, go to the **Device Profiles** page and click **Add device profile** button." loading="lazy"><figcaption>In Chirpstack UI, go to the **Device Profiles** page and click **Add device profile** button.</figcaption></figure><figure><img src="/images/samples/lansitec/device-profiles-2.webp" alt="Fill in the required fields." loading="lazy"><figcaption>Fill in the required fields.</figcaption></figure><figure><img src="/images/samples/lansitec/device-profiles-3.webp" alt="Navigate to the **Codec** tab, select &quot;JavaScript functions”, paste the **Solar Bluetooth Gateway decoder**, and click **Submit**." loading="lazy"><figcaption>Navigate to the **Codec** tab, select "JavaScript functions”, paste the **Solar Bluetooth Gateway decoder**, and click **Submit**.</figcaption></figure></div>


**Solar Bluetooth Gateway decoder**:

```javascript
  // Decode uplink function.
  //
  // Input is an object with the following fields:
  // - bytes = Byte array containing the uplink payload, e.g. [255, 230, 255, 0]
  // - fPort = Uplink fPort.
  // - variables = Object containing the configured device variables.
  //
  // Output must be an object with the following fields:
  // - data = Object representing the decoded payload.
  
  // Solar Bluetooth Gateway decoder
  function decodeUplink(input) {
    // bytes
    var bytes = input.bytes;
    // type
    var uplinkType = (bytes[0] >> 4) & 0x0f;
  
    switch (uplinkType) {
      case 0x01:
        return { data: decodeRegistration(bytes) };
  
      case 0x02:
        return { data: decodeHeartbeat(bytes) };
  
      case 0x03:
        return { data: decodeDeviceReportRule(bytes) };
  	  
  	case 0x05:
        return { data: decodeWaterLevelDetection(bytes) };
  
      case 0x08:
        return { data: decodeDeviceType1(bytes) };
  
      case 0x09:
        return { data: decodeDeviceType2(bytes) };
  
      case 0x0a:
        return { data: decodeDeviceType3(bytes) };
  
      case 0x0e:
        return { data: decodeMultiDeviceTypeMessage(bytes) };
  
      case 0x0f:
        return { data: decodeAcknowledgment(bytes) };
  
      default:
        return null;
    }
  }
  
  // type: 0x1 Registration
  function decodeRegistration(bytes) {
    var data = {};
    data.type = "Registration";
    // adr
    data.adr = ((bytes[0] >> 3) & 0x1) == 0 ? "OFF" : "ON";
    // mode
    data.mode = bytes[0] & 0x07;
    // loRaWANBand
    var loRaWANBandValue = bytes[1];
    if (loRaWANBandValue == 0x00) {
      data.loRaWANBand = "KR920";
    } else if (loRaWANBandValue == 0x01) {
      data.loRaWANBand = "AU915";
    } else if (loRaWANBandValue == 0x04) {
      data.loRaWANBand = "CN470";
    } else if (loRaWANBandValue == 0x08) {
      data.loRaWANBand = "AS923";
    } else if (loRaWANBandValue == 0x10) {
      data.loRaWANBand = "EU433";
    } else if (loRaWANBandValue == 0x20) {
      data.loRaWANBand = "EU868";
    } else if (loRaWANBandValue == 0x40) {
      data.loRaWANBand = "US915";
    }
    // power
    data.power = ((bytes[2] >> 3) & 0x1f) + "dBm";
    // continuousBleReceiveEnable
    data.continuousBleReceiveEnable =
      ((bytes[2] >> 1) & 0x1) == 0 ? "Disable" : "Enable";
    // dr
    data.dr = (bytes[3] >> 4) & 0x0f;
    // positionReportInterval
    data.positionReportInterval =
      (((bytes[4] << 8) & 0xff00) | (bytes[5] & 0xff)) * 5 + "s";
    // heartbeatInterval
    data.heartbeatInterval = bytes[6] * 30 + "s";
    // bleReceivingDuration
    data.bleReceivingDuration = bytes[7] + "s";
    // networkReconnectionInterval
    data.networkReconnectionInterval = bytes[8] * 5 + "min";
    return data;
  }
  
  // type: 0x2 Heartbeat
  function decodeHeartbeat(bytes) {
    var data = {};
    // type
    data.type = "Heartbeat";
    // battery
    var batteryValue = bytes[1];
    if (batteryValue > 100) {
      data.battery = bytes[1] / 100 + 1.5 + "V";
    } else {
      data.battery = bytes[1] + "%";
    }
    // rssi
    data.rssi = bytes[2] * -1 + "dBm";
    // snr
    data.snr = (((bytes[3] << 8) & 0xff00) | (bytes[4] & 0xff)) / 100 + "dB";
    // version
    data.version = ((bytes[5] << 8) & 0xff00) | (bytes[6] & 0xff);
    // chargeState
    var chargeStateValue = bytes[7] & 0xff;
    if (chargeStateValue == 0x00) {
      data.chargeState = "Not charging";
    } else if (chargeStateValue == 0x50) {
      data.chargeState = "Charging";
    } else if (chargeStateValue == 0x60) {
      data.chargeState = "Charging completed";
    }
    return data;
  }
  
  // type: 0x3 DeviceReportRule
  function decodeDeviceReportRule(bytes) {
    var data = {};
    data.type = "DeviceReportRule";
    data.deviceTypeQuantity = bytes[1] & 0xff;
    data.deviceTypeId = (bytes[2] >> 4) & 0x0f;
    data.filterAndDataBlockQuantity = bytes[2] & 0x0f;
    var filterBlock = [];
    var dataBlock = [];
    var macBlock = [];
    var index = 3;
    for (let i = 0; i < data.filterAndDataBlockQuantity; i++) {
      var ruleType = bytes[index++] & 0xff;
      var startAddress = bytes[index++] & 0xff;
      var endAddress = bytes[index++] & 0xff;
      var filter = {};
      if (ruleType == 1) {
        filter.ruleType = "FilterBlock";
        filter.startAddress = byteToHex(startAddress);
        filter.endAddress = byteToHex(endAddress);
        var len = endAddress - startAddress;
        var filterValue = "";
        for (let j = 0; j < len + 1; j++) {
          filterValue += byteToHex(bytes[index + j]);
        }
        filter.value = filterValue;
        index = index + (endAddress - startAddress + 1);
        filterBlock.push(filter);
      } else if (ruleType == 2) {
        filter.ruleType = "DataBlock";
        filter.startAddress = byteToHex(startAddress);
        filter.endAddress = byteToHex(endAddress);
        dataBlock.push(filter);
      } else if (ruleType == 3) {
        filter.ruleType = "MACBlock";
        filter.startAddress = byteToHex(startAddress);
        filter.endAddress = byteToHex(endAddress);
        macBlock.push(filter);
      }
    }
    data.filterBlock = filterBlock;
    data.dataBlock = dataBlock;
    data.macBlock = macBlock;
    return data;
  }
  
  // type: 0x5 WaterLevelDetection
  function decodeWaterLevelDetection(bytes) {
  	var data = {};
  	// type
  	data.type = "WaterLevelDetection";
  	data.waterLevel = (((bytes[1] << 8) & 0xff00) | (bytes[2] & 0xff)) + "mm";
  	return data;
  }
  
  // type: 0x8 DeviceType1
  function decodeDeviceType1(bytes) {
    var data = {
      type: "DeviceType1",
      number: bytes[0] & 0x0f,
    };
    var index = 1;
    for (let i = 0; i < data.number; i++) {
      var major = ((bytes[index] << 8) | bytes[index + 1])
        .toString(16)
        .toUpperCase()
        .padStart(4, "0");
      var minor = ((bytes[index + 2] << 8) | bytes[index + 3])
        .toString(16)
        .toUpperCase()
        .padStart(4, "0");
      var rssi = bytes[index + 4] - 256 + "dBm";
  
      data["beacon" + (i + 1)] = major + minor;
      data["rssi" + (i + 1)] = rssi;
  
      index = index + 5;
    }
  
    return data;
  }
  
  // type: 0x9 DeviceType2
  function decodeDeviceType2(bytes) {
    var data = {
      type: "DeviceType2",
      number: bytes[0] & 0x0f,
    };
    var index = 1;
    for (let i = 0; i < data.number; i++) {
      var major = ((bytes[index] << 8) | bytes[index + 1])
        .toString(16)
        .toUpperCase()
        .padStart(4, "0");
      var minor = ((bytes[index + 2] << 8) | bytes[index + 3])
        .toString(16)
        .toUpperCase()
        .padStart(4, "0");
      var rssi = bytes[index + 4] - 256 + "dBm";
  
      data["beacon" + (i + 1)] = major + minor;
      data["rssi" + (i + 1)] = rssi;
  
      index = index + 5;
    }
  
    return data;
  }
  
  // type: 0xa DeviceType3
  function decodeDeviceType3(bytes) {
    var data = {
      type: "DeviceType3",
      number: bytes[0] & 0x0f,
    };
    var index = 1;
    for (let i = 0; i < data.number; i++) {
      var major = ((bytes[index] << 8) | bytes[index + 1])
        .toString(16)
        .toUpperCase()
        .padStart(4, "0");
      var minor = ((bytes[index + 2] << 8) | bytes[index + 3])
        .toString(16)
        .toUpperCase()
        .padStart(4, "0");
      var rssi = bytes[index + 4] - 256 + "dBm";
  
      data["beacon" + (i + 1)] = major + minor;
      data["rssi" + (i + 1)] = rssi;
  
      index = index + 5;
    }
  
    return data;
  }
  
  // type: 0xe MultiDeviceTypeMessage
  function decodeMultiDeviceTypeMessage(bytes) {
    var data = {
      type: "MultiDeviceTypeMessage",
      number: bytes[0] & 0x0f,
    };
    var index = 1;
    for (let i = 0; i < data.number; i++) {
      var index = 1 + 6 * i;
      var deviceTypeId = bytes[index];
      var major = ((bytes[index + 1] << 8) | bytes[index + 2])
        .toString(16)
        .toUpperCase()
        .padStart(4, "0");
      var minor = ((bytes[index + 3] << 8) | bytes[index + 4])
        .toString(16)
        .toUpperCase()
        .padStart(4, "0");
      var rssi = bytes[index + 5] - 256 + "dBm";
  
      data["deviceTypeId" + (i + 1)] = deviceTypeId;
      data["beacon" + (i + 1)] = major + minor;
      data["rssi" + (i + 1)] = rssi;
  
      index = index + 6;
    }
  
    return data;
  }
  
  // type: 0xf Acknowledgment
  function decodeAcknowledgment(bytes) {
    var data = {};
    data.type = "Acknowledgment";
    data.result = (bytes[0] & 0x0f) == 0 ? "Success" : "Failure";
    data.msgId = (bytes[1] & 0xff).toString(16).toUpperCase();
  
    return data;
  }
  
  function byteToHex(str) {
    return str.toString(16).toUpperCase().padStart(2, "0");
  }
  
```


### Add a device on Chirpstack


1. Go to the **Applications** page and click **Add application** button.

1. Enter application name and click **Submit** button.

1. Click **Add device** button.

1. Fill in the device configuration parameters.

1. Go to the **Variables** dection, enter the "SENTIENTAccessToken" parameter, and then click the **Submit** button.

1. Enter your **Application key** in this field and click **Submit** button to save the device.


<div class="st-gallery"><figure><img src="/images/samples/lansitec/application-1.webp" alt="Go to the **Applications** page and click **Add application** button." loading="lazy"><figcaption>Go to the **Applications** page and click **Add application** button.</figcaption></figure><figure><img src="/images/samples/lansitec/application-2.webp" alt="Enter application name and click **Submit** button." loading="lazy"><figcaption>Enter application name and click **Submit** button.</figcaption></figure><figure><img src="/images/samples/lansitec/application-3.webp" alt="Click **Add device** button." loading="lazy"><figcaption>Click **Add device** button.</figcaption></figure><figure><img src="/images/samples/lansitec/application-4.webp" alt="Fill in the device configuration parameters." loading="lazy"><figcaption>Fill in the device configuration parameters.</figcaption></figure><figure><img src="/images/samples/lansitec/application-5.webp" alt="Go to the **Variables** dection, enter the &quot;SENTIENTAccessToken&quot; parameter, and then click the **Submit** button." loading="lazy"><figcaption>Go to the **Variables** dection, enter the "SENTIENTAccessToken" parameter, and then click the **Submit** button.</figcaption></figure><figure><img src="/images/samples/lansitec/application-6.webp" alt="Enter your **Application key** in this field and click **Submit** button to save the device." loading="lazy"><figcaption>Enter your **Application key** in this field and click **Submit** button to save the device.</figcaption></figure></div>


### Configure Application Integration with SENTIENT


1. Go to the **Integrations** page and click on **SENTIENT**.

1. Enter your **SENTIENT server** address and click **Submit**.


<div class="st-gallery"><figure><img src="/images/samples/lansitec/sentient-1.webp" alt="Go to the **Integrations** page and click on **SENTIENT**." loading="lazy"><figcaption>Go to the **Integrations** page and click on **SENTIENT**.</figcaption></figure><figure><img src="/images/samples/lansitec/sentient-2.webp" alt="Enter your **SENTIENT server** address and click **Submit**." loading="lazy"><figcaption>Enter your **SENTIENT server** address and click **Submit**.</figcaption></figure></div>


## Create device on SENTIENT


1. Go to the **Devices** page.

1. Click the **plus** icon to add new device.

1. Enter the device information and click "**Next: Credentials**" button.

1. Enter the **Access token** for the device and click **Add** button.

1. Click on the device to view detailed information.

1. Navigate to the **Latest telemetry** tab to view the device&#39;s reported data.


<div class="st-gallery"><figure><img src="/images/samples/lansitec/devices-1.webp" alt="Go to the **Devices** page." loading="lazy"><figcaption>Go to the **Devices** page.</figcaption></figure><figure><img src="/images/samples/lansitec/devices-2.webp" alt="Click the **plus** icon to add new device." loading="lazy"><figcaption>Click the **plus** icon to add new device.</figcaption></figure><figure><img src="/images/samples/lansitec/devices-3.webp" alt="Enter the device information and click &quot;**Next: Credentials**&quot; button." loading="lazy"><figcaption>Enter the device information and click "**Next: Credentials**" button.</figcaption></figure><figure><img src="/images/samples/lansitec/devices-4.webp" alt="Enter the **Access token** for the device and click **Add** button." loading="lazy"><figcaption>Enter the **Access token** for the device and click **Add** button.</figcaption></figure><figure><img src="/images/samples/lansitec/devices-5.webp" alt="Click on the device to view detailed information." loading="lazy"><figcaption>Click on the device to view detailed information.</figcaption></figure><figure><img src="/images/samples/lansitec/devices-6.webp" alt="Navigate to the **Latest telemetry** tab to view the device&#39;s reported data." loading="lazy"><figcaption>Navigate to the **Latest telemetry** tab to view the device&#39;s reported data.</figcaption></figure></div>


## Conclusion

With the information provided in this guide, you can easily connect your Solar Bluetooth Gateway and transmit data to SENTIENT.

For further learning about key concepts and features, explore the platform&#39;s [documentation](/docs/pe/). You can also configure [alarm rules](/docs/pe/user-guide//device-profiles/#alarm-rules) or set up [dashboards](/docs/pe/user-guide//dashboards/).
