+++
title = "Particle Integration"
description = "Particle Integration Guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/particle.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

## Overview

Particle is a cloud platform that connects a range of devices via the IoT.  
After integrating Particle with the SENTIENT, you can connect, manage, communicate, process, and visualize data from your devices in the SENTIENT IoT platform.

## Particle Integration Tutorial

In this tutorial, we will use a development board Particle Photon.  
You can use any other Particle device to connect it to Particle and get the data in SENTIENT.  

### Prerequisites

- To get data, we will need an [account in Particle Console](https://console.particle.io/).  
- To send downlinks we will also need a [Particle CLI](https://docs.particle.io/getting-started/developer-tools/cli/) to generate access token.  

### Particle Photon setup

At first, we need to connect device to Particle Console to get any data from it.  
To do this, we need to the following steps from [official guide](https://docs.particle.io/quickstart/photon/#connect-your-photon):
1. **Power On Your Device**:
   Plug the USB cable into your power source. (Your computer works perfectly for this purpose.) Your Particle device does not need your computer to connect to Wi-Fi.  
   You could just as easily power your device with a power brick, a battery shield, or another power source wired to the VIN pin.  
   As soon as it is plugged in, the RGB LED on your device should begin blinking blue.  
   If your device is not blinking blue, **hold** down the **SETUP** button.
2. **Connect your Photon to the Internet using the setup web application**: 
   -  Go to **[setup.particle.io](https://setup.particle.io/)**
   -  Click on **Setup a Photon**
   -  After clicking on NEXT, you should be presented with a file (**photonsetup.html**)
   -  Open the file

After connecting the device, it will become visible on the Particle console. This will allow you to create an integration to receive data on SENTIENT.  

![Devices list](/images/user-guide/integrations/particle/particle-console-device-list.webp)

## SENTIENT Integration Configuration

To receive data from Particle Console, we need to create an integration on SENTIENT and get a URL for Particle Integration.  

### Uplink Converter

Before setting up a **Particle integration**, you need to create an **Uplink Converter**, a script for parsing and transforming the data received by Particle integration to a format that SENTIENT can consume.

To create an **Uplink Converter**, go to the **Data Converters** section and click **Add new data converter** -> **Create new converter**, name it **"Uplink data converter for Particle Integration"** and select type **Uplink**. Use debug mode for now.

<b><font size="3">Debug mode</font></b>

Enabling debug mode allows you to track events, states, and potential errors related to the execution of integrations. This greatly simplifies development and troubleshooting.


<div class="st-callout info">


**Note:** Debug mode can quickly increase disk usage because all debug events are stored in the database.
Starting from **SENTIENT 3.9**, the platform stores the full set of debug events only during the first **15 minutes** after the integrations is created; afterward, only error events are retained.


</div>


Debug mode settings can be combined or disabled entirely.

> One can use either [TBEL](/docs/user-guide/rhai/) (SENTIENT expression language) or JavaScript to develop user defined functions. 
We recommend utilizing [TBEL](/docs/user-guide/rhai/) as it's execution in SENTIENT is much more efficient compared to JS.


<div class="tb-content-toggle" id="particleuplink">
    <div class="panel panel-default">
        <div class="panel-heading">
            
            
            
            
            <a class="content-toggle-button" data-target="#tbel">
                <div class="content-toggle-button-text">
                    TBEL<small>Recommended</small>
                </div>
            </a>
            
            
            
            
            <a class="content-toggle-button" data-target="#js">
                <div class="content-toggle-button-text">
                    JavaScript<small></small>
                </div>
            </a>
            
        </div>
        
        
        
        
        
        <div id="tbel" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


Now copy & paste the following script to the Decoder function section:

```javascript

// Decode an uplink message from a buffer
// payload - array of bytes
// metadata - key/value object

/** Decoder **/

// decode payload to JSON
var data = decodeToJson(payload);
if (data.coreid != "api") {
    var deviceName = data.coreid;
    var deviceType = 'Photon';
    var groupName = 'Particle devices';

    var attributes = {
        integrationName: metadata['integrationName']
    };

    var telemetry = {};

    if (data.data == 'online' || data.data == 'offline') {
        attributes.status = data.data;
    } else {
        telemetry.rawData = data.data;
    }

// Result object with device/asset attributes/telemetry data
    var result = {
// Use deviceName and deviceType or assetName and assetType, but not both.
        deviceName: deviceName,
        deviceType: deviceType,
        groupName: groupName,
        attributes: attributes,
        telemetry: telemetry
    };

    /** Helper functions 'decodeToString' and 'decodeToJson' are already built-in **/

    return result;
}
```


![image](/images/user-guide/integrations/particle/particle-create-uplink-converter-tbel.webp)

                </td></tr></table>
            </div>
        </div>
        
        
        
        
        
        <div id="js" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


Now copy & paste the following script to the Decoder function section:

```javascript
// Decode an uplink message from a buffer
// payload - array of bytes
// metadata - key/value object

/** Decoder **/

// decode payload to JSON
var data = decodeToJson(payload);
if (data.coreid != "api") {
    var deviceName = data.coreid;
    var deviceType = 'Photon';
    var groupName = 'Particle devices';

    var attributes = {
        integrationName: metadata['integrationName']
    };

    var telemetry = {};

    if (data.data == 'online' || data.data == 'offline') {
        attributes.status = data.data;
    } else {
        telemetry.rawData = data.data;
    }

// Result object with device/asset attributes/telemetry data
    var result = {
// Use deviceName and deviceType or assetName and assetType, but not both.
        deviceName: deviceName,
        deviceType: deviceType,
        groupName: groupName,
        attributes: attributes,
        telemetry: telemetry
    };

    /** Helper functions 'decodeToString' and 'decodeToJson' are already built-in **/

    return result;
}
/** Helper functions **/

function decodeToString(payload) {
    return String.fromCharCode.apply(String, payload);
}

function decodeToJson(payload) {
    // covert payload to string.
    var str = decodeToString(payload);

    // parse string to JSON
    var data = JSON.parse(str);
    return data;
}
```


![image](/images/user-guide/integrations/particle/particle-create-uplink-converter-js.webp)

                </td></tr></table>
            </div>
        </div>
        
    </div>
</div>


### Downlink Configuration (Optional)

#### Create downlink converter

The Downlink converter transforms outgoing RPC message, and then the Integration sends it to your device.

Create another converter named **"Downlink data converter for Particle Integration"**, and type **Downlink**. To see events - enable Debug.


<div class="tb-content-toggle" id="particledownlink">
    <div class="panel panel-default">
        <div class="panel-heading">
            
            
            
            
            <a class="content-toggle-button" data-target="#tbel">
                <div class="content-toggle-button-text">
                    TBEL<small>Recommended</small>
                </div>
            </a>
            
            
            
            
            <a class="content-toggle-button" data-target="#js">
                <div class="content-toggle-button-text">
                    JavaScript<small></small>
                </div>
            </a>
            
        </div>
        
        
        
        
        
        <div id="tbel" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


You can use our example of Downlink Converter, or write your own according to your configuration:

```javascript
/** Encoder **/

var command = {};
command["method"] = msg.method;
if (msg.params == "false" || msg.params == "true") {
    command["params"] = Boolean.valueOf(msg.params);
} else {
    command["params"] = msg.params;
}

var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",

    // downlink data
    data: JSON.stringify(command),

    // Optional metadata object presented in key/value format
    metadata: {
            deviceId: metadata.deviceName
    }

};

return result;
```


![image](/images/user-guide/integrations/particle/particle-create-downlink-tbel.webp)

                </td></tr></table>
            </div>
        </div>
        
        
        
        
        
        <div id="js" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


You can use our example of Downlink Converter, or write your own according to your configuration:

```javascript
/** Encoder **/

var command = {};
command["method"] = msg.method;
if (msg.params == "false" || msg.params == "true") {
    command["params"] = Boolean.valueOf(msg.params);
} else {
    command["params"] = msg.params;
}

var result = {

    // downlink data content type: JSON, TEXT or BINARY (base64 format)
    contentType: "JSON",

    // downlink data
    data: JSON.stringify(command),

    // Optional metadata object presented in key/value format
    metadata: {
            deviceId: metadata.deviceName
    }

};

return result;
```


![image](/images/user-guide/integrations/particle/particle-create-downlink-js.webp)

                </td></tr></table>
            </div>
        </div>
        
    </div>
</div>


#### Create access token in Particle CLI

To send message to a device, we will need an access token. To create it, you can use [Particle CLI](https://docs.particle.io/getting-started/developer-tools/cli/).  
To install it, you can use the following command:  
```bash
bash <( curl -sL https://particle.io/install-cli )
```


Then, according to [official documentation](https://docs.particle.io/reference/developer-tools/cli/#particle-login), you will need to login using the following command:  
```bash
particle login
```


![Login](/images/user-guide/integrations/particle/cli-login.webp)

After logging in, you will need to [create an access token](https://docs.particle.io/reference/developer-tools/cli/#particle-token-create).  
You can do this using one of the following commands:  
-  Create token that will never be expired (**Useful for integration**) - 
   ```bash
   particle token create --never-expires
   ```
   
-  Create token with default expiration time (**90 days**) - 
   ```bash
   particle token create
   ```
   
![Login](/images/user-guide/integrations/particle/cli-token-created.webp)

Save created token, we will need it in the next step.  

### Particle Integration Setup


Now, we should create an integration in SENTIENT. To do this, you can follow next steps:  


1. Go to **Integrations** section and click Add new integration button. Name it **Particle Integration**, and select type **Particle**.

1. Now, you can select the recently created **Uplink data Converter for Particle Integration**. Click **Next**.

1. If you added a downlink converter, select it. Click **Next**.

1. If you added a downlink converter and created a token - toggle **Allow downlink** and paste your access token. Click **Add** to create integration.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/particle/tb-create-integration.webp" alt="Go to **Integrations** section and click Add new integration button. Name it **Particle Integration**, and select type **Particle**." loading="lazy"><figcaption>Go to **Integrations** section and click Add new integration button. Name it **Particle Integration**, and select type **Particle**.</figcaption></figure><figure><img src="/images/user-guide/integrations/particle/tb-select-uplink.webp" alt="Now, you can select the recently created **Uplink data Converter for Particle Integration**. Click **Next**." loading="lazy"><figcaption>Now, you can select the recently created **Uplink data Converter for Particle Integration**. Click **Next**.</figcaption></figure><figure><img src="/images/user-guide/integrations/particle/tb-select-downlink.webp" alt="If you added a downlink converter, select it. Click **Next**." loading="lazy"><figcaption>If you added a downlink converter, select it. Click **Next**.</figcaption></figure><figure><img src="/images/user-guide/integrations/particle/tb-create-integration-configuration.webp" alt="If you added a downlink converter and created a token - toggle **Allow downlink** and paste your access token. Click **Add** to create integration." loading="lazy"><figcaption>If you added a downlink converter and created a token - toggle **Allow downlink** and paste your access token. Click **Add** to create integration.</figcaption></figure></div>


### Integration on particle.io

To receive incoming data from Particle cloud, we need to configure an integration on Particle CLI.  
To do this, please follow next steps:  


1. Go to **Integrations** section and click "**Add new integration**" button.

1. Click on the **Webhook**.

1. Fill in all required fields. Then click **Create webhook**.

1. Your integration was created successfully.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/particle/particle-console-integrations-2.webp" alt="Go to **Integrations** section and click &quot;**Add new integration**&quot; button." loading="lazy"><figcaption>Go to **Integrations** section and click "**Add new integration**" button.</figcaption></figure><figure><img src="/images/user-guide/integrations/particle/particle-console-integrations-3.webp" alt="Click on the **Webhook**." loading="lazy"><figcaption>Click on the **Webhook**.</figcaption></figure><figure><img src="/images/user-guide/integrations/particle/particle-console-integrations-4.webp" alt="Fill in all required fields. Then click **Create webhook**." loading="lazy"><figcaption>Fill in all required fields. Then click **Create webhook**.</figcaption></figure><figure><img src="/images/user-guide/integrations/particle/particle-console-integrations-5.webp" alt="Your integration was created successfully." loading="lazy"><figcaption>Your integration was created successfully.</figcaption></figure></div>


### Uplink message

Once integration is created and any message arrives to it - you will be able to see a new device in your **Devices**.

![image](/images/user-guide/integrations/particle/tb-new-device-created.webp)

### Rule Chain configuration

When integration is configured and ready to use, we need to go to **Rule Chains**, choose **"Root Rule Chain"** and create rule node **Integration Downlink**. Input some name here, choose earlier created Particle integration, and tap **Add**.

![image](/images/user-guide/integrations/particle/tb-create-downlink-rule-node.webp)

After these steps, we need to tap on a right grey square of rule node **message type switch** and drag this square to left side of **Integration Downlink**. In pop-up window, add **"RPC Request to Device"** relation and tap "Add".

![image](/images/user-guide/integrations/particle/tb-root-rule-chain.webp)

Click on check mark in bottom right corner of the screen to save the Root Rule Chain.

### Downlink message to device from dashboard

To process command on device, we will use an example app **Web-Connected LED** from [Particle WebIDE](https://build.particle.io/build).  

![Particle WebIDE](/images/user-guide/integrations/particle/particle-webide-example.webp)  

Click on **Use this example** and thunder icon to flash it to the device.  

#### Configure dashboard

Let's return to SENTIENT and configure the dashboard to control device.  
To demonstrate how to send a command to the device, we will use a **Switch Control Widget**. To use it, you can follow next steps:  
- Click on **Edit mode** button to enable edit mode.  
- Open existing or create a new dashboard.  
- Add new alias (Click on **Aliases** button -> **Add alias** -> Put the name for alias and select created device).  
- Add switch control widget (Click on **Add widget** button -> Click on **Control widgets** bundle -> Click on **Switch Control**).  
- Select your entity alias.  
- Open tab **Appearance** -> Change value for field "Retrieve value using method" to **Don't retrieve**.  
- Change "RPC set value method" to **led**.  
- Paste to the convert value function the following code:  
  ```javascript
  return value ? "on" : "off";
  ```
  
- Click on **Add** button to save a widget.  
- Click on save button to save a dashboard.

Now, you can toggle the button and LED on your Photon should change it&#39;s led state.  
If no - check that your device is connected to Particle and connection is stable.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/particle/particle-add-widget-1.webp" alt="Go to the &quot;**Dashboards**&quot; page, create a new dashboard and select &quot;**Switch Control**&quot; widget from the &quot;**Control Widgets**&quot; bundle." loading="lazy"><figcaption>Go to the "**Dashboards**" page, create a new dashboard and select "**Switch Control**" widget from the "**Control Widgets**" bundle.</figcaption></figure><figure><img src="/images/user-guide/integrations/particle/particle-add-widget-2.webp" alt="Add new alias with previously created device. Then navigate to the &quot;**Appearance**&quot; tab." loading="lazy"><figcaption>Add new alias with previously created device. Then navigate to the "**Appearance**" tab.</figcaption></figure><figure><img src="/images/user-guide/integrations/particle/particle-add-widget-3.webp" alt="Change retrieve value to &quot;**Don&#39;t retrieve**&quot; and change &quot;***RPC set value method***&quot; to &quot;**led**&quot;. Then paste the convert value function copied from the documentation. Click &quot;**Add**&quot;, then save dashboard." loading="lazy"><figcaption>Change retrieve value to "**Don&#39;t retrieve**" and change "***RPC set value method***" to "**led**". Then paste the convert value function copied from the documentation. Click "**Add**", then save dashboard.</figcaption></figure><figure><img src="/images/user-guide/integrations/particle/particle-add-widget-5.webp" alt="Now toggle the button and LED on your Photon should change it&#39;s led state." loading="lazy"><figcaption>Now toggle the button and LED on your Photon should change it&#39;s led state.</figcaption></figure></div>


Read more about dashboards [here](/docs/user-guide/dashboards/).

## Next steps
