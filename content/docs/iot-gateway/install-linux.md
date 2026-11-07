+++
title = "Install the gateway on Linux and Docker"
description = "Install SENTIENT Gateway from a .deb, .rpm or Arch package, as a bare binary, or with Docker, and connect it to SENTIENT."
weight = 222

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
SENTIENT Gateway runs on Linux as a systemd service or in a Docker container. Both run the same program, so the choice depends only on how you run other software on that machine. This page was checked against gateway 4.14.0.

You need a gateway device in SENTIENT first: open **Entities > Gateways**, click **+**, give it a name and click **Create**. The machine must reach SENTIENT's MQTT port, normally **1883**.

## Docker

1. In SENTIENT, open the gateway and click **Launch command** at the top right.

   ![The Launch command dialog with the Download button for docker-compose.yml](/images/st/gateway-launch-command.webp)

2. Under **Download configuration file**, click **Download**, and copy `docker-compose.yml` to the gateway machine. The file holds the gateway's access token, so keep it private.
3. In the folder with the file, run:

   ```sh
   docker compose up -d
   ```

The file starts the image `quakestring/sentient-gateway-rs` as the container `st-gateway` and keeps its data in three named volumes:

| Volume | Holds |
|---|---|
| `st-gw-config` | The configuration, mirrored from SENTIENT |
| `st-gw-data` | The queue of values kept while SENTIENT cannot be reached |
| `st-gw-logs` | The logs |

The volumes survive `docker compose down` and image updates. To update, run `docker compose pull` and then `docker compose up -d`.

Some connectors need a port on the host, for example the REST connector (5000, open by default), BACnet (1052) or Modbus slave (5026). Remove the `#` in front of those lines in the file before you start it.

A container started without `host` or `accessToken` stays up and logs `NOT COMMISSIONED`. It no longer restarts in a loop.

## Packages: Debian, Ubuntu, Fedora, Arch

Download the package for your distribution and processor from the gateway release on the [SENTIENT releases page](https://github.com/QuakeString/sentient-release/releases):

| Distribution | File | Processors |
|---|---|---|
| Debian, Ubuntu, Raspberry Pi OS | `sentient-gateway_<version>-1_<arch>.deb` | amd64, arm64, armhf |
| Fedora, RHEL and similar | `sentient-gateway-<version>-1.<arch>.rpm` | x86_64, aarch64, armv7hl |
| Arch Linux, Arch Linux ARM | `sentient-gateway-<version>-1-<arch>.pkg.tar.zst` | x86_64, aarch64, armv7h |
| Any other | `sentient-gateway-<version>-linux-<arch>.tar.gz` (the bare program) | x86_64, aarch64, armv7 |

Install it, then connect it to SENTIENT. The token is read from the keyboard, so it does not end up in the shell history:

```sh
sudo apt install ./sentient-gateway_<version>-1_amd64.deb      # or: sudo dnf install ./….rpm, sudo pacman -U ./….pkg.tar.zst
sudo sentient-gateway --install --host sentient.example.com --port 1883 --token -
```

On a packaged gateway, `--install` only writes the connection and restarts the service. `--install --compose docker-compose.yml` reads the connection from the file that **Launch command** downloads. Instead of `--install`, you can also connect the gateway from its [local web page](/docs/iot-gateway/admin-ui/).

### The bare program

Unpack the `.tar.gz` and let the program install itself as a service:

```sh
tar xzf sentient-gateway-<version>-linux-x86_64.tar.gz
cd sentient-gateway-<version>-linux-x86_64
sudo ./sentient-gateway --install --host sentient.example.com --port 1883 --token -
```

It copies itself to `/usr/local/lib/sentient-gateway/`, creates the user `sentient-gateway`, and starts `sentient-gateway.service`.

## Where things are

| What | Where |
|---|---|
| Configuration | `/etc/sentient-gateway/st_gateway.json`, readable only by root and the service user |
| Data: queue, logs, device list | `/var/lib/sentient-gateway` |
| Service | `sentient-gateway.service`, running as the user `sentient-gateway` |
| Local web page | `http://127.0.0.1:8642/`, on the gateway machine only |

`ST_GW_CONFIG_DIR` and `ST_GW_DATA_DIR` move either folder.

Check the service with `systemctl status sentient-gateway` and its log with `journalctl -u sentient-gateway -f`.

## Which connectors need what

The packages and the bare program are one self-contained file without the **ODBC**, **BLE** and **EtherCAT** connectors. A configuration that uses one of them is loaded and then refused by name in the log. Run those sites in **Docker**, whose image has all connectors.

- **Serial ports** (Modbus RTU, serial, DNP3 over serial): the packages add the service user to the `dialout` group (`uucp` on Arch). In Docker, map the device, for example `devices: ["/dev/ttyUSB0:/dev/ttyUSB0"]`.
- **PROFINET**, **EtherCAT** and IEC 61850 GOOSE send raw Ethernet frames. In Docker, add `cap_add: [NET_RAW]`; PROFINET and EtherCAT also need `network_mode: host` and a network port of their own.
- **BLE** uses the host's Bluetooth service. In Docker, mount `/run/dbus/system_bus_socket` from the host and run the container as root.
- **CAN** works on Linux only, through SocketCAN.

## Uninstall

Remove the package (`sudo apt remove sentient-gateway`, or `dnf` or `pacman`), or run `sudo sentient-gateway --uninstall` for the bare program. The configuration and data folders stay. Delete them to remove everything.

## Common problems

| What you see | What to do |
|---|---|
| The log says `NOT COMMISSIONED` | The gateway has no host or token. Run `--install` with the connection, or use the local web page |
| The gateway connects and drops every few seconds | Another gateway uses the same token. Stop it |
| `--install` refuses while `thingsboard-gateway.service` runs | Run `sudo systemctl disable --now thingsboard-gateway`, then `--install` again |
| The program stops with exit code 2 | It got an option it does not know, or `--host` without `--install`. Check the service definition or the compose `command:` |

## Related

- [Install on Windows](/docs/iot-gateway/install-windows/)
- [Local web page](/docs/iot-gateway/admin-ui/)
- [Getting started](/docs/iot-gateway/getting-started/)
