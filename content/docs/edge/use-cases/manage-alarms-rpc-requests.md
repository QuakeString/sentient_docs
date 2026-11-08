+++
title = "Manage alarms and RPC requests on edge devices"
description = "SENTIENT Edge use case"

[extra]
status = "imported"
checked = ""
source = "docs/edge/use-cases/manage-alarms-rpc-requests.md"
+++
## Use case

Let's assume you have a warehouse with two devices connected to SENTIENT **Edge**: 
* DHT22 temperature sensor
* Air Conditioner 

SENTIENT Edge has the following responsibilities:
 * **Collects temperature readings** from the DHT22 sensor
 * **Creates and updates alarms** if the temperature in the warehouse is higher than 50 °C
 * In case if the temperature becomes critical, SENTIENT Edge turns on the cooler system by **sending RPC call requests** to the Air Conditioner device
 * **Pushes telemetry to the cloud**

Please note that this is just a simple theoretical use case to demonstrate the capabilities of the platform. 
You can use this tutorial as a basis for much more complex scenarios.

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


 


## Configure Alarm Rules

We will use [alarm rules](/docs/user-guide/device-profiles/#alarm-rules) feature to raise alarm when temperature reading is greater than 50 °C degrees.
For this purpose, we should create new device profile and add new alarm rule. We recommend creating dedicated [device profiles](/docs/user-guide/device-profiles/) for each corresponding device type. Let's create new device profile "edge thermostat".


1. Login to your <b>SENTIENT</b> instance and open <b>Device profiles</b> menu page.

1. Click the <b>("+")</b> icon to add new device profile.

1. 1. Input device profile name. For e.g., <b>edge thermostat</b>. 2. Click on the <b>Transport configuration</b> to proceed.

1. For this example we will use default transport configuration. Click on the <b>Alarm rules</b> to proceed.

1. Click on the <b>Add alarm rule</b> button.

1. 1. Specify alarm type. For e.g., <b>High temperature</b>. 2. Click on the <b>("+")</b> icon to add new alarm condition.

1. Click on the <b>Add key filter</b> button.

1. 1. Select key type <b>Time series</b>. 2. Input key name <b>temperature</b>. 3. Select value type <b>Numeric</b>. 4. Click on the <b>Add</b> button.

1. 1. Select operation <b>greater than</b>. 2. Input threshold value <b>50</b>. 3. Click on the <b>Add</b> button.

1. Click on the <b>Save</b> button.

1. Click on the <b>Add</b> button.

1. Newly create device profile will be show first in the list, because default sort order is by created time.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-1.webp" alt="Login to your SENTIENT instance and open Device profiles menu page." loading="lazy"><figcaption>Login to your <b>SENTIENT</b> instance and open <b>Device profiles</b> menu page.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-2.webp" alt="Click the (&quot;+&quot;) icon to add new device profile." loading="lazy"><figcaption>Click the <b>("+")</b> icon to add new device profile.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-3.webp" alt="1. Input device profile name. For e.g., edge thermostat. 2. Click on the Transport configuration to proceed." loading="lazy"><figcaption>1. Input device profile name. For e.g., <b>edge thermostat</b>. 2. Click on the <b>Transport configuration</b> to proceed.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-4.webp" alt="For this example we will use default transport configuration. Click on the Alarm rules to proceed." loading="lazy"><figcaption>For this example we will use default transport configuration. Click on the <b>Alarm rules</b> to proceed.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-5.webp" alt="Click on the Add alarm rule button." loading="lazy"><figcaption>Click on the <b>Add alarm rule</b> button.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-6.webp" alt="1. Specify alarm type. For e.g., High temperature. 2. Click on the (&quot;+&quot;) icon to add new alarm condition." loading="lazy"><figcaption>1. Specify alarm type. For e.g., <b>High temperature</b>. 2. Click on the <b>("+")</b> icon to add new alarm condition.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-7.webp" alt="Click on the Add key filter button." loading="lazy"><figcaption>Click on the <b>Add key filter</b> button.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-8.webp" alt="1. Select key type Time series. 2. Input key name temperature. 3. Select value type Numeric. 4. Click on the Add button." loading="lazy"><figcaption>1. Select key type <b>Time series</b>. 2. Input key name <b>temperature</b>. 3. Select value type <b>Numeric</b>. 4. Click on the <b>Add</b> button.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-9.webp" alt="1. Select operation greater than. 2. Input threshold value 50. 3. Click on the Add button." loading="lazy"><figcaption>1. Select operation <b>greater than</b>. 2. Input threshold value <b>50</b>. 3. Click on the <b>Add</b> button.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-10.webp" alt="Click on the Save button." loading="lazy"><figcaption>Click on the <b>Save</b> button.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-11.webp" alt="Click on the Add button." loading="lazy"><figcaption>Click on the <b>Add</b> button.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-12.webp" alt="Newly create device profile will be show first in the list, because default sort order is by created time." loading="lazy"><figcaption>Newly create device profile will be show first in the list, because default sort order is by created time.</figcaption></figure></div>


Please open SENTIENT **Edge** UI using the URL: **EDGE_URL** to see provisioned device profiles.


1. Login to your SENTIENT <b>Edge</b> instance and open <b>Device profiles</b> menu page.

1. Verify that <b>edge thermostat</b> was provisioned to edge as well.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-13.webp" alt="Login to your SENTIENT Edge instance and open Device profiles menu page." loading="lazy"><figcaption>Login to your SENTIENT <b>Edge</b> instance and open <b>Device profiles</b> menu page.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/configure-rules-item-14.webp" alt="Verify that edge thermostat was provisioned to edge as well." loading="lazy"><figcaption>Verify that <b>edge thermostat</b> was provisioned to edge as well.</figcaption></figure></div>


## Provision devices

For simplicity, we will provision device manually using the UI.

Let's first create **DHT22 temperature sensor** and **Air Conditioner** devices on the edge and add relation between these devices. This relation will be used to find related **Air Conditioner** device once **DHT22 temperature sensor** will send critical temperature value.

We are going to provision device on the Edge. Please open SENTIENT **Edge** UI using the URL: **EDGE_URL**.


1. Login to your SENTIENT <b>Edge</b> instance and open <b>Devices</b> menu page.

1. Click on the <b>("+")</b> icon in the top right corner of the table.

1. 1. Input device name. For e.g., <b>DHT22</b>. 2. Select <b>edge thermostat</b> from device profiles list. No other changes required at this time. 3. Click <b>Add</b> to add the device.

1. Now your <b>DHT22</b> device should be listed first, since table sort devices using created time by default.

1. To add more devices, click on the <b>("+")</b> icon then <b>Add new device</b>.

1. 1. Input device name. For e.g., <b>Air Conditioner</b>. No other changes required at this time. 2. Click on the <b>Add</b> to add the device.

1. Now your <b>Air Conditioner</b> device should be listed first, since table sort devices using created time by default.

1. 1. Click on the <b>DHT22</b>. 2. Click on the <b>Relations</b>. 3. Click on the <b>("+")</b> icon.

1. 1. Specify <b>Manages</b> type. 2. Specify <b>Device</b> type. 3. Select <b>Air Conditioner</b> device. 4. Click on the "Add" button. Now we verify that devices were provisioned to cloud.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-1.webp" alt="Login to your SENTIENT Edge instance and open Devices menu page." loading="lazy"><figcaption>Login to your SENTIENT <b>Edge</b> instance and open <b>Devices</b> menu page.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-2.webp" alt="Click on the (&quot;+&quot;) icon in the top right corner of the table." loading="lazy"><figcaption>Click on the <b>("+")</b> icon in the top right corner of the table.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-3.webp" alt="1. Input device name. For e.g., DHT22. 2. Select edge thermostat from device profiles list. No other changes required at this time. 3. Click Add to add the device." loading="lazy"><figcaption>1. Input device name. For e.g., <b>DHT22</b>. 2. Select <b>edge thermostat</b> from device profiles list. No other changes required at this time. 3. Click <b>Add</b> to add the device.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-4.webp" alt="Now your DHT22 device should be listed first, since table sort devices using created time by default." loading="lazy"><figcaption>Now your <b>DHT22</b> device should be listed first, since table sort devices using created time by default.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-5.webp" alt="To add more devices, click on the (&quot;+&quot;) icon then Add new device." loading="lazy"><figcaption>To add more devices, click on the <b>("+")</b> icon then <b>Add new device</b>.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-6.webp" alt="1. Input device name. For e.g., Air Conditioner. No other changes required at this time. 2. Click on the Add to add the device." loading="lazy"><figcaption>1. Input device name. For e.g., <b>Air Conditioner</b>. No other changes required at this time. 2. Click on the <b>Add</b> to add the device.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-7.webp" alt="Now your Air Conditioner device should be listed first, since table sort devices using created time by default." loading="lazy"><figcaption>Now your <b>Air Conditioner</b> device should be listed first, since table sort devices using created time by default.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-8.webp" alt="1. Click on the DHT22. 2. Click on the Relations. 3. Click on the (&quot;+&quot;) icon." loading="lazy"><figcaption>1. Click on the <b>DHT22</b>. 2. Click on the <b>Relations</b>. 3. Click on the <b>("+")</b> icon.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-9.webp" alt="1. Specify Manages type. 2. Specify Device type. 3. Select Air Conditioner device. 4. Click on the &quot;Add&quot; button. Now we verify that devices were provisioned to cloud." loading="lazy"><figcaption>1. Specify <b>Manages</b> type. 2. Specify <b>Device</b> type. 3. Select <b>Air Conditioner</b> device. 4. Click on the "Add" button. Now we verify that devices were provisioned to cloud.</figcaption></figure></div>


Please open **SENTIENT** using the URL **SERVER_URL**:


1. Login to your <b>SENTIENT</b> instance and open <b>Devices</b> menu page.

1. Make sure that <b>DHT22</b> and <b>Air Conditioner</b> devices are in the devices list.

1. Verify that relation from <b>DHT22</b> to <b>Air Conditioner</b> was provisioned as well.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-10.webp" alt="Login to your SENTIENT instance and open Devices menu page." loading="lazy"><figcaption>Login to your <b>SENTIENT</b> instance and open <b>Devices</b> menu page.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-11.webp" alt="Make sure that DHT22 and Air Conditioner devices are in the devices list." loading="lazy"><figcaption>Make sure that <b>DHT22</b> and <b>Air Conditioner</b> devices are in the devices list.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/provision-devices-item-12.webp" alt="Verify that relation from DHT22 to Air Conditioner was provisioned as well." loading="lazy"><figcaption>Verify that relation from <b>DHT22</b> to <b>Air Conditioner</b> was provisioned as well.</figcaption></figure></div>


## Configure edge rule engine to handle alarms and send RPC calls

We are going to update "Edge Root Rule Chain" that will handle **Alarm Created** events for "DHT22" sensor and will send appropriate commands to the "Air Conditioner" device.
Here is the final configuration of edge root rule chain:


<div class="st-gallery"><figure><img src="/images/edge/use-cases/manage-alarms/root-rule-chain.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


In the next steps we are going to create **Rhai** script language node to create appropriate RPC commands to the **Air Conditioner** device.
JavaScript for script node that will emulate enabling of Air Conditioner:

<figure class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">newMsg</span> <span class="o">=</span> <span class="p">{};</span>
<span class="nx">newMsg</span><span class="p">.</span><span class="nx">method</span> <span class="o">=</span> <span class="dl">"</span><span class="s2">enabled_air_conditioner</span><span class="dl">"</span><span class="p">;</span>
<span class="nx">newMsg</span><span class="p">.</span><span class="nx">params</span> <span class="o">=</span> <span class="p">{</span><span class="dl">"</span><span class="s2">speed</span><span class="dl">"</span><span class="p">:</span> <span class="mf">1.0</span><span class="p">};</span>
<span class="k">return</span> <span class="p">{</span> <span class="na">msg</span><span class="p">:</span> <span class="nx">newMsg</span><span class="p">,</span> <span class="na">metadata</span><span class="p">:</span> <span class="nx">metadata</span><span class="p">,</span> <span class="na">msgType</span><span class="p">:</span> <span class="nx">msgType</span> <span class="p">};</span> </code></pre></figure>

Please use this snippet in the next steps, if required.

Here are the steps to update default edge "Root Rule Chain" to the rule chain above:


1. Login to your <b>SENTIENT</b> instance and open <b>Rule chain templates</b> menu page.

1. Open default <b>Edge Root Rule Chain</b>.

1. Filter node by <b>script</b> word and drag script node (Transformation) to rule chain.

1. Input node name and add <b>Rhai</b> script language code (you can copy and paste it from the snippet above) to create proper <b>enable</b> command for Air Conditioner device. Click <b>Add</b> to proceed.

1. Drag connection from <b>Device Profile Node</b> to newly added <b>enabled</b> script node.

1. Select <b>Alarm Created</b> from the list and click on the <b>Add</b> button.

1. Click on the <b>Apply changes</b> button to save current progress.

1. Filter rule nodes by <b>change</b> word and add <b>change originator</b> node to rule chain.

1. 1. Input <b>Switch to Air Conditioner</b>. 2. Select <b>Related entity</b>. 3. Select <b>Manages</b>. 4. Select <b>Device type</b>. 5. Click on the "Add" button

1. Add <b>Success</b> relations from script node to change originator and <b>Success</b> relation from change originator to <b>RPC Call Request</b> node. Save changes.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-1.webp" alt="Login to your SENTIENT instance and open Rule chain templates menu page." loading="lazy"><figcaption>Login to your <b>SENTIENT</b> instance and open <b>Rule chain templates</b> menu page.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-2.webp" alt="Open default Edge Root Rule Chain." loading="lazy"><figcaption>Open default <b>Edge Root Rule Chain</b>.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-3.webp" alt="Filter node by script word and drag script node (Transformation) to rule chain." loading="lazy"><figcaption>Filter node by <b>script</b> word and drag script node (Transformation) to rule chain.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-4.webp" alt="Input node name and add Rhai script language code (you can copy and paste it from the snippet above) to create proper enable command for Air Conditioner device. Click Add to proceed." loading="lazy"><figcaption>Input node name and add <b>Rhai</b> script language code (you can copy and paste it from the snippet above) to create proper <b>enable</b> command for Air Conditioner device. Click <b>Add</b> to proceed.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-5.webp" alt="Drag connection from Device Profile Node to newly added enabled script node." loading="lazy"><figcaption>Drag connection from <b>Device Profile Node</b> to newly added <b>enabled</b> script node.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-6.webp" alt="Select Alarm Created from the list and click on the Add button." loading="lazy"><figcaption>Select <b>Alarm Created</b> from the list and click on the <b>Add</b> button.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-7.webp" alt="Click on the Apply changes button to save current progress." loading="lazy"><figcaption>Click on the <b>Apply changes</b> button to save current progress.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-8.webp" alt="Filter rule nodes by change word and add change originator node to rule chain." loading="lazy"><figcaption>Filter rule nodes by <b>change</b> word and add <b>change originator</b> node to rule chain.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-9.webp" alt="1. Input Switch to Air Conditioner. 2. Select Related entity. 3. Select Manages. 4. Select Device type. 5. Click on the &quot;Add&quot; button" loading="lazy"><figcaption>1. Input <b>Switch to Air Conditioner</b>. 2. Select <b>Related entity</b>. 3. Select <b>Manages</b>. 4. Select <b>Device type</b>. 5. Click on the "Add" button</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-10.webp" alt="Add Success relations from script node to change originator and Success relation from change originator to RPC Call Request node. Save changes." loading="lazy"><figcaption>Add <b>Success</b> relations from script node to change originator and <b>Success</b> relation from change originator to <b>RPC Call Request</b> node. Save changes.</figcaption></figure></div>


Now let's open SENTIENT **Edge** UI to see updated root rule chain:


1. Login to your SENTIENT <b>Edge</b> instance and open <b>Rule chains</b> menu page.

1. Open <b>Edge Root Rule Chain</b> to verify changes.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-11.webp" alt="Login to your SENTIENT Edge instance and open Rule chains menu page." loading="lazy"><figcaption>Login to your SENTIENT <b>Edge</b> instance and open <b>Rule chains</b> menu page.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/update-root-item-12.webp" alt="Open Edge Root Rule Chain to verify changes." loading="lazy"><figcaption>Open <b>Edge Root Rule Chain</b> to verify changes.</figcaption></figure></div>


## Connect "Air Conditioner" to edge and subscribe for RPC commands

To subscribe to RPC commands from edge for the **Air Conditioner** device you need to get the **Air Conditioner** device credentials first.
SENTIENT supports different device credentials. We recommend to use default auto-generated credentials which is access token for this guide.

Please open SENTIENT **Edge** UI using the URL: **EDGE_URL**.


1. Open <b>Devices</b> menu page in the SENTIENT <b>Edge</b> instance.

1. Click on the <b>Air Conditioner</b> device row in the table to open device details.

1. Click on the <b>Copy access token</b>. Token will be copied to your clipboard. Save it to a safe place.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/manage-alarms/copy-access-token-item-1.webp" alt="Open Devices menu page in the SENTIENT Edge instance." loading="lazy"><figcaption>Open <b>Devices</b> menu page in the SENTIENT <b>Edge</b> instance.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/copy-access-token-item-2.webp" alt="Click on the Air Conditioner device row in the table to open device details." loading="lazy"><figcaption>Click on the <b>Air Conditioner</b> device row in the table to open device details.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/copy-access-token-item-3.webp" alt="Click on the Copy access token. Token will be copied to your clipboard. Save it to a safe place." loading="lazy"><figcaption>Click on the <b>Copy access token</b>. Token will be copied to your clipboard. Save it to a safe place.</figcaption></figure></div>


Now you are ready to subscribe to RPC commands for Air Conditioner device.
We will use simple commands to subscribe to RPC commands over MQTT protocol in this example.

Please download following scripts to your local folder:
- [**mqtt-js.sh**](/docs/edge/use-cases/resources/manage-alarms-rpc-requests/mqtt-js.sh)
- [**cooler.js**](/docs/edge/use-cases/resources/manage-alarms-rpc-requests/cooler.js)


<div class="st-callout info">


We assume that you have Node.js and NPM installed on your local PC.


</div>


Before running the scripts, please modify **mqtt-js.sh** accordingly:

- Replace **YOUR_ACCESS_TOKEN** with **Air Conditioner** device access token copied from the steps above. 
- Replace **YOUR_SENTIENT_EDGE_HOST** with your SENTIENT Edge host. For example, **localhost**.
- Replace **YOUR_SENTIENT_EDGE_MQTT_PORT** with your SENTIENT Edge MQTT port. For example, **11883** or **1883**.

Open the terminal, go to the folder that contains **mqtt-js.sh** and **cooler.js** scripts and make sure it is executable:
```bash
 chmod +x *.sh
```

Install **mqtt** node module to be able to use mqtt package in the **cooler.js** script:
```bash
npm install mqtt --save
```

Then run the following command:
```bash
bash mqtt-js.sh
```

You should see the following screen with your host and device token:

```bash
pc@pc-XPS-15-9550:~/alarm-tutorial$ bash mqtt-js.sh
Connecting to: localhost:1883 using access token: sFqoF18PTyViO8L0qo7c
Cooler is connected!
```


<div class="st-callout info">


Please open a new terminal tab to push temperature telemetry to device and leave this running in the background until end of the guide.

</div>


## Post telemetry to "DHT22" sensor to create alarm

To post temperature telemetry to the **DHT22** sensor you need to get the **DHT22** sensor credentials first.
SENTIENT support different device credentials. We recommend to use default auto-generated credentials which is access token for this guide.

Please open SENTIENT **Edge** UI using the URL: **EDGE_URL**.


1. Open <b>Devices</b> menu page in the SENTIENT <b>Edge</b> instance.

1. Click on the <b>DHT22</b> device row in the table to open device details.

1. Click on the <b>Copy access token</b>. Token will be copied to your clipboard. Save it to a safe place.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/manage-alarms/copy-access-token-item-1.webp" alt="Open Devices menu page in the SENTIENT Edge instance." loading="lazy"><figcaption>Open <b>Devices</b> menu page in the SENTIENT <b>Edge</b> instance.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/copy-access-token-item-4.webp" alt="Click on the DHT22 device row in the table to open device details." loading="lazy"><figcaption>Click on the <b>DHT22</b> device row in the table to open device details.</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/copy-access-token-item-5.webp" alt="Click on the Copy access token. Token will be copied to your clipboard. Save it to a safe place." loading="lazy"><figcaption>Click on the <b>Copy access token</b>. Token will be copied to your clipboard. Save it to a safe place.</figcaption></figure></div>


Now you are ready to publish temperature telemetry data on behalf of your device.
We will use simple commands to publish temperature data over HTTP or MQTT in this example.


<div class="st-tabs">

<div class="st-tab" data-label="HTTPLinux, macOS or Windows">

Install cURL for **Ubuntu**:

```bash
sudo apt-get install curl
```


Install cURL for **macOS**:

```bash
brew install curl
```


Install cURL for **Windows**:

Starting Windows 10 b17063, cURL is available by default. 
More info is available in this MSDB blog [post](https://blogs.msdn.microsoft.com/commandline/2018/01/18/tar-and-curl-come-to-windows/).
If you are using older version of Windows OS, you may find official installation guides [here](https://curl.haxx.se/).

<br>

This command works for Windows, Ubuntu and macOS, assuming the cURL tool is already installed. Replace $HOST_NAME and $ACCESS_TOKEN with corresponding values.

```bash
curl -v -X POST -d "{\"temperature\": 25}" $HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
```


For example, $HOST_NAME reference your local SENTIENT Edge installation, access token is **ABC123**:

```bash
curl -v -X POST -d "{\"temperature\": 25}" http://localhost:8080/api/v1/ABC123/telemetry --header "Content-Type:application/json"
```


<br>


</div>

<div class="st-tab" data-label="MQTTLinux or macOS">

Install mqtt client for **Ubuntu**:

```bash
sudo apt-get install mosquitto-clients
```


Install cURL for **macOS**:

```bash
brew install mosquitto-clients
```


Replace $HOST_NAME, $MQTT_PORT and $ACCESS_TOKEN with corresponding values.

```bash
mosquitto_pub -d -q 1 -h "$HOST_NAME" -p "$MQTT_PORT" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -m {"temperature":25}
```


For example, $HOST_NAME reference your local SENTIENT Edge installation, MQTT port is **1883** and access token is **ABC123**:

```bash
mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "ABC123" -m {"temperature":25}
```


Successful output should look similar to this one:

```
Client mosqpub|xxx sending CONNECT
Client mosqpub|xxx received CONNACK
Client mosqpub|xxx sending PUBLISH (d0, q1, r0, m1, 'v1/devices/me/telemetry', ... (16 bytes))
Client mosqpub|xxx received PUBACK (Mid: 1)
Client mosqpub|xxx sending DISCONNECT
```

**Note:** Since SENTIENT 3.2, you are able to use basic MQTT credentials (combination of client id, user name and password ) 
and customize **topic names** and **payload type** using Device Profile. See more info [here](/docs/user-guide/device-profiles/#mqtt-transport-type).

<br>


</div>

<div class="st-tab" data-label="MQTTWindows">


Install [MQTTBox](https://chrome.google.com/webstore/detail/mqttbox/kaajoficamnjijhkeomgfljpicifbkaf) plugin for [Chrome](https://www.google.com/chrome/). Use the instructions listed below:
 


1. Create new MQTT Client with the properties listed in screenshots below.

1. Populate the topic name and payload. Make sure the payload is a valid JSON document. Click on the <b>Publish</b> button.


<div class="st-gallery"><figure><img src="/images/edge/getting-started/mqtt-windows-item-1.webp" alt="Create new MQTT Client with the properties listed in screenshots below." loading="lazy"><figcaption>Create new MQTT Client with the properties listed in screenshots below.</figcaption></figure><figure><img src="/images/edge/getting-started/mqtt-windows-item-2.webp" alt="Populate the topic name and payload. Make sure the payload is a valid JSON document. Click on the Publish button." loading="lazy"><figcaption>Populate the topic name and payload. Make sure the payload is a valid JSON document. Click on the <b>Publish</b> button.</figcaption></figure></div>


<br>


</div>

<div class="st-tab" data-label="CoAPLinux or macOS">

Install coap-cli. Assuming you have Node.js and NPM installed on your Windows/Linux/MacOS machine, execute the following command:

```bash
npm install coap-cli -g
```


Replace $HOST_NAME, $COAP_PORT and $ACCESS_TOKEN with corresponding values. If $COAP_PORT is not specified, default **5683** used.

```bash
echo -n '{"temperature": 25}' | coap post coap://$HOST_NAME:$COAP_PORT/api/v1/$ACCESS_TOKEN/telemetry
```


For example, $HOST_NAME reference your local SENTIENT Edge installation, coap port is **5683** and access token is **ABC123**:

```bash
echo -n '{"temperature": 25}' | coap post coap://localhost:5683/api/v1/ABC123/telemetry
```


<br>


</div>

</div>


Once you have successfully published the "temperature" readings with value **51**:


<div class="st-tabs">

<div class="st-tab" data-label="HTTPLinux, macOS or Windows">

```bash
curl -v -X POST -d "{\"temperature\": 51}" http://localhost:8080/api/v1/ABC123/telemetry --header "Content-Type:application/json"
```


</div>

<div class="st-tab" data-label="MQTTLinux or macOS">

```bash
mosquitto_pub -d -q 1 -h "localhost" -p "1883" -t "v1/devices/me/telemetry" -u "ABC123" -m {"temperature":51}
```


</div>

<div class="st-tab" data-label="MQTTWindows">

Using MQTTBox please publish temperature telemetry with value **51**.


</div>

<div class="st-tab" data-label="CoAPLinux or macOS">

```bash
echo -n '{"temperature": 51}' | coap post coap://localhost:5683/api/v1/ABC123/telemetry
```


</div>

</div>


You should immediately see alarm in the Device Alarm Tab:


1. Click on the row of the <b>DHT22</b> device in the table to view the device details

1. Navigate to the <b>alarm tab</b>.


<div class="st-gallery"><figure><img src="/images/edge/use-cases/manage-alarms/copy-access-token-item-4.webp" alt="Click on the row of the DHT22 device in the table to view the device details" loading="lazy"><figcaption>Click on the row of the <b>DHT22</b> device in the table to view the device details</figcaption></figure><figure><img src="/images/edge/use-cases/manage-alarms/device-alarm-tab-item-1.webp" alt="Navigate to the alarm tab." loading="lazy"><figcaption>Navigate to the <b>alarm tab</b>.</figcaption></figure></div>


## Verify that RPC request was send to "Air Conditioner" device

Open the terminal where **mqtt-js.sh** script is running. 
You should see similar messages on the screen:

```bash
pc@pc-XPS-15-9550:~/alarm-tutorial$ bash mqtt-js.sh
Connecting to: localhost:1883 using access token: sFqoF18PTyViO8L0qo7c
Cooler is connected!
Received RPC command from edge!
Method: enabled_air_conditioner
Speed params: 1
```

Congratulations! RPC request was successfully sent to **Air Conditioner** device based on the temperature readings from the **DHT22** sensor.

## Next Steps
