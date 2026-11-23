+++
title = "Report builder"
description = "Lay out a report page by page: text, images, tables, charts, shapes, dashboards and subreports, with their data and appearance."
weight = 89

[extra]
status = "checked"
checked = "4.3.0.57"
+++
The **report builder** lays out a report the way it will be printed. Open it from **Reporting > Templates** with **Open report template**.

## The screen

- **Report components** on the left lists what you can add. **Search components** finds one, and **Favorites & Recent** keeps the ones you use most (the star adds a favourite). **Hide components** makes room.
- The page in the middle has a **Header**, the **Content** and a **Footer**, plus a **First page header** and **First page footer** for a different cover page. Each can be switched off.
- The toolbar holds **Aliases** and **Filters** (where the data comes from, as on dashboards), **Version control**, **Generate test report**, **Settings**, zoom (**Zoom in**, **Zoom out**, **Fit width**, **100% (True size)**) and full screen.

Drag a component from the left onto the page. Click it to select it, double-click to edit it, **Ctrl+C** copies it and **Del** removes it. Drag its edges to resize it.

## Components

| Group | Components |
|---|---|
| **Text & Images** | Rich text, Image |
| **Tables** | Entity table, Alarm table, Time series table, Batch analysis |
| **Charts** | Time series chart, Line chart, Bar chart, Bar chart with labels, State chart, Range chart, Bars, Pie, Doughnut, Horizontal doughnut |
| **Info & Layout** | Created time, Page number, Divider, Page break |
| **Primitive Shapes** | Line, Rectangle, Circle, Ellipse, Triangle, Hexagon, Star, Arrow |
| **Advanced** | **Dashboard** (a dashboard drawn into the report), **Subreport** (a subreport template, such as a shared cover page) |

Spreadsheet templates (CSV, XLSX, ODS) offer only the **Tables** group.

## Data

Tables and charts take their data the way dashboard widgets do: an entity alias, for example one device, all pumps of a profile or the devices of an asset, and the keys to show. If the template has no alias yet, add one under **Aliases** first.

**Use report time window** (on by default) makes a component cover the period chosen when the report is generated. Turn it off to give the component its own period, for example a 30-day trend in a daily report.

The **Batch analysis** table reports production batches or cycles found by an [event / batch analysis](/docs/user-guide/calculated-fields/) calculated field: per-batch values, phases, deviations and summaries.

## Appearance

Each component's editor has tabs for its data, its appearance (fonts, colours, borders, thresholds that colour values), and its layout on the page. Charts also set their axes and series. **Basic mode** and **Advanced mode** switch between the common settings and all of them.

## Try it and save

**Generate test report** builds the report from live data so you can see it as it will look. **Save** keeps your changes; **Decline** drops them. With **Version control** set up, each saved version can be compared and restored.

## Related

- [Report templates](/docs/reports/templates/)
- [PDF and spreadsheet export](/docs/reports/export/)
