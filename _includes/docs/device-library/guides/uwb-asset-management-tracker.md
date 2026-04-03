{% assign deviceName = page.title | remove: "How to connect " | remove: " to SENTIENT?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/uwb-asset-management-tracker/" %}
{% assign sentientHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [LoRaWAN Gateway](https://www.lansitec.com/products/outdoor-lorawan-gateway/){:target="_blank"}
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
- [Network Server account](https://www.chirpstack.io/){:target="_blank"}
'
%}

[UWB Asset Management Tracker]({{deviceVendorLink}}){:target="_blank"} is designed using LoRaWAN and UWB technologies.<br>
It calculates the distance with anchors and forward the distance information to a LoRaWAN gateway to calculate its position in the server. The accuracy can be as low as 10cm.<br>

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
' %}

{% include /docs/device-library/blocks/integrations/external-platforms/add-device-through-integration-with-external-converter.liquid target-integration-types=targetIntegrationTypes %}

{% include /docs/device-library/blocks/integrations/external-platforms/lansitec/check-data-on-sentient-block.md %}

{% include /docs/device-library/blocks/integrations/external-platforms/lansitec/conclusion-block.md %}
{% include add-device-banner.liquid %}
