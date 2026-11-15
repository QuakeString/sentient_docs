+++
title = "Device profiles"
description = "Group the settings that many devices share: rule chain, queue, transport, alarm rules, calculated fields and self-provisioning."
aliases = ["/docs/user-guide/ui/device-profiles/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **device profile** holds the settings that a kind of device has in common. Every device has exactly one profile. Change the profile, and every device that uses it follows. Make one profile per kind of equipment, for example `Centrifugal pump`, `Energy meter` or `Plant gateway`.

The tenant administrator manages profiles under **Profiles > Device profiles** in the left menu. The `default` profile exists from the start; new devices get it unless you choose another. To change that, use **Make device profile default** in another profile's row.

## Add a profile

1. Click **+**, then **Create new device profile**. To bring in a profile exported from another SENTIENT, choose **Import device profile** and load its JSON file; **Add from hub** takes a ready-made one from the [Solution hub](/docs/solution-hub/).
2. Fill in the **Device profile details** (below), then **Next**.
3. On the following steps, set the **Transport configuration**, **Alarm rules** and **Device provisioning**, or leave the defaults. All of them can be changed later.
4. Click **Add**.

## Details

| Setting | What it does |
|---|---|
| **Name** | Unique within the tenant |
| **Default rule chain** | The [rule chain](/docs/user-guide/rule-engine-2-0/overview/) that processes data from these devices. Empty means the tenant's **Root Rule Chain** |
| **Mobile dashboard** | The dashboard the mobile app opens for one of these devices |
| **Queue** | The queue the data goes through. Keep `Main` unless you have set up [queues](/docs/user-guide/rule-engine-2-5/queues/) for separate workloads |
| **Default edge rule chain** | The rule chain used on an [Edge](/docs/edge/) for these devices |
| **Assigned firmware** / **Assigned software** | The [OTA package](/docs/user-guide/ota-updates/) these devices should run |
| **Image** | Shown for the profile in lists and widgets |
| **Description** | Free text |

## Profile details tabs

Click a profile to open it. The tabs are:

![A device profile open on the Details tab, with the tabs Transport configuration, Calculated fields, Alarm rules and Device provisioning](/images/st/device-profile-details.webp)

| Tab | What it holds |
|---|---|
| **Details** | The settings above |
| **Transport configuration** | How these devices connect, below |
| **Calculated fields** | [Calculated fields](/docs/user-guide/calculated-fields/) that apply to every device of the profile |
| **Alarm rules** | [Alarm rules](/docs/user-guide/alarm-rules/) that apply to every device of the profile |
| **Device provisioning** | Whether devices may add themselves, below |
| **Audit logs** | Who changed the profile, and when |
| **Version control** | The profile's history in Git, when [version control](/docs/user-guide/version-control/) is set up |

## Transport configuration

| Transport type | Use it for |
|---|---|
| **Default** | Devices that use SENTIENT's standard MQTT topics, HTTP or CoAP API. Choose it unless you need one of the others |
| **MQTT** | MQTT devices whose topics or payload format you cannot change |
| **CoAP** | CoAP devices that send Protobuf or need special power-saving settings |
| **SNMP** | Network equipment read by SENTIENT over SNMP |
| **LWM2M** | Not available in 4.3.0.57: SENTIENT does not run an LwM2M server yet |

### MQTT

| Setting | What it does |
|---|---|
| **Telemetry topic filter** | The topic these devices publish telemetry on, for example `plant/+/telemetry`. Default `v1/devices/me/telemetry`. `+` matches one level, `#` the rest |
| **Attributes publish topic filter** | The topic they publish attributes on. Default `v1/devices/me/attributes` |
| **Attributes subscribe topic filter** | The topic they receive attribute updates on |
| **MQTT device payload** | **JSON** (default) or **Protobuf**. For Protobuf you enter the `.proto` schemas for telemetry, attributes and RPC |
| **Use Json format for default downlink topics** | With Protobuf, still send attribute updates and commands on the standard `v1/devices/me/…` topics as JSON |
| **Send PUBACK on PUBLISH message validation failure** | By default SENTIENT closes the connection when a message cannot be read. When on, it acknowledges the message and keeps the connection |

> **Note for 4.3.0.57:** the **MQTT Sparkplug B** option can be switched on, but SENTIENT does not decode Sparkplug messages yet.

## Device provisioning

**Provisioning** lets a device add itself on first start: it sends the profile's key and secret, and SENTIENT answers with the device's own access token. Use it when installers set up many identical devices and should not have to create each one in SENTIENT first.

| Strategy | What happens |
|---|---|
| **Disabled** | Devices cannot add themselves. The default |
| **Allow to create new devices** | A device with a new name is created with this profile. A name that already exists is refused |
| **Check for pre-provisioned devices** | Only devices you already created (for example by [bulk provisioning](/docs/user-guide/bulk-provisioning/)) can get their credentials. Unknown names are refused |
| **X509 Certificates Chain** | Devices that connect over MQTTs with a client certificate signed by the certificate you enter are recognised by it. With **Create new devices**, an unknown device is created |

The **Provision device key** and **Provision device secret** are generated for you; copy them into the device's settings. Treat the secret like a password: anyone with both can add devices to your tenant.

The device sends its request to `/api/v1/provision` over HTTP, to `/provision/request` over MQTT, or to `/api/v1/provision` over CoAP. See [Device provisioning](/docs/user-guide/device-provisioning/) for the request and the answers.

SENTIENT accepts at most 60 provisioning requests a minute for one key and 600 for the whole server. Change this with the environment variables `SENTIENT_PROVISION_RATE_PER_KEY` and `SENTIENT_PROVISION_RATE_GLOBAL`. Above it, the device gets "Too many provisioning requests. Please slow down."

### Provisioning answers

| Answer | Cause |
|---|---|
| `SUCCESS` with `credentialsValue` | The device is created or found; the value is its access token |
| `NOT_FOUND` "Provision data was not found!" | The key and secret match no profile |
| `FAILURE` "Provisioning is disabled for this device profile!" | The profile's strategy is **Disabled** |
| `FAILURE` "Device with this name already exists!" | **Allow to create new devices**, but the name is taken |
| `NOT_FOUND` "Device not found!" | **Check for pre-provisioned devices**, and no device has that name |
| `FAILURE` "Device profile mismatch!" | The pre-provisioned device has another profile |
| `FAILURE` "License limit exceeded" | Your licence allows no more devices |

## Delete a profile

Click the bin in the profile's row. SENTIENT refuses while devices still use the profile ("Cannot delete device profile. 3 device(s) are using this profile."): move them to another profile first. The default profile cannot be deleted either; make another one the default first.

## Related

- [Devices](/docs/user-guide/ui/devices/)
- [Asset profiles](/docs/user-guide/asset-profiles/)
- [Alarm rules](/docs/user-guide/alarm-rules/)
