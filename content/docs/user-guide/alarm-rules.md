+++
title = "Alarm rules"
description = "Creating alarm rules"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/alarm-rules.md"
+++
**Alarm rules** define the conditions for triggering alarms, the logic for setting severity levels, and the rules for clearing and automatically closing notifications. This enables administrators and developers to maintain full control over system behavior in real time and respond promptly to abnormal conditions.

Starting from SENTIENT **4.3**, alarm rule configuration capabilities have been significantly enhanced. Rules can now be defined at the level of a [Device](/docs/user-guide/ui/devices/), [Asset](/docs/user-guide/ui/assets/), **their Profiles**, or even a [Customer](/docs/user-guide/ui/customers/), enabling a multi-layered monitoring system that respects organizational structure and contextual logic. This approach allows precise control over when and where an alarm should be raised — globally, at the profile level, or for a specific device or entity.

Unified mechanisms for alarm uniqueness, severity levels, timestamps, and alarm propagation ensure consistent data handling and help operators efficiently analyze, filter, and process critical events.

<hr>

## Create alarm rule

The **alarm rules page** allows you to centrally manage all alarm rules in the system — both for individual entities and for profiles.

> **Note:** The process of creating an alarm rule is the same for [Devices](/docs/user-guide/ui/devices/), [Assets](/docs/user-guide/ui/assets/), [Device profiles](/docs/user-guide/device-profiles/), [Asset profiles](/docs/user-guide/asset-profiles/), and [Customers](/docs/user-guide/ui/customers/).
 
- Open the **Alarms** page from the left-hand menu.
- Go to the **Alarm rules** tab.
- Click the "**+**" button in the top-right corner.
- Select **Create new alarm rule** from the dropdown menu.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-1-add-alarm-rule-1-ce.webp" alt="Open the Alarms page from the left-hand menu. Go to the Alarm rules tab.This page allows you to centrally manage all alarm rules in the system — both for individual entities and for profiles." loading="lazy"><figcaption>Open the <b>Alarms</b> page from the left-hand menu. Go to the <b>Alarm rules</b> tab.<br>This page allows you to centrally manage all alarm rules in the system — both for individual entities and for profiles.</figcaption></figure></div>


> **Recommendation:** Create alarm rules in **Device profiles** or **Asset profiles** to avoid duplicating configurations across multiple entities.

<hr>

### General

The "General" section defines the basic configuration of the alarm rule:
- **Alarm type** — the name and unique identifier of the alarm (for example, "High Temperature"). The alarm type defines which event the alarm represents and allows SENTIENT to determine whether a new alarm should be created or an existing active one should be updated.
- **Entity type** - the target entity or entity profile where the alarm rule will be applied.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-2-general-section-1-ce.webp" alt="Specify the alarm type — the name and unique identifier of the alarm.- Set the entity type - the target entity or entity profile where the alarm rule will be applied." loading="lazy"><figcaption>Specify the <b>alarm type</b> — the name and unique identifier of the alarm.<br>- Set the <b>entity type</b> - the target entity or entity profile where the alarm rule will be applied.</figcaption></figure></div>


<br>


<b><font size="3">Debug mode</font></b>

Enabling debug mode allows you to track events, states, and potential errors related to the execution of alarm rule. This greatly simplifies development and troubleshooting.


<div class="st-callout info">


**Note:** Debug mode can quickly increase disk usage because all debug events are stored in the database.
Starting from **SENTIENT 3.9**, the platform stores the full set of debug events only during the first **15 minutes** after the alarm rule is created; afterward, only error events are retained.


</div>


Debug mode settings can be combined or disabled entirely.

<hr>

### Arguments

Before defining alarm conditions, you must add at least one **argument** — a data source that the rule will use during evaluation.

Click **Add argument** and configure the following parameters:


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-3-arguments-1-ce.webp" alt="Before defining alarm conditions, you must add at least one argument — a data source that the rule will use during evaluation.Click Add argument and configure the following parameters." loading="lazy"><figcaption>Before defining alarm conditions, you must add at least one <b>argument</b> — a data source that the rule will use during evaluation.Click <b>Add argument</b> and configure the following parameters.</figcaption></figure></div>


<b><font size="3">Entity type</font></b>

Defines where the argument value comes from:
- **Current entity** — the entity you are configuring (device, asset, customer, or profile).   
  If the rule is created at the **Device profile** or **Asset profile** level, it will apply to all entities that use this profile.
- Another **Device or Asset** — references telemetry or attributes from a different device or asset.
- **Customer** — retrieves data from the associated customer entity.
- **Current tenant** — uses data from the tenant entity.
- **Current owner** — data from the owner of the current entity.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-3-arguments-2-ce.webp" alt="Entity type defines where the argument value comes from." loading="lazy"><figcaption><b>Entity type</b> defines where the argument value comes from.</figcaption></figure></div>


<b><font size="3">Argument type</font></b>

Defines what kind of data the argument will represent:
- **Attribute**. Uses a key–value attribute stored on the entity. (e.g., model, max temperature).   
  You must specify:
  - **Attribute scope**: **Server** attributes, **Client** attributes, or **Shared** attributes
  - **Attribute key**
  - Optional: **Default value** (used when attribute value is missing)
- **Latest telemetry**. Uses the latest time series value from the entity. (e.g., temperature, speed, voltage).
  You must specify:
  - **Time series key**
  - Optional: **Default value**


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-3-arguments-3-ce.webp" alt="Argument type defines what kind of data the argument will represent." loading="lazy"><figcaption><b>Argument type</b> defines what kind of data the argument will represent.</figcaption></figure></div>


<b><font size="3">Argument name</font></b>

Enter an argument name — the identifier you will use in formulas and conditions (e.g., temperature, maxThreshold, deviceEnabled).

After configuring the fields, click **Add**.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-3-arguments-4-ce.webp" alt="Argument name — the identifier you will use in formulas and conditions.After configuring the fields, click Add." loading="lazy"><figcaption><b>Argument name</b> — the identifier you will use in formulas and conditions.<br>After configuring the fields, click <b>Add</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-3-arguments-5-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<hr>

### Trigger conditions

This step defines the core logic of the alarm rule:
- **when** the alarm should be created,
- **which severity** it receives, and
- **when** the rule is active based on the schedule.

Click **Add trigger condition** and configure the following parameters:


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-4-creation-conditions-1-ce.webp" alt="This step defines the core logic of the alarm rule.Click Add trigger condition and configure the following parameters." loading="lazy"><figcaption>This step defines the core logic of the alarm rule.<br>Click <b>Add trigger condition</b> and configure the following parameters.</figcaption></figure></div>


<hr>

#### Severity

In SENTIENT, **alarm severity** indicates how critical an alarm condition is and helps prioritize response actions.   
The following severity levels are available:
- <span style="color:#d12730">Critical</span> — Indicates a severe condition that requires **immediate action**, such as equipment failure, safety risks, or conditions that may cause data loss or system downtime. 
- <span style="color:#f66716">Major</span> — Represents a significant issue that can impact system operation but is **not immediately critical**, for example, performance degradation or operation outside recommended parameters. 
- <span style="color:#faa405">Minor</span> — Used for less severe problems that should be **monitored or addressed later**, such as temporary threshold violations or early warning conditions. 
- <span style="color:#f2da05">Warning</span> — Indicates a **potential or emerging issue** that does not yet affect normal operation but may require attention if it persists. 
- <span style="color:#9e9e9e">Indeterminate</span> — Used when an alarm is raised but the **severity cannot be clearly determined**, often due to incomplete data or ambiguous conditions.

