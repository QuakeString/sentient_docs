{% assign deviceName = page.title | remove: "How to connect " | remove: " to SENTIENT?" %}
{% assign deviceVendorLink = "https://www.lansitec.com/products/cat-1-badge-tracker/" %}
{% assign sentientHost = "https://" | append: hostName %}
{% assign prerequisites = '
- <a href="' | append: deviceVendorLink | append: '" target="_blank">' | append: deviceName | append: '</a>
- [Bluetooth Beacon](https://www.lansitec.com/products/bluetooth-beacon/){:target="_blank"}
'
%}

[Cat-1 Badge Tracker]({{deviceVendorLink}}){:target="_blank"} is designed based on GNSS, Bluetooth 5.0, and Cat-1 technology.<br>
It supports indoor and outdoor tracking. The badge is mainly used for personnel and asset management.<br> 
The build-in 3-axis accelerator could be used for determining the motion status of the terminal to help save battery life and enhance user experience.<br>

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