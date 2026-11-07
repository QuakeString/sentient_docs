+++
title = "Devices"
description = "Add, find, edit and delete devices, manage their credentials and open their data."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **device** is anything that sends data to SENTIENT or receives commands from it: a PLC read through the gateway, a meter, a sensor with its own MQTT client, or the gateway itself. Every device has a name, a [device profile](/docs/user-guide/device-profiles/) and its own credentials.

Open **Entities > Devices** in the left menu.

![The devices list of the Demo Plant tenant](/images/st/devices-list.webp)

## The devices list

| Column | Meaning |
|---|---|
| **Created time** | When the device was added. The list is sorted by it, newest first. Click another column header to sort by it |
| **Name** | Unique within the tenant |
| **Device profile** | Decides the transport settings, the rule chain and the queue used for its data |
| **Label** | Free text shown beside the name, for example the plant area |
| **State** | **Active** while the device sends data, **Inactive** after 10 minutes without data. See [Device connectivity status](/docs/user-guide/device-connectivity-status/) to change the timeout |
| **Customer** | The customer that owns the device, if any |
| **Groups** | The device groups it belongs to |
| **Is gateway** | Ticked for a SENTIENT Gateway or another gateway that reports for several devices |

Above the list:

- **All** and **Groups** switch between the full list and [device groups](/docs/administration/entity-groups/).
- **Device Filter** narrows the list, for example by device profile or by state (active or inactive).
- **Include customer entities** shows devices that belong to customers too. Switch it off to see only the tenant's own devices.
- The search icon searches by name.

In each row, the shield icon opens the device's credentials and the bin deletes it.

## Add a device

1. Click **+**, then **Add new device**.
2. Type a **Name**. Optionally add a **Label**.
3. Choose a **Device profile**. Use `default` if you have no profile of your own yet.
4. Switch on **Is gateway** for a gateway. For a gateway, **Overwrite activity time for connected device** lets the gateway's own activity keep its devices marked active.
5. Under **Owner and groups**, keep yourself (the tenant) as the **Owner** or pick a customer, and optionally add the device to **Groups**.
6. Optionally click **Next: Credentials** to set your own access token, an X.509 certificate or MQTT Basic credentials. Without it, SENTIENT generates an access token.
7. Click **Add**.

![The Add new device window](/images/st/add-device-wizard.webp)

SENTIENT then opens **Check connectivity**, which shows ready-to-copy commands for HTTP, MQTT and CoAP with the device's own token. Select **Do not show again** to skip it next time; the same window opens from the **Check connectivity** button in the device's details.

![Check connectivity, with the command that contains the token hidden](/images/st/check-connectivity.webp)

To add many devices at once, click **+**, then **Import device**, and load a CSV file. See [Bulk provisioning](/docs/user-guide/bulk-provisioning/).

## Credentials

Click the shield icon in the list, or **Manage credentials** in the device's details.

![The Device Credentials window, with the access token hidden](/images/st/device-credentials.webp)

| Type | Use it when |
|---|---|
| **Access token** | Most devices and gateways. The device sends the token as its MQTT user name or in the HTTP URL |
| **X.509** | Devices that authenticate with a client certificate over MQTTs |
| **MQTT Basic** | Devices that must send a client ID, user name and password |

After you change the credentials, the device must use the new ones to connect. See [Device credentials](/docs/user-guide/device-credentials/) and, when a device is refused, [Devices do not connect](/docs/troubleshooting/device-connection/).

## Device details

Click a device to open its details. The tabs are:

| Tab | What it shows |
|---|---|
| **Details** | Name, profile, label, gateway settings and description. Click the pencil to edit |
| **Attributes** | Client, server and shared attributes, see [Attributes](/docs/user-guide/attributes/) |
| **Latest telemetry** | The newest value of every key the device sends |
| **Calculated fields** | Values SENTIENT computes from this device's data, see [Calculated fields](/docs/user-guide/calculated-fields/) |
| **Alarm rules** | Rules that raise alarms from this device's data, see [Alarm rules](/docs/user-guide/alarm-rules/) |
| **Alarms** | This device's alarms |
| **Events** | Errors, lifecycle events and debug events of the device |
| **Relations** | Links to assets and other entities |
| **Audit logs** | Who changed the device, and when |
| **Version control** | Its history in Git, when version control is set up |

![Latest telemetry of a pump](/images/st/device-details-telemetry.webp)

The buttons at the top of the details:

- **Open details page** opens the details as a full page with its own address you can share.
- **Check connectivity** shows the connection commands again.
- **Manage credentials** opens the credentials.
- **Manage owner and groups** moves the device to a customer and adds it to or removes it from groups.
- **Delete device** deletes it.

## Delete devices

Click the bin in a device's row, or tick several devices and click the bin above the list. Deleting a device also removes its attributes, alarms and relations, and its token stops working. It cannot be undone.

## Related

- [First device to dashboard](/docs/getting-started-guides/helloworld/)
- [Device profiles](/docs/user-guide/device-profiles/)
- [Device connectivity status](/docs/user-guide/device-connectivity-status/)
