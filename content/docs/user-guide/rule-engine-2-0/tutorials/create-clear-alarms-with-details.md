+++
title = "Working with Alarm details"
description = "Create and Clear Alarms with details"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/rule-engine-2-0/tutorials/create-clear-alarms-with-details.md"
+++
## Use case

This tutorial is based on the [create & clear alarms](/docs/tutorials/create-clear-alarms/#use-case) tutorial and it's use case.
We will reuse the rule chains from the above-mentioned tutorial and will configure the Alarm Details function in the Create and Clear Alarm nodes.
Let's assume your device is using DHT22 sensor to collect and push temperature readings to SENTIENT.
DHT22 sensor is good for -40 to 80°C temperature readings. We want generate Alarms if temperature is out of good range.

In this tutorial we will configure SENTIENT Rule Engine to:

- Count number of critical temperature updates for each device and save this info in Alarm details.
- Save latest critical temperature value in Alarm details.

## Prerequisites

We assume you have completed the following guides and reviewed the articles listed below:

  * [Getting Started](/docs/getting-started-guides/helloworld/) guide.
  * [Rule Engine Overview](/docs/user-guide/rule-engine-2-0/overview/).
  * [Create & clear alarms](/docs/tutorials/create-clear-alarms/) guide.

## Message flow

In this section, we explain the purpose of each node in this tutorial:

- Node A: [**Create alarm**](/docs/user-guide/rule-engine-2-0/nodes/action/create-alarm/) node.
  - Creates or Updates an  alarm if the published temperature is not at expected time range (filter script node returns True).
- Node B: [**Clear alarm**](/docs/user-guide/rule-engine-2-0/nodes/action/clear-alarm/) node.
  - Clears alarm if it exists in case if the published temperature is in expected time range (script node returns False).
- Node C: [**Rule Chain**](/docs/user-guide/rule-engine-2-0/nodes/flow/rule-chain/) node.
  - Forwards incoming Message to specified Rule Chain **Create & Clear Alarms with details**.

<br>

## Configure Rule Chains

In this tutorial, we only modified **Create & Clear Alarms** rule chain, namely configured Alarm Details function in nodes that was described above in the section [Message flow](/docs/user-guide/rule-engine-2-0/tutorials/create-clear-alarms-with-details/#message-flow)<br> Also, we renamed this Rule Chain to **Create & Clear Alarms with details**.

<br>The following screenshots show how the above Rule Chains should look like:

  - **Create & Clear Alarms with details:**

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/create-clear-alarm-chain.webp)

  - **Root Rule Chain:**

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/root-rule-chain.webp)

<br>

Download the attached json [**file**](/docs/user-guide/rule-engine-2-0/tutorials/resources/create___clear_alarms_with_details.json) for the **Create & Clear Alarms with details:** rule chain.
Create Node **C** as shown on the image above in the root rule chain to forward telemetry to the imported rule chain.
<br>
<br>

