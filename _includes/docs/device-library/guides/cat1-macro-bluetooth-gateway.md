{% assign deviceName = page.title | remove: "How to connect " | remove: " to SENTIENT?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/cat-1-macro-bluetooth-gateway/" %}
{% assign sentientHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
'
%}

[Cat-1 Macro Bluetooth Gateway]({{deviceVendorLink}}){:target="_blank"} receives data from nearby Bluetooth beacons, sensors, or controllers, restructures it, and forwards it to a server via Cat-1 connectivity.<br>
It supports iBeacon, Eddystone, private protocols, and both scan and response features.<br>
Powered by a 38,000 mAh low-discharge-rate battery, the gateway offers a battery life of over 5 years.<br>

## Prerequisites

To continue with this guide we will need the following:
{{prerequisites}}
- [SENTIENT account]({{ sentientHost }}){: target="_blank"}


## Configuration

You will need to have access to SENTIENT Professional Edition. The easiest way is to use [SENTIENT Cloud](https://sentient.invenia.in/installations/choose-region/){:target="_blank"} server.
The alternative option is to install SENTIENT using [installation guide](/docs/user-guide/install/pe/installation-options/){:target="_blank"}.

{% include /docs/device-library/blocks/integrations/external-platforms/lansitec/cat1/create-device-on-sentient.md %}

{% include /docs/device-library/blocks/integrations/external-platforms/lansitec/cat1/check-data-on-sentient-cat-1-block.md %}

{% include /docs/device-library/blocks/integrations/external-platforms/lansitec/cat1/conclusion-cat-1-block.md %}
{% include add-device-banner.liquid %}