Choosing the appropriate severity helps ensure effective monitoring, escalation, and response in IoT systems.

<b><font size="3">How severity works</font></b>

The severity level applies to:
- **New alarms** created by the rule
- **Updates to an existing active alarm**, when the create condition triggers again with different criteria 
  For example, if a *Warning* alarm remains active but the new condition qualifies as *Major*, the severity will be increased.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-4-creation-conditions-severity-1-ce.webp" alt="Severity defines the criticality of the alarm at the moment it is created.It affects incident prioritization, UI representation, and automation workflows (Rule Engine, notification rules, etc.)." loading="lazy"><figcaption><b>Severity</b> defines the criticality of the alarm at the moment it is created.<br>It affects incident prioritization, UI representation, and automation workflows (Rule Engine, notification rules, etc.).</figcaption></figure></div>


<hr>

#### Condition

The **Condition** defines the logic that determines whether an alarm should be created or updated.   
This is the primary expression used to evaluate whether the rule is fulfilled.

Examples use cases:
- <span class="code-light">temperature > 30</span>
- <span class="code-light">device is offline</span>
- complex expressions using multiple arguments, telemetry fields, or attributes   
  (e.g., <span class="code-light">temperature > threshold AND doorState == open</span>)

<hr>

<b><font size="3">Add create condition</font></b>

Click **Add condition**

Configure the alarm trigger logic by defining one or more filters.

> You can create filters manually or use [TBEL](/docs/user-guide/tbel/) script functions for more advanced expressions.

Click **Add argument filter** and configure:

**1. General configuration**   
- **Argument** — the variable you want to compare (e.g., temperature)
- **Value type** — the data type of the value being evaluated (Numeric, Boolean, String, etc.)

**2. Configure filters**   
Under **Filters**, click **Add** and specify:
- **Operation** — the comparison operator, such as: *equal, not equal, missing for, greater than, less than, etc*.
- **Value source** — select one of the following:
  - **Static** — use a fixed predefined value 
  - **Dynamic** — use a value retrieved from another argument 
- **Value** — specify the value to compare against

**Combine multiple conditions**   
If you add more than one filter, choose a logical operator:
- **AND** — all conditions must be true
- **OR** — at least one condition must be true

After adding all required filters, click **Add** to save the condition.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-4-creation-condition-add-filter-1-ce.webp" alt="Click Add condition." loading="lazy"><figcaption>Click <b>Add condition</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-4-creation-condition-add-filter-2-ce.webp" alt="Configure the alarm trigger logic by defining one or more filters. Click Add argument filter." loading="lazy"><figcaption>Configure the alarm trigger logic by defining one or more filters. Click <b>Add argument filter</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-4-creation-condition-add-filter-3-ce.webp" alt="General configuration:- Argument — the variable you want to compare (e.g., temperature).- Value type — the data type of the value being evaluated (Numeric, Boolean, String, etc.)." loading="lazy"><figcaption><b>General configuration</b>:<br>- <b>Argument</b> — the variable you want to compare (e.g., temperature).<br>- <b>Value type</b> — the data type of the value being evaluated (Numeric, Boolean, String, etc.).</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-4-creation-condition-add-filter-4-ce.webp" alt="Configure filters:- Operation — the comparison operator.- Value source — select one of the following.- Value — specify the value to compare against.- After adding all required filters, click Add to save the condition." loading="lazy"><figcaption><b>Configure filters</b>:<br>- <b>Operation</b> — the comparison operator.<br>- <b>Value source</b> — select one of the following.<br>- <b>Value</b> — specify the value to compare against.<br>- After adding all required filters, click <b>Add</b> to save the condition.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-4-creation-condition-add-filter-5-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<b><font size="3">Condition types</font></b>

SENTIENT supports **three types** of conditions:

- **Simple.**   
  Triggers immediately when the expression becomes true.   
  Used for instant threshold violations.   
  *Example:* <span class="code-light">temperature > 10</span>
- **Duration.**   
  The condition must stay true continuously for a defined time period.   
  Helps reduce false positives caused by short data spikes.   
  *Example:* <span class="code-light">temperature > 10</span> for 60 seconds 
- **Repeating.**   
  Triggers only after the condition occurs a specified number of times.   
  Useful when repeated errors matter more than a single event.   
  *Example:* <span class="code-light">signalLost == true</span> three times in a row


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-4-creation-condition-types-1-ce.webp" alt="SENTIENT supports three types of conditions:- Simple. Triggers immediately when the expression becomes true. - Duration. The condition must stay true continuously for a defined time period.- Repeating. Triggers only after the condition occurs a specified number of times." loading="lazy"><figcaption>SENTIENT supports three types of conditions:<br>- <b>Simple.</b> Triggers immediately when the expression becomes true. <br>- <b>Duration.</b> The condition must stay true continuously for a defined time period.<br>- <b>Repeating.</b> Triggers only after the condition occurs a specified number of times.</figcaption></figure></div>


<hr>

#### Schedule

The **Schedule** defines the time periods during which the alarm creation rule is active.   
The system evaluates create conditions only when the current time falls within an allowed interval.

> If the create condition becomes true **outside the defined schedule**, the alarm **will not be created** — even if the logical expression evaluates to true.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-4-schedule-1-ce.webp" alt="The Schedule defines the time periods during which the alarm creation rule is active. The system evaluates create conditions only when the current time falls within an allowed interval." loading="lazy"><figcaption>The <b>Schedule</b> defines the time periods during which the alarm creation rule is active. The system evaluates create conditions only when the current time falls within an allowed interval.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-4-schedule-2-ce.webp" alt="If the create condition becomes true outside the defined schedule, the alarm will not be created — even if the logical expression evaluates to true." loading="lazy"><figcaption>If the create condition becomes true <b>outside the defined schedule</b>, the alarm <b>will not be created</b> — even if the logical expression evaluates to true.</figcaption></figure></div>


<b><font size="3">Schedule types</font></b>

**Static mode**

SENTIENT supports three schedule modes:
- **Active all time** — always active
- **Active at a specific time range**
  *Example:* Mon–Fri, 09:00–18:00 
- **Custom schedule** - define different intervals for each day of the week


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-4-schedule-types-1-ce.webp" alt="Active all time — always active" loading="lazy"><figcaption><b>Active all time</b> — always active</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-4-schedule-types-2-ce.webp" alt="Active at a specific time range Example: Mon–Fri, 09:00–18:00" loading="lazy"><figcaption><b>Active at a specific time range</b> <i>Example:</i> Mon–Fri, 09:00–18:00</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-4-schedule-types-3-ce.webp" alt="Custom schedule - define different intervals for each day of the week" loading="lazy"><figcaption><b>Custom schedule</b> - define different intervals for each day of the week</figcaption></figure></div>


**Dynamic mode**

Instead of configuring the schedule manually, you can provide a JSON object through an attribute or telemetry.
This is useful when the schedule needs to vary from one device to another or from one customer to another.

