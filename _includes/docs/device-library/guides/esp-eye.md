{% assign boardLedCount = 1 %}
{% assign hasCamera = "true" %}
{% assign deviceName = page.title | remove: "How to connect " | remove: "to SENTIENT?" %}
{% assign arduinoBoardPath = "**M5Stack** > **M5TimerCAM**" %}
{% assign prerequisites = "
- " | append: deviceName | append: "
- [Arduino IDE](https://www.arduino.cc/en/software)"
 %}

## Introduction

[ESP-EYE](https://www.espressif.com/en/products/devkits/esp-eye/overview) is a development board for image recognition and audio processing, which can be used in various AIoT applications.  
It features an ESP32 chip, a 2-Megapixel camera and a microphone. ESP-EYE offers plenty of storage, with an 8 Mbyte PSRAM and a 4 Mbyte flash.  
It also supports image transmission via Wi-Fi and debugging through a Micro-USB port.

{% include /docs/device-library/blocks/basic/introduction-block.md %}

## Create device on SENTIENT

{% include /docs/device-library/blocks/basic/sentient-create-device-block.md %}

## Install required libraries and tools

{% include /docs/device-library/blocks/microcontrollers/esp32-arduino-library-install-block.md %}

{% include /docs/device-library/blocks/microcontrollers/sentient-arduino-library-install-block.md %}

## Connect device to SENTIENT 

{% include /docs/device-library/blocks/basic/sentient-provide-device-access-token-block.md %}

{% include /docs/device-library/blocks/microcontrollers/camera-code-to-program-block.md %}

## Check data on SENTIENT

{% include /docs/device-library/blocks/basic/sentient-upload-example-dashboard.md %}

{% include /docs/device-library/blocks/microcontrollers/sentient-check-example-data-block.md %}

## Synchronize device state using client and shared attribute requests

{% include /docs/device-library/blocks/microcontrollers/sentient-synchronize-device-state-using-attribute-requests-block.md %}

## Control device using shared attributes

{% include /docs/device-library/blocks/microcontrollers/sentient-update-shared-attributes-device-block.md %}

## Control device using RPC

{% include /docs/device-library/blocks/microcontrollers/sentient-send-rpc-to-device-block.md %}

## Conclusion

 {% include /docs/device-library/blocks/basic/conclusion-block.md %} 
{% include add-device-banner.liquid %}