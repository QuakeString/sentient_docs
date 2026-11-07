+++
title = "Reports"
description = "Make PDF and spreadsheet reports from your plant data: design them once, generate them on demand or on a schedule, and send them to people."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT makes reports from the same data your dashboards show: a daily production report as PDF, a monthly energy table as Excel, a batch record per shift. You design a report once as a **template**, then generate it whenever you need it, or let a **schedule** generate it and send it to people.

Open **Reporting** in the left menu. It has three pages:

| Page | What it is for |
|---|---|
| **Templates** | The report designs. Each has a format (PDF, CSV, XLSX, ODS or Script) and is laid out in the [report builder](/docs/reports/builder/) |
| **Scheduling** | [Schedules](/docs/reports/scheduling/) that generate reports at set times, or when a value crosses a limit, and send them |
| **Reports** | Every generated report: download, view, compare and share them. See [Export](/docs/reports/export/) |

## A first report in five minutes

1. In **Reporting > Templates**, click **+** › **Create new report template**. Name it, keep **Type** **Report** and **Format** **PDF**, and click **Add**.
2. The [report builder](/docs/reports/builder/) opens. Drag a **Time series chart** and a **Time series table** from **Report components** onto the page, and choose the device and keys for each.
3. Click **Generate test report** to see the PDF, then **Save**.
4. Back in **Templates**, **Generate report** asks for the time window, for example the last 24 hours, and makes the report. **Schedule report** makes it every day by itself.

## Reports on dashboards

The **Report launcher** widget, in the **Report widgets** bundle, lets dashboard users generate reports without opening the reporting pages. In its settings, choose the **Report templates** it offers (empty offers every template the user may use), **Download automatically when ready**, and **Show my recent reports**.

## In this section

- [Report templates](/docs/reports/templates/)
- [Report builder](/docs/reports/builder/)
- [Schedule and send reports](/docs/reports/scheduling/)
- [PDF and spreadsheet export](/docs/reports/export/)
