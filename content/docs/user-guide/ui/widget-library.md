+++
title = "Widgets library"
description = "The widgets and widget bundles that come with SENTIENT, how to find the right one, and how to add, import or build your own."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
The **widgets library** holds every widget you can put on a [dashboard](/docs/user-guide/dashboards/). SENTIENT 4.3.0.57 ships about 1,350 widgets and symbols in 44 **bundles**. You add them from a dashboard in edit mode with **Add widget**; the library pages are for looking through them and for managing your own.

Open **Resources > Widgets library** in the left menu. It has two lists:

- **Widgets**: every widget, with a search box and a filter by type and bundle.
- **Widgets bundles**: the groups the widgets come in. Click a bundle to see its widgets.

## Kinds of widget

| Kind | Shows or does | Examples |
|---|---|---|
| **Latest values** | The newest value of one or more keys | Value cards, gauges, tank levels, status indicators |
| **Time series** | Values over the dashboard's time window | Line and bar charts, tables of history |
| **Control** | Sends commands to a device ([RPC](/docs/user-guide/rpc/)) or writes attributes | Switches, buttons, knobs, set-point inputs |
| **Alarm** | Lists and counts alarms | Alarms table, alarm count |
| **Static** | Fixed content | Text, HTML, images, navigation |

## Bundles that come with SENTIENT

| For | Bundles |
|---|---|
| Values and charts | Cards, Charts, Analogue gauges, Digital gauges, Count widgets, Tables, Status indicators, Date |
| Operating equipment | Control widgets, Buttons, Input widgets, GPIO widgets, Recipe widgets, SAF Control Widgets |
| Process screens | [SCADA](/docs/user-guide/scada/) symbol bundles: General high-performance SCADA symbols, High-performance SCADA energy system, fluid system and oil & gas, Traditional SCADA fluid system, Primitive Symbols |
| Drawings to standard | ISA-5.1 P&ID Symbols (221), IEC Electrical Symbols (245) |
| Plant equipment | Industrial widgets, Rotating Equipment, Valves, Liquid level, Material Handling, Combustion, Condition monitoring |
| Environment | Air quality, Indoor Environment, Outdoor Environment |
| Maps and navigation | Maps, Navigation widgets |
| Platform | Alarm widgets, Entity widgets, Entity admin widgets, Gateway widgets, Edge widgets, Home page widgets, Report widgets, HTML widgets, Utilities |

System bundles belong to the system administrator. Tenants use them but cannot change them; to change one, make your own copy (below).

## Find a widget

On a dashboard in edit mode, click **Add widget**, then type in the search box at the top of the panel (or press **/**). The search looks through all bundles by name and description. Click a bundle instead to look through it.

## Your own widgets and bundles

A tenant administrator can:

- **Create new widgets bundle** under **Widgets bundles** (**+**), to collect the widgets your plant uses, for example `Plant A standard`. On a dashboard, that bundle then appears with the system ones.
- **Import widget** or **Import widgets bundle** from a JSON file exported from another SENTIENT. Export works from the widget's or bundle's row.
- Make a changed copy of a widget: open it, change it, and choose **Save as**. The copy is yours; the system widget stays as it is and keeps getting updates.
- Build a widget from scratch with **+** › **Create new widget**: choose its kind, then write its HTML, CSS and JavaScript in the widget editor and try it on the right. See [Widget development](/docs/user-guide/contribution/widgets-development/).

## Related

- [Dashboards](/docs/user-guide/dashboards/)
- [SCADA](/docs/user-guide/scada/)