**How to enable dynamic mode**
- In the **Schedule** section, choose **Dynamic mode**.
- Select the argument (attribute or telemetry) that contains the JSON with the desired schedule configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-4-schedule-dynamic-mode-1-ce.webp" alt="Dynamic mode. Instead of configuring the schedule manually, you can provide a JSON object through an attribute or telemetry. This is useful when the schedule needs to vary from one device to another or from one customer to another." loading="lazy"><figcaption><b>Dynamic mode</b><br>. Instead of configuring the schedule manually, you can provide a JSON object through an attribute or telemetry. This is useful when the schedule needs to vary from one device to another or from one customer to another.</figcaption></figure></div>


<b><font size="3">Examples of schedule JSON</font></b>

**1. Active all time**

The JSON object may include:

```json
{}
```


or

```json
{
  "type": "ANY_TIME"
}
```


<br>
**2. Specific time schedule**

This format allows you to define an exact time range for selected days of the week.

**Example:**   
Active all day on **Tuesday** and **Thursday**:

```json
{
  "type": "SPECIFIC_TIME",
  "daysOfWeek": [2, 4],
  "startsOn": 0,
  "endsOn": 0,
  "timezone": "Europe/Kiev"
}
```


**Field explanation:**
- **timezone** — the time zone in which the schedule is interpreted
- **daysOfWeek** — days of the week in numeric format (1–7, where 1 = Monday)
- **startsOn** — the start of the active period, in milliseconds from the beginning of the day 
- **endsOn** — the end of the active period, in milliseconds from the beginning of the day

When both **startsOn** and **endsOn** are set to **0**, it means the rule is active for the entire day.

<br>
**3. Custom schedule**

Defines a separate time interval for each individual day.

**Example:**   
The schedule is active every day for the full 24 hours:

```json
{
  "type": "CUSTOM",
  "timezone": "Europe/Kiev",
  "items": [
    { "dayOfWeek": 1, "enabled": true, "startsOn": 0, "endsOn": 0 },
    { "dayOfWeek": 2, "enabled": true, "startsOn": 0, "endsOn": 0 },
    { "dayOfWeek": 3, "enabled": true, "startsOn": 0, "endsOn": 0 },
    { "dayOfWeek": 4, "enabled": true, "startsOn": 0, "endsOn": 0 },
    { "dayOfWeek": 5, "enabled": true, "startsOn": 0, "endsOn": 0 },
    { "dayOfWeek": 6, "enabled": true, "startsOn": 0, "endsOn": 0 },
    { "dayOfWeek": 7, "enabled": true, "startsOn": 0, "endsOn": 0 }
  ]
}
```


**Field explanation:**

- **timezone** — the time zone used for interpreting the schedule
- **items** — an array containing the configuration for each day

Each item includes:
- **daysOfWeek** - a list of days in numeric format (Monday = 1, Tuesday = 2, etc.) during which the schedule will be active.
- **enabled** — whether the rule is active on that day
- **startsOn** - a timestamp in milliseconds from which the schedule becomes active for the specified days.
- **endsOn**: - a timestamp in milliseconds until which the schedule remains active for the specified days.

When both **startsOn** and **endsOn** are set to **0**, it means the rule is active for the entire day.

<hr>

#### Additional info

The **Additional info** field allows you to enrich an alarm with extra contextual data that may be useful for incident analysis or troubleshooting.
This information is stored together with the alarm and displayed in the alarm details view, helping operators, technicians, and analysts work more efficiently.

**Examples of useful additions:**
- operator notes
- troubleshooting steps
- links to documentation
- contextual fields such as:
  - zone ID 
  - critical threshold description 
  - responsible person

<hr>

#### Mobile dashboard

This option defines which **mobile dashboard** will open in the SENTIENT mobile app when a user views the alarm.

<b><font size="3">How it works</font></b>

After selecting a mobile dashboard:
- the mobile app automatically opens it when navigating to the alarm 
- the user immediately sees relevant widgets and indicators 
- troubleshooting becomes much faster

<b><font size="3">Example use cases</font></b>

- Diagnostic dashboard for **High Temperature** alarms
- Technician-focused dashboard with control buttons
- Geolocation dashboard for mobile assets

<b><font size="3">Especially useful when:</font></b>
- field engineers respond to alarms on-site
- quick diagnostics is required
- monitoring distributed devices (refrigerators, sensors, vehicles)

<hr>

### Clear condition

The **Clear condition** defines the logic by which SENTIENT automatically transitions an alarm into the **Cleared** state.

If no clear condition is configured, the alarm will **never** clear automatically, even if the monitored values return to normal.   
In such cases, the alarm can only be cleared manually — via the UI or API.

Click **Add clear condition** and configure the following parameters:


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-5-clear-conditions-1-ce.webp" alt="Click Add clear condition." loading="lazy"><figcaption>Click <b>Add clear condition</b>.</figcaption></figure></div>


<br><b><font size="4">Step 5.1 Clear condition</font></b>

The Clear condition specifies **when an alarm is considered resolved** and can safely transition into the *Cleared* state.

**Examples of clear conditions:**
 - <span class="code-light">temperature ≤ 30</span>
- values return to normal ranges 
- device connection restored 
- complex expressions involving multiple arguments

<hr>

<b><font size="3">Add clear condition</font></b>

Click **Add condition** to define the logic for clearing the alarm.

Configure the clear condition by adding one or more filters.   
Filters can be created manually or using TBEL script functions for more advanced scenarios.

**1. General configuration**   
Click **Add argument filter** and specify:
- **Argument** — the variable to evaluate (e.g., temperature)
- **Value type** — the expected input type (Numeric, Boolean, String, etc.)

**2. Configure filters**   
In the **Filters** section, click **Add** and set:
- **Operation** — the comparison operator, for example: *equal, not equal, missing for, greater than, less than, greater or equal, less or equal, starts with, ends with, contains, not contains, in, not in*.
- **Value source:**
  - **Static** — use a fixed value 
  - **Dynamic** — use a value retrieved from another argument
- **Value** — the value to compare against

**Combine multiple conditions**   
If you add more than one filter, choose a logical operator:
- **AND** — all conditions must be true 
- **OR** — at least one condition must be true

After adding all required filters, click **Add** to save the clear condition.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-5-clearing-condition-add-filter-1-ce.webp" alt="Click Add condition." loading="lazy"><figcaption>Click <b>Add condition</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-5-clearing-condition-add-filter-2-ce.webp" alt="Configure the alarm trigger logic by defining one or more filters. Click Add argument filter." loading="lazy"><figcaption>Configure the alarm trigger logic by defining one or more filters. Click <b>Add argument filter</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-5-clearing-condition-add-filter-3-ce.webp" alt="- Argument — the variable you want to compare (e.g., temperature)- Value type — the data type of the value being evaluated (Numeric, Boolean, String, etc.)." loading="lazy"><figcaption>- <b>Argument</b> — the variable you want to compare (e.g., temperature)<br>- <b>Value type</b> — the data type of the value being evaluated (Numeric, Boolean, String, etc.).</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-5-clearing-condition-add-filter-4-ce.webp" alt="Configure filters.- Operation — the comparison operator.- Value source — select one of the following.- Value — specify the value to compare against- After adding all required filters, click Add to save the condition." loading="lazy"><figcaption><b>Configure filters</b>.<br>- <b>Operation</b> — the comparison operator.<br>- <b>Value source</b> — select one of the following.<br>- <b>Value</b> — specify the value to compare against<br>- After adding all required filters, click <b>Add</b> to save the condition.</figcaption></figure></div>


