+++
title = "Integration Syrus 4 IoT Telematics Gateway - Sentient"
description = "Syrus 4 IoT Telematics Gateway integration guide"

[extra]
status = "imported"
checked = ""
source = "docs/samples/syrus/syrus.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only [**Professional Edition**](/products/sentient-pe/) supports **Platform Integrations** feature.<br>
Use [**SENTIENT Cloud**](/installations/choose-region/) or [**install**](/docs/user-guide/install/pe/installation-options/) your own platform instance.


</div>

## Description

Here&#39;s a detailed integration example between Syrus 4G IoT Telematics Gateway with Sentient Platform over MQTT connection.

## Getting Started

[Syrus 4G IoT Telematics Gateway.](https://syrus.pegasusgateway.com/syrdocs/syrus4/getting-started/)

[SENTIENT Cloud](https://sentient.invenia.in/installations/)

## Provisioning the device for Sentient

For simplicity, we will provision device manually using the UI.

### 1. Login to your SENTIENT instance and open Devices page.

![image](/images/samples/syrus/device_page.webp)

Click on the &quot;+&quot; icon in the top right corner of the table and then select &quot;Add new device&quot;.

![image](/images/samples/syrus/add_device.webp)

Input device name. For example, &quot;Syrus&quot;. No other changes are required at this time. Click &quot;Add&quot; to add the device.

![image](/images/samples/syrus/name_device.webp)

Now your device should be listed first, since the table sorts the devices by using created time as default.

![image](/images/samples/syrus/device_details.webp)

### 2. Token creation

To connect the device you need to get the device credentials first. SENTIENT supports different device credentials. We recommend using default auto-generated credentials which is an access token for this guide.

Click on the device row in the table to open device details

![image](/images/samples/syrus/copy_token.webp)

Click &quot;Copy access token&quot;. Token will be copied to your clipboard. Save it to a safe place.

## Syrus 4G IoT Telematics Gateway Configuration

The first step to do is make sure you have the latest version of Apex OS

### 1. Preparing your System

Go to Management Tool (**http://192.168.9.2**) if you&#39;re over USB cable), select System and confirm that you&#39;re up to date

![image](/images/samples/syrus/update_device.webp)

Now go to Applications Manager and Check for updates and make sure you have the latest version of SyrusJS application installed:

![image](/images/samples/syrus/js_latest.webp)

### 2. Create an instance

In application manager pull down the menu of SyrusJS, this will show you all versions installed of the application, select the latest one and Create a New Instance:

![image](/images/samples/syrus/new_instance.webp)

Name your instance and select the &quot;Create Instance&quot; button:

![image](/images/samples/syrus/name_instance.webp)


Now you have your instance created:

![image](/images/samples/syrus/instance_created.webp)

### 3. Creating your configuration files

We need to create two files on any notepad application (notepad++, sublime, vscode, etc), you can name it as you want but the extension must be syrus.conf

![image](/images/samples/syrus/configuration_files.webp)

One file contains the destination data, protocol, output format, MQTT URI, username and topics.

you may define custom MQTT topics in the MQTT transport configuration. See [transport configuration](/docs/user-guide/device-profiles/#transport-configuration)

here is an example:

![image](/images/samples/syrus/example.webp)

Replace [YOUR\_TOKEN] with the copied access token you got from Sentient when you created the device.

More information about: [https://syrus.pegasusgateway.com/syrdocs/syrus4/syruslang/#destinations](https://syrus.pegasusgateway.com/syrdocs/syrus4/syruslang/#destinations)

The second file contains all the events that will be sent to the Sentient over MQTT, here is an example, this will send Ignition On/Off events and track points every minute:

<figure class="highlight"><pre><code class="language-bash" data-lang="bash">_####### <span class="c">###### ####### ###### #######_
</span>

_############ START MQTT EVENT <span class="c">###########_
</span>

define variable constant_1 1

define fieldset sentient
<span class="nv">fields</span><span class="o">=</span><span class="s2">"ident"</span>:<span class="nv">$modem</span>.imei,position.context.lat:<span class="nv">$gnss</span>.latitude,position.context.lng:<span class="nv">$gnss</span>.longitude,
position.value:<span class="nv">$variables</span>.constant_1,<span class="s2">"position.direction"</span>:<span class="nv">$gnss</span>.heading,<span class="s2">"position.hdop"</span>:<span class="nv">$gnss</span>.hdop,
<span class="s2">"position.pdop"</span>:<span class="nv">$gnss</span>.pdop,<span class="s2">"position.vdop"</span>:<span class="nv">$gnss</span>.vdop,<span class="s2">"position.speed"</span>:<span class="nv">$gnss</span>.mph,
<span class="s2">"position.altitude"</span>:<span class="nv">$gnss</span>.altitude,<span class="s2">"event.enum"</span>:code,<span class="s2">"can.engine.rpm"</span>:<span class="nv">$ecu</span>.rpm,
<span class="s2">"can.throttle.pedal.level"</span>:<span class="nv">$ecu</span>.accel_pedal_position,<span class="s2">"can.engine.temperature"</span>:<span class="nv">$ecu</span>.coolant_temp,
<span class="s2">"can.fuel.consumed"</span>:<span class="nv">$ecu</span>.fuel_total,<span class="s2">"can.intake.map"</span>:<span class="nv">$ecu</span>.intake_manif_pressure,
<span class="s2">"can.vehicle.speed"</span>:<span class="nv">$ecu</span>.fe6c_7-8,<span class="s2">"can.fuel.temperature"</span>:<span class="nv">$ecu</span>.fuel_temp,<span class="s2">"can.engine.load"</span>:<span class="nv">$ecu</span>.engine_load,
<span class="s2">"can.engine.torque"</span>:<span class="nv">$ecu</span>.actual_engine_torque,<span class="s2">"can.catalyst.outlet.temp"</span>:<span class="nv">$ecu</span>.aftmt_catalyst_outlet_gas_temp
<span class="s2">"can.fuel.rate"</span>:<span class="nv">$ecu</span>.fuel_rate,<span class="s2">"can.engine.hours"</span>:<span class="nv">$ecu</span>.hours_total,<span class="s2">"can.ambient.temp"</span>:<span class="nv">$ecu</span>.ambient_air_temp,
<span class="s2">"can.oil.pressure"</span>:<span class="nv">$ecu</span>.oil_pressure

define group sentient

<span class="nb">set </span>destinations <span class="nv">group</span><span class="o">=</span>sentient sentient

define tracking_resolution sentient_tracking 5m 25deg 1000mts

define signal ignitionON <span class="nv">min_duration</span><span class="o">=</span>5s <span class="nv">$io</span>.ign <span class="o">==</span> <span class="nb">true
</span>define signal ignitionOFF <span class="nv">min_duration</span><span class="o">=</span>5s <span class="nv">$io</span>.ign <span class="o">==</span> <span class="nb">false

</span>define event ignitionONmqtt <span class="nv">group</span><span class="o">=</span>sentient <span class="nv">fieldset</span><span class="o">=</span>sentient <span class="nv">ack</span><span class="o">=</span><span class="nb">seq </span><span class="nv">label</span><span class="o">=</span>ignonmqtt <span class="nv">code</span><span class="o">=</span>102 <span class="nv">trigger</span><span class="o">=</span>ignitionON
define event ignitionOFFmqtt <span class="nv">group</span><span class="o">=</span>sentient <span class="nv">fieldset</span><span class="o">=</span>sentient <span class="nv">ack</span><span class="o">=</span><span class="nb">seq </span><span class="nv">label</span><span class="o">=</span>ignoffmqtt <span class="nv">code</span><span class="o">=</span>103 <span class="nv">trigger</span><span class="o">=</span>ignitionOFF
 
_# Define tracking event, a single tracking resolution signal that can be controlled by different actions

define event trackingOffMqtt <span class="nv">group</span><span class="o">=</span>sentient <span class="nv">fieldset</span><span class="o">=</span>sentient <span class="nv">ack</span><span class="o">=</span><span class="nb">seq </span><span class="nv">label</span><span class="o">=</span>prdtst <span class="nv">code</span><span class="o">=</span>100 <span class="nv">trigger</span><span class="o">=</span>@tracking_resolution.sentient_tracking.signal,ignitionOFF,and
define event trackingOnMqtt <span class="nv">group</span><span class="o">=</span>sentient <span class="nv">fieldset</span><span class="o">=</span>sentient <span class="nv">ack</span><span class="o">=</span><span class="nb">seq </span><span class="nv">label</span><span class="o">=</span>trckpnt <span class="nv">code</span><span class="o">=</span>101 <span class="nv">trigger</span><span class="o">=</span>@tracking_resolution.sentient_tracking.time,ignitionON,and
define event trackingHeadingMqtt <span class="nv">group</span><span class="o">=</span>sentient <span class="nv">fieldset</span><span class="o">=</span>sentient <span class="nv">ack</span><span class="o">=</span><span class="nb">seq </span><span class="nv">label</span><span class="o">=</span>heading <span class="nv">code</span><span class="o">=</span>140 <span class="nv">trigger</span><span class="o">=</span>@tracking_resolution.sentient_tracking.heading,ignitionON,and
define event trackingDistanceMqtt <span class="nv">group</span><span class="o">=</span>sentient <span class="nv">fieldset</span><span class="o">=</span>sentient <span class="nv">ack</span><span class="o">=</span><span class="nb">seq </span><span class="nv">label</span><span class="o">=</span>distance <span class="nv">code</span><span class="o">=</span>141 <span class="nv">trigger</span><span class="o">=</span>@tracking_resolution.sentient_tracking.distance,ignitionON,and


_############ END MQTT EVENT <span class="c">###########_
</span>

_####### <span class="c">###### ####### ###### #######_
</span>

define event trackingOnMqtt <span class="nv">group</span><span class="o">=</span>mqtt <span class="nv">fieldset</span><span class="o">=</span>mqtt <span class="nv">ack</span><span class="o">=</span><span class="nb">seq </span><span class="nv">label</span><span class="o">=</span>trckpnt <span class="nv">code</span><span class="o">=</span>101 <span class="nv">trigger</span><span class="o">=</span>@tracking_resolution.mqtt_tracking.time,ignitionON,and
define event trackingHeadingMqtt <span class="nv">group</span><span class="o">=</span>mqtt <span class="nv">fieldset</span><span class="o">=</span>mqtt <span class="nv">ack</span><span class="o">=</span><span class="nb">seq </span><span class="nv">label</span><span class="o">=</span>heading <span class="nv">code</span><span class="o">=</span>140 <span class="nv">trigger</span><span class="o">=</span>@tracking_resolution.mqtt_tracking.heading,ignitionON,and
define event trackingDistanceMqtt <span class="nv">group</span><span class="o">=</span>mqtt <span class="nv">fieldset</span><span class="o">=</span>mqtt <span class="nv">ack</span><span class="o">=</span><span class="nb">seq </span><span class="nv">label</span><span class="o">=</span>distance <span class="nv">code</span><span class="o">=</span>141 <span class="nv">trigger</span><span class="o">=</span>@tracking_resolution.mqtt_tracking.distance,ignitionON,and
_############ END MQTT EVENT <span class="c">###########
</span>
_####### <span class="c">###### ####### ###### #######</span></code></pre></figure>

If you need more information about how to configure more events please refer to SyrusLang documentation:

[https://syrus.pegasusgateway.com/syrdocs/syrus4/syruslang](https://syrus.pegasusgateway.com/syrdocs/syrus4/syruslang)

### 4. Upload your configuration files

Select your created instance:

![image](/images/samples/syrus/select_instance.webp)

Go to Data Folder Tab:

![image](/images/samples/syrus/data_tab.webp)

Select Upload File:

![image](/images/samples/syrus/upload_file.webp)

And search in your local disk the previous configurations files created, and upload it one by one

![image](/images/samples/syrus/upload_config.webp)

Go to Configuration tab, pull down in Configuration and Destination File, select you previously updated items and click Save button: 

![image](/images/samples/syrus/select_configuration.webp)

### 5. Start your instance

Finally, go back to the Information tab and click the Start button:

![image](/images/samples/syrus/information_tab.webp)

## Check your data in Sentient demo account

The reported variables are automatically created according to the fieldset configuration.

Go to Devices, choose Syrus 4 and click &quot;Latest telemetry&quot;

![image](/images/samples/syrus/latest_telemetry.webp)

Now you can use Sentient&#39;s tools to design your own dashboard with Syrus 4G data:

![image](/images/samples/syrus/dashboard.webp)
