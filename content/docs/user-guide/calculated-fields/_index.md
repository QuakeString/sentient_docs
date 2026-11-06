+++
title = "Calculated fields"
description = "Calculated fields"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/calculated-fields/index.md"
+++
<table style="width:auto">
   <thead>
     <tr>
	 <td style="text-align: center"><strong><em>Available since TB Version 4.0.0</em></strong></td>
     </tr>
   </thead>
</table> 


<br>

Calculated fields allow you to transform raw data into actionable insights in real time. 
Think of Calculated Fields as a built-in "logic layer" for your IoT entities. 
Instead of just storing raw data, you can automatically generate high-value metrics as soon as data arrives.

By combining data from **multiple sources** — such as incoming telemetry, existing entity attributes, or even data from related assets — you can execute custom logic the moment your data arrives.
The resulting output is automatically stored as either **time-series data** or **attributes**, ensuring your calculated insights are immediately ready for visualization, reporting, or further automation.
 
To support complex workflows, calculated field execution can be **chained**: the output of one field can automatically trigger the execution of another, allowing you to build sophisticated data processing pipelines step-by-step.

Calculated fields can be applied at two different levels within the system:
- Entity Level: At this level, the calculation is applied to a single, specific entity - [Device](/docs/user-guide/ui/devices/) or [Asset](/docs/user-guide/ui/assets/).
- Profile Level: When a calculated field is defined within a [Device profile](/docs/user-guide/device-profiles/) or [Asset profile](/docs/user-guide/asset-profiles/), the logic is inherited by every entity associated with that profile.

This flexibility allows users to either define unique calculations per entity or apply standardized logic across a group of similar entities, optimizing data processing and management.

