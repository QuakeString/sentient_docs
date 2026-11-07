+++
title = "Working with alarms"
description = "See, acknowledge, assign, comment on and clear alarms in SENTIENT, and understand severity, status and propagation."
aliases = ["/docs/samples/alarms/basic-rules/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
An **alarm** tells operators that something on a device or asset needs attention, for example a high bearing temperature or a tank running low. [Alarm rules](/docs/user-guide/alarm-rules/) raise and clear alarms by themselves from the incoming data. Rule chains and the API can raise them too.

New alarms and changes reach every open SENTIENT page at once, without reloading: the alarm list, alarm widgets on dashboards, and the bell at the top right.

## The alarm list

Open **Alarms > Alarm list** in the left menu.

![The alarm list with three active alarms: originator, type, severity, assignee and status](/images/st/alarms-list.webp)

Each row shows the **Created time**, the **Originator** (the device or asset the alarm belongs to), the **Type**, the **Severity**, the **Assignee** and the **Status**. Click the originator to open it.

- **Filter** narrows the list by **Alarm status list**, **Alarm severity list**, **Alarm type list** and **Assignee**. **Search propagated alarms** also lists alarms raised on related entities (see [Propagation](#propagation)). By default the list shows active alarms.
- The time button limits the list to a period. **For all time** shows everything.
- The magnifier searches the list.

The same list appears in the **Alarms** tab of a device, asset or customer, limited to that entity. On dashboards, the **Alarms table** widget shows it with the same actions, and the **Alarm count** widget shows how many alarms match a filter.

## Acknowledge, assign and clear

| Action | Does |
|---|---|
| **Acknowledge** | Marks that someone has seen the alarm. The alarm stays active |
| **Assign** | Click the **Assignee** cell and pick a user. Only users who can see the originator can be assigned. **Assigned to me** in the filter finds your alarms |
| **Clear** | Closes the alarm. An alarm rule with a clear condition clears its alarms by itself once the values are back to normal |

Select several rows with the check boxes to acknowledge or clear them together.

## Details and comments

Click **⋯** in the **Details** column to open **Alarm details**: the originator, type, severity, start time, duration and status, with **Acknowledge** and **Clear**.

- **Details** shows the text that the alarm rule's **Alarm details** template filled in, for example the reading and the limit. **JSON** shows the raw data.
- **Open dashboard** opens the dashboard that the alarm names, when it names one.
- **Activity** holds the comments, newest or oldest first. Type in **Add a comment...** to leave a note for the next shift. SENTIENT adds its own entries when the alarm is acknowledged, assigned, cleared or changes severity. You can edit and delete your own comments. **Export to CSV** saves the activity.

## Severity

From most to least urgent: **Critical**, **Major**, **Minor**, **Warning**, **Indeterminate**. An alarm rule can raise its alarm at different severities for different conditions, and moves the alarm up or down as the values change.

## Status

An alarm is **Active** or **Cleared**, and **Acknowledged** or **Unacknowledged**, so its status is one of four: **Active Unacknowledged**, **Active Acknowledged**, **Cleared Unacknowledged** and **Cleared Acknowledged**.

## One alarm per problem

An originator has at most one active alarm of each type. While a "High temperature" alarm is active on a pump, new readings above the limit update that alarm instead of raising another one. Its **end time** moves forward with each update. Once it is cleared, the next reading above the limit raises a new alarm.

For example, with a rule that raises "High temperature" above 80 °C and clears it at 80 °C or below:

| Time | Reading | Alarm |
|---|---|---|
| 12:00 | 78 °C | None |
| 12:30 | 84 °C | Raised, start time 12:30 |
| 13:00 | 88 °C | Same alarm, updated |
| 13:30 | 76 °C | Cleared, end time 13:30 |

**Start time** is the time of the reading that crossed the limit. **Created time** is when SENTIENT processed it. They differ when a device sends stored readings late, for example after a network outage.

## Propagation

An alarm belongs to its originator. **Propagation** also shows it on other entities, so that, for example, a line asset lists the alarms of the machines on it. You set it in the alarm rule's **Advanced settings**:

- **Propagate alarm to related entities**, optionally only along some **Relation types**.
- **Propagate alarm to entity owner (Customer or Tenant)**, and **Propagate alarm to entity owners hierarchy**.
- **Propagate alarm to Tenant**.

Propagated alarms appear on those entities' **Alarms** tab and in alarm widgets that include them.

## Notifications

Who hears about an alarm, and how (web, email, SMS, Telegram, WhatsApp, mobile app), is set in the [notification center](/docs/user-guide/notifications/), including escalation to a supervisor when nobody acknowledges the alarm in time.

## Related

- [Alarm rules](/docs/user-guide/alarm-rules/)
- [Notification center](/docs/user-guide/notifications/)
