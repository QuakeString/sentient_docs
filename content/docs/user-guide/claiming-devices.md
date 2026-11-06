+++
title = "Claiming devices"
description = "IoT device management using SENTIENT claiming devices feature"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/claiming-devices.md"
+++
## Use Case description

As a Tenant, I would like to pre-provision my devices via script or UI. My customers purchase devices directly from me or through the distributors.
I would like my customers to claim their devices based on the QR code or similar technique, once they get physical access to the device.

Once device is claimed, the customer becomes its owner and customer users may access device data as well as control the device.   

## Device Claiming scenarios
 
SENTIENT User can claim the device if they "know" the device Name and Secret Key. 
The Secret Key is optional, always has an expiration time, and may also change over time. 

The Secret Key may be provisioned in two different ways:

1. *Device-side key* scenario - Device contains **expirationTime** server attribute with expiration timestamp. The device sends claiming request to SENTIENT with claiming data and only after this customer is able to claim device by using device claiming widget.   
2. *Server-side key* scenario - Device contains **claimingData** server attribute with claiming data and customer claim device using claim device widget.  

See below for more details.


<div class="st-tabs">

<div class="st-tab" data-label="Claiming using device-side key scenario">


This procedure requires device to generate the Secret Key based on some trigger event. 
For example, once device is booted or when some physical button is pressed. 
Once the Secret Key is generated, it is valid for certain period of time. 
The device sends Claiming Information to the server which contains both the Secret Key and the duration of the validity of the key.


<div class="st-callout info">


By default, you can set the expiration date as the date and time the request was received plus 1 day as the maximum value.  
To add more time, you should increase the value of the parameter **caffeine.specs.claimDevices.timeToLiveInMinutes** in sentient.yaml file.

</div>


SENTIENT server stores Claiming Information for the duration of the validity of the key. See diagram below.

![image](/images/user-guide/claiming-devices/device-side-key-diagram.webp)

Device may send Claiming Information to TB using all supported transport protocols. The message body has two parameters: **secretKey** and **durationMs**, which may be optionally specified. 
The **secretKey** parameter adds security to the claiming process.
The **durationMs** parameter determines the expiration of claiming time.
In case the **secretKey** is not specified, the empty string as a default value is used.
In case the **durationMs** is not specified, the system parameter **device.claim.duration** is used (in the file **/etc/sentient/conf/sentient.yml**).


In order to enable claiming devices feature a system parameter **security.claim.allowClaimingByDefault** (see [configuration guide](/docs/user-guide/install/config/)) 
should be set to **true**, otherwise a server-side **claimingAllowed** attribute with the value **true** is obligatory for provisioned devices.


