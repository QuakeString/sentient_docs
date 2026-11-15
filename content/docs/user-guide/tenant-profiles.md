+++
title = "Tenant profiles"
description = "Set what each tenant may use: entity counts, monthly quotas, data retention, rate limits, files, WebSocket sessions and AI."
aliases = ["/docs/user-guide/ui/tenant-profiles", "/docs/user-guide/ui/tenant-profiles/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **tenant profile** sets the limits for the [tenants](/docs/user-guide/ui/tenants/) that use it: how many devices they may add, how long their data is kept, how fast their devices may send. A single-plant installation can keep the `Default` profile, which is unlimited. Use profiles when one SENTIENT serves several plants or customers that must not slow each other down.

The system administrator manages them under **Tenant profiles** in the left menu. Each tenant has one profile, chosen in the tenant's details. A change to a profile applies to all its tenants at once.

## The licence comes first

Your SENTIENT [licence](/docs/installation/licence/) can also set limits, for example the number of devices. Where it does, the licence value replaces the profile's value for every tenant: you cannot raise a limit above the licence in a profile.

## Values

In every number field, **0 means unlimited**. Monthly quotas count from the first of the month and start again each month. When a tenant reaches 80 % of a quota, its state turns to warning; at 100 % that feature stops for the tenant until the next month or until you raise the quota. The tenant's [API usage](/docs/administration/api-usage/) page shows how far each counter is.

## Sections

| Section | What you set |
|---|---|
| **Entities** | The maximum number of devices, dashboards, assets, users, customers, rule chains and edges. At the limit, adding one more fails with, for example, "Devices limit reached" |
| **Rule Engine** | Monthly quotas for rule engine executions, transport messages, transport data points, JavaScript and Rhai script executions, and how many rule nodes one message may pass through |
| **Calculated fields** | Calculated fields per entity, arguments per field, data points in a rolling argument, and the size of a field's state |
| **Time-to-live** | How many days SENTIENT keeps time-series data (**Storage TTL days by default**), alarms, RPC commands, queue statistics and rule engine errors. Older data is deleted. **Data points storage days maximum number** is a monthly quota of stored data point-days |
| **Alarms and notifications** | Whether the tenant may send SMS, and monthly quotas for SMS, emails and created alarms |
| **Debug** | How long debug mode stays on for a rule node or calculated field before it switches off by itself |
| **Files** | Total size of resource files (images, JavaScript modules, SCADA symbols) and of [OTA packages](/docs/user-guide/ota-updates/), and the size of one resource file, in bytes |
| **WS** | WebSocket sessions and subscriptions per tenant, per customer and per user. Each open dashboard uses a session; each widget's data uses subscriptions |
| **Rate limits** | How fast devices, gateways, the REST API and other parts may go, below |
| **Report limits** | The number of [report](/docs/reports/) templates and schedules |
| **Data keys limits** | The number of different telemetry keys and attribute keys |
| **AI** | Whether the tenant may add its own AI models, use the system's models (with monthly token and per-minute request limits), and use the AI assistant, also for customer users |

## Rate limits

A rate limit is one or more pairs of **number of messages** per **seconds**, for example `100` per `1` and `1000` per `60`: at most 100 in any second and at most 1,000 in any minute. Click a limit to edit it, **Add limit** for another pair. Empty means no limit.

The most used:

| Limit | Applies to |
|---|---|
| **Transport tenant messages** | All messages from all the tenant's devices together |
| **Transport device messages** | Messages from one device |
| **Transport gateway messages** | Messages from one gateway, for all the devices behind it |
| **Transport tenant telemetry data points** | Values per second across the tenant |
| **REST requests for tenant** / **for customer** | Calls to the REST API by the tenant's users and API clients |

Over a transport limit, MQTT messages are dropped (the server logs a warning) and HTTP calls get `429 Too Many Requests`. See [Rate limits](/docs/user-guide/api-limits/).

## Add, default and delete

Click **+** to add a profile; give it a **Name** and set the sections. **Make tenant profile default** in a profile's row makes it the one new tenants get. A profile can only be deleted when no tenant uses it ("Cannot delete tenant profile. 2 tenant(s) are using this profile.") and it is not the default.

## Related

- [Tenants](/docs/user-guide/ui/tenants/)
- [API usage](/docs/administration/api-usage/)
- [Licence](/docs/installation/licence/)
