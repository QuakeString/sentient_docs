+++
title = "Industrial Equipment Health — AI-Based Anomaly Detection with SENTIENT"
description = "Using Calculated Fields and Rule Engine AI nodes for predictive maintenance in SENTIENT"

[extra]
status = "imported"
checked = ""
source = "docs/samples/analytics/ai-predictive-maintenance.md"
+++
This document describes a SENTIENT solution that turns raw device telemetry into actionable maintenance insights:

**Workflow:**
1. Devices send `vibration` (mm/s), `temperature` (°C), and `acousticDev` (% deviation from baseline).
2. [Calculated Fields](/docs/user-guide/calculated-fields/) maintain a rolling window of the last N values (default: 100) and/or last M minutes for each metric.
3. The rolling window is forwarded to an AI Rule Node (OpenAI or another LLM provider).
4. If the AI detects an anomaly, the rule chain creates a SENTIENT Alarm and optionally sends a notification.


### Architecture

![image](/images/samples/analytics/iot-anomaly-detection-diagram.svg)

### Prerequisites

- SENTIENT version **4.2+**
- Device(s) capable of sending the required telemetry values (for this guide, we will emulate them)
- LLM provider credentials (OpenAI, Azure OpenAI, etc.)

### Telemetry Input and Output

**Expected telemetry keys (per device):**
- `vibration` — mm/s (float)
- `temperature` — °C (float)
- `acousticDev` — % deviation from baseline (float)

**AI Output:**
- `anomaly` — short label (e.g., `"Bearing Wear"`)
- `summary` — concise human-readable recommendation (e.g., `"Vibration has reached 7.4 mm/s and temperature is at 86°C accompanied by irregular acoustic patterns, indicating bearing wear. Recommend immediate bearing inspection and replacement to avoid catastrophic failure."`)

### Calculated field configuration

**Purpose:** Maintain a rolling window of the last N readings (default 100, configurable) efficiently and forward them directly to the AI node.

**Steps:**

<b>1. [Download](/docs/samples/analytics/resources/equipment_sensor.json)</b> and import the **EquipmentSensor** device profile into your SENTIENT instance.


<div class="st-gallery"><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-equipment-sensor-device-profile-1-ce.webp" alt="Navigate to the &quot;Device profiles&quot; page. Click the &quot;plus&quot; icon button, and select &quot;Import device profile&quot; from the dropdown menu." loading="lazy"><figcaption>Navigate to the "<b>Device profiles</b>" page. Click the "<b>plus</b>" icon button, and select "<b>Import device profile</b>" from the dropdown menu.</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-equipment-sensor-device-profile-2-ce.webp" alt="In the opened window, upload the JSON file with the device profile configuration and click &quot;Import&quot;." loading="lazy"><figcaption>In the opened window, upload the JSON file with the device profile configuration and click "<b>Import</b>".</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-equipment-sensor-device-profile-3-ce.webp" alt="You have imported the device profile configuration." loading="lazy"><figcaption>You have imported the device profile configuration.</figcaption></figure></div>


<b>2. [Download](/docs/samples/analytics/resources/rolling-window-records.json)</b> and import the calculated field into the **EquipmentSensor** device profile.


<div class="st-gallery"><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-calculated-field-into-profile-1-ce.webp" alt="Navigate to the &quot;Calculated fields&quot; tab of the target entity or profile. Click the &quot;plus&quot; icon button, and select &quot;Import calculated field&quot; from the dropdown menu." loading="lazy"><figcaption>Navigate to the "<b>Calculated fields</b>" tab of the target entity or profile. Click the "<b>plus</b>" icon button, and select "<b>Import calculated field</b>" from the dropdown menu.</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-calculated-field-into-profile-2-ce.webp" alt="In the opened window, upload the JSON file with the calculated field configuration and click &quot;Import&quot;." loading="lazy"><figcaption>In the opened window, <b>upload the JSON file</b> with the calculated field configuration and click "<b>Import</b>".</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-calculated-field-into-profile-3-ce.webp" alt="Verify the imported configuration: when importing, the edit window will open to allow modifications. Click &quot;Add&quot; to complete the import." loading="lazy"><figcaption>Verify the imported configuration: when importing, the edit window will open to allow modifications. Click "<b>Add</b>" to complete the import.</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-calculated-field-into-profile-4-ce.webp" alt="You have imported the calculated field configuration." loading="lazy"><figcaption>You have imported the calculated field configuration.</figcaption></figure></div>


