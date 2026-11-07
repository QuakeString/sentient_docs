+++
title = "Data pipelines"
description = "Process device data with analytics pipelines: filters, maths, spectra, statistics, forecasts and plant calculations, built in the visual pipeline builder."
weight = 121

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **data pipeline** takes a device's telemetry through a chain of processing steps and writes the results back as new telemetry, attributes or alarms. Use one when a [calculated field](/docs/user-guide/calculated-fields/) is not enough: smoothing a noisy signal, a vibration spectrum, an OEE figure, a trend or a forecast.

Open **Analytics > Data Pipelines** in the left menu. Ready-made pipelines are in the [solution hub](/docs/solution-hub/) under **Templates › Analytics pipelines**.

## Make a pipeline

1. Click **+** › **Add Pipeline** (or **Add from Solution hub**), give it a **Pipeline Name** and a **Description**, and click **Add**. **Import Pipeline** reads a pipeline exported earlier as JSON.
2. Click the pipeline, then **Open Pipeline Builder**.
3. The builder shows the **Node Library** on the left and the pipeline on the canvas. Drag nodes onto the canvas and connect them from output to input. Double-click a node to set it up.
4. Save. The pipeline starts as soon as it is enabled.

### The input node: what the pipeline works on

Every pipeline starts with a **Telemetry Input** node. In it, set:

| Setting | Value |
|---|---|
| **Applies to** | One **Device**, or a **Device profile**: then the pipeline runs for every device of that profile, without copies |
| Keys | The time series and attribute keys the pipeline uses. Empty means all |
| When it runs | **Event-driven**: on every incoming value, the way a calculated field does, with no rule chain needed. **Fixed interval** (**Run every** so many minutes) or **Cron**: as a job over stored data, covering the last **Data window** minutes |
| **Output Prefix** | Put in front of every result key, for example `analytics_` |

A pipeline is either event-driven or scheduled, never both. **Run over stored data** (the **Run** button) processes the last hours of stored data once, for example to fill in results for data that arrived before the pipeline existed.

### The output nodes

- **Telemetry Output** writes the results as **Telemetry (time series)**, which keeps history, or as **Server attributes** or shared attributes, which keep only the latest value. **Delivery** is **Through the rule chain**, so rule nodes and alarms see the results, or **Direct to storage**, the cheapest way to store derived series.
- **Alarm Output** raises an alarm of an **Alarm Type** and **Severity** when the result says so.

## The node library

| Category | Nodes |
|---|---|
| **Filter** | Moving Average (simple or exponential), Exponential Filter, Median Filter, Savitzky-Golay, Butterworth Filter, Deadband, Hysteresis, Rate Limiter, Gap Fill, Resample |
| **Math** | Expression (for example `a * 2.0 + b`), Scale & Offset, Delta, Rate of Change, Clamp, Accumulator, If / Then / Else |
| **Spectral** | FFT / Power Spectrum, THD Analysis, Harmonic Extract, Band Power, Spectral Entropy, Envelope (Hilbert), Spectrogram (STFT), Order Analysis, Wavelet Transform |
| **Statistical** | Rolling Statistics, EWMA, Z-Score, CUSUM, Percentile, Correlation, Time-Weighted Avg, State Duration, Data Quality, Frozen Signal, Lag, Linear Regression, RMS, Crest Factor, Skewness, Kurtosis, Entropy, Autocorrelation, SPC Control Chart (Nelson rules), Min/Max + Timestamp, Zero Crossings, Peak Detection, Lempel-Ziv Complexity, Matrix Profile |
| **ML** | Anomaly Detection, Anomaly Clustering, Change Point, Forecast, ARIMA Forecast, Remaining Useful Life |
| **Domain** | OEE, Power Factor, Efficiency, Energy Accumulator, Specific Energy, Health Index, Run Hours, Degradation Tracking, Vibration Spectra, Bearing Frequencies, Motor Current Analysis, Valve Stiction, PID Performance, MPC Control, and calculations for submerged arc furnaces (electrode impedance, power and energy balance, arc resistance, impedance rate, furnace state) |

Each node's settings name its **Input Column** and **Output Column**, the keys it reads and writes, plus its own parameters, with a hint for each. **Reset to Defaults** puts back the node's default settings.

## Example: smooth a flow signal and count running hours

1. **Telemetry Input**: **Applies to** the device profile **Centrifugal pump**, keys `flow` and `running`, **Event-driven**.
2. **Median Filter**: input `flow`, output `flowClean`, window 5, to remove spikes.
3. **Run Hours**: from `running`, output `runHours`.
4. **Telemetry Output**: **Telemetry (time series)**, **Direct to storage**.

Every pump of that profile now has `flowClean` and `runHours`, ready for dashboards and alarm rules.

## Find problems

**Enable debug mode** in the pipeline's settings, or the bug button on a node in the builder, stores each run as an event with its inputs and results, so you can see where a value went wrong. Like rule chain debugging, it fills the database quickly, so turn it off when you are done.

**Enable Pipeline** and **Disable Pipeline** start and stop a pipeline without deleting it. **Export Pipeline** saves it as JSON, and **Save to Solution hub** keeps a copy in the hub to install elsewhere.

## Related

- [Solution hub](/docs/solution-hub/)
- [Calculated fields](/docs/user-guide/calculated-fields/)
- [Asset health](/docs/asset-health/)
