+++
title = "Gateway errors"
description = "Common SENTIENT Gateway problems: offline gateway, unreachable PLCs, failed writes and a full storage queue."
weight = 189

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Most gateway problems show up in one of two places: the gateway's own log, and the **Gateways** page in SENTIENT. The log lines quoted below are what the SENTIENT Gateway writes, so you can search for them.

## Where the gateway keeps its files

| Installation | Configuration | Data (queue, logs) |
|---|---|---|
| Windows | `%ProgramData%\Sentient Gateway\config` | `%ProgramData%\Sentient Gateway\data` |
| Linux | `/etc/sentient-gateway` | `/var/lib/sentient-gateway` |
| Docker | `/sentient_gateway/config` (volume `st-gw-config`) | `/sentient_gateway/data` (volume `st-gw-data`) |

On Linux the service is `sentient-gateway.service`: read its log with `journalctl -u sentient-gateway -f`. With Docker use `docker logs -f st-gateway`. The gateway's local web page on port **8642** also shows the recent log.

## The gateway shows offline

Error ID: [ST-GW-001](/docs/troubleshooting/errors/st-gw-001/)

The gateway cannot reach SENTIENT, or it was never commissioned.

**In the log:**

- `uplink connection error; retrying in …`: the gateway tries again with a growing wait, up to 30 seconds between attempts.
- `still not commissioned: …`: the gateway was installed without a host and token.

**Fix:**

1. Check `st_gateway.json` in the configuration folder: `host` must be the SENTIENT server and `port` its MQTT port (1883, or 8883 with TLS).
2. Check the access token. It is the token of the gateway device in SENTIENT. A wrong token makes the server refuse the connection, see [Devices do not connect](/docs/troubleshooting/device-connection/#3-wrong-credentials).
3. Test the port from the gateway machine, for example `nc -vz <server> 1883`.

A gateway installed without a host and token commissions itself a few seconds after you add them to `st_gateway.json` or set them on its local web page. No restart is needed. Values set through environment variables need a restart.

**Data is not lost while the gateway is offline.** Readings are kept in the gateway's storage queue and sent when the connection returns, see [The storage queue is full](#the-storage-queue-is-full).

## A connector cannot reach the PLC

The gateway is online but one device has no values, or shows offline.

| Log message | Meaning | What to check |
|---|---|---|
| `Modbus read failed` | No answer, or an error answer | IP address, port (502), unit ID, serial settings |
| `the Modbus server cannot serve this value: …` | The PLC answered with a Modbus exception | Register address and function code. The gateway counts from 0, so register 40001 in a PLC manual is address 0 |
| `no read answered; marking the device offline` | Every read in a cycle failed | Network cable, PLC powered, polling period not too short |
| `OPC-UA connect failed` | The server refused or did not answer | Endpoint URL, security mode, user name and password, whether the server trusts the gateway's certificate |
| `node not found` | The node id in the mapping does not exist | Node id or browse path, namespace index |
| `the server offers no endpoint with the asked security; trying unsecured` | The security policy is not offered by the server | Pick a policy the server offers |
| `S7 connect failed` | The CPU refused or did not answer | IP address, rack and slot, PUT/GET access allowed in the CPU's protection settings |
| `S7 value decode failed` | The address or data type does not match the PLC | Data block number, offset, type |
| `connector failed to start` | The connector configuration is invalid | Open the connector in **Gateways** and save it again; check the line after it for the reason |

**Fix:** correct the connector in SENTIENT under **Gateways > (your gateway) > Connectors**. The gateway applies saved changes without a restart.

## A write (RPC) fails

You write a value from a dashboard or the RPC debug terminal, and the result is an error.

| Response | Meaning | Fix |
|---|---|---|
| `{"error": "Request timeout", "code": 408}` | The device is not connected to the gateway: its connector is stopped or disabled, or the device has not registered yet | Start the connector and wait for the device to send one value. The gateway waits 5 seconds by default, longer when the request sets `timeout` (at most 60 seconds) |
| `Method not found: no running connector handles '…'` (code 404) | No running connector matches the method name | Check the method name, and that the connector of that type is running |
| `connector not running` | The connector was found but is stopped | Start it |
| A timeout in the widget, no error from the gateway | The gateway is offline, or the write took longer than the widget's timeout | See [The gateway shows offline](#the-gateway-shows-offline); raise the widget's RPC timeout |
| A Modbus exception or `shared attribute could not be written` | The PLC refused the write | The register or node may be read-only, or the value out of range |

To make a key writable, add it to the connector's RPC section. You can create it straight from a read key, see [Write values to equipment](/docs/iot-gateway/rpc-write/).

## The storage queue is full

Error ID: [ST-GW-010](/docs/troubleshooting/errors/st-gw-010/)

The log shows `storage full — dropping new events until the backlog drains`.

The gateway stores readings while SENTIENT is unreachable. By default it keeps up to 10 files of 10,000 records each, 1 GB at most, and discards readings older than 7 days. Once the queue is full, **new** readings are dropped. Readings already stored are kept and sent first.

**Fix:**

- Restore the connection to SENTIENT. The queue drains on its own.
- For longer outages, raise the storage limits in the gateway's **General** configuration (storage section), and make sure the disk has room.
- Reduce the polling rate of connectors that do not need fast values.

## Sign-in to the local web page fails

Error ID: [ST-GW-011](/docs/troubleshooting/errors/st-gw-011/)

The page at `http://<gateway>:8642` is protected by its own password, separate from SENTIENT.

- `the default password from the network, refused` in the log: the default password works only on the gateway machine itself. Sign in there once and set your own password.
- Forgotten password: set a new one on the gateway machine with `sentient-gateway --ui-password -` (Docker: `docker exec -it st-gateway sentient-gateway --ui-password -`) and type it when asked.
- The password needs at least 8 characters. Common passwords and one character repeated are refused.
