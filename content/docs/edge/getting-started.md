+++
title = "Getting Started with SENTIENT Edge"
description = "Getting Started with SENTIENT Edge"

[extra]
status = "imported"
checked = ""
source = "docs/edge/getting-started.md"
+++
This tutorial will guide you through the fundamentals of the **SENTIENT Edge** platform and introduce you to the most widely used features. From this tutorial, you will learn how to:
* Install and run **SENTIENT Edge** on your machine.
* Connect local devices, such as temperature sensors.
* Transmit data from the device to the **Edge** and then from the **Edge** to the **SENTIENT Cloud**.
* Create and configure real-time dashboards.

To keep it simple, we will skip over lengthy descriptions. However, if you need more detailed information, check out the [“What is SENTIENT Edge” article](/docs/edge/getting-started-guides/what-is-edge/) and explore our other documentation. 


<div class="st-callout info">


Looking for **white-labeling** or **premium features**? <a href="/docs/" target="_blank">Explore Edge Professional Edition documentation →</a>


</div>


## Prerequisites

To start running **SENTIENT Community Edition Edge**, you will need an active **SENTIENT Community Edition account** that supports **Edge** functionality.


You can install the **SENTIENT** local server. For this, please refer to the [SENTIENT installation guide](/docs/user-guide/install/installation-options/).

