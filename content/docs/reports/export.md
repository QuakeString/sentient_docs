+++
title = "PDF and spreadsheet export"
description = "Find, download, view, compare and share generated reports; the PDF, CSV, XLSX and ODS formats; and script reports written in Rhai."
weight = 91

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Every report SENTIENT generates, on demand or by a schedule, is kept under **Reporting > Reports**.

## The report list

Each row shows the **Created time**, **File name**, **Report template**, the **User** who ran it, the **Format** and the **Status**: **Pending**, **Generating**, **Completed** or **Failed**.

| Action | Does |
|---|---|
| **Download** | Saves the file. For a report with several documents, choose one of them or **All formats (ZIP)** |
| **View report** | Opens a PDF in the browser |
| **Split View** | Select two or more completed PDF reports to see them side by side, for example this week's against last week's |
| **Make report public** | Gives the report a public link that anyone can download without signing in. **Copy public link** copies it; **Make report private** stops the link working |
| **Export reports** | Downloads the selected reports together |

> A public link works for anyone who has it. Use it for reports you would also send by email, never for confidential data.

## Formats

| Format | Holds | Best for |
|---|---|---|
| **PDF** | Every component: text, images, tables, charts, shapes, dashboards | Printing, sending, archiving |
| **XLSX** (Excel), **ODS** (LibreOffice) | Tables, one per sheet | Further calculation |
| **CSV** | Tables as plain text | Other software |
| **Script** | Whatever the script builds (below) | Layouts that depend on the data |

## Script reports

A **Script** template is a small Rhai program that builds the document itself. Use it when the layout depends on the data, for example one sheet per machine or a section per batch, or when you prefer code to the builder.

In the script editor:

- **Time window** is the period the report covers. The script sees it as `ctx.startTs` and `ctx.endTs`, with `ctx.timezone`.
- **Arguments** fetch data before the script runs and hand it over as plain variables, the way [calculated fields](/docs/user-guide/calculated-fields/) do. Types: **Timeseries**, **Timeseries (sampled)** (one row per interval with each key's last value), **Latest value**, **Attributes**, **Batches** and **Fleet batches** (from an event / batch analysis definition). Change a report's device by editing its argument, not the code.
- **Test script** runs it on the server against live data and shows errors and a preview, without generating a report.

The output follows the code: `workbook()` builds an Excel workbook, `csv(text)` a CSV file, `pdf()` renders the workbook's sheets as PDF tables. A script that makes several documents produces a ZIP. For example, with a **Timeseries (sampled)** argument `flow` (key `flow`, every hour):

```rhai
let wb = workbook();
let sh = wb.sheet("Flow");
sh.row(0, ["Time", "Flow (m³/h)"], #{bold: true});
let r = 1;
for p in flow {
    sh.row(r, [fmt_ts(p.ts, ctx.timezone), p.flow]);
    r += 1;
}
```

## Related

- [Report templates](/docs/reports/templates/)
- [Schedule and send reports](/docs/reports/scheduling/)