Please see the Device API references to get the information about the message structure and topics/URLs to which to send the claiming messages.
You can use the MQTT Gateway API that allows initiating claiming of multiple devices per time as well.

 - [MQTT Device API](/docs/reference/mqtt-api/#claiming-devices)
 - [CoAP Device API](/docs/reference/coap-api/#claiming-devices)
 - [HTTP Device API](/docs/reference/http-api/#claiming-devices)
 - [MQTT Gateway API](/docs/reference/gateway-mqtt-api/#claiming-devices-api)
 

Once the Claiming Info is sent, device may display the Secret Key either in plain text or using the QR code. User should scan this key and use it to send the Claiming Request.
Claiming Request consists of the device Name and Secret Key. You may use MAC address or other unique property as the device Name. 
See instructions how to send the Claiming Request [here](/docs/user-guide/claiming-devices/#device-claiming-api-request).   

**Note:** The Secret Key may also be an empty string. This is useful if your device does not have any way to display the Secret Key. 
For example, you may allow to claim device within 30 seconds after the claim button is pressed on the device. In this case user needs to know the device Name (MAC address, etc) only.

Server validates the Claiming Request and replies with the Claiming Response. Claiming Response contains status of the Claiming operation and Device ID if the operation was successful.

Once Claiming Information is provisioned, Customer User may use [Claim Device](/docs/user-guide/claiming-devices/#device-claiming-widget) widget.   


</div>

<div class="st-tab" data-label="Claiming using server-side key scenario">


Let's assume you have thousands of NB IoT/LoRaWAN/Sigfox devices connected using one of SENTIENT [Integrations](/docs/user-guide/integrations/).
The integration layer will automatically provision them in SENTIENT. 
Assuming Tenant Admin knows the list of DevEUIs (LoRaWAN) or any other device identifiers, 
it is possible to generate a random Secret Key per device and upload this key to SENTIENT as a server-side attribute using [REST API](/docs/reference/rest-api/) or UI.
Once this is done, tenant admin can email those keys to the Customer, or put them inside the device package box. 

![image](/images/user-guide/claiming-devices/server-side-key-diagram.webp)

In order to provision device Secret Key, Tenant Administrator should set server-side attribute "claimingData" like the following value:

```json
{"secretKey": "YOUR_SECRET_KEY", "expirationTime": 1640995200000}
``` 

, where expiration date is the end of the time when the device can be claimed that is 01/01/2022 as a unix timestamp with milliseconds precision.

Once server-side attribute is provisioned, Customer User may use [Claim Device](/docs/user-guide/claiming-devices/#device-claiming-widget) widget.  


</div>

</div>


## Device Claiming Widget


1. You are able to find Device Claiming Widget in <b>Static widget</b> section of <b>Input widgets</b> bundle.

1. Claim device widget is quite simple and allows to input device name and Secret Key.

1. It is possible to "hide" Secret Key input field and change the labels in "General settings".

1. It is also possible to configure all sorts of messages to the user in "Message settings".

1. Finally, you can relate the claimed device to the current state entity of the dashboard.<br> This is useful if you have multiple assets and would like to relate your device to one of them. 


<div class="st-gallery"><figure><img src="/images/user-guide/claiming-devices/claiming-widget-location.webp" alt="You are able to find Device Claiming Widget in Static widget section of Input widgets bundle." loading="lazy"><figcaption>You are able to find Device Claiming Widget in <b>Static widget</b> section of <b>Input widgets</b> bundle.</figcaption></figure><figure><img src="/images/user-guide/claiming-devices/claim-device-widget.webp" alt="Claim device widget is quite simple and allows to input device name and Secret Key." loading="lazy"><figcaption>Claim device widget is quite simple and allows to input device name and Secret Key.</figcaption></figure><figure><img src="/images/user-guide/claiming-devices/claim-device-widget-advanced-settings.webp" alt="It is possible to &quot;hide&quot; Secret Key input field and change the labels in &quot;General settings&quot;." loading="lazy"><figcaption>It is possible to "hide" Secret Key input field and change the labels in "General settings".</figcaption></figure><figure><img src="/images/user-guide/claiming-devices/claim-device-widget-message-settings.webp" alt="It is also possible to configure all sorts of messages to the user in &quot;Message settings&quot;." loading="lazy"><figcaption>It is also possible to configure all sorts of messages to the user in "Message settings".</figcaption></figure><figure><img src="/images/user-guide/claiming-devices/claim-device-widget-relation-settings.webp" alt="Finally, you can relate the claimed device to the current state entity of the dashboard. This is useful if you have multiple assets and would like to relate your device to one of them. " loading="lazy"><figcaption>Finally, you can relate the claimed device to the current state entity of the dashboard.<br> This is useful if you have multiple assets and would like to relate your device to one of them. </figcaption></figure></div>

 

## Device Claiming API Request

The Claiming Request is sent as a POST request to the following URL:

```bash
http(s)://host:port/api/customer/device/$DEVICE_NAME/claim
```


The supported data format is:

```json
{
  "secretKey":"value"
}
```


**Note:** the message does not contain **durationMs** parameter and the **secretKey** parameter is optional.

Whenever claiming is succeed the device is being assigned to the specific customer. The **claimingAllowed** attribute is automatically deleted in case the system parameter **allowClaimingByDefault** is **false**.

In addition, there is a possibility to reclaim the device, which means the device will be unassigned from the customer. The **claimingAllowed** attribute will appear again in case the **allowClaimingByDefault** is **false**. 

See the following for more details regarding the above steps. 

## Device Reclaiming API Request

In order to reclaim the device, you can send DELETE request to the following URL (Don't forget to replace device name with the correct name):

```bash
curl -X DELETE https://localhost/api/customer/device/$DEVICE_NAME/claim
```


You will receive the response like the following one:

```json
{
  "result": {},
  "setOrExpired": true
}
```


## Python example scripts

In this section you may get examples of code for claiming device feature.  
We will use **tb-mqtt-client** python module to connect and claim device.  
You are able to install it using the following command:  

```bash
pip3 install tb-mqtt-client --user
```


### Basic claiming example

Let's assume we have a device on tenant level and configured customer, like it is described above.  
At the moment, we want to connect the device and send claiming request to assign it to customer.  

Case description:
We have a device on ThingsBord with a name **Test claiming device**.  
The device has access token credentials - **Eypdinl1gUF5fSerOPJF**.  

We should [download the script](/docs/user-guide/resources/claiming-device/basic_claiming_example.py) below and run it to send claiming request to the server.  

```python
#
# Copyright © 2016-2024 The Sentient Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from tb_device_mqtt import TBDeviceMqttClient

def collect_required_data():
    config = {}
    print("\n\n", "="*80, sep="")
    print(" "*20, "SENTIENT basic device claiming example script.", sep="")
    print("="*80, "\n\n", sep="")
    host = input("Please write your SENTIENT server hostname or leave it blank to use default (localhost): ")
    config["host"] = host if host else "localhost"
    token = ""
    while not token:
        token = input("Please write accessToken for device: ")
        if not token:
            print("Access token is required!")
    config["token"] = token
    config["secret_key"] = input("Please write secret key for claiming request: ")
    if not config["secret_key"]:
        print("Please make sure that you have claimingData in server attributes for device to use this feature without device secret in the claiming request.")
    duration_ms = input("Please write duration in milliseconds for claiming request or leave it blank to use default (30000): ")
    config["duration_ms"] = int(duration_ms) if duration_ms else 30000
    print("\n", "="*80, "\n", sep="")
    return config


if __name__ == '__main__':
    config = collect_required_data()
    client = TBDeviceMqttClient(config["host"], username=config["token"])
    client.connect()
    rc = client.claim(secret_key=config["secret_key"], duration=config["duration_ms"]).get()
    if rc == 0:
        print("Claiming request was sent, now you should use claiming device widget to finish the claiming process.")

```


Then we are able to use [Device Claiming Widget](#device-claiming-widget).

## Next steps