**Condition types**

SENTIENT supports the same condition types as for alarm creation:
- **Simple** — clears immediately when the condition becomes true
- **Duration** — must remain true for a specified period before clearing
- **Repeating** — the condition must be satisfied a certain number of times before clearing


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-5-clearing-condition-add-filter-5-ce.webp" alt="SENTIENT supports three types of conditions:- Simple. Clears immediately when the condition becomes true. - Duration. Must remain true for a specified period before clearing.- Repeating. The condition must be satisfied a certain number of times before clearing." loading="lazy"><figcaption>SENTIENT supports three types of conditions:<br>- <b>Simple.</b> Clears immediately when the condition becomes true. <br>- <b>Duration.</b> Must remain true for a specified period before clearing.<br>- <b>Repeating.</b> The condition must be satisfied a certain number of times before clearing.</figcaption></figure></div>


After completing all required configurations, click **Save** to store the clear condition.

<hr>

<b><font size="4">Step 5.2 Schedule</font></b>

The **Clear Schedule** defines *when* a clear condition is allowed to trigger.

**Example use cases:**
- callow automatic clearing only during working hours 
- allow clearing only at night 
- restrict clearing during specific time intervals

> If the clear condition becomes true outside the allowed schedule, the alarm will not be cleared 


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-5-schedule-1-ce.webp" alt="The clear schedule defines when a clear condition is allowed to trigger." loading="lazy"><figcaption>The <b>clear schedule</b> defines <i>when</i> a clear condition is allowed to trigger.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-5-schedule-2-ce.webp" alt="Example use cases:- callow automatic clearing only during working hours- allow clearing only at night- restrict clearing during specific time intervals." loading="lazy"><figcaption>Example use cases:<br>- callow automatic clearing only during working hours<br>- allow clearing only at night<br>- restrict clearing during specific time intervals.</figcaption></figure></div>


<hr>

<b><font size="4">Step 5.3 Additional info</font></b>

This block allows you to attach extra data that will be stored in **Alarm Details** at the moment the alarm is cleared.

Useful for:
- keeping a structured event log
- adding operator notes 
- saving additional diagnostic context 
- providing hints for follow-up actions

Supports dynamic placeholders using *${attributeName}*.

<hr>

<b><font size="4">Step 5.4 Mobile dashboard</font></b>

Defines which mobile dashboard is opened in the SENTIENT mobile app when viewing a cleared alarm.

This is useful when:
- additional diagnostics should be shown after clearance
- the operator must confirm system recovery
- the user needs to be redirected to another scenario or dashboard

<hr>

### Configure the advanced settings

In this step, you can define **alarm propagation** — how the alarm is distributed across other entities in the system.      
Propagation determines **who can see the alarm** and at **which level of the entity hierarchy** it becomes visible.

This is especially important for multi-level asset structures, customer hierarchies, enterprise environments, and MSP deployments.

<hr>

<b><font size="3">Available propagation options</font></b>

<b><font size="3">Propagate alarm to related entities</font></b>

When enabled, the alarm becomes visible to **all entities related** to the originator, regardless of the relation type.

Useful when:
- a **Device** is assigned to an **Asset**
- an **Asset** is linked to a **Customer**
- you want alarms to be visible across interconnected entities

This ensures that all entities within the relation graph—such as *Device &#8702; Office &#8702; Building* — can view and process the alarm.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-6-propagate-alarm-1-ce.webp" alt="Propagate alarm to related entities.When enabled, the alarm becomes visible to all entities related to the originator, regardless of the relation type." loading="lazy"><figcaption><b>Propagate alarm to related entities</b>.<br>When enabled, the alarm becomes visible to all entities related to the originator, regardless of the relation type.</figcaption></figure></div>


<hr>

<b><font size="3">Propagate alarm to the owner (Customer / Tenant)</font></b>

Makes the alarm visible to the **direct owner** of the originator — either a **Customer** or the **Tenant**.

This allows owners to see alarms from all their managed devices/assets **without needing to set up additional relations**.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-6-propagate-alarm-2-ce.webp" alt="Propagate alarm to the owner (Customer / Tenant).Makes the alarm visible to the direct owner of the originator — either a Customer or the Tenant." loading="lazy"><figcaption><b>Propagate alarm to the owner (Customer / Tenant)</b>.<br>Makes the alarm visible to the direct owner of the originator — either a Customer or the Tenant.</figcaption></figure></div>


<hr>

 

<b><font size="3">Propagate alarm to Tenant</font></b>

Makes the alarm visible **at the Tenant level**, regardless of ownership or relations.

**Use this when:**
- the Tenant Administrator needs visibility into **all critical events**
- a **centralized overview** of the entire infrastructure is required

This is the most global visibility option.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-6-propagate-alarm-3-ce.webp" alt="Propagate alarm to Tenant.Makes the alarm visible at the Tenant level, regardless of ownership or relations." loading="lazy"><figcaption><b>Propagate alarm to Tenant</b>.<br>Makes the alarm visible at the Tenant level, regardless of ownership or relations.</figcaption></figure></div>


<hr>

### Save the rule

Click **Add** to save the rule configuration.

After saving, SENTIENT will automatically begin creating, updating, and processing alarms according to the conditions, schedule, and propagation settings you defined.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/step-7-save-rule-1-ce.webp" alt="Click Add to save the rule configuration." loading="lazy"><figcaption>Click <b>Add</b> to save the rule configuration.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/step-7-save-rule-2-ce.webp" alt="After saving, SENTIENT will automatically begin creating, updating, and processing alarms according to the conditions, schedule, and propagation settings you defined." loading="lazy"><figcaption>After saving, SENTIENT will automatically begin creating, updating, and processing alarms according to the conditions, schedule, and propagation settings you defined.</figcaption></figure></div>


<hr>

## Managing alarm rules

After you create an alarm rule, it appears in the table on the **Alarms &#8702; Alarm rules** page.    
Here, you can quickly view the key parameters of each rule — alarm type, target entity, severity levels, and whether a clear condition is configured — and manage the rule using a set of available actions.

Each rule row includes an action panel that lets you copy, export, debug, edit, or delete the configuration.

Each alarm rule includes an action bar for managing it:
1. **Copy alarm rule configuration**. Copies the rule configuration, allowing you to quickly create a new rule based on the existing one.
2. **Export**. Exports the rule as a JSON file for backup or migration to another SENTIENT instance.
3. **Events**. Opens the event log associated with the rule, including triggers, clears, state changes, and errors.
4. **Debug configuration**. Enables debug mode and provides access to detailed execution information for troubleshooting.
5. **Edit**. Opens the rule editor where you can modify any configuration parameters.
6. **Delete**. Removes the alarm rule from the system.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/alarm-rules-parameters-1-ce.webp" alt="Managing Alarm Rules in the Alarm rules list." loading="lazy"><figcaption>Managing Alarm Rules in the Alarm rules list.</figcaption></figure></div>


<br><b><font size="4">View alarm rule details</font></b>

