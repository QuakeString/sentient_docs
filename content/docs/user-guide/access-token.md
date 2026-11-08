+++
title = "Access Token based authentication for MQTT"
description = "SENTIENT Access Token based authentication."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/access-token.md"
+++
Access Token based authentication is the default device authentication type.
The unique access token is generated once the device is created in SENTIENT. It can be changed afterwards.
The client must specify the access token as a username in MQTT connect message.

## Plain MQTT (without SSL)

Let's review a simple command to upload temperature readings using Access Token *YOUR_ACCESS_TOKEN* to SENTIENT Cloud.
See [MQTT API](/docs/reference/mqtt-api/) for more details. The command is using plain MQTT without TLS:

```bash
mosquitto_pub -d -q 1 -h "YOUR_SENTIENT_HOST" -p "1883" \ 
-t "v1/devices/me/telemetry" -u "YOUR_ACCESS_TOKEN" -m {"temperature":25}
```


The above command requires mosquitto clients library that you can install using the following command: **apt-get install mosquitto-clients**.
Don't forget to replace **YOUR_SENTIENT_HOST** with the host of your SENTIENT instance and **YOUR_ACCESS_TOKEN** with the access token of your device.

## MQTTS (MQTT over SSL)

One-way SSL authentication is a standard authentication mode, where your client device verifies the identity of a server using server certificate.


Follow the [MQTT over SSL](/docs/user-guide/mqtt-over-ssl/) guide to provision server certificate if you are hosting your own SENTIENT instance.


Once provisioned, you should prepare a CA root certificate in pem format. This certificate will be used by mqtt client to validate the server certificate.
Save the CA root certificate to your working directory as "**ca-root.pem**".
An example of CA root certificate for *localhost* is located [here](/docs/user-guide/resources/mqtt-over-ssl/ca-root.pem).

Now you may use the *ca-root.pem* to setup secure connection to your SENTIENT instance (*YOUR_SENTIENT_HOST*) and Access Token (*YOUR_ACCESS_TOKEN*) to authenticate the device to upload telemetry:

```bash
mosquitto_pub --cafile ca-root.pem -d -q 1 -h "YOUR_SENTIENT_HOST" -p "8883" \
-t "v1/devices/me/telemetry" -u "YOUR_ACCESS_TOKEN" -m {"temperature":25}
```


The above command requires mosquitto clients library that you can install using the following command: **apt-get install mosquitto-clients**.
Don't forget to replace **YOUR_SENTIENT_HOST** with the host of your SENTIENT instance and **YOUR_ACCESS_TOKEN** with the access token of your device.