**Key notes:**

- Rolling window time range is set to **1 day**.
- The number of stored values is set to **100**. The default maximum is 1000, configurable in system settings.
- The TBEL script outputs the rolling values in a single message to the rule engine:

```javascript
// Sample script to output raw values of the rolling arguments;
return {
    "acousticDevRecords": acousticDevRecords,
    "temperatureRecords": temperatureRecords,
    "vibrationRecords": vibrationRecords
};
```

### Rule chain configuration

**Purpose:** Analyze the rolling window data, classify anomalies, and generate a plain-language summary. Works with OpenAI or other LLM providers.

**Steps:**

- [Download](/docs/samples/analytics/resources/equipment_health_analysis.json) the <b>json file</b> with the "<b>Equipment Health Analysis</b>" rule chain configuration.


1. Navigate to the "<b>Rule chains</b>" page. Click the "<b>plus</b>" icon button, and select "<b>Import rule chain</b>" from the dropdown menu.

1. In the opened window, upload the JSON file with the rule chain configuration and click "<b>Import</b>".

1. Locate "<b>AI request</b>" node and enter its <b>edit mode</b>.

1. Click "<b>Create new</b>" AI model.

1. Enter a <b>name for the AI model</b>, choose the <b>AI provider</b>, and paste your <b>API key</b>. This example uses <b>o4-mini</b> from OpenAI. <b>Test connectivity</b> before saving. Then, click "<b>Save</b>".

1. <b>Apply changes</b> to "AI request" node.

1. <b>Save rule chain</b>.


<div class="st-gallery"><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-equipment-health-analysis-rule-chain-1-ce.webp" alt="Navigate to the &quot;Rule chains&quot; page. Click the &quot;plus&quot; icon button, and select &quot;Import rule chain&quot; from the dropdown menu." loading="lazy"><figcaption>Navigate to the "<b>Rule chains</b>" page. Click the "<b>plus</b>" icon button, and select "<b>Import rule chain</b>" from the dropdown menu.</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-equipment-health-analysis-rule-chain-2-ce.webp" alt="In the opened window, upload the JSON file with the rule chain configuration and click &quot;Import&quot;." loading="lazy"><figcaption>In the opened window, upload the JSON file with the rule chain configuration and click "<b>Import</b>".</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-equipment-health-analysis-rule-chain-3-ce.webp" alt="Locate &quot;AI request&quot; node and enter its edit mode." loading="lazy"><figcaption>Locate "<b>AI request</b>" node and enter its <b>edit mode</b>.</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-equipment-health-analysis-rule-chain-4-ce.webp" alt="Click &quot;Create new&quot; AI model." loading="lazy"><figcaption>Click "<b>Create new</b>" AI model.</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-equipment-health-analysis-rule-chain-5-ce.webp" alt="Enter a name for the AI model, choose the AI provider, and paste your API key. This example uses o4-mini from OpenAI. Test connectivity before saving. Then, click &quot;Save&quot;." loading="lazy"><figcaption>Enter a <b>name for the AI model</b>, choose the <b>AI provider</b>, and paste your <b>API key</b>. This example uses <b>o4-mini</b> from OpenAI. <b>Test connectivity</b> before saving. Then, click "<b>Save</b>".</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-equipment-health-analysis-rule-chain-6-ce.webp" alt="Apply changes to &quot;AI request&quot; node." loading="lazy"><figcaption><b>Apply changes</b> to "AI request" node.</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/import-equipment-health-analysis-rule-chain-7-ce.webp" alt="Save rule chain." loading="lazy"><figcaption><b>Save rule chain</b>.</figcaption></figure></div>


<b>5.</b> Update the <b>EquipmentSensor</b> profile to reference the "<b>Equipment Health Analysis</b>" rule chain.


