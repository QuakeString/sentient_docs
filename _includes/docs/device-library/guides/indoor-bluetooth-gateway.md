{% assign deviceName = page.title | remove: "How to connect " | remove: " to SENTIENT?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/indoor-bluetooth-gateway/" %}
{% assign sentientHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [LoRaWAN Gateway](https://www.lansitec.com/products/outdoor-lorawan-gateway/){:target="_blank"}
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
- [Network Server account](https://www.chirpstack.io/){:target="_blank"}
'
%}

[Indoor Bluetooth Gateway]({{deviceVendorLink}}){:target="_blank"} is based on Bluetooth 5.0 technology and LoRaWAN.<br>
It receives nearby [Bluetooth beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"} messages and transmits them to the server through LoRaWAN. With LoRaWAN technology, there is no network usage fee for long-distance transmission.<br><br>

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
