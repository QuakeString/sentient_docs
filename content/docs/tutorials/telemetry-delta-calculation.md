+++
title = "Telemetry delta calculation"
description = "Telemetry delta calculation using the Calculated fields feature"

[extra]
status = "imported"
checked = ""
source = "docs/tutorials/telemetry-delta-calculation.md"
+++
This guide explains how to calculate the difference (delta) between telemetry values in SENTIENT and use this calculated value to automatically trigger and clear alarms.

The guide is introductory and focuses on demonstrating the core capabilities of the platform rather than building configurations from scratch.   
For this reason, predefined configurations for calculated fields and alarm rules are provided and imported during the setup.

After importing these configurations into your SENTIENT instance, you can explore their structure, logic, and behavior, and later adapt them for your own use cases.

<hr>

## Use case

Assume you have a device equipped with a temperature sensor that periodically sends telemetry data to SENTIENT.

You need to:
- Monitor temperature changes over a fixed time window (for example, 15 minutes).
- Trigger an alarm when the temperature change exceeds a defined threshold (5 °C).
- Automatically clear the alarm when the value returns to normal.

This workflow represents a common real-time monitoring and anomaly detection scenario and can be easily extended to support more advanced use cases.

<hr>

## Prerequisites

Before proceeding, it is recommended to review the following SENTIENT documentation:
- [Calculated fields](/docs/user-guide/calculated-fields/) - learn how to compute new telemetry values based on incoming data.
- [Alarm rules](/docs/user-guide/alarm-rules) - learn how to define alarm trigger conditions to promptly respond to abnormal conditions.

These concepts are essential for understanding the configuration described below.

<hr>

## Step 1. Add demo device

Start by adding a demo device that publishes temperature telemetry.

The device serves as the source of telemetry data used by the calculated field and alarm rules.

<b><font size="3">Actions</font></b>

1. Navigate to **Entities** **&#8702;** **Devices**.
2. Click the **"&#43; Add device"** button in the top-right corner, select **"Add new device"** and create:   
&#8194;&#8226;&#8194;**Device name**: Thermometer   
&#8194;&#8226;&#8194;**Device profile**: thermostat

The device is registered in SENTIENT and ready to publish telemetry data.

<hr>

## Step 2. Import a calculated field for telemetry delta

The provided configuration calculates the temperature delta over the last 15 minutes and stores the result as a new telemetry key: <span class="code-light">deltaTemperature</span>.

<b><font size="3">Actions</font></b>

1. Download the calculated field configuration file:   
   [telemetry_delta_calculation_cf.json](/docs/user-guide/resources/guides/telemetry_delta_calculation_cf.json).
2. Navigate to the **Calculated fields** page.
3. Click the **"&#43; Add calculated field"** button in the top-right corner and select **"Import calculated field"**.
4. [Upload the calculated field configuration file](/docs/user-guide/calculated-fields/#export--import-calculated-field).
5. Select the <span class="code-light">thermostat</span> [device profile](/docs/user-guide/device-profiles/) as the target entity so the calculated field is applied automatically to all relevant devices.
6. Click **Add** to complete the import.

<b><font size="3">Calculation logic</font></b>
   
The calculated field script:
- Collects temperature values from the last 5 minutes
- Uses the first and last values within the time window
- Calculates their difference
- Stores the absolute value as telemetry

**Script used in this example**

function calculate(ctx, altitude, temperature) {
```js
var delta = 0;

if (temperature.values.size() >= 2) {
  delta = temperature.last - temperature.first;
}

return {
  "deltaTemperature": Math.abs(toInt(delta))
}
```

}

**Key points**
- If fewer than two values are available, the delta is set to <span class="code-light">0</span>
- The script is resilient to sparse telemetry
- The result is stored as **time series telemetry** and updated automatically

<hr>

## Step 3. Configure alarm rules based on telemetry delta

Configure the [alarm rule](/docs/user-guide/alarm-rules) that react to changes in the <span class="code-light">deltaTemperature</span> key value.

**Alarm logic:**   
&#8194;&#8226;&#8194;Trigger the alarm when <span class="code-light">deltaTemperature ≥ 5</span>   
&#8194;&#8226;&#8194;Clear the alarm when <span class="code-light">deltaTemperature < 5</span>

**Actions**
1. Download the alarm rule configuration file:   
   [temperature_deviation_alarm_rule.json](/docs/user-guide/resources/guides/temperature_deviation_alarm_rule.json).
2. Navigate to **Alarms** **&#8702;** **Alarm rules**.
3. [Upload the alarm rule configuration file](/docs/user-guide/alarm-rules/#export--import-alarm-rule).
4. Configure the alarm rule for a <span class="code-light">thermostat</span> [device profile](/docs/user-guide/device-profiles/) to ensure it is applied consistently to all devices that use this profile.
5. Click **Add**.

Once imported, the alarm lifecycle is managed automatically by SENTIENT.

<hr>

## Step 4. Verify the configuration

To confirm that everything works as expected, publish two temperature values within a 15-minute interval.

**Verification steps**

1. Publish an initial temperature value (for example, 25).   
   The easiest way is to use the [check connectivity](/docs/user-guide/ui/devices/#check-connectivity) feature. Alternatively, execute the command below:   
   > **Don&#39;t forget to replace:**   
   &#8194;&#8226;&#8194;<code></code> with your SENTIENT hostname or IP address.   
   &#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

   
   ```bash
   curl -v -X POST http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header Content-Type:application/json --data "{temperature:25}"
   ```
   
   
   
    

2. Open the device **Latest telemetry** tab to monitor incoming data in real time.   
   At this stage, you should see the following telemetry keys:
   - <span class="code-light">temperature = 25</span>
   - <span class="code-light">deltaTemperature = 0</span>

3. Publish a second temperature value within 15 minutes (for example, 32).   
   
   ```bash
   curl -v -X POST http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header Content-Type:application/json --data "{temperature:32}"
   ```
   
   
   
   

4. After the second update:   
   &#8194;&#8226;&#8194;<span class="code-light">deltaTemperature = 7</span>. The alarm is triggered because the threshold is exceeded
5. Open the **Alarms** tab to verify the alarm status.

As soon as the <span class="code-light">deltaTemperature</span> key value becomes less than <span class="code-light">5</span>, the alarm will be automatically cleared.

<hr>

## Next steps
