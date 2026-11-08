+++
title = "Basic MQTT authentication"
description = "SENTIENT MQTT based authentication."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/basic-mqtt.md"
+++
MQTT Based Authentication is available for devices that connect using MQTT. To do this, you need to change the device credential type from "Access token" to "MQTT Basic".
Basic MQTT credentials consist of the optional client id, username and password. See [MQTT API](/docs/reference/mqtt-api/) for more details.

Next, we will explore how to change the device credentials and how clients can connect to the device using these credentials.
Let's consider several options:

## Authentication based on Client ID only. 

To enable this, only the client ID needs to be populated in the device credentials. MQTT clients will be able to connect if they specify correct client ID.

Let's review a simple command to publish telemetry readings using only MQTT client ID to the SENTIENT.
The command is using plain MQTT without TLS:


```bash
mosquitto_pub -d -q 1 -h "YOUR_SENTIENT_HOST" -p "1883" -t "v1/devices/me/telemetry" -i "YOUR_CLIENT_ID" -m {"temperature":25}
```


where:

* **YOUR_SENTIENT_HOST** with the host of your SENTIENT instance;
* **YOUR_CLIENT_ID** with your client id.

<br>
SENTIENT offers a convenient "Check Connectivity" feature that automatically generates a command based on your host and the device credentials you provide. All you have to do is copy and run it.

Let's publish telemetry readings using only MQTT client ID. First, change the credential type for your device from "Access token" to "MQTT Basic":


1. Go to the "Devices" page, click on your device to open the device details window, and click the "Manage credentials" button;

1. In the "Device Credentials" window, select "MQTT Basic" credential type, and specify client ID. Click "Save".


<div class="st-gallery"><figure><img src="/images/user-guide/basic-mqtt/authentication-manage-credentials-1-ce.webp" alt="Go to the &quot;Devices&quot; page, click on your device to open the device details window, and click the &quot;Manage credentials&quot; button;" loading="lazy"><figcaption>Go to the "Devices" page, click on your device to open the device details window, and click the "Manage credentials" button;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-client-id-only-1-ce.webp" alt="In the &quot;Device Credentials&quot; window, select &quot;MQTT Basic&quot; credential type, and specify client ID. Click &quot;Save&quot;." loading="lazy"><figcaption>In the "Device Credentials" window, select "MQTT Basic" credential type, and specify client ID. Click "Save".</figcaption></figure></div>


After changing device credentials, use the "Check connectivity" feature to post telemetry:

- Click "Check connectivity" button to open the corresponding window;
- In the opened window, select your operating system;
- Install the necessary client tools using the command from the guide;
- Copy and run command to publish telemetry;

Once you have successfully executed the command, you should see the published "temperature" readings.


<div class="st-gallery"><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-client-id-only-2-ce.webp" alt="Click &quot;Check connectivity&quot; button to open the corresponding window;" loading="lazy"><figcaption>Click "Check connectivity" button to open the corresponding window;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-client-id-only-3-ce.webp" alt="In the opened window select your operating system, and install the necessary client tools using the command from the guide. Copy and run the command to publish telemetry;" loading="lazy"><figcaption>In the opened window select your operating system, and install the necessary client tools using the command from the guide. Copy and run the command to publish telemetry;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-client-id-only-4-ce.webp" alt="Once you have successfully executed the command, you should see the published &quot;temperature&quot; readings." loading="lazy"><figcaption>Once you have successfully executed the command, you should see the published "temperature" readings.</figcaption></figure></div>


## Authentication based on Username and Password. 

For this purpose, only the username and password need to be populated in the credentials form.
MQTT Clients will be able to connect if they specify correct username and password.

Let's review a simple command to publish telemetry readings using MQTT client username and password to the SENTIENT. The command is using plain MQTT without TLS:


```bash
mosquitto_pub -d -q 1 -h "YOUR_SENTIENT_HOST" -p "1883" -t "v1/devices/me/telemetry" -u "YOUR_CLIENT_USERNAME" -P "YOUR_CLIENT_PASSWORD" -m {"temperature":25}
```


where:

* **YOUR_SENTIENT_HOST** with the host of your SENTIENT instance;
 * **YOUR_CLIENT_USERNAME**, **YOUR_CLIENT_PASSWORD** with your client username and password.

<br>
In the "Check Connectivity", you'll find an auto-generated command based on your host and device credentials that you've provided. All you have to do is copy and run it.

Let's publish telemetry readings using the MQTT client username and password. First, change the credential type for your device from "Access token" to "MQTT Basic":


1. Go to the "Devices" page, click on your device to open the device details window, and click the "Manage credentials" button;

