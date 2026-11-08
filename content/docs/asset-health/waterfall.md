+++
title = "Waterfall views"
description = "See how a machine's spectrum changed over many captures: colour map, stacked lines or 3D."
weight = 153

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A spectrum shows one moment. The **waterfall** shows many captures of one measurement point together, oldest at the back, so you can see a peak appear, grow or move: a bearing defect developing over weeks, or a resonance that comes and goes with speed.

The waterfall is on the machine page of the Asset Health Monitoring dashboard, and can be added to any dashboard as a condition monitoring widget.

## Use it

1. Pick the **Measurement point**.
2. Choose **Velocity** or **Envelope**. The envelope spectrum shows bearing defects best.
3. Choose the view:

   | View | Shows |
   |---|---|
   | **Colour map** | Frequency across, time down, amplitude as colour. Best for spotting a line that grows or drifts |
   | **Stacked lines** | One spectrum line per capture, offset so they do not overlap |
   | **3D** | A surface. Drag to turn it, double-click to reset |

The toolbar shows how many captures are drawn (**Last N captures**). **Refresh** loads new ones.

## Read it

- A **vertical line** that stays at one frequency and grows brighter or taller is a fault developing at that frequency. Compare it with the machine's fault frequencies on the [spectrum](/docs/asset-health/vibration-analysis/#read-the-diagnosis), for example the outer race frequency of a bearing.
- A line that **moves** with time follows the running speed: check it against the speed, it is usually 1× or a harmonic.
- **Bands** that come and go across all frequencies point to process changes, such as load or flow, rather than a part.

## Settings

In the widget's settings, under **Waterfall**: the **Velocity spectrum key**, **Captures shown** (how many recent captures are drawn), the highest frequency shown and the amplitude unit. The measurement points come from the machine setup.

## Related

- [Vibration analysis](/docs/asset-health/vibration-analysis/)
- [Set up a machine](/docs/asset-health/machine-setup/)
