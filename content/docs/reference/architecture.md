+++
title = "Architecture"
description = "How SENTIENT is built: one server program with its database, the optional services around it, and the path a value takes from a device to a dashboard."


aliases = ["/docs/reference/iot-platform-deployment-scenarios/", "/docs/reference/mcp-server/", "/docs/reference/monolithic/", "/docs/reference/msa/", "/docs/reference/performance/", "/docs/reference/performance/tools/java-jmx-monitoring/", "/docs/reference/performance/tools/postgres-pgadmin-monitoring/", "/docs/reference/performance/tools/sentient-performance-charts/", "/docs/reference/performance-aws-instances/", "/docs/reference/1m-devices-test/", "/docs/reference/20k-devices-test/", "/docs/reference/performance-tests/", "/docs/reference/performance-tools/"]
[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT is one server program, written in Rust, with its database next to it. The web UI, the REST API, the device connections, the rule engine and every background job run inside that program, so a plant runs SENTIENT on one machine without a cluster to look after.

{{ diagram(name="architecture") }}

## The parts

| Part | What it does | Runs as |
|---|---|---|
| **SENTIENT server** | Web UI, REST and WebSocket API, device transports, rule engine, alarms, notifications, reports, scheduler, analytics | One program: `sentient` container, or the SENTIENT service on Windows and Linux |
| **PostgreSQL** | Devices, assets, dashboards, users, alarms, attributes and all other configuration. Also telemetry, unless ClickHouse holds it | Its own container or service |
| **TimescaleDB** (optional) | PostgreSQL extension that compresses telemetry history | Inside PostgreSQL |
| **ClickHouse** (optional) | Column store for telemetry history and latest values at high rates | Its own container; on Windows inside WSL2 |
| **SENTIENT translator** (optional) | Offline translation of your dashboards' texts | Its own container, on this or another machine |
| **SENTIENT Gateway** | Reads PLCs and other equipment over industrial protocols and forwards their data | Separate program near the equipment |
| **Platform Manager** | Installs, updates, backs up and repairs the server | Desktop program on the server |

The licence server at `license.invenia.in` is contacted to activate the [licence](/docs/installation/licence/).

## From a device to a dashboard

1. **Transport.** A device or gateway connects over MQTT (port 1883, or 8883 with TLS), HTTP (port 8080), CoAP (5683, or 5684 with DTLS) or SNMP, or data arrives from a cloud [integration](/docs/user-guide/integrations/). The transport checks the device's credentials, the [rate limits](/docs/user-guide/api-limits/) and the tenant's [quotas](/docs/administration/api-usage/), and turns the payload into a message.
2. **Device.** Each device has an actor inside the server that tracks whether it is active, its sessions and pending commands.
3. **Queue.** The message goes to a rule engine queue: **Main** by default, or another queue such as **HighPriority** chosen in the device profile. Queues set how messages are retried and in what order. See [Queues](/docs/user-guide/rule-engine-2-5/queues/).
4. **Rule chain.** The device profile's rule chain processes the message: it filters, transforms and enriches it, saves telemetry and attributes, raises [alarms](/docs/user-guide/alarms/), sends notifications and calls other systems. [Calculated fields](/docs/user-guide/calculated-fields/) and [alarm rules](/docs/user-guide/alarm-rules/) run on the values too.
5. **Storage.** Values are written in batches: history to PostgreSQL, TimescaleDB or ClickHouse; latest values to PostgreSQL, or to ClickHouse with a memory cache. See [Performance tuning](/docs/operations/tuning/).
6. **Dashboard.** Open dashboards keep a WebSocket connection to the server and subscribe to the values their widgets show. A new value, or an alarm change, is pushed to them at once; nothing polls.

Commands go the other way: a widget or a [scheduler](/docs/user-guide/scheduler/) event sends an [RPC](/docs/user-guide/rpc/) or writes a shared attribute, the rule chain passes it on, and the transport delivers it to the device or gateway.

## Tenants and isolation

All data belongs to a [tenant](/docs/user-guide/ui/tenants/). Each tenant has its own devices, rule chains, dashboards, users and limits, and cannot see another tenant's data. Inside a tenant, [customers](/docs/user-guide/ui/customers/), [roles](/docs/administration/roles/) and [entity groups](/docs/administration/entity-groups/) decide which user sees what.

## Compatibility

SENTIENT uses widely supported open device protocols and a documented REST API, so existing devices, gateways and client libraries for that API work with it unchanged. See the [device APIs](/docs/reference/protocols/) and the [REST API](/docs/reference/rest-api/).

## Related

- [System requirements](/docs/installation/requirements/)
- [Ports and firewall](/docs/operations/ports/)
- [Environment settings](/docs/operations/settings/)
