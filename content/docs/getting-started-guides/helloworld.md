+++
title = "First device to dashboard"
description = "Add a device, send it a value from your computer and show it on a dashboard. About 15 minutes."

aliases = ["/docs/getting-started/"]
[extra]
status = "checked"
checked = "4.3.0.57"
+++
In this guide you add one device to SENTIENT, send it readings from your computer as if it were a real pump, and show the readings on a dashboard. It takes about 15 minutes and needs nothing but a browser and a command prompt.

You need:

- A SENTIENT installation and a **tenant administrator** account. If you have just installed SENTIENT, see [Sign in for the first time](/docs/getting-started-guides/first-login/).
- The address of the server, for example `http://192.168.1.20:8080`. Below it is written as `SERVER`.
- `curl`. Windows 10 and 11 include it; on Linux it is usually installed.

## Step 1. Add the device

1. In the left menu, open **Entities > Devices**.
2. Click **+** at the top right of the list, then **Add new device**.
3. Type a **Name**, for example `Feed pump P-101`. The name must be unique in your tenant.
4. Leave **Device profile** at `default` and click **Add**.

![The Add new device window: name, label, device profile, gateway switch, owner and groups](/images/st/add-device-wizard.webp)

SENTIENT creates the device and opens the **Check connectivity** window. It shows ready-made commands for HTTP, MQTT and CoAP, for Windows, macOS and Linux, with this device's token already filled in. Copy the command, run it, and the values appear at the bottom of the window. You can close it and open it again from the device's details.

![Check connectivity: install curl, then run the command shown (hidden here, it contains the token)](/images/st/check-connectivity.webp)

The steps below do the same by hand, so you know where each part comes from.

## Step 2. Copy the access token

Every device has its own credentials. A new device gets an **access token**, a random string that the device sends with every reading.

1. Click the device in the list to open its details.
2. Click **Manage credentials** (the shield icon in the list does the same).
3. Click the copy button next to **Access token**.

![The Device Credentials window, with the access token hidden](/images/st/device-credentials.webp)

Treat the token like a password: anyone who has it can send data as this device.

## Step 3. Send a reading

Send one reading over HTTP. Replace `SERVER` and `TOKEN` with your values.

**Windows (Command Prompt):**

```
curl -X POST SERVER/api/v1/TOKEN/telemetry -H "Content-Type: application/json" -d "{\"flow\": 42.5, \"pressure\": 6.1}"
```

**Linux or macOS:**

```
curl -X POST SERVER/api/v1/TOKEN/telemetry -H 'Content-Type: application/json' -d '{"flow": 42.5, "pressure": 6.1}'
```

No output means success. If you see `Invalid access token` or the command cannot connect, see [Devices do not connect](/docs/troubleshooting/device-connection/).

Prefer MQTT? With the Mosquitto client, the token is the user name:

```
mosquitto_pub -h SERVER_HOST -p 1883 -u TOKEN -t v1/devices/me/telemetry -m '{"flow": 42.5}'
```

Send a few readings with different values, a few seconds apart, so the chart in step 5 has a line to draw.

## Step 4. See the values

Open the device and select the **Latest telemetry** tab. Each key you sent appears with its newest value and the time it arrived. The device's state in the list changes from **Inactive** to **Active**.

![Latest telemetry of Feed pump P-101: flow, motorCurrent, pressure and vibration](/images/st/device-details-telemetry.webp)

Values appear here within a second of arriving. If nothing appears, the reading did not reach SENTIENT: check the command's output.

## Step 5. Show the values on a dashboard

1. In the left menu, open **Dashboards**, click **+**, then **Create new dashboard**.
2. Type a **Title**, for example `Pump P-101`, and click **Add**. The new, empty dashboard opens in edit mode.
3. Click **Add new widget**. Open the **Cards** bundle and choose **Value card**.

   ![Select widgets bundle: Cards, Charts, gauges, buttons and more](/images/st/dashboard-add-widget.webp)

4. Under **Datasource**, pick your device. Under the key, pick `flow`. Click **Add**.
5. Click **Add new widget** again. Open the **Charts** bundle and choose **Time series chart**, with the same device and the keys `flow` and `pressure`. Click **Add**.
6. Drag the widgets into place and resize them by their corners. Click **Save**.

The dashboard updates live: send another reading from step 3 and watch the card change.

## What next

- **Raise an alarm** when a value is out of range: [Alarm rules](/docs/user-guide/alarm-rules/).
- **Connect real equipment** such as PLCs over Modbus, OPC UA or S7: [SENTIENT Gateway](/docs/iot-gateway/).
- **Connect a device that speaks MQTT or HTTP itself**: [Device connectivity](/docs/getting-started-guides/connectivity/).
- **Share the dashboard** with a customer's users: [Customers](/docs/user-guide/ui/customers/).
- **Build a plant screen** with pumps, tanks and pipes: [SCADA](/docs/user-guide/scada/).