1. In the "Device Credentials" window, select "MQTT Basic" credential type, and specify username and password. Click "Save".


<div class="st-gallery"><figure><img src="/images/user-guide/basic-mqtt/authentication-manage-credentials-1-ce.webp" alt="Go to the &quot;Devices&quot; page, click on your device to open the device details window, and click the &quot;Manage credentials&quot; button;" loading="lazy"><figcaption>Go to the "Devices" page, click on your device to open the device details window, and click the "Manage credentials" button;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-username-and-password-1-ce.webp" alt="In the &quot;Device Credentials&quot; window, select &quot;MQTT Basic&quot; credential type, and specify username and password. Click &quot;Save&quot;." loading="lazy"><figcaption>In the "Device Credentials" window, select "MQTT Basic" credential type, and specify username and password. Click "Save".</figcaption></figure></div>


After changing device credentials, use the "Check connectivity" feature to post telemetry:

- Click "Check connectivity" button to open the corresponding window;
- In the opened window, select your operating system;
- Install the necessary client tools using the command from the guide;
- Copy and run command to publish telemetry;

Once you have successfully executed the command, you should see the published "temperature" readings.


<div class="st-gallery"><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-username-and-password-2-ce.webp" alt="Click &quot;Check connectivity&quot; button to open the corresponding window;" loading="lazy"><figcaption>Click "Check connectivity" button to open the corresponding window;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-username-and-password-3-ce.webp" alt="In the opened window select your operating system and install the necessary client tools using the command from the guide. Copy and run the command to publish telemetry;" loading="lazy"><figcaption>In the opened window select your operating system and install the necessary client tools using the command from the guide. Copy and run the command to publish telemetry;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-username-and-password-4-ce.webp" alt="Once you have successfully executed the command, you should see the published &quot;temperature&quot; readings." loading="lazy"><figcaption>Once you have successfully executed the command, you should see the published "temperature" readings.</figcaption></figure></div>


## Authentication based on Client ID, Username and Password. 

For this option, you should populate Client ID, Username and Password. MQTT Clients will be able to connect if they specify correct combination of client ID, username and password.

Let's review a simple command to publish telemetry readings using MQTT client ID, username and password to the SENTIENT. The command is using plain MQTT without TLS:


```bash
mosquitto_pub -d -q 1 -h "YOUR_SENTIENT_HOST" -p "1883" -t "v1/devices/me/telemetry" -i "YOUR_CLIENT_ID" -u "YOUR_CLIENT_USERNAME" -P "YOUR_CLIENT_PASSWORD" -m {"temperature":25}
```


where:

* **YOUR_SENTIENT_HOST** with the host of your SENTIENT instance;
* **YOUR_CLIENT_ID** with your client id;
* **YOUR_CLIENT_USERNAME**, **YOUR_CLIENT_PASSWORD** with your client username and password.

<br>
In the "Check Connectivity", you'll find an auto-generated command based on your host and device credentials that you've provided. All you have to do is copy and run it.

Let's publish telemetry readings using the MQTT client ID, username and password. First, change the credential type for your device from "Access token" to "MQTT Basic":


1. Go to the "Devices" page, click on your device to open the device details window, and click the "Manage credentials" button;

1. In the "Device Credentials" window, select "MQTT Basic" credential type, and specify client ID, username and password. Click "Save".


<div class="st-gallery"><figure><img src="/images/user-guide/basic-mqtt/authentication-manage-credentials-1-ce.webp" alt="Go to the &quot;Devices&quot; page, click on your device to open the device details window, and click the &quot;Manage credentials&quot; button;" loading="lazy"><figcaption>Go to the "Devices" page, click on your device to open the device details window, and click the "Manage credentials" button;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-client-id-username-and-password-1-ce.webp" alt="In the &quot;Device Credentials&quot; window, select &quot;MQTT Basic&quot; credential type, and specify client ID, username and password. Click &quot;Save&quot;." loading="lazy"><figcaption>In the "Device Credentials" window, select "MQTT Basic" credential type, and specify client ID, username and password. Click "Save".</figcaption></figure></div>


After changing device credentials, use the "Check connectivity" feature to post telemetry:

- Click "Check connectivity" button to open the corresponding window;
- In the opened window, select your operating system;
- Install the necessary client tools using the command from the guide;
- Copy and run command to publish telemetry;
 
Once you have successfully executed the command, you should see the published "temperature" readings.


