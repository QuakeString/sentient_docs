+++
title = "Data filtering and traffic reduce"
description = "SENTIENT Edge use case"

[extra]
status = "imported"
checked = ""
source = "docs/edge/use-cases/data-filtering-traffic-reduce.md"
+++
## Use case

This use case demonstrates how to configure an "in-vehicle IoT monitoring system" connected to SENTIENT **Edge** platform. 

The goal is to collect data from various sensors, process it locally on the **Edge**, and selectively push relevant data (e.g., mileage readings) to the cloud. This setup ensures efficient tracking of the remaining mileage until the next oil change.

To achieve this, we will configure the "Edge Root Rule Chain" to process sensor readings locally on the SENTIENT **Edge** platform. This setup will handle inputs from all 10 sensors and use a rule node to filter and forward only the distance readings (mileage) to the cloud.

The "in-vehicle monitoring system" includes 10 sensors:
* Distance
* Gas consumption
* Vehicle speed
* Engine temperature
* Ambient temperature
* Tire temperature
* Pressure in each tire (4x)

SENTIENT **Edge** has the following responsibilities:
* Collecting readings from all 10 sensors
* Sending only "distance" readings to the cloud

Please note that this is just a simple theoretical use case to demonstrate the capabilities of the platform. You can use this tutorial as a basis for much more complex scenarios.

## Prerequisites

We assume you have completed the following guides and reviewed the articles listed below:


* [Getting Started](/docs/getting-started-guides/helloworld/) guide.
* [Rule Engine Overview](/docs/user-guide/rule-engine-2-0/overview/) article.
* [SENTIENT Edge Getting Started](/docs/edge/getting-started/) article.
* [Edge Rule Chain Templates](/docs/edge/rule-engine/rule-chain-templates/) guide.

Please make sure that you have **SENTIENT** server up and running. Additionally, SENTIENT **Edge** must be up, running and connected to the cloud.

If you have these prerequisites in place let's go to next steps.

In other case please visit this link to provision, install and connect Edge to Server [guide](/docs/user-guide/install/edge/installation-options/).


<div class="st-callout info">


For simplicity we are going to refer to server UI URL as **SERVER_URL** despite if you installed SENTIENT server on-previse or using cloud host version.
Edge UI URL respectively as **EDGE_URL** below in tutorial.


</div>


<div class="st-callout info">


