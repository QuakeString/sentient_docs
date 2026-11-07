+++
title = "KPN Things Integration"
description = "KPN Things integration guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/kpn-things.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

## Overview

KPN Things is an IoT (Internet of Things) platform provided by KPN, a telecommunications company.  
This platform allows users to connect and manage their IoT devices, facilitating communication and data exchange between these devices and the cloud.  
After integrating KPN Things with the SENTIENT, you can connect, manage, communicate, process and visualize data from your devices in the SENTIENT IoT platform.

<object width="100%" style="max-width: max-content;" data="/images/user-guide/integrations/http-integration.svg"></object>

## Create integration

Follow the steps below to add the KPN Things integration:


1. Go to "Integrations center" section -> "Integrations" page and click "plus" button to create new integration. Select type "KPN Things". Click "Next";

1. At this step, choose "Create new" uplink converter. The new converter will contain necessary code to convert incoming data and click "Next";

1. At the step of adding a downlink converter, you can also select a previously created or create a new downlink converter. But for now, leave the "Downlink data converter" field empty. Click "Skip";

1. Specify your base URL. Please note down "HTTP endpoint URL" we will use this value later. Then, click the "Add" button. KPN Things integration is created.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/kpn/kpn-add-integration-1-pe.webp" alt="Go to &quot;Integrations center&quot; section -> &quot;Integrations&quot; page and click &quot;plus&quot; button to create new integration. Select type &quot;KPN Things&quot;. Click &quot;Next&quot;;" loading="lazy"><figcaption>Go to "Integrations center" section -> "Integrations" page and click "plus" button to create new integration. Select type "KPN Things". Click "Next";</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-add-integration-2-pe.webp" alt="At this step, choose &quot;Create new&quot; uplink converter. The new converter will contain necessary code to convert incoming data and click &quot;Next&quot;;" loading="lazy"><figcaption>At this step, choose "Create new" uplink converter. The new converter will contain necessary code to convert incoming data and click "Next";</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-add-integration-3-pe.webp" alt="At the step of adding a downlink converter, you can also select a previously created or create a new downlink converter. But for now, leave the &quot;Downlink data converter&quot; field empty. Click &quot;Skip&quot;;" loading="lazy"><figcaption>At the step of adding a downlink converter, you can also select a previously created or create a new downlink converter. But for now, leave the "Downlink data converter" field empty. Click "Skip";</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-add-integration-4-pe.webp" alt="Specify your base URL. Please note down &quot;HTTP endpoint URL&quot; we will use this value later. Then, click the &quot;Add&quot; button. KPN Things integration is created." loading="lazy"><figcaption>Specify your base URL. Please note down "HTTP endpoint URL" we will use this value later. Then, click the "Add" button. KPN Things integration is created.</figcaption></figure></div>


We have pre-configured integration on SENTIENT, but we need to configure KPN Things to send data to SENTIENT.

## Configure KPN Things

