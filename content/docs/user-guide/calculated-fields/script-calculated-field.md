+++
title = "Script calculated field"
description = "For complex calculations, Rhai is used. It enables advanced operations such as conditional statements, loops, and access to historical data."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/calculated-fields/script-calculated-field.md"
+++
Script calculated fields use [Rhai](/docs/user-guide/rhai/) (SENTIENT Expression Language) to perform advanced, real-time computations on telemetry and attributes. Unlike Simple fields, Script fields support conditional logic, iteration over rolling time-series values, working with historical windows, and returning multiple results in a single execution.

Use "Script" calculated fields when you need logic that goes beyond a single math expression, such as:
- Multi-step calculations (e.g., dew point, air density, efficiency metrics)
- Conditional rules (e.g., generate status flags based on multiple inputs)
- Multi-output results (e.g., compute several derived values at once)
- Event-like telemetry generation (e.g., produce anomaly records with timestamps)
- Rolling analytics using historical windows (e.g., rolling average, trend detection, smoothing)

<hr>

## Configuration


Open the [create calculated field](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#creating-a-calculated-field) dialog and specify:
- the calculated field **title**,
- the **entity or entity profile** to which the calculated field will be applied,
- Select "**Script**" as a calculated field **type**.

<hr>

### Arguments

Arguments define which data sources and keys are passed into the script. For Script calculated fields, arguments can be [Latest telemetry](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=latestTelemetry#arguments), [Attribute](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments), or [time series rolling](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=timeSeriesRolling#arguments)).   
The data source can be **Current entity**, another **Device/Asset**, the **Customer**, the **Current tenant**, or the **Current owner**.

For details about argument types and parameters, see the [Arguments](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments) section in the Calculated fields documentation.

<hr>

### Script

Define the calculation logic using a [Rhai](/docs/user-guide/rhai/) function based on the variables configured in [Arguments](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#arguments).

Script calculated fields must implement:

```js
function calculate(ctx, arg1, arg2, ...): object | object[]
```
The function can return a single JSON object (multiple output keys) or an array of JSON objects (multiple time series records).

> The output variable names are defined directly in the returned object.

Example: Dew point calculation

```js
// Constants for Magnus formula
var a = 17.625;
var b = 243.04;

var alpha = ((a * temperature) / (b + temperature)) + Math.log(humidity / 100.0);
var dewPoint = toFixed((b * alpha) / (a - alpha), 1);

return {"dewPoint": dewPoint};
```


The function uses the <span class="code-light">temperature</span> and <span class="code-light">humidity</span> arguments to calculate the dew point value.
The calculation result will be stored in the variable <span class="code-light">dewPoint</span>, rounding the value to one decimal places.

<b><font size="4">Direct argument access</font></b>   
Arguments are also passed as function parameters (`arg1`, `arg2`, ...), so you can use them directly (for example, temperature, humidity) for cleaner scripts.

> Use either direct parameters or `ctx.args.<arg>` depending on clarity and your preferred style.

<br><b><font size="4">Context object (ctx)</font></b>

The `ctx` object provides metadata and access to argument values:
- `ctx.latestTs` — the most recent timestamp (milliseconds) from telemetry-based arguments. Useful for storing results with the same timestamp as incoming data.
- `ctx.args` — an object containing all configured arguments, accessible via dot (`.`) notation:
    - **Single-value arguments** <i>(attributes or latest telemetry)</i>
        - `ctx.args.<arg>.ts` — timestamp of the argument.
        - `ctx.args.<arg>.value` — value of the argument.
    - **Rolling time series arguments**
        - `ctx.args.<arg>.timeWindow` — object with start and end timestamps `{ startTs, endTs }`.
        - `ctx.args.<arg>.values` — array of `{ ts, value }` records representing timestamped telemetry.
        - `ctx.args.<arg>.<method>()` — built-in methods such as `mean()`, `sum()`, `min()`, `max()`, `first()`, `last()`, `merge()`, and others.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-function-1-ce.webp" alt="Define a function that will perform calculations using the variables defined in the &quot;Arguments&quot; section. The variable name that will store the calculation result is defined within the function itself." loading="lazy"><figcaption>Define a function that will perform calculations using the variables defined in the "Arguments" section. The variable name that will store the calculation result is defined within the function itself.</figcaption></figure></div>


<hr>

### Output

The calculation result is stored either as a [time series](/docs/user-guide/telemetry/) or an [attribute](/docs/user-guide/attributes/).   

For more details about output types and processing strategies, see the [Output](/docs/user-guide/calculated-fields/?calculatedfieldsargumenttype=attribute#output) section.

<hr>

## Examples

To help you get started, here are three common configuration patterns applied to real-world scenarios.

### Example 1: Fahrenheit to Celsius

<b><font size="4">Scenario</font></b>   
A device reports indoor temperature in **degrees Fahrenheit** as telemetry under the <span class="code-light">temperatureF</span> key.

<b><font size="4">Goal</font></b>   
Convert <span class="code-light">temperatureF</span> to **degrees Celsius**, round to two decimal places, and store the result as telemetry under the <span class="code-light">temperatureC</span> key using the same timestamp as the incoming data.

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Fahrenheit to Celsius" calculated field configuration (JSON)](/docs/user-guide/resources/calculated-fields/script/f_to_c_script_cf.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo device</font></b>

Import a device that publishes temperature telemetry.
1. Download the CSV file: [fahrenheit-to-celsius-calculation-device-data.csv](/docs/user-guide/resources/calculated-fields/script/fahrenheit-to-celsius-calculation-device-data.csv)
2. Go to the "Devices" and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Smart Device
- **Type:** smart-device
- **Time series:** <span class="code-light">temperatureF</span>

> **Important note about the CSV:** the column type for the <span class="code-light">temperatureF</span> key must be set to "**Time series**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-1-1-ce.webp" alt="Import a device that publishes temperature telemetry." loading="lazy"><figcaption>Import a device that publishes temperature telemetry.</figcaption></figure></div>


<br><b><font size="3">2. Apply the calculated field to the device profile</font></b>

1. [Download the calculated field configuration file (JSON)](/docs/user-guide/resources/calculated-fields/script/f_to_c_script_cf.json).
2. Go to the "Calculated fields" tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.   
   Apply a calculated field to the "smart-device" profile, which is automatically created during device import. This field will apply to all devices associated with this profile.

This configuration reads <span class="code-light">temperatureF</span>, converts it to Celsius, and stores the result as <span class="code-light">temperatureC</span>.

**Script used in this example:**

**function calculate(ctx, altitude, temperature) {**
```js
var temperatureC = (temperatureF - 32) / 1.8;
return {
    "ts": ctx.latestTs,
    "values": {
        "temperatureC": toFixed(temperatureC, 2)
    }
}
```

}


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-1-2-ce.webp" alt="Go to the **Calculated fields** tab and import the calculated field configuration." loading="lazy"><figcaption>Go to the **Calculated fields** tab and import the calculated field configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-1-3-ce.webp" alt="Apply the calculated field to the **smart-device** profile so it runs for all devices using it." loading="lazy"><figcaption>Apply the calculated field to the **smart-device** profile so it runs for all devices using it.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-1-4-ce.webp" alt="Argument settings:- **Entity type:** Current entity- **Argument type:** Latest telemetry- **Time series key:** temperatureF- **Argument name:** temperatureF." loading="lazy"><figcaption>Argument settings:<br>- **Entity type:** Current entity<br>- **Argument type:** Latest telemetry<br>- **Time series key:** temperatureF<br>- **Argument name:** temperatureF.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-1-5-ce.webp" alt="The specified script converts the temperature value from Fahrenheit to Celsius and stores the result under the temperatureC telemetry key.Click Add to save the calculated field." loading="lazy"><figcaption>The specified <b>script</b> converts the temperature value from Fahrenheit to Celsius and stores the result under the <b>temperatureC</b> telemetry key.<br>Click <b>Add</b> to save the calculated field.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

On the "Latest telemetry" tab of the Smart Device, the calculated temperature value in Celsius is displayed under a new telemetry key: <span class="code-light">temperatureC</span>.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-1-6-ce.webp" alt="On the &quot;Latest telemetry&quot; tab of the Smart Device, the calculated temperature value in Celsius is displayed under a new telemetry key: **temperatureC**." loading="lazy"><figcaption>On the "Latest telemetry" tab of the Smart Device, the calculated temperature value in Celsius is displayed under a new telemetry key: **temperatureC**.</figcaption></figure></div>


<hr>

### Example 2: Air density calculation

<b><font size="4">Scenario</font></b>   
The **Building A** asset has two associated devices:
- **Smart Device** — publishes temperature (Fahrenheit) as telemetry under (<span class="code-light">temperature</span>)
- **Altimeter** — provides altitude as a server attribute (<span class="code-light">altitude</span>)

<b><font size="4">Goal</font></b>   
Calculate air density based on:
- average temperature over the last 15 minutes (rolling window)
- altitude attribute

Store the result as a new telemetry value under the <span class="code-light">airDensity</span> key on Building A.

<b><font size="4">Calculated field configuration</font></b>   
[Click to download the "Air density calculation" field configuration (JSON)](/docs/user-guide/resources/calculated-fields/script/air_density_calculation_cf.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo device</font></b>

Import two devices: one publishing temperature telemetry and one providing altitude as an attribute.
1. Download the CSV file: [air-density-calculation-device-data.csv](/docs/user-guide/resources/calculated-fields/script/air-density-calculation-device-data.csv)
2. Go to the "Devices" and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

<b><font size="3">CSV includes:</font></b>

**Device 1**
- **Name:** Smart Device
- **Type:** smart-device
- **Time series:** <span class="code-light">temperature</span>

**Device 2**
- **Name:** Altimeter
- **Type:** height-sensor
- **Server attribute:** <span class="code-light">altitude</span>

> **Important notes about the CSV:**
- the column type for the <span class="code-light">temperature</span> key must be set to "**Time series**".
- the column type for the <span class="code-light">altitude</span> key must be set to "**Server attribute**".
 


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-1-ce.webp" alt="Go to the **Devices** and **import** device configurations from a CSV file." loading="lazy"><figcaption>Go to the **Devices** and **import** device configurations from a CSV file.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-2-ce.webp" alt="**Servet attribute:** altitude**Time series:** temperature" loading="lazy"><figcaption>**Servet attribute:** altitude<br>**Time series:** temperature</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-3-ce.webp" alt="The imported **Altimeter** device publishes **altitude** as a server-side attribute." loading="lazy"><figcaption>The imported **Altimeter** device publishes **altitude** as a server-side attribute.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-4-ce.webp" alt="The imported **Smart Device** publishes **temperature** as telemetry data." loading="lazy"><figcaption>The imported **Smart Device** publishes **temperature** as telemetry data.</figcaption></figure></div>


<br><b><font size="3">2. Import demo asset</font></b>

Import the asset that represents the building.
1. Download the CSV file: [air-density-calculation-asset-data.csv](/docs/user-guide/resources/calculated-fields/script/air-density-calculation-asset-data.csv)
2. Go to "Assets" and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Building A
- **Type:** building


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-5-ce.webp" alt="Import the demonstration asset Building A." loading="lazy"><figcaption>Import the demonstration asset Building A.</figcaption></figure></div>


<br><b><font size="3">3. Apply the calculated field to the asset profile</font></b>

Apply the calculated field to the "building" asset profile, so it runs for Building A.
1. [Download the calculated field configuration file](/docs/user-guide/resources/calculated-fields/script/air_density_calculation_cf.json).
2. Go to the "Calculated fields" tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.   

This configuration:
- reads rolling temperature from Smart Device
- reads altitude from Altimeter as an attribute
- calculates air density
- stores the output as telemetry on the asset

**Script used in this example:**

function calculate(ctx, altitude, temperature) {
```js
var avgTemperature = temperature.mean(); // Get average temperature
var temperatureK = (avgTemperature - 32) * (5 / 9) + 273.15; // Convert Fahrenheit to Kelvin

// Estimate air pressure based on altitude
var pressure = 101325 * Math.pow((1 - 2.25577e-5 * altitude), 5.25588);

// Air density formula
var airDensity = pressure / (287.05 * temperatureK);

return {
    "airDensity": toFixed(airDensity, 2)
};

```

}

<br>


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-6-ce.webp" alt="Go to the **Calculated fields** tab and import the calculated field configuration." loading="lazy"><figcaption>Go to the **Calculated fields** tab and import the calculated field configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-7-ce.webp" alt="Apply the calculated field to the **building** profile so it runs for all asset using it." loading="lazy"><figcaption>Apply the calculated field to the **building** profile so it runs for all asset using it.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-8-ce.webp" alt="First argument settings:- **Entity:** Altimeter- **Argument type:** Attribute- **Attribute scope:** Server attribute- **Attribute key:** altitude- **Argument name:** altitude" loading="lazy"><figcaption>First argument settings:<br>- **Entity:** Altimeter<br>- **Argument type:** Attribute<br>- **Attribute scope:** Server attribute<br>- **Attribute key:** altitude<br>- **Argument name:** altitude</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-9-ce.webp" alt="Second argument settings:- **Entity:** Smart Device- **Argument type:** Time series rolling- **Time series key:** temperature- **Argument name:** temperature- **Time window:** 15 minutes" loading="lazy"><figcaption>Second argument settings:<br>- **Entity:** Smart Device<br>- **Argument type:** Time series rolling<br>- **Time series key:** temperature<br>- **Argument name:** temperature<br>- **Time window:** 15 minutes</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-10-ce.webp" alt="The specified script calculates the air density and stores the result under the airDensity key.Click Add to save the calculated field." loading="lazy"><figcaption>The specified <b>script</b> calculates the air density and stores the result under the <b>airDensity</b> key.<br>Click <b>Add</b> to save the calculated field.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

In the "Latest telemetry" tab of the Building A asset, the calculated value appears under the <span class="code-light">airDensity</span> key.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-2-11-ce.webp" alt="In the **Latest telemetry** tab of the **Building A** asset, the calculated value appears under the **airDensity** key." loading="lazy"><figcaption>In the **Latest telemetry** tab of the **Building A** asset, the calculated value appears under the **airDensity** key.</figcaption></figure></div>


<hr>

### Example 3: Freezer temperature analysis

<b><font size="4">Scenario</font></b>   
A freezer device publishes two telemetry keys:
- <span class="code-light">temperature</span> — freezer temperature (°C)
- <span class="code-light">defrost</span> — defrost mode status (0 = OFF, 1 = ON)

<b><font size="4">Goal</font></b>   
Generate an event-like telemetry record under the issue key whenever:
- <span class="code-light">defrost</span> = 0 (defrost is OFF), and
- <span class="code-light">temperature</span> > -5°C

When the condition is met, store an "issue record" with a timestamp.

<b><font size="4">Calculated field configuration</font></b>   
[Download the "Freezer temperature analysis" calculated field configuration (JSON)](/docs/user-guide/resources/calculated-fields/script/freezer_temperature_analysis_cf.json).

<br><b><font size="4">Configuration steps</font></b>

<b><font size="3">1. Import demo device</font></b>

Import a device that publishes **temperature** and **defrost** data as telemetry.
1. Download the CSV file: [freezer-temperature-analysis-device-data.csv](/docs/user-guide/resources/calculated-fields/script/freezer-temperature-analysis-device-data.csv)
2. Go to the "Devices" and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Smart Device
- **Type:** smart-device
- **Time series:** <span class="code-light">temperature</span>, <span class="code-light">defrost</span>

> **Important note about the CSV:** the column type for the <span class="code-light">temperature</span> and <span class="code-light">defrost</span> keys must be set to "**Time series**".


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-3-1-ce.webp" alt="Import a device that publishes **temperature** and **defrost** data as telemetry." loading="lazy"><figcaption>Import a device that publishes **temperature** and **defrost** data as telemetry.</figcaption></figure></div>


<br><b><font size="3">2. Apply the calculated field to the device profile</font></b>

Apply the calculated field to the "smart-device" profile so it runs for the freezer device(s).

1. [Download the calculated field configuration file](/docs/user-guide/resources/calculated-fields/script/freezer_temperature_analysis_cf.json).
2. Go to the "Calculated fields" tab and [import](/docs/user-guide/calculated-fields/#export--import-calculated-field) the configuration.

This configuration:
- Aligns the temperature and defrost state data by timestamp.
- Selects only the moments when the temperature is higher than -5°C and defrost is off. 
- As a result, you get a list of such moments with the timestamp, the temperature value, and a <span class="code-light">defrostState</span>: **false** flag (or an empty list if no such moments exist).

**Script used in this example:**

function calculate(ctx, altitude, temperature) {
```js
var merged = temperature.merge(defrost);
var result = [];

foreach(item: merged) {
  if (item.v1 > -5.0 && item.v2 == 0) {
    result.add({
      ts: item.ts,
      values: {
        issue: {
          temperature: item.v1,
          defrostState: false
        }
      }
    });
  }
}

return result;
```

}

<br>


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-3-2-ce.webp" alt="Go to the **Calculated fields** tab and import the calculated field configuration." loading="lazy"><figcaption>Go to the **Calculated fields** tab and import the calculated field configuration.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-3-3-ce.webp" alt="Apply the calculated field to the **smart-device** profile so it runs for all devices using it." loading="lazy"><figcaption>Apply the calculated field to the **smart-device** profile so it runs for all devices using it.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-3-4-ce.webp" alt="First argument settings:- **Entity type:** Current entity- **Argument type:** Time series rolling- **Time series key:** defrost- **Argument name:** defrost- **Time window:** 15 minutes" loading="lazy"><figcaption>First argument settings:<br>- **Entity type:** Current entity<br>- **Argument type:** Time series rolling<br>- **Time series key:** defrost<br>- **Argument name:** defrost<br>- **Time window:** 15 minutes</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-3-5-ce.webp" alt="Second argument settings:- **Entity type:** Current entity- **Argument type:** Time series rolling- **Attribute key:** temperature- **Argument name:** temperature- **Time window:** 15 minutes" loading="lazy"><figcaption>Second argument settings:<br>- **Entity type:** Current entity<br>- **Argument type:** Time series rolling<br>- **Attribute key:** temperature<br>- **Argument name:** temperature<br>- **Time window:** 15 minutes</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-3-6-ce.webp" alt="The function aligns the temperature and defrost state data by timestamp, and then selects only the moments when the temperature is higher than -5°C and defrost is off.As a result, you get a list of such moments with the timestamp, the **temperature** value, and a **defrostState: false** flag (or an empty list if no such moments exist).Click **Add** to save the calculated field." loading="lazy"><figcaption>The function aligns the temperature and defrost state data by timestamp, and then selects only the moments when the temperature is higher than -5°C and defrost is off.<br>As a result, you get a list of such moments with the timestamp, the **temperature** value, and a **defrostState: false** flag (or an empty list if no such moments exist).<br>Click **Add** to save the calculated field.</figcaption></figure></div>


<br><b><font size="4">Result</font></b>

In the "Latest telemetry" tab of the Smart Device, the issue key appears when the condition is met, for example:

```json
{
  "issue": {
    "temperature": 0.8,
    "defrostState": false
  }
}

```

This indicates the freezer is in a potentially critical state and may require attention.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/script/script-cf-example-3-7-ce.webp" alt="In the **Latest telemetry** tab of the Smart Device, the issue key appears when the condition is met. This indicates the freezer is in a potentially critical state and may require attention." loading="lazy"><figcaption>In the **Latest telemetry** tab of the Smart Device, the issue key appears when the condition is met. This indicates the freezer is in a potentially critical state and may require attention.</figcaption></figure></div>


<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please contact us.
