+++
title = "Over-the-air firmware and software updates"
description = "IoT device firmware updates"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ota-updates.md"
+++
## Overview

Since SENTIENT 3.3, SENTIENT allows you to upload and distribute over-the-air(OTA) updates to devices. 
As a tenant administrator, you may upload firmware or software packages to the OTA repository. 
Once uploaded, you may assign them to [Device Profile](/docs/user-guide/device-profiles/) or [Device](/docs/user-guide/ui/devices/). 
SENTIENT will notify devices about the available update and provide a protocol-specific API to download the firmware. 
The platform tracks status of the update and stores history of the updates. 
As a platform user, you may monitor the update process using the dashboard.
<br>
<object data="/images/user-guide/firmware/firmware-anim3.svg"></object>
<br>

## Provision OTA package to SENTIENT repository

Navigate to the "OTA Updates" menu item to list and upload OTA update packages. Each package consist of:

* Title - the name of your package. You can use different names for production and debug firmware/software. 
* Version - the version of your package. Combination of the title and version must be unique in scope of a tenant.
* Device Profile - each package is compatible with one device profile. We track compatibility to prevent accidental updates of devices with incompatible firmware/software. 
  Link to a device profile means that device that use this profile *may* be updated to the current package. 
  However, the update is not triggered, until the user or script [assigns](#assign-ota-package-to-device-profile) the package to the device profile or device.
* Type - can be either *Firmware* or *Software*.    
* Checksum algorithm - optional parameter, it is a short name of the checksum algorithm to use. 
* Checksum - optional parameter, it's a value of the file checksum. If no checksum provided by the user, server will use SHA-256 algorithm automatically.
* Description - optional text description of the firmware. 


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/add-firmware-ce.webp" alt="You have to enter title and version; select type and device profile (this field we define what type of device this firmware will be available; choose file contains firmware. Optionally add checksum algorithm and checksum." loading="lazy"><figcaption>You have to enter title and version; select type and device profile (this field we define what type of device this firmware will be available; choose file contains firmware. Optionally add checksum algorithm and checksum.</figcaption></figure></div>


You can browse the provisioned packages as well as search them by title. Also, you are able to download and delete packages.
To open package details, click the table row. Package details allow you to copy package ID and checksum. 
Also, [Audit logs](/docs/user-guide/audit-log/) track information about users who provisioned the firmware.


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/list-firmware-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/firmware/list-firmware-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/firmware/list-firmware-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/firmware/list-firmware-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


All actions listed are also available via [REST API](/docs/reference/rest-api/).

## Firmware vs Software

There is a very minor difference between FOTA and SOTA implementation inside SENTIENT core. Many use-cases and applications will need to use FOTA only. 
However, [LwM2M](/docs/reference/lwm2m-api/) devices process FOTA and SOTA updates differently. 

## Assign OTA package to device profile

You may assign firmware/software to the device profile to automatically distribute the package to all devices that share the same profile. See screenshots below.


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/fw-deviceprofile-ce.webp" alt="Go to the Device profile page and open needed device profile details to edit its information." loading="lazy"><figcaption>Go to the Device profile page and open needed device profile details to edit its information.</figcaption></figure><figure><img src="/images/user-guide/firmware/fw-deviceprofile-1-ce.webp" alt="From the drop-down menu select firmware that you&#39;d like to assign to this device profile." loading="lazy"><figcaption>From the drop-down menu select firmware that you&#39;d like to assign to this device profile.</figcaption></figure><figure><img src="/images/user-guide/firmware/fw-deviceprofile-2-ce.webp" alt="After selecting firmware, apply changes by clicking the orange check mark in the right corner of the page." loading="lazy"><figcaption>After selecting firmware, apply changes by clicking the orange check mark in the right corner of the page.</figcaption></figure></div>


The device profile details will let you choose only compatible OTA update packages (see [provisioning](#provision-ota-package-to-sentient-repository) for more info).
Device profile may be used by thousands of devices. Assignment of the firmware/software triggers the [update process](#update-process).


## Assign OTA package to device

You may also assign firmware/software to specific device. See screenshots below.


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/device-firmware-ce.webp" alt="Go to the Device page and open needed device details to edit its information." loading="lazy"><figcaption>Go to the Device page and open needed device details to edit its information.</figcaption></figure><figure><img src="/images/user-guide/firmware/device-firmware-1-ce.webp" alt="From the drop-down menu select firmware that you&#39;d like to assign to this device." loading="lazy"><figcaption>From the drop-down menu select firmware that you&#39;d like to assign to this device.</figcaption></figure><figure><img src="/images/user-guide/firmware/device-firmware-2-ce.webp" alt="After selecting firmware, apply changes by clicking the orange check mark in the right corner of the page." loading="lazy"><figcaption>After selecting firmware, apply changes by clicking the orange check mark in the right corner of the page.</figcaption></figure><figure><img src="/images/user-guide/firmware/device-firmware-3-ce.webp" alt="." loading="lazy"><figcaption>.</figcaption></figure></div>


The firmware version assigned to the device will automatically overwrite firmware version that is assigned to the device profile. 

For example, let's assume you have Devices D1 and D2 that has Profile P1:

* If you assign package F1 to Profile P1 (via [profile details UI](/docs/user-guide/ota-updates/#assign-ota-package-to-device-profile) or REST API), Devices D1 and D2 will be updated to F1. 
* If you assign package F2 to Device D1 (via [device details UI](/docs/user-guide/ota-updates/#assign-ota-package-to-device) or REST API), Device D1 will be updated to F2.
* Subsequent assignment of the package F3 to the Profile P1 will affect only D2, since it has no specific firmware version assigned on the device level.
So, D2 will be updated to F3, while D1 will continue to use F2.


Customers may choose available firmware and assign it to the devices that belong to them. However, customers can't provision or manage firmware packages.


<div class="st-callout info">


Deletion of the firmware packages that is assigned to at least one device or device profile is prohibited.


</div>


## Update process

Assignment of the firmware/software to the device or device profile triggers the update process.
SENTIENT tracks the progress of the update and persists it to the device attributes.

Update progress may have one of the following states. The state of the update is stored as an attribute of the device and is used to visualize the update process on the [dashboard](#dashboard).

### QUEUED state

The very first state of the firmware/software update. 
Means that the notification about new firmware/software is queued but not yet pushed to the device. 
SENTIENT queues the update notifications to avoid peak loads. The queue is processed with the constant pace. 
By default, it is configured to notify up to 100 device per minute. See [configuration properties](/docs/user-guide/ota-updates/#queue-processing-pace) for more details.
   
### INITIATED state

Means that the notification about firmware/software is fetched from queue and pushed to device.
Under the hood, SENTIENT converts notification to the update of the following [shared attributes](/docs/user-guide/attributes/#shared-attributes):

- fw(sf)_title - name of the firmware (software).
- fw(sf)_version - version of the firmware (software).
- fw(sf)_size - size of the firmware (software) file in bytes.
- fw(sf)_checksum - attribute that is used to verify integrity of the received file.
- fw(sf)_checksum_algorithm - the algorithm used to calculate file checksum.


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/fw-attributes-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Device is able to subscribe to shared attribute update using [MQTT](/docs/reference/mqtt-api/), 
[HTTP](/docs/reference/http-api/), [CoAP](/docs/reference/coap-api/) or [LwM2M](/docs/reference/lwm2m-api/) API.

### Update states reported by the device

The remaining states are reported by the device firmware/software that is currently processing the update. 
We have prepared description of those states and sample applications for the most popular protocols written in python. 
Sample applications simulate behavior of the device firmware/software and may used as a reference for the implementation.  

 * DOWNLOADING - notification about new firmware/software update was received and device started downloading the update package.
 * DOWNLOADED - device completed downloading of the update package.
 * VERIFIED - device verified the checksum of the downloaded package.
 * UPDATING - device started the firmware/software update. Typically is sent before reboot of the device or restart of the service. 
 * UPDATED - the firmware was successfully updated to the next version.
 * FAILED - checksum wasn't verified, or the device failed to update. See "Device failed" tab on the Firmware dashboard for more details.


Once the firmware/software is updated, SENTIENT expect the device to send the following telemetry:

for firmware:
```json
{"current_fw_title": "myFirmware", "current_fw_version": "1.2.3", "fw_state": "UPDATED"}
```

for software:
```json
{"current_sw_title": "mySoftware", "current_sw_version": "1.2.3", "sw_state": "UPDATED"}
```

If the firmware/software update failed, SENTIENT expect the device to send the following telemetry:

for firmware:
```json
{"fw_state": "FAILED", "fw_error":  "the human readable message about the cause of the error"}
```

for software:
```json
{"sw_state": "FAILED", "sw_error":  "the human readable message about the cause of the error"}
```


<div class="st-tabs">

<div class="st-tab" data-label="HTTP">


Execute the following command in terminal to install the HTTP and checksum libs:

```bash
pip3 install requests mmh3 --user
```


Enter the path to the client's folder in terminal and execute the following command for SENTIENT
to get firmware example script:

```bash
python3 http_firmware_client.py 
```


Download HTTP client example: [**http_firmware_client.py**](/docs/user-guide/resources/firmware/http_firmware_client.py)

After getting the following messages
- `Please write your SENTIENT host or leave it blank to use default (localhost):` - use your localhost, or the platform address;
- `Please write your SENTIENT port or leave it blank to use default (8080):` - you can just continue by pressing "enter", or 
input your port number;
- `Please write accessToken for device:` - copy device accessToken from SENTIENT and paste it into the terminal;
- `Please write firmware chunk size in bytes or leave it blank to get all firmware by request:` - if you leave it blank, the file will be downloaded at once
in the full size. If you want to download in parts, enter the size of the chunk.


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/fw-http-updated.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Firmware of the device is updated. To see its status, you should go to the firmware dashboard as it shows in the following paragraph.

To find out about the firmware update, you need to [make a request and subscribe to attributes](/docs/reference/http-api/#firmware-api).


</div>

<div class="st-tab" data-label="MQTT">


After, you should execute the following command to install the MQTT and checksum libs:

```bash
pip3 install paho-mqtt mmh3 --user
```


Enter the path to the client's folder and execute the following command for SENTIENT to get firmware example script:

```bash
python3 mqtt_firmware_client.py 
```


Download MQTT client example: [**mqtt_firmware_client.py**](/docs/user-guide/resources/firmware/mqtt_firmware_client.py)

After getting the following messages, 
- `Please write your SENTIENT host or leave it blank to use default (localhost):` - use your localhost, or the platform address;
- `Please write your SENTIENT port or leave it blank to use default (1883):` - you can just continue by pressing "enter", or 
input your port number;
- `Please write accessToken for device:` - copy device accessToken from SENTIENT and paste it into the terminal;
- `Please write firmware chunk size in bytes or leave it blank to get all firmware by request:` - if you leave it blank, the file will be downloaded at once
in the full size. If you want to download in parts, enter the size of the chunk.


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/fw-mqtt-updated.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Firmware of the device is updated. To see its status, you should go to the firmware dashboard as it shows in the following paragraph.

To find out about the firmware update, you need to [make a request and subscribe to attributes](/docs/reference/mqtt-api/#firmware-api).


</div>

<div class="st-tab" data-label="CoAP">

Execute the following command in terminal to install the CoAP and checksum libs:

```bash
pip3 install asyncio aiocoap mmh3 --user
```


Enter the path to the client's folder in terminal and execute the following command for SENTIENT
to get firmware example script:

```bash
python3 coap_firmware_client.py 
```


Download CoAP client example: [**coap_firmware_client.py**](/docs/user-guide/resources/firmware/coap_firmware_client.py)

After getting the following messages
- `Please write your SENTIENT host or leave it blank to use default (localhost):` - use your localhost, or the platform address;
- `Please write your SENTIENT port or leave it blank to use default (5683):` - you can just continue by pressing "enter", or 
input your port number;
- `Please write accessToken for device:` - copy device accessToken from SENTIENT and paste it into the terminal;
- `Please write firmware chunk size in bytes or leave it blank to get all firmware by request:` - if you leave it blank, the file will be downloaded at once
in the full size. If you want to download in parts, enter the size of the chunk.


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/fw-coap-updated.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Firmware of the device is updated. To see its status, you should go to the firmware dashboard as it shows in the following paragraph.

To find out about the firmware update, you need to [make a request and subscribe to attributes](/docs/reference/coap-api/#firmware-api).


</div>

</div>


## Dashboard

SENTIENT provides the summary of the firmware/software update to monitor and track the firmware/software update status of your device, such as which devices are updating right now, any boot issues, and which ones have already been updated.

### Firmware update monitoring dashboard

The dashboard is created automatically for each new tenant that you add to SENTIENT. 
You can also download the dashboard JSON [here](https://github.com/sentient/sentient/blob/master/application/src/main/data/json/demo/dashboards/firmware.json) and import it for existing tenants.

There you can see a list of all devices with full information about their firmware. 


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/fw-dashboard-ce.webp" alt="Monitor and track the firmware status of your device in the Firmware dashboard. You can see a list of all devices with full information about their firmware. Use the tabs on the right side of the page to see more detailed status information." loading="lazy"><figcaption>Monitor and track the firmware status of your device in the Firmware dashboard. You can see a list of all devices with full information about their firmware. Use the tabs on the right side of the page to see more detailed status information.</figcaption></figure><figure><img src="/images/user-guide/firmware/fw-dashboard-2-ce.webp" alt="Find out more about the firmware status of specific devices by clicking the buttons next to the device names." loading="lazy"><figcaption>Find out more about the firmware status of specific devices by clicking the buttons next to the device names.</figcaption></figure></div>


Click the "History of the firmware updates" button next to the device name to learn about the firmware update status of specific device.


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/fw-status-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/firmware/fw-status-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Software update monitoring dashboard

The dashboard is created automatically for each new tenant that you add to SENTIENT.
You can also download the dashboard JSON [here](https://github.com/sentient/sentient/blob/master/application/src/main/data/json/demo/dashboards/software.json) and import it for existing tenants.

There you can see a list of all devices with full information about their software.


<div class="st-gallery"><figure><img src="/images/user-guide/firmware/sw-dashboard-1-ce.webp" alt="Monitor and track the software status of your device in the Software dashboard." loading="lazy"><figcaption>Monitor and track the software status of your device in the Software dashboard.</figcaption></figure><figure><img src="/images/user-guide/firmware/sw-dashboard-2-ce.webp" alt="Find out more about the software status of specific devices by clicking the buttons next to the device names." loading="lazy"><figcaption>Find out more about the software status of specific devices by clicking the buttons next to the device names.</figcaption></figure></div>


### Configuration

#### Queue processing pace

To set the max number of devices that will be notified in the chosen time period using the following [configuration](/docs/user-guide/install/config/) properties:

```bash
export TB_QUEUE_CORE_FW_PACK_INTERVAL_MS=60000
export TB_QUEUE_CORE_FW_PACK_SIZE=100
```


#### Max size setting

By default, the maximum size of firmware that we can save in database is 2 gb. It can not be configured.
