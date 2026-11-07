+++
title = "Glossary"
description = "Terms used in SENTIENT and in this manual, from alarms and assets to tenants, with the industrial terms that come up when you connect plants."
weight = 216

[extra]
status = "checked"
checked = "4.3.0.57"
+++
## Platform terms

| Term | Meaning |
|---|---|
| **Access token** | The secret a device uses to identify itself when it sends data. Each device has its own. See [Device credentials](/docs/user-guide/device-credentials/). |
| **Alarm** | A problem SENTIENT raised for an entity, with a type, a severity (Critical, Major, Minor, Warning, Indeterminate) and a state (active or cleared, acknowledged or not). See [Alarms](/docs/user-guide/alarms/). |
| **Alarm rule** | The condition, set on a device or asset profile, that raises and clears an alarm. See [Alarm rules](/docs/user-guide/alarm-rules/). |
| **Alias** | A named way for a dashboard to find its entities, such as "the device chosen in the list" or "all pumps". Widgets refer to aliases, not to fixed devices. See [Aliases](/docs/user-guide/ui/aliases/). |
| **API usage** | A tenant's use of its monthly quotas: device messages, stored data, rule engine executions, e-mails and more. See [API usage and limits](/docs/administration/api-usage/). |
| **Asset** | Something that is not a device but groups or describes devices, such as a plant, a line or a machine. See [Assets](/docs/user-guide/ui/assets/). |
| **Attribute** | A value that describes an entity and changes rarely, such as a serial number or a set point. Attributes are client, server or shared. See [Attributes](/docs/user-guide/attributes/). |
| **Calculated field** | A value SENTIENT computes from other values as they arrive, for example power from voltage and current. See [Calculated fields](/docs/user-guide/calculated-fields/). |
| **Customer** | A group of users inside a tenant who see only what is assigned or shared with them, for example a client or a department. See [Customers](/docs/user-guide/ui/customers/). |
| **Dashboard** | A screen of widgets showing live and historical data, and controls to act on equipment. See [Dashboards](/docs/dashboards/). |
| **Device** | Anything that sends data to SENTIENT or receives commands from it: a sensor, a PLC, a meter, a gateway. See [Devices](/docs/user-guide/ui/devices/). |
| **Device profile** | Settings shared by devices of one kind: how they connect, their alarm rules, and which rule chain handles their data. See [Device profiles](/docs/user-guide/device-profiles/). |
| **Entity** | Any item SENTIENT stores: devices, assets, customers, users, dashboards, rule chains and so on. |
| **Entity group** | A named set of entities of one kind, used to give permissions and share entities. See [Entity groups](/docs/administration/entity-groups/). |
| **Entity view** | A limited view of a device or asset that shows only some of its keys, for sharing with a customer. See [Entity views](/docs/user-guide/entity-views/). |
| **Error ID** | The stable code of a SENTIENT error, such as `ST-LIC-002`. See the [error catalogue](/docs/troubleshooting/errors/). |
| **Gateway** | A program that reads PLCs and other equipment over industrial protocols and forwards the data to SENTIENT as many devices over one connection. See [SENTIENT Gateway](/docs/iot-gateway/). |
| **Key** | The name of a value, such as `temperature`. Telemetry and attributes are stored as key and value. |
| **Licence** | The key that allows SENTIENT to run, with its limits and expiry, bound to one machine. See [Licence](/docs/installation/licence/). |
| **Platform Manager** | The program that installs, updates, backs up and repairs SENTIENT on Windows and Linux. See [Install on Windows](/docs/installation/windows/). |
| **Recipe** | A set of set points for one product or batch, sent to a machine in one step. See [Recipes](/docs/user-guide/recipes/). |
| **Relation** | A link between two entities, such as "Plant contains Line 1". Dashboards and rule chains follow relations. See [Entities and relations](/docs/user-guide/entities-and-relations/). |
| **Role** | What a user may see and do. Users get roles through their user group. See [Roles and permissions](/docs/administration/roles/). |
| **RPC** | A command sent to a device, such as "open valve" or "write set point 75". See [Remote commands (RPC)](/docs/user-guide/rpc/). |
| **Rule chain** | A flow of rule nodes that processes every incoming message: filter, transform, save, raise alarms, notify, call other systems. See [Rule engine](/docs/user-guide/rule-engine-2-0/re-getting-started/). |
| **SCADA symbol** | An animated drawing of equipment, such as a pump, valve or tank, that shows live state on a SCADA dashboard. See [SCADA](/docs/user-guide/scada/). |
| **Secret** | A password, token or key stored once, encrypted, and referred to as `${secret:name}`. See [Secrets](/docs/administration/secrets/). |
| **Shared attribute** | An attribute set in SENTIENT that the device receives, used for configuration and set points. |
| **Solution hub** | Ready-made rule chains and data pipelines you install with one click. See [Solution hub](/docs/solution-hub/). |
| **Telemetry** (time series) | Values a device sends over time, each with a timestamp, such as temperature every second. See [Time series data](/docs/user-guide/telemetry/). |
| **Tenant** | A separate organisation in SENTIENT with its own devices, users and data. A single plant usually has one. See [Tenants](/docs/user-guide/ui/tenants/). |
| **Tenant profile** | The limits shared by tenants of one kind: entity counts, monthly quotas, rate limits and data retention. See [Tenant profiles](/docs/user-guide/tenant-profiles/). |
| **Widget** | One element of a dashboard: a chart, gauge, table, map, button, SCADA symbol and so on. See [Widgets library](/docs/user-guide/ui/widget-library/). |

## Industrial terms

| Term | Meaning |
|---|---|
| **Data block (DB)** | A memory area of a Siemens S7 PLC holding variables at fixed addresses, such as `DB1.DBD0`. See [Siemens S7](/docs/iot-gateway/config/s7/). |
| **Function code** | In Modbus, the kind of read or write: 1 coils, 2 discrete inputs, 3 holding registers, 4 input registers, 5 and 15 write coils, 6 and 16 write registers. |
| **Holding register** | A 16-bit Modbus value the master can read and write, often numbered from 40001 in PLC manuals. See [Modbus](/docs/iot-gateway/config/modbus/). |
| **Node ID** | The address of a value on an OPC UA server, such as `ns=2;s=Line1.Pump1.Speed`. See [OPC UA](/docs/iot-gateway/config/opc-ua/). |
| **Polling period** | How often the gateway reads a value from equipment. Shorter periods give fresher values and more load. |
| **Rack and slot** | Where a Siemens CPU sits in its rack. The gateway needs them to connect: rack 0, slot 1 for S7-1200 and S7-1500. |
| **Set point** | A target value written to a controller, such as a temperature or speed. |
| **Tag** | A named value in a PLC or SCADA system. In SENTIENT a tag usually becomes a telemetry key or attribute. |
| **Unit ID** (slave ID) | The address of one device on a Modbus bus or behind a Modbus gateway. |

## Related

- [Architecture](/docs/reference/architecture/)
- [Error catalogue](/docs/troubleshooting/errors/)
