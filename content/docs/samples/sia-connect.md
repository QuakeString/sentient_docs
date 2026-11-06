+++
title = "SIA Connect"
description = "SIA Connect Guide"

[extra]
status = "imported"
checked = ""
source = "docs/samples/sia-connect.md"
+++
In this comprehensive guide, we will walk you through the process of connecting an OPC-UA device to the SENTIENT platform via SIA Connect. 

The [SIA Connect](https://sia-connect.com/) is a tool that enables this process. 
By connecting your OPC-UA device to the SENTIENT platform, you can monitor, control, and automate your devices in a highly scalable and flexible way. Stay tuned as we guide you step by step through this process.


<div class="st-callout info">


Before proceeding with this guide, it's recommended that you follow [Getting Started](/docs/pe/getting-started-guides/helloworld/) guide to become familiar with SENTIENT devices and dashboards. This will enhance your learning experience and understanding of the concepts presented here.


</div>


## Creating device on SENTIENT

For simplicity, we will provide the device manually using the UI:


1. Login to your SENTIENT instance, and navigate to the "<b>Devices</b>" page of the "<b>Entities</b>" section. By default, will be redirected to the "<b>All</b>" device group. Click on the "<b>plus</b>" icon in the top right corner of the table and then select "<b>Add new device</b>" from drop-down menu;

1. Input device name. For example,"<b>OPC-UA Device</b>". Use the default device profile. Now, click the "<b>Credentials</b>" button;

1. Select "<b>MQTT Basic</b>" credentials type. Set "<b>opcua_device</b>" as a client ID, "<b>sia_connect</b>" as a user name and use your own password. Click "<b>Add</b>";

1. A window will open where you can check the device&#39;s connection to SENTIENT. Close this window by clicking "<b>Close</b>" button;

1. Congratulations on adding the device!


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/creating-opc-ua-device-1-paas.webp" alt="Login to your SENTIENT instance, and navigate to the &quot;Devices&quot; page of the &quot;Entities&quot; section. By default, will be redirected to the &quot;All&quot; device group. Click on the &quot;plus&quot; icon in the top right corner of the table and then select &quot;Add new device&quot; from drop-down menu;" loading="lazy"><figcaption>Login to your SENTIENT instance, and navigate to the "<b>Devices</b>" page of the "<b>Entities</b>" section. By default, will be redirected to the "<b>All</b>" device group. Click on the "<b>plus</b>" icon in the top right corner of the table and then select "<b>Add new device</b>" from drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/creating-opc-ua-device-2-paas.webp" alt="Input device name. For example,&quot;OPC-UA Device&quot;. Use the default device profile. Now, click the &quot;Credentials&quot; button;" loading="lazy"><figcaption>Input device name. For example,"<b>OPC-UA Device</b>". Use the default device profile. Now, click the "<b>Credentials</b>" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/creating-opc-ua-device-3-paas.webp" alt="Select &quot;MQTT Basic&quot; credentials type. Set &quot;opcua_device&quot; as a client ID, &quot;sia_connect&quot; as a user name and use your own password. Click &quot;Add&quot;;" loading="lazy"><figcaption>Select "<b>MQTT Basic</b>" credentials type. Set "<b>opcua_device</b>" as a client ID, "<b>sia_connect</b>" as a user name and use your own password. Click "<b>Add</b>";</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/creating-opc-ua-device-4-paas.webp" alt="A window will open where you can check the device&#39;s connection to SENTIENT. Close this window by clicking &quot;Close&quot; button;" loading="lazy"><figcaption>A window will open where you can check the device&#39;s connection to SENTIENT. Close this window by clicking "<b>Close</b>" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/creating-opc-ua-device-5-paas.webp" alt="Congratulations on adding the device!" loading="lazy"><figcaption>Congratulations on adding the device!</figcaption></figure></div>


## Launching demo OPC-UA server

We will use docker image as a demo OPC-UA server, which can be installed and run using the following command:

```
docker run -it -p 4840:4840 sentient/tb-gw-opcua-server:latest
```


After running the docker image, you will see the following logs in your terminal:

![image](/images/user-guide/integrations/sia-connect/terminal-opc-ua.webp)

## Setup SIA Connect

### Installing SIA Connect

In our case, we installed SIA Connect as a <b>.deb</b> package. You can find the official installation guide [here](https://help.sia-connect.com/en_US/linux-installation/install-sia-connect-on-linux). Additionally, you can install SIA Connect as a Docker image [here](https://help.sia-connect.com/en_US/docker/install-sia-connect-using-docker).
After successful installation, navigate to the default host <b>127.0.0.1:80</b> where the Web UI is running (host might differ, depending on your settings).


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/installing-sia-connect-1-paas.webp" alt="Go to the host, where the SIA Connect web UI is running." loading="lazy"><figcaption>Go to the host, where the SIA Connect web UI is running.</figcaption></figure></div>


You need to log in and provide your LICENSE key. Alternatively, you can use the demo version, which has a 30-minute session limit.

### Installing OPC-UA connector

Now, we have to download <b>OPC-UA</b> connector. For this purpose, follow these steps:

- Navigate to "<b>Connectors</b>" page in the side menu;
- Click on "<b>Search for Connector to download & install</b>" input field, and start typing the connector name - "<b>OPC-UA</b>";
- Find "<b>OPC-UA Client</b>", and download it by clicking the appropriate button.

<b>OPC-UA</b> connector installed.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/installing-opc-ua-connector-1-paas.webp" alt="Go to &quot;Connectors&quot; page in the side menu. Click on &quot;Search for Connector to download & install&quot; input field, and start typing the connector name - &quot;OPC-UA&quot;. Find &quot;OPC-UA Client&quot;, and download it by clicking the appropriate button. OPC-UA connector installed." loading="lazy"><figcaption>Go to "<b>Connectors</b>" page in the side menu. Click on "<b>Search for Connector to download & install</b>" input field, and start typing the connector name - "<b>OPC-UA</b>". Find "<b>OPC-UA Client</b>", and download it by clicking the appropriate button. <b>OPC-UA</b> connector installed.</figcaption></figure></div>


### Installing MQTT connector

Also, we need to download <b>MQTT</b> connector to establish connection with SENTIENT. The steps are as for downloading MQTT connector:

- Go to "<b>Connectors</b>" page in the side menu;
- Click on "<b>Search for Connector to download & install</b>" input field and type "<b>MQTT</b>";
- Find "<b>MQTT</b>", and download it by clicking the appropriate button. 

<b>MQTT</b> connector installed.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/installing-mqtt-connector-1-paas.webp" alt="Go to &quot;Connectors&quot; page in the side menu. Click on &quot;Search for Connector to download & install&quot; input field and type &quot;MQTT&quot;. Find &quot;MQTT&quot;, and download it by clicking the appropriate button. MQTT connector installed." loading="lazy"><figcaption>Go to "<b>Connectors</b>" page in the side menu. Click on "<b>Search for Connector to download & install</b>" input field and type "<b>MQTT</b>". Find "<b>MQTT</b>", and download it by clicking the appropriate button. <b>MQTT</b> connector installed.</figcaption></figure></div>


## Adding instances

To connect our test device, we need to create two instances:

- One for the device - this instance will connect to the demo OPC-UA server and receive data from it;
- One for SENTIENT - this instance will map data from the device instance, convert it to a suitable format, and send data to SENTIENT.

### Adding OPC-UA Device instance

First of all, we need to create OPC-UA Device instance, for this purpose, follow the steps below:

- Go to "<b>Instance</b>" tab in the side menu and click "<b>+ Add new instance</b>" button;
- Fill in the input fields:
  - "<b>Name</b>" - "<b>OPC-UA Device</b>";
  - "<b>Address</b>" - "<b>opc.tcp://127.0.0.1:4840/freeopcua/server/</b>";
- Disable security settings;
- Click the "<b>Save instance</b>" button.

OPC-UA Device instance added.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/adding-opc-ua-device-instance-1-paas.webp" alt="Go to &quot;Instance&quot; tab in the side menu and click &quot;+ Add new instance&quot; button;" loading="lazy"><figcaption>Go to "<b>Instance</b>" tab in the side menu and click "<b>+ Add new instance</b>" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/adding-opc-ua-device-instance-2-paas.webp" alt="Fill in the &quot;Name&quot; field by &quot;OPC-UA Device&quot; value, and &quot;“Address&quot; field by &quot;opc.tcp://127.0.0.1:4840/freeopcua/server/&quot; value. Also, don’t forget to disable security settings. Then, click the &quot;Save instance&quot; button;" loading="lazy"><figcaption>Fill in the "<b>Name</b>" field by "<b>OPC-UA Device</b>" value, and "<b>“Address</b>" field by "<b>opc.tcp://127.0.0.1:4840/freeopcua/server/</b>" value. Also, don’t forget to disable security settings. Then, click the "<b>Save instance</b>" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/adding-opc-ua-device-instance-3-paas.webp" alt="OPC-UA Device instance added." loading="lazy"><figcaption>OPC-UA Device instance added.</figcaption></figure></div>


Also, we need to create an item. An item represents a data point inside the instance. E.g a tag in a PLC, a topic on MQTT broker, an endpoint on REST API, or a query in database. Follow the steps below to add a new item to OPC-UA Device instance:

- Click on "<b>+ New item</b>" in the "<b>Items</b>" section;'
- Fill in the input fields:
  - "<b>Name</b>" - "<b>Temperature</b>"; 
  - Set the "<b>Read write</b>" field to "<b>Read only</b>" option;
  - "<b>Identifier</b>" - "<b>ns=2;i=13</b>"; 
- Click the "<b>Save item</b>" button.

You will now see the "<b>Temperature</b>" item added.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/adding-opc-ua-device-instance-4-paas.webp" alt="Click on &quot;+ New item&quot; in the &quot;Items&quot; section;" loading="lazy"><figcaption>Click on "<b>+ New item</b>" in the "<b>Items</b>" section;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/adding-opc-ua-device-instance-5-paas.webp" alt="Fill in the &quot;Name&quot; field using the &quot;Temperature&quot; value, set the &quot;Read write&quot; field to &quot;Read only&quot; option, and fill in the &quot;Identifier&quot; field by &quot;ns=2;i=13&quot; value. Then, click the &quot;Save item&quot; button;" loading="lazy"><figcaption>Fill in the "<b>Name</b>" field using the "<b>Temperature</b>" value, set the "<b>Read write</b>" field to "<b>Read only</b>" option, and fill in the "<b>Identifier</b>" field by "<b>ns=2;i=13</b>" value. Then, click the "<b>Save item</b>" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/adding-opc-ua-device-instance-6-paas.webp" alt="You will now see the &quot;Temperature&quot; item added." loading="lazy"><figcaption>You will now see the "<b>Temperature</b>" item added.</figcaption></figure></div>


Add other items, such as "<b>Power</b>" and "<b>Humidity</b>", by following the steps described above.

| **Item Name** | **Identifier** |
|:--------------|:---------------|
| Power         | **ns=2;i=14**  |
| Humidity      | **ns=2;i=15**  |

So, in the final result, you will have the following list of items:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/adding-opc-ua-device-instance-7-paas.webp" alt="Add other items, such as &quot;Power&quot; and &quot;Humidity&quot;." loading="lazy"><figcaption>Add other items, such as "<b>Power</b>" and "<b>Humidity</b>".</figcaption></figure></div>


### Adding SENTIENT instance

This instance will map data from the device instance, convert it to a suitable format, and send data to SENTIENT. To add a new instance, use follow these steps:

- Go to the <b>"Instance"</b> tab in the side menu and click <b>"+ Add new instance"</b> button;
- Fill in the input fields:
  - "<b>Name</b>" - "<b>SENTIENT</b>";
  - "<b>Address</b>" - "<b>your SENTIENT host</b>". In our case - <b>sentient.cloud</b>;
  - <b>"Port"</b> - "<b>1883</b>";
  - Fill in the values specified in [your device credentials](#creating-device-on-sentient) for the <b>"Username"</b>, <b>"Device id"</b>, and <b>"Password"</b> fields]
-  Click <b>"Save instance"</b> button.

SENTIENT instance has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/adding-sentient-instance-1-paas.webp" alt="Go to the &quot;Instance&quot; tab in the side menu and click &quot;+ Add new instance&quot; button. Fill in the input fields &quot;Name&quot;, &quot;Address&quot;, &quot;Port&quot;, &quot;Username&quot;, &quot;Device id&quot;, &quot;Password&quot; with the values shown in the screenshot below. Click &quot;Save instance&quot; button;" loading="lazy"><figcaption>Go to the "<b>Instance</b>" tab in the side menu and click "<b>+ Add new instance</b>" button. Fill in the input fields "<b>Name</b>", "<b>Address</b>", "<b>Port</b>", "<b>Username</b>", "<b>Device id</b>", "<b>Password</b>" with the values shown in the screenshot below. Click "<b>Save instance</b>" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/adding-sentient-instance-2-paas.webp" alt="SENTIENT instance has been added." loading="lazy"><figcaption>SENTIENT instance has been added.</figcaption></figure></div>


Now, we have to add new item. For this purpose, follow these steps:

- Click on the <b>"+ New item"</b> in the "<b>Items</b>" section;
- Fill in the input fields:
  - "<b>Name</b>" - "<b>Publish data</b>";
  - Set "<b>Read write</b>" field to <b>"Write only"</b> option;
  - "<b>Topic</b>" - "<b>v1/devices/me/telemetry</b>";
  - "<b>Input template</b>" - "<b>{&#37;ITEM.NAME&#37;: &#37;VALUE&#37;}</b>"; 
- Click on <b>"Save item"</b> button.

<b>Publish data</b> item has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/adding-sentient-instance-3-paas.webp" alt="Click on the &quot;+ New item&quot; in the &quot;Items&quot; section;" loading="lazy"><figcaption>Click on the "<b>+ New item</b>" in the "<b>Items</b>" section;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/adding-sentient-instance-4-paas.webp" alt="Set &quot;Read write&quot; select field to &quot;Write only&quot; option, fill in &quot;Topic&quot; field by &quot;v1/devices/me/telemetry&quot; value and &quot;Input template&quot; field by &quot;{%ITEM.NAME%: %VALUE%}&quot; value. Click on &quot;Save item&quot; button. Publish data item has been added." loading="lazy"><figcaption>Set "<b>Read write</b>" select field to "<b>Write only</b>" option, fill in "<b>Topic</b>" field by "<b>v1/devices/me/telemetry</b>" value and "<b>Input template</b>" field by "<b>{%ITEM.NAME%: %VALUE%}</b>" value. Click on "<b>Save item</b>" button. Publish data item has been added.</figcaption></figure></div>


And finally, we have to add mapping. A mapping is a virtual connection between two items which will handle data transmission between the two  (e.g. a mapping from a PLC item to a MQTT item). For this purpose, follow these steps:

- Click on the <b>"+ New mapping"</b> in the "<b>Mappings on SENTIENT</b>" section;
- For "<b>Sender Item</b>" select "<b>OPC-UA Device</b>" as instance and "<b>Temperature</b>" as "<b>Item</b>"; 
- For "<b>Receiver item</b>" select "<b>SENTIENT</b>" as "<b>Instance</b>" and "<b>Publish data</b>" as "<b>Item</b>"; 
- Click on "<b>Save mapping</b>" button.
 
Mapping has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/adding-sentient-instance-5-paas.webp" alt="Click on the &quot;+ New mapping&quot; in the &quot;Mappings on SENTIENT&quot; section;" loading="lazy"><figcaption>Click on the "<b>+ New mapping</b>" in the "<b>Mappings on SENTIENT</b>" section;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/adding-sentient-instance-6-paas.webp" alt="For &quot;Sender Item&quot; select &quot;OPC-UA Device&quot; as instance and &quot;Temperature&quot; as &quot;Item&quot;. For &quot;Receiver item&quot; select &quot;SENTIENT&quot; as &quot;Instance&quot; and &quot;Publish data&quot; as &quot;Item&quot;. Click on &quot;Save mapping&quot; button. Mapping has been added." loading="lazy"><figcaption>For "<b>Sender Item</b>" select "<b>OPC-UA Device</b>" as instance and "<b>Temperature</b>" as "<b>Item</b>". For "<b>Receiver item</b>" select "<b>SENTIENT</b>" as "<b>Instance</b>" and "<b>Publish data</b>" as "<b>Item</b>". Click on "<b>Save mapping</b>" button. Mapping has been added.</figcaption></figure></div>


Add other mappings, such as "<b>Power</b>" and "<b>Humidity</b>", by following the steps described above.

After completing these steps, you will have the following list of mappings:


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/adding-sentient-instance-7-paas.webp" alt="Add other mappings, such as &quot;Power&quot; and &quot;Humidity&quot;." loading="lazy"><figcaption>Add other mappings, such as "<b>Power</b>" and "<b>Humidity</b>".</figcaption></figure></div>


## Check data on SENTIENT

Once you have successfully done all the steps above and SIA Connect has sent data, you can view it in the "Latest telemetry" tab of the device in your SENTIENT instance:

- Navigate to the "<b>Devices</b>" page of the "<b>Entities</b>" section of your <b>SENTIENT</b> instance;
- Click on the OPC-UA Device row in the table to open device details;
- Navigate to the "<b>Latest telemetry</b>" tab.

You should see incoming data displayed.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/check-data-on-sentient-1-paas.webp" alt="Navigate to the &quot;Devices&quot; page of the &quot;Entities&quot; section of your SENTIENT instance, and click on the OPC-UA Device row in the table to open device details. Navigate to the &quot;Latest telemetry&quot; tab. You must see incoming data." loading="lazy"><figcaption>Navigate to the "<b>Devices</b>" page of the "<b>Entities</b>" section of your <b>SENTIENT</b> instance, and click on the OPC-UA Device row in the table to open device details. Navigate to the "<b>Latest telemetry</b>" tab. You must see incoming data.</figcaption></figure></div>


## Change OPC-UA node values using shared attributes

In this section, we will configure SIA Connect to modify the value of an OPC-UA node. Specifically, we will be changing the device status node.

For this purpose we need to create one more item in <b>SENTIENT</b> instance of the <b>SIA Connect</b>, like the following:

- Go to the "<b>Instance</b>" tab in the side menu and select "<b>SENTIENT</b>";
- Click on the "<b>+ New item</b>" in the "<b>Items</b>" section;
- Fill in the input fields:
  - "<b>Name</b>" - "<b>Shared attribute update</b>"; 
  - Set "<b>Read write</b>" select field to "<b>Read only</b>" option;
  - "<b>Topic</b>" - "<b>v1/devices/me/attributes</b>";
- Click on "<b>Save item</b>" button. 

Item has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/shared-attributes-1-paas.webp" alt="Go to the &quot;Instance&quot; tab in the side menu and select &quot;SENTIENT&quot;;" loading="lazy"><figcaption>Go to the "<b>Instance</b>" tab in the side menu and select "<b>SENTIENT</b>";</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/shared-attributes-2-paas.webp" alt="Click on the &quot;+ New item&quot; in the &quot;Items&quot; section;" loading="lazy"><figcaption>Click on the "<b>+ New item</b>" in the "<b>Items</b>" section;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/shared-attributes-3-paas.webp" alt="Fill the &quot;Name&quot; field by &quot;Shared attribute update&quot; value, set &quot;Read write&quot; select field to &quot;Read only&quot; option, and fill in &quot;Topic&quot; field by &quot;v1/devices/me/attributes&quot; value. Click on &quot;Save item&quot; button. Item has been added." loading="lazy"><figcaption>Fill the "<b>Name</b>" field by "<b>Shared attribute update</b>" value, set "<b>Read write</b>" select field to "<b>Read only</b>" option, and fill in "<b>Topic</b>" field by "<b>v1/devices/me/attributes</b>" value. Click on "<b>Save item</b>" button. Item has been added.</figcaption></figure></div>


Also, we need to create item on **OPC-UA Device** instance, for this purpose, follow these steps:

- Go to the "<b>Instance</b>" tab in the side menu and select <b>OPC-UA Device</b>;
- Click on the "<b>+ New item</b>" in the "<b>Items</b>" section;
- Fill in the input fields:
  - "<b>Name</b>" - "<b>Status</b>";
  - Set "<b>Read write</b>" select field to "<b>Read and Write</b>";
  - "<b>Post-processing (reading)</b>" - <b>“%VALUE%”</b>;
  - "<b>Identifier</b>" - "<b>ns=4;s=Status_s</b>";
- Click on "<b>Save item</b>" button.
 
Item added.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/status-attributes-1-paas.webp" alt="Go to the &quot;Instance&quot; tab in the side menu and select OPC-UA Device;" loading="lazy"><figcaption>Go to the "<b>Instance</b>" tab in the side menu and select <b>OPC-UA Device</b>;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/status-attributes-2-paas.webp" alt="Click on the &quot;+ New item&quot; in the &quot;Items&quot; section;" loading="lazy"><figcaption>Click on the "<b>+ New item</b>" in the "<b>Items</b>" section;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/status-attributes-3-paas.webp" alt="Fill in &quot;Name&quot; field with &quot;Status&quot; value, set &quot;Read write&quot; select field to &quot;Read and Write&quot;, fill in &quot;Post-processing (reading)&quot; field by “%VALUE%”, and fill in &quot;Identifier&quot; field by &quot;ns=4;s=Status_s&quot;. Click on &quot;Save item&quot; button. Item added." loading="lazy"><figcaption>Fill in "<b>Name</b>" field with "<b>Status</b>" value, set "<b>Read write</b>" select field to "<b>Read and Write</b>", fill in "<b>Post-processing (reading)</b>" field by <b>“%VALUE%”</b>, and fill in "<b>Identifier</b>" field by "<b>ns=4;s=Status_s</b>". Click on "<b>Save item</b>" button. Item added.</figcaption></figure></div>


The next step is to create another mapping for data transmission between the SENTIENT instance and the OPC-UA Device. For this purpose, follow the steps below:

- On the <b>SENTIENT</b> instance, scroll down to "<b>Mappings</b>" section and click on "<b>+ New Mapping</b>" button;
- For "<b>Sender Item</b>" select "<b>SENTIENT</b>" as instance and "<b>Shared attribute update</b>" as "<b>Item</b>"; 
- For "<b>Receiver item</b>" select "<b>OPC-UA Device</b>" as instance and "<b>Status</b>" as "<b>Item</b>";
- Paste "<b>%VALUE.status%</b>" to the "<b>Custom value</b>" field; 
- Click on "<b>Save mapping</b>" button.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/create-another-mapping-1-paas.webp" alt="On the SENTIENT instance, scroll down to &quot;Mappings&quot; section and click on &quot;+ New Mapping&quot; button;" loading="lazy"><figcaption>On the <b>SENTIENT</b> instance, scroll down to "<b>Mappings</b>" section and click on "<b>+ New Mapping</b>" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/create-another-mapping-2-paas.webp" alt="For &quot;Sender Item&quot; select &quot;SENTIENT&quot; as instance and &quot;Shared attribute update&quot; as &quot;Item&quot;. For &quot;Receiver item&quot; select &quot;OPC-UA Device&quot; as instance and &quot;Status&quot; as &quot;Item&quot;. Paste &quot;%VALUE.status%&quot; to the &quot;Custom value&quot; field. Click on &quot;Save mapping&quot; button;" loading="lazy"><figcaption>For "<b>Sender Item</b>" select "<b>SENTIENT</b>" as instance and "<b>Shared attribute update</b>" as "<b>Item</b>". For "<b>Receiver item</b>" select "<b>OPC-UA Device</b>" as instance and "<b>Status</b>" as "<b>Item</b>". Paste "<b>%VALUE.status%</b>" to the "<b>Custom value</b>" field. Click on "<b>Save mapping</b>" button;</figcaption></figure></div>


Finally, we need to create shared attribute on the device on SENTIENT platform. For this purpose, follow these steps:

- Go to the "<b>Devices</b>" page of the "<b>Entities</b>" section of your <b>SENTIENT</b> instance;
- Click on "<b>OPC-UA Device</b>", and navigate to the "<b>Attributes</b>" tab;
- Select "<b>Shared attributes</b>" from dropdown field and click on "<b>plus</b>" button to create a new one;
- Fill in "<b>Key</b>" field with "<b>status</b>" value and select "<b>Boolean</b>" data type from dropdown field;
- Click on "<b>Add</b>" button.

Shared attribute has been added.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/shared-attribute-on-device-1-paas.webp" alt="Go to the &quot;Devices&quot; tab on the left side menu bar. Click on &quot;OPC-UA Device&quot;, and navigate to the &quot;Attributes&quot; tab. Select &quot;Shared attributes&quot; from dropdown field, and click on &quot;plus&quot; button for create new one;" loading="lazy"><figcaption>Go to the "<b>Devices</b>" tab on the left side menu bar. Click on "<b>OPC-UA Device</b>", and navigate to the "<b>Attributes</b>" tab. Select "<b>Shared attributes</b>" from dropdown field, and click on "<b>plus</b>" button for create new one;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/shared-attribute-on-device-2-paas.webp" alt="Fill in &quot;Key&quot; field by &quot;status&quot; value, and select &quot;Boolean&quot; data type from dropdown field. Then, click on &quot;Add&quot;;" loading="lazy"><figcaption>Fill in "<b>Key</b>" field by "<b>status</b>" value, and select "<b>Boolean</b>" data type from dropdown field. Then, click on "<b>Add</b>";</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/shared-attribute-on-device-3-paas.webp" alt="Shared attribute has been added." loading="lazy"><figcaption>Shared attribute has been added.</figcaption></figure></div>


## Visualize data on SENTIENT

To visualize data from Sia Connect, we will create [the dashboard](/docs/pe/user-guide/dashboards/):

- First, download the [sia_connect.json](/docs/pe/user-guide/resources/sia_connect.json) file;


1. Go to the "<b>Dashboard</b>" page of your "<b>SENTIENT</b>" instance. By default, you will be redirected to the "<b>All</b>" device group. Click on the "<b>plus</b>" icon in the top right corner of the table and then select "<b>Import dashboard</b>" from drop-down menu;

1. In the import dashboard window, upload the previously downloaded dashboard configuration JSON file, and click "<b>Import</b>";

1. You have successfully imported a dashboard. You should open it.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/import-dashboard-1-paas.webp" alt="Go to the &quot;Dashboard&quot; page of your &quot;SENTIENT&quot; instance. By default, you will be redirected to the &quot;All&quot; device group. Click on the &quot;plus&quot; icon in the top right corner of the table and then select &quot;Import dashboard&quot; from drop-down menu;" loading="lazy"><figcaption>Go to the "<b>Dashboard</b>" page of your "<b>SENTIENT</b>" instance. By default, you will be redirected to the "<b>All</b>" device group. Click on the "<b>plus</b>" icon in the top right corner of the table and then select "<b>Import dashboard</b>" from drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/import-dashboard-2-paas.webp" alt="In the import dashboard window, upload the previously downloaded dashboard configuration JSON file, and click &quot;Import&quot;;" loading="lazy"><figcaption>In the import dashboard window, upload the previously downloaded dashboard configuration JSON file, and click "<b>Import</b>";</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/import-dashboard-3-paas.webp" alt="You have successfully imported a dashboard. You should open it." loading="lazy"><figcaption>You have successfully imported a dashboard. You should open it.</figcaption></figure></div>


After importing the dashboard, verify that your OPC-UA Device is specified in the [entity alias](/docs/pe/user-guide/ui/aliases/). This ensures that the data will be displayed correctly.


1. Enter dashboard editing mode;

1. Click the "Entity aliases" icon;

1. In the opened "<b>Entity aliases</b>" window click the "<b>Edit alias</b>" icon opposite the "<b>OPC-UA Device</b>" alias;

1. In the opened "<b>Edit alias</b>" dialog, specify your <b>OPC-UA Device</b>. A filter type should be "<b>Single entity</b>". Click the "<b>Save</b>" button;

1. Click "<b>Save</b>" in the lower right corner of the dialog box;

1. Save the dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/change-entity-alias-1-paas.webp" alt="Enter dashboard editing mode;" loading="lazy"><figcaption>Enter dashboard editing mode;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/change-entity-alias-2-paas.webp" alt="Click the &quot;Entity aliases&quot; icon;" loading="lazy"><figcaption>Click the "Entity aliases" icon;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/change-entity-alias-3-paas.webp" alt="In the opened &quot;Entity aliases&quot; window click the &quot;Edit alias&quot; icon opposite the &quot;OPC-UA Device&quot; alias;" loading="lazy"><figcaption>In the opened "<b>Entity aliases</b>" window click the "<b>Edit alias</b>" icon opposite the "<b>OPC-UA Device</b>" alias;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/change-entity-alias-4-paas.webp" alt="In the opened &quot;Edit alias&quot; dialog, specify your OPC-UA Device. A filter type should be &quot;Single entity&quot;. Click the &quot;Save&quot; button;" loading="lazy"><figcaption>In the opened "<b>Edit alias</b>" dialog, specify your <b>OPC-UA Device</b>. A filter type should be "<b>Single entity</b>". Click the "<b>Save</b>" button;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/change-entity-alias-5-paas.webp" alt="Click &quot;Save&quot; in the lower right corner of the dialog box;" loading="lazy"><figcaption>Click "<b>Save</b>" in the lower right corner of the dialog box;</figcaption></figure><figure><img src="/images/user-guide/integrations/sia-connect/change-entity-alias-6-paas.webp" alt="Save the dashboard." loading="lazy"><figcaption>Save the dashboard.</figcaption></figure></div>


If you have followed these steps correctly, you should now see this dashboard populated with data from the OPC-UA Device.


<div class="st-gallery"><figure><img src="/images/user-guide/integrations/sia-connect/change-entity-alias-7-paas.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Conclusion

By following the instructions provided in this guide, you'll be able to effortlessly establish a connection between your OPC-UA device and the SENTIENT platform using SIA Connect. 
This comprehensive guide has been carefully designed to provide you with all the necessary information and steps needed to successfully set up this connection. 
So whether you're a seasoned expert or a beginner, this guide will make the process simple and straightforward.