<div class="st-gallery"><figure><img src="/images/samples/analytics/ai-predictive-maintenance/update-equipment-sensor-profile-1-ce.webp" alt="Go to the &quot;Device profiles&quot; page. Click on the &quot;EquipmentSensor&quot; profile and enter edit mode." loading="lazy"><figcaption>Go to the "<b>Device profiles</b>" page. Click on the "<b>EquipmentSensor</b>" profile and enter edit mode.</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/update-equipment-sensor-profile-2-ce.webp" alt="Specify &quot;Equipment Health Analysis&quot; as the default rule chain." loading="lazy"><figcaption>Specify "<b>Equipment Health Analysis</b>" as the default rule chain.</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/update-equipment-sensor-profile-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Important details:

* System and user prompts can reference incoming message data:
  * `$[*]` — entire message body
  * `${*}` — entire message metadata
  * `$[key]` — a specific message body field
  * `${key}` — a specific metadata value
* Supported response formats: **TEXT**, **JSON**, and **JSON Schema** (we use JSON Schema here).
* A **deduplication** node with a 5-second interval is used to reduce AI token usage.

### Testing

<b>Step 1.</b> Create a test device **Equipment Sensor 1** with the **EquipmentSensor** profile.


<div class="st-gallery"><figure><img src="/images/samples/analytics/ai-predictive-maintenance/create-test-device-1-ce.webp" alt="Navigate to the &quot;Devices&quot; page. Click the &quot;plus&quot; icon button, and select &quot;Add new device&quot; from the dropdown menu." loading="lazy"><figcaption>Navigate to the "<b>Devices</b>" page. Click the "<b>plus</b>" icon button, and select "<b>Add new device</b>" from the dropdown menu.</figcaption></figure><figure><img src="/images/samples/analytics/ai-predictive-maintenance/create-test-device-2-ce.webp" alt="Name the device &quot;Equipment Sensor 1&quot;. Set the device to the &quot;EquipmentSensor&quot; profile. Click &quot;Add&quot;." loading="lazy"><figcaption>Name the device "<b>Equipment Sensor 1</b>". Set the device to the "<b>EquipmentSensor</b>" profile. Click "<b>Add</b>".</figcaption></figure></div>


<b>Step 2.</b> Copy the "<b>Check connectivity</b>" command from the device details. 


<div class="st-gallery"><figure><img src="/images/samples/analytics/ai-predictive-maintenance/create-test-device-3-ce.webp" alt="Copy the check connection command." loading="lazy"><figcaption>Copy the <b>check connection</b> command.</figcaption></figure></div>


Your command will look something like this: 

```bash
curl -v -X POST http://localhost:8080/api/v1/6sED1ALqyJg0P6ezIODH/telemetry \
--header Content-Type:application/json \
--data "{temperature:25}"
```

<b>&#8195; *</b> Where `localhost:8080` is the <b>host of your SENTIENT instance</b>, and `6sED1ALqyJg0P6ezIODH` is the <b>device access token</b>.


<div class="st-gallery"><figure><img src="/images/samples/analytics/ai-predictive-maintenance/check-connectivity-command-from-device-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<br><b>Step 3.</b> Modify and send test data.

<b>Step 3.1 No alarm case:</b>


Send the following test data to SENTIENT. Be sure to replace:
- `$SENTIENT_HOST_NAME` with the host of your SENTIENT instance,
- `$YOUR_DEVICE_ACCESS_TOKEN` with your device&#39;s access token.

```bash
curl -v -X POST http://$SENTIENT_HOST_NAME/api/v1/$YOUR_DEVICE_ACCESS_TOKEN/telemetry \
--header Content-Type:application/json \
--data '{"vibration":4.2,"temperature":70,"acousticDev":5}'
```


There won&#39;t be an alarm created.


<div class="st-gallery"><figure><img src="/images/samples/analytics/ai-predictive-maintenance/send-test-data-no-alarm-case-1-ce.webp" alt="Send the following test data to SENTIENT. Be sure to replace $SENTIENT_HOST_NAME with the host of your SENTIENT instance, and $YOUR_DEVICE_ACCESS_TOKEN with your device&#39;s access token." loading="lazy"><figcaption>Send the following test data to SENTIENT. Be sure to replace $SENTIENT_HOST_NAME with the host of your SENTIENT instance, and $YOUR_DEVICE_ACCESS_TOKEN with your device&#39;s access token.</figcaption></figure></div>


