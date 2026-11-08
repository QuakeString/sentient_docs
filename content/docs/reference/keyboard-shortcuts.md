+++
title = "Keyboard shortcuts"
description = "Every keyboard shortcut in the SENTIENT web UI: search anywhere, the dashboard editor, SCADA layouts, the rule chain editor and the widget editor."
weight = 90

[extra]
status = "checked"
checked = "4.3.0.57"
+++
On a Mac, use **Cmd** wherever this page says **Ctrl**. Shortcuts do not fire while you type in a text field, so **Ctrl+A** in a search box still selects its text.

## Anywhere

| Keys | Does |
|---|---|
| **Ctrl+K** | Open or close the search palette |
| **/** | Open the search palette (not while typing in a field) |

In the search palette:

| Keys | Does |
|---|---|
| **↑** **↓** | Move through the results |
| **Enter** | Open the result |
| **Ctrl+Enter** | Open the result in a new tab |
| **Esc** | Close the palette |
| **?** | List the search filters |

Type a filter before your search to narrow it: **>** commands, **p:** pages, **d:** devices, **g:** gateways, **a:** assets, **db:** dashboards, **ev:** entity views, **c:** customers, **u:** users, **rc:** rule chains, and **t:** tenants (system administrator). For example `d: pump` finds devices named like *pump*.

## Dashboard editor

These work in edit mode, with widgets selected and no widget dialog open.

| Keys | Does |
|---|---|
| **Ctrl+S** | Save and stay in edit mode (the **Save** button saves and leaves edit mode) |
| **Ctrl+Z** | Undo |
| **Ctrl+Y** or **Ctrl+Shift+Z** | Redo |
| **Ctrl+A** | Select all widgets |
| **Ctrl+C** | Copy the selected widgets |
| **Ctrl+V** | Paste copied widgets |
| **Ctrl+R** | Copy the selected widgets as references |
| **Ctrl+I** | Paste references |
| **Ctrl+X** | Remove the selected widget |
| **Delete** or **Backspace** | Remove the selected widgets, after one confirmation |
| **←** **→** **↑** **↓** | Move the selected widgets one grid cell |
| **Shift+arrow** | Move the selected widgets ten grid cells |
| **Ctrl+K** or **/** | With the widget bar open: search widgets to add, or search the properties of the widget you edit |

### SCADA layouts

On dashboards with a SCADA layout, in edit mode:

| Keys | Does |
|---|---|
| **R** | Rotate the selected widgets by 90° |
| **Tab** | Cycle through widgets stacked on top of each other |
| **Ctrl+]** | Bring forward |
| **Ctrl+[** | Send backward |
| **Ctrl+Shift+]** | Bring to front |
| **Ctrl+Shift+[** | Send to back |

## Rule chain editor

| Keys | Does |
|---|---|
| **Ctrl+S** | Apply changes |
| **Ctrl+Z** | Decline changes (back to the last applied version) |
| **Ctrl+A** | Select all nodes and connections |
| **Ctrl+C** | Copy the selected nodes |
| **Ctrl+V** | Paste |
| **Ctrl+R** | Make the selected nodes into a nested rule chain |
| **Delete** | Delete the selected nodes and connections |
| **Esc** | Clear the selection |

## Widget editor

| Keys | Does |
|---|---|
| **Ctrl+Enter** | Run the widget with the current code |
| **Ctrl+S** | Save the widget |
| **Ctrl+Shift+S** | Save as a new widget |
| **Ctrl+Q** | Undo the changes since the last save |
| **Ctrl+Shift+F** | Full screen on or off |

## Data pipeline builder

| Keys | Does |
|---|---|
| **Ctrl+A** | Select all nodes and connections |
| **Delete** or **Backspace** | Delete the selected nodes and connections |
| **Esc** | Clear the selection |

## Related

- [Dashboards](/docs/dashboards/)
- [SCADA editor](/docs/dashboards/scada-editor/)
- [Rule engine](/docs/user-guide/rule-engine-2-0/re-getting-started/)
