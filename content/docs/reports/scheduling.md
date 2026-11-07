+++
title = "Schedule and send reports"
description = "Generate reports by themselves at set times or when a value crosses a limit, and send them to people by email and in SENTIENT."
weight = 90

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **report schedule** generates a report from a template by itself and sends it to people. Open **Reporting > Scheduling**, or click **Schedule report** on a template.

## Create a schedule

Click **+** and set:

1. **Name**, and **Event type** **Generate Report**.
2. **Report template**, and the **Timezone** that the report's days and hours follow.
3. **Recipients**: one or more [recipient groups](/docs/user-guide/notifications/#recipients) from the notification center, or **Create new**. Optionally a notification template for the message that goes with the report.
4. When it runs: by time or by a trigger (below).
5. **Enable scheduler** and save.

## By time

Set the **Start time** and turn on **Repeat**. **Repeats** can be **Once**, **Daily**, **Every N days**, **Weekly** (on chosen days), **Every N weeks**, **Monthly**, **Yearly**, or **Timer-based** (every so many seconds, minutes or hours). **Ends on** stops the schedule at a date; leave it empty to keep it running.

For a daily shift report at 06:00, choose **Daily** with start time 06:00 in the plant's timezone.

## By a trigger

Turn on **Trigger** instead to generate the report when a value crosses a limit, for example a batch report when a batch ends. Choose the device or alias, then add **Trigger conditions**: a key, an operator (**Equals**, **Not equals**, **Greater than**, **Less than**, **Greater or equal**, **Less or equal**) and a **Constant** or **Another key** to compare with. With several conditions, any one of them fires the trigger.

In 4.3.0.57 a trigger reacts only to values posted through the REST API. From the release after 4.3.0.57 it also reacts to values that devices send over MQTT, HTTP or CoAP.

A schedule runs either by time or by trigger, not both.

## How people receive it

Each recipient gets the report:

- **By email**, with the report attached. Reports larger than 15 MB are sent as a download link instead. The server setting `REPORT_EMAIL_MAX_ATTACHMENT_MB` changes the limit. Email needs a working [mail server](/docs/user-guide/ui/mail-settings/).
- **In SENTIENT**, as a notification in the bell with a link to the report.

Every generated report is also listed under **Reporting > Reports**.

## Manage schedules

The list shows each schedule's **Last Execution**, **Next Execution** and whether it is **Enabled**. **Enable** and **Disable** pause it without deleting it; **Export scheduler events** saves the selected ones as JSON.

The same scheduler also runs other jobs, such as writing attributes or sending commands to devices at set times. See [Scheduler](/docs/user-guide/scheduler/).

## Related

- [Report templates](/docs/reports/templates/)
- [PDF and spreadsheet export](/docs/reports/export/)