The following section shows you how to modify this rule chain, specifically: rule nodes [**A**](/docs/user-guide/rule-engine-2-0/tutorials/create-clear-alarms-with-details/#node-a-create-alarm) and [**B**](/docs/user-guide/rule-engine-2-0/tutorials/create-clear-alarms-with-details/#node-b-clear-alarm).


## Modify **Create & Clear Alarms with details:**

### Modify the required nodes

In this rule chain, you will modify 2 nodes as it will be explained in the following sections:

#### Node A: **Create alarm**

If published temperature **is not in** expected time range (**script** node returns **True**) we want to create an Alarm.
We want to add current **temperature** into Alarm Details field.
Also we want to increment **count** field in Alarm Details if alarm already exist, otherwise set count to 1.
 
For making it we will overwrite **Details** function:

**Details** function:
<figure class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">details</span> <span class="o">=</span> <span class="p">{};</span>
<span class="nx">details</span><span class="p">.</span><span class="nx">temperature</span> <span class="o">=</span> <span class="nx">msg</span><span class="p">.</span><span class="nx">temperature</span><span class="p">;</span>

<span class="k">if</span> <span class="p">(</span><span class="nx">metadata</span><span class="p">.</span><span class="nx">prevAlarmDetails</span><span class="p">)</span> <span class="p">{</span>
    <span class="kd">var</span> <span class="nx">prevDetails</span> <span class="o">=</span> <span class="nx">JSON</span><span class="p">.</span><span class="nx">parse</span><span class="p">(</span><span class="nx">metadata</span><span class="p">.</span><span class="nx">prevAlarmDetails</span><span class="p">);</span>
    <span class="nx">details</span><span class="p">.</span><span class="nx">count</span> <span class="o">=</span> <span class="nx">prevDetails</span><span class="p">.</span><span class="nx">count</span> <span class="o">+</span> <span class="mi">1</span><span class="p">;</span>
<span class="p">}</span> <span class="k">else</span> <span class="p">{</span>
    <span class="nx">details</span><span class="p">.</span><span class="nx">count</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span>
<span class="p">}</span>

<span class="k">return</span> <span class="nx">details</span><span class="p">;</span></code></pre></figure>

**Details** function create required **details** object with initial parameters. Then, in **if** statement, we verify is it a new Alarm or Alarm already exist.
If exist - take previous **count** field and increment it.

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/create-alarm.webp)

If new Alarm was created in **Create Alarm** node it is passed to other nodes via relation **Created** if they exist. 
If Alarm was updated - it is passed to other nodes via relation **Updated** if they exist. 

#### Node B: **Clear Alarm**

If published temperature **is in** expected time range (**script** node returns **False**) we want to clear an existing Alarm.
Also during clearing, we want to add latest **temperature** to the existing Alarm details.

For making it we will overwrite **Details** function:

**Alarm Details** function:
<figure class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">details</span> <span class="o">=</span> <span class="p">{};</span>
<span class="k">if</span> <span class="p">(</span><span class="nx">metadata</span><span class="p">.</span><span class="nx">prevAlarmDetails</span><span class="p">)</span> <span class="p">{</span>
    <span class="nx">details</span> <span class="o">=</span> <span class="nx">JSON</span><span class="p">.</span><span class="nx">parse</span><span class="p">(</span><span class="nx">metadata</span><span class="p">.</span><span class="nx">prevAlarmDetails</span><span class="p">);</span>
<span class="p">}</span>
<span class="nx">details</span><span class="p">.</span><span class="nx">clearedTemperature</span> <span class="o">=</span> <span class="nx">msg</span><span class="p">.</span><span class="nx">temperature</span><span class="p">;</span>

<span class="k">return</span> <span class="nx">details</span><span class="p">;</span></code></pre></figure>

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/clear-alarm.webp)

If **Clear Alarm** node could not find existing Alarm, nothing is changed and original message is passed to other nodes via relation **False** if they exist. 
If Alarm do exist - it is cleared and passed to other nodes via relation **Cleared**.


Chain configuration is finished and we need to **save it**.

## Alarm entity JSON (reference)

The example below shows the JSON structure of a typical (default) created alarm.
```bash
{
  "type": "High Temperature Alarm",
  "originator": {
    "id": "784f394c-42b6-435a-983c-b7beff2784f9",
    "entityType": "DEVICE"
  },
  "originatorName": "SCADA device A1",
  "status": "ACTIVE_UNACK",
  "severity": "CRITICAL",
  "acknowledged": false,
  "cleared": false,
  "assigneeId": {
    "id": "784f394c-42b6-435a-983c-b7beff2784f9",
    "entityType": "USER"
  },
  "createdTime": 1634058704565,
  "startTs": 1634058704565,
  "endTs": 1634111163522,
  "ackTs": 1634115221948,
  "clearTs": 1634114528465,
  "assignTs": 1634115928465,
  "details": {},
  "propagate": true,
  "propagateToOwner": true,
  "propagateToOwnerHierarchy": true,
  "propagateToTenant": true,
  "propagateRelationTypes": [
    "string"
  ],
  "id": {
    "id": "784f394c-42b6-435a-983c-b7beff2784f9",
    "entityType": "ALARM"
  }
}
```


