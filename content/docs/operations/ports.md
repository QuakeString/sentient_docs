+++
title = "Ports and firewall"
description = "Network ports SENTIENT, its databases and SENTIENT Gateway use, and which ones to open."
weight = 18

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Open only the ports that people and devices actually need. The database ports must never be reachable from the plant network or the internet.

## SENTIENT server

| Port | Protocol | Used for | Open to |
|---|---|---|---|
| 8080 | TCP | Web UI, REST API and WebSocket (live values, alarms) | Users, gateways, integrations |
| 1883 | TCP | MQTT for devices and gateways | Devices and gateways |
| 8883 | TCP | MQTT over TLS | Devices and gateways |
| 5683 | UDP | CoAP | CoAP devices only |
| 5684 | UDP | CoAP over DTLS. Starts only after you configure certificates. | CoAP devices only |

The installation also makes **outgoing** HTTPS connections to `license.invenia.in` to activate the licence, and then about once an hour for the licence heartbeat. See [Activate your licence](/docs/installation/licence/).

## Databases

| Port | Service | Open to |
|---|---|---|
| 5432 | PostgreSQL | Nobody outside the server |
| 8123, 9000 | ClickHouse (HTTP and native) | Nobody outside the server |

<div class="st-callout warn">

The Docker Compose files publish 5432, and also 8123 and 9000 in the ClickHouse file, on the host so that you can run maintenance tools. They use the default password `sentient`. On a server that others can reach, either block these ports in the host firewall, or delete their `ports:` lines from the compose file. The SENTIENT container reaches its databases over Docker's internal network and doesn't need them published.

</div>

## SENTIENT Gateway

| Port | Used for | Open to |
|---|---|---|
| 8642 | Gateway admin UI (when it is turned on) | Engineers who configure the gateway |

The gateway connects **out** to SENTIENT on MQTT (1883 or 8883), so the SENTIENT server never needs to reach the gateway. The gateway also needs network access to your PLCs and field devices on their own ports, for example 502 for Modbus TCP, 102 for Siemens S7 and 4840 for OPC UA.

## Change a port

With Docker, change the left-hand number in the `ports:` mapping. For example, `"8090:8080"` serves the web UI on 8090. The container side stays the same.
