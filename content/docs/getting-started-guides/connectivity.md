+++
title = "Connectivity diagram"
description = "Understand how to connect your IoT devices to SENTIENT"

aliases = ["/docs/devices-library/sensy32/"]
[extra]
status = "imported"
checked = ""
source = "docs/getting-started-guides/connectivity.md"
+++
<div class="st-callout info">


SENTIENT provides a lot of device connectivity options. The diagram below is designed to provide a visual overview of existing options and help you to choose the correct option for your devices. 
In case you have not found out how to connect your device using the diagram or something is not clear, please contact us and help us to improve this guide.


</div>


{{ diagram(name="connectivity") }}


## Connecting well-known devices

You can check the [Device Library](/docs/getting-started-guides/connectivity/) section to explore how to connect widely used devices to SENTIENT.

## Built-in transport protocols

The built-in transport protocol implementations are applicable for devices that communicate over those protocols and are able to connect directly to SENTIENT.

- [MQTT API reference](/docs/reference/mqtt-api)
- [MQTT Sparkplug API reference](/docs/reference/mqtt-sparkplug-api)
- [CoAP API reference](/docs/reference/coap-api)
- [HTTP API reference](/docs/reference/http-api)
- [LwM2M API reference](/docs/reference/lwm2m-api)
- [SNMP API reference](/docs/reference/snmp-api)

Most of the protocols above support JSON, Protobuf or own data format. This is the best option for new devices when you have control over the firmware.

## IoT Gateway

SENTIENT IoT Gateway helps to connect devices that are located in the local network and do not have access to the internet or use specific non-IP protocols.
IoT Gateway supports MQTT, OPC-UA, Modbus, BLE, HTTP, CAN, BACnet, ODBC, SNMP and other protocols.
The gateway converts the data from devices to internal SENTIENT format and upload it over MQTT to the platform.
See [What is IoT Gateway?](/docs/iot-gateway/what-is-iot-gateway/) for more info.

## LoRaWAN

It is possible to integrate ChirpStack network server with SENTIENT using this [guide](https://www.chirpstack.io/application-server/integrations/sentient/).

SENTIENT Professional Edition supports ChirpStack and many other network servers via [Integrations](/docs/user-guide/integrations/).
For example: [TheThingsStack](/docs/user-guide/integrations/ttn/), [TheThingsIndustries](/docs/user-guide/integrations/tti/),
[LORIOT](/docs/user-guide/integrations/loriot/),
[Actility ThingPark](/docs/user-guide/integrations/thingpark/) or any other network server that supports the [webhooks](/docs/user-guide/integrations/http/) or [mqtt](/docs/user-guide/integrations/mqtt/).
Big advantage of SENTIENT Professional Edition integrations is the ability to define custom [data converter](/docs/user-guide/integrations/#data-converters) functions.

## Sigfox

SENTIENT Professional Edition supports Sigfox [integration](/docs/user-guide/integrations/sigfox/) out-of-the-box.

## NB IoT and other protocols

SENTIENT Professional Edition supports many [Integrations](/docs/user-guide/integrations/) that cover most of the devices on the market.
Please contact us if you need help to connect your device.
