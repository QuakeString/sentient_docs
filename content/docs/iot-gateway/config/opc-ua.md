+++
title = "OPC-UA Connector Configuration"
description = "OPC-UA protocol support for SENTIENT IoT Gateway"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/config/opc-ua.md"
+++
## Overview

This documentation will help you set up the OPC-UA connector for the SENTIENT IoT Gateway. We'll explain the configuration 
parameters in simple terms to make it easy for you to understand and follow. The OPC-UA (Open Platform Communications 
Unified Architecture) is a machine-to-machine communication protocol for industrial automation, and this connector 
allows seamless integration with the SENTIENT platform. Use 
[general configuration](/docs/iot-gateway/configuration/) to enable this connector.

Also, if you are new to SENTIENT IoT Gateway, we recommend you to read the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) 
guide to understand the basic concepts of SENTIENT IoT Gateway and how it works with OPC-UA protocol.

The connector can be configured via the user interface form, which helps you set up a connection to the OPC-UA server, 
collect data and write data to nodes. Let's look at all the available settings and explain each one clearly. 
This will help you understand how everything works.


<div class="st-callout info">


**Please note:**
To access the actual UI for the gateway - you need to a have connected gateway before adding a connector. Otherwise, you will see the old UI.


</div>


## Configuration modes

The OPC-UA connector can be configured in two modes: **Basic** and **Advanced**.
- **Basic** mode is designed for users who are new to SENTIENT IoT Gateway and want to quickly set up the connector with minimal configuration. It provides a simplified interface with essential settings.
- **Advanced** mode is intended for experienced users who need more control over the configuration. It offers additional options and flexibility for advanced use cases.


<div class="st-callout info">


**Please note:**
If you are new to IoT Gateway, use the "Basic" configuration mode. If you are familiar with configuring IoT Gateway, 
you can use the "Advanced" configuration mode.


</div>


You can switch between these modes using the toggle button at the top of the configuration page:

![image](/images/gateway/opc-ua-connector/opc-ua-modes-toggle.webp)

## General settings

This configuration section contains general connector settings, such as:

- **Name** - connector name used for logs and saving to persistent devices;
- **Logs configuration** - settings for local and remote logging:
  - **Enable remote logging** - enables remote logging for the connector;
  - **Logging level** - logging level for local and remote logs: NONE, ERROR, CRITICAL, WARNING, INFO, DEBUG, TRACE;
- **Report strategy** - strategy for sending data to SENTIENT:
  - **Report period** - period for sending data to SENTIENT in milliseconds;
  - **Type** - type of the report strategy:
    - **On report period** - sends data to SENTIENT after the report period;
    - **On value change** - sends data to SENTIENT when the value changes;
    - **On value change or report period** - sends data to SENTIENT when the value changes or after the report period;
    - **On received** - sends data to SENTIENT after receiving data from the device (default strategy).


<div class="st-callout info">


Additional information about the report strategy can be found [here](/docs/iot-gateway/features-overview/report-strategy).


</div>


![image](/images/gateway/opc-ua-connector/opc-ua-general-basic-1-ce.webp)


<div class="st-callout info">


The General tab in settings is the same for both the basic and advanced configurations.


</div>


## Connection settings

Connection settings define how the OPC-UA connector establishes and maintains communication with the OPC-UA 
server. These settings cover the basic connection parameters, server discovery behavior, security configuration, and 
authentication modes.

### Server

This subsection specifies the target OPC-UA server and how the gateway interacts with it. It includes the server’s 
URL, timeout settings, scan intervals, and the option to use either subscriptions or polling to monitor 
data nodes.

This configuration section contains settings of the OPC-UA server connection, such as:
- **Server endpoint url** - hostname or ip address of OPC-UA server;
- **Timeout in milliseconds** - timeout in milliseconds for connecting to OPC-UA server;
- **Security policy** - security policy (**Basic128Rsa15**, **Basic256**, **Basic256Sha256**);
- **Scan period in milliseconds** - period in milliseconds to rescan the server;
- **Poll period** - period in milliseconds to poll the server;
- **Subscription check period in milliseconds** - period to check the subscriptions in the OPC-UA server;
- **Enable subscription** - if true - the gateway will subscribe to interesting nodes and wait for data update and if false - the gateway will rescan OPC-UA server every **scanPeriodInMillis**;
- **Show map** - show nodes on scanning **true** or **false**.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/opc-ua/#advanced-configuration) section.


</div>


![image](/images/gateway/opc-ua-connector/opc-ua-application-basic-certificates-1-ce.webp)


### Security

OPC-UA server connections offer three distinct security types:


1. **Anonymous** - the simplest option of identity;

1. **Basic** - using this option, you can provide the username and password to connect to the OPC-UA server;

1. **Certificates** - the safest option of identity. Using this option, you can also provide path on machine with the gateway to certificate, private key and CA certificate. Optionally, you can provide the username/password pair.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/opc-ua-application-basic-anonymous-1-ce.webp" alt="**Anonymous** - the simplest option of identity;" loading="lazy"><figcaption>**Anonymous** - the simplest option of identity;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-application-basic-basic-1-ce.webp" alt="**Basic** - using this option, you can provide the username and password to connect to the OPC-UA server;" loading="lazy"><figcaption>**Basic** - using this option, you can provide the username and password to connect to the OPC-UA server;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-application-basic-certificates-2-ce.webp" alt="**Certificates** - the safest option of identity. Using this option, you can also provide path on machine with the gateway to certificate, private key and CA certificate. Optionally, you can provide the username/password pair." loading="lazy"><figcaption>**Certificates** - the safest option of identity. Using this option, you can also provide path on machine with the gateway to certificate, private key and CA certificate. Optionally, you can provide the username/password pair.</figcaption></figure></div>


## Data mapping

Data mapping is a section that allows you to configure which node from the OPC-UA server will be assigned to which 
device in SENTIENT.
You can also use this section to configure which data will be sent as device attributes or telemetry.
Data mapping contains all the necessary settings for flexible device and data management.