Click an alarm rule to view its detailed information.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/alarm-rules-parameters-2-ce.webp" alt="Click an alarm rule to view its detailed information." loading="lazy"><figcaption>Click an alarm rule to view its detailed information.</figcaption></figure></div>


<br><b><font size="4">Edit the alarm rule</font></b>

To modify the alarm rule, click the rule. The alarm rule details window will open.
Click the **orange pencil** icon to switch to **edit mode**.

After making the required changes, click the **orange checkmark** icon to apply and save the changes.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/alarm-rules-parameters-3-ce.webp" alt="To modify the alarm rule, click the rule. The alarm rule details window will open.Click the orange pencil icon to switch to edit mode." loading="lazy"><figcaption>To modify the alarm rule, click the rule. The alarm rule details window will open.<br>Click the <b>orange pencil</b> icon to switch to <b>edit mode</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/alarm-rules-parameters-4-ce.webp" alt="After making the required changes, click the orange checkmark icon to apply and save the changes." loading="lazy"><figcaption>After making the required changes, click the <b>orange checkmark</b> icon to apply and save the changes.</figcaption></figure></div>


<hr>

## Export / Import alarm rule

You can **export** the alarm rule to a JSON file and **import** it into the same or another SENTIENT instance.

<br><b><font size="4">Export alarm rule</font></b>

- Navigate to **Alarms** page &#8702; **Alarm rules** tab.
- Click the **Export** button located in the corresponding alarm rule row.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/export-alarm-rule-1-ce.webp" alt="Navigate to Alarms page &#8702; Alarm rules tab.Click the Export button located in the row of the specific alarm rule." loading="lazy"><figcaption>Navigate to <b>Alarms</b> page &#8702; <b>Alarm rules</b> tab.<br>Click the <b>Export</b> button located in the row of the specific alarm rule.</figcaption></figure></div>


<br><b><font size="4">Import alarm rule</font></b>

SENTIENT allows you to import previously exported alarm rules in JSON format. This simplifies configuration migration between instances, rapid deployment of standard alarm templates, and restoration from backups.

Steps to import:
- Navigate to **Alarms** page &#8702; **Alarm rules** tab.
- Click the "**+**" button in the upper-right corner and select **Import alarm rule** from the drop-down menu. 
- In the import dialog, drag and drop the JSON file or choose it manually with the alarm rule configuration.
- Click **Import** to upload the configuration.
- In the dialog that opens, specify the entity or profile to which the alarm rule will be applied.
- Click **Add** to save the rule.

After saving, the rule becomes active immediately and SENTIENT starts applying it according to its configured logic.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/import-alarm-rule-1-ce.webp" alt="- Navigate to Alarms page &#8702; Alarm rules tab.- Click the &quot;+&quot; button in the top-right corner, and select Import alarm rule from the dropdown menu." loading="lazy"><figcaption>- Navigate to <b>Alarms</b> page &#8702; <b>Alarm rules</b> tab.<br>- Click the "<b>+</b>" button in the top-right corner, and select <b>Import alarm rule</b> from the dropdown menu.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/import-alarm-rule-2-ce.webp" alt="- In the import dialog, drag and drop the JSON file or choose it manually.- Click Import to upload the configuration." loading="lazy"><figcaption>- In the import dialog, drag and drop the JSON file or choose it manually.<br>- Click <b>Import</b> to upload the configuration.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/import-alarm-rule-3-ce.webp" alt="- Specify the target profile or entity for the imported alarm rule.- Finally, click Add to save the rule." loading="lazy"><figcaption>- Specify the <b>target profile or entity</b> for the imported alarm rule.<br>- Finally, click <b>Add</b> to save the rule.</figcaption></figure></div>


<hr>

## Examples of alarm rule configurations

To better understand how alarm rules work, let&#39;s review several practical examples. Each example demonstrates a specific scenario, condition type, or alarm rule feature that can be used in real-world projects.

In the scenarios below, we will create alarm rules **directly on a device**.


<div class="st-callout info">


**Recommendation:** If the same rule should apply to multiple devices, create it at the **Device Profile** level.   
This ensures centralized alarm logic, reduces duplication, and simplifies ongoing maintenance.


</div>


<b><font size="4">Preparation</font></b>

For the following examples, you need a device named **Thermometer** that sends **temperature** telemetry.
1. Download the CSV file: [thermometer-device-data.csv](/docs/user-guide/resources/alarm-rules/thermometer-device-data.csv)
2. Go to the "Devices" and [import](/docs/user-guide/bulk-provisioning/) the CSV file.

**CSV includes:**
- **Name:** Thermometer
- **Type:** thermostat
- **Time series:** <span class="code-light">temperature</span>

> **Important note about the CSV:** the column type for the <span class="code-light">temperature</span> key must be set to "**Time series**".


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-prepare-device-1-ce.webp" alt="Create a device named Thermometer that sends temperature telemetry." loading="lazy"><figcaption>Create a device named <b>Thermometer</b> that sends temperature telemetry.</figcaption></figure></div>


<hr>

### Example 1. Simple alarm condition: temperature monitoring

**Scenario:**   
A refrigeration chamber is used to store perishable goods.   
The temperature inside must be continuously monitored to prevent product loss and maintain proper storage conditions.

**Goal:**   
Create a **critical alarm** when the temperature exceeds **10°C**.

<hr>

<b><font size="3">Step 1. Create the alarm rule</font></b>

- Open the **Alarms** page from the left-hand menu.
- Go to the **Alarm rules** tab.
- Click the "**+**" button in the top-right corner.
- Select **Create new alarm rule** from the dropdown menu.

<b><font size="3">Step 2. General section</font></b>

In the **General** section, specify:
- **Alarm type:** *High Temperature*
- Select the **Target entity type** - Device 
- Specify the specific **entity** that the rule should apply to - Thermometer

<b><font size="3">Step 3. Add argument</font></b>

- In the **Arguments** section, click **Add argument** and fill in:
  - **Argument name:** temperature
  - **Entity type:** *Current entity*
  - **Argument type:** *Latest telemetry*
  - **Time series key:** <span class="code-light">temperature</span>
- Click **Add** when finished.

This creates a <span class="code-light">temperature</span> variable that you will use in the rule&#39;s logical condition.

<b><font size="3">Step 4. Configure the trigger condition</font></b>

In the **Trigger condition** section, click **Add trigger condition**.

**Step 4.1 Severity**
- **Severity:** *Critical*

**Step 4.2 Condition**

Click "<b>Add condition</b>".   

In the filter configuration window, click **Add argument filter** and specify:
- **Argument:** <span class="code-light">temperature</span>
- **Value type:** *Numeric*
- **Operation:** *greater than* 
- **Value:** 10
- Click **Add**

**Type:** *Simple*
- Click **Save**

As a result, the alarm will be created immediately once the temperature exceeds **10°C**.

<b><font size="3">Step 5. Save the rule</font></b>

Click **Add** to save the rule.

<hr>

<b><font size="4">Result</font></b>

