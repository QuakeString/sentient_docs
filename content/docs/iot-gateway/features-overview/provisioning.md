+++
title = "Device Provisioning"
description = "Learn how to use SENTIENT IoT Gateway's device provisioning feature to automatically register and obtain credentials from the platform."

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/features-overview/provisioning.md"
+++
The **SENTIENT IoT Gateway** supports the [device provisioning](https://sentient.invenia.in/docs/user-guide/device-provisioning/) feature, allowing it to **automatically register itself** on the SENTIENT platform and obtain credentials without manual setup.

This is especially useful for:  
- **Device manufacturers** — enabling mass deployment with minimal configuration.
- **System integrators** — simplifying field installation and avoiding per‑device manual setup.

Once provisioned, the gateway uses the received credentials to connect to the platform and operate as a standard SENTIENT device.  

---

## How it works

When the gateway starts:  
1. It checks if device credentials are already stored locally.  
2. If credentials are missing, it uses **provisioning credentials** (key & secret) to request registration from the platform.  
3. The platform:  
    - Creates a device or use existing, depending on chosen in device profile device provisioning strategy.
    - Assigns it the requested or default name.
    - Generates device credentials.
4. The gateway stores these credentials locally and uses them for all future connections.

If credentials need to be changed or regenerated, they can be removed, and the gateway will re-provision itself on the next start.  

---

## Environment variables

Provisioning parameters are configured via environment variables.  
You can define them in your `docker-compose.yml` or set them manually in your environment.  

| Variable Name                               | Required | Description |
|---------------------------------------------|----------|-------------|
| **`TB_GW_PROVISIONING_DEVICE_KEY`**         | Yes      | Provisioning device key (provided by platform administrator). |
| **`TB_GW_PROVISIONING_DEVICE_SECRET`**      | Yes      | Provisioning device secret (provided by platform administrator). |
| **`TB_GW_PROVISIONING_DEVICE_NAME`**        | No       | Name of the provisioned device in SENTIENT. If not set, a random name will be generated. |
| **`TB_GW_PROVISIONING_DEVICE_ACCESS_TOKEN`**| No       | If set, the platform will assign this token to the device and use **Access Token** authentication. |
| **`TB_GW_PROVISIONING_DEVICE_USERNAME`**    | No       | MQTT Basic authentication username. Must be used together with password/client ID (credentials type will be **MQTT Basic**). |
| **`TB_GW_PROVISIONING_DEVICE_PASSWORD`**    | No       | MQTT Basic authentication password. Used together with username/client ID. |
| **`TB_GW_PROVISIONING_DEVICE_CLIENT_ID`**   | No       | MQTT Basic authentication client ID. |
| **`TB_GW_PROVISIONING_DEVICE_CA_CERT_FILENAME`** | No  | Name of CA certificate file in the `config/` folder. If set, the gateway will generate a client certificate and use **X.509 Certificate** authentication. |

**Note:**  
The credentials type is determined by which optional parameters you provide.  
For example:  
- `ACCESS_TOKEN` → Access Token authentication
- `USERNAME`/`PASSWORD`/`CLIENT_ID` → MQTT Basic authentication
- `CA_CERT_FILENAME` → X.509 authentication

---

## Provisioning process

1. **Start the gateway** with the provisioning variables configured.
2. The gateway sends a **provision request** with the device key and secret.
3. The platform responds with generated credentials according to the provided configuration.
4. Credentials are **saved locally** in the gateway’s config directory.
5. The gateway connects to SENTIENT using these credentials.

---

## Resetting provisioned credentials

If you want the gateway to re-provision itself (for example, to change authentication type or rotate credentials), you can remove the stored credentials via a service RPC:

**RPC Method:** [remove_provisioned_credentials](/docs/iot-gateway/guides/how-to-use-gateway-rpc-methods/#remove_provisioned_credentials-rpc-method)

When executed:
- The gateway deletes the stored credentials from its config folder.
- On the next restart, it will perform the provisioning process again.

---

## Example: Using device provisioning

To use the provisioning feature you need to follow next steps:

**1. Create a Device profile**

- Go to the "**Devices profile**" page, click the "**plus**" button and select "**Create new device profile**" from drop-down menu.
- Enter a device profile name and open the **Device provisioning** tab.
- Enable provisioning by selecting "**Allow to create new devices**" option.
- Copy/save the **Provisioning device key** and **Provisioning device secret**.
- Click "**Add**" to create the device profile.


<div class="st-gallery"><figure><img src="/images/gateway/device-provisioning/gateway-device-provisioning-1-ce.webp" alt="Go to the &quot;**Devices profile**&quot; page, click the &quot;**plus**&quot; button and select &quot;**Create new device profile**&quot; from drop-down menu." loading="lazy"><figcaption>Go to the "**Devices profile**" page, click the "**plus**" button and select "**Create new device profile**" from drop-down menu.</figcaption></figure><figure><img src="/images/gateway/device-provisioning/gateway-device-provisioning-2-ce.webp" alt="Enter a device profile name and open the **Device provisioning** tab." loading="lazy"><figcaption>Enter a device profile name and open the **Device provisioning** tab.</figcaption></figure><figure><img src="/images/gateway/device-provisioning/gateway-device-provisioning-3-ce.webp" alt="Enable provisioning by selecting &quot;**Allow to create new devices**&quot; option. Copy/save the **Provisioning device key** and **Provisioning device secret**. Click &quot;**Add**&quot; to create the device profile." loading="lazy"><figcaption>Enable provisioning by selecting "**Allow to create new devices**" option.<br> Copy/save the **Provisioning device key** and **Provisioning device secret**. <br>Click "**Add**" to create the device profile.</figcaption></figure><figure><img src="/images/gateway/device-provisioning/gateway-device-provisioning-4-ce.webp" alt="Device profile created." loading="lazy"><figcaption>Device profile created.</figcaption></figure></div>


**2. Download the Gateway configuration file**

- [Click to download docker-compose.yml for the Gateway.](/docs/iot-gateway/resources/docker-compose.yml)

**3. Edit the configuration file**

- Open the downloaded `docker-compose.yml` and set the provisioning variables:

```yaml
...
  environment:
    - host=SENTIENT_HOST
    - port=SENTIENT_PORT
    - TB_GW_PROVISIONING_DEVICE_KEY=YOUR_PROVISION_KEY
    - TB_GW_PROVISIONING_DEVICE_SECRET=YOUR_PROVISION_SECRET
    - TB_GW_PROVISIONING_DEVICE_NAME=Factory-Gateway-01
...
```


&#42; Replace `SENTIENT_HOST` and `SENTIENT_PORT` with the **host** and **port** of your SENTIENT instance.<br>
&#42; Replace `YOUR_PROVISION_KEY` and `YOUR_PROVISION_SECRET` with the ** values from the device profile**.


<div class="st-gallery"><figure><img src="/images/gateway/device-provisioning/gateway-device-provisioning-5-ce.webp" alt="Open the downloaded `docker-compose.yml` and set the provisioning variables." loading="lazy"><figcaption>Open the downloaded `docker-compose.yml` and set the provisioning variables.</figcaption></figure><figure><img src="/images/gateway/device-provisioning/gateway-device-provisioning-6-ce.webp" alt="Replace `SENTIENT_HOST` and `SENTIENT_PORT` with the host and port of your SENTIENT instance.Replace `YOUR_PROVISION_KEY` and `YOUR_PROVISION_SECRET` with the values from the device profile." loading="lazy"><figcaption>Replace `SENTIENT_HOST` and `SENTIENT_PORT` with the host and port of your SENTIENT instance.<br>Replace `YOUR_PROVISION_KEY` and `YOUR_PROVISION_SECRET` with the values from the device profile.</figcaption></figure></div>


**4. Start the Gateway** 

- Execute the following command to run the Gateway:

```
docker compose up
```


<div class="st-gallery"><figure><img src="/images/gateway/device-provisioning/gateway-device-provisioning-7-ce.webp" alt="Execute `docker compose up` command to run the Gateway." loading="lazy"><figcaption>Execute `docker compose up` command to run the Gateway.</figcaption></figure></div>


**5. Verify the connection**

The Gateway **auto‑registers**, obtains credentials, and connects using them.


<div class="st-gallery"><figure><img src="/images/gateway/device-provisioning/gateway-device-provisioning-8-ce.webp" alt="The Gateway auto‑registers, obtains credentials, and connects using them." loading="lazy"><figcaption>The Gateway auto‑registers, obtains credentials, and connects using them.</figcaption></figure></div>


In the SENTIENT UI, check status on the "**Gateways**" page or in the device details.


<div class="st-gallery"><figure><img src="/images/gateway/device-provisioning/gateway-device-provisioning-9-ce.webp" alt="In the SENTIENT UI, check status on the &quot;**Gateways**&quot; page or in the device details." loading="lazy"><figcaption>In the SENTIENT UI, check status on the "**Gateways**" page or in the device details.</figcaption></figure></div>