The following parameters are used to configure the base node of the device, its name and profile, as well as for 
report strategy:
- **Device node** - the base node for the device. Paths to the device name, profile, attributes, and telemetry can be specified relative to this node.
- **Device name** - the name of the device in SENTIENT. It can be specified as a path or identifier to the node or as a static value (more information about types can be found in the [Additional information](/docs/iot-gateway/config/opc-ua/#additional-information) section).
- **Device profile** - the profile of the device in SENTIENT. It can be specified as a path or identifier to the node or as a static value (more information about types can be found in the [Additional information](/docs/iot-gateway/config/opc-ua/#additional-information) section).
- **Report strategy** - strategy for sending data to SENTIENT:
  - **Report period** - period for sending data to SENTIENT in milliseconds;
  - **Type** - type of the report strategy:
    - **On report period** - sends data to SENTIENT after the report period;
    - **On value change** - sends data to SENTIENT when the value changes;
    - **On value change or report period** - sends data to SENTIENT when the value changes or after the report
      period;
    - **On received** - sends data to SENTIENT after receiving data from the device (default strategy).

![image](/images/gateway/opc-ua-connector/opc-ua-data-mapping-overview.webp)

To add a new device, use the following steps:


1. Click the **+ Add mapping** button.

1. Provide the following fields in the opened model window: Device node, Device name and Profile name (all of them can be `path` or `identifier`).


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/adding-device-1.webp" alt="Click the **+ Add mapping** button." loading="lazy"><figcaption>Click the **+ Add mapping** button.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/adding-device-2.webp" alt="Provide the following fields in the opened model window: Device node, Device name and Profile name (all of them can be `path` or `identifier`)." loading="lazy"><figcaption>Provide the following fields in the opened model window: Device node, Device name and Profile name (all of them can be `path` or `identifier`).</figcaption></figure></div>


<div class="st-callout info">


Additional information about the report strategy can be found [here](/docs/iot-gateway/features-overview/report-strategy).

All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/opc-ua/#device-mapping) section.

More usage examples can be found in the [Usage examples](/docs/iot-gateway/config/opc-ua/#usage-examples) section.


</div>


### Subsection "Attributes" and "Time series"

The configuration in this subsection provides settings for processing data from the OPC-UA node. These settings will be 
interpreted in SENTIENT platform instance as attributes/time series of the device.

The following parameters are used to configure device attributes and time series:
- **Key** - the key of the attribute/time series in SENTIENT. It can be specified as a static value.
- **Type** - the type of expression in the **Value** field (more information about types can be found in the [Additional information](/docs/iot-gateway/config/opc-ua/#additional-information) section):
  - **[Path](/docs/iot-gateway/config/opc-ua/#path-types)** - can be absolute or relative path to the node in the OPC-UA server. The value will be taken from the node with the specified path.
  - **[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)** - can be numeric, string, byte string or GUID identifier of the node in the OPC-UA server. The value will be taken from the node with the specified identifier.
  - **Constant** - a static value that will be sent to the device as an attribute/time series key.
- **Value** - the value of the attribute/time series that will be sent to the platform device. It should be specified depending on the selected type (Path, Identifier or Constant).


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/opc-ua/#device-attributes-and-telemetry) section.

More usage examples can be found in the [Usage examples](/docs/iot-gateway/config/opc-ua/#usage-examples) section.


</div>


![image](/images/gateway/opc-ua-connector/opc-ua-attributes-timeseries-overview.webp)

To add new time series or attribute key, follow these steps:


1. Click the “**pencil**” icon in the “**Attributes**” section to add new attribute key;

1. Click on "**Add attribute**" in the opened window;

1. Enter the "**Key**" field, select the "**Type**" (can be [path](#path-types), [identifier](#identifier-types) or constant), enter "**Value**" and click "**Apply**" button;

1. Now click on the “**pencil**” icon in the “**Time series**” section to add new time series key;

1. Click on "**Add time series**" in the opened window;

1. Enter the "**Key**" field, select the "**Type**" (can be [path](#path-types), [identifier](#identifier-types) or constant), enter "**Value**" and click "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-3-ce.webp" alt="Click the “**pencil**” icon in the “**Attributes**” section to add new attribute key;" loading="lazy"><figcaption>Click the “**pencil**” icon in the “**Attributes**” section to add new attribute key;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-4-ce.webp" alt="Click on &quot;**Add attribute**&quot; in the opened window;" loading="lazy"><figcaption>Click on "**Add attribute**" in the opened window;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-5-ce.webp" alt="Enter the &quot;**Key**&quot; field, select the &quot;**Type**&quot; (can be [path](#path-types), [identifier](#identifier-types) or constant), enter &quot;**Value**&quot; and click &quot;**Apply**&quot; button;" loading="lazy"><figcaption>Enter the "**Key**" field, select the "**Type**" (can be [path](#path-types), [identifier](#identifier-types) or constant), enter "**Value**" and click "**Apply**" button;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-6-ce.webp" alt="Now click on the “**pencil**” icon in the “**Time series**” section to add new time series key;" loading="lazy"><figcaption>Now click on the “**pencil**” icon in the “**Time series**” section to add new time series key;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-7-ce.webp" alt="Click on &quot;**Add time series**&quot; in the opened window;" loading="lazy"><figcaption>Click on "**Add time series**" in the opened window;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-8-ce.webp" alt="Enter the &quot;**Key**&quot; field, select the &quot;**Type**&quot; (can be [path](#path-types), [identifier](#identifier-types) or constant), enter &quot;**Value**&quot; and click &quot;**Apply**&quot; button." loading="lazy"><figcaption>Enter the "**Key**" field, select the "**Type**" (can be [path](#path-types), [identifier](#identifier-types) or constant), enter "**Value**" and click "**Apply**" button.</figcaption></figure></div>


You can enable a specific report strategy for each time series or attribute. This strategy defines how often  
data is sent to the SENTIENT server. The following strategies are available:

- **On report period** - sends data to SENTIENT after the report period;
- **On value change** - sends data to SENTIENT when the value changes;
- **On value change or report period** - sends data to SENTIENT when the value changes or after the report period;
- **On received** - sends data to SENTIENT after receiving data from the device (default strategy).


<div class="st-callout info">


Additional information about the report strategy can be found [here](/docs/iot-gateway/features-overview/report-strategy).


</div>


![image](/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-10-ce.webp)


### Usage examples


<div class="st-tabs">

<div class="st-tab" data-label="Device name/profile with Absolute Path">

The device name and profile can be set dynamically using node values. In this example, we will use an 
[absolute path](/docs/iot-gateway/config/opc-ua/#absolute-path) to specify the device name and profile.

As an example, we will use Prosys OPC-UA Simulation Server, which is available at
`opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`. The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview.webp)

We are interested in nodes: "**DeviceModelName**" and "**DeviceSeries**". We will use these nodes to set the device name
and profile, respectively.

Let's configure the device name and profile in the OPC-UA connector. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created OPC-UA connector, click on the "**Data mapping**" tab. Firstly, we need to configure parent (or device) node. Click on the "**+ Add mapping**" button.

1. In the opened window, fill in "**Device node**" field with `Root\.Objects\.DemoDevice`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" in "**Source**" field. This is an absolute path to the parent node of the device we want to create.

1. In the "**Name**" field, enter `${Root\.Objects\.DemoDeviceInfo\.DeviceModelName}`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" in "**Source**" field. This is an absolute path to the node that contains the device name.

1. In the "**Profile name**" field, enter `${Root\.Objects\.DemoDeviceInfo\.DeviceSeries}`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" in "**Source**" field. This is an absolute path to the node that contains the device profile.

1. Also, we need to add one attribute/time series because the connector will not add a device without any data to read (you can use any pre-installed Prosys OPC-UA Simulation Server node). Click on the "**pencil**" icon next to the "**Attributes**" section.

1. In the opened window, click on the "**Add attribute**" button and fill the fields as on the corresponding image.

1. Remember to save your changes by clicking the "**Save**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the right sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-3.webp" alt="Select the created OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Firstly, we need to configure parent (or device) node. Click on the &quot;**+ Add mapping**&quot; button." loading="lazy"><figcaption>Select the created OPC-UA connector, click on the "**Data mapping**" tab. Firstly, we need to configure parent (or device) node. Click on the "**+ Add mapping**" button.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-4.webp" alt="In the opened window, fill in &quot;**Device node**&quot; field with `Root\.Objects\.DemoDevice`, also select &quot;**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**&quot; in &quot;**Source**&quot; field. This is an absolute path to the parent node of the device we want to create." loading="lazy"><figcaption>In the opened window, fill in "**Device node**" field with `Root\.Objects\.DemoDevice`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" in "**Source**" field. This is an absolute path to the parent node of the device we want to create.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-5.webp" alt="In the &quot;**Name**&quot; field, enter `${Root\.Objects\.DemoDeviceInfo\.DeviceModelName}`, also select &quot;**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**&quot; in &quot;**Source**&quot; field. This is an absolute path to the node that contains the device name." loading="lazy"><figcaption>In the "**Name**" field, enter `${Root\.Objects\.DemoDeviceInfo\.DeviceModelName}`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" in "**Source**" field. This is an absolute path to the node that contains the device name.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-6.webp" alt="In the &quot;**Profile name**&quot; field, enter `${Root\.Objects\.DemoDeviceInfo\.DeviceSeries}`, also select &quot;**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**&quot; in &quot;**Source**&quot; field. This is an absolute path to the node that contains the device profile." loading="lazy"><figcaption>In the "**Profile name**" field, enter `${Root\.Objects\.DemoDeviceInfo\.DeviceSeries}`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" in "**Source**" field. This is an absolute path to the node that contains the device profile.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-7.webp" alt="Also, we need to add one attribute/time series because the connector will not add a device without any data to read (you can use any pre-installed Prosys OPC-UA Simulation Server node). Click on the &quot;**pencil**&quot; icon next to the &quot;**Attributes**&quot; section." loading="lazy"><figcaption>Also, we need to add one attribute/time series because the connector will not add a device without any data to read (you can use any pre-installed Prosys OPC-UA Simulation Server node). Click on the "**pencil**" icon next to the "**Attributes**" section.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-8.webp" alt="In the opened window, click on the &quot;**Add attribute**&quot; button and fill the fields as on the corresponding image." loading="lazy"><figcaption>In the opened window, click on the "**Add attribute**" button and fill the fields as on the corresponding image.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-9.webp" alt="Remember to save your changes by clicking the &quot;**Save**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Save**" button.</figcaption></figure></div>


Now we can check if the device name and profile are set correctly. Go to "**Entities**" > "**Devices**" and as you can see, the device
name is set to `Demo Device` and the profile is set to `Demo Series`.

![image](/images/gateway/opc-ua-connector/examples/result-device-overview.webp)

If you are using advanced configuration mode and want to set the device name and profile using an absolute path, you can
use the following configuration:

```json
{
  "name": "OPC-UA",
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "pollPeriodInMillis": 5000,
    "enableSubscriptions": false,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    }
  },
  "mapping": [
    {
      "deviceNodeSource": "path",
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceInfo": {
        "deviceNameExpression": "${Root\\.Objects\\.DemoDeviceInfo\\.DeviceModelName}",
        "deviceNameExpressionSource": "path",
        "deviceProfileExpressionSource": "path",
        "deviceProfileExpression": "${Root\\.Objects\\.DemoDeviceInfo\\.DeviceSeries}"
      },
      "attributes": [
        {
          "key": "some_key",
          "type": "identifier",
          "value": "${ns=3;i=1001}"
        }
      ],
      "timeseries": [],
      "rpc_methods": [],
      "attributes_updates": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="Device name/profile with Relative Path">

The device name and profile can be set dynamically using node values. In this example, we will use a 
[relative path](/docs/iot-gateway/config/opc-ua/#relative-path) to specify the device name and profile.

As an example, we will use Prosys OPC-UA Simulation Server, which is available at
`opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`. The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview-1.webp)

We are interested in nodes: "**DeviceModelName**" and "**DeviceSeries**". We will use these nodes to set the device name
and profile, respectively.

Let's configure the device name and profile in the OPC-UA connector. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created OPC-UA connector, click on the "**Data mapping**" tab. Firstly, we need to configure parent (or device) node. Click on the "**+ Add mapping**" button.

1. In the opened window, fill in "Device node" field with `Root\.Objects\.DemoDevice`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**" in "**Source**" field. This is an absolute path to the parent node of the device we want to create.

1. In the "**Name**" field, enter `${DeviceModelName}`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**" in "**Source**" field. This is a relative path to the node that contains the device name.

1. In the "**Profile name**" field, enter `${DeviceSeries}`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**" in "**Source**" field. This is a relative path to the node that contains the device profile.

1. Also, we need to add one attribute/time series because the connector will not add a device without any data to read (you can use any pre-installed Prosys OPC-UA Simulation Server node). Click on the "**pencil**" icon next to the "**Attributes**" section.

1. In the opened window, click on the "**Add attribute**" button and fill the fields as on the corresponding image.

1. Remember to save your changes by clicking the "**Save**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the right sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-3.webp" alt="Select the created OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Firstly, we need to configure parent (or device) node. Click on the &quot;**+ Add mapping**&quot; button." loading="lazy"><figcaption>Select the created OPC-UA connector, click on the "**Data mapping**" tab. Firstly, we need to configure parent (or device) node. Click on the "**+ Add mapping**" button.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-4.webp" alt="In the opened window, fill in &quot;Device node&quot; field with `Root\.Objects\.DemoDevice`, also select &quot;**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**&quot; in &quot;**Source**&quot; field. This is an absolute path to the parent node of the device we want to create." loading="lazy"><figcaption>In the opened window, fill in "Device node" field with `Root\.Objects\.DemoDevice`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**" in "**Source**" field. This is an absolute path to the parent node of the device we want to create.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-relative-path-5.webp" alt="In the &quot;**Name**&quot; field, enter `${DeviceModelName}`, also select &quot;**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**&quot; in &quot;**Source**&quot; field. This is a relative path to the node that contains the device name." loading="lazy"><figcaption>In the "**Name**" field, enter `${DeviceModelName}`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**" in "**Source**" field. This is a relative path to the node that contains the device name.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-relative-path-6.webp" alt="In the &quot;**Profile name**&quot; field, enter `${DeviceSeries}`, also select &quot;**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**&quot; in &quot;**Source**&quot; field. This is a relative path to the node that contains the device profile." loading="lazy"><figcaption>In the "**Profile name**" field, enter `${DeviceSeries}`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**" in "**Source**" field. This is a relative path to the node that contains the device profile.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-relative-path-7.webp" alt="Also, we need to add one attribute/time series because the connector will not add a device without any data to read (you can use any pre-installed Prosys OPC-UA Simulation Server node). Click on the &quot;**pencil**&quot; icon next to the &quot;**Attributes**&quot; section." loading="lazy"><figcaption>Also, we need to add one attribute/time series because the connector will not add a device without any data to read (you can use any pre-installed Prosys OPC-UA Simulation Server node). Click on the "**pencil**" icon next to the "**Attributes**" section.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-8.webp" alt="In the opened window, click on the &quot;**Add attribute**&quot; button and fill the fields as on the corresponding image." loading="lazy"><figcaption>In the opened window, click on the "**Add attribute**" button and fill the fields as on the corresponding image.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-relative-path-9.webp" alt="Remember to save your changes by clicking the &quot;**Save**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Save**" button.</figcaption></figure></div>


Now we can check if the device name and profile are set correctly. Go to "**Entities**" > "**Devices**" and as you can see, the device
name is set to `Demo Device` and the profile is set to `Demo Series`.

![image](/images/gateway/opc-ua-connector/examples/result-device-overview.webp)

If you are using advanced configuration mode and want to set the device name and profile using a relative path, you can
use the following configuration:

```json
{
  "name": "OPCUA",
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "pollPeriodInMillis": 5000,
    "enableSubscriptions": false,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    }
  },
  "mapping": [
    {
      "deviceNodeSource": "path",
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceInfo": {
        "deviceNameExpression": "${DeviceModelName}",
        "deviceNameExpressionSource": "path",
        "deviceProfileExpressionSource": "path",
        "deviceProfileExpression": "${DeviceSeries}"
      },
      "attributes": [
        {
          "key": "some_key",
          "type": "identifier",
          "value": "${ns=3;i=1001}"
        }
      ],
      "timeseries": [],
      "rpc_methods": [],
      "attributes_updates": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="Device name/profile with Identifier">

The device name and profile can be set dynamically using node values. In this example, we will use identifier to
specify the device name and profile. [Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types) can be **numeric**,
**string**, **byte string** or **GUID** identifier of the node in the OPC-UA server.

As an example, we will use Prosys OPC-UA Simulation Server, which is available at
`opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`. The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview.webp)

We are interested in nodes: "**DeviceModelName**" that have `ns=3;i=1014` identifier and "**DeviceSeries**" that 
have `ns=3;i=1015` identifier. We will use these nodes to set the device name and profile, respectively.

Let's configure the device name and profile in the OPC-UA connector. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created OPC-UA connector, click on the "**Data mapping**" tab. Firstly, we need to configure parent (or device) node. Click on the "**+ Add mapping**" button.

1. In the opened window, fill in "**Device node**" field with `Root\.Objects\.DemoDevice`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" in "**Source**" field. This is an absolute path to the parent node of the device we want to create.

1. In the "**Name**" field, enter `${ns=3;i=1014}`, also select "**[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)**" in "**Source**" field.

1. In the "**Profile name**" field, enter `${ns=3;i=1015}`, also select "**[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)**" in "**Source**" field. This is an absolute path to the node that contains the device profile.

1. Also, we need to add one attribute/time series because the connector will not add a device without any data to read (you can use any pre-installed Prosys OPC-UA Simulation Server node). Click on the "**pencil**" icon next to the "**Attributes**" section.

1. In the opened window, click on the "**Add attribute**" button and fill the fields as on the corresponding image.

1. Remember to save your changes by clicking the "**Save**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the right sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-3.webp" alt="Select the created OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Firstly, we need to configure parent (or device) node. Click on the &quot;**+ Add mapping**&quot; button." loading="lazy"><figcaption>Select the created OPC-UA connector, click on the "**Data mapping**" tab. Firstly, we need to configure parent (or device) node. Click on the "**+ Add mapping**" button.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-4.webp" alt="In the opened window, fill in &quot;**Device node**&quot; field with `Root\.Objects\.DemoDevice`, also select &quot;**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**&quot; in &quot;**Source**&quot; field. This is an absolute path to the parent node of the device we want to create." loading="lazy"><figcaption>In the opened window, fill in "**Device node**" field with `Root\.Objects\.DemoDevice`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" in "**Source**" field. This is an absolute path to the parent node of the device we want to create.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-identifier-path-5.webp" alt="In the &quot;**Name**&quot; field, enter `${ns=3;i=1014}`, also select &quot;**[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)**&quot; in &quot;**Source**&quot; field." loading="lazy"><figcaption>In the "**Name**" field, enter `${ns=3;i=1014}`, also select "**[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)**" in "**Source**" field.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-identifier-path-6.webp" alt="In the &quot;**Profile name**&quot; field, enter `${ns=3;i=1015}`, also select &quot;**[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)**&quot; in &quot;**Source**&quot; field. This is an absolute path to the node that contains the device profile." loading="lazy"><figcaption>In the "**Profile name**" field, enter `${ns=3;i=1015}`, also select "**[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)**" in "**Source**" field. This is an absolute path to the node that contains the device profile.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-identifier-path-7.webp" alt="Also, we need to add one attribute/time series because the connector will not add a device without any data to read (you can use any pre-installed Prosys OPC-UA Simulation Server node). Click on the &quot;**pencil**&quot; icon next to the &quot;**Attributes**&quot; section." loading="lazy"><figcaption>Also, we need to add one attribute/time series because the connector will not add a device without any data to read (you can use any pre-installed Prosys OPC-UA Simulation Server node). Click on the "**pencil**" icon next to the "**Attributes**" section.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-8.webp" alt="In the opened window, click on the &quot;**Add attribute**&quot; button and fill the fields as on the corresponding image." loading="lazy"><figcaption>In the opened window, click on the "**Add attribute**" button and fill the fields as on the corresponding image.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-identifier-path-9.webp" alt="Remember to save your changes by clicking the &quot;**Save**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Save**" button.</figcaption></figure></div>


Now we can check if the device name and profile are set correctly. Go to "**Entities**" > "**Devices**" and as you can see, the device
name is set to `Demo Device` and the profile is set to `Demo Series`.

![image](/images/gateway/opc-ua-connector/examples/result-device-overview.webp)

If you are using advanced configuration mode and want to set the device name and profile using an identifier, you can
use the following configuration:

```json
{
  "name": "OPCUA",
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "pollPeriodInMillis": 5000,
    "enableSubscriptions": false,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    }
  },
  "mapping": [
    {
      "deviceNodeSource": "path",
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceInfo": {
        "deviceNameExpression": "${ns=3;i=1014}",
        "deviceNameExpressionSource": "identifier",
        "deviceProfileExpressionSource": "identifier",
        "deviceProfileExpression": "${ns=3;i=1015}"
      },
      "attributes": [
        {
          "key": "some_key",
          "type": "identifier",
          "value": "${ns=3;i=1003}"
        }
      ],
      "timeseries": [],
      "rpc_methods": [],
      "attributes_updates": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="Attributes/Time series with Relative Path">

Attributes and time series data can be accessed using [relative paths](/docs/iot-gateway/config/opc-ua/#relative-path)
in the OPC UA Connector. This allows you to retrieve data without needing to specify the full path to the node.

As an example, we will use Prosys OPC-UA Simulation Server, which is available at
`opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`. The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview-2.webp)

We are interested in node "**Humidity**". We will use this node to retrieve the humidity data.

Let's configure the humidity data in the OPC-UA connector. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the OPC-UA connector, click on the "**Data mapping**" tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples).

1. In the opened data mapping windows, click on the "**pencil**" icon next to the "**Time series**" or "**Attributes**" section.

1. Click on the "**Add time series**" button. Fill in the "**Key**" field with `Humidity`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**" in "**Type**" field, and fill in the "**Value**" field with `${Humidity}`. This is a relative path to the node that contains the humidity data.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the right sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-absolute-path-1.webp" alt="Select the OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples)." loading="lazy"><figcaption>Select the OPC-UA connector, click on the "**Data mapping**" tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples).</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-absolute-path-2.webp" alt="In the opened data mapping windows, click on the &quot;**pencil**&quot; icon next to the &quot;**Time series**&quot; or &quot;**Attributes**&quot; section." loading="lazy"><figcaption>In the opened data mapping windows, click on the "**pencil**" icon next to the "**Time series**" or "**Attributes**" section.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-relative-path-3.webp" alt="Click on the &quot;**Add time series**&quot; button. Fill in the &quot;**Key**&quot; field with `Humidity`, also select &quot;**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**&quot; in &quot;**Type**&quot; field, and fill in the &quot;**Value**&quot; field with `${Humidity}`. This is a relative path to the node that contains the humidity data." loading="lazy"><figcaption>Click on the "**Add time series**" button. Fill in the "**Key**" field with `Humidity`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**" in "**Type**" field, and fill in the "**Value**" field with `${Humidity}`. This is a relative path to the node that contains the humidity data.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-absolute-path-4.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


Now we can check if the humidity data is sending correctly. Go to "**Entities**" > "**Devices**", select a created device and as you
can see, the humidity data is available in the "**Time series**" section:

![image](/images/gateway/opc-ua-connector/examples/result-device-overview-1.webp)

If you are using advanced configuration mode and want to set the humidity data using a relative path, you can 
use the following configuration:

```json
{
  "name": "OPCUA",
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "pollPeriodInMillis": 5000,
    "enableSubscriptions": false,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    }
  },
  "mapping": [
    {
      "deviceNodeSource": "path",
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpressionSource": "constant",
        "deviceProfileExpression": "default"
      },
      "attributes": [],
      "timeseries": [
        {
          "key": "Humidity",
          "type": "path",
          "value": "${Humidity}"
        }
      ],
      "rpc_methods": [],
      "attributes_updates": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="Attributes/Time series with Relative Path and Identifier device node">

Attributes and time series data can be accessed using [relative paths](/docs/iot-gateway/config/opc-ua/#relative-path)
in the OPC UA Connector. This allows you to retrieve data without needing to specify the full path to the node.
Additionally, we may use [identifiers](/docs/iot-gateway/config/opc-ua/#identifier-types) for "**Device node**".
 
As an example, we will use Prosys OPC-UA Simulation Server, which is available at
`opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`. The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview-2.webp)


We are interested in node "**Humidity**". We will use this node to retrieve the humidity data.

Let's configure the humidity data in the OPC-UA connector, using [relative paths](/docs/iot-gateway/config/opc-ua/#relative-path).
For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the OPC-UA connector, click on the "**Data mapping**" tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples).

1. In the opened data mapping windows, click on the "**pencil**" icon next to the "**Time series**" or "**Attributes**" section.

1. Click on the "**Add time series**" button. Fill in the "**Key**" field with `Humidity`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**" in "**Type**" field, and fill in the "**Value**" field with `${Humidity}`. This is a relative path to the node that contains the humidity data.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the left sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-relative-path-device-identifier-1.webp" alt="Select the OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples)." loading="lazy"><figcaption>Select the OPC-UA connector, click on the "**Data mapping**" tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples).</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-relative-path-device-identifier-2.webp" alt="In the opened data mapping windows, click on the &quot;**pencil**&quot; icon next to the &quot;**Time series**&quot; or &quot;**Attributes**&quot; section." loading="lazy"><figcaption>In the opened data mapping windows, click on the "**pencil**" icon next to the "**Time series**" or "**Attributes**" section.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-relative-path-3.webp" alt="Click on the &quot;**Add time series**&quot; button. Fill in the &quot;**Key**&quot; field with `Humidity`, also select &quot;**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**&quot; in &quot;**Type**&quot; field, and fill in the &quot;**Value**&quot; field with `${Humidity}`. This is a relative path to the node that contains the humidity data." loading="lazy"><figcaption>Click on the "**Add time series**" button. Fill in the "**Key**" field with `Humidity`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#relative-path)**" in "**Type**" field, and fill in the "**Value**" field with `${Humidity}`. This is a relative path to the node that contains the humidity data.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-relative-path-device-identifier-3.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


Now we can check if the humidity data is sending correctly. Go to "**Entities**" > "**Devices**", select a created device and as you
can see, the humidity data is available in the "**Time series**" section:

![image](/images/gateway/opc-ua-connector/examples/result-device-overview-relative-path-device-identifier.webp)

If you are using advanced configuration mode and want to set the humidity data using a relative path, you can 
use the following configuration:

```json
{
  "name": "OPCUA",
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "pollPeriodInMillis": 5000,
    "enableSubscriptions": false,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    }
  },
  "mapping": [
    {
      "deviceNodeSource": "identifier",
      "deviceNodePattern": "ns=3;i=1008",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpressionSource": "constant",
        "deviceProfileExpression": "default"
      },
      "attributes": [],
      "timeseries": [
        {
          "key": "Humidity",
          "type": "path",
          "value": "${Humidity}"
        }
      ],
      "rpc_methods": [],
      "attributes_updates": []
    }
  ]
}
```

</div>

<div class="st-tab" data-label="Attributes/Time series with Absolute Path">

Attributes and time series data can be accessed using [absolute paths](/docs/iot-gateway/config/opc-ua/#absolute-path)
in the OPC UA Connector. This will allow you to get data from a node that does not refer to the parent (device) node.

As an example, we will use Prosys OPC-UA Simulation Server, which is available at
`opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`. The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview-2.webp)

We are interested in node "**Humidity**". We will use this node to retrieve the humidity data.

Let's configure the humidity data in the OPC-UA connector. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the OPC-UA connector, click on the "**Data mapping**" tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples).

1. In the opened data mapping windows, click on the "**pencil**" icon next to the "**Time series**" or "**Attributes**" section.

1. Click on the "**Add time series**" button. Fill in the "**Key**" field with `Humidity`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" in "**Type**" field, and fill in the "**Value**" field with `${Root\.Objects\.DemoDevice\.Humidity}`. This is an absolute path to the node that contains the humidity data.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the right sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-absolute-path-1.webp" alt="Select the OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples)." loading="lazy"><figcaption>Select the OPC-UA connector, click on the "**Data mapping**" tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples).</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-absolute-path-2.webp" alt="In the opened data mapping windows, click on the &quot;**pencil**&quot; icon next to the &quot;**Time series**&quot; or &quot;**Attributes**&quot; section." loading="lazy"><figcaption>In the opened data mapping windows, click on the "**pencil**" icon next to the "**Time series**" or "**Attributes**" section.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-absolute-path-3.webp" alt="Click on the &quot;**Add time series**&quot; button. Fill in the &quot;**Key**&quot; field with `Humidity`, also select &quot;**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**&quot; in &quot;**Type**&quot; field, and fill in the &quot;**Value**&quot; field with `${Root\.Objects\.DemoDevice\.Humidity}`. This is an absolute path to the node that contains the humidity data." loading="lazy"><figcaption>Click on the "**Add time series**" button. Fill in the "**Key**" field with `Humidity`, also select "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" in "**Type**" field, and fill in the "**Value**" field with `${Root\.Objects\.DemoDevice\.Humidity}`. This is an absolute path to the node that contains the humidity data.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-absolute-path-4.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


Now we can check if the humidity data is sending correctly. Go to "**Entities**" > "**Devices**", select a created 
device and as you can see, the humidity data is available in the "**Time series**" section:

![image](/images/gateway/opc-ua-connector/examples/result-device-overview-1.webp)

If you are using advanced configuration mode and want to set the humidity data using an absolute path, you can
use the following configuration:

```json
{
  "name": "OPCUA",
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "pollPeriodInMillis": 5000,
    "enableSubscriptions": false,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    }
  },
  "mapping": [
    {
      "deviceNodeSource": "path",
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpressionSource": "constant",
        "deviceProfileExpression": "default"
      },
      "attributes": [],
      "timeseries": [
        {
          "key": "Humidity",
          "type": "path",
          "value": "${Root\\.Objects\\.DemoDevice\\.Humidity}"
        }
      ],
      "rpc_methods": [],
      "attributes_updates": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="Attributes/Time series with Identifier">

Attributes and time series data can be accessed using [identifiers](/docs/iot-gateway/config/opc-ua/#identifier-types)
in the OPC UA Connector. This will allow you to get data from a node that does not refer to the parent (device) node
by identifier.

As an example, we will use Prosys OPC-UA Simulation Server, which is available at
`opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`. The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview-2.webp)

We are interested in node "**Humidity**" that have `ns=3;i=1011` identifier. We will use this node to retrieve the 
humidity data.

Let's configure the humidity data in the OPC-UA connector. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the OPC-UA connector, click on the "**Data mapping**" tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples).

1. In the opened data mapping windows, click on the "**pencil**" icon next to the "**Time series**" or "**Attributes**" section.

1. Click on the "**Add time series**" button. Fill in the "**Key**" field with `Humidity`, also select "**[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)**" in "**Type**" field, and fill in the "**Value**" field with `${ns=3;i=1011}`. This is a relative path to the node that contains the humidity data.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the left sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-absolute-path-1.webp" alt="Select the OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples)." loading="lazy"><figcaption>Select the OPC-UA connector, click on the "**Data mapping**" tab. Select data mapping with device to which you want to add time series data (if you do not know how to add a new device, see the [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) section of this guide with respective examples).</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-absolute-path-2.webp" alt="In the opened data mapping windows, click on the &quot;**pencil**&quot; icon next to the &quot;**Time series**&quot; or &quot;**Attributes**&quot; section." loading="lazy"><figcaption>In the opened data mapping windows, click on the "**pencil**" icon next to the "**Time series**" or "**Attributes**" section.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-identifier-path-3.webp" alt="Click on the &quot;**Add time series**&quot; button. Fill in the &quot;**Key**&quot; field with `Humidity`, also select &quot;**[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)**&quot; in &quot;**Type**&quot; field, and fill in the &quot;**Value**&quot; field with `${ns=3;i=1011}`. This is a relative path to the node that contains the humidity data." loading="lazy"><figcaption>Click on the "**Add time series**" button. Fill in the "**Key**" field with `Humidity`, also select "**[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)**" in "**Type**" field, and fill in the "**Value**" field with `${ns=3;i=1011}`. This is a relative path to the node that contains the humidity data.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attributes-time-series-absolute-path-4.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


Now we can check if the humidity data is sending correctly. Go to "**Entities**" > "**Devices**", select a created device and as you
can see, the humidity data is available in the "**Time series**" section:

![image](/images/gateway/opc-ua-connector/examples/result-device-overview-1.webp)

If you are using advanced configuration mode and want to set the humidity data using an identifier, you can
use the following configuration:

```json
{
  "name": "OPCUA",
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "pollPeriodInMillis": 5000,
    "enableSubscriptions": false,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    }
  },
  "mapping": [
    {
      "deviceNodeSource": "path",
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpressionSource": "constant",
        "deviceProfileExpression": "default"
      },
      "attributes": [],
      "timeseries": [
        {
          "key": "Humidity",
          "type": "identifier",
          "value": "${ns=3;i=1011}"
        }
      ],
      "rpc_methods": [],
      "attributes_updates": []
    }
  ]
}
```


</div>

</div>


## Requests mapping

The Requests mapping section allows you to configure how the SENTIENT platform instance will interact with the 
devices. That is, how the platform will request data from the devices, how it will update device attributes, and how 
it will send RPC commands to the devices.

OPC-UA connector supports the following requests mapping:
- **Attribute updates** - allows update device nodes values from SENTIENT platform instance.
- **RPC methods** - allows sending RPC commands to devices. Using RPC methods, you can get or set values of the OPC-UA nodes.
  OPC-UA connector supports different types of RPC methods, such as:
  - **Reserved GET/SET methods** - these methods are automatically created for each attribute and time series parameter. 
    You can use them to get or set values of the OPC-UA nodes.
  - **RPC method to connector** - this method allows you to send a command to the connector from the SENTIENT IoT Gateway UI. 
    The command will be processed by the connector, and the result will be sent back to the SENTIENT platform instance.
  - **Configurable RPC methods to device** - these methods allow you to configure custom RPC commands in connector configuration that can be sent to the devices.

### Subsection "Attribute updates"

This subsection contains configuration for attribute updates request from SENTIENT platform instance.

SENTIENT allows the provisioning of device attributes and fetches some of them from
the device application. You can treat this as a remote configuration for devices, enabling them to request 
shared attributes from SENTIENT. See [user guide](/docs/user-guide/attributes/) for more details.

The following parameters are used to configure attribute updates:
- **Key** - the key of the shared attribute in SENTIENT. It can be specified as a static value.
- **Type** - the type of expression in the **Value** field (more information about types can be found in the [Additional information](/docs/iot-gateway/config/opc-ua/#additional-information) section):
  - **[Path](/docs/iot-gateway/config/opc-ua/#path-types)** - can be absolute or relative path to the node in the OPC-UA server. The value will be taken from the node with the specified path.
  - **[Identifier](/docs/iot-gateway/config/opc-ua/#identifier-types)** - can be numeric, string, byte string or GUID identifier of the node in the OPC-UA server. The value will be taken from the node with the specified identifier.
  - **Constant** - a static value that will be sent to the device.
- **Value** - the node in which the shared attribute value will be written. It should be specified depending on the selected type (Path, Identifier or Constant).


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/opc-ua/#device-attributes-updates) section.

More usage examples can be found in the [Usage examples](/docs/iot-gateway/config/opc-ua/#usage-examples-1) section.


</div>


![image](/images/gateway/opc-ua-connector/opc-ua-attribute-updates-overview.webp)

In order to add new attribute update, follow these steps:


1. Click the “**pencil**” icon in the “**Attribute updates**” section to add new attribute update;

1. Click on "**Add attribute update**" in the opened window;

1. Enter the "**Key**" field, select the "**Type**" (can be [path](#path-types), [identifier](#identifier-types) or constant), enter "**Value**" and click "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-11-ce.webp" alt="Click the “**pencil**” icon in the “**Attribute updates**” section to add new attribute update;" loading="lazy"><figcaption>Click the “**pencil**” icon in the “**Attribute updates**” section to add new attribute update;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-12-ce.webp" alt="Click on &quot;**Add attribute update**&quot; in the opened window;" loading="lazy"><figcaption>Click on "**Add attribute update**" in the opened window;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-13-ce.webp" alt="Enter the &quot;**Key**&quot; field, select the &quot;**Type**&quot; (can be [path](#path-types), [identifier](#identifier-types) or constant), enter &quot;**Value**&quot; and click &quot;**Apply**&quot; button." loading="lazy"><figcaption>Enter the "**Key**" field, select the "**Type**" (can be [path](#path-types), [identifier](#identifier-types) or constant), enter "**Value**" and click "**Apply**" button.</figcaption></figure></div>


### Subsection "RPC methods"

SENTIENT allows sending [RPC commands](https://sentient.invenia.in/docs/user-guide/rpc/) to devices connected directly to SENTIENT or via Gateway.
The following parameters are used to configure RPC methods:

- **Method name** - the name of the method on OPC-UA server.
- **Arguments** - list of arguments that will pass to OPC-UA server method.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/opc-ua/#device-rpc-methods) section.

More usage examples can be found in the [Usage examples](/docs/iot-gateway/config/opc-ua/#usage-examples-1) section.


</div>


![image](/images/gateway/opc-ua-connector/opc-ua-rpc-overview.webp)

In order to add new RPC method, follow these steps:


1. Click the “**pencil**” icon in the “**RPC methods**” section to add new RPC method;

1. Click on "**Add method**" in the opened window;

1. Fill in "**Method name**" field. If the method has arguments, click on "**Add argument**" button and select the type of argument. Fill in the "**Value**" field and click "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-14-ce.webp" alt="Click the “**pencil**” icon in the “**RPC methods**” section to add new RPC method;" loading="lazy"><figcaption>Click the “**pencil**” icon in the “**RPC methods**” section to add new RPC method;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-15-ce.webp" alt="Click on &quot;**Add method**&quot; in the opened window;" loading="lazy"><figcaption>Click on "**Add method**" in the opened window;</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/opc-ua-gateway-configuring-16-ce.webp" alt="Fill in &quot;**Method name**&quot; field. If the method has arguments, click on &quot;**Add argument**&quot; button and select the type of argument. Fill in the &quot;**Value**&quot; field and click &quot;**Apply**&quot; button." loading="lazy"><figcaption>Fill in "**Method name**" field. If the method has arguments, click on "**Add argument**" button and select the type of argument. Fill in the "**Value**" field and click "**Apply**" button.</figcaption></figure></div>


<div class="st-callout info">


Also, every telemetry and attribute parameter has built-in GET and SET RPC methods out of the box, so you don’t need to configure
it manually. See [the guide](/docs/iot-gateway/guides/how-to-use-get-set-rpc-methods).


</div>


### Usage examples


<div class="st-tabs">

<div class="st-tab" data-label="Attribute Updateswith Relative Path">

Attribute updates allow you to update node values in the OPC-UA server. 
You can add new attribute updates in the "**Attribute updates**" section of the device configuration page.

As an example, we will use Prosys OPC-UA Simulation Server, which is available at `opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`.
The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview-3.webp)

#### Example: Relay Controlling (Relative Path)

We are interested in node "**Relay**", we added this node as a telemetry parameter with the key `relay`. We used 
telemetry so that later it would be convenient for us to see if the value we changed using the attribute update 
has changed. You, also, can add this telemetry datapoint to the device configuration or use the reserved `get` RPC 
method to check the value of the node.

Let's add an attribute update to our configuration. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created OPC-UA connector, click on the "**Data mapping**" tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the "**Pencil**" icon on a device you want to configure attribute updates for.

1. Scroll down to the "**Attribute updates**" section and click on the "**Pencil**" icon to edit the attribute updates.

1. Click on the "**Add attribute update**" button. In our case, we will add `relay` attribute update, so the "**Key**" field, enter `relay`, select the "**Type**" as **Path**, and in the "**Value**" field enter `${Relay}`. This is a relative path to the device node we want to update.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the right sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-1.webp" alt="Select the created OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the &quot;**Pencil**&quot; icon on a device you want to configure attribute updates for." loading="lazy"><figcaption>Select the created OPC-UA connector, click on the "**Data mapping**" tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the "**Pencil**" icon on a device you want to configure attribute updates for.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-2.webp" alt="Scroll down to the &quot;**Attribute updates**&quot; section and click on the &quot;**Pencil**&quot; icon to edit the attribute updates." loading="lazy"><figcaption>Scroll down to the "**Attribute updates**" section and click on the "**Pencil**" icon to edit the attribute updates.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-3.webp" alt="Click on the &quot;**Add attribute update**&quot; button. In our case, we will add `relay` attribute update, so the &quot;**Key**&quot; field, enter `relay`, select the &quot;**Type**&quot; as **Path**, and in the &quot;**Value**&quot; field enter `${Relay}`. This is a relative path to the device node we want to update." loading="lazy"><figcaption>Click on the "**Add attribute update**" button. In our case, we will add `relay` attribute update, so the "**Key**" field, enter `relay`, select the "**Type**" as **Path**, and in the "**Value**" field enter `${Relay}`. This is a relative path to the device node we want to update.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-relative-path-9.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


Now we can check if the attribute update works. Go to "**Entities**" → "**Devices**" → select a created device → "**Attributes**" tab → 
select "**Shared attributes**" → click on the "**+**" icon and add `relay` attribute with type "**Boolean**" set it 
to "**True**".


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-4.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-5.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Now, let's check the value of the relay node. In the selected device, go to the "**Last telemetry**" tab and check the 
value of the `relay` telemetry. It should be `true` since we set the shared attribute to `true`.

![image](/images/gateway/opc-ua-connector/examples/result-device-overview-2.webp)

Try to change the value of the `relay` shared attribute to `false`. After a few seconds, you should see that the
`relay` telemetry value has changed to `false`, which means that the attribute update worked correctly.

Full configuration for OPC-UA connector for the examples above will look like this:

```json
{
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "enableSubscriptions": true,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    },
    "pollPeriodInMillis": 5000
  },
  "mapping": [
    {
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceNodeSource": "path",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpression": "default",
        "deviceProfileExpressionSource": "constant"
      },
      "attributes": [],
      "attributes_updates": [
        {
          "key": "relay",
          "type": "path",
          "value": "${Relay}"
        }
      ],
      "timeseries": [
        {
          "key": "relay",
          "type": "identifier",
          "value": "${ns=3;i=1012}"
        }
      ],
      "rpc_methods": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="Attribute Updateswith Absolute Path">

Attribute updates allow you to update node values in the OPC-UA server. 
You can add new attribute updates in the "**Attribute updates**" section of the device configuration page.

As an example, we will use Prosys OPC-UA Simulation Server, which is available at `opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`.
The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview-4.webp)

#### Example: Fan Speed (Absolute Path)

We are interested in node "**FanSpeed**", we added this node as a telemetry parameter with the key `fan_speed`. We used 
telemetry so that later it would be convenient for us to see if the value we changed using the attribute update  
has changed. You, also, can add this telemetry datapoint to the device configuration or use the reserved `get` method 
to check the value of the node.

Let's add an attribute update to our configuration. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created OPC-UA connector, click on the "**Data mapping**" tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the "**Pencil**" icon on a device you want to configure attribute updates for.

1. Scroll down to the "**Attribute updates**" section and click on the "**Pencil**" icon to edit the attribute updates.

1. Click on the "**Add attribute update**" button. In our case, we will add `fan_speed` attribute update, so the "**Key**" field, enter `fan_speed`, select the "**Type**" as **Path**, and in the "**Value**" field enter `${Root\.Objects\.DemoDeviceInfo\.FanSpeed}`. This is an absolute path to the OPC-UA server node we want to update.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the left sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-1.webp" alt="Select the created OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the &quot;**Pencil**&quot; icon on a device you want to configure attribute updates for." loading="lazy"><figcaption>Select the created OPC-UA connector, click on the "**Data mapping**" tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the "**Pencil**" icon on a device you want to configure attribute updates for.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-absolute-path-1.webp" alt="Scroll down to the &quot;**Attribute updates**&quot; section and click on the &quot;**Pencil**&quot; icon to edit the attribute updates." loading="lazy"><figcaption>Scroll down to the "**Attribute updates**" section and click on the "**Pencil**" icon to edit the attribute updates.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-absolute-path-2.webp" alt="Click on the &quot;**Add attribute update**&quot; button. In our case, we will add `fan_speed` attribute update, so the &quot;**Key**&quot; field, enter `fan_speed`, select the &quot;**Type**&quot; as **Path**, and in the &quot;**Value**&quot; field enter `${Root\.Objects\.DemoDeviceInfo\.FanSpeed}`. This is an absolute path to the OPC-UA server node we want to update." loading="lazy"><figcaption>Click on the "**Add attribute update**" button. In our case, we will add `fan_speed` attribute update, so the "**Key**" field, enter `fan_speed`, select the "**Type**" as **Path**, and in the "**Value**" field enter `${Root\.Objects\.DemoDeviceInfo\.FanSpeed}`. This is an absolute path to the OPC-UA server node we want to update.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-relative-path-9.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


Now we can check if the attribute update works. Go to "**Devices**" → select a created device → "**Attributes**" tab → 
select "**Shared attributes**" → click on the "**+**" icon and add `fan_speed` attribute with type "**Integer**" set it 
to "**90**".


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-4.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-absolute-path-3.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Now, let's check the value of the fan speed node. In the selected device, go to the "**Last telemetry**" tab and check the 
value of the `fan_speed` telemetry. It should be `90` since we set the shared attribute to `90`.

![image](/images/gateway/opc-ua-connector/examples/result-device-overview-3.webp)

Try to change the value of the `fan_speed` shared attribute to `30`. After a few seconds, you should see that the
`fan_speed` telemetry value has changed to `30`, which means that the attribute update worked correctly.

Full configuration for OPC-UA connector for the examples above will look like this:

```json
{
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "enableSubscriptions": true,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    },
    "pollPeriodInMillis": 5000
  },
  "mapping": [
    {
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceNodeSource": "path",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpression": "default",
        "deviceProfileExpressionSource": "constant"
      },
      "attributes": [],
      "attributes_updates": [
        {
          "key": "fan_speed",
          "type": "path",
          "value": "${Root\\.Objects\\.DemoDeviceInfo\\.FanSpeed}"
        }
      ],
      "timeseries": [
        {
          "key": "fan_speed",
          "type": "identifier",
          "value": "${ns=3;i=1017}"
        }
      ],
      "rpc_methods": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="Attribute Updateswith Identifier">

Attribute updates allow you to update node values in the OPC-UA server. 
You can add new attribute updates in the "**Attribute updates**" section of the device configuration page.

As an example, we will use Prosys OPC-UA Simulation Server, which is available at `opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`.
The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview-4.webp)

### Example: Text Message Editing (Identifier)

We are interested in node "**TextMessage**", we added this node as a telemetry parameter with the key `text_message`. 
We used telemetry so that later it would be convenient for us to see if the value we changed using the attribute update  
has changed. You, also, can add this telemetry datapoint to the device configuration or use the reserved `get` method 
to check the value of the node.

Let's add an attribute update to our configuration. For this purpose, follow these steps:
- Go to "**Entities**" → "**Gateways**" in the right sidebar.
- Select your gateway.
- Click on the "**Connectors**" tab.
- Select the OPC-UA connector and click on the "**Data mapping**" tab.
- Make sure you have configured and connected device (if you don't know how to do it, see Getting Started guide or 
  Connection settings and Data mapping sections of this guide). Click on the "**Pencil**" icon on a device you want to 
  configure attribute updates for.
- Scroll down to the "**Attribute updates**" section and click on the "**Pencil**" icon to edit the attribute updates.
- Click on the "**Add attribute update**" button. In our case, we will add `text_message` attribute update, so the "**Key**" 
  field, enter `text_message`, select the "**Type**" as **Identifier**, and in the "**Value**" field enter 
  `${ns=2;i=1005}`. This is an identifier of the OPC-UA server node we want to update.
- Remember to save your changes by clicking the "**Apply**" button.


1. Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created OPC-UA connector, click on the "**Data mapping**" tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the "**Pencil**" icon on a device you want to configure attribute updates for.

1. Scroll down to the "**Attribute updates**" section and click on the "**Pencil**" icon to edit the attribute updates.

1. Click on the "**Add attribute update**" button. In our case, we will add `text_message` attribute update, so the "**Key**" field, enter `text_message`, select the "**Type**" as **Identifier**, and in the "**Value**" field enter `${ns=2;i=1005}`. This is an identifier of the OPC-UA server node we want to update.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the right sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-1.webp" alt="Select the created OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the &quot;**Pencil**&quot; icon on a device you want to configure attribute updates for." loading="lazy"><figcaption>Select the created OPC-UA connector, click on the "**Data mapping**" tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the "**Pencil**" icon on a device you want to configure attribute updates for.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-identifier-1.webp" alt="Scroll down to the &quot;**Attribute updates**&quot; section and click on the &quot;**Pencil**&quot; icon to edit the attribute updates." loading="lazy"><figcaption>Scroll down to the "**Attribute updates**" section and click on the "**Pencil**" icon to edit the attribute updates.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-identifier-2.webp" alt="Click on the &quot;**Add attribute update**&quot; button. In our case, we will add `text_message` attribute update, so the &quot;**Key**&quot; field, enter `text_message`, select the &quot;**Type**&quot; as **Identifier**, and in the &quot;**Value**&quot; field enter `${ns=2;i=1005}`. This is an identifier of the OPC-UA server node we want to update." loading="lazy"><figcaption>Click on the "**Add attribute update**" button. In our case, we will add `text_message` attribute update, so the "**Key**" field, enter `text_message`, select the "**Type**" as **Identifier**, and in the "**Value**" field enter `${ns=2;i=1005}`. This is an identifier of the OPC-UA server node we want to update.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-relative-path-9.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


Now we can check if the attribute update works. Go to "**Devices**" → select a created device → "**Attributes**" tab → 
select "**Shared attributes**" → click on the "**+**" icon and add `text_message` attribute with type "**String**" set 
it to "**Hello from Gateway!**".


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-4.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-identifier-3.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Now, let's check the value of the text message node. In the selected device, go to the "**Last telemetry**" tab and check the 
value of the `text_message` telemetry. It should be `Hello from Gateway!` since we set the shared attribute to `Hello from Gateway!`.

![image](/images/gateway/opc-ua-connector/examples/result-device-overview-4.webp)

Try to change the value of the `text_message` shared attribute to `Hello from <your_name>!`. After a few seconds, 
you should see that the `text_message` telemetry value has changed to `Hello from <your_name>!`, which means that the 
attribute update worked correctly.

Full configuration for OPC-UA connector for the examples above will look like this:

```json
{
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "enableSubscriptions": true,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    },
    "pollPeriodInMillis": 5000
  },
  "mapping": [
    {
      "deviceNodeSource": "path",
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpression": "default",
        "deviceProfileExpressionSource": "constant"
      },
      "attributes": [],
      "timeseries": [
        {
          "key": "text_message",
          "type": "identifier",
          "value": "${ns=3;i=1018}"
        }
      ],
      "rpc_methods": [],
      "attributes_updates": [
        {
          "key": "text_message",
          "type": "identifier",
          "value": "${ns=3;i=1018}"
        }
      ]
    }
  ]
}
```


</div>

<div class="st-tab" data-label="RPC to Device">

RPC to Device allows you to execute an OPC-UA server method on a specific device.
It is important to note that the method you are calling must be defined on the OPC-UA server.

As an example, we will use SENTIENT OPC-UA Demo Server, which can be run using Docker and the following command:
```bash
docker run -it -p 4840:4840 sentient/st-gw-opcua-server:latest
```

The server has the following endpoint URL: `opc.tcp://0.0.0.0:4840/freeopcua/server/`.

#### Example: Multiplying Numbers

We are interested in "**multiply**" method node which will multiply two numbers that we will pass as arguments.
To call this method, first we need to configure the OPC-UA connector to support RPC calls. For this purpose, follow 
these steps:


1. Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created OPC-UA connector, click on the "**Data mapping**" tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the "**Pencil**" icon on a device you want to configure RPC method for.

1. Scroll down to the "**RPC methods**" section and click on the "**Pencil**" icon to edit the RPC methods.

1. Click on the "Add method" button. In our case, we will add the `multiply` method, so fill in the "**Method**" field with `multiply` and in the "**Arguments**" field, enter the arguments that the method accepts, in our case it is two numbers, feel free to enter any numbers.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the right sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-1.webp" alt="Select the created OPC-UA connector, click on the &quot;**Data mapping**&quot; tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the &quot;**Pencil**&quot; icon on a device you want to configure RPC method for." loading="lazy"><figcaption>Select the created OPC-UA connector, click on the "**Data mapping**" tab. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide). Click on the "**Pencil**" icon on a device you want to configure RPC method for.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/rpc-to-device-1.webp" alt="Scroll down to the &quot;**RPC methods**&quot; section and click on the &quot;**Pencil**&quot; icon to edit the RPC methods." loading="lazy"><figcaption>Scroll down to the "**RPC methods**" section and click on the "**Pencil**" icon to edit the RPC methods.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/rpc-to-device-2.webp" alt="Click on the &quot;Add method&quot; button. In our case, we will add the `multiply` method, so fill in the &quot;**Method**&quot; field with `multiply` and in the &quot;**Arguments**&quot; field, enter the arguments that the method accepts, in our case it is two numbers, feel free to enter any numbers." loading="lazy"><figcaption>Click on the "Add method" button. In our case, we will add the `multiply` method, so fill in the "**Method**" field with `multiply` and in the "**Arguments**" field, enter the arguments that the method accepts, in our case it is two numbers, feel free to enter any numbers.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-relative-path-9.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


We are done with configuration, so let's check how to call the method. In the RPC Debug Terminal widget, run the 
following command:

```bash
multiply
```

In this case, the method will be called with the arguments that we specified in the configuration (default arguments). 
As you remember, in our case, we enter 5 and 4, so the result is:

![image](/images/gateway/opc-ua-connector/examples/result-device-overview-5.webp)

Also, we can pass arguments to the method directly from the RPC Debug Terminal widget using the following command:

```bash
multiply [3,4]
```

Response:

![image](/images/gateway/opc-ua-connector/examples/result-device-overview-6.webp)

Full configuration for OPC-UA connector for the example above will look like this:

```json
{
  "name": "OPCUA",
  "server": {
    "url": "opc.tcp://0.0.0.0:4840/freeopcua/server/",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "pollPeriodInMillis": 5000,
    "enableSubscriptions": false,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    }
  },
  "mapping": [
    {
      "deviceNodeSource": "path",
      "deviceNodePattern": "Root\\.Objects\\.MyObject",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpression": "default",
        "deviceProfileExpressionSource": "constant"
      },
      "attributes": [],
      "timeseries": [
        {
          "key": "some_key",
          "type": "path",
          "value": "${some_key}"
        }
      ],
      "rpc_methods": [
        {
          "method": "multiply",
          "arguments": [
            {
              "type": "integer",
              "value": 5
            },
            {
              "type": "integer",
              "value": 4
            }
          ]
        }
      ],
      "attributes_updates": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="Reserved RPCs">

Every telemetry and attribute parameter has `GET` and `SET` RPC methods out of the box, so you don’t need to configure 
them manually.

As an example, we will use Prosys OPC-UA Simulation Server, which is 
available at `opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`. The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview-3.webp)

We are interested in node "**Relay**" that have `ns=3;i=1012` identifier, we added this node as a telemetry parameter 
with the key `relay` and as a path we used the node identifier `${ns=3;i=1012}`, so the configuration for this 
telemetry will look like this:

```json
"timeseries": [
  {
    "key": "relay",
    "type": "identifier",
    "value": "${ns=3;i=1012}"
  }
]
```

Let's check the value of the relay node using the reserved `get` method. To get the current value of relay node, 
run the query in RPC debug terminal:

```bash
get ns=3;i=1012;
```

Response:

```json
{"result":  {"value":  false}}
```

![image](/images/gateway/opc-ua-connector/examples/opc-ua-reserved-rpc-get-result-1.webp)

So, the `get` method returns the current value of the relay node, and we can see that the relay is off.


<div class="st-callout info">


The RPC Debug Terminal is used only for example purpose, so you can use any other widget that supports RPC calls.


</div>


To set the value of the relay node and turn it on, run the query:

```bash
set ns=3;i=1012; true
```

Response:

```json
{"result":  {"value":  true}}
```

And as you can see, from the screenshot below, the relay telemetry value has changed to `true`:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-reserved-rpc-set-result-1.webp)

Also, let's check the value of the relay telemetry again:

```bash
get ns=3;i=1012;
```

Response:

```json
{"result":  {"value":  true}}
```

![image](/images/gateway/opc-ua-connector/examples/opc-ua-reserved-rpc-get-result-2.webp)

Full configuration for OPC-UA connector for the examples above will look like this:

```json
{
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "enableSubscriptions": true,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    },
    "pollPeriodInMillis": 5000
  },
  "mapping": [
    {
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceNodeSource": "path",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpression": "default",
        "deviceProfileExpressionSource": "constant"
      },
      "attributes": [],
      "attributes_updates": [],
      "timeseries": [
        {
          "key": "relay",
          "type": "identifier",
          "value": "${ns=3;i=1012}"
        }
      ],
      "rpc_methods": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="Reserved RPCs to foreign nodes">

Every telemetry and attribute parameter comes with built-in `get` and `set` RPC methods, so you don’t need to configure them manually.

Additionally, you can use the reserved RPC methods to access any node on the OPC-UA server - even if it doesn’t belong to a specific device. This is especially useful when management or control nodes are located outside the device’s node tree.
We will set the device node to `Root\.Objects\.DemoDevice`, but we will access the `TextMessage` node located at `Root\.Objects\.DemoDeviceInfo\.TextMessage`, which is outside the device node tree.
As an example, we will use Prosys OPC-UA Simulation Server, which is 
available at `opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer`. The server has the following structure:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-server-structure-overview-4.webp)

We’re interested in the "**TextMessage**" which has the "**[Path](/docs/iot-gateway/config/opc-ua/#absolute-path)**" - `Root\.Objects\.DemoDeviceInfo\.TextMessage`, 
and does not belong to the device node tree. We added this node as a telemetry parameter
with the key `textmessage`, so it would be easy to verify later whether the value changed after calling the reserved `set` RPC method.

```json
"timeseries": [
  {
    "key": "textmessage",
    "type": "path",   
    "value": "${Root\\.Objects\\.DemoDeviceInfo\\.TextMessage}"
  }
]
```


Let's check the value of the textmessage node using the reserved `get` method. To get the current value of textmessage node, 
run the query in RPC debug terminal:

```bash
get Root\\.Objects\\.DemoDeviceInfo\\.TextMessage;
```


Response:

```json
{"result":{"value":"HI"}}
```


![image](/images/gateway/opc-ua-connector/examples/opc-ua-reserved-rpc-get-foreign-nodes-result-1.webp)

So, the `get` method returns the current value of the textmessage node, and we can see that the textmessage is `HI`.


<div class="st-callout info">


The RPC Debug Terminal is used only for example purpose, so you can use any other widget that supports RPC calls.


</div>


To set the value of the textmessage node and change its value, run the query:

```bash
set Root\\.Objects\\.DemoDeviceInfo\\.TextMessage; New Message
```


Response:

```json
{"result":{"value":"New Message"}}
```


And as you can see, from the screenshot below, the textmessage telemetry value has changed to `New Message`:

![image](/images/gateway/opc-ua-connector/examples/opc-ua-reserved-rpc-set-foreign-nodes-result-1.webp)

Also, let's check the value of the textmessage telemetry again:

```bash
get Root\\.Objects\\.DemoDeviceInfo\\.TextMessage;
```


Response:

```json
{"result":{"value":"New Message"}}
```


![image](/images/gateway/opc-ua-connector/examples/opc-ua-reserved-rpc-get-foreign-nodes-result-2.webp)

Full configuration for OPC-UA connector for the examples above will look like this:

```json
{
  "server": {
    "url": "opc.tcp://0.0.0.0:53530/OPCUA/SimulationServer",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "enableSubscriptions": true,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    },
    "pollPeriodInMillis": 5000
  },
  "mapping": [
    {
      "deviceNodePattern": "Root\\.Objects\\.DemoDevice",
      "deviceNodeSource": "path",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpression": "default",
        "deviceProfileExpressionSource": "constant"
      },
      "attributes": [],
      "attributes_updates": [],
      "timeseries": [
        {
          "key": "textmessage",
          "type": "path",
          "value": "${Root\\.Objects\\.DemoDeviceInfo\\.TextMessage}"
        }
      ],
      "rpc_methods": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="RPC to Connector">

RPC To Connector allows you to send a command to the connector from the SENTIENT IoT Gateway UI.
It is important to note that the method you are calling must be defined on the OPC-UA server.


<div class="st-callout info">


**Please note**: The RPC To Connector will execute the method on every device that has the OPC-UA connector configured.


</div>


As an example, we will use SENTIENT OPC-UA Demo Server, which can be run using Docker and the following command:
```bash
docker run -it -p 4840:4840 sentient/st-gw-opcua-server:latest
```

The server has the following endpoint URL: `opc.tcp://0.0.0.0:4840/freeopcua/server/`.

#### Example: Relay Controlling

Let's see a practical example of using RPC To Connector. On our OPC-UA server, we have "set_relay" method that
turns on or off the relay. The method accepts a boolean argument, where `true` turns on the relay and `false` turns 
it off. To call this method, use the following steps:


1. Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created OPC-UA connector, click on the "**RPC**" icon. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide).


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-1.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the right sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the right sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/device-name-and-profile-absolute-path-2.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/rpc-to-connector-1.webp" alt="Select the created OPC-UA connector, click on the &quot;**RPC**&quot; icon. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide)." loading="lazy"><figcaption>Select the created OPC-UA connector, click on the "**RPC**" icon. Make sure you have configured and connected device (if you do not know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=opcua) guide or [Connection settings](/docs/iot-gateway/config/opc-ua/#connection-settings) and [Data mapping](/docs/iot-gateway/config/opc-ua/#data-mapping) sections of this guide).</figcaption></figure></div>