<div class="st-gallery"><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-client-id-username-and-password-2-ce.webp" alt="Click &quot;Check connectivity&quot; button to open the corresponding window;" loading="lazy"><figcaption>Click "Check connectivity" button to open the corresponding window;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-client-id-username-and-password-3-ce.webp" alt="In the opened window select your operating system, and install the necessary client tools using the command from the guide. Copy and run the command to publish telemetry;" loading="lazy"><figcaption>In the opened window select your operating system, and install the necessary client tools using the command from the guide. Copy and run the command to publish telemetry;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-client-id-username-and-password-4-ce.webp" alt="Once you have successfully executed the command, you should see the published &quot;temperature&quot; readings." loading="lazy"><figcaption>Once you have successfully executed the command, you should see the published "temperature" readings.</figcaption></figure></div>


## MQTTS (MQTT over TLS)

One-way SSL authentication is a standard authentication mode, where your client device verifies the identity of a server using server certificate. 


Follow the [MQTT over SSL](/docs/user-guide/mqtt-over-ssl/) guide to provision server certificate for your own SENTIENT instance. This certificate will be used by MQTT client to validate the server certificate.

Once provisioned, use "Check connectivity" feature to download the CA root certificate to your working directory and publish telemetry. But first, change the credential type for your device from "Access token" to "MQTT Basic":


1. Go to the "Devices" page, click on your device to open the device details window, and click the "Manage credentials" button;

1. In the "Device Credentials" window, select "MQTT Basic" credential type, and specify device credentials. Click "Save".


<div class="st-gallery"><figure><img src="/images/user-guide/basic-mqtt/authentication-manage-credentials-1-ce.webp" alt="Go to the &quot;Devices&quot; page, click on your device to open the device details window, and click the &quot;Manage credentials&quot; button;" loading="lazy"><figcaption>Go to the "Devices" page, click on your device to open the device details window, and click the "Manage credentials" button;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-client-id-username-and-password-1-ce.webp" alt="In the &quot;Device Credentials&quot; window, select &quot;MQTT Basic&quot; credential type, and specify device credentials. Click &quot;Save&quot;." loading="lazy"><figcaption>In the "Device Credentials" window, select "MQTT Basic" credential type, and specify device credentials. Click "Save".</figcaption></figure></div>


- Now, click "Check connectivity" button. In the opened window, select your operating system and install the necessary client tools using the command from the guide;
- Switch to the "MQTTs" protocol. Copy and run the first command to download the valid CA certificate;
- Copy and run the second command from your working directory (where you saved the certificate) to publish telemetry. This command uses the *root-ca.pem* certificate to establish a secure connection with the SENTIENT and the device credentials you specified for its authentication.

Once you have successfully executed the command, you should see the published "temperature" readings.


<div class="st-gallery"><figure><img src="/images/user-guide/basic-mqtt/authentication-based-on-client-id-username-and-password-2-ce.webp" alt="Click &quot;Check connectivity&quot; button to open the corresponding window;" loading="lazy"><figcaption>Click "Check connectivity" button to open the corresponding window;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/mqtt-over-tls-2-ce.webp" alt="In the opened window select your operating system, and install the necessary client tools using the command from the guide. Switch to the &quot;MQTTs&quot; protocol. Copy and run the first command to download the valid CA certificate;" loading="lazy"><figcaption>In the opened window select your operating system, and install the necessary client tools using the command from the guide. Switch to the "MQTTs" protocol. Copy and run the first command to download the valid CA certificate;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/mqtt-over-tls-3-ce.webp" alt="Copy and run the second command to publish telemetry using the sentient-cloud-root-ca.pem certificate and the device credentials you specified for its authentication;" loading="lazy"><figcaption>Copy and run the second command to publish telemetry using the sentient-cloud-root-ca.pem certificate and the device credentials you specified for its authentication;</figcaption></figure><figure><img src="/images/user-guide/basic-mqtt/mqtt-over-tls-4-ce.webp" alt="Once you have successfully executed the command, you should see the published &quot;temperature&quot; readings." loading="lazy"><figcaption>Once you have successfully executed the command, you should see the published "temperature" readings.</figcaption></figure></div>


<br>
Example of a generated command to publish telemetry using the *root-ca.pem* certificate, host of your SENTIENT instance (YOUR_SENTIENT_HOST), client id (YOUR_CLIENT_ID), and client username and password (YOUR_CLIENT_USERNAME / YOUR_CLIENT_PASSWORD) of the selected device:


```bash
mosquitto_pub -d -q 1 --cafile root-ca.pem -h YOUR_SENTIENT_HOST -p 8883 -t v1/devices/me/telemetry -i "YOUR_CLIENT_ID" -u "YOUR_CLIENT_USERNAME" -P "YOUR_CLIENT_PASSWORD" -m {"temperature":25}
```
