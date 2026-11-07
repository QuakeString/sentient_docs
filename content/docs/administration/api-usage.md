+++
title = "API usage and limits"
description = "See how much of each monthly quota a tenant has used, what each counter counts, and what stops when a quota runs out."
weight = 175

[extra]
status = "checked"
checked = "4.3.0.57"
+++
**API usage** shows what a tenant has used this month against the quotas in its [tenant profile](/docs/user-guide/tenant-profiles/): device messages, stored data, rule engine and script executions, alarms, reports and messages sent.

Open **API usage** in the left menu as a tenant administrator. Quotas are set by the system administrator in the tenant profile.

## The overview

The first screen has one card per counter, each with this month's value, the quota (empty when unlimited) and a status:

| Status | Meaning |
|---|---|
| **Enabled** | Below the warning threshold |
| **Warning** | Over the warning threshold, by default 80 % of the quota. The feature still works |
| **Disabled** | The quota is used up. The feature has stopped for the tenant |

Below the cards, charts show the last hours of device messages, device data points, rule engine executions and storage data point-days. **View details** on a card opens that counter's hourly, daily and monthly charts.

## The counters

| Counter | Counts |
|---|---|
| **Transport messages** | Messages received from devices and gateways over MQTT, HTTP, CoAP and the other transports. A message with ten values counts once |
| **Transport data points** | Values received from devices. A message with ten values counts ten |
| **Data points storage days** | Stored values multiplied by the days they are kept, so data kept longer counts more |
| **Rule Engine executions** | Rule nodes run on messages |
| **JavaScript executions** / **Rhai executions** | Script runs in rule nodes, calculated fields and converters |
| **Alarms created** | New alarms |
| **Created reports** | Reports generated |
| **Emails**, **SMS**, **WhatsApp messages**, **Telegram messages** | Messages sent by rule nodes and notifications |

**Rule Engine Statistics**, from **View statistics**, shows each queue's successful, failed and timed-out messages and the latest rule engine errors. Use it when messages pile up or go missing.

## When a quota runs out

Quotas count from the first day of the month and start again each month. At 100 % the feature stops for that tenant until the next month or until the system administrator raises the quota in the tenant profile:

| Disabled | Effect |
|---|---|
| Transport | Device messages are rejected |
| Storage | Telemetry is no longer saved |
| Rule Engine | Messages are no longer processed by rule chains |
| Alarms | No new alarms are created |
| Email, SMS | Messages are no longer sent |

A quota of **0** means unlimited. The default tenant profile is unlimited, so a single-plant installation never reaches a quota unless you set one.

> Quotas are different from **rate limits**, which cap how fast messages arrive (for example 100 per second) rather than how many arrive in a month. See [Rate limits](/docs/user-guide/api-limits/).

## Related

- [Tenant profiles](/docs/user-guide/tenant-profiles/)
- [Rate limits](/docs/user-guide/api-limits/)