Let's first turn on the relay. To do this, fill in the "**Method**" field with `set_relay` and in the "**Arguments**" field
enter `true`, then click on the "**Send**" button.

![image](/images/gateway/opc-ua-connector/examples/rpc-to-connector-2.webp)

As you can see, the response contains `true`, which means that the method was executed successfully and the relay is 
now on:

![image](/images/gateway/opc-ua-connector/examples/rpc-to-connector-3.webp)

And finally, let's turn off the relay. To do this, fill in the "**Method**" field with `set_relay` and in the
"**Arguments**" field enter `false`, then click on the "**Send**" button:

![image](/images/gateway/opc-ua-connector/examples/rpc-to-connector-4.webp)

Result:

![image](/images/gateway/opc-ua-connector/examples/rpc-to-connector-5.webp)

Full configuration for OPC-UA connector for the example above will look like this:

```json
{
  "server": {
    "url": "opc.tcp://0.0.0.0:4840/freeopcua/server/",
    "timeoutInMillis": 5000,
    "scanPeriodInMillis": 3600000,
    "enableSubscriptions": true,
    "subCheckPeriodInMillis": 100,
    "showMap": false,
    "security": "Basic128Rsa15",
    "identity": {
      "type": "anonymous"
    },
    "pollPeriodInMillis": 5000
  },
  "mapping": [
    {
      "deviceNodePattern": "Root\\.Objects\\.MyObject",
      "deviceNodeSource": "path",
      "deviceInfo": {
        "deviceNameExpression": "Demo Device",
        "deviceNameExpressionSource": "constant",
        "deviceProfileExpression": "default",
        "deviceProfileExpressionSource": "constant"
      },
      "attributes": [],
      "attributes_updates": [],
      "timeseries": [
        {
          "key": "Frequency",
          "type": "path",
          "value": "${Frequency}"
        }
      ],
      "rpc_methods": []
    }
  ]
}
```


