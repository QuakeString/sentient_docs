+++
title = "Task manager"
description = "Follow the background tasks SENTIENT runs for a tenant, such as reprocessing calculated fields and cleaning up the data of deleted entities."
weight = 178

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Some work takes longer than a click: recalculating a calculated field over months of history, or removing all the telemetry, attributes and alarms of a deleted device. SENTIENT runs such work as a **task** in the background. Tasks survive a restart: if the server stops halfway, the task is picked up again and failed steps are retried.

Open **Features > Task manager** in the left menu as a tenant administrator.

## The task list

| Column | Shows |
|---|---|
| **Created time** | When the task was started |
| **Type** | What the task does, below |
| **Entity** | The entity the task works on |
| **Status** | **Queued**, **Pending**, **Running**, **Completed**, **Failed** or **Cancelled** |
| **Progress** | Successful and failed entities out of the total, while running and after |

Use the filter button to show only some **Task types** or **Statuses**, and the search box to find a task by name. Each row has:

- **Task parameters**: what the task was started with, for example the calculated field and the time range to reprocess.
- **Task info**: the result, with the time taken, the number of entities that succeeded and failed, and the errors.
- **Delete**: removes the task from the list. Deleting a finished task does not undo its work.

## Task types

| Type | Started by |
|---|---|
| **Calculated field reprocessing** | **Reprocess** on a [calculated field](/docs/user-guide/calculated-fields/), with a **Time window**, to recalculate its output over a past time range. The reprocess dialog shows the progress and can **Cancel reprocessing** or retry the entities that failed |
| **Entity cleanup** | Deleting a device, asset or other entity. The entity disappears at once; its stored telemetry, attributes and other data are removed by this task afterwards |

## Related

- [Calculated fields](/docs/user-guide/calculated-fields/)
- [Audit log](/docs/user-guide/audit-log/)