The Alarm Status Filter node filters by status only (Active, Cleared, Acknowledged, etc.). To filter by type or another attribute, use a filter node such as [Script](/docs/user-guide/rule-engine-2-0/nodes/filter/script/) or [Switch](/docs/user-guide/rule-engine-2-0/nodes/filter/switch/) in your rule chain.

## Configure Dashboard 

Download the attached json [**file**](/docs/user-guide/resources/thermostat_dashboard.json) for the dashboard indicated in this tutorial and import it.

- Go to **Dashboards** -> **Add new Dashboard** -> **Import Dashboard** and drop the downloaded json file.

Also you can Create Dashboard from scratch and the following section show you how to do this:

## Creating Dashboard 

We will create Dashboard for all **Thermostat** devices and add Alarm widget on it. Create new Dashboard:

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/add-dashboard.webp)

Press **Edit** dashboard and **add alias** that will be resolved to all devices with type **Thermostat**:

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/add-alias.webp)

Add **Alarm widget** to the Dashboard (Add new widget -> Alarm widget bundle -> Alarms). Select configured alias **entity alarm source**. 
Also, add additional **alarm fields**.

- details.temperature.
- details.count.
- details.clearedTemperature.

And rename label of each field by press **edit** button on the field:

 - From: -> To:
   - details.temperature        -> Event Temperature.
   - details.count              -> Events count.
   - details.clearedTemperature -> Clear Temperature.

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/alarm-widget-config.webp)

## Post telemetry and verify

For posting device telemetry we will use Rest API ([link](/docs/reference/http-api/#telemetry-upload-api)). For this we will need to
copy device access token from then device **Thermostat Home**. 

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/copy-access-token.webp)

***you need to replace $ACCESS_TOKEN with actual device token**

Lets post temperature = 99. Alarm should be created:

<figure class="highlight"><pre><code class="language-bash" data-lang="bash">curl <span class="nt">-v</span> <span class="nt">-X</span> POST <span class="nt">-d</span> <span class="s1">'{"temperature":99}'</span> http://localhost:8080/api/v1/<span class="nv">$ACCESS_TOKEN</span>/telemetry <span class="nt">--header</span> <span class="s2">"Content-Type:application/json"</span></code></pre></figure>

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/alarm-created.webp)

Lets post temperature = 180. Alarm should be updated and count field incremented:

<figure class="highlight"><pre><code class="language-bash" data-lang="bash">curl <span class="nt">-v</span> <span class="nt">-X</span> POST <span class="nt">-d</span> <span class="s1">'{"temperature":180}'</span> http://localhost:8080/api/v1/<span class="nv">$ACCESS_TOKEN</span>/telemetry <span class="nt">--header</span> <span class="s2">"Content-Type:application/json"</span></code></pre></figure>

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/alarm-updated.webp)

Lets post temperature = 30. Alarm should be cleared and cleared temperature should be shown:

<figure class="highlight"><pre><code class="language-bash" data-lang="bash">curl <span class="nt">-v</span> <span class="nt">-X</span> POST <span class="nt">-d</span> <span class="s1">'{"temperature":30}'</span> http://localhost:8080/api/v1/<span class="nv">$ACCESS_TOKEN</span>/telemetry <span class="nt">--header</span> <span class="s2">"Content-Type:application/json"</span></code></pre></figure>

![image](/images/user-guide/rule-engine-2-0/tutorials/alarms/alarm-cleared.webp)

Also, you can see how to:

 - Define an additional logic for alarm processing, for example, sending an email or sending notification to Telegram App.

 Please refer links under the **See Also** section to see how to do this.

<br>

## See Also

 - [Send Email](/docs/tutorials/send-email/) guide.
 - [Notifications and Alarms on your smartphone using Telegram Bot](/docs/user-guide/rule-engine-2-0/tutorials/integration-with-telegram-bot/) guide.

## Next steps