</div>

</div>


## Advanced configuration

The advanced configuration section provides a detailed overview of all available parameters for the OPC-UA connector.

### Server

The server object specifies the target OPC-UA server and how the gateway interacts with it.

| **Parameter**                                      | **Default value** | **Description**                                                                                                                                                                                                                                                                                                                                   |
|:---------------------------------------------------|:------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server                                             |                   | The server object specifies the target OPC-UA server and how the gateway interacts with it.                                                                                                                                                                                                                                                       |
| server.url                                         |                   | Hostname or ip address of OPC-UA server.                                                                                                                                                                                                                                                                                                          |
| server.timeoutInMillis (in ms)                     | **5000**          | Timeout in seconds for connecting to OPC-UA server.                                                                                                                                                                                                                                                                                               |
| server.scanPeriodInMillis (in ms)                  | **3600000**       | Period in milliseconds for scanning the OPC-UA server for changes. If your OPC-UA server structure doesn't change often, you can set a big period for gateway resource saving.                                                                                                                                                                    |
| server.pollPeriodInMillis (in ms)                  | **5000**          | Period in milliseconds to poll the server. **If enableSubscriptions is set to true, pollPeriodInMillis does not affect data reading.**                                                                                                                                                                                                            |
| server.enableSubscriptions                         | **true**          | If true - the gateway will subscribe to interesting nodes and wait for data update and if false - the gateway will rescan OPC-UA server every `scanPeriodInMillis`.                                                                                                                                                                               |
| server.subCheckPeriodInMillis (in ms)              | **100**           | Defines the publishing/check interval that the connector requests when creating OPC-UA subscriptions.                                                                                                                                                                                                                                             |
| server.subKeepAlivePeriodInSeconds (in seconds) ** | **0**             | The interval at which the connector checks whether OPC-UA subscriptions are still “alive” (i.e., the publish/data-change flow is not stalled). This check is disabled by default (set to 0). If a subscription shows no activity longer than this threshold, the connector treats it as expired and triggers resubscription to restore updates.   |
| server.subDataMaxBatchSize                         | **1000**          | Maximum number of data items in a single subscription update. This is useful for performance optimization.                                                                                                                                                                                                                                        |
| server.subDataMinBatchCreationTimeMs (in ms)       | **200**           | Minimum time in milliseconds to wait before creating a new batch of data items in a subscription update. This helps to reduce the number of updates sent to SENTIENT.                                                                                                                                                                          |
| server.subscriptionProcessBatchSize                | **2000**          | Maximum number of data items to process in a single batch when handling subscription updates. This is useful for performance optimization.                                                                                                                                                                                                        |
| server.sessionTimeoutInMillis (in ms)              | **120000**        | Session timeout in milliseconds. This is the maximum time the session can be inactive before it is closed by the server.                                                                                                                                                                                                                          |
| server.showMap                                     | **false**         | If true - the gateway will show a map of OPC-UA server nodes in the terminal. This is useful for debugging and understanding the structure of the OPC-UA server.                                                                                                                                                                                  |
| server.security                                    | **Basic128Rsa15** | Security policy (`Basic128Rsa15`, `Basic256`, `Basic256Sha256`).                                                                                                                                                                                                                                                                                  |
| ---                                                |                   |                                                                                                                                                                                                                                                                                                                                                   |