In addition to real-time processing, SENTIENT supports calculated field [reprocessing](#data-reprocessing), which allows you to apply the same calculation logic to historical telemetry data and generate missing or updated results for a selected time range.

<hr>

### Creating a calculated field

> The process of creating a calculated field is the same for [Devices](/docs/user-guide/ui/devices/), [Assets](/docs/user-guide/ui/assets/), [Device profiles](/docs/user-guide/device-profiles/), or [Asset profiles](/docs/user-guide/asset-profiles/).

- Open the "Calculated fields" page from the left-hand menu.
- Click the "**+**" button in the top-right corner.
- Select **Create new calculated field** from the dropdown menu.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/create-new-calculated-field-1-ce.webp" alt="Open the **Calculated fields** page from the left-hand menu.Click the &quot;**+**&quot; button in the top-right corner and select **Create new calculated field** from the dropdown menu." loading="lazy"><figcaption>Open the **Calculated fields** page from the left-hand menu.<br>Click the "**+**" button in the top-right corner and select **Create new calculated field** from the dropdown menu.</figcaption></figure></div>


<hr>

## Types

SENTIENT supports several types of calculated fields, each designed for a specific class of tasks:


<ul class="calculated-fields">
    
        <li class="field">
            <a class="field-link" href="/docs/user-guide/calculated-fields/simple-calculated-field">
                <div class="field-img">
                    <img src="/images/user-guide/calculated-fields/icons/simple.svg" alt="Simple icon" width="36" height="36" loading="lazy">
                </div>
                <div class="field-text">
                    <span>Simple</span>
                    <p>Basic arithmetic expressions and standard functions.</p>
                </div>
            </a>
        </li>
    
        <li class="field">
            <a class="field-link" href="/docs/user-guide/calculated-fields/script-calculated-field">
                <div class="field-img">
                    <img src="/images/user-guide/calculated-fields/icons/script.svg" alt="Script icon" width="36" height="36" loading="lazy">
                </div>
                <div class="field-text">
                    <span>Script</span>
                    <p>Complex computations using TBEL, with the ability to return multiple values.</p>
                </div>
            </a>
        </li>
    
        <li class="field">
            <a class="field-link" href="/docs/user-guide/calculated-fields/geofencing-calculated-field">
                <div class="field-img">
                    <img src="/images/user-guide/calculated-fields/icons/geofencing.svg" alt="Geofencing icon" width="36" height="36" loading="lazy">
                </div>
                <div class="field-text">
                    <span>Geofencing</span>
                    <p>Determining an entity&#39;s position relative to geozones, detecting enter/exit events, and generating notifications.</p>
                </div>
            </a>
        </li>
    
        <li class="field">
            <a class="field-link" href="/docs/user-guide/calculated-fields/propagation-calculated-field">
                <div class="field-img">
                    <img src="/images/user-guide/calculated-fields/icons/propagation.svg" alt="Propagation icon" width="36" height="36" loading="lazy">
                </div>
                <div class="field-text">
                    <span>Propagation</span>
                    <p>Propagation or transformation of data to related entities based on the relationship direction and type.</p>
                </div>
            </a>
        </li>
    
        <li class="field">
            <a class="field-link" href="/docs/user-guide/calculated-fields/related-entities-aggregation-calculated-field">
                <div class="field-img">
                    <img src="/images/user-guide/calculated-fields/icons/related.svg" alt="Related entities aggregation icon" width="36" height="36" loading="lazy">
                </div>
                <div class="field-text">
                    <span>Related entities aggregation</span>
                    <p>Aggregating latest data (min, max, avg, sum, count, etc.) from related entities.</p>
                </div>
            </a>
        </li>
    
        <li class="field">
            <a class="field-link" href="/docs/user-guide/calculated-fields/time-series-data-aggregation-calculated-field">
                <div class="field-img">
                    <img src="/images/user-guide/calculated-fields/icons/timeseries.svg" alt="Time series data aggregation icon" width="36" height="36" loading="lazy">
                </div>
                <div class="field-text">
                    <span>Time series data aggregation</span>
                    <p>Aggregating historical data from a current entity.</p>
                </div>
            </a>
        </li>
    
</ul>


<hr>

## Configuration

### General

The "General" section defines the basic configuration of the calculated field:
- **Title** — descriptive name for the calculated field that reflects its purpose.
- **Entity type** - the target entity or entity profile where the calculated field will be applied.
- **Type** - the calculated field [type](#types) that defines the calculation model and available configuration blocks.


  


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/calculated-field-general-1-ce.webp" alt="Enter a descriptive name for the calculated field, select the entity or entity profile to which the calculated field will be applied, and choose calculated field type." loading="lazy"><figcaption>Enter a <b>descriptive name</b> for the calculated field, select the entity or entity profile to which the calculated field will be applied, and choose calculated field <b>type</b>.</figcaption></figure></div>


<hr>

### Arguments

Arguments define which data the calculated field reads and exposes as variables for the calculation logic. Each argument maps to a specific data source (attributes or telemetry) from a selected entity, so it can be referenced in a Simple expression, TBEL script, or other calculated field types.

Click the **Add argument** button and fill in the required fields:

<b><font size="3">Entity type</font></b>   
Define where the data is read from:
- **Current entity** — the same device/asset (device profile/asset profile) to which the calculated field is applied.   
  If the field is created at the **Device profile** or **Asset profile** level, the calculation is performed for each entity associated with that profile.
- Another **Device / Asset** — a specific referenced entity 
- **Customer** — the customer associated with the entity 
- **Current tenant** — the tenant entity 
- **Current owner** — the owner of the current entity 
- **Related entities** (for specific calculated field types) — entities resolved dynamically via relations


  


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/argument-name-1-ce.webp" alt="Click the **Add argument** button (1) and fill in the required fields:Defines the data source (2) that will be used in calculations.Choose the desired argument type (3)." loading="lazy"><figcaption>Click the **Add argument** button (1) and fill in the required fields:<br>Defines the data source (2) that will be used in calculations.<br>Choose the desired argument type (3).</figcaption></figure></div>


<br><b><font size="3">Argument types</font></b>

Calculated fields support the following argument types:


<div class="st-tabs">

<div class="st-tab" data-label="Attribute">

Uses **static** or **semi-static data** stored as entity attributes

**Examples:** model, maxTemperature, safeZone, buildingId

**Configuration:**
- **Argument type**: Attribute
- Choose the scope: **Server**, **Client**, or **Shared**.
- Specify the **attribute key**.
- Set the **argument name** - the variable name used in the script logic.
- Optionally, set **default value** for attribute.


  


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/argument-attribute-1-ce.webp" alt="Select the **attribute** argument type (3), choose the **attribute scope** (4), specify the **attribute key** (5), and set the **argument name** (6). Optionally, define a default value (7). Click **Add** (8) to add the argument." loading="lazy"><figcaption>Select the **attribute** argument type (3), choose the **attribute scope** (4), specify the **attribute key** (5), and set the **argument name** (6). Optionally, define a default value (7). Click **Add** (8) to add the argument.</figcaption></figure></div>


</div>

<div class="st-tab" data-label="Latest telemetry">

Uses the most recent **latest telemetry value** for the specified time series key.

**Examples:** temperature, humidity, latitude, longitude

**Configuration:**
- **Argument type**: Latest telemetry
- Specify the **time series key**.
- Set the **argument name** - the variable name used in the script logic.
- Optionally, set **default value** for time series.


  


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/argument-latest-telemetry-1-ce.webp" alt="Select the **latest telemetry** (3) argument type, specify the **time series key** (4), and set the **argument name** (5). Optionally, define a default value (6). Finally, click **Add** (7)." loading="lazy"><figcaption>Select the **latest telemetry** (3) argument type, specify the **time series key** (4), and set the **argument name** (5). Optionally, define a default value (6). Finally, click **Add** (7).</figcaption></figure></div>


</div>

<div class="st-tab" data-label="Time series rollingfor Script-based calculations and specific aggregation modes">

Uses **historical time series data** over a specified time window for trend analysis.

**Examples:** speed, voltage

**Configuration:**
- **Argument type**: Time series rolling
- Specify the **time series key**.
- Set the **argument name** - the variable name used in the script logic.
- Define the **time window** for data collection, which determines the period over which historical telemetry is gathered for calculations.
- Set the **maximum number of values** to be processed (This setting is configured in the [Tenant profile](/docs/user-guide/tenant-profiles/#api-limits--usage) by the system administrator.)


  


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/argument-time-series-rolling-1-ce.webp" alt="Select the **time series rolling** argument type (3), specify the **time series key** (4), and set the **argument name** (5). Define the **time window for data collection** (6) and the maximum number of values (7) to be processed, then click **Add** (8)." loading="lazy"><figcaption>Select the **time series rolling** argument type (3), specify the **time series key** (4), and set the **argument name** (5). Define the **time window for data collection** (6) and the maximum number of values (7) to be processed, then click **Add** (8).</figcaption></figure></div>


</div>

</div>


### Calculation

Calculated fields support multiple calculation models depending on the selected type. A calculation can be defined as a single expression, a TBEL script, a geospatial zone evaluation, a value propagation to related entities, or an aggregation.

For more details about the capabilities and configuration options, refer to the documentation for the corresponding calculated field [type](#types).

### Output

Regardless of the type, the calculated field produces one or more output values that are then stored as telemetry or attributes and processed according to the configured [output strategy](#output-strategy) (immediately or via Rule Chains).

The result can be stored as:
- [Time series](/docs/user-guide/telemetry/) — the function returns a JSON object or an array of JSON objects **with or without a timestamp** containing the computed value(s).
- [Attribute](/docs/user-guide/attributes/) — the function returns a JSON object **without timestamp information** containing the computed value(s). Attributes can be stored in **Server** or **Shared** scope.


  


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/output-1-ce.webp" alt="Time series: function must return a JSON object or array with or without a timestamp containing the computed value.To finish adding the calculated field, click **Add**." loading="lazy"><figcaption>Time series: function must return a JSON object or array with or without a timestamp containing the computed value.<br>To finish adding the calculated field, click **Add**.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/output-2-ce.webp" alt="Attribute: function must return a JSON object without timestamp information containing the computed value.To finish adding the calculated field, click **Add**." loading="lazy"><figcaption>Attribute: function must return a JSON object without timestamp information containing the computed value.<br>To finish adding the calculated field, click **Add**.</figcaption></figure></div>


<hr>

##### Output strategy

The output strategy defines how the calculated field result is processed. Two strategies are available:
- **Process immediately** (default) — the result is processed and stored right away, without using a Rule Chain.
- **Process via Rule Chains** — the result is passed to a entity&#39;s Default Rule Chain for additional processing logic.


<div class="st-tabs">

<div class="st-tab" data-label="Process right away">

The result is processed right away without using a Rule Chain, ensuring minimal latency and direct handling based on the selected options.

**Options for Time series:**
- **Save to time series** — stores historical values in <span class="code-light">ts_kv</span>.
- **Save to latest values** — updates <span class="code-light">ts_kv_latest</span> if the timestamp is newer.
- **Send to WebSockets** — pushes updates to active WebSocket subscribers (no DB write).
- **Send to Calculated fields** — forwards updates to other calculated fields.   
  This enables building *chains of dependent fields*, where a single event can trigger multiple secondary calculations without using Rule Chains.
- **Custom TTL** — sets a custom storage duration (TTL) for this time series.   
  If disabled, the TTL defined in the **Tenant Profile** is used.

**Options for Attributes:**
- **Save to database** — writes the attribute to persistent storage.
- **Send to WebSockets** — pushes updates to active WebSocket subscribers (without DB write).
- **Send to Calculated fields** — notifies other calculated fields about the attribute change, enabling cascaded calculations.
- **Update attribute only on value change** — updates the attribute only when the value actually changes.
- **Send attributes updates notification** — generates an "Attributes Updated" event and sends it to the Default Rule Chain.

</div>

<div class="st-tab" data-label="Process via Rule Chains">

The result is not stored directly on database. Instead, SENTIENT generates an internal message:
- <span class="code-light">POST_TELEMETRY_REQUEST</span>, or
- <span class="code-light">POST_ATTRIBUTES_REQUEST</span>

and routes it to the entity&#39;s **Default Rule Chain**.

Use this strategy when you need:
- additional processing logic
- filters, scripts, or conversions
- conditional persistence
- enrichment, routing, or forwarding

To store the result, the Rule Chain must include a [save time series](/docs/user-guide/rule-engine-2-0/action-nodes/#save-timeseries-node) or [save attributes](/docs/user-guide/rule-engine-2-0/action-nodes/#save-attributes-node) node.

> This is the classic processing model used before direct processing was introduced.

</div>

</div>


## Debug 

SENTIENT provides built-in tools that help you validate and troubleshoot calculated fields in real time.

<b><font size="3">Enable debug mode</font></b> (_&#42; recommended during development_)

Each calculated field can be switched to Debug mode. When enabled, SENTIENT records execution details for every run, including the input arguments that triggered the execution (e.g. incoming telemetry or attribute updates) and the calculation result or any execution problems (script errors, missing arguments, invalid values).


  


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/calculated-field-enable-debug-1-ce.webp" alt="Enable/manage debug mode when creating a calculated field." loading="lazy"><figcaption>Enable/manage debug mode when creating a calculated field.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/calculated-field-enable-debug-2-ce.webp" alt="Enable/manage debug mode for an existing calculated field." loading="lazy"><figcaption>Enable/manage debug mode for an existing calculated field.</figcaption></figure></div>


<b><font size="3">Debug mode</font></b>

Enabling debug mode allows you to track events, states, and potential errors related to the execution of . This greatly simplifies development and troubleshooting.


<div class="st-callout info">


**Note:** Debug mode can quickly increase disk usage because all debug events are stored in the database.
Starting from **SENTIENT 3.9**, the platform stores the full set of debug events only during the first **15 minutes** after the  is created; afterward, only error events are retained.


</div>


Debug mode settings can be combined or disabled entirely.

<br><b><font size="3">Review debug events</font></b>

Click the **Events** icon in the calculated field row to view recorded debug events

Each event includes:
- **Entity ID** — the ID of the entity where the calculated field was executed (the target entity)
- **Message ID** — unique execution identifier
- **Message type** — indicates which type of internal request triggered the calculated field execution
- **Arguments** — the resolved argument values used during execution, including timestamps where applicable
- **Result** — generated output by the calculated field
- **Error** — execution failure reason (appears if the execution failed)


  


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/calculated-field-review-debug-events-1-ce.webp" alt="Click the **Events** icon in the calculated field row to view recorded debug events" loading="lazy"><figcaption>Click the **Events** icon in the calculated field row to view recorded debug events</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/calculated-field-review-debug-events-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<br><b><font size="4">Testing mode for script-based calculated fields</font></b>

For script-based calculated fields (for example, Script, Propagation (Calculation result mode), SENTIENT provides a **Test script function (TBEL)** mode that helps you validate execution using real input data before applying changes.

This allows you to:
- re-run the calculation using the same input data
- temporarily modify argument data or script logic (_without saving configuration changes_)
- validate output JSON structure and timestamps
- see the exact script execution output
- quickly reproduce errors and fix the logic

**How it works:**

Click **Test with this message** in the event row to run the testing function.
- **Left panel — Script editor**   
  Shows the TBEL calculate(ctx, ...) function used by the calculated field. You can modify the script directly in this window.
- **Top-right panel — Arguments**   
  Displays the list of arguments used in the calculation. You can adjust the argument value, type, and timestamp to simulate different incoming data. 
- **Bottom-right panel — Output** 
  Shows the result returned by the script after execution (or an error message if execution fails).


  


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/calculated-field-debug-test-mode-1-ce.webp" alt="Click **Test with this message** in the event row to run the testing function." loading="lazy"><figcaption>Click **Test with this message** in the event row to run the testing function.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/calculated-field-debug-test-mode-2-ce.webp" alt="**Left panel — Script editor**. Shows the TBEL calculate(ctx, ...) function used by the calculated field. You can modify the script directly in this window.**Top-right panel — Arguments**. Displays the list of arguments used in the calculation. You can adjust the argument value, type, and timestamp to simulate different incoming data.**Bottom-right panel — Output**. Shows the result returned by the script after execution (or an error message if execution fails)." loading="lazy"><figcaption>**Left panel — Script editor**. Shows the TBEL calculate(ctx, ...) function used by the calculated field. You can modify the script directly in this window.<br>**Top-right panel — Arguments**. Displays the list of arguments used in the calculation. You can adjust the argument value, type, and timestamp to simulate different incoming data.<br>**Bottom-right panel — Output**. Shows the result returned by the script after execution (or an error message if execution fails).</figcaption></figure></div>


**Workflow:**
- Update the script and/or the argument values.
- Click Test to execute the function with the provided inputs.
- Review the Output section to confirm the returned JSON structure and values.
- When the result is correct, click Save to keep the changes.
- If needed, apply the changes to the calculated field configuration to activate the updated logic.


  


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/calculated-field-debug-test-mode-3-ce.webp" alt="**1.** Update **script** and/or **argument values**.**2.** Click **Test** to run the function.**3.** Review Output JSON**4.** Click **Save** to apply changes." loading="lazy"><figcaption>**1.** Update **script** and/or **argument values**.<br>**2.** Click **Test** to run the function.<br>**3.** Review Output JSON<br>**4.** Click **Save** to apply changes.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/calculated-field-debug-test-mode-4-ce.webp" alt="**5.** If needed, apply changes to the calculated field configuration." loading="lazy"><figcaption>**5.** If needed, apply changes to the calculated field configuration.</figcaption></figure></div>


<hr>

## Rule Engine integration

Calculated fields are integrated with SENTIENT [Rule Engine](/docs/user-guide/rule-engine-2-0/overview/), the platform&#39;s flexible system for routing and processing messages.
The execution is seamlessly integrated into your data workflow, triggered automatically whenever telemetry or attributes are processed by the following rule nodes:
- [Save Time Series](/docs/user-guide/rule-engine-2-0/nodes/action/save-timeseries): Triggers calculations when new telemetry is persisted.
- [Save Attributes](/docs/user-guide/rule-engine-2-0/nodes/action/save-attributes): Triggers calculations when client, shared, or server-side attributes are updated.
- [Calculated Fields](/docs/user-guide/rule-engine-2-0/nodes/action/calculated-fields): A dedicated node used to manually invoke field evaluations or facilitate complex chaining.

<hr>

## Data reprocessing

<table style="width:auto">
   <thead>
     <tr>
	 <td style="text-align: center"><strong><em>The <b>telemetry data reprocessing</b> feature is available only in <b>SENTIENT Professional Edition</b> and <b>SENTIENT Cloud</b> editions.</em></strong></td>
     </tr>
   </thead>
</table> 

**Calculated field reprocessing** is a mechanism that allows you to apply calculated field logic to historical data.   
This is especially useful when you modify existing calculations or add new fields and want those changes to affect not only new data but also previously collected telemetry.

> **Note:** reprocessing cannot be applied to a calculated field that contains only attribute-based arguments. The Calculated field must include at least one argument based on a time series — either "Latest telemetry" or "Time series rolling" data.

<b><font size="3">Key features</font></b>

- **Recalculation of historical data** — apply updated logic to previously collected telemetry.
- **Flexible time range selection** — choose a specific time period for reprocessing.
- **Store results as telemetry** — processed data is saved in SENTIENT as telemetry, enabling further use in widgets, rules, or analytics.

<b><font size="4">How to configure</font></b>

- Choose the target **Entity** or **Profile**, go to the "**Calculated fields**" tab, and either [create a new calculated field](#creating-a-calculated-field) or select an existing one that needs historical telemetry reprocessing.
- Click the "**Reprocess calculated field**" icon next to the desired field.
- In the pop-up window, define the time interval for which you want to reprocess telemetry data.
- Click "**Reprocess**" — the system will start recalculating and update historical telemetry data according to the latest logic.
- Once the data reprocessing is complete, click **Finish**.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/how-to-configure-reprocessing-1-pe.webp" alt="Choose the target **Entity or Profile**, go to the **Calculated fields** tab, and either create a new calculated field or select an existing one that needs historical telemetry reprocessing.Click the **Reprocess calculated field** icon next to the desired field." loading="lazy"><figcaption>Choose the target **Entity or Profile**, go to the **Calculated fields** tab, and either create a new calculated field or select an existing one that needs historical telemetry reprocessing.<br>Click the **Reprocess calculated field** icon next to the desired field.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/how-to-configure-reprocessing-2-pe.webp" alt="In the pop-up window, define the time interval for which you want to reprocess telemetry data, and click **Reprocess** — the system will start recalculating and update historical telemetry data according to the latest logic." loading="lazy"><figcaption>In the pop-up window, define the time interval for which you want to reprocess telemetry data, and click **Reprocess** — the system will start recalculating and update historical telemetry data according to the latest logic.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/how-to-configure-reprocessing-3-pe.webp" alt="Once the data reprocessing is complete, click **Finish**." loading="lazy"><figcaption>Once the data reprocessing is complete, click **Finish**.</figcaption></figure></div>


<b><font size="4">Example of using the data reprocessing feature</font></b>

Assume that the Smart Device sends temperature and humidity data in real time. Later, you configure a calculated field to compute the dew point.
On the time series widget, you can see that dew point values start appearing only from 13:44:35 — before that moment, the calculation was not performed.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/reprocessing-example-1-pe.webp" alt="On the time series widget, you can see that dew point values start appearing only from 13:44:35 — before that moment, the calculation was not performed." loading="lazy"><figcaption>On the time series widget, you can see that dew point values start appearing only from 13:44:35 — before that moment, the calculation was not performed.</figcaption></figure></div>


To recalculate the dew point for a historical period (before the calculated field was created), follow these steps:


1. Go to the **Calculated fields** tab of the corresponding **Smart Device**. Click the **Reprocess calculated field** icon in the row of the required field.

1. In the dialog window, specify the time interval for recalculation and click **Reprocess**.

1. After the process is completed, click **Finish**.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/reprocessing-example-2-pe.webp" alt="Go to the **Calculated fields** tab of the corresponding **Smart Device**. Click the **Reprocess calculated field** icon in the row of the required field." loading="lazy"><figcaption>Go to the **Calculated fields** tab of the corresponding **Smart Device**. Click the **Reprocess calculated field** icon in the row of the required field.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/reprocessing-example-3-pe.webp" alt="In the dialog window, specify the time interval for recalculation and click **Reprocess**." loading="lazy"><figcaption>In the dialog window, specify the time interval for recalculation and click **Reprocess**.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/reprocessing-example-4-pe.webp" alt="After the process is completed, click **Finish**." loading="lazy"><figcaption>After the process is completed, click **Finish**.</figcaption></figure></div>


As a result, the **dewPoint** values will be generated and stored for the entire selected historical period.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/reprocessing-example-5-pe.webp" alt="As a result, the **dewPoint** values will be generated and stored for the entire selected historical period." loading="lazy"><figcaption>As a result, the **dewPoint** values will be generated and stored for the entire selected historical period.</figcaption></figure></div>


<hr>

<br><b><font size="3">Task manager</font></b>

The Task manager allows you to view the status of tasks, track their progress, see results, and identify any errors that occurred during data processing.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/task-manager-1-pe.webp" alt="The Task manager allows you to view the status of tasks, track their progress, see results, and identify any errors that occurred during data processing." loading="lazy"><figcaption>The Task manager allows you to view the status of tasks, track their progress, see results, and identify any errors that occurred during data processing.</figcaption></figure></div>


<hr>

## Built-in methods for rolling arguments

Time series rolling arguments support built-in functions for calculations. These functions accept an optional `ignoreNaN` boolean parameter.

| Method          | Default Behavior (`ignoreNaN = true`)               | Alternative (`ignoreNaN = false`)           |
|-----------------|-----------------------------------------------------|---------------------------------------------|
| `max()`         | Returns the highest value, ignoring NaN values.     | Returns NaN if any NaN values exist.        |
| `min()`         | Returns the lowest value, ignoring NaN values.      | Returns NaN if any NaN values exist.        |
| `mean(), avg()` | Computes the average value, ignoring NaN values.    | Returns NaN if any NaN values exist.        |
| `std()`         | Calculates the standard deviation, ignoring NaN.    | Returns NaN if any NaN values exist.        |
| `median()`      | Returns the median value, ignoring NaN values.      | Returns NaN if any NaN values exist.        |
| `count()`       | Counts values, ignoring NaN values.                 | Counts all values, including NaN.           |
| `last()`        | Returns the most recent value, skipping NaN values. | Returns the last value, even if it is NaN.  |
| `first()`       | Returns the oldest value, skipping NaN values.      | Returns the first value, even if it is NaN. |
| `sum()`         | Computes the total sum, ignoring NaN values.        | Returns NaN if any NaN values exist.        |

<br><b><font size="4">Assuming the following time series rolling argument</font></b>

```json
{
  "temperature": {
    "timeWindow": {
      "startTs": 1740643762896,
      "endTs": 1740644662896
    },
    "values": [
      { "ts": 1740644350000, "value": 72.32 },
      { "ts": 1740644360000, "value": 72.86 },
      { "ts": 1740644370000, "value": 73.58 },
      { "ts": 1740644380000, "value": "NaN" }
    ]
  }
}
```
<br><b><font size="4">Usage and result</font></b>

```javascript
var avgTemp = temperature.mean(); // Returns 72.92
var tempMax = temperature.max(); // Returns 73.58
var valueCount = temperature.count(); // Returns 3

var avgTempNaN = temperature.mean(false);  // Returns NaN
var tempMaxNaN = temperature.max(false);   // Returns NaN
var valueCountNaN = temperature.count(false); // Returns 4
```

**Where it can be useful**

- **statistical analysis**: computing mean, median, and standard deviation for trend analysis.
- **data filtering**: identifying maximum and minimum values within a time window.
- **quality control**: detecting missing or outlier values with count() and std().
- **energy efficiency monitoring**: summing up power consumption over a period to evaluate energy usage patterns.

<hr>

## Merging time series arguments

Time series rolling arguments can be **merged** to align timestamps across multiple datasets.
The merge function combines two or more rolling arguments by taking all timestamps from all arguments and merging the values based on these timestamps.
If value by timestamp does not exist in an argument, it assigns the previous value from that argument; if no previous value exists, it assigns `NaN`.
The result is a new rolling argument that contains a time window and an array of values corresponding to each argument value by each timestamp.

| Method                       | Description                                                                                                               | Returns                                             |
|:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|
| `merge(other, settings)`     | Merges with another rolling argument. Aligns timestamps and filling missing values with the previous available value.     | Merged object with `timeWindow` and aligned values. |
| `mergeAll(others, settings)` | Merges multiple rolling arguments. Aligns timestamps and filling missing values with the previous available value.        | Merged object with `timeWindow` and aligned values. |

<b><font size="4">Parameters</font></b>

| Parameter            | Description                                                                                                                                                |
|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `other` or `others`  | Another rolling argument or array of rolling arguments to merge with.                                                                                      |
| `settings`(optional) | Configuration object that supports: <br> - `ignoreNaN` - controls whether NaN values should be ignored.<br> - `timeWindow` - defines a custom time window. |

**Assuming the following arguments and their values:**

```json
{
  "humidity": {
    "timeWindow": {
      "startTs": 1741356332086,
      "endTs": 1741357232086
    },
    "values": [{
      "ts": 1741356882759,
      "value": 43
    }, {
      "ts": 1741356918779,
      "value": 46
    }]
  },
  "pressure": {
    "timeWindow": {
      "startTs": 1741356332086,
      "endTs": 1741357232086
    },
    "values": [{
      "ts": 1741357047945,
      "value": 1023
    }, {
      "ts": 1741357056144,
      "value": 1026
    }, {
      "ts": 1741357147391,
      "value": 1025
    }]
  },
  "temperature": {
    "timeWindow": {
      "startTs": 1741356332086,
      "endTs": 1741357232086
    },
    "values": [{
      "ts": 1741356874943,
      "value": 76
    }, {
      "ts": 1741357063689,
      "value": 77
    }]
  }
}
```

**Usage:**

```javascript
var mergedData = temperature.merge(humidity, { ignoreNaN: false });
```

**Output:**

```json
{
  "mergedData": {
    "timeWindow": {
      "startTs": 1741356332086,
      "endTs": 1741357232086
    },
    "values": [{
      "ts": 1741356874943,
      "values": [76.0, "NaN"]
    }, {
      "ts": 1741356882759,
      "values": [76.0, 43.0]
    }, {
      "ts": 1741356918779,
      "values": [76.0, 46.0]
    }, {
      "ts": 1741357063689,
      "values": [77.0, 46.0]
    }]
  }
}
```

**Usage:**

```javascript
var mergedData = temperature.mergeAll([humidity, pressure], { ignoreNaN: true });
```

**Output:**

```json
{
  "mergedData": {
    "timeWindow": {
      "startTs": 1741356332086,
      "endTs": 1741357232086
    },
    "values": [{
      "ts": 1741357047945,
      "values": [76.0, 46.0, 1023.0]
    }, {
      "ts": 1741357056144,
      "values": [76.0, 46.0, 1026.0]
    }, {
      "ts": 1741357063689,
      "values": [77.0, 46.0, 1026.0]
    }, {
      "ts": 1741357147391,
      "values": [77.0, 46.0, 1025.0]
    }]
  }
}
```

**Where it can be useful**

Merging time series arguments is useful in scenarios where multiple sensors provide data streams at different intervals.
By aligning timestamps and filling missing values, merging enables:

- **sensor data synchronization**: aligns readings from different sensors measuring related parameters, such as temperature and humidity.
- **anomaly detection**: merges multiple telemetry sources to identify inconsistencies or deviations in system performance.
- **energy consumption analysis**: combines power usage data from various devices to provide a unified view of energy trends.
- **predictive maintenance**: merges vibration, temperature, and operational status data to predict equipment failures.

<hr>

## Export / Import calculated field

You can **export** the calculated field to a JSON file and **import** it into the same or another SENTIENT instance.

<br><b><font size="4">Export calculated field</font></b>

- Navigate to the **Calculated fields** page.
- Click the **Export** button located in the corresponding calculated field row. 


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/export-calculated-field-1-ce.webp" alt="Navigate to the Calculated fields page and click the Export button located in the row of the specific calculated field." loading="lazy"><figcaption>Navigate to the <b>Calculated fields</b> page and click the <b>Export</b> button located in the row of the specific calculated field.</figcaption></figure></div>


<br><b><font size="4">Import calculated field</font></b>

You can import a calculated field configuration from a JSON configuration file.
This feature is particularly useful when transferring calculated field configurations between entities or profiles, ensuring consistency and reducing manual setup efforts.

Steps to import:


1. Navigate to the **Calculated fields** page. Click the "**+**" icon button, and select **Import calculated field** from the dropdown menu.

1. In the opened window, upload the JSON file with the calculated field configuration and click **Import**.

1. In the dialog that opens, **specify the entity or profile** to which the calculated field will be applied.

1. If there are any problems with arguments, they will be highlighted.

1. Ensure the imported field is correctly applied and update any necessary parameters.

1. Click **Add** to complete the import.

1. You have imported the calculated field configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/import-calculated-field-1-ce.webp" alt="Navigate to the **Calculated fields** page. Click the &quot;**+**&quot; icon button, and select **Import calculated field** from the dropdown menu." loading="lazy"><figcaption>Navigate to the **Calculated fields** page. Click the "**+**" icon button, and select **Import calculated field** from the dropdown menu.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/import-calculated-field-2-ce.webp" alt="In the opened window, upload the JSON file with the calculated field configuration and click **Import**." loading="lazy"><figcaption>In the opened window, upload the JSON file with the calculated field configuration and click **Import**.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/import-calculated-field-3-ce.webp" alt="In the dialog that opens, **specify the entity or profile** to which the calculated field will be applied." loading="lazy"><figcaption>In the dialog that opens, **specify the entity or profile** to which the calculated field will be applied.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/import-calculated-field-4-ce.webp" alt="If there are any problems with arguments, they will be highlighted." loading="lazy"><figcaption>If there are any problems with arguments, they will be highlighted.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/import-calculated-field-5-ce.webp" alt="Ensure the imported field is correctly applied and update any necessary parameters." loading="lazy"><figcaption>Ensure the imported field is correctly applied and update any necessary parameters.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/import-calculated-field-6-ce.webp" alt="Click **Add** to complete the import." loading="lazy"><figcaption>Click **Add** to complete the import.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/import-calculated-field-7-ce.webp" alt="You have imported the calculated field configuration." loading="lazy"><figcaption>You have imported the calculated field configuration.</figcaption></figure></div>


> **Note**: ensure the imported field is correctly applied and update any necessary parameters:
  - if the referenced entity is the current entity, no error occurs. 
  - if a referenced entity does not exist in your tenant, it will be highlighted as an error in the argument where it is used. 
  - if the referenced entity is the current tenant and you import it into another tenant, it will automatically adjust to the new tenant without errors.

<hr>

## Managing calculated fields

Use the "Calculated fields" page to manage all calculated fields from a single place.

Each calculated field includes an action panel for managing the field:

2. **Copy** — duplicate the configuration to quickly create a new calculated field.
3. **Export** — download the configuration as a JSON file for backup or migration.
4. **Events** — view execution events, including state changes and errors.
5. **Debug** — enable debug mode and inspect detailed execution data.
6. **Delete** — remove the calculated field from the system.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/calculated-fields-parameters-1-ce.webp" alt="Each calculated field includes an action panel for managing the field." loading="lazy"><figcaption>Each calculated field includes an action panel for managing the field.</figcaption></figure></div>


<br><b><font size="4">View detailed information of the calculated field</font></b>

Click the calculated field to view its details.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/calculated-fields-parameters-2-ce.webp" alt="Click the calculated field to view its details." loading="lazy"><figcaption>Click the calculated field to view its details.</figcaption></figure></div>


<br><b><font size="4">Modify the calculated field</font></b>

To modify the calculated field, click it to open the details view, then click the orange **pencil** button.   
After making your changes, click the orange **check** button to apply the updates.


<div class="st-gallery"><figure><img src="/images/user-guide/calculated-fields/calculated-fields-parameters-3-ce.webp" alt="To modify the calculated field, click it to open the details view, then click the orange **pencil** button." loading="lazy"><figcaption>To modify the calculated field, click it to open the details view, then click the orange **pencil** button.</figcaption></figure><figure><img src="/images/user-guide/calculated-fields/calculated-fields-parameters-4-ce.webp" alt="After making your changes, click the orange **check** button to apply the updates." loading="lazy"><figcaption>After making your changes, click the orange **check** button to apply the updates.</figcaption></figure></div>


## Calculated fields overview video

Prefer visual learning? Watch this short video for a quick introduction to **Calculated fields** in SENTIENT.   
It covers the core concepts, supported calculation types, and practical examples for processing and transforming data in real time.


<div id="video">  
    <div id="video_wrapper">
        <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/wBUcWMSH4QI" frameborder="0" allowfullscreen></iframe>
    </div>
</div>

<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please [contact us](/docs/contact-us/).
