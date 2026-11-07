+++
title = "OTA updates"
description = "Store firmware and software packages in SENTIENT and assign them to devices, and what devices can do with them in 4.3.0.57."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
**OTA** (over-the-air) updates let you keep firmware and software packages in SENTIENT, say which device or device profile should run which version, and let the devices fetch their package.

> **Note for 4.3.0.57:** only part of the update chain works yet. You can upload packages and assign them, and **CoAP** devices can download their assigned package. SENTIENT does not yet tell devices that a new package is assigned (the `fw_title`, `fw_version` and related shared attributes are not sent), MQTT and HTTP devices cannot download packages, and the update state a device reports is not followed. Plan OTA around CoAP devices that check for updates themselves, or update devices with your own tools for now.

## Upload a package

Open **Advanced features > OTA updates** in the left menu and click **+**.

| Setting | What to enter |
|---|---|
| **Title** and **Version** | For example `pump-controller` and `2.4.1`. A device asks for its package by these |
| **Version tag** | Optional: the version string your device reports, if it differs |
| **Device profile** | The package is offered only for devices of this profile |
| **Package type** | **Firmware** or **Software** |
| **Upload binary file** or **Use external URL** | The file itself, or a link to where it is kept |
| **Checksum algorithm** and **Checksum** | Leave the checksum empty to let SENTIENT compute it |
| **Description** | Free text, for example what changed |

The total size of a tenant's packages may be limited in its [tenant profile](/docs/user-guide/tenant-profiles/).

## Assign a package

- **To all devices of a profile:** open the [device profile](/docs/user-guide/device-profiles/) and set **Assigned firmware** or **Assigned software**.
- **To one device:** open the device's details and set **Assigned firmware** or **Assigned software** there. It takes the place of the profile's package for that device.

## Download over CoAP

The device asks for its assigned package with its access token:

```text
GET coap://sentient.example.com/fw/ACCESS_TOKEN?title=pump-controller&version=2.4.1&size=512&chunk=0
```

Use `sw` instead of `fw` for software. `size` is the chunk size in bytes and `chunk` the chunk number from `0`; a device can resume at the chunk it had reached after losing power. Without `size`, SENTIENT sends the whole package, split by CoAP block transfer.

| Answer | Means |
|---|---|
| **2.05** with data | A chunk. An empty 2.05 means the package is complete |
| **4.04** | No package is assigned: nothing to update |
| **4.00** | `title` or `version` differ from the assigned package, for example because it was changed during the download. Start again |

## Related

- [Device profiles](/docs/user-guide/device-profiles/)
- [Devices](/docs/user-guide/ui/devices/)
