+++
title = "OTA updates"
description = "Store firmware and software packages in SENTIENT, assign them to devices or device profiles, and let devices download them over MQTT, HTTP or CoAP."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
**OTA** (over-the-air) updates let you keep firmware and software packages in SENTIENT, say which device or device profile should run which version, and let the devices fetch their package.

<div class="st-callout warn">

**In 4.3.0.57 only part of the update chain works.** You can upload and assign packages, and **CoAP** devices can download a package assigned to the device itself. SENTIENT does not tell devices about a new package, MQTT and HTTP devices cannot download, and the state a device reports is not followed. **From the release after 4.3.0.57** the whole chain on this page works.

</div>

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

**Title** and **Version** together must be unique in the tenant. You can search the list and download a package again. A package that a device or device profile uses cannot be deleted; remove the assignment first.

The total size of a tenant's packages may be limited in its [tenant profile](/docs/user-guide/tenant-profiles/).

## Assign a package

- **To all devices of a profile:** open the [device profile](/docs/user-guide/device-profiles/) and set **Assigned firmware** or **Assigned software**.
- **To one device:** open the device's details and set **Assigned firmware** or **Assigned software** there.

A device's own assignment wins over its profile's. The lists offer only packages of that device profile that have a file or a URL.

In 4.3.0.57 the CoAP download serves only a package assigned to the device itself; a package set only on the profile is not served. Assign packages per device there.

## What the device receives

*From the release after 4.3.0.57.*

When a package is assigned, SENTIENT sets these **shared attributes** on the device:

| Attribute | Holds |
|---|---|
| `fw_title`, `fw_version`, `fw_ts`, `fw_tag` | The package and when it was assigned |
| `fw_size`, `fw_checksum_algorithm`, `fw_checksum` | For an uploaded file |
| `fw_url` | For a package given as a URL, instead of the three above |

It also saves the telemetry `fw_state = INITIATED` and `target_fw_title`, `target_fw_version` and related `target_fw_*` keys, so the update shows on dashboards. For software, every key starts with `sw_` instead of `fw_`. When you remove the assignment, the attributes are removed.

A device subscribed to shared attributes (see [MQTT](/docs/reference/mqtt-api/) and [HTTP](/docs/reference/http-api/)) learns about the package at once.

## What the device reports back

The device sends its progress as telemetry `fw_state` (or `sw_state`):

| Value | Means |
|---|---|
| `DOWNLOADING` | Download started |
| `DOWNLOADED` | File received |
| `VERIFIED` | Checksum matched |
| `UPDATING` | Installing |
| `UPDATED` | Running the new version |
| `FAILED` | The update failed |

After `UPDATED` it can also send `current_fw_title` and `current_fw_version`.

## Download over MQTT

*From the release after 4.3.0.57.*

1. Subscribe to `v2/fw/response/+/chunk/+` and `v2/fw/error`.
2. Publish the chunk size in bytes, as text (for example `4096`), to `v2/fw/request/{requestId}/chunk/{n}`, with `n` counting from `0`. `requestId` is any id you choose.
3. Each chunk arrives on `v2/fw/response/{requestId}/chunk/{n}`. Ask for the next one until a chunk comes back **empty**: the download is complete.

Use `v2/sw/...` for software.

## Download over HTTP

*From the release after 4.3.0.57.*

```text
GET http://sentient.example.com:8080/api/v1/ACCESS_TOKEN/firmware?title=pump-controller&version=2.4.1&size=4096&chunk=0
```

Use `/software` for software. `size` and `chunk` work as in the CoAP download below. The answer is **404** when no package is assigned and **400** when `title` or `version` differ from the assigned package.

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
