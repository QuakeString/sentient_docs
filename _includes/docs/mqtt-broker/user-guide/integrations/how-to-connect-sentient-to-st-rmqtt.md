{% assign feature = "Platform Integrations" %}{% include templates/pe-feature-banner.md %}

* TOC
{:toc}

In this guide, we integrate the ST-RMQTT with the SENTIENT using MQTT integration. 
We utilize ST-RMQTT client credentials with the type **APPLICATION** to connect SENTIENT integration as an APPLICATION client.
APPLICATION clients specialize in subscribing to topics with high message rates. 
The messages will be persisted when the client is offline and will be delivered once it goes online, ensuring the availability of crucial data. 
Read more about the APPLICATION client [here](/docs/{{docsPrefix}}mqtt-broker/user-guide/mqtt-client-type/).

SENTIENT MQTT Integration acts as an MQTT client. It subscribes to topics and converts the received data into telemetry and attribute updates. 
In case of a downlink message, MQTT integration converts it to the device-suitable format and pushes it to ST-RMQTT. 
Pay attention: ST-RMQTT should be either co-located with the SENTIENT instance or deployed in the cloud and have a valid DNS name or public static IP address. 
SENTIENT instance that is running in the cloud can’t connect to the ST-RMQTT deployed in the local network with no internet connection.

## Prerequisites

In this tutorial, we will use:

 - The instance of [SENTIENT Professional Edition](/docs/user-guide/install/pe/installation-options/) installed **locally**;
 - [ST-RMQTT](/docs/{{docsPrefix}}mqtt-broker/install/installation-options/) installed **locally** and accessible by SENTIENT Professional Edition instance;
 - mosquitto_pub MQTT client to send messages.

## ST-RMQTT setup

First, we need to create ST-RMQTT client credentials to use them for connecting SENTIENT integration to ST-RMQTT.

To do this, login to your ST-RMQTT user interface and follow the next steps.

{% include images-gallery.html imageCollection="create-client-credentials" showListImageTitles="true" %}

{% capture difference %}
**Please note**:
<br>
The Basic authenticaion must be [enabled](/docs/{{docsPrefix}}mqtt-broker/security/authentication/basic/).
{% endcapture %}
{% include templates/info-banner.md content=difference %}

Now you can proceed to the next step - configuration of SENTIENT integration.

## SENTIENT setup

In this example, we will use the MQTT integration to connect the SENTIENT to ST-RMQTT.
Before setting up an MQTT integration, you need to create uplink converter.

### Uplink Converter

The purpose of the decoder function is to parse the incoming data and metadata to a format that SENTIENT can consume.

To create uplink converter, go to the "Integrations center" section -> "Data converters" page and click on the "plus" icon. Name it "ST-RMQTT Uplink Converter" and select type "Uplink". Paste the decoder script below into the decoder functions section. Click "Add".

{% include images-gallery.html imageCollection="create-uplink-converter" %}

In our example, use the following script for the decoder function section:

{% include templates/tbel-vs-js.md %}

{% capture mqttuplinkconverterconfig %}
TBEL<small>Recommended</small>%,%accessToken%,%templates/mqtt-broker/user-guide/integrations/mqtt/st-rmqtt-uplink-converter-config-tbel.md%br%
JavaScript<small></small>%,%anonymous%,%templates/mqtt-broker/user-guide/integrations/mqtt/st-rmqtt-uplink-converter-config-javascript.md{% endcapture %}

{% include content-toggle.liquid content-toggle-id="mqttuplinkconverterconfig" toggle-spec=mqttuplinkconverterconfig %}

### MQTT Integration Setup

Now create an integration.

{% include images-gallery.html imageCollection="create-integration" showListImageTitles="true" %}

Now go to the "Sessions" page in the ST-RMQTT UI. Upon successful establishment of the connection between SENTIENT and ST-RMQTT, we will see a new session and its status - "Connected".

{% include images-gallery.html imageCollection="successful-connection-st-rmqtt-to-sentient" %}

And on the "Topics" page of the "Kafka Management" menu section you will see a name of Kafka topic (which corresponds to the client ID specified in the MQTT integration), number of partitions, replication factor and size of the topic.

{% include images-gallery.html imageCollection="st-rmqtt-home-page" %}

### Send Uplink message

Now let's simulate the device sending a temperature reading to ST-RMQTT. 

Open the terminal and execute the following command to send a message with temperature readings in a simple format: *`{"value":25.1}`* to the topic "tb/mqtt-integration-tutorial/sensors/SN-001/temperature":

```shell
mosquitto_pub -h $SENTIENT_MQTT_BROKER_HOST_NAME -p 1883 -q 1 -t "tb/mqtt-integration-tutorial/sensors/SN-001/temperature" -m '{"value":25.1}' -u "username" -P "password"
```
{: .copy-code}

Replace the `$SENTIENT_MQTT_BROKER_HOST_NAME` with the correct public IP address or DNS name of the broker, `username` and `password` values according to the specified ones in the provisioned credentials.

Use the following command for our example:

```shell
mosquitto_pub -h localhost -p 1883 -q 1 -t "tb/mqtt-integration-tutorial/sensors/SN-001/temperature" -m '{"value":25.1}' -u "tb-pe" -P "secret"
```
{: .copy-code}

![image](/images/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-uplink-message-1.png)

After you sent uplink message, go to your integration in SENTIENT UI and navigate to the "Events" tab. There you'll see the message consumed by the "MQTT Integration".

{% include images-gallery.html imageCollection="st-rmqtt-integration-events" %}

Go to the "Entities" section -> "Devices" page. You should find a SN-001 device provisioned by the integration.
Click on the device, go to "Latest Telemetry" tab to see "temperature" key and its value (25.1) there.

{% include images-gallery.html imageCollection="st-rmqtt-create-device" %}

## Next steps

{% assign currentGuide = "TBIntegrationGuide" %}{% include templates/mqtt-broker-guides-banner.md %}