If the Edge **HTTP bind port** was changed to **18080** during Edge installation, access the **SENTIENT Edge** instance at [http://localhost:18080](http://localhost:18080).


</div>


 


## Create device

To begin, let's create a new device named "In-vehicle monitoring system" on the **Edge**.

Please open SENTIENT **Edge** UI using the URL **EDGE_URL**.


1. Log in to your SENTIENT <b>Edge</b> instance and navigate to the "Devices" page.

1. Click on the ("+") icon located in the top right corner. Then, click "Add new device" button.

1. Enter the Name of the input device, for example, "In-vehicle monitoring system", then click "Add" button.

1. Now, your device named "In-vehicle monitoring system" should appear in the devices table.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/data-filtering/provision-devices-item-1.webp" alt="Log in to your SENTIENT Edge instance and navigate to the &quot;Devices&quot; page." loading="lazy"><figcaption>Log in to your SENTIENT <b>Edge</b> instance and navigate to the "Devices" page.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/provision-devices-item-2.webp" alt="Click on the (&quot;+&quot;) icon located in the top right corner. Then, click &quot;Add new device&quot; button." loading="lazy"><figcaption>Click on the ("+") icon located in the top right corner. Then, click "Add new device" button.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/provision-devices-item-3.webp" alt="Enter the Name of the input device, for example, &quot;In-vehicle monitoring system&quot;, then click &quot;Add&quot; button." loading="lazy"><figcaption>Enter the Name of the input device, for example, "In-vehicle monitoring system", then click "Add" button.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/provision-devices-item-4.webp" alt="Now, your device named &quot;In-vehicle monitoring system&quot; should appear in the devices table." loading="lazy"><figcaption>Now, your device named "In-vehicle monitoring system" should appear in the devices table.</figcaption></figure></div>


Please open **SENTIENT** using the URL **SERVER_URL**:


1. Log in to your SENTIENT server instance and navigate to the "Devices" page.

1. Please verify that the device "In-vehicle monitoring system" is listed in the devices list.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/data-filtering/provision-devices-item-5.webp" alt="Log in to your SENTIENT server instance and navigate to the &quot;Devices&quot; page." loading="lazy"><figcaption>Log in to your SENTIENT server instance and navigate to the "Devices" page.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/provision-devices-item-6.webp" alt="Please verify that the device &quot;In-vehicle monitoring system&quot; is listed in the devices list." loading="lazy"><figcaption>Please verify that the device "In-vehicle monitoring system" is listed in the devices list.</figcaption></figure></div>


## Configure edge rule engine to push filtered data to the cloud

We will update “Edge Root Rule Chain” that will be saving on the edge 10 sensor readings. In the rule chain we add rule node that transforms incoming messages and pushes to the cloud message only with distance readings. Here is the final configuration of the edge root rule chain:


<div class="st-gallery"><figure><img src="/images/edge/use-cases/data-filtering/root-rule-chain.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


In the next steps, we will create a [Rhai](https://sentient.invenia.in/docs/user-guide/rhai/) node to filter data. The [Rhai](https://sentient.invenia.in/docs/user-guide/rhai/) script language node will create an empty object *newMsg*, 
add a property named “distance” with the corresponding value from the “In-vehicle monitoring system”, and then send the *newMsg* object as a new message.

<figure class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">newMsg</span> <span class="o">=</span> <span class="p">{};</span>
<span class="nx">newMsg</span><span class="p">.</span><span class="nx">distance</span> <span class="o">=</span> <span class="nx">msg</span><span class="p">.</span><span class="nx">distance</span><span class="p">;</span>
<span class="k">return</span> <span class="p">{</span> <span class="na">msg</span><span class="p">:</span> <span class="nx">newMsg</span><span class="p">,</span> <span class="na">metadata</span><span class="p">:</span> <span class="nx">metadata</span><span class="p">,</span> <span class="na">msgType</span><span class="p">:</span> <span class="nx">msgType</span> <span class="p">};</span> </code></pre></figure>

Here are the steps to update the default Edge "Root Rule Chain" with the provided rule chain:


1. Log in to your SENTIENT instance. Open the "Rule chain templates" page. Navigate to "Edge management" and select "Rule chain templates". Finally, click on "Edge Root Rule Chain".

1. Use the filter to search for nodes containing the word "script". Drag the Script node (Transformation) to the rule chain.

1. Input the node name, e.g., "Transform Incoming Message" and add the JavaScript code (please copy and paste it from the snippet above) to send further only "distance" readings.

1. Delete the connection between the "save timeseries" and "push to cloud" nodes. Select the connection path, then click on the ("X") icon to delete it.

1. Drag a connection from the "save timeseries" to the transformation script node.

1. Choose "Success" from the dropdown list, and click the "Add" button.

1. Drag a connection from "Transform Incoming Message" to the "push to cloud" node.

1. Choose "Success" from the dropdown list, and click the "Add" button.

1. Click "Apply Changes" to save your progress.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-1.webp" alt="Log in to your SENTIENT instance. Open the &quot;Rule chain templates&quot; page. Navigate to &quot;Edge management&quot; and select &quot;Rule chain templates&quot;. Finally, click on &quot;Edge Root Rule Chain&quot;." loading="lazy"><figcaption>Log in to your SENTIENT instance. Open the "Rule chain templates" page. Navigate to "Edge management" and select "Rule chain templates". Finally, click on "Edge Root Rule Chain".</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-2.webp" alt="Use the filter to search for nodes containing the word &quot;script&quot;. Drag the Script node (Transformation) to the rule chain." loading="lazy"><figcaption>Use the filter to search for nodes containing the word "script". Drag the Script node (Transformation) to the rule chain.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-3.webp" alt="Input the node name, e.g., &quot;Transform Incoming Message&quot; and add the JavaScript code (please copy and paste it from the snippet above) to send further only &quot;distance&quot; readings." loading="lazy"><figcaption>Input the node name, e.g., "Transform Incoming Message" and add the JavaScript code (please copy and paste it from the snippet above) to send further only "distance" readings.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-4.webp" alt="Delete the connection between the &quot;save timeseries&quot; and &quot;push to cloud&quot; nodes. Select the connection path, then click on the (&quot;X&quot;) icon to delete it." loading="lazy"><figcaption>Delete the connection between the "save timeseries" and "push to cloud" nodes. Select the connection path, then click on the ("X") icon to delete it.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-5.webp" alt="Drag a connection from the &quot;save timeseries&quot; to the transformation script node." loading="lazy"><figcaption>Drag a connection from the "save timeseries" to the transformation script node.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-6.webp" alt="Choose &quot;Success&quot; from the dropdown list, and click the &quot;Add&quot; button." loading="lazy"><figcaption>Choose "Success" from the dropdown list, and click the "Add" button.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-8.webp" alt="Drag a connection from &quot;Transform Incoming Message&quot; to the &quot;push to cloud&quot; node." loading="lazy"><figcaption>Drag a connection from "Transform Incoming Message" to the "push to cloud" node.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-9.webp" alt="Choose &quot;Success&quot; from the dropdown list, and click the &quot;Add&quot; button." loading="lazy"><figcaption>Choose "Success" from the dropdown list, and click the "Add" button.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-10.webp" alt="Click &quot;Apply Changes&quot; to save your progress." loading="lazy"><figcaption>Click "Apply Changes" to save your progress.</figcaption></figure></div>


Now let's open SENTIENT **Edge** UI to see updated Root Rule Chain:


1. Log in to your SENTIENT <b>Edge</b> instance and navigate to the "Rule chains" page.

1. Open the "Edge Root Rule Chain" to verify the changes.

1. You should see the same configuration of rule chain nodes as on the cloud.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-11.webp" alt="Log in to your SENTIENT Edge instance and navigate to the &quot;Rule chains&quot; page." loading="lazy"><figcaption>Log in to your SENTIENT <b>Edge</b> instance and navigate to the "Rule chains" page.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-12.webp" alt="Open the &quot;Edge Root Rule Chain&quot; to verify the changes." loading="lazy"><figcaption>Open the "Edge Root Rule Chain" to verify the changes.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/update-root-item-13.webp" alt="You should see the same configuration of rule chain nodes as on the cloud." loading="lazy"><figcaption>You should see the same configuration of rule chain nodes as on the cloud.</figcaption></figure></div>


## Connect device to edge and post telemetry

To connect "In-vehicle monitoring system" to the SENTIENT **Edge** you need to get device credentials first.
SENTIENT supports different device credentials. We recommend to use default auto-generated credentials which is access token for this guide.

Please open SENTIENT **Edge** UI using the URL: **EDGE_URL**.


1. Open Devices page in the SENTIENT <b>Edge</b> instance.

1. Click on the "In-vehicle monitoring system" device row in the table to open device details.

1. Click on the "Copy access token" button. The token will be copied to your clipboard.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/data-filtering/copy-access-token-item-1.webp" alt="Open Devices page in the SENTIENT Edge instance." loading="lazy"><figcaption>Open Devices page in the SENTIENT <b>Edge</b> instance.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/copy-access-token-item-2.webp" alt="Click on the &quot;In-vehicle monitoring system&quot; device row in the table to open device details." loading="lazy"><figcaption>Click on the "In-vehicle monitoring system" device row in the table to open device details.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/copy-access-token-item-3.webp" alt="Click on the &quot;Copy access token&quot; button. The token will be copied to your clipboard." loading="lazy"><figcaption>Click on the "Copy access token" button. The token will be copied to your clipboard.</figcaption></figure></div>


We will use simple commands to generate random telemetry for the device "In-vehicle monitoring system" and publish to the SENTIENT **Edge** by the MQTT protocol.

Please download following script to your local folder:
- [**mqtt-generator.py**](/docs/edge/use-cases/resources/data-filtering-traffic-reduce/mqtt-generator.py)

Before running the scripts, please modify **mqtt-generator.py** as follows:

- Replace **YOUR_ACCESS_TOKEN** with the access token of the **"In-vehicle monitoring system"** device copied from the previous steps.
- Replace **YOUR_SENTIENT_EDGE_HOST** with your SENTIENT Edge host address. For example, **localhost**.
- Replace **YOUR_SENTIENT_EDGE_MQTT_PORT** with your SENTIENT Edge MQTT port number. For example, **11883** or **1883**.

Open the terminal and install the MQTT Python library using the following command:

```bash
sudo pip install paho-mqtt
```
Navigate to the directory containing your Python script and launch the application with the following command:

```bash
python mqtt-generator.py
```
Open the SENTIENT **Edge** UI and verify that the device successfully receives telemetry:


1. Navigate to the "Devices" page.

1. Click on the "In-vehicle monitoring system" device row in the table to open the device details.

1. Click on the "Copy Access Token" button. The token will be copied to your clipboard.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/data-filtering/verify-device-telemetry-item-1.webp" alt="Navigate to the &quot;Devices&quot; page." loading="lazy"><figcaption>Navigate to the "Devices" page.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/verify-device-telemetry-item-2.webp" alt="Click on the &quot;In-vehicle monitoring system&quot; device row in the table to open the device details." loading="lazy"><figcaption>Click on the "In-vehicle monitoring system" device row in the table to open the device details.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/verify-device-telemetry-item-3.webp" alt="Click on the &quot;Copy Access Token&quot; button. The token will be copied to your clipboard." loading="lazy"><figcaption>Click on the "Copy Access Token" button. The token will be copied to your clipboard.</figcaption></figure></div>


Open **SENTIENT** UI and verify that edge successfully pushes data to the cloud:


1. Log in in to your <b>SENTIENT</b> instance and open "Devices" page.

1. Click on the row labeled "In-vehicle monitoring system" in the table to view its details.

1. Click on the "Latest telemetry" tab to confirm that distance readings are successfully being pushed from the edge to the cloud.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/data-filtering/verify-device-telemetry-item-4.webp" alt="Log in in to your SENTIENT instance and open &quot;Devices&quot; page." loading="lazy"><figcaption>Log in in to your <b>SENTIENT</b> instance and open "Devices" page.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/verify-device-telemetry-item-5.webp" alt="Click on the row labeled &quot;In-vehicle monitoring system&quot; in the table to view its details." loading="lazy"><figcaption>Click on the row labeled "In-vehicle monitoring system" in the table to view its details.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/verify-device-telemetry-item-6.webp" alt="Click on the &quot;Latest telemetry&quot; tab to confirm that distance readings are successfully being pushed from the edge to the cloud." loading="lazy"><figcaption>Click on the "Latest telemetry" tab to confirm that distance readings are successfully being pushed from the edge to the cloud.</figcaption></figure></div>


## Create dashboard

In the following steps, we will create a dashboard that displays both the total miles traveled and the remaining miles until the next oil change for the vehicle.

Please open **SENTIENT** to create a new dashboard:


1. Log in to your <b>SENTIENT</b> instance. Navigate to the "Dashboards" page.

1. Click on the ("+") "Add" icon and select "Create new dashboard".

1. Enter a title for the new dashboard, e.g., "Edge Vehicle". Click on the "Add" button to create the dashboard.

1. Click on the "Edge Vehicle" dashboard in the table to start editing it.

1. Click on the "Entity aliases" icon located in the toolbar at the top right to open the "Entity aliases" menu.

1. Click on the "Add alias" button.

1. Enter "edge device" into the Alias name field. For the Filter type, select "Single entity". In the Type field, choose "Device". Then, in the Device field, select "In-vehicle monitoring system". Finally, click the "Save" button.

1. Click on the "Add Widget" button.

1. Click on the "Widgets Bundle" and find "Digital gauges". Click on it to open the widget list group.

1. Select the widget from the list that matches the image provided in the guide, then click on it to start adding a data source.

1. In the "Type" dropdown menu, select "Entity". In the "Entity Alias" dropdown menu, select "edge device". In the "Data Key" field, select "distance". Then click the "Add" button to apply changes.

1. Click on the "Edit Widget" icon in the upper right corner of the widget to add style.

1. Select the "Appearance" tab to customize your dashboard widget.

1. Set max value to "10000".

1. Input the unit title as "MLS". Click the "Add" button to apply changes.

1. Dashboard widget successfully created.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-1.webp" alt="Log in to your SENTIENT instance. Navigate to the &quot;Dashboards&quot; page." loading="lazy"><figcaption>Log in to your <b>SENTIENT</b> instance. Navigate to the "Dashboards" page.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-2.webp" alt="Click on the (&quot;+&quot;) &quot;Add&quot; icon and select &quot;Create new dashboard&quot;." loading="lazy"><figcaption>Click on the ("+") "Add" icon and select "Create new dashboard".</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-3.webp" alt="Enter a title for the new dashboard, e.g., &quot;Edge Vehicle&quot;. Click on the &quot;Add&quot; button to create the dashboard." loading="lazy"><figcaption>Enter a title for the new dashboard, e.g., "Edge Vehicle". Click on the "Add" button to create the dashboard.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-4.webp" alt="Click on the &quot;Edge Vehicle&quot; dashboard in the table to start editing it." loading="lazy"><figcaption>Click on the "Edge Vehicle" dashboard in the table to start editing it.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-5.webp" alt="Click on the &quot;Entity aliases&quot; icon located in the toolbar at the top right to open the &quot;Entity aliases&quot; menu." loading="lazy"><figcaption>Click on the "Entity aliases" icon located in the toolbar at the top right to open the "Entity aliases" menu.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-6.webp" alt="Click on the &quot;Add alias&quot; button." loading="lazy"><figcaption>Click on the "Add alias" button.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-7.webp" alt="Enter &quot;edge device&quot; into the Alias name field. For the Filter type, select &quot;Single entity&quot;. In the Type field, choose &quot;Device&quot;. Then, in the Device field, select &quot;In-vehicle monitoring system&quot;. Finally, click the &quot;Save&quot; button." loading="lazy"><figcaption>Enter "edge device" into the Alias name field. For the Filter type, select "Single entity". In the Type field, choose "Device". Then, in the Device field, select "In-vehicle monitoring system". Finally, click the "Save" button.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-8.webp" alt="Click on the &quot;Add Widget&quot; button." loading="lazy"><figcaption>Click on the "Add Widget" button.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-9.webp" alt="Click on the &quot;Widgets Bundle&quot; and find &quot;Digital gauges&quot;. Click on it to open the widget list group." loading="lazy"><figcaption>Click on the "Widgets Bundle" and find "Digital gauges". Click on it to open the widget list group.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-10.webp" alt="Select the widget from the list that matches the image provided in the guide, then click on it to start adding a data source." loading="lazy"><figcaption>Select the widget from the list that matches the image provided in the guide, then click on it to start adding a data source.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-11.webp" alt="In the &quot;Type&quot; dropdown menu, select &quot;Entity&quot;. In the &quot;Entity Alias&quot; dropdown menu, select &quot;edge device&quot;. In the &quot;Data Key&quot; field, select &quot;distance&quot;. Then click the &quot;Add&quot; button to apply changes." loading="lazy"><figcaption>In the "Type" dropdown menu, select "Entity". In the "Entity Alias" dropdown menu, select "edge device". In the "Data Key" field, select "distance". Then click the "Add" button to apply changes.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-12.webp" alt="Click on the &quot;Edit Widget&quot; icon in the upper right corner of the widget to add style." loading="lazy"><figcaption>Click on the "Edit Widget" icon in the upper right corner of the widget to add style.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-13.webp" alt="Select the &quot;Appearance&quot; tab to customize your dashboard widget." loading="lazy"><figcaption>Select the "Appearance" tab to customize your dashboard widget.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-14.webp" alt="Set max value to &quot;10000&quot;." loading="lazy"><figcaption>Set max value to "10000".</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-15.webp" alt="Input the unit title as &quot;MLS&quot;. Click the &quot;Add&quot; button to apply changes." loading="lazy"><figcaption>Input the unit title as "MLS". Click the "Add" button to apply changes.</figcaption></figure><figure><img src="/images/edge/use-cases/data-filtering/configure-dashboards-item-16.webp" alt="Dashboard widget successfully created." loading="lazy"><figcaption>Dashboard widget successfully created.</figcaption></figure></div>


**Congratulations!** You have successfully sent telemetry from the device, saved it on the edge, pushed filtered data to the cloud, and visualized it on the dashboard.

## Next Steps
