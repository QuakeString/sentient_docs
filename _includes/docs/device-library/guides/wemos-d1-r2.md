
{% assign boardLedCount = 1 %}
{% assign deviceName = page.title | remove: "How to connect " | remove: "to SENTIENT?" %}
{% assign arduinoBoardPath="**ESP8266** > **LOLIN(WEMOS) D1 R2 & mini**" %}
{% assign prerequisites = "
- " | append: deviceName | append: "
- [Arduino IDE](https://www.arduino.cc/en/software)"
 %}

## Introduction


The WeMos D1 board, developed by WeMos company, is based on the ESP8266 ESP-12 WiFi module.  
Board programming is carried out using the standard Arduino IDE development environment.  
The controller includes a processor, peripherals, RAM and input/output devices.  
Most often, microcontrollers are used in computer equipment, household appliances and other electronic devices.  
WeMos is distinguished by its low cost and ease of connection and programming.  

{% include /docs/device-library/blocks/basic/introduction-block.md %}

## Create device on SENTIENT

{% include /docs/device-library/blocks/basic/sentient-create-device-block.md %}

## Install required libraries and tools

{% include /docs/device-library/blocks/microcontrollers/esp8266-arduino-library-install-block.md %}

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
