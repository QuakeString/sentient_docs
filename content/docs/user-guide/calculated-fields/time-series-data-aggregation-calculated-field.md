+++
title = "Time series data aggregation calculated field"
description = "Simple calculated fields use basic arithmetic operations (+, -, *, /) and standard functions such as sqrt (square root), pow (power), abs (absolute value), etc."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/calculated-fields/time-series-data-aggregation-calculated-field.md"
+++
Time series data aggregation is a calculated field that computes **aggregated metrics over historical telemetry** of the **current entity** (hour/day/week/month, etc.) and stores the results as new telemetry keys.

Unlike “latest-value” aggregation across related entities, this type operates on historical time series data — ideal for analytics, reporting, and long-term KPIs.

When to use
- Analytics & KPIs
  - Generate hourly/daily/weekly aggregates (e.g., hourly average temperature)
  - Build KPIs from historical data (daily runtime, peak load, total consumption)
  - Create reporting-ready statistics for exports, audits, or automation
- Performance & reliability
  - Reduce dashboard/API load by storing pre-aggregated metrics
  - Handle delayed telemetry and automatically correct historical aggregates
  - Track near-real-time aggregates using intermediate results (e.g., "current hour average so far")

<hr>

## Configuration


Open the [create calculated field](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#creating-a-calculated-field) dialog and specify:
- the calculated field **title**,
- the **entity or entity profile** to which the calculated field will be applied,
- Select "**Time series data aggregation**" as a calculated field **type**.

<hr>

### Arguments

Arguments define which telemetry values are used for aggregation.
This calculated field type reads **historical telemetry only from the current entity**.

Click **Add argument** and fill in the required fields:
- **Time series key** — the telemetry key whose data will be aggregated (for example, temperature, power, voltage)
- **Argument name** — the variable name referenced by metrics


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggregation-argument-1-ce.webp" alt="Click **Add argument** (1) and fill in the required fields:- **Time series key** (2) — the telemetry key whose data will be aggregated (for example, temperature, power, voltage)- **Argument name** (3) — the variable name referenced by metrics.Then click **Add** (4)." loading="lazy"><figcaption>Click **Add argument** (1) and fill in the required fields:<br>- **Time series key** (2) — the telemetry key whose data will be aggregated (for example, temperature, power, voltage)<br>- **Argument name** (3) — the variable name referenced by metrics.<br>Then click **Add** (4).</figcaption></figure></div>


<hr>

### Metrics

Each metric produces **one output telemetry key (Metric name)** by applying one aggregation function to one argument.

Click the **Add metric** button and fill in the required fields:
- **Metric name**: output telemetry key name (e.g., tempAvg, tempMax)
- **Aggregation**: Average / Min / Max / Sum / Count
- **Argument name**: the argument whose value is being aggregated.
- **Default value**: used if the interval contains no data

> You can create multiple metrics from the same argument (e.g., <span class="code-light">tempAvg</span>, <span class="code-light">tempMin</span>, <span class="code-light">tempMax</span>).


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggregation-metric-1-ce.webp" alt="Click the **Add metric** button (1) and fill in the required fields:- **Metric name** (2): output telemetry key name (e.g., tempAvg, tempMax)- **Aggregation** (3): Average / Min / Max / Sum / Count- **Argument name** (4): the argument whose value is being aggregated.- **Default value** (5): used if the interval contains no dataThen click **Add** (6)." loading="lazy"><figcaption>Click the **Add metric** button (1) and fill in the required fields:<br>- **Metric name** (2): output telemetry key name (e.g., tempAvg, tempMax)<br>- **Aggregation** (3): Average / Min / Max / Sum / Count<br>- **Argument name** (4): the argument whose value is being aggregated.<br>- **Default value** (5): used if the interval contains no data<br>Then click **Add** (6).</figcaption></figure></div>


<hr>

### Aggregation interval

Defines how often aggregation runs and how time boundaries are aligned.
Example: **every 1 hour** produces results at 00:00, 01:00, 02:00, etc.
- **Aggregate interval type**: Hour / Day / Week (Mon–Sun) / Week (Sun–Sat) / Month / Quarter / Year / Custom
- **Time zone**: aligns interval boundaries for daily/weekly reports and region-specific KPIs


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggregation-interval-1-ce.webp" alt="Defines how often aggregation runs and how time boundaries are aligned." loading="lazy"><figcaption>Defines how often aggregation runs and how time boundaries are aligned.</figcaption></figure></div>


<br>

<b><font size="4">Advanced interval options</font></b>

<b><font size="3">Apply offset to aggregation interval</font></b>   
Shifts the start of each interval by a fixed offset (e.g., +10 minutes → 00:10, 01:10…).   
Useful when telemetry arrives slightly after boundaries or when aligning with external systems.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-agr-advanced-interval-1-ce.webp" alt="Shifts the start of each interval by a fixed offset (e.g., +10 minutes → 00:10, 01:10…)." loading="lazy"><figcaption>Shifts the start of each interval by a fixed offset (e.g., +10 minutes → 00:10, 01:10…).</figcaption></figure></div>


<br><b><font size="3">Apply await timeout for delayed telemetry</font></b>   
Defines how long the system waits for late telemetry after an interval ends. 
If late telemetry belongs to that interval, the system recalculates the result to improve accuracy.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-agr-advanced-interval-2-ce.webp" alt="Defines how long the system waits for late telemetry after an interval ends." loading="lazy"><figcaption>Defines how long the system waits for late telemetry after an interval ends.</figcaption></figure></div>


<br><b><font size="3">Produce intermediate result</font></b>   
Calculates aggregates during the current (not yet finished) interval and stores intermediate values:
- updates occur no more often than once every 5 minutes
- useful for dashboards that need "current interval" values (e.g., "current hourly average so far")


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-agr-advanced-interval-3-ce.webp" alt="Calculates aggregates during the current (not yet finished) interval and stores intermediate values." loading="lazy"><figcaption>Calculates aggregates during the current (not yet finished) interval and stores intermediate values.</figcaption></figure></div>


<hr>

### Output

Aggregated values are stored as [telemetry](/docs/user-guide/telemetry/) on the current entity under the configured Metric names (output keys).

> This calculated field stores results **only as time series**.

For more details about output processing strategies, see the [Output](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#output) section.

<hr>

## Example: Hourly energy KPIs

<b><font size="4">Scenario</font></b>   
An Energy Meter device installed in Building A continuously publishes historical telemetry values such as:
- <span class="code-light">power</span> (kW) — current power usage
- <span class="code-light">energy</span> (kWh) — total consumption counter

<b><font size="4">Goal</font></b>   
Compute hourly aggregates from historical telemetry and store them as new time series keys on the Energy Meter device:
- <span class="code-light">energyHourlySum</span> — total energy consumption per hour (sum)
- <span class="code-light">powerHourlyAvg</span> — average power per hour (avg)
- <span class="code-light">powerHourlyMax</span> — maximum power per hour (max)

This produces reporting-ready KPIs and reduces dashboard/API load by storing pre-aggregated metrics instead of computing them on the fly.

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Time series data aggregation" calculated field configuration file (JSON)](/docs/user-guide/resources/calculated-fields/time-series-data-aggregation/hourly_energy_kpis.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo devices</font></b>

Import a device that publishes <span class="code-light">power</span> and <span class="code-light">energy</span> telemetry.
1. Download the CSV file: [energy-meter-with-telemetry.csv](/docs/user-guide/resources/calculated-fields/time-series-data-aggregation/energy-meter-with-telemetry.csv)
2. Go to the **Devices** and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Energy Meter 1
- **Type:** energy-meter
- **Time series:** <span class="code-light">power</span>, <span class="code-light">energy</span>

> **Important note about the CSV:** the column type for the <span class="code-light">power</span> and <span class="code-light">energy</span> keys must be set to "**Time series**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-1-ce.webp" alt="Go to the **Devices** and **import** device configurations from a CSV file." loading="lazy"><figcaption>Go to the **Devices** and **import** device configurations from a CSV file.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-2-ce.webp" alt="Name: Energy Meter 1Type: energy-meterTime series: power, energy" loading="lazy"><figcaption>Name: Energy Meter 1<br>Type: energy-meter<br>Time series: power, energy</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-3-ce.webp" alt="The imported device that publishes **power** and **energy** telemetry." loading="lazy"><figcaption>The imported device that publishes **power** and **energy** telemetry.</figcaption></figure></div>


> **Note:** make sure the device already has historical telemetry for at least 1–2 hours, otherwise the first aggregation interval may use default values.

<br><b><font size="3">2. Apply the calculated field to the device</font></b>

Apply the **Time series data aggregation** calculated field to the **Energy Meter 1** device.
1. [Download the calculated field configuration file](/docs/user-guide/resources/calculated-fields/time-series-data-aggregation/hourly_energy_kpis.json).
2. Go to the Calculated fields tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.

Ensure the calculated field is configured as:
- Type: Time series data aggregation
- Arguments (Current entity only):
  - <span class="code-light">power</span> → argument name <span class="code-light">power</span>
  - <span class="code-light">energy</span> → argument name <span class="code-light">energy</span>
- Metrics:
  - <span class="code-light">powerHourlyAvg</span> → Average of <span class="code-light">power</span>
  - <span class="code-light">powerHourlyMax</span> → Max of <span class="code-light">power</span>
  - <span class="code-light">energyHourlySum</span> → Sum of <span class="code-light">energy</span>
- Aggregation interval: Hour
- Time zone: your reporting time zone (recommended: local time zone)

(Optional) Enable [Debug mode](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#debug) and review execution events using the **Events** icon.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-4-ce.webp" alt="Go to the **Calculated fields** tab and import the calculated field configuration." loading="lazy"><figcaption>Go to the **Calculated fields** tab and import the calculated field configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-5-ce.webp" alt="Apply the calculated field to the **energy-meter** device profile." loading="lazy"><figcaption>Apply the calculated field to the **energy-meter** device profile.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-6-ce.webp" alt="First argument settings:- **Time series key:** energy- **Argument name:** energy." loading="lazy"><figcaption>First argument settings:<br>- **Time series key:** energy<br>- **Argument name:** energy.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-7-ce.webp" alt="Second argument settings:- **Time series key:** power- **Argument name:** power." loading="lazy"><figcaption>Second argument settings:<br>- **Time series key:** power<br>- **Argument name:** power.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-8-ce.webp" alt="First metric settings:- **Metric name:** energyHourlySum- **Aggregation:** Sum- **Argument name:** energy." loading="lazy"><figcaption>First metric settings:<br>- **Metric name:** energyHourlySum<br>- **Aggregation:** Sum<br>- **Argument name:** energy.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-9-ce.webp" alt="Second metric settings:- **Metric name:** powerHourlyAvg- **Aggregation:** Average- **Argument name:** power." loading="lazy"><figcaption>Second metric settings:<br>- **Metric name:** powerHourlyAvg<br>- **Aggregation:** Average<br>- **Argument name:** power.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-10-ce.webp" alt="Third metric settings:- **Metric name:** powerHourlyMax- **Aggregation:** Maximum- **Argument name:** power." loading="lazy"><figcaption>Third metric settings:<br>- **Metric name:** powerHourlyMax<br>- **Aggregation:** Maximum<br>- **Argument name:** power.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-11-ce.webp" alt="Aggregation interval: Hour; Time zone: use your reporting time zone.The computed values are stored as telemetry (time series) keys.Click **Add** to save the calculation field." loading="lazy"><figcaption>Aggregation interval: Hour; Time zone: use your reporting time zone.<br>The computed values are stored as telemetry (time series) keys.<br>Click **Add** to save the calculation field.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

> New values will be calculated at the beginning of the next hour (in my case, at 13:00).

On the Energy Meter 1 device, the aggregated values are stored as telemetry (time series) keys:
- <span class="code-light">powerHourlyAvg</span> — hourly average power usage
- <span class="code-light">powerHourlyMax</span> — hourly peak power usage
- <span class="code-light">energyHourlySum</span> — hourly energy consumption

Example output for one interval:
```json
{
  "powerHourlyAvg": 12.4,
  "powerHourlyMax": 18.9,
  "energyHourlySum": 6.7
}
```


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/time-series-data-aggregation/time-series-data-aggr-cf-example-1-12-ce.webp" alt="On the **Energy Meter 1** device, the aggregated values are stored as telemetry (time series) keys:- **powerHourlyAvg**— hourly average power usage- **powerHourlyMax** —hourly peak power usage- **energyHourlySum** — hourly energy consumption" loading="lazy"><figcaption>On the **Energy Meter 1** device, the aggregated values are stored as telemetry (time series) keys:<br>- **powerHourlyAvg**— hourly average power usage<br>- **powerHourlyMax** —hourly peak power usage<br>- **energyHourlySum** — hourly energy consumption</figcaption></figure></div>


<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please [contact us](/docs/contact-us/).
