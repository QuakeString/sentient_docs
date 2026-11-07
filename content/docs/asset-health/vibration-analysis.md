+++
title = "Vibration analysis"
description = "Send spectra, waveforms or summary levels from vibration sensors; read findings, spectra and phase; capture on demand; check sensor settings and health."
weight = 152

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Sensors send their data with the device's access token, like any telemetry. What they send decides what the diagnosis can find:

| Sensor sends | The diagnosis finds |
|---|---|
| Overall levels only | The ISO zone and the health score, but not the cause |
| Orders 1X to 10X | Also unbalance, misalignment and looseness |
| A full spectrum or the raw waveform | Also bearing, gear, belt and vane pass faults, cavitation |

## Spectra and waveforms

- A sensor that computes its own FFT posts it to `POST /api/v1/{token}/spectrum` with `key`, `ts`, `freqStartHz`, `freqStepHz` and `bins` (a number array) or `binsB64` (32-bit floats, little-endian, base64).
- A sensor that sends the raw capture posts it to `POST /api/v1/{token}/waveform` with `key`, `ts`, `sampleRateHz` and `samples` or `samplesB64`. [Data pipelines](/docs/solution-hub/pipelines/) bound to the device turn it into spectra.

Raw waveforms are kept `WAVEFORM_TTL_DAYS` days (default 90), spectra `SPECTRUM_TTL_DAYS` days (default 365).

## Standard tri-axial sensors

Most MEMS vibration sensors measure X, Y and Z and report summary values. SENTIENT takes them in under the sensor's own key names, over MQTT or Modbus, and saves the asset health keys next to them:

| Sensor sends | Saved as |
|---|---|
| `x_rms_vel`, `y_rms_vel`, `z_rms_vel` (mm/s) | `vib_h_velocity_rms`, `vib_v_velocity_rms`, `vib_a_velocity_rms` |
| `x_rms_acl` … (g) | `vib_h_rms` … |
| `x_peak_acl` … (g), `x_peak_vel` … (mm/s) | `vib_h_peak` …, `vib_h_velocity_peak` … |
| `temp_c`, `SPL_dB` | `temperature`, `sound_level_db` |
| `x_vel_1x_amp` + `x_vel_1x_hz` … up to `10x` | An order spectrum, `vib_h_velocity_spectrum` |

Which machine axis X, Y and Z face comes from the device attribute `axisOrientation` (three letters, for example `VAH`: X vertical, Y axial, Z horizontal); otherwise X horizontal, Y vertical, Z axial.

For wired RS-485 sensors, each sensor device of the solution carries its Modbus register map in the `modbusRegisterMap` attribute. Copy it into the [Modbus connector](/docs/iot-gateway/config/modbus/) of the SENTIENT gateway and set the port and unit id.

## Read the diagnosis

The **diagnosis panel** lists the findings with their confidence and advice. Click a row of a finding's evidence (the expected frequency, the peak found, its amplitude and how far it stands above the noise floor): the spectrum on the same page switches to that point, and to the envelope spectrum for bearing faults, zooms to the peak and marks it.

On the **spectrum** chart:

- **Harmonics** cursor: click a peak to mark 1× to 10× of it.
- **Sidebands** cursor: click a peak to mark it ± 1 to 4 × running speed.
- **Set this spectrum as the baseline** keeps the spectrum as this channel's reference, drawn dashed under every later spectrum. **Hide baseline** hides it.
- The capture timeline has one dot per stored spectrum, coloured by the zone at that time. Click a dot to show that capture; **Back to the latest captures** returns.

The **time waveform** widget shows the raw capture.

## Temperature

Each sensor's `temperature` is judged with its vibration:

| Finding | When |
|---|---|
| **High temperature** | At or above the warning or critical limit |
| **Temperature rising fast** | Climbing 5 °C per hour or more (10 °C: high risk) while running and warmer than usual |
| **Running hotter than normal** | 15 °C or more above its usual level, still below the warning limit |

Without limits of its own, a sensor uses the machine type's default: warning 80 °C and critical 95 °C on the bearing housing, 85 °C and 100 °C for gearboxes, compressors, turbines and plain bearings. A cold machine warming up after a start is not flagged. A hot point also raises the confidence of its bearing, misalignment, rub and oil-whirl findings.

## Phase

The diagnosis reads the phase at running speed from channels captured at the same moment: the three axes of one tri-axial capture, or sensors triggered together. Horizontal and vertical about 90° apart support unbalance; about 0° or 180° apart point to misalignment, eccentricity, looseness or a soft base. Axial readings of two bearings about 180° apart support misalignment.

## Capture now and the settings check

- **Capture now**, in the time waveform widget, asks the sensor for a new capture. It is queued while the sensor is offline. The widget shows **Sent**, **Received**, **Partly received** or **Timed out** (after `SENSOR_CAPTURE_TIMEOUT_SECS`, default 600 seconds).
- The **settings check** compares the settings SENTIENT sent, the settings the sensor reports and its last waveform. **Mismatch** lists every setting that differs, so a wrong sample rate or range is found before it spoils a diagnosis.

## Sensor health

The **Sensor health** widget shows, for one sensor or all sensors of a machine: last seen, signal (`rssi`; good above −70 dBm, poor below −85), battery, reboots in the last 7 days, firmware, last capture, the settings check, and supply faults. A sensor **needs attention** when it is offline, its signal is poor, its battery is below 20 %, it reports a supply fault, or its settings differ from those sent. **Sync time** and **Reboot** send those commands to the sensor. Every item is optional: a sensor that does not send `rssi` shows a dash.

## Related

- [Set up a machine](/docs/asset-health/machine-setup/)
- [Waterfall views](/docs/asset-health/waterfall/)
