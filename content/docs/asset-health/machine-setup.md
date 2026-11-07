+++
title = "Set up a machine"
description = "Describe a machine, its train, bearings, gears and sensors so SENTIENT can diagnose it; set its limits with the threshold assistant; commission sensors from a phone."
weight = 151

[extra]
status = "checked"
checked = "4.3.0.57"
+++
The diagnosis compares each measured spectrum with the frequencies the machine's parts produce. It works them out from what you enter in **Machine setup**, on the machine's **Setup** page, so a complete setup gives better findings. Anything missing is listed at the top as **Not configured**; click a line to go to the field. The **Fault frequencies** panel on the right shows what the diagnosis will look for at the current speed.

## Machine

| Field | Value |
|---|---|
| **Machine type**, **Machine class** | The type, and the ISO 10816 / 20816 group for the vibration zones |
| **Running speed** | In rpm, or the **speed key** of a reading that reports it. A reported speed wins over the entered one |
| **Line frequency** | 50 or 60 Hz, so electrical faults are told apart from mechanical ones |
| **Idle below** | Below this overall level the machine counts as stopped and is not diagnosed |
| **Rated power**, **foundation**, **mounting** | Pick the vibration standard while no machine class is chosen: above 300 kW ISO 20816-3 group 1, 15 to 300 kW group 2 (flexible or rigid), below 15 kW ISO 10816-1 class I |
| **Lubrication** | Shapes a bearing finding's advice: re-grease, check oil, or replace a sealed-for-life bearing |
| **Coupling** | Shapes a misalignment finding's advice: the flexible element, the grid, the gear coupling's lubrication, or pulley alignment |
| **Role**, **orientation** | Horizontal, vertical or overhung, for the people reading the findings |

### Machine train

A machine whose parts turn at different speeds, such as a motor driving a crusher through a 1:35 gearbox or a fan on a belt, is one machine with several shafts. The running speed above is the **input shaft**. Under **Machine train**, add each other shaft with its **ratio**: input speed divided by that shaft's speed (35 for a 1:35 reduction, below 1 for a speed-up). Then, on the **Components** and **Sensors** tabs, pick the shaft each bearing, gear and sensor sits on.

Each sensor is then diagnosed at its own shaft's speed, a gear's mesh frequency is recognised on both sides of the gearbox, and the other shafts' speeds are marked on every spectrum so their peaks are not mistaken for faults.

### Slow machines

Below 600 rpm, running speed and bearing frequencies sit at a few hertz. The spectrum's resolution is 1 divided by the capture length, and running speed needs four lines, so a 41 rpm shaft needs captures of at least 6 seconds; 12.8 s (for example 5.12 kHz × 65 536 samples) is a good choice. The **Machine** tab shows the length needed, and the diagnosis warns when captures are too short. Bearing defects are still found in the envelope spectrum, as long as the sample rate is above about 1.7 kHz.

## Components

- **Bearings**: type the bearing number, for example `6205-2RS`, and pick it from the library. Each match is marked **ours (maker data)** (your own library, exact), **exact** (from published research data), or **estimated** (from ISO outer sizes, typically within a few percent). If it is not listed, switch on **Multipliers** and enter BPFO, BPFI, BSF and FTF from the datasheet.

  > The number of rolling elements matters most: one too many or too few moves the race frequencies by about 10 %. Next to an estimated bearing, check the count against the maker's sheet.

  **Our bearing library** holds your plant's bearings with the maker's figures. Add them one by one, or import a CSV (download the template first). Tenant administrators can change it.
- **Gears**: the teeth of each gear and of its mating gear.
- **Other parts**: impeller or fan vanes, belt pulleys and belt length.

## Sensors

One entry per measurement point: name, standard mount point, axis (horizontal, vertical, axial), the shaft it measures, the sensor device, and the keys it sends (velocity spectrum, envelope spectrum, overall velocity, sound).

**Add H, V and A** creates the three points of a tri-axial sensor. When the sensor reports X, Y and Z, pick which machine axis each faces once mounted (**Sensor X / Y / Z**).

## Custom features

Named frequency bands you want watched, in Hz or in orders of running speed, measured as RMS or peak, with a warning and a critical limit and the advice to show. They become findings like the built-in faults.

## Photos

Photos of the machine, its nameplate and the sensor spots. **Add photos** opens the camera on a phone. Give each a caption.

## Limits and the threshold assistant

The **Limits** widget sets a **warning** and a **critical** limit for each key. The **threshold assistant** reads the last 15, 30 or 60 days and suggests limits from how the machine normally runs (median and 95th percentile), next to the ISO limits for the machine class. Check the **Normal running** column: if the history includes a fault, the suggestion is too high.

**Accept** takes one suggestion, **Accept all** every one. **Save** stores the limits on the sensor; remaining life uses them too. With **Send to sensor** on, the limits are also written to sensors that hold their own thresholds.

The zone bar shows the overall velocity against the standard's zones: **A** (new machine), **B** (unrestricted long-term running), **C** (restricted running, plan action) and **D** (damage likely). Zone C or D raises the alarm `Asset health: Vibration level`.

## Commission from a phone

Open the machine's **Setup** page on a phone at the machine. **Phone commissioning** walks through one measurement point at a time:

1. Pick the point, or add one.
2. Tap the spot on the machine drawing where you fixed the sensor. Dashed spots already have one.
3. Pick the sensor axis. The standard keys are filled in.
4. Pick the sensor.
5. Optionally record how the machine sounds today. The clip becomes the healthy baseline in the sound player.

**Save measurement point** writes it into the machine setup.

## Related

- [Vibration analysis](/docs/asset-health/vibration-analysis/)
- [Asset health](/docs/asset-health/)
