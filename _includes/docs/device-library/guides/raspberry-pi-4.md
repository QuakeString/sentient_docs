{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
{% assign deviceName = page.title | remove: "How to install SENTIENT Edge on " | remove: "?" %}
{% assign prerequisites = "
- [" | append: deviceName | append: "](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/){:target='_blank' rel='noopener'}
- [tb-mqtt-client library](https://pypi.org/project/tb-mqtt-client/){:target='_blank' rel='noopener'}
- [python ≥ 3.7](https://www.python.org/){:target='_blank' rel='noopener'}
- [Adafruit-Blinka](https://pypi.org/project/Adafruit-Blinka/){:target='_blank' rel='noopener'} "
 %}
{% else %}  
{% assign deviceName = page.title | remove: "How to connect " | remove: "to SENTIENT?" %}
{% assign prerequisites = "
- [" | append: deviceName | append: "](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/){:target='_blank' rel='noopener'}
- [tb-mqtt-client library](https://pypi.org/project/tb-mqtt-client/){:target='_blank' rel='noopener'}
- [python ≥ 3.7](https://www.python.org/){:target='_blank' rel='noopener'}
- [Adafruit-Blinka](https://pypi.org/project/Adafruit-Blinka/){:target='_blank' rel='noopener'} "
 %}
{% endif %}

## Introduction
Raspberry Pi has long been the gold standard for inexpensive single-board computing, powering everything from robots to
smart home devices to digital kiosks. When it launched in 2019, the Raspberry Pi 4 took Pi to another level, with
performance that’s good enough to use in a pinch as a desktop PC, plus the ability to output 4K video at 60 Hz or power
dual monitors. More recently, the Raspberry Pi 4 (8GB) model came out, offering enough RAM for serious desktop computing,
productivity and database hosting.

{% include /docs/device-library/blocks/basic/introduction-block.md %}

{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
## Starting Edge on the {{deviceName}} {#starting-edge-on-device}
{% assign userName = "pi" %}
{% include /templates/edge/devices-library/install-edge-gw.md %}
{% endif %}

{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
## Create device on SENTIENT Edge {#create-device-on-sentient-gateway}
{% else %}
## Create device on SENTIENT {#create-device-on-sentient}
{% endif %}

{% include /docs/device-library/blocks/basic/sentient-create-device-block.md %}

## Install required libraries and tools {#install-required-libraries-and-tools}

{% include /docs/device-library/blocks/single-board-computers/install-required-libraries-and-tools-block.md %}

{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
{% assign hostName = "RPi_4_IP_ADDRESS" %}
## Connect device to SENTIENT Edge {#connect-device-to-sentient-gateway}
{% else %}
## Connect device to SENTIENT {#connect-device-to-sentient}
{% endif %}

{% include /docs/device-library/blocks/basic/sentient-provide-device-access-token-block.md %}

{% include /docs/device-library/blocks/single-board-computers/general-code-to-program-block.md %}

## Synchronize device state using client and shared attribute requests {#synchronize-device-state-using-client-and-shared-attribute-requests}

{% include /docs/device-library/blocks/single-board-computers/sentient-synchronize-device-state-using-attribute-requests-block.md %}

{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
## Check data on SENTIENT Edge {#check-data-on-sentient-gateway}
{% else %}
## Check data on SENTIENT {#check-data-on-sentient}
{% endif %}

{% include /docs/device-library/blocks/single-board-computers/check-data-on-sentient-block.md %}

## Control device using shared attributes {#control-device-using-shared-attributes}

{% include /docs/device-library/blocks/single-board-computers/update-shared-attributes-block.md %}

## Control device using RPC {#control-device-using-rpc}

{% include /docs/device-library/blocks/single-board-computers/using-rpc-block.md %}

## Conclusion

{% include /docs/device-library/blocks/basic/conclusion-block.md %}
{% include add-device-banner.liquid %}
