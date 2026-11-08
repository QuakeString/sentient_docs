+++
title = "Simple calculated field"
description = "Simple calculated fields use basic arithmetic operations (+, -, *, /) and standard functions such as sqrt (square root), pow (power), abs (absolute value), etc."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/calculated-fields/simple-calculated-field.md"
+++
Simple calculated fields perform real-time calculations using a single **mathematical expression**. 
They support basic arithmetic operations (<span class="code-light">+</span>, <span class="code-light">-</span>, <span class="code-light">*</span>, <span class="code-light">/</span>) and standard functions such as <span class="code-light">sqrt</span>, <span class="code-light">pow</span>, <span class="code-light">abs</span>, <span class="code-light">min</span>, and <span class="code-light">max</span>. 
This type is designed for lightweight transformations and derived values that do not require scripting.

Use Simple calculated fields when you need fast, declarative computations such as:
- Normalization and scaling (multipliers, offsets, calibration factors)
- Derived sensor metrics (e.g., dew point, heat index, power = voltage × current)
- Threshold-based values (clamping, simple scoring, deltas)
- Cross-entity calculations (e.g., combine device telemetry with asset attributes)

<hr>

## Configuration


Open the [create calculated field](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#creating-a-calculated-field) dialog and specify:
- the calculated field **title**,
- the **entity or entity profile** to which the calculated field will be applied,
- Select "**Simple**" as a calculated field **type**.

<hr>

### Arguments

For a Simple calculated field, arguments can be either [latest telemetry](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=latestTelemetry#arguments) or [attribute](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments).   
The data source can be **Current entity**, another **Device/Asset**, the **Customer**, the **Current tenant**, or the **Current owner**.

For details about argument types and configuration parameters, see the [Arguments](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments).

<hr>

### Expression

In the **Expression** section, define the calculation using a single mathematical formula.
- References [argument](#arguments) variables directly by name (e.g., temperature, humidity)
- Supports arithmetic operations (<span class="code-light">+</span>, <span class="code-light">-</span>, <span class="code-light">*</span>, <span class="code-light">/</span>) and standard functions such as <span class="code-light">abs</span>, <span class="code-light">sqrt</span>, <span class="code-light">pow</span>, <span class="code-light">min</span>, and <span class="code-light">max</span>.
- Produces a **single result value**, saved under the configured output key

<hr>

### Output

The calculation result is stored either as a [time series](/docs/user-guide/telemetry/) or an [attribute](/docs/user-guide/attributes/).

In Output, specify:
- **Key** — the name under which the computed value will be saved
- **Decimals** — optional rounding

> **[Only for Time series]**   
**Use latest timestamp** — stores the result using the most recent argument timestamp instead of server time.

For more details about output types and processing strategies, see the [Output](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#output).

<hr>

## Example: Dew point calculation

<b><font size="4">Scenario</font></b>   
The Smart Device sends <span class="code-light">temperature</span> and <span class="code-light">humidity</span> telemetry in real time.

<b><font size="4">Goal</font></b>   
Calculate the dew point and store the result as telemetry under the <span class="code-light">dewPoint</span> key on the same device.

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Dew point calculation" calculated field configuration (JSON)](/docs/user-guide/resources/calculated-fields/simple/dew_point_calculation_simple_cf.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo device</font></b>

Import a device that publishes temperature and humidity telemetry.
1. Download the CSV file: [dew-point-calculation-device-data.csv](/docs/user-guide/resources/calculated-fields/propagation/dew-point-calculation-device-data.csv)
2. Go to the "Devices" and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Smart Device
- **Type:** smart-device
- **Time series:** <span class="code-light">humidity</span>, <span class="code-light">temperature</span>

> **Important note about the CSV:** the column type for the <span class="code-light">humidity</span> and <span class="code-light">temperature</span> keys must be set to "**Time series**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/simple/simple-example-1-ce.webp" alt="Import a device that publishes **temperature** and **humidity** telemetry." loading="lazy"><figcaption>Import a device that publishes **temperature** and **humidity** telemetry.</figcaption></figure></div>


<br><b><font size="3">2. Apply the calculated field to the device profile</font></b>

During the Smart Device import, a "smart-device" profile is automatically created and assigned to it.   
Apply the calculated field to this profile so it runs for all devices that use the same profile.
1. [Download the calculated field configuration file (JSON)](/docs/user-guide/resources/calculated-fields/simple/dew_point_calculation_simple_cf.json).
2. Go to the "Calculated fields" tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.   

Expression used in this example:

```bash
(243.04 * (ln(humidity / 100) + 17.625 * temperature / (243.04 + temperature)) /
(17.625 - (ln(humidity / 100) + 17.625 * temperature / (243.04 + temperature))))
```


Output settings:
- **Output type:** Time series
- **Key:** <span class="code-light">dewPoint</span>


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/simple/simple-example-2-ce.webp" alt="Go to the **Calculated fields** tab and import the calculated field configuration." loading="lazy"><figcaption>Go to the **Calculated fields** tab and import the calculated field configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/simple/simple-example-3-ce.webp" alt="Apply the calculated field to the **smart-device** profile so it runs for all devices using it." loading="lazy"><figcaption>Apply the calculated field to the **smart-device** profile so it runs for all devices using it.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/simple/simple-example-4-ce.webp" alt="First argument settings:- **Entity type:** Current entity- **Argument type:** Latest telemetry- **Time series key:** humidity- **Argument name:** humidity." loading="lazy"><figcaption>First argument settings:<br>- **Entity type:** Current entity<br>- **Argument type:** Latest telemetry<br>- **Time series key:** humidity<br>- **Argument name:** humidity.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/simple/simple-example-5-ce.webp" alt="Second argument settings:- **Entity type:** Current entity- **Argument type:** Latest telemetry- **Time series key:** temperature- **Argument name:** temperature." loading="lazy"><figcaption>Second argument settings:<br>- **Entity type:** Current entity<br>- **Argument type:** Latest telemetry<br>- **Time series key:** temperature<br>- **Argument name:** temperature.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/simple/simple-example-6-ce.webp" alt="The specified **mathematical expression** calculates the dew point.The output value is stored as a time series under the **dewPoint** key.Click **Add** to save the calculated field." loading="lazy"><figcaption>The specified **mathematical expression** calculates the dew point.<br>The output value is stored as a time series under the **dewPoint** key.<br>Click **Add** to save the calculated field.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

The dew point is calculated and saved as telemetry on the Smart Device under the <span class="code-light">dewPoint</span> key.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/simple/simple-example-7-ce.webp" alt="The dew point is calculated and saved as telemetry on the Smart Device under the **dewPoint** key." loading="lazy"><figcaption>The dew point is calculated and saved as telemetry on the Smart Device under the **dewPoint** key.</figcaption></figure></div>


<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please contact us.