<div class="st-callout info">


**Please note:**
\** -- Subscription lifetime in OPC-UA is negotiated using the publishing interval, keep-alive, and lifetime settings, and can be approximated as RequestedLifetimeCount * RequestedPublishingInterval.
In asyncua, RequestedLifetimeCount is typically an internal default which is 1000 ms, while the publishing interval comes from the value used to create the subscription (here: `server.subCheckPeriodInMillis`, e.g. 100 ms), so the approximate lifetime is (1000 * 100) / 1000 = 100 seconds.
However, the exact removal time depends on the OPC-UA server implementation and its cleanup logic - some servers keep subscriptions longer, others may drop them earlier under load or session/publish issues. Therefore, this setting is made to detect “silent” subscriptions and renew them, but you should validate it against your server to avoid extra overhead.


</div>


Example of the server configuration:

```json
"server": {
  "url": "localhost:4840/freeopcua/server/",
  "timeoutInMillis": 5000,
  "scanPeriodInMillis": 3600000,
  "pollPeriodInMillis": 5000,
  "enableSubscriptions": true,
  "subCheckPeriodInMillis": 100,
  "subDataMaxBatchSize": 1000,
  "subDataMinBatchCreationTimeMs": 200,
  "subscriptionProcessBatchSize": 2000,
  "sessionTimeoutInMillis": 120000,
  "showMap": false,
  "security": "Basic128Rsa15",
  "identity": {
    "type": "anonymous"
  }
}
```

