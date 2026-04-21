---
layout: docwithnav-pe-mqtt-broker
assignees:
- stitenko
title: Integration with SENTIENT
description: Integration guide of ST-RMQTT with SENTIENT

create-client-credentials:
    0:
        image: /images/pe/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-add-client-credentials-1-pe.png
        title: 'Navigate to "Credentials" tab, click on the "plus" icon in the top right corner of the table;'
    1:
        image: /images/pe/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-add-client-credentials-2-pe.png
        title: 'Input client credentials name, select client type. Enable "Basic" authentication type.'
    2:
        image: /images/pe/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-add-client-credentials-3-pe.png
        title: 'Input "Username" and "Password" with chosen values. For example, use `tb-pe` value for Username and `secret` for Password fields. Click "Add" to save credentials.'
    3:
        image: /images/pe/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-add-client-credentials-4-pe.png
        title: 'New client credential is created.'

create-uplink-converter:
    0:
        image: /images/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-uplink-converter-tbel-1-pe.png

create-integration:
    0:
        image: /images/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-integration-add-integration-1-pe.png
        title: 'Go to the "Integrations center" section -> "Integrations" page and click "plus" icon to add a new integration. Name it "MQTT Integration", select type "MQTT";'
    1:
        image: /images/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-integration-add-integration-2-pe.png
        title: 'Add the recently created uplink converter;'
    2:
        image: /images/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-integration-add-integration-3-pe.png
        title: 'Leave the "Downlink data converter" field empty. Click "Skip";'
    3:
        image: /images/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-integration-add-integration-4-pe.png
        title: 'Specify host and port of ST-RMQTT instance. Select "Basic" credentials type and specify ST-RMQTT client credentials. Add a topic filter: "tb/mqtt-integration-tutorial/sensors/+/temperature" and select an MQTT QoS level higher than 0;'
    4:
        image: /images/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-integration-add-integration-5-pe.png
        title: 'Now go to the advanced settings. Uncheck the "Clean session" parameter and specify client ID as `tbpeintegration`;'
    5:
        image: /images/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-integration-add-integration-6-pe.png
        title: '[Optional] Click on Check connection button to check connection to ST-RMQTT. Click Add button to create the integration.'

successful-connection-st-rmqtt-to-sentient:
    0:
        image: /images/pe/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-sessions-1-pe.png
        title: 'Go to the "Sessions" page in the ST-RMQTT UI. Upon successful establishment of the connection SENTIENT to ST-RMQTT, we will see a new session and its status - "Connected".'

st-rmqtt-home-page:
    0:
        image: /images/pe/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-home-page-1-pe.png
        title: 'On the "Topics" page you will see a name of Kafka topic (which corresponds to the client ID specified in the MQTT integration), number of partitions, replication factor and size of the topic.'

st-rmqtt-create-device:
    0:
        image: /images/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-create-device-1-pe.png

st-rmqtt-integration-events:
    0:
        image: /images/mqtt-broker/user-guide/integrations/how-to-connect-tbqm-to-sentient/st-rmqtt-integration-events-1-pe.png

---

{% assign docsPrefix = "pe/" %}
{% include /docs/mqtt-broker/user-guide/integrations/how-to-connect-sentient-to-st-rmqtt.md %}
