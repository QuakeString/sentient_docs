+++
title = "Dashboards"
description = "Build, edit and share dashboards: widgets, layouts, states, aliases, filters, time window, languages and split views for control-room screens."
aliases = ["/docs/user-guide/ui/dashboards/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **dashboard** shows live and historical data in **widgets**: charts, gauges, tables, maps, buttons and [SCADA symbols](/docs/user-guide/scada/). Operators use dashboards on control-room screens, managers on their laptops, and maintenance staff in the mobile app.

Open **Dashboards** in the left menu. The list shows each dashboard's title, its owner and its groups.

![The dashboards list of the Demo Plant tenant](/images/st/dashboards-list.webp)

## Create a dashboard

1. Click **+**, then **Create new dashboard**.
2. Type a **Title**, and optionally a description and an image for the list.
3. Click **Add**. The new, empty dashboard opens in edit mode.

![A dashboard in view mode: four value cards and two 24-hour charts, with Edit mode at the top right](/images/st/dashboard-view.webp)

**Import dashboard** loads a dashboard exported as JSON; **Add from hub** takes a ready-made one from the [Solution hub](/docs/solution-hub/).

## Edit mode

Open a dashboard and click **Edit mode** (the pencil) at the top right. In edit mode:

![Edit mode: States and Layouts on the left; Add widget, settings, undo history, Close and Save on the right](/images/st/dashboard-edit-mode.webp)

- **Add widget** opens the widget library at the side. Search it, or open a bundle, and click a widget to add it. Then choose its data source, see [Widgets](/docs/user-guide/ui/widget-library/).
- Drag a widget to move it; drag its corner to resize it. Click a widget's pencil to change its data and appearance.
- Right-click the empty dashboard for **Undo** (Ctrl+Z), **Redo** (Ctrl+Y), select all, paste and more. Right-click a widget to copy, cut or delete it.
- **Save** keeps the changes; **Close** leaves edit mode and asks before throwing changes away.

Unsaved changes live only in this browser tab. Save often while you build a large dashboard.

![Adding a widget in edit mode](/images/st/dashboard-add-widget.webp)

## The toolbar

| Button | What it does |
|---|---|
| **Time window** | The period the widgets show: **Realtime** (for example the last 2 hours, moving on) or **History** (a fixed range), and how values are grouped. A widget can have its own time window instead |
| **Filters** | Narrow the entities a dashboard shows, for example only devices whose `zone` is `Boiler house` |
| **Entity aliases** | Edit mode only: names for "which entities", used by widgets, see below |
| **Layouts** | Edit mode only: a second layout on the right, separate layouts for breakpoints (desktop, tablet, phone), or a **SCADA** layout with a fixed grid for process screens |
| **States** | Edit mode only: the dashboard's pages, see below |
| **Settings** | Edit mode only: title, logo, toolbar, colours, mobile settings |
| **Language** | Shows the dashboard in another language, when it has [translations](/docs/administration/translations/) |
| **Export** | Downloads the dashboard as JSON, optionally with its images and resources embedded |
| **Version control** | Commits or restores the dashboard in Git, when [version control](/docs/user-guide/version-control/) is set up |

## Entity aliases

A widget does not name devices directly: it uses an **alias**, such as `Pumps` or `Selected pump`. The alias says how to find the entities: one named device, all devices of a profile, the devices related to an asset, the entity the user clicked, and so on. Change the alias, and every widget that uses it follows. Edit them under **Entity aliases** in edit mode.

## States

**States** are pages inside one dashboard, for example an overview of the plant and a detail page for one pump. A widget action, such as a click on a table row, opens another state and passes the clicked entity to it. The detail page then works for every pump: its widgets use an alias of the type **Entity from dashboard state**.

The **Root state** is the one that opens first. Add, rename and duplicate states under **States** in edit mode.

## Keep dashboards open in memory

Going back to a dashboard you just left is instant, because SENTIENT keeps recent dashboards running in the browser. Each kept dashboard uses memory (a large one 50–100 MB) and keeps receiving data. Under your initials › **Account** › **Profile**, **Dashboards kept in memory when you navigate away** sets how many: empty uses the server's default, `0` turns it off. The server limit is 10, set with the environment variable `DASHBOARD_KEEP_ALIVE_MAX`.

On an older control-room PC with little memory, set it to `1` or `0`.

## Show several dashboards on one screen

A **split view** shows two to four dashboards side by side, for a control-room screen. Click **+** in the dashboards list, then **Create split view**, give it a name, and choose:

- the **Layout**: **Side by side**, **Top and bottom**, **2 × 2**, **1 + 2** or **3 columns**;
- a dashboard, and optionally its state, for each pane. Drag the dividers to resize the panes;
- the **Time window**: **Same for all panes** or **Each pane its own**.

A split view can have several **pages**. With the **Slideshow** on, the screen shows them in turn, for example every 30 seconds. **Open in full screen (kiosk)** hides the menu for a wall screen.

## Share a dashboard

| Way | Who sees it |
|---|---|
| **Manage owner and groups** in the dashboard's row | Moves the dashboard to a customer, or adds it to dashboard groups that customers' users can see. Each user still sees only their own data |
| A user's **Default dashboard** | Opens right after that user signs in, see [Users](/docs/user-guide/ui/users/) |
| A customer's **Home dashboard** | Opens for all users of that customer without a default dashboard of their own |

## Delete

Click the bin in the dashboard's row. Its widgets go with it, and split views that show it get an empty pane; the devices and their data stay. It cannot be undone, so export important dashboards first.

## Related

- [Widgets](/docs/user-guide/ui/widget-library/)
- [SCADA](/docs/user-guide/scada/)
- [First device to dashboard](/docs/getting-started-guides/helloworld/)