#### Server identity

The identity object specifies the authentication method used to connect to the OPC-UA server. It can be one of the 
following: **anonymous**, **basic**, **certificates**.

##### Anonymous identity

| **Parameter**        | **Default value** | **Description**                    |
|:---------------------|:------------------|------------------------------------|
| server.identity.type | **anonymous**     | Type of identity on OPC-UA server. |
| ---                  |                   |                                    |

##### Basic identity

| **Parameter**            | **Default value** | **Description**                              |
|:-------------------------|:------------------|----------------------------------------------|
| server.identity.type     | **basic**         | Type of identity on OPC-UA server.           |
| server.identity.username |                   | Username for logging into the OPC-UA server. |
| server.identity.password |                   | Password for logging into the OPC-UA server. |
| ---                      |                   |                                              |

Example of the basic identity configuration:

```json
"identity": {
  "type": "basic",
  "username": "user",
  "password": "5Tr0nG?@$sW0rD"
},
```

##### Certificates identity

| **Parameter**              | **Default value**  | **Description**                                                   |
|:---------------------------|:-------------------|-------------------------------------------------------------------|
| server.identity.type       | **cert.PEM**       | Type of identity on OPC-UA server.                                |
| server.identity.caCert     |                    | Path to the CA certificate.                                       |
| server.identity.cert       |                    | Path to the client certificate.                                   |
| server.identity.privateKey |                    | Path to the client private key.                                   |
| server.identity.mode       | **SignAndEncrypt** | Security mode, there are 2 options – `Sign` and `SignAndEncrypt`. |
| username                   |                    | (Optional) Username for logging into the OPC-UA server.           |
| password                   |                    | (Optional) Password for logging into the OPC-UA server.           |
| ---                        |                    |                                                                   |

