+++
title = "Create and clear alarms"
description = "Create and clear alarms using an Alarm rules feature"

[extra]
status = "imported"
checked = ""
source = "docs/tutorials/create-clear-alarms.md"
+++
## Use case

Assume your refrigeration equipment is fitted with a temperature sensor that periodically publishes telemetry data to SENTIENT.

The normal operating temperature range is between 2 °C and 5 °C.   
If the reported temperature goes outside this range, it should be treated as an abnormal condition.

Your objective is to:
- **Create an alarm** when the temperature drops below **2 °C** or rises above **5 °C**
- **Automatically clear the alarm** when the temperature returns to the acceptable range

Although this scenario is simplified, it demonstrates a **common telemetry monitoring pattern** applicable to real-world IoT deployments such as **cold storage**, **food logistics**, and **industrial refrigeration systems**.

To keep the focus on platform capabilities rather than manual setup, the guide uses **predefined alarm rule configurations** that can be [imported](/docs/user-guide/alarm-rules/#export--import-alarm-rule) directly into SENTIENT. 
This allows you to quickly understand how alarm rules work, examine their logic, and reuse or adapt them for your own IoT scenarios.

<hr>

## Prerequisites

Before proceeding, review the [Alarm rules](/docs/user-guide/alarm-rules/) documentation, which explains the concepts of alarm creation, trigger conditions, and alarm lifecycle management used in this guide.

You will also need a device to test alarm triggering. You can use an existing device or [create a new one](/docs/user-guide/ui/devices/#adding-new-device) by following these steps:
1. Navigate to **Entities &#8702; Devices**.
2. Click the **"&#43; Add device** button in the top-right corner and select **"Add new device"**.
3. Create the device with the following parameters:   
   &#8194;&#8226;&#8194;**Device name**: Thermometer   
   &#8194;&#8226;&#8194;**Device profile**: thermostat
4. Click **Add** to complete the device creation.

The device is now ready to publish telemetry and be used for alarm rule testing.

> **Recommendation:** Apply alarm rules at the device profile level to avoid duplicating configurations across multiple devices of the same type and to ensure consistent alarm

<hr>

## Alarm rules configuration

You need to create two separate alarm rules, each responsible for a specific temperature threshold and alarm type.

<b><font size="3">High temperature alarm rule</font></b>   
- **Alarm type**: High temperature
- **Create alarm when**: temperature > 5 °C
- **Clear alarm when**: temperature ≤ 5 °C

<b><font size="3">Low temperature alarm rule</font></b>   
- **Alarm type**: Low temperature
- **Create alarm when**: temperature < 2 °C
- **Clear alarm when**: temperature ≥ 2 °C

Each alarm rule is evaluated every time telemetry is received from the target entity:
- The incoming temperature value is read
- The value is compared against the create and clear conditions
- If a condition is met, the alarm is created, updated, or cleared

## Step 1. Import High temperature alarm rule

1. Download the [High temperature alarm rule](/docs/user-guide/resources/guides/high_temperature_alarm_rule.json) configuration file.
2. Go to **Alarms &#8702; Alarm rules**.
3. Click the **"&#43; Add alarm rule"** in the top-right corner, and select **"Import alarm rule"**.
4. Specify your **device** or **device profile** as target entity.
5. Click **Add** to complete the import.

## Step 2. Import Low temperature alarm rule

1. Download the [Low temperature alarm rule](/docs/user-guide/resources/guides/low_temperature_alarm_rule.json) configuration file.
2. In **Alarms &#8702; Alarm rules**, click the **"&#43; Add alarm rule"** and select **"Import alarm rule"**. 
3. Specify your **device** or **device profile** as target entity.
4. Click **Add**.

## Verify alarm triggering

To verify that the alarm rules work correctly, publish several temperature values.   
The easiest way is to use [Check connectivity](/docs/user-guide/ui/devices/#check-connectivity). Alternatively, use the commands below.

⚠️ Replace    
&#8194;&#8226;&#8194;**$SENTIENT_HOST_NAME** with your SENTIENT hostname or IP address.   
&#8194;&#8226;&#8194;**$ACCESS_TOKEN** with the device access token.

1. Trigger the High temperature alarm.   
   Publish a temperature value above the upper threshold (for example, 7 °C).
   
   ```bash
   curl -v -X POST http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header Content-Type:application/json --data "{temperature:7}"
   ```
   
   
   
   

2. Clear High temperature alarm.   
   Publish a temperature value within the normal range (for example, 4 °C).
   
   ```bash
   curl -v -X POST http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header Content-Type:application/json --data "{temperature:4}"
   ```
   
   
   
   


3. Trigger Low temperature alarm.   
   Publish a temperature value below the lower threshold (for example, 1 °C).
   
   ```bash
   curl -v -X POST http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header Content-Type:application/json --data "{temperature:1}"
   ```
   
   
   
   


4. Clear Low temperature alarm.   
   Publish a temperature value within the acceptable range again (for example, 4 °C).
   
   ```bash
   curl -v -X POST http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header Content-Type:application/json --data "{temperature:4}"
   ```
   
   
   
   

After each step, observe the alarm state in the **Alarms** page, in the corresponding tab inside device details or on a dashboard to confirm correct behavior.

<hr>

## See also

- [Validate and filter incoming telemetry](/docs/tutorials/validate-incoming-telemetry)
- [Send email notifications on alarm events](/docs/tutorials/send-email/)

<hr>

## Next steps
