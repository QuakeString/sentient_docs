+++
title = "SCADA"
description = "Build process screens in SENTIENT: the SCADA layout, ready-made symbols to ISA-5.1 and IEC standards, connecting them to data, and your own symbols."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **SCADA dashboard** is a process screen: pumps, valves, tanks, motors and pipes drawn as they are in the plant, each showing its live state and, where allowed, taking commands. SENTIENT gathers the data from PLCs and meters, usually through the [SENTIENT Gateway](/docs/iot-gateway/), and adds [alarms](/docs/user-guide/alarms/) and [notifications](/docs/user-guide/notifications/) around it.

A SCADA dashboard is an ordinary [dashboard](/docs/user-guide/dashboards/) with the **SCADA** layout, filled mostly with **SCADA symbols**.

## The SCADA layout

The SCADA layout differs from the default one:

- There is **no gap between widgets**, so pipes and symbols join up exactly.
- Widgets have **no background or shadow** by default, so regular widgets such as charts and value cards sit on the drawing without a box.
- Widgets may **overlap**, and the layout has **layers**: put a background drawing on one layer and the symbols on another. In edit mode, **Active Layer** says where new widgets go, **Manage Layers** adds, hides and orders them, and **Move to Layer…** in a widget's right-click menu moves it.

To use it:

1. Create a dashboard, or open one, and click **Edit mode**.
2. Click **Layouts**, change the layout from **Default** to **SCADA**, and click **Save**.
3. Add symbols with **Add widget**: search for the equipment, for example `centrifugal pump` or `gate valve`, or open one of the SCADA bundles.

## Symbols that come with SENTIENT

| Bundle | Contains |
|---|---|
| **General high-performance SCADA symbols** and **High-performance SCADA energy system / fluid system / oil & gas** | Grey, low-colour symbols in the style of ISA-101 high-performance HMI: colour only where something needs attention |
| **Traditional SCADA fluid system** | Coloured 3D-style tanks, pumps, pipes and valves |
| **ISA-5.1 P&ID Symbols** | 221 instrument and equipment symbols as on a P&ID |
| **IEC Electrical Symbols** | 245 symbols for single-line and switchgear diagrams |
| **Primitive Symbols** | Lines, shapes and labels to draw the rest |
| **Industrial widgets**, **Rotating Equipment**, **Valves**, **Material Handling**, **Combustion** | Animated equipment such as belt conveyors, fans, compressors, burners |

See the [widgets library](/docs/user-guide/ui/widget-library/) for all bundles.

## Connect a symbol to data

Click a symbol's pencil in edit mode. Most symbols have the same settings:

1. **Target device**: the device the symbol stands for. Choose a device, or an alias so the same screen serves several identical units.
2. **Behavior**: what each part of the symbol shows or does. A pump has, for example, **Running** (a key whose `true` turns the impeller), **Warning** and **Critical** (usually alarms), and **On click** (a command). Each behaviour reads a time-series key, an attribute, or an alarm state, or sends a command or writes an attribute.
3. **Appearance**: colours, labels, units and the number of decimals.

Commands go to the device as [RPC](/docs/user-guide/rpc/) or as a shared attribute that the device or gateway writes to the PLC. Give operators confirmation dialogs for commands that move equipment.

## Your own symbols

The tenant administrator manages symbols under **Resources > SCADA symbols**. **Include system symbols** shows the built-in ones too.

- **Upload SCADA symbol**: load an SVG file drawn in any vector editor.
- **Edit SCADA symbol**: name the parts of the drawing, then define the **Properties** (the settings users will see) and the **State render function** that changes the drawing from the data, and try it in **Preview**.
- **Create widget**: turns the symbol into a widget, so it appears in **Add widget** on dashboards.

See [SCADA symbol development](/docs/user-guide/scada/scada-symbols-dev-guide/) for the details.

## Related

- [Dashboards](/docs/user-guide/dashboards/)
- [Widgets library](/docs/user-guide/ui/widget-library/)
- [SENTIENT Gateway](/docs/iot-gateway/)