To configure KPN Things, you need to open [KPN Things Portal](https://portal.kpnthings.com/) and log in to your account.

*The KPN Things Portal interface may change in the future.*

**Add new device**:

- Go to the "Things manager" tab, and click on the "Add new device";
- Choose the "Device Simulator", set a name for your device, and click on the "Add device" button;
- Install and open the "KPN Things Device simulator" app on your phone. Follow the instructions on your phone to scan this QR code. Then, click on the "Add Network Info" button;
- KPN Internet Network is created. Now, click on the "Finish" button;
 


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-1-pe.webp" alt="Go to the &quot;Things manager&quot; tab, and click on the &quot;Add new device&quot;;" loading="lazy"><figcaption>Go to the "Things manager" tab, and click on the "Add new device";</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-2-pe.webp" alt="Choose the &quot;Device Simulator&quot;, set a name for your device, and click on the &quot;Add device&quot; button;" loading="lazy"><figcaption>Choose the "Device Simulator", set a name for your device, and click on the "Add device" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-3-pe.webp" alt="Install and open the &quot;KPN Things Device simulator&quot; app on your phone. Follow the instructions on your phone to scan this QR code. Then, click on the &quot;Add Network Info&quot; button;" loading="lazy"><figcaption>Install and open the "KPN Things Device simulator" app on your phone. Follow the instructions on your phone to scan this QR code. Then, click on the "Add Network Info" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-4-pe.webp" alt="KPN Internet Network is created. Now, click on the &quot;Finish&quot; button." loading="lazy"><figcaption>KPN Internet Network is created. Now, click on the "Finish" button.</figcaption></figure></div>


**Link the device to the "Flow":**

- Go to the "Flows" in left menu and click on the "My first flow" row;
- Click on the "Link Device" button in the "Devices" row;
- Click on the "Link" button next to the device you created earlier;
- The device has been successfully linked to the "Flow". Now, click on the "My Device" row;


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-5-pe.webp" alt="Go to the &quot;Flows&quot; in left menu and click on the &quot;My first flow&quot; row;" loading="lazy"><figcaption>Go to the "Flows" in left menu and click on the "My first flow" row;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-6-pe.webp" alt="Click on the &quot;Link Device&quot; button in the &quot;Devices&quot; row;" loading="lazy"><figcaption>Click on the "Link Device" button in the "Devices" row;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-7-pe.webp" alt="Click on the &quot;Link&quot; button next to the device you created earlier;" loading="lazy"><figcaption>Click on the "Link" button next to the device you created earlier;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-8-pe.webp" alt="The device has been successfully linked to the Flow." loading="lazy"><figcaption>The device has been successfully linked to the Flow.</figcaption></figure></div>


**Data processing setup for my flow:**

- A "Device & Connectivity detail" page will open. Now, go to the "Flows" tab, and click on "My first flow" row;
- Click on the "Data Processing" row to open "Data Processing details" page;
- Change the switch to enabled state for "Decoders" section;


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-9-pe.webp" alt="Click on the &quot;My Device&quot; row;" loading="lazy"><figcaption>Click on the "My Device" row;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-10-pe.webp" alt="The &quot;Device & Connectivity detail&quot; page will open. Now, go to the &quot;Flows&quot; tab, and click on &quot;My first flow&quot; row;" loading="lazy"><figcaption>The "Device & Connectivity detail" page will open. Now, go to the "Flows" tab, and click on "My first flow" row;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-11-pe.webp" alt="Click on the &quot;Data Processing&quot; row to open &quot;Data Processing details&quot; page;" loading="lazy"><figcaption>Click on the "Data Processing" row to open "Data Processing details" page;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-12-pe.webp" alt="Change the switch to enabled state for &quot;Decoders&quot; section;" loading="lazy"><figcaption>Change the switch to enabled state for "Decoders" section;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-13-pe.webp" alt="Your change has been saved." loading="lazy"><figcaption>Your change has been saved.</figcaption></figure></div>


**Add new Destination:**

- Go to "Destinations" in left menu and click on the "Add new Destination" button;
- Find the "SENTIENT" destination type, and click on "Choose SENTIENT" button;
- Set a name for your destination. 
- Paste "HTTP endpoint URL" from SENTIENT integration page to "HTTP endpoint URL" field. 
- Now, click on the "Generate" button, and save generated value. We will use it on SENTIENT. 
- Click on the "Add SENTIENT Destination" button;


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-14-pe.webp" alt="Go to &quot;Destinations&quot; in left menu and click on the &quot;Add new Destination&quot; button;" loading="lazy"><figcaption>Go to "Destinations" in left menu and click on the "Add new Destination" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-15-pe.webp" alt="Find the &quot;SENTIENT&quot; destination type, and click on &quot;Choose SENTIENT&quot; button;" loading="lazy"><figcaption>Find the "SENTIENT" destination type, and click on "Choose SENTIENT" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-16-pe.webp" alt="Set a name for your destination. Paste &quot;HTTP endpoint URL&quot; from SENTIENT integration page to &quot;HTTP endpoint URL&quot; field. Now, click on the &quot;Generate&quot; button, and save generated value. We will use it on SENTIENT. Finally, click on the &quot;Add SENTIENT Destination&quot; button." loading="lazy"><figcaption>Set a name for your destination. Paste "HTTP endpoint URL" from SENTIENT integration page to "HTTP endpoint URL" field. Now, click on the "Generate" button, and save generated value. We will use it on SENTIENT. Finally, click on the "Add SENTIENT Destination" button.</figcaption></figure></div>


**Link the "Destination" to the "Flow":**

- Go to the "Flows" -> "My first flow" and click on the "Link Destination" button in the "Destinations" row;
- Click on the "Link" button next to the destination you created earlier;
- The "Destination" has been successfully linked to the Flow.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-17-pe.webp" alt="Go to the &quot;Flows&quot; -> &quot;My first flow&quot; and click on the &quot;Link Destination&quot; button in the &quot;Destinations&quot; row;" loading="lazy"><figcaption>Go to the "Flows" -> "My first flow" and click on the "Link Destination" button in the "Destinations" row;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-18-pe.webp" alt="Click on the &quot;Link&quot; button next to the destination you created earlier;" loading="lazy"><figcaption>Click on the "Link" button next to the destination you created earlier;</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-things-configure-19-pe.webp" alt="The &quot;Destination&quot; has been successfully linked to the Flow." loading="lazy"><figcaption>The "Destination" has been successfully linked to the Flow.</figcaption></figure></div>


## Update integration

In order to validate the sender we can add a token to integration on SENTIENT. To do this, please follow the steps below:


1. Go to "Integrations center" section -> "Integrations" page and click on the integration you created earlier. Click on "Edit" button to enter edit mode.

1. Switch "Enable security (Headers filter)" toggle to enabled state and click "Add" button in "Headers filter" section.

1. Put "X-Things-Secret" to "Header" field and generated token to "Value" field. Finally, apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/kpn/kpn-add-integration-5-pe.webp" alt="Go to &quot;Integrations center&quot; section -> &quot;Integrations&quot; page and click on the integration you created earlier. Click on &quot;Edit&quot; button to enter edit mode." loading="lazy"><figcaption>Go to "Integrations center" section -> "Integrations" page and click on the integration you created earlier. Click on "Edit" button to enter edit mode.</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-add-integration-6-pe.webp" alt="Switch &quot;Enable security (Headers filter)&quot; toggle to enabled state and click &quot;Add&quot; button in &quot;Headers filter&quot; section." loading="lazy"><figcaption>Switch "Enable security (Headers filter)" toggle to enabled state and click "Add" button in "Headers filter" section.</figcaption></figure><figure><img src="/images/user-guide/integrations/kpn/kpn-add-integration-7-pe.webp" alt="Put &quot;X-Things-Secret&quot; to &quot;Header&quot; field and generated token to &quot;Value&quot; field. Finally, apply changes." loading="lazy"><figcaption>Put "X-Things-Secret" to "Header" field and generated token to "Value" field. Finally, apply changes.</figcaption></figure></div>


That's all that is needed to configured integration between KPN Things and SENTIENT. Now we can send data from KPN Things to SENTIENT.

## Send Uplink message

Now let’s use the "KPN Things Device simulator" app to send a message with the data to the SENTIENT. Click the "Send data now" button in the app. 


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/kpn/kpn-send-data-now.webp" alt="Use the &quot;KPN Things Device simulator&quot; app to send a message with the data to the SENTIENT. Click the &quot;Send data now&quot; button." loading="lazy"><figcaption>Use the "KPN Things Device simulator" app to send a message with the data to the SENTIENT. Click the "Send data now" button.</figcaption></figure></div>


After you sent message a new device was created in your SENTIENT instance.

Go to the SENTIENT instance, then navigate to the "Devices" page. Here you will find a new KPN Device and information about it as well as the telemetry that we sent to the device.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/kpn/kpn-things-device-1-pe.webp" alt="Go to the &quot;Devices&quot; page. Here you will find a new KPN Device and information about it as well as the telemetry that we sent to the device." loading="lazy"><figcaption>Go to the "Devices" page. Here you will find a new KPN Device and information about it as well as the telemetry that we sent to the device.</figcaption></figure></div>


Go to the "Integrations" page, select "KPN Things integration" and navigate to the "Events" tab. There you’ll see the message consumed by the KPN Things integration.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/kpn/kpn-things-uplink-1-pe.webp" alt="Go to the &quot;Integrations&quot; page, select &quot;KPN Things integration&quot; and navigate to the &quot;Events&quot; tab. There you&#39;ll see the message consumed by the KPN Things integration." loading="lazy"><figcaption>Go to the "Integrations" page, select "KPN Things integration" and navigate to the "Events" tab. There you&#39;ll see the message consumed by the KPN Things integration.</figcaption></figure></div>


## Next steps
