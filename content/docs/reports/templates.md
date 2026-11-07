+++
title = "Report templates"
description = "Create, import, export and generate report templates: types, formats, page settings and report language."
weight = 88

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **report template** is the design of a report: its pages, charts and tables, and where their data comes from. Open **Reporting > Templates**.

## Create a template

Click **+** › **Create new report template** and set:

| Setting | Choices |
|---|---|
| **Name** | Unique in the tenant, for example `Boiler house daily` |
| **Type** | **Report**, which you generate and send, or **Subreport**, a block that other reports include, such as a common cover page |
| **Format** | **PDF**, **CSV**, **XLSX** (Excel), **ODS** (LibreOffice), or **Script** |
| **Description**, **Owner** | Optional |

The format cannot be changed afterwards. CSV, XLSX and ODS templates hold tables only, because a spreadsheet has no charts or pictures. A **Script** template is a small Rhai program that builds the document itself, see [Script reports](/docs/reports/export/#script-reports).

**Import report template** reads a template exported earlier as JSON.

## Template actions

Each row in the list has these actions:

- **Open report template** opens the [report builder](/docs/reports/builder/).
- **Generate report** asks for a time window and makes the report now. Progress is shown as it fetches data, renders the widgets and builds the PDF.
- **Schedule report** creates a [schedule](/docs/reports/scheduling/) for it.
- **Export report template** saves it as JSON, to import on another SENTIENT.
- **Copy report template Id**, and delete.

## Page and report settings

In the builder, the gear button opens **Settings**:

| Setting | Does |
|---|---|
| **Paper size**, **Orientation** (**Portrait** or **Landscape**), **Margins** | The page |
| **Background** | The page colour |
| **File name pattern** | The downloaded file's name. `{date}`, `{time}`, `{datetime}` and `{name}` are filled in, for example `{name}-{date}` |
| **Default date format** | How dates are written in the report |
| **Report language** | Titles, headings and text are translated into this language when the report is generated. **Language of the person who runs it** follows the user. Texts without a translation stay as written. See [Translations](/docs/administration/translations/) |

## Related

- [Report builder](/docs/reports/builder/)
- [Schedule and send reports](/docs/reports/scheduling/)