After saving, SENTIENT will automatically create a critical alarm whenever the <span class="code-light">temperature</span> value exceeds **10°C**.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-simple-1-ce.webp" alt="Go to the Alarm rules page under Alarms.Click the &quot;+&quot; button in the top-right corner. Select Create new alarm rule from the dropdown menu." loading="lazy"><figcaption>Go to the <b>Alarm rules</b> page under <b>Alarms</b>.<br>Click the "<b>+</b>" button in the top-right corner. Select <b>Create new alarm rule</b> from the dropdown menu.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-simple-2-ce.webp" alt="In the General section:- Set Alarm type to High temperature.- Select Target entity type: Device.- Specify the target device: Thermometer." loading="lazy"><figcaption>In the <b>General</b> section:<br>- Set <b>Alarm type</b> to <i>High temperature</i>.<br>- Select <b>Target entity type</b>: <i>Device</i>.<br>- Specify the <b>target device</b>: <i>Thermometer</i>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-simple-3-ce.webp" alt="In the Arguments section, add new argument." loading="lazy"><figcaption>In the <b>Arguments</b> section, add new argument.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-simple-4-ce.webp" alt="In the Trigger conditions section, click Add trigger condition." loading="lazy"><figcaption>In the <b>Trigger conditions</b> section, click <b>Add trigger condition</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-simple-5-ce.webp" alt="- Severity: Critical- Click Add condition." loading="lazy"><figcaption>- <b>Severity:</b> Critical<br>- Click <b>Add condition</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-simple-6-ce.webp" alt="Click Add argument filter." loading="lazy"><figcaption>Click <b>Add argument filter</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-simple-7-ce.webp" alt="Argument: temperature; Value type: Numeric; Operation: greater than; Static value: 10." loading="lazy"><figcaption><b>Argument:</b> temperature; <b>Value type:</b> Numeric; <b>Operation:</b> greater than; <b>Static value:</b> 10.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-simple-8-ce.webp" alt="Condition type: Simple. Click Save." loading="lazy"><figcaption><b>Condition type:</b> Simple. Click <b>Save</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-simple-9-ce.webp" alt="Click Add." loading="lazy"><figcaption>Click <b>Add</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-simple-10-ce.webp" alt="As a result, the rule will create a critical alarm as soon as the temperature exceeds 10°C." loading="lazy"><figcaption>As a result, the rule will create a <b>critical</b> alarm as soon as the temperature exceeds <b>10°C</b>.</figcaption></figure></div>


<hr>

### Example 2. Alarm clear condition

*Continuation of the example "[Simple alarm condition: temperature monitoring](#example-1-simple-alarm-condition-temperature-monitoring)"*

**Scenario**   
A refrigerator is used to store perishable products. After the critical **High Temperature** alarm is triggered, it must be cleared automatically once the temperature returns to a safe level.

**Goal**   
Update the existing **High Temperature** rule by adding a clear condition that sets the alarm to **Cleared** when the temperature is **≤ 4°C**.

<hr>

<b><font size="3">Step 1. Open the High Temperature rule</font></b>

- In the side menu, go to **Alarm** &#8702; **Alarm rules**.
- Find the **High Temperature** rule in the list.
- Click the **Edit** icon (pencil) to open the rule editor.

<b><font size="3">Step 2. Configure clear condition</font></b>

Scroll down to the **Clear condition** section:
- Click **Add clear condition**.
- Click "**Add condition**" to open the configuration window.

<b><font size="3">Step 2.1 Add a filter</font></b>

In the configuration window, click **Add argument filter** and specify:
- **Argument:** <span class="code-light">temperature</span>
- **Value type:** *Numeric*
- **Operation:** *less or equal*
- **Value:** 4

This condition defines the moment when the temperature returns to a safe level. Click **Add**

**Type:** *Simple*
- Click **Save**

After this, the alarm will be cleared as soon as the temperature drops to **4°C or below**.

<b><font size="3">Step 3. Save the rule</font></b>

Click **Apply** to save the updated rule.

<hr>

<b><font size="4">Result</font></b>

After saving, SENTIENT will:
- create a **Critical** — **High Temperature** alarm when the temperature exceeds **10°C**
- automatically clear the alarm when the temperature is **≤ 4°C**

This configuration forms a complete alarm lifecycle, keeps the system state accurate, and eliminates the need for manual intervention.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rule-example-clear-condition-1-ce.webp" alt="Go to the High Temperature rule and open it for editing." loading="lazy"><figcaption>Go to the <b>High Temperature</b> rule and open it for editing.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rule-example-clear-condition-2-ce.webp" alt="Scroll down to the Clear condition section. Click Add clear condition." loading="lazy"><figcaption>Scroll down to the <b>Clear condition</b> section. Click <b>Add clear condition</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rule-example-clear-condition-3-ce.webp" alt="Click Add condition." loading="lazy"><figcaption>Click <b>Add condition</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rule-example-clear-condition-4-ce.webp" alt="Click Add argument filter." loading="lazy"><figcaption>Click <b>Add argument filter</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rule-example-clear-condition-5-ce.webp" alt="Argument: temperature; Value type: Numeric; Operation: less or equal; Static value: 4.Click Add." loading="lazy"><figcaption><b>Argument:</b> temperature; <b>Value type:</b> Numeric; <b>Operation:</b> less or equal; <b>Static value:</b> 4.<br>Click <b>Add</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rule-example-clear-condition-6-ce.webp" alt="Click Save." loading="lazy"><figcaption>Click <b>Save</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rule-example-clear-condition-7-ce.webp" alt="Apply changes." loading="lazy"><figcaption>Apply changes.</figcaption></figure></div>


<hr>

### Example 3. Alarm condition with a duration

*Continuation of the example "[Simple alarm condition: temperature monitoring](#example-1-simple-alarm-condition-temperature-monitoring)".*

**Goal:**   
Update the existing **High Temperature** rule so that it triggers only when the temperature exceeds the threshold for a specified duration — for example, **1 minute**.
This mechanism helps avoid false alarms caused by short-term temperature spikes.

<hr>

<b><font size="3">Step 1. Open the High Temperature rule</font></b>

- In the side menu, go to **Alarm** &#8702; **Alarm rules**.
- Find the **High Temperature** rule in the list.
- Click the **Edit** icon (pencil) to open the rule editor.

<b><font size="3">Step 2. Configure trigger condition</font></b>

Scroll down to the **Trigger condition** section and edit the existing condition:
- **Condition type:** change *Simple* &#8702; **Duration**
- **Duration value:** 1
- **Time unit:** *Minutes*
- Click **Save** to apply the updated alarm condition settings.

The alarm will now be triggered only if the temperature exceeds the threshold **continuously for 60 seconds**.

<b><font size="3">Step 3. Save the updated rule</font></b>

Click **Apply** to save the updated rule configuration.

<hr>

<b><font size="4">Result</font></b>

After saving, SENTIENT will:
- create the **High Temperature** alarm only when the temperature exceeds the threshold for **1 full minute**
- ignore short, random temperature spikes
- provide a more stable alarm system with fewer false alerts


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-duration-1-ce.webp" alt="Go to the High Temperature rule and open it for editing." loading="lazy"><figcaption>Go to the <b>High Temperature</b> rule and open it for editing.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-duration-2-ce.webp" alt="Scroll down to the Trigger condition section and edit the existing condition." loading="lazy"><figcaption>Scroll down to the <b>Trigger condition</b> section and edit the existing condition.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-duration-3-ce.webp" alt="Condition type: Duration; Duration value: 1 minute.Click Save." loading="lazy"><figcaption><b>Condition type:</b> Duration; <b>Duration value:</b> 1 minute.<br>Click <b>Save</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-duration-4-ce.webp" alt="Apply changes." loading="lazy"><figcaption>Apply changes.</figcaption></figure></div>


