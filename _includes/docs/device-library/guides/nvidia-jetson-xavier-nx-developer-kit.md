{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
{% assign deviceName = page.title | remove: "How to install SENTIENT GATEWAY on " | remove: "?" %}
{% assign prerequisites = "
- " | append: deviceName | append: "
- [tb-mqtt-client library](https://pypi.org/project/tb-mqtt-client/){:target='_blank' rel='noopener'}
- [python ≥ 3.7](https://www.python.org/){:target='_blank' rel='noopener'}
- [Adafruit-Blinka](https://pypi.org/project/Adafruit-Blinka/){:target='_blank' rel='noopener'} "
  %}
{% else %}  
{% assign deviceName = page.title | remove: "How to connect " | remove: "to SENTIENT?" %}
{% assign prerequisites = "
- " | append: deviceName | append: "
- [tb-mqtt-client library](https://pypi.org/project/tb-mqtt-client/){:target='_blank' rel='noopener'}
- [python ≥ 3.7](https://www.python.org/){:target='_blank' rel='noopener'}
- [Adafruit-Blinka](https://pypi.org/project/Adafruit-Blinka/){:target='_blank' rel='noopener'} "
 %}
{% endif %}

## Introduction

The NVIDIA Jetson Xavier NX Developer Kit is a powerful, compact AI computer that delivers up to 21 TOPS of accelerated computing in a small form factor.
 It's designed for autonomous machines, industrial robots, and embedded systems that require high-performance AI at the edge.

{% include /docs/device-library/blocks/basic/introduction-block.md %}

{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
## Starting Edge on the {{deviceName}} {#starting-edge-on-device}
{% assign userName = "nvidia" %}
{% include /templates/edge/devices-library/install-edge-gw.md %}
{% endif %}

{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
## Create device on SENTIENT GATEWAY {#create-device-on-sentient-gateway}
{% else %}
## Create device on SENTIENT {#create-device-on-sentient}
{% endif %}

{% include /docs/device-library/blocks/basic/sentient-create-device-block.md %}

## Install required libraries and tools {#install-required-libraries-and-tools}

{% include /docs/device-library/blocks/single-board-computers/install-required-libraries-and-tools-block.md %}

{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
{% assign hostName = "NVIDIA_JETSON_XAVIER_NX_IP_ADDRESS" %}
## Connect device to SENTIENT GATEWAY {#connect-device-to-sentient-gateway}
{% else %}
## Connect device to SENTIENT {#connect-device-to-sentient}
{% endif %}

{% include /docs/device-library/blocks/basic/sentient-provide-device-access-token-block.md %}

{% include /docs/device-library/blocks/single-board-computers/general-code-to-program-block.md %}

## Synchronize device state using client and shared attribute requests {#synchronize-device-state-using-client-and-shared-attribute-requests}
{% include /docs/device-library/blocks/single-board-computers/sentient-synchronize-device-state-using-attribute-requests-block.md %}

{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
## Check data on SENTIENT GATEWAY {#check-data-on-sentient-gateway}
{% else %}
## Check data on SENTIENT {#check-data-on-sentient}
{% endif %}

{% include /docs/device-library/blocks/single-board-computers/check-data-on-sentient-block.md %}

## Control device using shared attributes  {#control-device-using-shared-attributes}

{% include /docs/device-library/blocks/single-board-computers/update-shared-attributes-block.md %}

## Control device using RPC {#control-device-using-rpc}

{% include /docs/device-library/blocks/single-board-computers/using-rpc-block.md %}

## Conclusion

{% include /docs/device-library/blocks/basic/conclusion-block.md %}
{% include add-device-banner.liquid %}
