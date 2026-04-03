{% assign deviceName = page.title | remove: "How to connect " | remove: " to SENTIENT?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/tracking-label/" %}
{% assign sentientHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [LoRaWAN Gateway](https://www.lansitec.com/products/outdoor-lorawan-gateway/){:target="_blank"}
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
- [Network Server account](https://www.chirpstack.io/){:target="_blank"}
'
%}

[Tracking Label]({{deviceVendorLink}}){:target="_blank"} say goodbye to lost shipments and untraceable assets with Lansitec&#39;s ultra-thin Tracking Label. Combining GNSS, Bluetooth 5.0, and LoRaWAN technology, this disposable tracking solution provides reliable indoor and outdoor positioning for packages, pallets, and containers.<br>
Whether you&#39;re shipping goods across the globe or simply managing inventory within a warehouse, the Tracking Label&#39;s 3-axis accelerometer and automatic BLE/GNSS switching ensure efficient power use without compromising on accuracy.<br>
With up to three years of battery life (based on six GNSS reports per day) and an IP66 rating, this label is built to stand up to harsh conditions and lengthy transit times — giving you the confidence to monitor and manage your assets from end to end.

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
