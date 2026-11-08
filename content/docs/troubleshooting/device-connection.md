+++
title = "Devices do not connect"
description = "Find out why a device sends no data: credentials, ports, payload format and limits."
weight = 188

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A device that sends nothing shows **Inactive** in the device list and has no recent values on its **Latest telemetry** tab. Work through the checks below in order. Each one names the line the server writes to its log, so you can confirm the cause in [the server logs](/docs/troubleshooting/logs/).

## 1. The port is not reachable

Error ID: [ST-DEV-007](/docs/troubleshooting/errors/st-dev-007/)

SENTIENT listens for devices on these ports by default:

| Protocol | Port | Notes |
|---|---|---|
| HTTP | 8080 (TCP) | Same port as the web UI: `http://<server>:8080/api/v1/<token>/telemetry` |
| MQTT | 1883 (TCP) | MQTT 3.1, 3.1.1 and 5 on the same port |
| MQTT over TLS | 8883 (TCP) | Only when MQTTs is switched on and a certificate is configured |
| CoAP | 5683 (UDP) | |
| CoAP over DTLS | 5684 (UDP) | |

**Check:** from the device's network, test the port, for example `Test-NetConnection <server> -Port 1883` on Windows or `nc -vz <server> 1883` on Linux. If it fails, a firewall is in the way or the port is not published. See [Network ports](/docs/operations/ports/).

**Fix:**

- Open the port in the Windows or Linux firewall of the server, and in any firewall between the device and the server.
- With Docker, check that the port is published in your compose file (`ports:`).
- The system administrator can change or switch off each protocol under **Settings > General > Device connectivity**. Restart the server after changing a port.

## 2. MQTTs does not start

Error ID: [ST-DEV-008](/docs/troubleshooting/errors/st-dev-008/)

MQTT over TLS needs a certificate and its key. They are read from the environment variables `MQTT_SSL_PEM_CERT` and `MQTT_SSL_PEM_KEY` (and `MQTT_SSL_PEM_CA` for client certificates). When MQTTs is switched on but either file is missing, port 8883 stays closed.

**Fix:** set both variables to readable PEM files and restart the server.

## 3. Wrong credentials

Error ID: [ST-DEV-001](/docs/troubleshooting/errors/st-dev-001/)

The device must present the credentials shown on its **Manage credentials** dialog. Which field carries them depends on the credential type:

| Credential type | What the device sends |
|---|---|
| Access token | MQTT: the token as **user name**, no password. HTTP and CoAP: the token in the URL |
| MQTT Basic | Client ID, user name and password, all three must match |
| X.509 certificate | A client certificate whose Common Name matches the device's credential (MQTTs only) |

What you see when they are wrong:

- **MQTT:** the broker refuses the connection, and most clients report *not authorized* or *bad user name or password*. The server log shows `MQTT CONNECT rejected: auth failed` or `CONNECT rejected: empty username (access token required)`.
- **HTTP:** the request gets **401** with `{"error": "Invalid access token"}`.

**Common mistakes:**

- A space or line break copied with the token.
- The token sent as the MQTT password instead of the user name.
- The device was deleted and created again, which gives it a new token.
- An MQTT Basic device whose client ID differs from the one in its credentials.

After you correct a token, allow up to five minutes: a token that was tried and not found is remembered as invalid for that long. Restarting the device does not shorten this, but restarting the server does.

## 4. Payload format errors

Error ID: [ST-DEV-003](/docs/troubleshooting/errors/st-dev-003/)

The device connects but no values arrive.

**HTTP:** the server answers **400** with `Invalid JSON` and the parser's message. Fix the JSON the device sends.

**MQTT:** a bad message is dropped and the connection stays open, so the device does not notice. Check the log for `Invalid JSON payload`.

Payloads SENTIENT accepts on the telemetry topic `v1/devices/me/telemetry`:

```json
{"temperature": 21.5, "pressure": 6.1}
```

```json
{"ts": 1730880000000, "values": {"temperature": 21.5}}
```

```json
[{"ts": 1730880000000, "values": {"temperature": 21.5}},
 {"ts": 1730880060000, "values": {"temperature": 21.7}}]
```

**Common mistakes:**

- `ts` in seconds instead of milliseconds: the values are stored, but in January 1970, so charts of the last day look empty.
- Single quotes or a trailing comma (not valid JSON).
- A device profile set to **Protobuf** while the device sends JSON, or the other way round. Check the **Transport configuration** of the device profile.
- A device profile with custom MQTT topics while the device publishes to the default topic. The topics on the profile must match.
- A message larger than 10 MB.

## 5. Limits stop the data

Messages are refused when a limit is reached. Nothing is wrong with the device itself.

| Limit | What you see | Where to look |
|---|---|---|
| Transport rate limit of the tenant profile | MQTT: messages dropped, log line `Transport rate limit exceeded - message rejected` with `exceeded_by` = tenant, device or gateway | **Tenant profiles > Rate limits** |
| Usage limit reached (API usage) | HTTP **429**; MQTT messages dropped, log line `Transport feature disabled for tenant` | **API usage** page of the tenant |
| Licence device limit | New devices are not created, including devices a gateway or provisioning would add | [Licence errors](/docs/troubleshooting/licence-errors/) |

**Fix:** raise the limit on the tenant profile, wait for the usage period to reset, or reduce how often the device sends. A device that sends a value every 100 ms rarely needs to.

## 6. Still no data

- Open the device's **Latest telemetry** tab while the device sends. Values appear within a second when data reaches SENTIENT.
- If values arrive but a dashboard shows nothing, the problem is in the dashboard: check the widget's data source and time window.
- If values arrive but alarms or rules do nothing, check the device profile's rule chain and [the rule engine debug](/docs/user-guide/rule-engine-2-0/overview/).
- Devices behind a SENTIENT Gateway: see [Gateway errors](/docs/troubleshooting/gateway-errors/).
