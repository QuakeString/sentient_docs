{% assign deviceName = page.title | remove: "How to connect " | remove: " to SENTIENT?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/contact-tracing-badge/" %}
{% assign sentientHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [LoRaWAN Gateway](https://www.lansitec.com/products/outdoor-lorawan-gateway/){:target="_blank"}
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
- [Network Server account](https://www.chirpstack.io/){:target="_blank"}
'
%}

[Contact Tracing Badge]({{deviceVendorLink}}){:target="_blank"} is designed based on Bluetooth 5.0 and LoRaWAN technology. It uses RSSI for distance measurement and contact tracing.<br>
The badge is mainly used for keeping social distance at the workplace or hospital and is especially useful during COVID-19.<br>
Proximity detection function: the badge beeps when other badges approach. The badge can use vibration and sound to alert the user even without the LoRaWAN network.<br>
NFC function is also integrated into the badge to facilitate management.

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