<hr>

### Example 4. Alarm with dynamic duration (based on an attribute value)

*Continuation of the example "[Alarm condition with a duration](#example-3-alarm-condition-with-a-duration)".*

**Scenario**   
You already have a **High Temperature** alarm configured to trigger when the temperature exceeds the threshold for **1 minute**.   
In this example, we extend that logic by making the duration **dynamic** — meaning the duration required to trigger the alarm will be defined by a **server attribute** on the device.

**Goal**   
Update the High Temperature rule so that:
- the alarm is created only when the temperature stays above the critical threshold for the duration specified in the device&#39;s <span class="code-light">highTemperatureDurationThreshold</span> [server attribute](/docs/user-guide/attributes/#server-side-attributes)
- the duration can be changed without editing the alarm rule — simply by updating the device’s attribute value

<hr>

**Preparation**   
Add a **server attribute** to the **Thermometer** device:
- **Key:** <span class="code-light">highTemperatureDurationThreshold</span>
- **Value type** *Integer*
- **Value:** 2


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-with-dynamic-duration-1-ce.webp" alt="Add a highTemperatureDurationThreshold server attribute to the Thermometer device." loading="lazy"><figcaption>Add a <b>highTemperatureDurationThreshold</b> server attribute to the <b>Thermometer</b> device.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-with-dynamic-duration-2-ce.webp" alt="This value will be used by the alarm rule as the duration requirement." loading="lazy"><figcaption>This value will be used by the alarm rule as the duration requirement.</figcaption></figure></div>


This value will be used by the alarm rule as the duration requirement.

<hr>

<b><font size="3">Step 1. Open the High Temperature rule</font></b>

- In the side menu, go to **Alarm** &#8702; **Alarm rules**.
- Find the **High Temperature** rule in the list.
- Click the **Edit** icon (pencil) to open the rule editor.

<b><font size="3">Step 2. Add argument</font></b>

In the **Arguments** section:
- Click **Add argument**
- Fill in the fields:
  - **Entity type:** *Current entity* 
  - **Argument type:** *Attribute*
  - **Attribute scope:** *Server attributes* 
  - **Attribute key:** <span class="code-light">highTemperatureDurationThreshold</span>
  - **Argument name:** highTemperatureDurationThreshold
- Click **Add**

You now have a dynamic variable that can be used in the **Duration** condition.

<b><font size="3">Step 3. Configure trigger condition</font></b>

Scroll to the **Trigger condition** section and edit the existing condition:
- **Condition type:** *Duration* 
- **Value type:** change *Static* to **Dynamic** 
- **Value:** specify the argument <span class="code-light">highTemperatureDurationThreshold</span>
- **Unit:** *Minutes*
- Click **Save** inside the condition block.

From now on, the duration required to trigger the alarm is determined by the device attribute rather than a fixed number.

<b><font size="3">Step 4. Save the rule</font></b>

Click **Apply** to save the updated configuration.

<hr>

<b><font size="4">Result</font></b>

After saving, SENTIENT will:
- create a **High Temperature** alarm if the temperature:
  - exceeds the threshold (e.g., >10°C), **and**
  - remains above it for the period defined in the <span class="code-light">highTemperatureDurationThreshold</span> attribute (e.g., 2 minutes)

This ensures the alarm responds only to **sustained deviations**, not to short-term sensor spikes.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-with-dynamic-duration-3-ce.webp" alt="Go to the High Temperature rule and open it for editing." loading="lazy"><figcaption>Go to the <b>High Temperature</b> rule and open it for editing.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-with-dynamic-duration-4-ce.webp" alt="In the Arguments section, add new argument that will be used in the Duration condition." loading="lazy"><figcaption>In the <b>Arguments</b> section, add new argument that will be used in the <b>Duration</b> condition.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-with-dynamic-duration-5-ce.webp" alt="Scroll down to the Trigger condition section and edit the existing condition." loading="lazy"><figcaption>Scroll down to the <b>Trigger condition</b> section and edit the existing condition.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-with-dynamic-duration-6-ce.webp" alt="Condition type: Duration; Dynamic value: Argument highTemperatureDurationThreshold; Time unit: minutes.Click Save." loading="lazy"><figcaption><b>Condition type:</b> Duration; <b>Dynamic value:</b> <b>Argument</b> highTemperatureDurationThreshold; <b>Time unit:</b> minutes.<br>Click <b>Save</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-with-dynamic-duration-7-ce.webp" alt="Apply changes." loading="lazy"><figcaption>Apply changes.</figcaption></figure></div>


<hr>

### Example 5. Alarm with repeating condition

*Continuation of the example "[Simple alarm condition: temperature monitoring](#example-1-simple-alarm-condition-temperature-monitoring)".*

**Goal:**   
Update the **High Temperature** rule so that the alarm is created only when the threshold condition occurs a specified number of times in a row.
This helps filter out random sensor spikes and react only to repeated or consistent deviations.

<hr>

<b><font size="3">Step 1. Open the High Temperature rule</font></b>

- In the side menu, go to **Alarm** &#8702; **Alarm rules**.
- Find the **High Temperature** rule in the list.
- Click the **Edit** icon (pencil) to open the rule editor.

<b><font size="3">Step 2. Edit the trigger condition</font></b>

Update the existing trigger condition by changing the following parameters:
- **Condition type:** *Repeating*
- **Count of events:** 3   
Click **Save** to apply the changes.

With this configuration, SENTIENT will check whether the threshold condition occurs **three times in a row** before creating the alarm.

<b><font size="3">Step 3. Save the rule</font></b>

Click **Apply** to save the updated configuration.

<hr>

<b><font size="4">Result</font></b>

After saving, SENTIENT behaves as follows:
- create the **High Temperature** alarm only when the condition is met **3 times in a row**
- Single or random temperature spikes will not trigger an alarm


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-repeating-1-ce.webp" alt="Go to the High Temperature rule and open it for editing." loading="lazy"><figcaption>Go to the <b>High Temperature</b> rule and open it for editing.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-repeating-2-ce.webp" alt="Scroll down to the Trigger condition section and edit the existing condition." loading="lazy"><figcaption>Scroll down to the <b>Trigger condition</b> section and edit the existing condition.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-repeating-3-ce.webp" alt="Condition type: &quot;Repeating&quot;. Count of events: 3. Save the condition." loading="lazy"><figcaption>Condition type: "<b>Repeating</b>". <b>Count of events</b>: 3. Save the condition.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-condition-repeating-4-ce.webp" alt="Apply changes." loading="lazy"><figcaption>Apply changes.</figcaption></figure></div>


<hr>

### Example 6. Define alarm rule schedule

*Continuation of the example "[Simple alarm condition: temperature monitoring](#example-1-simple-alarm-condition-temperature-monitoring)".*

**Goal:**   
Update the **High Temperature** rule so that the alarm triggers **only during working hours**.
This is useful when monitoring is required only at certain times—for example, during staff working hours.

<hr>

<b><font size="3">Step 1. Open the High Temperature rule</font></b>

