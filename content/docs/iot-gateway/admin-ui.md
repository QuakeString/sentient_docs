+++
title = "Gateway local web page"
description = "Commission and inspect SENTIENT Gateway at the machine: sign in, connect it to SENTIENT, and see its connectors, devices, queue and logs."
weight = 223

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
Every SENTIENT Gateway installed on Windows or Linux has its own web page at **http://127.0.0.1:8642/**. Use it to connect a new gateway to SENTIENT at the machine, and to see why a gateway is not sending data: the link to SENTIENT, the connectors, the devices with their last values, the queue and the log. This page was checked against gateway 4.14.0.

SENTIENT stays in charge of the gateway's configuration. Changes you make on the local page are sent to SENTIENT, and a later save in SENTIENT wins.

## Open it and sign in

1. On the gateway machine, open **http://127.0.0.1:8642/** in a browser. On Windows, the Start menu has **Sentient Gateway (local web page)**.
2. Sign in as **admin** with the password you set in the Windows setup program.

If no password was set yet, the default user `admin` with the password `invenia` works, but only from the gateway machine itself. It opens only a screen where you set your own user name and password. The password must be at least 8 characters long. Common passwords and one character repeated are refused.

### Forgot the password

Set a new one from an administrator prompt. The command asks for it and does not show it:

| Where | Command |
|---|---|
| Windows | `"C:\Program Files\Sentient Gateway\sentient-gateway.exe" --ui-password -` |
| Linux | `sudo /usr/local/lib/sentient-gateway/sentient-gateway --ui-password -` (bare program) or `sudo sentient-gateway --ui-password -` (package) |
| Docker | `docker exec -it st-gateway sentient-gateway --ui-password -` |

A new password signs every browser out.

## What is on the page

| Menu | Pages |
|---|---|
| **Status** | **Overview**: the link to SENTIENT with the reason when it is down, the connectors and their states. **Devices**: each device with its last values. Devices that the gateway reads but does not send to SENTIENT are marked. **Data buffer**: values waiting to be sent |
| **Network** | **Interfaces**: the machine's network interfaces, read only. Change them in the operating system |
| **Services** | **Platform connection**: host, port and access token. **Connectors**: add, edit, switch on or off and delete connectors. A connector's **Devices** tab edits its devices and keys as a table |
| **System** | **Backup and restore**: download the connectors and settings as one JSON file, or restore such a file. **Restart**: restarts the gateway after you confirm with the password |
| **Logs** | **Events**: warnings, errors and changes as a timeline, repeats folded into one row. **System log**: the full log |
| **Settings** | **General**, **Storage**, **Logging**, **Statistics**, **Advanced**, **Security** (user name and password) and **Certificates** (the page's HTTPS certificate) |

A backup never holds the connection to SENTIENT or its access token, and a restore never changes them.

## Connect a gateway to SENTIENT

Open **Services > Platform connection**, type SENTIENT's MQTT host and port (normally 1883) and the gateway's access token, and save. The token is under **Manage credentials** on the gateway device in SENTIENT. A gateway that was not commissioned connects within seconds, without a restart.

You can change the connection only while the gateway is **not** connected. While it is connected, SENTIENT's gateway configuration sets it, and the page shows it read only. The same goes for a gateway in Docker, whose connection comes from the container's environment, and for a gateway that was provisioned.

**Test reachability** checks that SENTIENT answers, without signing in as this gateway. **Test the token** signs in with a token you type, and refuses the token the gateway is running with, so a test cannot knock the running gateway offline.

## Edits made here and in SENTIENT

When you edit a connector or a setting on the local page, the gateway applies it at once, saves it, and reports it to SENTIENT. SENTIENT copies the edit into the gateway's configuration, so the gateway management pages show it, and the local page then shows **In sync**. If someone saves the same thing in SENTIENT later, SENTIENT's version wins.

## Reach it from another computer

By default the page answers only on the gateway machine. To open it to the network:

1. Set `"localUi": {"listen": "0.0.0.0:8642"}` at the top level of `st_gateway.json`, or run `--install --ui-listen 0.0.0.0:8642`, and restart the gateway.
2. On Windows, open the port: `netsh advfirewall firewall add rule name="Sentient Gateway page" dir=in action=allow protocol=TCP localport=8642`.
3. Open **https://&lt;gateway address&gt;:8642/**. Any address other than the machine itself uses HTTPS only. The gateway makes its own certificate and renews it 30 days before it ends. Upload your own under **Settings > Certificates**.

> **Protect this password like an administrator's.** While the gateway is not connected, the page can point it at another server, and a server can push connectors that write to your equipment. Open the page only on a network you control.

In **Docker**, the page is off by default. Set `ST_GW_UI=on` in the container's environment and publish the port to the host's own address only: `ports: ["127.0.0.1:8642:8642"]`.

## Turn it off

Run `--install --no-ui`, clear the setup program's **Install the local web page** box, or set `"localUi": {"enabled": false}` in `st_gateway.json`. The gateway then opens no web port at all. `sentient-gateway --ui-url` prints the page's address, or nothing when it is off.

Uninstalling keeps the password and the certificate in `config\local-ui`. Delete that folder to forget them.

## Related

- [Install on Windows](/docs/iot-gateway/install-windows/)
- [Install on Linux and Docker](/docs/iot-gateway/install-linux/)
- [General configuration](/docs/iot-gateway/configuration/)
