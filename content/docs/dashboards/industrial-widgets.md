+++
title = "Industrial equipment widgets"
description = "46 animated equipment widgets for plant screens: pumps, fans, motors, valves, conveyors, hoppers, chutes and burners that move with live data."
weight = 73

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT adds 46 widgets that draw plant equipment as it looks and make it move with live data: a pump that ramps up when it starts and coasts down when it stops, a valve whose stem lifts as it opens, a belt that runs at the measured speed, a burner whose flame follows the firing rate. Each one shows its own faults and readouts, so one widget replaces a picture, a few value cards and an alarm light.

They are [SCADA symbols](/docs/user-guide/scada/), so they work on any dashboard and on SCADA screens alike.

## The bundles

In edit mode, click **Add widget** and open one of these bundles, or type the equipment's name in the search box.

![The Rotating Equipment bundle in the widgets library](/images/st/industrial-widgets-bundle.webp)


| Bundle | Widgets |
|---|---|
| **Rotating Equipment** | **Pump** (12 types: centrifugal end suction, vertical inline, multistage, split case, gear, progressive cavity, diaphragm metering, plunger, submersible, vertical turbine, lobe, peristaltic), **Fan** (8 types: ID, FD, axial, cooling tower, roof exhaust, belt-driven blower, roots blower), **Electric Motor** (foot mounted, flange, vertical, gearmotor, explosion-proof, slip-ring, DC) |
| **Valves** | 33 valves and strainers drawn in 3D: gate, globe, ball, butterfly, plug, needle, knife gate, angle, diaphragm, pinch, check, control, motor-operated, solenoid, relief, pressure reducing, three-way and four-way valves; bucket, T, Y and duplex strainers |
| **Material Handling** | **Belt Conveyor**, **Hopper**, **Weigh Hopper**, **Chute** |
| **Combustion** | **Gas Burner**, **Oil Burner**, **Dual-Fuel Burner**, **Pilot Burner**, **Radiant Tube Burner**, **Line Burner** |

## Connect a widget to your data

1. Add the widget and choose the device in its data source, as for any widget.
2. In the widget's settings, the **Behavior** section lists what the widget can show. For each line, choose where the value comes from: **Get time series** or **Get attribute** with the key that holds it, or **Do nothing** to leave it out.
3. In **Properties**, choose the type and look: for example the pump type, the belt profile and length, or a valve's body finish.

Lines you leave at **Do nothing** keep their default, so a widget works with only one or two keys. For example, a pump needs only **Running** to start and stop.

### What each kind shows

| Widget | Main lines in **Behavior** |
|---|---|
| Pump, Fan, Electric Motor | Running, Speed, Standby, Tripped, Trip code, Duty / standby and Local / remote badges, Vibration, Bearing temperature, Fault. Plus Flow and Discharge pressure (pump), Damper / IGV / pitch, Airflow and Pressure (fan), Motor current, Power and Winding temperature (motor) |
| Valves | Position (0 = closed to 100 = open), Open, Fault. Three-way valves have Mix position instead |
| Belt Conveyor | Running, Reverse, Belt speed, Load, Warning, Fault, Fault code |
| Hopper | Level, Filling, Outlet running, High and low level switches, Warning, Fault |
| Weigh Hopper | Weight, Setpoint, Filling, Discharging, Weight stable, Fault code, Warning, Fault |
| Chute | Flowing, Top and bottom gate open, Flap to B, Blocked, Warning, Fault |
| Burners | Burner state, Firing, Firing rate, Flame detected, Fuel valve open, Air damper, Warning, Fault, Fault code |

Limits such as the rated speed, the vibration limit, the bearing temperature limit or the gauge full scale are under **Properties**.

### Clicks

Every equipment widget has **On click**, **On press** and **On release** in its **Behavior** section. Use **On click** to open a detail state or another dashboard, and **On press** / **On release** to send a command, for example a jog button.

## Colours and look

- **Style** sets the drawing of pumps, fans, motors, conveyors and burners: **Line**, **Filled**, **ISA-101 (high performance)**, **Shaded** or **3D**. Valves are always drawn in 3D; **Body finish** chooses stainless, painted cast steel or cast iron.
- The colours for running, stopped, warning and fault are under **Properties**. Keep them the same on every screen of a plant, so operators read states at a glance.
- **Tag name** and **Show tag name** print the equipment's tag, for example `P-101`, next to it.

## Related

- [SCADA dashboards](/docs/user-guide/scada/)
- [Widget library](/docs/user-guide/ui/widget-library/)
- [What is new in SENTIENT dashboards](/docs/dashboards/)
