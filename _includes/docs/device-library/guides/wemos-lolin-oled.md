
{% assign hasDisplay = "true" %}
{% assign deviceName = page.title | remove: "How to connect " | remove: "to SENTIENT?" %}
{% assign arduinoBoardPath = "**ESP32** > **WEMOS LOLIN32**" %}
{% assign OLEDInstallationRequired = "true" %}
{% assign prerequisites = "
- " | append: deviceName | append: "
- [Arduino IDE](https://www.arduino.cc/en/software)"
 %}

## Introduction


{{deviceName}} is an ESP32 development board with a built-in 128×64 pixels SSD1306 OLED display.  
The display communicates with the ESP32 via I2C communication protocol.  
ESP32 has integrated antenna and power amplifier, low noise amplifier, filter and supply management module.

{% include /docs/device-library/blocks/basic/introduction-block.md %}

## Create device on SENTIENT

{% include /docs/device-library/blocks/basic/sentient-create-device-block.md %}

## Install required libraries and tools

{% include /docs/device-library/blocks/microcontrollers/esp32-arduino-library-install-block.md %}

{% include /docs/device-library/blocks/microcontrollers/sentient-arduino-library-install-block.md %}

## Connect device to SENTIENT 

{% include /docs/device-library/blocks/basic/sentient-provide-device-access-token-block.md %}

{% include /docs/device-library/blocks/microcontrollers/oled-example-code-to-program-block.md %}

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