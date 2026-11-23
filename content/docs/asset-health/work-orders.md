+++
title = "Work orders"
description = "Turn a health finding into a work order, route it to the right team, record what was done, and export the equipment history."
weight = 154

[extra]
status = "checked"
checked = "4.3.0.57"
+++
The **Findings and work orders** widget, on the Overview and Machine pages of the Asset Health Monitoring dashboard, is where the maintenance team works.

## Findings

Each active finding shows its advice and evidence. You can **Acknowledge** it, add a **Comment**, or **Create work order**. Comments and actions are also written to the finding's [alarm](/docs/user-guide/alarms/), so the alarm's history tells the full story.

## Work orders

A work order moves through **Open**, **In progress**, **On hold** and **Done**, or **Cancelled**. A done order can be reopened. In its side panel you can:

- change the status;
- assign it to a team;
- record the **action taken**, with parts used, downtime and the outcome;
- read the activity log.

When the finding behind an open work order clears, the order gets a note saying so.

The [AI assistant](/docs/ai/assistant/) can also draft a work order (*Draft a work order for Pump 3*). It shows the draft, with the priority and team from your routing, and creates it only after you agree.

## Routing: who gets a work order

The server attribute `maintenanceRouting` decides who gets a work order. SENTIENT looks on the machine first, then on each asset above it (line, area, plant), then on the tenant, and uses the first rule that matches:

```json
{
  "rules": [
    { "minSeverity": "MAJOR", "alarmTypes": ["Asset health: "], "team": "Mechanical",
      "priority": "HIGH", "dueHours": 24, "autoCreate": true }
  ]
}
```

| Field | Means |
|---|---|
| `minSeverity` | The least severe alarm the rule takes |
| `alarmTypes` | Alarm type prefixes. Empty means all |
| `team`, `assigneeId` | Who gets the order |
| `priority` | `LOW`, `MEDIUM`, `HIGH` or `URGENT` |
| `dueHours` | Due this many hours after it is raised |
| `autoCreate` | Raise the order by itself when the alarm appears |

The Asset Health Monitoring solution sets up a routing to your maintenance team when you install it.

## Notifications

The solution adds a [notification rule](/docs/user-guide/notifications/#rules) that tells the tenant administrators, in SENTIENT and by email, when a major or critical finding is raised. Its alarm type is `Asset health: *`: a type ending in `*` matches every alarm type that starts with the text before it. Change the recipients or severities under **Notification center > Rules**.

## Equipment history

**Export history** downloads a machine's history (findings, actions taken, downtime and the health score over time) as a PDF report or as CSV, for audits and reliability reviews.

## Related

- [Asset health](/docs/asset-health/)
- [Working with alarms](/docs/user-guide/alarms/)
