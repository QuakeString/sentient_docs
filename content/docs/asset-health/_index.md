+++
title = "Asset health"
description = "Watch rotating machines through vibration, temperature, sound and process readings: health score, findings with their cause and advice, remaining life, and work orders."
sort_by = "weight"

[extra]
status = "checked"
checked = "4.3.0.57"
+++
**Asset health** watches rotating machines (pumps, fans, motors, gearboxes, compressors, conveyors) through their vibration, temperature, sound and process readings. For each machine it says how healthy it is, what is wrong, how sure it is, and what to do next. Findings become alarms and work orders, so the maintenance team works from the same screens.

## Get started

1. Install **Asset Health Monitoring** from the [solution hub](/docs/solution-hub/). It creates the plant, the machine and sensor profiles, the dashboards, and the routing of work orders to your maintenance team. For a whole plant, download the CSV template of the machines list, fill it in a spreadsheet and import it in the install form.
2. Describe each machine in **Machine setup**: type, running speed, bearings, gears and sensor positions. See [Set up a machine](/docs/asset-health/machine-setup/). The diagnosis can only find bearing or gear faults it knows the parts for.
3. Connect the sensors. They send spectra, waveforms, summary levels or sound clips. See [Vibration analysis](/docs/asset-health/vibration-analysis/).
4. Set the limits in the **Limits** widget. The threshold assistant suggests them from the last weeks of normal running.

## Where things are

| Dashboard page | Shows |
|---|---|
| **Overview** | Fleet summary rings, the fleet heatmap, faults by area, open findings and work orders |
| **Machine** | Health score, diagnosis, spectrum and waveform, [waterfall](/docs/asset-health/waterfall/), remaining life, sound, pump performance and the machine's [work orders](/docs/asset-health/work-orders/) |
| **Setup** | Machine setup, limits, and phone commissioning |

The solution also brings a **machine status** dashboard for operators (which machines need attention and what to do) and an **asset health summary** for the plant head (risk, remaining life and the work in hand). Every widget has a **?** button that opens its help.

## Health states

Every machine and measurement point has one state, always with a reason:

| State | Means |
|---|---|
| **Not operational** | The machine is stopped: its overall level is below **Idle below** |
| **Not configured** | Something the diagnosis needs is missing. The reason names the field |
| **No spectrum yet** | Set up, but the sensor has not sent a spectrum |
| **Low**, **Medium**, **High**, **Highest risk** | The diagnosis ran. The worst finding sets the risk |

The score card's **Last 30 days** bar shows the state over time.

## Health score

The **health score** runs from 100 (as new) to 0. It loses points for the vibration zone and for each finding, weighted by the finding's risk and confidence. **What lowers the score** lists every deduction, largest first, so you can see why a machine is at 62 and not 90.

A **finding** names a fault (unbalance, misalignment, looseness, a bearing defect, gear mesh, belt, vane pass, cavitation, temperature, a custom feature or a pump problem), its confidence, the evidence behind it and the recommended action.

## Alarms

SENTIENT diagnoses each machine when a new spectrum or new readings arrive, at most every `MACHINE_HEALTH_INTERVAL_SECS` seconds (default 300). Findings at or above `MACHINE_HEALTH_ALARM_MIN_RISK` (default medium) raise [alarms](/docs/user-guide/alarms/) named `Asset health: <finding>`, which clear by themselves when the finding goes away. The solution adds a notification rule for major and critical findings.

## Remaining life

Remaining life estimates when a reading will reach its warning and critical limits if it keeps the trend of the last 30 days. SENTIENT fits a straight line and an exponential curve and keeps the better one; readings while the machine stands are left out.

- **Confidence** falls with scatter, few readings, a short history and a long look-ahead. Treat a low-confidence estimate as a hint, not a date.
- **Insufficient data**: fewer than 10 readings or less than a day of history.
- **Stable**: the trend does not reach the limit. **Beyond warning** and **Beyond critical**: it is already there.

The figures are also saved as telemetry: `rul_state`, `rul_warning_days`, `rul_critical_days`, `rul_confidence`, `rul_point`.

## The fleet

- The **fleet heatmap** shows every machine as a tile, grouped by area, coloured and sorted worst first by **Health score**, **Risk** or **Remaining life**. Click a tile to open the machine.
- The **fleet summary** rings count machines by risk and sensors by state (critical, warning, operational, idle, disconnected). Click a slice to list its machines.
- The **fault sunburst** shows the plant in the middle, then areas, then fault types.

## Sound

The sound channel keeps short clips from a microphone or ultrasound sensor, so anyone can listen to a machine from the dashboard and compare it with how it sounded when healthy. Devices send a WAV file to `POST /api/v1/{token}/sound?key=sound`; a phone can record one during commissioning. Each clip saves `<key>_level_db`, `<key>_peak_db` and `<key>_crest`, so the level can have limits and a trend. A rising crest factor often means impacts: bearing damage, looseness or cavitation.

The **sound player** lists the clips with their level and spectrogram. **Mark as baseline** keeps a clip from when the machine was healthy; **Against baseline** plays the baseline, then the latest clip.

## Pumps

For pumps, SENTIENT also works out the energy figures from flow, head (or suction and discharge pressure) and electrical power: hydraulic power, wire-to-water efficiency against the datasheet curve, kWh per m³, flow as a share of the best efficiency point, and the daily cost of the efficiency lost. It raises findings for running far from the best efficiency point, low efficiency, more energy than the baseline, and running below the curve (worn impeller, low speed, air in the pump). Set the keys and the datasheet on the machine's **Pump** tab.

## Ask the AI assistant

The [AI assistant](/docs/ai/assistant/) answers questions about machine health with your data, for example *Which machines got worse this week?*, *Why is Cooling water pump 2 orange?* or *Draft a work order for Pump 3*. It shows a work order draft first and creates it only after you agree. It sees exactly what you can see in SENTIENT.

## In this section

- [Set up a machine](/docs/asset-health/machine-setup/)
- [Vibration analysis](/docs/asset-health/vibration-analysis/)
- [Waterfall views](/docs/asset-health/waterfall/)
- [Work orders](/docs/asset-health/work-orders/)