- In the side menu, go to **Alarm** &#8702; **Alarm rules**.
- Find the **High Temperature** rule in the list.
- Click the **Edit** icon (pencil) to open the rule editor.

<b><font size="3">Step 2. Configure the alarm rule schedule</font></b>

Scroll to the **Trigger condition** section and open the **Schedule** settings.
- **Select the schedule type:** *Active at a specific time*
- Configure the working hours:
  - **Timezone:** Europe/Kiev (UTC+02:00)
  - **Days**: Monday, Tuesday, Wednesday, Thursday, Friday
  - **Time range:**
    - **From:** 10:00
    - **To:** 19:00
- Click **Save** to apply the schedule configuration.

With this setup, the rule is active **only on weekdays from 10:00 to 19:00**.
Outside this interval, the system will **not** create a **High Temperature** alarm, even if <span class="code-light">temperature > 10°C</span> is true.

<b><font size="3">Step 3. Save the rule</font></b>

Click **Apply** to save the updated configuration.

<hr>

<b><font size="4">Result</font></b>

After saving, SENTIENT will:
- activate the **High Temperature** rule only on weekdays **from 10:00 to 19:00**
- ignore temperature threshold violations that occur outside this time window


1. Go to the <b>High Temperature</b> rule and open it for editing.

1. Open the schedule settings for the alarm&#39;s trigger condition.

1. Select the schedule type: <i>Active at a specific time</i>.<br>Configure the rule to be active only on weekdays from 10:00 to 19:00. Click <b>Save</b>.

1. Apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-schedule-1-ce.webp" alt="Go to the High Temperature rule and open it for editing." loading="lazy"><figcaption>Go to the <b>High Temperature</b> rule and open it for editing.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-schedule-2-ce.webp" alt="Open the schedule settings for the alarm&#39;s trigger condition." loading="lazy"><figcaption>Open the schedule settings for the alarm&#39;s trigger condition.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-schedule-3-ce.webp" alt="Select the schedule type: Active at a specific time.Configure the rule to be active only on weekdays from 10:00 to 19:00. Click Save." loading="lazy"><figcaption>Select the schedule type: <i>Active at a specific time</i>.<br>Configure the rule to be active only on weekdays from 10:00 to 19:00. Click <b>Save</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-schedule-4-ce.webp" alt="Apply changes." loading="lazy"><figcaption>Apply changes.</figcaption></figure></div>


<hr>

### Example 7. Advanced thresholds

*Continuation of the example "[Simple alarm condition: temperature monitoring](#example-1-simple-alarm-condition-temperature-monitoring)".*

**Goal:**   
Update the **High Temperature** rule by adding the ability to enable or disable the alarm using a server attribute at the device level.

In this example, the alarm should trigger **only when both conditions are true**:
1. <span class="code-light">temperatureAlarmFlag == true</span>
2. <span class="code-light">temperature > 10°C</span>

This allows you to flexibly control whether the alarm should be active for a specific device — **without editing the rule**.

<hr>

**Preparation**   
Add a **server attribute** to the **Thermometer** device:
- **Key:** <span class="code-light">temperatureAlarmFlag</span>
- **Type:** Boolean 
- **Value:** `true`

This attribute determines whether the alarm rule is active for the device.


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-advanced-thresholds-1-ce.webp" alt="Add a temperatureAlarmFlag server attribute to the Thermometer device." loading="lazy"><figcaption>Add a <b>temperatureAlarmFlag</b> <i>server attribute</i> to the <b>Thermometer</b> device.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-advanced-thresholds-2-ce.webp" alt="This attribute determines whether the alarm rule is active for the device." loading="lazy"><figcaption>This attribute determines whether the alarm rule is active for the device.</figcaption></figure></div>


<hr>

<b><font size="3">Step 1. Open the High Temperature alarm rule</font></b>

- In the side menu, go to **Alarm** &#8702; **Alarm rules**.
- Find the **High Temperature** rule in the list.
- Click the **Edit** icon (pencil) to open the rule editor.
- <b><font size="3">Step 2. Add an argument</font></b>

In the **Arguments** section:
- Click **Add argument**
- Fill in the fields:
  - **Entity type:** *Current entity* 
  - **Argument type:** *Attribute*
  - **Attribute scope:** *Server attributes*
  - **Attribute key:** <span class="code-light">temperatureAlarmFlag</span>
  - **Argument name:** temperatureAlarmFlag
- Click **Add**

You now have a boolean variable that can be used in the alarm conditions.

<b><font size="3">Step 3. Configure the trigger condition</font></b>

Scroll to the **Trigger condition** section and edit the existing condition.

Add another condition:
- Click **Add argument filter** and configure:
  - **Argument:** <span class="code-light">temperatureAlarmFlag</span>
  - **Value type:** *Boolean* 
  - **Operation:** *equal* 
  - **Value:** `true`
- Click **Add**.

This filter determines whether the alarm is allowed to trigger for the specific device.

<b><font size="3">Step 4. Save the rule</font></b>

Click **Apply** to save the updated configuration.

<hr>

<b><font size="4">Result</font></b>

After saving, SENTIENT will:
- create the High Temperature alarm only if:
  - <span class="code-light">temperatureAlarmFlag == true</span>, and 
  - the <span class="code-light">temperature</span> exceeds **10°C**
- ignore the rule entirely for this device if temperatureAlarmFlag == false, even when the threshold is exceeded


<div class="st-gallery"><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-advanced-thresholds-3-ce.webp" alt="Go to the High Temperature rule and open it for editing." loading="lazy"><figcaption>Go to the <b>High Temperature</b> rule and open it for editing.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-advanced-thresholds-4-ce.webp" alt="In the Arguments section, add new argument that will be used in the creation condition." loading="lazy"><figcaption>In the <b>Arguments</b> section, add new argument that will be used in the <b>creation</b> condition.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-advanced-thresholds-5-ce.webp" alt="Scroll down to the Trigger condition section and edit the existing condition." loading="lazy"><figcaption>Scroll down to the <b>Trigger condition</b> section and edit the existing condition.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-advanced-thresholds-6-ce.webp" alt="Click Add argument filter." loading="lazy"><figcaption>Click <b>Add argument filter</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-advanced-thresholds-7-ce.webp" alt="Argument: temperatureAlarmFlag; Value type: Boolean; Operation: equal; Static value: True.Click Add." loading="lazy"><figcaption><b>Argument:</b> <i>temperatureAlarmFlag</i>; <b>Value type:</b> <i>Boolean</i>; <b>Operation:</b> <i>equal</i>; <b>Static value:</b> <i>True</i>.<br>Click <b>Add</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-advanced-thresholds-8-ce.webp" alt="Click Save." loading="lazy"><figcaption>Click <b>Save</b>.</figcaption></figure><figure><img src="/images/user-guide/alarm-rules/examples/alarm-rules-example-advanced-thresholds-9-ce.webp" alt="Apply changes." loading="lazy"><figcaption>Apply changes.</figcaption></figure></div>


<hr>

<b><font size="4">Benefits of this approach</font></b>

- You can enable or disable alarms **without editing a rule**
- Each device can have its own alarm activation state 
- Ideal for large projects with varying alerting policies across devices 
- Easy to integrate with dashboards — operators can toggle the alarm using a simple switch

<hr>

## Next steps


<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please [contact us](/docs/contact-us/).
