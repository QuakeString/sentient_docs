
{% assign boardLedCount = 0 %}
{% assign deviceName = page.title | remove: "How to connect " | remove: "to SENTIENT?" %}
{% assign arduinoBoardPath = "**ESP32** > **ESP32 Pico-D4** (Old name is ESP32 Pico Kit)" %}
{% assign prerequisites = "
- " | append: deviceName | append: "
- [Arduino IDE](https://www.arduino.cc/en/software)"
 %}

## Introduction


ESP32 PICO KIT is an ESP32-based development board produced by Espressif.  
The development board features a USB-to-UART Bridge circuit which allows developers to connect the board to a computer’s USB port for flashing and debugging.  
Official documentation is available [here](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-pico-kit-1.html).

{% include /docs/device-library/blocks/basic/introduction-block.md %}

## Create device on SENTIENT

{% include /docs/device-library/blocks/basic/sentient-create-device-block.md %}

## Install required libraries and tools

{% include /docs/device-library/blocks/microcontrollers/esp32-arduino-library-install-block.md %}

{% include /docs/device-library/blocks/microcontrollers/sentient-arduino-library-install-block.md %}

## Connect device to SENTIENT 

{% include /docs/device-library/blocks/basic/sentient-provide-device-access-token-block.md %}

{% include /docs/device-library/blocks/microcontrollers/general-code-to-program-block.md %}

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
