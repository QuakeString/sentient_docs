+++
title = "Getting started with SENTIENT IoT Gateway"
description = "Configure MQTT, OPC-UA, and Modbus connectors to establish connections with their respective demo servers in the Docker container and retrieve data."

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/getting-started.md"
+++
The SENTIENT IoT Gateway is an open-source solution, designed to serve as a bridge between IoT devices connected to 
legacy and third-party systems with SENTIENT.

This guide covers initial IoT Gateway installation and configuration, we will do the following things:
- Create a new gateway device;
- Launch the gateway using Docker command;
- Configure different connector types ([MQTT](/docs/iot-gateway/config/mqtt/), [OPC-UA](/docs/iot-gateway/config/opc-ua/), [Modbus](/docs/iot-gateway/config/modbus/)) in order to connect to a local demo servers and read data from them;
- Check received device data on SENTIENT.

## Prerequisites

- Before initiating the Gateway setup, ensure that the SENTIENT server is up and running. The simplest approach is to use [SENTIENT Cloud](https://sentient.invenia.in/installations/). Alternatively, you can install SENTIENT manually by following the steps outlined in the [Installation Guide](/docs/user-guide/install/installation-options/).
- Before moving forward, ensure Docker is installed and properly configured on your machine. If you haven't installed Docker yet, you can download it from the [official Docker website](https://docs.docker.com/engine/install/) and follow their installation guide for your specific operating system.

## Step 1. Create a new gateway device on SENTIENT

First, add a gateway device to your SENTIENT instance by following these steps:


1. Go to "**Entities**" > "**Gateways**" tab.

1. Click the "**+**" button, enter the gateway device name (e.g., "My Gateway"), and select the device profile. Click on "**Create**" button.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/gateway-getting-started-1-ce.webp" alt="Go to &quot;**Entities**&quot; > &quot;**Gateways**&quot; tab." loading="lazy"><figcaption>Go to "**Entities**" > "**Gateways**" tab.</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-2-ce.webp" alt="Click the &quot;**+**&quot; button, enter the gateway device name (e.g., &quot;My Gateway&quot;), and select the device profile. Click on &quot;**Create**&quot; button." loading="lazy"><figcaption>Click the "**+**" button, enter the gateway device name (e.g., "My Gateway"), and select the device profile. Click on "**Create**" button.</figcaption></figure></div>

 


<div class="st-callout info">


<div>
  <p>
    <span style="color:black">If you've previously configured the gateway, create a backup, as the new remote configuration will overwrite existing settings files.  
    <br>For those who used a gateway version earlier than 3.4, the gateway will automatically generate a new configuration file in JSON format.</span>
  </p>
</div>


</div>


To launch the gateway, use the following steps:


1. Select and click on newly created gateway, click on **"Launch command"** button in the top right corner.

1. Click to download `docker-compose.yml` file to your PC, copy command and execute it in your terminal.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/gateway-getting-started-3-ce.webp" alt="Select and click on newly created gateway, click on **&quot;Launch command&quot;** button in the top right corner." loading="lazy"><figcaption>Select and click on newly created gateway, click on **"Launch command"** button in the top right corner.</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-4-ce.webp" alt="Click to download `docker-compose.yml` file to your PC, copy command and execute it in your terminal." loading="lazy"><figcaption>Click to download `docker-compose.yml` file to your PC, copy command and execute it in your terminal.</figcaption></figure></div>


After running gateway docker image, you can see the following logs in your terminal:

![](/images/gateway/dashboard/launch-gateway-docker.webp)

## Step 2. Enable remote logging

To view gateway and connector logs on the platform side, you need to enable remote logging. For this purpose, 
use the following steps:


1. On selected gateway page, click on **"General configuration"** button on the right panel.

1. Navigate to the "**Logs**" tab. Enable the "**Remote logging**" toggle. Select "**DEBUG**" in the "**Log level**" drop-down menu. Click on the "**Save**" button to apply changes.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/general-configuration-1-ce.webp" alt="On selected gateway page, click on **&quot;General configuration&quot;** button on the right panel." loading="lazy"><figcaption>On selected gateway page, click on **"General configuration"** button on the right panel.</figcaption></figure><figure><img src="/images/gateway/dashboard/general-configuration-2-ce.webp" alt="Navigate to the &quot;**Logs**&quot; tab. Enable the &quot;**Remote logging**&quot; toggle. Select &quot;**DEBUG**&quot; in the &quot;**Log level**&quot; drop-down menu. Click on the &quot;**Save**&quot; button to apply changes." loading="lazy"><figcaption>Navigate to the "**Logs**" tab. Enable the "**Remote logging**" toggle. Select "**DEBUG**" in the "**Log level**" drop-down menu. Click on the "**Save**" button to apply changes.</figcaption></figure></div>


## Step 3. Add new connector

By choosing the type of connector, you determine the specific method of connection you will use to ensure the 
interaction of your gateway with other systems or devices.

To see how the connector works, you can choose one of the following connectors:


<div class="st-tabs">

<div class="st-tab" data-label="MQTT">

Let's add an **MQTT connector**, which will subscribe to some data topics using the 
demo broker with a built-in data generator and send data to the gateway.

### Setup demo MQTT broker

As a demo MQTT broker, we will use docker image, that can be installed and run using the following command:

```bash
docker run -it -p 1884:1884 sentient/tb-gw-mqtt-broker:latest
```


After running docker image, you can see the following logs in your terminal:

![](/images/gateway/dashboard/run-demo-mqtt-broker-image.webp)

### Setup connector

MQTT connector will establish a connection to a broker named **“Demo Broker”** at **“host.docker.internal”** on port **1884**, using an anonymous security type. 
It will include a data mapping for the **“data/”** topic, specifying a JSON converter and defining attribute and time series mappings for device data. 
Additionally, it will handle connect and disconnect requests for sensors with expressions to extract device names from topic filters.

To create a connector, follow these steps:


1. Click on "**Connectors configuration**" button on the right panel;

1. Click the "**+ Add connector**" button;

1. Choose "**MQTT**" connector type from the dropdown, fill in "**Name**" field, choose "**Logging level**" to INFO, disable "**Fill configuration with default values**" field and click on "**Add**" button;

1. Connector created.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/gateway-getting-started-7-ce.webp" alt="Click on &quot;**Connectors configuration**&quot; button on the right panel;" loading="lazy"><figcaption>Click on "**Connectors configuration**" button on the right panel;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-8-ce.webp" alt="Click the &quot;**+ Add connector**&quot; button;" loading="lazy"><figcaption>Click the "**+ Add connector**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-mqtt-9-ce.webp" alt="Choose &quot;**MQTT**&quot; connector type from the dropdown, fill in &quot;**Name**&quot; field, choose &quot;**Logging level**&quot; to INFO, disable &quot;**Fill configuration with default values**&quot; field and click on &quot;**Add**&quot; button;" loading="lazy"><figcaption>Choose "**MQTT**" connector type from the dropdown, fill in "**Name**" field, choose "**Logging level**" to INFO, disable "**Fill configuration with default values**" field and click on "**Add**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-mqtt-10-ce.webp" alt="Connector created." loading="lazy"><figcaption>Connector created.</figcaption></figure></div>

 

First, we need to configure the connection to the demo broker. Let’s start from the "**Connection to broker**" section. 
This section offers detailed connection configuration options and contains several important fields, including host, port, MQTT version, client ID, and security settings. 
The **host** field specifies the address of the broker, while the **port** field indicates the communication port. The **MQTT version** field ensures compatibility with the protocol version being used. The **client ID** uniquely identifies the client, and the **security** settings provides configuration for client authorization at MQTT Broker.

Fill in the following fields with values:

| **Field name** | **Value**            |
|:---------------|:---------------------|
| Host           | host.docker.internal |
| Port           | 1884                 |
| MQTT version   | 5                    |
| Client ID      | randomly generated   |
| Security       | Anonymous            |
| ---            |                      |


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/connection-to-broker-section-1-ce.webp" alt="First, we need to configure the connection to the demo broker. Let’s start from the &quot;**Connection to broker**&quot; section. This section offers detailed connection configuration options and contains several important fields, including host, port, MQTT version, client ID, and security settings. The **host** field specifies the address of the broker, while the **port** field indicates the communication port. The **MQTT version** field ensures compatibility with the protocol version being used. The **client ID** uniquely identifies the client, and the **security** settings provides configuration for client authorization at MQTT Broker." loading="lazy"><figcaption>First, we need to configure the connection to the demo broker. Let’s start from the "**Connection to broker**" section. This section offers detailed connection configuration options and contains several important fields, including host, port, MQTT version, client ID, and security settings. The **host** field specifies the address of the broker, while the **port** field indicates the communication port. The **MQTT version** field ensures compatibility with the protocol version being used. The **client ID** uniquely identifies the client, and the **security** settings provides configuration for client authorization at MQTT Broker.</figcaption></figure></div>


<br>
Now, we are ready to move to the "**Data mapping**" section. This configuration section contains an array of topics that the gateway will subscribe to after connecting to the broker, along with settings about processing incoming messages (converter).

Let's configure data map using the following steps:
- Click on "**Add mapping**" button
- In the opened window, fill in the "**Topic filter**" field with "**data/**", select the "**QoS**" field to "**0 - At most once**", and select the "**Payload type**" to **JSON**.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/data-mapping-0-ce.webp" alt="Click &quot;**Connectors configuration**&quot; button on the right panel." loading="lazy"><figcaption>Click "**Connectors configuration**" button on the right panel.</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-1-ce.webp" alt="In the opened window, fill in the &quot;**Topic filter**&quot; field with &quot;**data/**&quot;, select the &quot;**QoS**&quot; field to &quot;**0 - At most once**&quot;, and select the &quot;**Payload type**&quot; to **JSON**." loading="lazy"><figcaption>In the opened window, fill in the "**Topic filter**" field with "**data/**", select the "**QoS**" field to "**0 - At most once**", and select the "**Payload type**" to **JSON**.</figcaption></figure></div>


- Scroll down to "**Data conversion**" section:
  - For "**Device**" subsection use the following options/values:
    - In the "**Name**" row, select "**Constant**" in the "**Source**" dropdown field, fill in the "**Value / Expression**" field with the "**Device Demo**" value.
    - In the "**Profile name**" row, select "**Constant**" in the "**Source**" dropdown field, fill in the "**Value / Expression**" field with the "**default**" value.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/data-mapping-2-ce.webp" alt="Scroll down to &quot;**Data conversion**&quot; section. For &quot;**Device**&quot; subsection use the following options/values: In the **Name** row, select &quot;**Constant**&quot; in the &quot;**Source**&quot; dropdown field, fill in the &quot;**Value / Expression**&quot; field with the &quot;**Device Demo**&quot; value. In the &quot;**Profile name**&quot; row, select &quot;**Constant**&quot; in the &quot;**Source**&quot; dropdown field, fill in the &quot;**Value / Expression**&quot; field with the &quot;**default**&quot; value." loading="lazy"><figcaption>Scroll down to "**Data conversion**" section. For "**Device**" subsection use the following options/values: In the **Name** row, select "**Constant**" in the "**Source**" dropdown field, fill in the "**Value / Expression**" field with the "**Device Demo**" value. In the "**Profile name**" row, select "**Constant**" in the "**Source**" dropdown field, fill in the "**Value / Expression**" field with the "**default**" value.</figcaption></figure></div>


  - Click on pencil icon opposite to "**Attributes**" subsection and use the following options/values in the opened window:
    - Click on "**Add attribute**" button and fill in "**Key**" field with "**frequency**" value, select "**Integer**" option in "**Type**" field and fill in "**Value**" field with "**${frequency}**" value.
    - Click on "**Add attribute**" button and fill in "**Key**" field with "**power**" value, select "**Integer**" option in "**Type**" field and fill in "**Value**" field with "**${power}**" value.
    - Click on "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/data-mapping-3-ce.webp" alt="Click on pencil icon opposite to &quot;**Attributes**&quot; subsection;" loading="lazy"><figcaption>Click on pencil icon opposite to "**Attributes**" subsection;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-4-ce.webp" alt="Click on &quot;**Add attribute**&quot; button;" loading="lazy"><figcaption>Click on "**Add attribute**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-5-ce.webp" alt="Fill in &quot;**Key**&quot; field with &quot;**frequency**&quot; value, select &quot;**Integer**&quot; option in &quot;**Type**&quot; field and fill in &quot;**Value**&quot; field with &quot;**${frequency}**&quot; value. Click on &quot;**Add attribute**&quot; button again;" loading="lazy"><figcaption>Fill in "**Key**" field with "**frequency**" value, select "**Integer**" option in "**Type**" field and fill in "**Value**" field with "**${frequency}**" value. Click on "**Add attribute**" button again;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-6-ce.webp" alt="Fill in &quot;**Key**&quot; field with &quot;**power**&quot; value, select &quot;**Integer**&quot; option in &quot;**Type**&quot; field and fill in &quot;**Value**&quot; field with &quot;**${power}**&quot; value. Click on &quot;**Apply**&quot; button." loading="lazy"><figcaption>Fill in "**Key**" field with "**power**" value, select "**Integer**" option in "**Type**" field and fill in "**Value**" field with "**${power}**" value. Click on "**Apply**" button.</figcaption></figure></div>

 

  - Click on pencil icon opposite to "**Time series**" subsection and use the following options/values in the opened window:
    - Click on "**Add time series**" button and fill in "**Key**" field with "**temperature**" value, select "**Integer**" option in "**Type**" field and fill in "**Value**" field with "**${temperature}**" value.
    - Click on "**Add time series**" button and fill in "**Key**" field with "**humidity**" value, select "**Integer**" option in "**Type**" field and fill in "**Value**" field with "**${humidity}**" value.
    - Click on "**Apply**" button.
- Click "**Add**" button. Data mapping added.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/data-mapping-7-ce.webp" alt="Click on pencil icon opposite to &quot;**Time series**&quot; subsection;" loading="lazy"><figcaption>Click on pencil icon opposite to "**Time series**" subsection;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-8-ce.webp" alt="Click on &quot;**Add time series**&quot; button;" loading="lazy"><figcaption>Click on "**Add time series**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-9-ce.webp" alt="Fill in &quot;**Key**&quot; field with &quot;**temperature**&quot; value, select &quot;**Integer**&quot; option in &quot;**Type**&quot; field and fill in &quot;**Value**&quot; field with &quot;**${temperature}**&quot; value. Click on &quot;**Add time series**&quot; button again;" loading="lazy"><figcaption>Fill in "**Key**" field with "**temperature**" value, select "**Integer**" option in "**Type**" field and fill in "**Value**" field with "**${temperature}**" value. Click on "**Add time series**" button again;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-10-ce.webp" alt="Fill in &quot;**Key**&quot; field with &quot;**humidity**&quot; value, select &quot;**Integer**&quot; option in &quot;**Type**&quot; field and fill in &quot;**Value**&quot; field with &quot;**${humidity}**&quot; value. Click &quot;**Apply**&quot; button;" loading="lazy"><figcaption>Fill in "**Key**" field with "**humidity**" value, select "**Integer**" option in "**Type**" field and fill in "**Value**" field with "**${humidity}**" value. Click "**Apply**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-11-ce.webp" alt="Click &quot;**Add**&quot; button;" loading="lazy"><figcaption>Click "**Add**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-12-ce.webp" alt="Data mapping added. Click on &quot;**Save**&quot; button." loading="lazy"><figcaption>Data mapping added. Click on "**Save**" button.</figcaption></figure></div>


Following the steps outlined, your gateway will receive and apply the new configuration. 
It will then synchronize its state with the remote server. You can view the synchronization status of the connector configuration in the "**Configuration**" column, which will indicate whether the gateway is successfully aligned with the remote settings.

Also, you can see the connector logs to make sure that the connector works, for this purpose, follow these steps:


1. In the "**General**" connector tab enable remove logging by turning on the "**Enable remote logging**" toggle. Choose "**DEBUG**" in the "**Log level**" drop-down menu. Click on the "**Save**" button to apply changes;

1. Click on logs icon to open connector logs page;

1. You can see the "**Logs**" table that consists of "**Created time**", "**Status**" and "**Message**" columns.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/gateway-getting-started-mqtt-logs-14-ce.webp" alt="In the &quot;**General**&quot; connector tab enable remove logging by turning on the &quot;**Enable remote logging**&quot; toggle. Choose &quot;**DEBUG**&quot; in the &quot;**Log level**&quot; drop-down menu. Click on the &quot;**Save**&quot; button to apply changes;" loading="lazy"><figcaption>In the "**General**" connector tab enable remove logging by turning on the "**Enable remote logging**" toggle. Choose "**DEBUG**" in the "**Log level**" drop-down menu. Click on the "**Save**" button to apply changes;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-mqtt-11-ce.webp" alt="Click on logs icon to open connector logs page;" loading="lazy"><figcaption>Click on logs icon to open connector logs page;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-mqtt-logs-12-ce.webp" alt="You can see the &quot;**Logs**&quot; table that consists of &quot;**Created time**&quot;, &quot;**Status**&quot; and &quot;**Message**&quot; columns." loading="lazy"><figcaption>You can see the "**Logs**" table that consists of "**Created time**", "**Status**" and "**Message**" columns.</figcaption></figure></div>


For now, the gateway is ready to process data through the newly created and configured MQTT connector.

Let's publish data to the MQTT Broker defined in the configuration above, you can follow these steps using a tool like 
**mosquitto_pub** or an MQTT client library in your preferred programming language. In this example, we'll use the 
**mosquitto_pub** command-line tool.

1.Ensure that the Mosquitto MQTT clients are installed on your system. Typically, you can install them using the 
package manager of your operating system:
- For Ubuntu:
  ```bash
  sudo apt-get install mosquitto-clients
  ```
  

- For Windows:

    Download the Mosquitto client tools from [the official website](https://mosquitto.org/download/).

    Install the tools, ensuring that the installation directory is added to the system's PATH.
- For MacOS:
  ```bash
  brew install mosquitto
  ```
  

2.Use the mosquitto_pub command to publish data to a specific MQTT topic. In this case, we'll use the "data/" topic as defined in the configuration:
```bash
mosquitto_pub -h localhost -p 1884 -t data/ -m '{"frequency": 50, "power": 100, "temperature": 25, "humidity": 60}'
```


Where:
- `-h` - specifies the MQTT broker's host address;
- `-p` - specifies the MQTT broker's port;
- `-t` - specifies the MQTT topic to publish to ("data/" in our case);
- `-m` - specifies the payload or message to publish. It should be in JSON format, following the structure defined in the mapping section of your configuration.

Adjust the payload values as needed.


</div>

<div class="st-tab" data-label="Modbus">

Let's add a **Modbus connector**, which will read some data from the demo slave to the 
created gateway.

### Setup demo server

As a demo simulation slave, we will use docker image, that can be installed and run using the following command:

```bash
docker run -it -p 5021:5021 sentient/tb-gw-modbus-server:latest
```


After running docker image, you can see the following logs in your terminal:

![](/images/gateway/dashboard/run-demo-modbus-server.webp)

### Setup connector

This Modbus connector configuration sets up a master to communicate with a slave device located at **"host.docker.internal"** on port 5021 using TCP. 
The configuration includes specifications for data retrieval such as byte and word order, timeout, and polling period. 
The slave device, named **"Demo Device"** is configured to handle Modbus function code 4 requests. 
Attribute and time series mappings are defined for parameters like **frequency**, **power**, **humidity**, and **temperature**. Additionally, settings for connection attempts, retries, and wait times after failed attempts are provided.

To create a connector, follow these steps:


1. Click on "**Connectors configuration**" button on the right panel;

1. Click the "**+ Add connector**" button;

1. Choose "**MODBUS**" connector type from the dropdown, fill in "**Name**" field, choose "**Logging level**" to "**INFO**", turn off the "**Fill configuration with default values**" option and click on "**Add**" button;

1. Connector created.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/gateway-getting-started-7-ce.webp" alt="Click on &quot;**Connectors configuration**&quot; button on the right panel;" loading="lazy"><figcaption>Click on "**Connectors configuration**" button on the right panel;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-8-ce.webp" alt="Click the &quot;**+ Add connector**&quot; button;" loading="lazy"><figcaption>Click the "**+ Add connector**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-modbus-9-ce.webp" alt="Choose &quot;**MODBUS**&quot; connector type from the dropdown, fill in &quot;**Name**&quot; field, choose &quot;**Logging level**&quot; to &quot;**INFO**&quot;, turn off the &quot;**Fill configuration with default values**&quot; option and click on &quot;**Add**&quot; button;" loading="lazy"><figcaption>Choose "**MODBUS**" connector type from the dropdown, fill in "**Name**" field, choose "**Logging level**" to "**INFO**", turn off the "**Fill configuration with default values**" option and click on "**Add**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-modbus-10-ce.webp" alt="Connector created." loading="lazy"><figcaption>Connector created.</figcaption></figure></div>

 

First, we need to add new slave and configure the connection to it. Let's start from the "**Master Connections**" tab. 
This section offers slave adding and detailed connection configuration options that contains several important fields, including connection type, host, port, unit ID, method, and other.

- Go to the "**Master Connections**" tab, and click "**Add Slave**" button;
- Fill in fields with the following values:

| **Field name**    | **Value**            |
|:------------------|:---------------------|
| Server Connection | TCP                  |
| Host              | host.docker.internal |
| Port              | 5021                 |
| Method            | Socket               |
| Unit ID           | 1                    |
| Device name       | Demo Device          |
| Device profile    | default              |
| ---               |                      |


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/add-new-slave-1-ce.webp" alt="Go to the &quot;**Master Connections**&quot; tab, and click &quot;**Add Slave**&quot; button;" loading="lazy"><figcaption>Go to the "**Master Connections**" tab, and click "**Add Slave**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/add-new-slave-2-ce.webp" alt="Fill in the fields with values taken from the documentation." loading="lazy"><figcaption>Fill in the fields with values taken from the documentation.</figcaption></figure></div>


Now, we are ready to move to the "**Attributes**" section. The configuration in this unit provides settings for processing data on Modbus server. These settings will be interpreted in the SENTIENT platform instance as attributes of the device.

Let&#39;s configure attribute section using the following steps:

- Click on "**pencil**" icon in the "**Attributes**" section;
- In the opened window, click on "**Add attribute**" button;
- Fill in the fields:
  - Fill the "**Key**" field with "**frequency**";
  - Select the "**Type**" field to "**16int**";
  - Select the "**Function code**" to "**03 - Read Multiple Holding Registers**";
  - Set "**Objects count**" to "**1**";
  - Set "**Address**" field to "**3**".
  - Enable the "**Modifier**" toggle;
  - In the "**Modifier**" section, set the "**Type**" field to "**divider**";
  - In the "**Modifier**" section, set the "**Value**" field to "**10**".


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/slave-configuration-1-ce.webp" alt="Click on &quot;**pencil**&quot; icon in the &quot;**Attributes**&quot; section;" loading="lazy"><figcaption>Click on "**pencil**" icon in the "**Attributes**" section;</figcaption></figure><figure><img src="/images/gateway/dashboard/slave-configuration-2-ce.webp" alt="In the opened window, click on &quot;**Add attribute**&quot; button;" loading="lazy"><figcaption>In the opened window, click on "**Add attribute**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/slave-configuration-3-ce.webp" alt="Fill in the fields with values taken from the documentation." loading="lazy"><figcaption>Fill in the fields with values taken from the documentation.</figcaption></figure></div>


Let&#39;s add another attribute. Collapse the recently added "frequency" attribute, click the "**Add attribute**" button, and fill in the fields with the following values, using the same process as before:

| **Field name** | **Value** |
|:---------------|:----------|
| Key            | power     |
| Type           | 16int     |
| Function code  | 3         |
| Objects count  | 1         |
| Address        | 2         |
| Modifier       | Divider   |
| Modifier Value | 10        |
| ---            |           |

Click the "**Apply**" button after you&#39;ve completed the "**Attributes**" section configuration.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/slave-configuration-4-ce.webp" alt="Collapse the recently added &quot;**frequency**&quot; attribute, and click &quot;**Add attribute**&quot; button to add another attribute;" loading="lazy"><figcaption>Collapse the recently added "**frequency**" attribute, and click "**Add attribute**" button to add another attribute;</figcaption></figure><figure><img src="/images/gateway/dashboard/slave-configuration-5-ce.webp" alt="Fill in the fields with values taken from the documentation. Then, click &quot;**Apply**&quot;." loading="lazy"><figcaption>Fill in the fields with values taken from the documentation. Then, click "**Apply**".</figcaption></figure></div>


We finish with the "**Attributes**" section, so let&#39;s move to the "**Time series**" section. The configuration in this unit provides settings for processing data on Modbus server. These settings will be interpreted in SENTIENT platform instance as time series of the device.

Let&#39;s configure time series section using the following steps:

- Click on "**pencil**" icon on "**Time series**" section.
- In the opened window, click on "**Add time series**" button;
- Fill in the fields:
  - Fill the "**Key**" field with "**humidity**";
  - Select the "**Type**" field to "**16int**"; 
  - Select the "**Function code**" to "**03 - Read Multiple Holding Registers**";
  - Set "**Objects count**" to "**1**"; 
  - Set "**Address**" field to "**1**".
  - Enable the "**Modifier**" toggle;
  - In the "**Modifier**" section, set the "**Type**" field to "**divider**";
  - In the "**Modifier**" section, set the "**Value**" field to "**10**".


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/slave-configuration-6-ce.webp" alt="Click on the &quot;**pencil**&quot; icon in &quot;**Time series**&quot; section;" loading="lazy"><figcaption>Click on the "**pencil**" icon in "**Time series**" section;</figcaption></figure><figure><img src="/images/gateway/dashboard/slave-configuration-7-ce.webp" alt="In the opened window, click on &quot;**Add time series**&quot; button;" loading="lazy"><figcaption>In the opened window, click on "**Add time series**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/slave-configuration-8-ce.webp" alt="Fill in the fields with values taken from the documentation." loading="lazy"><figcaption>Fill in the fields with values taken from the documentation.</figcaption></figure></div>


Let&#39;s add another time series. Collapse the recently added "**humidity**" time series, click the "**Add time series**" button, and fill in the fields with the following values, using the same process as before:

| **Field name** | **Value**   |
|:---------------|:------------|
| Key            | temperature |
| Type           | 16int       |
| Function code  | 3           |
| Objects count  | 1           |
| Address        | 0           |
| Modifier       | Divider     |
| Modifier Value | 10          |
| ---            |             |


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/slave-configuration-9-ce.webp" alt="Collapse the recently added &quot;**humidity**&quot; time series, and click &quot;**Add time series**&quot; button to add another time series;" loading="lazy"><figcaption>Collapse the recently added "**humidity**" time series, and click "**Add time series**" button to add another time series;</figcaption></figure><figure><img src="/images/gateway/dashboard/slave-configuration-10-ce.webp" alt="Fill in the fields with values taken from the documentation. Then, click &quot;**Apply**&quot;." loading="lazy"><figcaption>Fill in the fields with values taken from the documentation. Then, click "**Apply**".</figcaption></figure></div>


The final view of your configured connector will look like on the following image. Click the "**Add**" button after you&#39;ve completed the configuration.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/final-configured-slave-1-ce.webp" alt="The final view of your configured connector. Click the &quot;**Add**&quot; button after you&#39;ve completed the configuration." loading="lazy"><figcaption>The final view of your configured connector. Click the "**Add**" button after you&#39;ve completed the configuration.</figcaption></figure></div>


Finally, save the Modbus configuration by clicking the "**Save**" button.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/final-configured-slave-2-ce.webp" alt="Finally, the save Modbus configuration by clicking the &quot;**Save**&quot; button." loading="lazy"><figcaption>Finally, the save Modbus configuration by clicking the "**Save**" button.</figcaption></figure></div>


Following the steps outlined, your gateway will receive and apply the new configuration. It will then synchronize its state with the remote server. 
You can view the synchronization status of the connector configuration in the "**Configuration**" column, which will indicate whether the gateway is successfully aligned with the remote settings.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/final-configured-slave-3-ce.webp" alt="You can view the synchronization status of the connector configuration in the &quot;**Configuration**&quot; column, which will indicate whether the gateway is successfully aligned with the remote settings." loading="lazy"><figcaption>You can view the synchronization status of the connector configuration in the "**Configuration**" column, which will indicate whether the gateway is successfully aligned with the remote settings.</figcaption></figure></div>


Also, you can see the connector logs to make sure that the connector works, for this purpose, follow these steps:


1. In the "**General**" connector tab enable remove logging by turning on the "**Enable remote logging**" toggle. Choose "**DEBUG**" in the "**Log level**" drop-down menu. Click on the "**Save**" button to apply changes;

1. Click on "**logs**" icon to open connector logs page;

1. You can see the "**Logs**" table that consists of "**Created time**", "**Status**" and "**Message**" columns.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/gateway-getting-started-modbus-logs-14-ce.webp" alt="In the &quot;**General**&quot; connector tab enable remove logging by turning on the &quot;**Enable remote logging**&quot; toggle. Choose &quot;**DEBUG**&quot; in the &quot;**Log level**&quot; drop-down menu. Click on the &quot;**Save**&quot; button to apply changes;" loading="lazy"><figcaption>In the "**General**" connector tab enable remove logging by turning on the "**Enable remote logging**" toggle. Choose "**DEBUG**" in the "**Log level**" drop-down menu. Click on the "**Save**" button to apply changes;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-modbus-12-ce.webp" alt="Click on &quot;**logs**&quot; icon to open connector logs page;" loading="lazy"><figcaption>Click on "**logs**" icon to open connector logs page;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-modbus-logs-13-ce.webp" alt="You can see the &quot;**Logs**&quot; table that consists of &quot;**Created time**&quot;, &quot;**Status**&quot; and &quot;**Message**&quot; columns." loading="lazy"><figcaption>You can see the "**Logs**" table that consists of "**Created time**", "**Status**" and "**Message**" columns.</figcaption></figure></div>


For now, the gateway is ready to process data through the newly created and configured Modbus connector.

</div>

<div class="st-tab" data-label="OPC-UA">

Let's add an **OPC-UA connector**, which will read some data from the demo server to the 
created gateway.

### Setup demo server

As a demo simulation server, we will use docker image, that can be installed and run using the following command:

```bash
docker run -it -p 4840:4840 sentient/tb-gw-opcua-server:latest
```


After running docker image, you can see the following logs in your terminal:

![](/images/gateway/dashboard/run-demo-opcua-server.webp)

### Setup connector

This OPC-UA connector configuration establishes a connection to a server named **"OPC-UA Demo Server"** at **"opc.tcp://host.docker.internal:4840/freeopcua/server/"**. 
The configuration specifies various settings, including timeouts, scan periods, and security mechanisms such as **"Basic128Rsa15"** with anonymous identity.

The mapping section defines how OPC-UA nodes are mapped to devices and their attributes and time series. In this case, a device with the name **"Demo Device"** and type **"default"** is mapped to nodes under **"`Root\.Objects\.MyObject`"**. 
Attributes such as **frequency** and **power**, as well as time series like **temperature** and **humidity**, are mapped to specific paths in the OPC-UA server. 
Additionally, the configuration supports RPC methods and attribute updates.

To create a connector, follow these steps:


1. Click on "**Connectors configuration**" button on the right panel;

1. Click the "**+ Add connector**" button;

1. Choose "**OPCUA**" connector type from the dropdown, fill in "**Name**" field, choose "**Logging level**" to "**INFO**", turn off the "**Fill configuration with default values**" option and click on "**Add**" button;

1. Connector created.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/gateway-getting-started-7-ce.webp" alt="Click on &quot;**Connectors configuration**&quot; button on the right panel;" loading="lazy"><figcaption>Click on "**Connectors configuration**" button on the right panel;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-8-ce.webp" alt="Click the &quot;**+ Add connector**&quot; button;" loading="lazy"><figcaption>Click the "**+ Add connector**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-opc-ua-9-ce.webp" alt="Choose &quot;**OPCUA**&quot; connector type from the dropdown, fill in &quot;**Name**&quot; field, choose &quot;**Logging level**&quot; to &quot;**INFO**&quot;, turn off the &quot;**Fill configuration with default values**&quot; option and click on &quot;**Add**&quot; button;" loading="lazy"><figcaption>Choose "**OPCUA**" connector type from the dropdown, fill in "**Name**" field, choose "**Logging level**" to "**INFO**", turn off the "**Fill configuration with default values**" option and click on "**Add**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-opc-ua-10-ce.webp" alt="Connector created." loading="lazy"><figcaption>Connector created.</figcaption></figure></div>

 

First, we need to configure the connection to the demo OPC-UA server. Let's start from the "**Server**" tab. 
This section offers detailed connection configuration options and contains several important fields, including server endpoint url, security settings, scan period, poll period, subscriptions settings and other.

- Go to the "**Server**" tab, and fill in the fields with following values:

| **Field name**      | **Value**                                             |
|:--------------------|:------------------------------------------------------|
| Server endpoint url | opc.tcp://host.docker.internal:4840/freeopcua/server/ |
| Enable subscription | false                                                 |
| Security            | Anonymous                                             |
| Poll period         | 5000                                                  |
| Security policy     | Basic128RSA15                                         |
| ---                 |                                                       |


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/server-configuration-1-ce.webp" alt="Go to the &quot;**Server**&quot; tab, and fill in the fields with the value taken from the documentation." loading="lazy"><figcaption>Go to the "**Server**" tab, and fill in the fields with the value taken from the documentation.</figcaption></figure></div>


Now, we are ready to move to the "**Data mapping**" section. This configuration section contains list of nodes that the gateway will subscribe to after connecting to the OPC-UA server, along with settings for processing data from these nodes.

Let&#39;s add new node using the following steps:

- Go to the "**Data mapping**" tab, and click on "**Add mapping**" button.
- In the opened window, fill in the "**Device node**" with "**Path**" type and "`Root\.Objects\.MyObject`" value;
- For "**Device**" subsection use the following options/values:
    - The "**Name**" row: select "**Constant**" in the "**Source**" dropdown field, fill in the "**Value / Expression**" field with the "**Device Demo**" value;
    - The "**Profile name**" row: select "**Constant**" in the "**Source**" dropdown field, fill in the "**Value / Expression**" field with the "**default**" value.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/data-mapping-configuration-1-ce.webp" alt="Go to the &quot;**Data mapping**&quot; tab, and click &quot;**Add mapping**&quot; button;" loading="lazy"><figcaption>Go to the "**Data mapping**" tab, and click "**Add mapping**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-configuration-2-ce.webp" alt="Fill in the fields with values taken from the documentation." loading="lazy"><figcaption>Fill in the fields with values taken from the documentation.</figcaption></figure></div>


Let&#39;s move to "**Attributes**" section to add "frequency" and "power" attributes. The configuration in this unit provides settings for processing data from OPC-UA server. These settings will be interpreted in SENTIENT platform instance as attributes of the device. Also we will use path for finding corresponding node.


<div class="st-callout info">


A **Path** type refers to the hierarchical address within the OPC-UA server's namespace. It is used to navigate to specific nodes in the server. The path for the attribute/time series value can be absolute or relative (relative in our case).


</div>


Let&#39;s configure attribute section using the following steps:

- Click on the "**pencil**" icon in the "**Attributes**" section;
- In the opened window, click on the "**Add attribute**" button;
- Fill in the "**Key**" field with the "**frequency**", select the "**Type**" field to the "**Path**", and fill in the "**Value**" with the "**${Frequency}**".


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/data-mapping-configuration-3-ce.webp" alt="Click on the &quot;**pencil**&quot; icon in the &quot;**Attributes**&quot; section;" loading="lazy"><figcaption>Click on the "**pencil**" icon in the "**Attributes**" section;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-configuration-4-ce.webp" alt="In the opened window, click on the &quot;**Add attribute**&quot; button;" loading="lazy"><figcaption>In the opened window, click on the "**Add attribute**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-configuration-5-ce.webp" alt="Fill in the &quot;**Key**&quot; field with the &quot;**frequency**&quot;, select the &quot;**Type**&quot; field to the &quot;**Path**&quot;, and fill in the &quot;**Value**&quot; with the &quot;**${Frequency}**&quot;." loading="lazy"><figcaption>Fill in the "**Key**" field with the "**frequency**", select the "**Type**" field to the "**Path**", and fill in the "**Value**" with the "**${Frequency}**".</figcaption></figure></div>


Let&#39;s add another attribute. Collapse the recently added "frequency" attribute, click the "**Add attribute**" button, and fill in the fields with the following values, using the same process as before:

| **Field name** | **Value** |
|:---------------|:----------|
| Key            | power     |
| Type           | Path      |
| Value          | ${Power}  |
| ---            |           |

Click the "**Apply**" button after you&#39;ve completed the configuration.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/data-mapping-configuration-6-ce.webp" alt="Collapse the recently added &quot;frequency&quot; attribute, and click &quot;**Add attribute**&quot; button to add another attribute;" loading="lazy"><figcaption>Collapse the recently added "frequency" attribute, and click "**Add attribute**" button to add another attribute;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-configuration-7-ce.webp" alt="Fill in the fields with values taken from the documentation. Then, click &quot;**Apply**&quot;." loading="lazy"><figcaption>Fill in the fields with values taken from the documentation. Then, click "**Apply**".</figcaption></figure></div>


We finish with the "**Attributes**" section, so let&#39;s move to the "**Time series**" section. The configuration in this unit provides settings for processing data from the OPC-UA server. These settings will be interpreted in SENTIENT platform instance as time series of the device.

Let&#39;s configure time series section using the following steps:

- Click on the "**pencil**" icon in the "**Time series**" section;
- In the opened window, click on the "**Add time series**" button;
- Fill in the fields:
  - Fill in the "**Key**" field with the "**temperature**";
  - Select the "**Type**" field to the "**Path**";
  - Fill in the "**Value**" with "**${Temperature}**".


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/data-mapping-configuration-8-ce.webp" alt="Click on the &quot;**pencil**&quot; icon in &quot;**Time series**&quot; section;" loading="lazy"><figcaption>Click on the "**pencil**" icon in "**Time series**" section;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-configuration-9-ce.webp" alt="In the opened window, click on &quot;**Add time series**&quot; button;" loading="lazy"><figcaption>In the opened window, click on "**Add time series**" button;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-configuration-10-ce.webp" alt="Fill in the fields with values taken from the documentation." loading="lazy"><figcaption>Fill in the fields with values taken from the documentation.</figcaption></figure></div>


Let&#39;s add another attribute. Collapse the recently added "**temperature**" time series, click the "**Add time series**" button, and fill in the fields with the following values, using the same process as before:

| **Field name** | **Value**   |
|:---------------|:------------|
| Key            | humidity    |
| Type           | Path        |
| Value          | ${Humidity} |
| ---            |             |


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/data-mapping-configuration-11-ce.webp" alt="Collapse the recently added &quot;**temperature**&quot; time series, and click &quot;**Add time series**&quot; button to add another time series;" loading="lazy"><figcaption>Collapse the recently added "**temperature**" time series, and click "**Add time series**" button to add another time series;</figcaption></figure><figure><img src="/images/gateway/dashboard/data-mapping-configuration-12-ce.webp" alt="Fill in the fields with values taken from the documentation. Then, click &quot;**Apply**&quot;." loading="lazy"><figcaption>Fill in the fields with values taken from the documentation. Then, click "**Apply**".</figcaption></figure></div>


The final view of your configured connector will look like on the following image. Click the "**Add**" button after you&#39;ve completed the configuration.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/final-configured-data-mapping-1-ce.webp" alt="The final view of your configured connector. Click the &quot;**Add**&quot; button after you&#39;ve completed the configuration." loading="lazy"><figcaption>The final view of your configured connector. Click the "**Add**" button after you&#39;ve completed the configuration.</figcaption></figure></div>


Finally, save the OPC-UA configuration by clicking the "**Save**" button.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/final-configured-data-mapping-2-ce.webp" alt="Finally, the save OPC-UA configuration by clicking the &quot;**Save**&quot; button." loading="lazy"><figcaption>Finally, the save OPC-UA configuration by clicking the "**Save**" button.</figcaption></figure></div>


Following the steps outlined, your gateway will receive and apply the new configuration. It will then synchronize its state with the remote server.
You can view the synchronization status of the connector configuration in the "**Configuration**" column, which will indicate whether the gateway is successfully aligned with the remote settings.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/final-configured-data-mapping-3-ce.webp" alt="You can view the synchronization status of the connector configuration in the &quot;**Configuration**&quot; column, which will indicate whether the gateway is successfully aligned with the remote settings." loading="lazy"><figcaption>You can view the synchronization status of the connector configuration in the "**Configuration**" column, which will indicate whether the gateway is successfully aligned with the remote settings.</figcaption></figure></div>


Also, you can see the connector logs to make sure that the connector works, for this purpose, follow these steps:


1. In the "**General**" connector tab enable remove logging by turning on the "**Enable remote logging**" toggle. Choose "**DEBUG**" in the "**Log level**" drop-down menu. Click on the "**Save**" button to apply changes;

1. Click on logs icon to open connector logs page;

1. You can see the "**Logs**" table that consists of "**Created time**", "**Status**" and "**Message**" columns.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/gateway-getting-started-opc-ua-14-ce.webp" alt="In the &quot;**General**&quot; connector tab enable remove logging by turning on the &quot;**Enable remote logging**&quot; toggle. Choose &quot;**DEBUG**&quot; in the &quot;**Log level**&quot; drop-down menu. Click on the &quot;**Save**&quot; button to apply changes;" loading="lazy"><figcaption>In the "**General**" connector tab enable remove logging by turning on the "**Enable remote logging**" toggle. Choose "**DEBUG**" in the "**Log level**" drop-down menu. Click on the "**Save**" button to apply changes;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-opc-ua-12-ce.webp" alt="Click on logs icon to open connector logs page;" loading="lazy"><figcaption>Click on logs icon to open connector logs page;</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-opc-ua-logs-13-ce.webp" alt="You can see the &quot;**Logs**&quot; table that consists of &quot;**Created time**&quot;, &quot;**Status**&quot; and &quot;**Message**&quot; columns." loading="lazy"><figcaption>You can see the "**Logs**" table that consists of "**Created time**", "**Status**" and "**Message**" columns.</figcaption></figure></div>


For now, the gateway is ready to process data through the newly created and configured OPC-UA connector.

</div>

</div>


## Step 4. Check device data

To review the data uploaded from your gateway, use the following steps:


1. Navigate to the **Entities** > **Devices** page and click on the created device. This will open the device details page. From there, switch to the **"Attributes"** tab to view the attributes that were configured in the connector.

1. To view real-time telemetry data from the device, navigate to the "**Latest Telemetry**" tab. Here, you will find the telemetry data being sent by the device, including metrics like "**humidity**" and "**temperature**". This tab provides real-time device telemetry updates.


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/review-gateway-statistics-1-ce.webp" alt="Navigate to the **Entities** > **Devices** page and click on the created device. This will open the device details page. From there, switch to the **&quot;Attributes&quot;** tab to view the attributes that were configured in the connector." loading="lazy"><figcaption>Navigate to the **Entities** > **Devices** page and click on the created device. This will open the device details page. From there, switch to the **"Attributes"** tab to view the attributes that were configured in the connector.</figcaption></figure><figure><img src="/images/gateway/dashboard/review-gateway-statistics-2-ce.webp" alt="To view real-time telemetry data from the device, navigate to the &quot;**Latest Telemetry**&quot; tab. Here, you will find the telemetry data being sent by the device, including metrics like &quot;**humidity**&quot; and &quot;**temperature**&quot;. This tab provides real-time device telemetry updates." loading="lazy"><figcaption>To view real-time telemetry data from the device, navigate to the "**Latest Telemetry**" tab. Here, you will find the telemetry data being sent by the device, including metrics like "**humidity**" and "**temperature**". This tab provides real-time device telemetry updates.</figcaption></figure></div>


## Configure other connectors

After the successful installation and configuration of your first connector, you can configure other connectors to 
connect to different devices. You can find more information about connectors in the following articles:  
 - [**MQTT** connector](/docs/iot-gateway/config/mqtt/)
 - [**OPC-UA** connector](/docs/iot-gateway/config/opc-ua/)
 - [**Modbus** connector](/docs/iot-gateway/config/modbus/)
 - [**BLE** connector](/docs/iot-gateway/config/ble/)
 - [**Request** connector](/docs/iot-gateway/config/request/)
 - [**REST** connector](/docs/iot-gateway/config/rest/)
 - [**CAN** connector](/docs/iot-gateway/config/can/)
 - [**FTP** connector](/docs/iot-gateway/config/ftp/)
 - [**Socket** connector](/docs/iot-gateway/config/socket/)
 - [**XMPP** connector](/docs/iot-gateway/config/xmpp/)
 - [**BACnet** connector](/docs/iot-gateway/config/bacnet/)
 - [**OCPP** connector](/docs/iot-gateway/config/ocpp/)
 - [**ODBC** connector](/docs/iot-gateway/config/odbc/)
 - [**SNMP** connector](/docs/iot-gateway/config/snmp/)
 - [**Custom** connector](/docs/iot-gateway/custom/)

More about *SENTIENT IoT Gateways* Dashboard, you can [read here](/docs/iot-gateway/guides/how-to-enable-remote-configuration/).

## Next steps

Explore guides related to main SENTIENT features:

 - [Data Visualization](/docs/user-guide/visualization/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine/) - how to use rule engine to analyze data from devices.