The local server can be accessed via [http://localhost:8080](http://localhost:8080). Throughout this tutorial, we will refer to this URL as **SERVER_URL.** Log in with:
* **Username:** tenant@sentient.org
* **Password:** tenant


### Edge Hardware Requirements

The hardware requirements for **SENTIENT Edge** are determined by the number of connected devices and the intensity of interactions with the platform interface.
To ensure optimal performance, we recommend the following:
* **At least 1GB of RAM (Light workload):** It is suitable for minimal interactions with the platform interface, such as dashboards and device management, and fewer than 100 connected devices.
* **At least 4GB of RAM (Heavy workload):** This configuration is suitable for intense platform interactions and 100+ devices connected to a single machine.

### Deploying a New Edge Instance

To create a new **Edge**:


1. Sign in to your **SENTIENT** instance and navigate to the **Edge Management > Instances** section. Click the **"+"** icon in the top right corner and select the **"Add new edge"** option.

1. Enter a name for the Edge you are creating. For example, "My New Edge". Click the **"Add"** button to confirm the addition of the **Edge instance**.

1. Your new **Edge** is created and will appear at the top of the list, as entries are sorted by creation time by default.


<div class="st-gallery"><figure><img src="/images/edge/installation-add-edge-item-1.webp" alt="Sign in to your **SENTIENT** instance and navigate to the **Edge Management > Instances** section. Click the **&quot;+&quot;** icon in the top right corner and select the **&quot;Add new edge&quot;** option." loading="lazy"><figcaption>Sign in to your **SENTIENT** instance and navigate to the **Edge Management > Instances** section. Click the **"+"** icon in the top right corner and select the **"Add new edge"** option.</figcaption></figure><figure><img src="/images/edge/installation-add-edge-item-2.webp" alt="Enter a name for the Edge you are creating. For example, &quot;My New Edge&quot;. Click the **&quot;Add&quot;** button to confirm the addition of the **Edge instance**." loading="lazy"><figcaption>Enter a name for the Edge you are creating. For example, "My New Edge". Click the **"Add"** button to confirm the addition of the **Edge instance**.</figcaption></figure><figure><img src="/images/edge/installation-add-edge-item-3.webp" alt="Your new **Edge** is created and will appear at the top of the list, as entries are sorted by creation time by default." loading="lazy"><figcaption>Your new **Edge** is created and will appear at the top of the list, as entries are sorted by creation time by default.</figcaption></figure></div>


### Edge Installation and Configuration

#### Guided Installation with SENTIENT Server Pre-configured Instructions


Once the **Edge** instance has been created, the installation instructions will be available for use. 
Each **Edge** has preset configurations that contain important credentials, such as **Edge Secret**, **Edge Key**, etc.  To access these configurations:


1. Click on the **Edge** entity to open its details.

1. Click the **"Install & Connection Instructions"** button.

1. Follow the instructions to install **Edge** and connect it to the server.


<div class="st-gallery"><figure><img src="/images/edge/installation/prepared-instructions-install-item-1-ce.webp" alt="Click on the **Edge** entity to open its details." loading="lazy"><figcaption>Click on the **Edge** entity to open its details.</figcaption></figure><figure><img src="/images/edge/installation/prepared-instructions-install-item-2-ce.webp" alt="Click the **&quot;Install & Connection Instructions&quot;** button." loading="lazy"><figcaption>Click the **"Install & Connection Instructions"** button.</figcaption></figure><figure><img src="/images/edge/installation/prepared-instructions-install-item-3-ce.webp" alt="Follow the instructions to install **Edge** and connect it to the server." loading="lazy"><figcaption>Follow the instructions to install **Edge** and connect it to the server.</figcaption></figure></div>


<div class="st-callout info">


If for any reason you are unable to access and/or use **Edge preset configurations**, please refer to the [manual installation instructions](/docs/user-guide/install/installation-options/).


</div>


### Accessing User Interfaces: URLs and Credentials


Once **Edge** is installed, you’ll be able to access the interface via [http://localhost:18080](http://localhost:18080).
This URL will be referred to as **EDGE_URL** throughout the rest of this tutorial.

To log in, use the same credentials as **SERVER_URL**:
* **Username:** tenant@sentient.org
* **Password:** tenant


<div class="st-callout warn">


Currently, **Edge** does not support **OAuth 2.0** for login purposes. 
If you wish to access Edge using your OAuth 2.0 **user credentials**, it is necessary to **assign a password** for this user on the **SENTIENT server.**


</div>


<div class="st-callout info">


If the Edge **HTTP bind port** was changed to **18080** during Edge installation, access the **SENTIENT Edge** instance at [http://localhost:18080](http://localhost:18080).


</div>


## Step 1. Connecting Device and Sending Telemetry Data

In **SENTIENT**, the **device** is the key entity that generates telemetry data, which is stored and processed for dashboards and analytics. 
**SENTIENT** also provides a **virtual device shell** for sending telemetry on behalf of the physical device for testing purposes.

To add a new device on the **Edge**, log in to your **SENTIENT Edge** instance at **EDGE_URL** and follow these steps:


1. Go to the <b>Entities > Devices</b> section.

1. Click the <b>"+"</b> icon and select the <b>"Add new device"</b> option. Enter a name for the device, for example, "My New Device". No other changes are required. Click the <b>"Add"</b> button to create the device.

1. After the device is created, instructions on how to check its <b>connectivity</b> will be provided. Select the <b>messaging protocol</b> and your <b>operating system</b>. Install the required client tools, then copy the provided command.

1. Run the previously copied command. Once the "temperature" readings are published, the device state will change from <span style="color:red">"Inactive"</span> to <span style="color:green">"Active"</span>, and you will see the published "temperature" readings. Finally, close the connectivity window.

1. To verify the received telemetry, click on the device entity and open the <b>"Latest Telemetry"</b> tab.


<div class="st-gallery"><figure><img src="/images/edge/getting-started/step-1-item-1-ce.webp" alt="Go to the Entities > Devices section." loading="lazy"><figcaption>Go to the <b>Entities > Devices</b> section.</figcaption></figure><figure><img src="/images/edge/getting-started/step-1-item-2-ce.webp" alt="Click the &quot;+&quot; icon and select the &quot;Add new device&quot; option. Enter a name for the device, for example, &quot;My New Device&quot;. No other changes are required. Click the &quot;Add&quot; button to create the device." loading="lazy"><figcaption>Click the <b>"+"</b> icon and select the <b>"Add new device"</b> option. Enter a name for the device, for example, "My New Device". No other changes are required. Click the <b>"Add"</b> button to create the device.</figcaption></figure><figure><img src="/images/edge/getting-started/step-1-item-3-ce.webp" alt="After the device is created, instructions on how to check its connectivity will be provided. Select the messaging protocol and your operating system. Install the required client tools, then copy the provided command." loading="lazy"><figcaption>After the device is created, instructions on how to check its <b>connectivity</b> will be provided. Select the <b>messaging protocol</b> and your <b>operating system</b>. Install the required client tools, then copy the provided command.</figcaption></figure><figure><img src="/images/edge/getting-started/step-1-item-4-ce.webp" alt="Run the previously copied command. Once the &quot;temperature&quot; readings are published, the device state will change from &quot;Inactive&quot; to &quot;Active&quot;, and you will see the published &quot;temperature&quot; readings. Finally, close the connectivity window." loading="lazy"><figcaption>Run the previously copied command. Once the "temperature" readings are published, the device state will change from <span style="color:red">"Inactive"</span> to <span style="color:green">"Active"</span>, and you will see the published "temperature" readings. Finally, close the connectivity window.</figcaption></figure><figure><img src="/images/edge/getting-started/step-1-item-5-ce.webp" alt="To verify the received telemetry, click on the device entity and open the &quot;Latest Telemetry&quot; tab." loading="lazy"><figcaption>To verify the received telemetry, click on the device entity and open the <b>"Latest Telemetry"</b> tab.</figcaption></figure></div>


In addition, the following may be used:
* [Bulk provisioning](/docs/user-guide/bulk-provisioning/): Use to deploy multiple devices from a CSV file via user interface.
* [REST API](/docs/api/): Use to add devices and other entities programmatically.


<div class="st-callout info">


Once a device is created on the **Edge**, it will be **automatically provisioned** to the **SENTIENT server**. To view the Edge device on the Server, visit the **SERVER_URL** and navigate to the **Entities > Devices** section.


</div>


## Step 2. Creating Dashboard and Configuring Widgets

A **Dashboard** is another key entity within **SENTIENT**. It allows you to visualize IoT data and control devices through the user interface.

To create a **dashboard**, login to your **SENTIENT Edge** instance and navigate to the **Dashboard** section. Then, follow these steps:


1. Click the <b>"+"</b> icon and select the <b>"Create new dashboard"</b> option from the drop-down menu.

1. Enter the dashboard name, for example, "New Dashboard", and click the <b>"Add"</b> button to create the dashboard.


<div class="st-gallery"><figure><img src="/images/edge/getting-started/step-4-item-1-ce.webp" alt="Click the &quot;+&quot; icon and select the &quot;Create new dashboard&quot; option from the drop-down menu." loading="lazy"><figcaption>Click the <b>"+"</b> icon and select the <b>"Create new dashboard"</b> option from the drop-down menu.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-2-ce.webp" alt="Enter the dashboard name, for example, &quot;New Dashboard&quot;, and click the &quot;Add&quot; button to create the dashboard." loading="lazy"><figcaption>Enter the dashboard name, for example, "New Dashboard", and click the <b>"Add"</b> button to create the dashboard.</figcaption></figure></div>


Once the **dashboard** is created, the system will automatically redirect you to the **Edit mode** page. 
To add a **widget**, select one from the **widget library**, where widgets are grouped into bundles. 
Each widget is linked to a data source, which defines the data it will display. 

For example, let's add and configure the **Entities table** and **Time series chart** widgets:


1. Click the <b>"Add widget"</b> button.

1. Locate the <b>"Tables"</b> bundle and click on it.

1. Select the <b>"Entities table"</b> widget.

1. In the <b>"Add Widget"</b> pop-up window, select the previously created device, "My New Device", in the <b>"Device"</b> field.<ul><li>The <b>“name”</b> key has already been added to the <b>“Columns”</b> section. It will display the column with the device name.</li><li>To add another column with different key value, click the <b>"Add column"</b> button.</li></ul>

1. To select an additional data key to display, click on the newly appeared field. In the drop-down menu, you will see the list of the available data keys. Select the <b>"temperature"</b> data key. Click the <b>"Add"</b> button.

1. The <b>"Entities table"</b> widget has been added, and <b>"My New Device"</b> is now displayed in the list. To add another widget, click the <b>"Add widget"</b> button.

1. Locate the <b>"Charts"</b> widgets bundle and click on it.

1. Select the <b>"Time series chart"</b> widget.

1. Select the previously created device, "My New Device", as the <b>data source</b>, and click the <b>"Add"</b> button. The <b>"Time series chart"</b> widget has been successfully added to the dashboard.

1. After configuring all the desired widgets, you can adjust their size and placement on the dashboard as needed. Drag and drop the widget to reposition it on the dashboard.

1. To resize the widget, drag its bottom-right corner.

1. To apply all changes to the dashboard, click the <b>"Save"</b> button in the upper-right corner of the screen.

1. Congratulations! You have successfully configured the dashboard. Now, all new telemetry readings will instantly appear on the dashboard widgets.


<div class="st-gallery"><figure><img src="/images/edge/getting-started/step-4-item-3-ce.webp" alt="Click the &quot;Add widget&quot; button." loading="lazy"><figcaption>Click the <b>"Add widget"</b> button.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-4-ce.webp" alt="Locate the &quot;Tables&quot; bundle and click on it." loading="lazy"><figcaption>Locate the <b>"Tables"</b> bundle and click on it.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-5-ce.webp" alt="Select the &quot;Entities table&quot; widget." loading="lazy"><figcaption>Select the <b>"Entities table"</b> widget.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-6-ce.webp" alt="In the &quot;Add Widget&quot; pop-up window, select the previously created device, &quot;My New Device&quot;, in the &quot;Device&quot; field.The “name” key has already been added to the “Columns” section. It will display the column with the device name.To add another column with different key value, click the &quot;Add column&quot; button." loading="lazy"><figcaption>In the <b>"Add Widget"</b> pop-up window, select the previously created device, "My New Device", in the <b>"Device"</b> field.<ul><li>The <b>“name”</b> key has already been added to the <b>“Columns”</b> section. It will display the column with the device name.</li><li>To add another column with different key value, click the <b>"Add column"</b> button.</li></ul></figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-7-ce.webp" alt="To select an additional data key to display, click on the newly appeared field. In the drop-down menu, you will see the list of the available data keys. Select the &quot;temperature&quot; data key. Click the &quot;Add&quot; button." loading="lazy"><figcaption>To select an additional data key to display, click on the newly appeared field. In the drop-down menu, you will see the list of the available data keys. Select the <b>"temperature"</b> data key. Click the <b>"Add"</b> button.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-9-ce.webp" alt="The &quot;Entities table&quot; widget has been added, and &quot;My New Device&quot; is now displayed in the list. To add another widget, click the &quot;Add widget&quot; button." loading="lazy"><figcaption>The <b>"Entities table"</b> widget has been added, and <b>"My New Device"</b> is now displayed in the list. To add another widget, click the <b>"Add widget"</b> button.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-10-ce.webp" alt="Locate the &quot;Charts&quot; widgets bundle and click on it." loading="lazy"><figcaption>Locate the <b>"Charts"</b> widgets bundle and click on it.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-11-ce.webp" alt="Select the &quot;Time series chart&quot; widget." loading="lazy"><figcaption>Select the <b>"Time series chart"</b> widget.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-12-ce.webp" alt="Select the previously created device, &quot;My New Device&quot;, as the data source, and click the &quot;Add&quot; button. The &quot;Time series chart&quot; widget has been successfully added to the dashboard." loading="lazy"><figcaption>Select the previously created device, "My New Device", as the <b>data source</b>, and click the <b>"Add"</b> button. The <b>"Time series chart"</b> widget has been successfully added to the dashboard.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-13-ce.webp" alt="After configuring all the desired widgets, you can adjust their size and placement on the dashboard as needed. Drag and drop the widget to reposition it on the dashboard." loading="lazy"><figcaption>After configuring all the desired widgets, you can adjust their size and placement on the dashboard as needed. Drag and drop the widget to reposition it on the dashboard.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-14-ce.webp" alt="To resize the widget, drag its bottom-right corner." loading="lazy"><figcaption>To resize the widget, drag its bottom-right corner.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-15-ce.webp" alt="To apply all changes to the dashboard, click the &quot;Save&quot; button in the upper-right corner of the screen." loading="lazy"><figcaption>To apply all changes to the dashboard, click the <b>"Save"</b> button in the upper-right corner of the screen.</figcaption></figure><figure><img src="/images/edge/getting-started/step-4-item-16-ce.webp" alt="Congratulations! You have successfully configured the dashboard. Now, all new telemetry readings will instantly appear on the dashboard widgets." loading="lazy"><figcaption>Congratulations! You have successfully configured the dashboard. Now, all new telemetry readings will instantly appear on the dashboard widgets.</figcaption></figure></div>


## Step 3. Pushing Data From Edge to Cloud

To process data on site, and communicate with local and cloud-side services, the **Edge Rule Chain Template** is used.  
In essence, the **Edge Root Rule Chain** refers to the **Rule Chain** within the **SENTIENT Edge** that processes incoming data and can trigger specific actions based on certain conditions.

To understand how the telemetry data is transmitted from the **Edge** to the **Cloud**, let's review the default **Edge Root Rule Chain**:


1. Within your <b>Edge</b> instance, go to the <b>Rule Chains</b> section and open the <b>"Edge Root Rule Chain"</b>.

1. The <a href="/docs/user-guide/rule-engine-2-0/nodes/action/push-to-cloud/" target="_blank">Push to Cloud</a> rule node is used to transmit messages from edge to cloud after they have been stored in the local database.


<div class="st-gallery"><figure><img src="/images/edge/getting-started/step-3-item-1-ce.webp" alt="Within your Edge instance, go to the Rule Chains section and open the &quot;Edge Root Rule Chain&quot;." loading="lazy"><figcaption>Within your <b>Edge</b> instance, go to the <b>Rule Chains</b> section and open the <b>"Edge Root Rule Chain"</b>.</figcaption></figure><figure><img src="/images/edge/getting-started/step-3-item-2-ce.webp" alt="The Push to Cloud rule node is used to transmit messages from edge to cloud after they have been stored in the local database." loading="lazy"><figcaption>The <a href="/docs/user-guide/rule-engine-2-0/nodes/action/push-to-cloud/" target="_blank">Push to Cloud</a> rule node is used to transmit messages from edge to cloud after they have been stored in the local database.</figcaption></figure></div>


<div class="st-callout info">


To edit the **Edge Rule Chain Template** or create a new one, log in to your **SENTIENT Server** instance at **SERVER_URL** and navigate to the **Edge management > Rule chain templates** section and follow [these instructions](/docs/edge/rule-engine/rule-chain-templates/).


</div>


## Step 4. Provisioning Entities From Edge to Server

Any real-world assets, devices, sensors or other logical components are represented within **SENTIENT** as corresponding [entities](/docs/user-guide/entities-and-relations/).
Most of the entities can be created on the **Edge instance**. Once an entity is created on the **Edge instance**, it will be automatically published to the **SENTIENT Server**, requiring no additional actions.

To view the published entity (e.g., device), log in to the **SENTIENT** at **SERVER_URL**:


1. Navigate to the <b>Devices</b> section to confirm that the newly created device, "My New Device", has been published to the <b>SENTIENT Server (Cloud)</b>.

1. Click on the "My New Device" to open the <b>"Device details"</b> page and select the <b>"Relations"</b> tab. Switch the direction from <b>"From"</b> to <b>"To"</b> to view the relation to the Edge that provisioned this device.


<div class="st-gallery"><figure><img src="/images/edge/getting-started/step-2-item-1-ce.webp" alt="Navigate to the Devices section to confirm that the newly created device, &quot;My New Device&quot;, has been published to the SENTIENT Server (Cloud)." loading="lazy"><figcaption>Navigate to the <b>Devices</b> section to confirm that the newly created device, "My New Device", has been published to the <b>SENTIENT Server (Cloud)</b>.</figcaption></figure><figure><img src="/images/edge/getting-started/step-2-item-2-ce.webp" alt="Click on the &quot;My New Device&quot; to open the &quot;Device details&quot; page and select the &quot;Relations&quot; tab. Switch the direction from &quot;From&quot; to &quot;To&quot; to view the relation to the Edge that provisioned this device." loading="lazy"><figcaption>Click on the "My New Device" to open the <b>"Device details"</b> page and select the <b>"Relations"</b> tab. Switch the direction from <b>"From"</b> to <b>"To"</b> to view the relation to the Edge that provisioned this device.</figcaption></figure></div>


## Step 5. Provisioning Entities From Server to Edge

The **entities** can also be created on the **Server** and then assigned to the **Edge instance**. 
This approach simplifies the management of entities across multiple **Edge instances**.

To assign entities to the **Edge**, log in to your **SENTIENT Server** at **SERVER_URL** and create an **entity**, for example, a dashboard. 


1. Then, navigate to the <b>Edge management > Instances</b> section and click on the <b>"Manage dashboards"</b> button of the instance in question.

1. On the <b>Edge Dashboards</b> page, you will see all the dashboards that are already assigned to this <b>Edge</b>. Click the <b>"+"</b> icon and select newly created dashboard from the drop-down menu. Click the <b>"Assign"</b> button to confirm the assignment.


<div class="st-gallery"><figure><img src="/images/edge/getting-started/step-5-item-1-ce.webp" alt="Then, navigate to the Edge management > Instances section and click on the &quot;Manage dashboards&quot; button of the instance in question." loading="lazy"><figcaption>Then, navigate to the <b>Edge management > Instances</b> section and click on the <b>"Manage dashboards"</b> button of the instance in question.</figcaption></figure><figure><img src="/images/edge/getting-started/step-5-item-2-ce.webp" alt="On the Edge Dashboards page, you will see all the dashboards that are already assigned to this Edge. Click the &quot;+&quot; icon and select newly created dashboard from the drop-down menu. Click the &quot;Assign&quot; button to confirm the assignment." loading="lazy"><figcaption>On the <b>Edge Dashboards</b> page, you will see all the dashboards that are already assigned to this <b>Edge</b>. Click the <b>"+"</b> icon and select newly created dashboard from the drop-down menu. Click the <b>"Assign"</b> button to confirm the assignment.</figcaption></figure></div>


To confirm that assigned entity is available on the **Edge**, open the **EDGE_URL** and go to the corresponding entity section:


1. Go to the <b>Dashboards</b> section and open the dashboard you have created on the <b>SENTIENT Server</b>

1. Verify that these are the same widgets that you have added on the Cloud.


<div class="st-gallery"><figure><img src="/images/edge/getting-started/step-5-item-3-ce.webp" alt="Go to the Dashboards section and open the dashboard you have created on the SENTIENT Server" loading="lazy"><figcaption>Go to the <b>Dashboards</b> section and open the dashboard you have created on the <b>SENTIENT Server</b></figcaption></figure><figure><img src="/images/edge/getting-started/step-5-item-4-ce.webp" alt="Verify that these are the same widgets that you have added on the Cloud." loading="lazy"><figcaption>Verify that these are the same widgets that you have added on the Cloud.</figcaption></figure></div>


## Your Feedback

Congratulations! You have successfully completed the initial configuration steps for **SENTIENT Edge**. Now you can send new telemetry readings and they will appear on the dashboard immediately.

Help us improve by providing your feedback at [GitHub/Issues](https://github.com/sentient/sentient-gateway/issues) or through the ["Contact us"](https://sentient.invenia.in/docs/contact-us/) form.
We would also greatly appreciate it if you could star our project on [GitHub](https://github.com/sentient/sentient-gateway)!

## Next steps