<br>
<b>Step 3.2 Bearing wear detection:</b>


Simulate a bearing wear event by sending the following test data to SENTIENT. Be sure to replace:
- `$SENTIENT_HOST_NAME` with the host of your SENTIENT instance,
- `$YOUR_DEVICE_ACCESS_TOKEN` with your device&#39;s access token.

```bash
curl -v -X POST http://$SENTIENT_HOST_NAME/api/v1/$YOUR_DEVICE_ACCESS_TOKEN/telemetry \
--header Content-Type:application/json \
--data '{"vibration":8.2,"temperature":88,"acousticDev":5}'
```


<div class="st-gallery"><figure><img src="/images/samples/analytics/ai-predictive-maintenance/alarm-created-1-ce.webp" alt="Simulate a bearing wear event by sending the following test data to SENTIENT. Be sure to replace $SENTIENT_HOST_NAME with the host of your SENTIENT instance, and $YOUR_DEVICE_ACCESS_TOKEN with your device&#39;s access token." loading="lazy"><figcaption>Simulate a bearing wear event by sending the following test data to SENTIENT. Be sure to replace $SENTIENT_HOST_NAME with the host of your SENTIENT instance, and $YOUR_DEVICE_ACCESS_TOKEN with your device&#39;s access token.</figcaption></figure></div>


<br>An alarm will be created. Below is an example of the AI output:

```json
{
  "anomaly": "Bearing Wear",
  "summary": "Vibration has reached 7.4 mm/s and temperature is at 86 °C accompanied by irregular acoustic patterns, indicating bearing wear. Recommend immediate bearing inspection and replacement to avoid catastrophic failure."
}
```

<br>
<b>Step 3.3 Misalignment</b> detection:


Simulate a misalignment event by sending the following test data to SENTIENT. Be sure to replace:
- `$SENTIENT_HOST_NAME` with the host of your SENTIENT instance,
- `$YOUR_DEVICE_ACCESS_TOKEN` with your device&#39;s access token.

```bash
curl -v -X POST http://$SENTIENT_HOST_NAME/api/v1/$YOUR_DEVICE_ACCESS_TOKEN/telemetry \
--header Content-Type:application/json \
--data '{"vibration":32.2,"temperature":38,"acousticDev":5}'
```


<div class="st-gallery"><figure><img src="/images/samples/analytics/ai-predictive-maintenance/alarm-created-2-ce.webp" alt="Simulate a misalignment event by sending the following test data to SENTIENT. Be sure to replace $SENTIENT_HOST_NAME with the host of your SENTIENT instance, and $YOUR_DEVICE_ACCESS_TOKEN with your device&#39;s access token." loading="lazy"><figcaption>Simulate a misalignment event by sending the following test data to SENTIENT. Be sure to replace $SENTIENT_HOST_NAME with the host of your SENTIENT instance, and $YOUR_DEVICE_ACCESS_TOKEN with your device&#39;s access token.</figcaption></figure></div>


<br>An alarm will be created. Below is an example of the AI output:

```json
{
  "anomaly": "Misalignment",
  "summary": "A sudden vibration spike to 32.2 mm/s without a corresponding temperature rise or acoustic deviation indicates likely misalignment in the drive train. Please perform an immediate shaft-and-coupling alignment check to prevent further mechanical damage."
}
```

### Performance & Cost Controls

* **Batching & debounce**: Send to AI only after N points or every T seconds.
* **Early filters**: Skip AI call if all metrics are comfortably within normal bands.
* **Payload compacting**: Send statistics (min/mean/max/std, trend) instead of full arrays if prompt allows.

### Troubleshooting

* **No alarms**: 
  1. Verify raw device data is available in 'Latest telemetry' tab. 
  2. Enable and browse the calculated field debug events.
  3. Enable and browse the corresponding rule nodes debug events. 
* **High costs**: Increase the de-duplication period, tune prompt or switch AI model.

### Next steps

Experiment with AI prompts and share your feedback with community!
