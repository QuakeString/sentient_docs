+++
title = "Install the gateway on Windows"
description = "Install SENTIENT Gateway on Windows with its setup program, connect it to SENTIENT, and run it as a Windows service."
weight = 221

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
On Windows, SENTIENT Gateway runs as a Windows service named **SentientGateway**. The setup program installs the service, connects it to SENTIENT, and sets up the [local web page](/docs/iot-gateway/admin-ui/). This page was checked against gateway 4.14.0.

## Before you start

- Windows 10 or later, 64-bit, and an administrator account on the machine.
- A gateway device in SENTIENT. Open **Entities > Gateways**, click **+**, give it a name and click **Create**. See [Getting started](/docs/iot-gateway/getting-started/).
- The machine must reach SENTIENT's MQTT port, normally **1883**.

## 1. Get the connection file

1. In SENTIENT, open the gateway and click **Launch command** at the top right.
2. Under **Download configuration file**, click **Download**. You get a `docker-compose.yml` file. It holds SENTIENT's address, the MQTT port and the gateway's access token, so keep it private.

You can also skip the file and type the host, port and access token yourself. You find the token under the gateway device's **Manage credentials**.

> If this gateway already runs in Docker with the same token, stop it first with `docker compose down`. SENTIENT keeps one session per token, so two gateways with the same token push each other off.

## 2. Run the setup program

1. Download `SentientGatewaySetup-<version>.exe` from the gateway release on the [SENTIENT releases page](https://github.com/QuakeString/sentient-release/releases).
2. Run it and accept the Windows prompt for administrator rights.
3. On the connection page, choose one of these:

   | Choice | What it does |
   |---|---|
   | **Import** | Reads the host, port and token from the `docker-compose.yml` you downloaded. A host or port you type on the same page is used instead of the file's |
   | **Enter** | You type the MQTT host, port and access token |
   | **Skip** | Installs the service without a connection. You connect it later from the local web page |
   | **Keep the current connection** | Offered when you upgrade an installed gateway |

   If the file names `host.docker.internal`, SENTIENT runs on the same machine that made the file. Type the address of the SENTIENT server instead.
4. Click **Next**. Setup checks your answers before anything changes. A token that is malformed or still the placeholder is refused, with the reason.
5. On **Local web page**, keep **Install the local web page** ticked and type a password for the user `admin` twice. It must be at least 8 characters long; common passwords are refused.
6. Finish the setup. The summary shows the token only as a fingerprint.

The service starts at once and on every boot. In SENTIENT, the gateway shows as **Active** within a few seconds.

## Where things are

| What | Where |
|---|---|
| Program | `C:\Program Files\Sentient Gateway\sentient-gateway.exe` |
| Configuration | `C:\ProgramData\Sentient Gateway\config\st_gateway.json` |
| Data: queue, logs, device list | `C:\ProgramData\Sentient Gateway\data` |
| Local web page | `http://127.0.0.1:8642/`, also in the Start menu as **Sentient Gateway (local web page)** |

Only SYSTEM and administrators can read `C:\ProgramData\Sentient Gateway`, because the configuration holds the access token.

Connectors, devices and other settings come from SENTIENT. You configure them in the gateway's pages in SENTIENT, not in these files.

## Install from the command line

From an elevated Command Prompt, one line installs and connects the gateway. The token is read from the keyboard, so it does not end up in the command history:

```bat
sentient-gateway.exe --install --host sentient.example.com --port 1883 --token -
```

`--install --compose docker-compose.yml` reads the connection from the file instead. Add `--check` to see what would happen without changing anything.

For an unattended install with the setup program:

```bat
SentientGatewaySetup-<version>.exe /VERYSILENT /SUPPRESSMSGBOXES /LOG=C:\temp\setup.log /COMPOSE=C:\temp\docker-compose.yml
```

Use `/HOST=… /PORT=… /TOKENFILE=C:\temp\token.txt` instead of `/COMPOSE` to give the values directly. All paths must be absolute. Exit code **7** means the install was refused or failed; the log gives the reason, and the previous service is restored. Exit code **1** means the old Python gateway is still installed.

## Upgrade

Run the setup program of the new version and choose **Keep the current connection**. The configuration, the queue and the local web page password stay.

The old Python gateway must be uninstalled first, in **Settings > Apps**. Its `st_gateway.json` stays in `C:\ProgramData\Sentient Gateway\config`, and the new gateway reads it.

## Uninstall

Uninstall **Sentient Gateway** in **Settings > Apps**, or run `sentient-gateway.exe --uninstall`. The service and the program go. The configuration and data folders stay, so a later install picks up where it stopped. Delete `C:\ProgramData\Sentient Gateway` to remove them too.

## Common problems

| What you see | What to do |
|---|---|
| The service does not start and its log is empty | Read `C:\ProgramData\Sentient Gateway\service-error.log`. It holds errors from before logging starts, for example a data folder on a drive that is not mounted |
| The log says `NOT COMMISSIONED` | The gateway has no host or token. Connect it from the [local web page](/docs/iot-gateway/admin-ui/), or run `--install` again with the connection |
| The gateway connects and drops every few seconds | Another gateway uses the same token, often an old Docker container. Stop it |
| The import says *placeholder* | The file came from an older SENTIENT. Copy the access token from the device's **Manage credentials** and choose **Enter** |
| Another copy refuses to start and names a process id | One gateway per data folder. Stop the service before you run the program in a console |

## Related

- [Install on Linux and Docker](/docs/iot-gateway/install-linux/)
- [Local web page](/docs/iot-gateway/admin-ui/)
- [Getting started](/docs/iot-gateway/getting-started/)
