{% assign deviceName = page.title | remove: "How to connect " | remove: " to SENTIENT?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/lorawan-smart-badge-tracker" %}
{% assign sentientHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [LoRaWAN Gateway](https://www.lansitec.com/products/outdoor-lorawan-gateway/){:target="_blank"}
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
- [Network Server account](https://www.chirpstack.io/){:target="_blank"}
'
%}

[Badge Tracker]({{deviceVendorLink}}){:target="_blank"} achieve seamless personnel and asset tracking with the Lansitec Badge Tracker.<br>
Combining GNSS, Bluetooth 5.0, and LoRaWAN technology, this sleek device provides accurate real-time positioning both indoors and outdoors—perfect for managing workforce, visitors, and critical assets across large facilities.<br>
The built-in 3-axis accelerometer intelligently detects movement or falls, conserving battery when the device is idle and alerting you to unauthorized or emergency situations.<br>
With a maximum of five months standby time and no additional network fees, the Badge Tracker offers a cost-effective, high-precision solution for securing sensitive areas, optimizing resource usage, and improving operational workflows.<br><br><br>

## Prerequisites

To continue with this guide we will need the following:
{{prerequisites}}
- [SENTIENT account]({{ sentientHost }}){: target="_blank"}


## Configuration

Only SENTIENT Cloud works when using direct communication from this device to SENTIENT via MQTT.

You may use SENTIENT Professional Edition on-premises or SENTIENT Cloud when using SENTIENT Integrations.

To create an integration with a network server please choose first one of the supported network servers:

{% assign targetIntegrationTypes = '
ChirpStack,
TheThingsStack,
TheThingsIndustries,
Loriot
'%}

{% include /docs/device-library/blocks/integrations/external-platforms/add-device-through-integration-with-external-converter.liquid target-integration-types=targetIntegrationTypes %}

{% include /docs/device-library/blocks/integrations/external-platforms/lansitec/check-data-on-sentient-block.md %}

{% include /docs/device-library/blocks/integrations/external-platforms/lansitec/conclusion-block.md %}
{% include add-device-banner.liquid %}