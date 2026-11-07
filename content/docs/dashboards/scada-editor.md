+++
title = "SCADA symbol editor"
description = "Turn an SVG drawing into a live SCADA symbol inside SENTIENT: tags, behaviors, properties, the state render function, preview, and a widget for dashboards."
weight = 75

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT's built-in symbols cover most plant equipment (see [Industrial equipment widgets](/docs/dashboards/industrial-widgets/) and [SCADA dashboards](/docs/user-guide/scada/)). When you need your own, for example a machine drawn the way your operators know it, draw it in any vector editor and make it live in the **SCADA symbol editor**.

## Open the editor

1. Go to **Resources > SCADA symbols**.
2. Click **+** and **Upload SCADA symbol**, and choose the SVG file. Or click an existing symbol. With **Include system symbols** on, the built-in symbols are listed too; open one to study how it is made.
3. The editor opens with the drawing on the left and its settings on the right.

The drawing can be shown as the picture (**SVG**) or as its code (**XML**). **Show hidden elements** reveals parts that are hidden until the data says otherwise, for example a fault outline.

## The settings

| Tab | What you set |
|---|---|
| **General** | **Title**, **Description**, **Search tags** (words that find it in **Add widget**), **Widget size** in columns and rows, and the **State render function**: a script that runs on every data change and can redraw the whole symbol |
| **Tags** | Names for parts of the drawing. Click a part, then **Add tag**, for example `rotor` or `flame`. A tag can have its own **On click action**, **On press action** and **On release action**, and its own script that changes that part |
| **Behavior** | What a dashboard user connects to data. A **Value** behavior reads a value (for example *Running* from a time series); an **Action** behavior writes one (for example *Start* through an RPC); a **Widget action** behavior runs the action the dashboard user picks for it, such as opening a state or another dashboard |
| **Properties** | The settings a dashboard user can change without code, such as colours, labels, limits or which parts to draw |

Each behavior has an **Id** that the scripts use, a **Name** the user sees, a **Value type** and a **Default value**. Ids must be unique.

## Try it

Click **Preview**. Give each behavior a test value and change the properties to see the drawing respond. Clicking a tag with an action shows a message that the action was invoked. **Back** returns to the editor. **Apply** saves the symbol; **Decline** drops your changes.

## Use it on dashboards

Click **Create widget**. The symbol becomes a widget in your tenant's widget library, with its behaviors and properties as the widget's settings. Add it to a dashboard like any other widget.

A symbol made by the system administrator is a system symbol: every tenant sees it and can use it. A tenant's own symbols stay in that tenant. To move a symbol between servers, use **Export SCADA symbol to JSON** and **Import SCADA symbol from JSON**, or **Download SCADA symbol** for the bare SVG.

## Good habits

- Draw at the size it will be shown, with a `viewBox`, and keep text as text, not paths, so labels stay sharp.
- Give each moving part its own group in the drawing, and tag the groups, not single shapes.
- Put limits and colours in **Properties** rather than in the script, so the same symbol works on every screen.
- Keep animations light. Dozens of animated symbols on one screen add up; animate only what the operator needs to see move.

## Related

- [SCADA dashboards](/docs/user-guide/scada/)
- [SCADA symbol development guide](/docs/user-guide/scada/scada-symbols-dev-guide/)
- [Industrial equipment widgets](/docs/dashboards/industrial-widgets/)