Example of the basic certificates configuration:

```json
"identity": {
  "type": "cert.PEM",
  "caCert": "etc/sentient-gateway/ca.pem",
  "privateKey": "etc/sentient-gateway/private_key.pem", 
  "cert": "etc/sentient-gateway/cert.pem",
  "mode": "SignAndEncrypt",
  "username": "user",
  "password": "5Tr0nG?@$sW0rD"
},
```

### Mapping

The Mapping list is used to configure how the OPC-UA connector will map data from the OPC-UA server to
SENTIENT devices. It allows you to specify which nodes from the OPC-UA server will be used as device names,
device profiles, device attributes, and telemetry data.

#### Device mapping

| **Parameter**                                   | **Description**                                                                                                                                                                                                                                |
|:------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mapping[].deviceNodeSource                      | Source of the device node, can be: path, identifier or constant.                                                                                                                                                                               |
| mapping[].deviceNodePattern                     | Absolute or relative [path](#path-types), or [identifier](#identifier-types), which is used for looking up the node for a current device. Paths to the device name, profile, attributes, and telemetry can be specified relative to this node. |
| mapping[].deviceInfo                            | Device info object using for configuring device name and profile.                                                                                                                                                                              |
| mapping[].deviceInfo.deviceNameExpressionSource | Source of the device name (can be [path](#path-types), [identifier](#identifier-types) or constant).                                                                                                                                           |
| mapping[].deviceInfo.deviceNameExpression       | Path to a variable with device name, which is used for looking up the device name in a variable.                                                                                                                                               |
| mapping[].deviceInfo.deviceProfileSource        | Source of the device profile (can be [path](#path-types), [identifier](#identifier-types) or constant).                                                                                                                                        |
| mapping[].deviceInfo.deviceProfileExpression    | Path to a variable with device profile, is used for looking the device profile in some variable.                                                                                                                                               |
| mapping[].reportStrategy                        | Report strategy object using for configuring report strategy for device.                                                                                                                                                                       |
| ---                                             |                                                                                                                                                                                                                                                |

Example of the device mapping configuration:

```json
"mapping": [
  {
    "deviceNodeSource": "path",
    "deviceNodePattern": "Root\\.Objects\\.MyObject",
    "deviceInfo": {
      "deviceNameExpression": "OPCUA New Advanced Device",
      "deviceNameExpressionSource": "path",
      "deviceProfileExpression": "some other default 1",
      "deviceProfileExpressionSource": "constant"
    },
    "attributes": [],
    "timeseries": [],
    "attributes_updates": [],
    "rpc_methods": [],
  },
]
```

#### Device attributes and time series

| **Parameter**                            | **Description**                                                                                                                                            |
|:-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mapping[].attributes[]                   | List of attributes that will be sent to the SENTIENT platform instance.                                                                                 |
| mapping[].attributes[].key               | Key name of the attribute in SENTIENT. It can be specified as a static value.                                                                           |
| mapping[].attributes[].type              | Type of the expression in the value field (can be [path](#path-types), [identifier](#identifier-types) or constant).                                       |
| mapping[].attributes[].value             | Value of the attribute that will be sent to the platform. It should be specified depending on the selected type (`path`, `identifier` or `constant`).      |
| mapping[].attributes[].reportStrategy    | (Optional) Report strategy for the attributes data. If not specified, the device report strategy will be used.                                             |
| mapping[].timeseries[]                   | List of telemetry data that will be sent to the SENTIENT platform instance.                                                                             |
| mapping[].timeseries[].key               | Key name of the telemetry data in SENTIENT. It can be specified as a static value.                                                                      |
| mapping[].timeseries[].type              | Type of the expression in the value field (can be [path](#path-types), [identifier](#identifier-types) or constant).                                       |
| mapping[].timeseries[].value             | Value of the telemetry data that will be sent to the platform. It should be specified depending on the selected type (`path`, `identifier` or `constant`). |
| mapping[].timeseries[].timestampLocation | (Optional) Location of the timestamp for the attribute. If not specified, the current time will be used. Can be: `sourcetimestamp`, `servertimestamp`      |
| mapping[].timeseries[].reportStrategy    | (Optional) Report strategy for the time series data. If not specified, the device report strategy will be used.                                            |
| ---                                      |                                                                                                                                                            |

Example of the attributes and telemetry configuration:

```json
"attributes": [
  {
    "key": "Power",
    "type": "path",
    "value": "${Power}"
  },
  {
    "key": "Frequency",
    "type": "path",
    "value": "${Frequency}"
  }
],
"timeseries": [
  {
    "key": "Humidity",
    "type": "path",
    "value": "${ns=2;i=16}"
  },
  {
    "key": "Temperature",
    "type": "path",
    "value": "${Root\\.Objects\\.MyObject\\.Temperature}"
  }
],
```

#### Device attributes updates

| **Parameter**                                  | **Default value** | **Description**                                                                                                                                     |
|:-----------------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| mapping[].attributes_updates[]                 |                   | List of attributes that will be updated on the device.                                                                                              |
| mapping[].attributes_updates[].key             |                   | Key name of the shared attribute in SENTIENT. It can be specified as a static value.                                                             |
| mapping[].attributes_updates[].type            |                   | Type of the expression in the value field (can be [path](#path-types), [identifier](#identifier-types) or constant).                                |
| mapping[].attributes_updates[].value           |                   | Value of the attribute that will be sent to the device. It should be specified depending on the selected type (`path`, `identifier` or `constant`). |
| mapping[].attributes_updates[].timeout (in ms) | **5000**          | Timeout in milliseconds for the attribute update request.                                                                                           |
| ---                                            |                   |                                                                                                                                                     |

Example of the attributes updates configuration:

```json
"attributes_updates": [
  {
    "key": "nodeById",
    "type": "path",
    "value": "ns=2;i=23"
    "timeout": 5000
  },
]
```

#### Device RPC methods

| **Parameter**                             | **Default value** | **Description**                                                                  |
|:------------------------------------------|-------------------|----------------------------------------------------------------------------------|
| mapping[].rpc_methods[]                   |                   | List of RPC methods that will be sent to the device.                             |
| mapping[].rpc_methods[].method            |                   | Name of the method on the OPC-UA server.                                         |
| mapping[].rpc_methods[].arguments         |                   | (Optional) List of default arguments that will pass to the OPC-UA server method. |
| mapping[].rpc_methods[].arguments[].type  |                   | Type of the argument.                                                            |
| mapping[].rpc_methods[].arguments[].value |                   | (Optional) Value of the argument.                                                |
| mapping[].rpc_methods[].timeout (in ms)   | **5000**          | Timeout in milliseconds for the RPC method execution.                            |
| ---                                       |                   |                                                                                  |

Example of the RPC methods configuration:

```json
"rpc_methods": [
  {
    "timeout": 3000,
    "method": "multiply",
    "arguments": [
      {
        "type": "integer",
        "value": 2
      },
      {
        "type": "integer",
        "value": 4
      }
    ]
  },
]
```

## Additional information

### Path types

A Path type refers to the hierarchical address within the OPC-UA server's namespace. It is used to navigate to specific 
nodes in the server.

The path for the attribute value can be absolute or relative.

#### Absolute path

An **absolute path** specifies the full hierarchical address from the root of the OPC-UA server's namespace to the 
target node.

**Example:**

Gateway expects the node to exist and the value of "**Root\.Objects\.TempSensor\.Temperature**" to be **23.54**.

_Expression:_

`${Root\\.Objects\\.TempSensor\\.Temperature}`

_Converted data:_

`23.54`

#### Relative path

A **relative path** specifies the address relative to a predefined starting point in the OPC-UA server's namespace.

**Example:**

Gateway expects the node to exist and the value of “**Root\.Objects\.TempSensor\.Temperature**” to be 23.56.

_Device Node Expression:_

`Root\\.Objects\\.TempSensor`

_Expression:_

`${Temperature}`

_Converted data:_

`23.56`

### Identifier types

An **Identifier** type is a unique ID assigned to a node within the OPC-UA server. It is used to directly reference 
specific nodes without navigating through the namespace hierarchy.

The Identifier type in the OPC-UA connector configuration can take various forms to uniquely reference nodes 
in the OPC-UA server's address space. Identifiers can be of different types, such as numeric (`i`), string (`s`), 
byte string (`b`), and GUID (`g`). Below is an explanation of each identifier type with examples.

- **Numeric Identifier (`i`)**

  A **numeric identifier** uses an integer value to uniquely reference a node in the OPC-UA server.

  _Expression:_

  `${ns=2;i=1235}`
  
  _Converted data:_
  
  `21.34`

- **String Identifier (`s`)**

  A **string identifier** uses a string value to uniquely reference a node in the OPC-UA server.

  _Expression:_

  `${ns=3;s=TemperatureSensor}`
  
  _Converted data:_
  
  `21.34`

- **Byte String Identifier (`b`)**

  A **byte string identifier** uses a byte string to uniquely reference a node in the OPC-UA server. This is useful for binary data that can be converted to a byte string.

  _Expression:_

  `${ns=3;b=Q2xpZW50RGF0YQ==}`
  
  _Converted data:_
  
  `21.34`

- **GUID Identifier (`g`)**

  A **GUID identifier** uses a globally unique identifier (GUID) to uniquely reference a node in the OPC-UA server.

  _Expression:_

  `${ns=3;g=550e8400-e29b-41d4-a716-446655440000}`
  
  _Converted data:_
  
  `21.34`

## Next steps

Explore guides related to main SENTIENT features:
 - [How to connect OPC-UA device to SENTIENT using SENTIENT IoT Gateway](/docs/iot-gateway/guides/how-to-connect-opc-ua-device-to-sentient-ce/)
 - [SENTIENT IoT Gateway Features](/docs/iot-gateway/features/)
 - [Data Visualization](/docs/user-guide/dashboards/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine-2-0/overview/) - how to use rule engine to analyze data from devices.
