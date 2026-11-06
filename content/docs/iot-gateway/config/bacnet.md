+++
title = "BACnet Connector Configuration"
description = "BACnet protocol support for SENTIENT IoT Gateway"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/config/bacnet.md"
+++
## Overview

This documentation will help you set up the BACnet connector for the SENTIENT IoT Gateway. We’ll explain the
configuration parameters in simple terms to make it easy for you to understand and follow. The BACnet protocol is
widely used in building automation and control systems for applications such as heating, ventilation, air conditioning 
(HVAC), lighting control, access control, and fire detection systems. Use
[general configuration](/docs/iot-gateway/configuration/) to enable this extension.

The BACnet connector allows the SENTIENT IoT Gateway to communicate with BACnet devices, enabling data exchange and 
control capabilities. The connector can be configured via the user interface form, which helps you set up a connection 
to the BACnet devices, collect data and write data to devices. Let’s look at all the available settings and explain 
each one clearly. This will help you understand how everything works.


<div class="st-callout info">


**Please note**:
Connect the gateway before creating the connector. Otherwise, the UI will display the old configuration fields for
backward compatibility.


</div>


## Configuration modes

The BACnet connector can be configured in two modes: **Basic** and **Advanced**.

- **Basic** mode is designed for users who are new to SENTIENT IoT Gateway and want to quickly set up the connector
  with minimal configuration. It provides a simplified interface with essential settings.
- **Advanced** mode is intended for experienced users who need more control over the configuration. It offers additional
  options and flexibility for advanced use cases.


<div class="st-callout info">


**Please note:**
If you are new to IoT Gateway, use the "**Basic**" configuration mode. If you are familiar with configuring IoT Gateway,
you can use the "**Advanced**" configuration mode.


</div>


You can switch between these modes using the toggle button at the top of the configuration page:

![image](/images/gateway/bacnet-connector/bacnet-modes-toggle.webp)

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


![image](/images/gateway/bacnet-connector/bacnet-general-basic-1-ce.webp)


<div class="st-callout info">


The General tab in settings is the same for both the basic and advanced configurations.


</div>


## Application

Configuration in this section is used to configure the gateway in the BACnet network.
The following parameters are used to configure application settings:

- **Object Name** - the gateway object name in the BACnet network.
- **Host** - the gateway host in the BACnet network. **Make sure you use the correct network address where your devices are located so that the gateway can find them.**
- **Port** - the gateway port in the BACnet network.
- **Network mask** - the gateway mask in the BACnet network.
- **Object ID** - the gateway object identifier in the BACnet network.
- **Vendor ID** - the gateway vendor identifier in the BACnet network.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/bacnet/#advanced-configuration) section.


</div>


![image](/images/gateway/bacnet-connector/bacnet-application-basic-1-ce.webp)


## Advanced application settings

You can configure additional application settings like: APDU length, segmentation, network number and discovering timeout.

| **Parameter**                | **Default value** | **Description**                                                                                                  |
|:-----------------------------|:------------------|------------------------------------------------------------------------------------------------------------------|
| APDU Length (in bytes)       | **1476**          | Maximal length of the APDU.                                                                                      |
| Segmentation                 | **Both**          | Segmentation type for transmitting large BACnet messages. Can be: **Both**, **Transmit**, **Receive**, **None**. |
| Network number               | **3**             | Identifier of the network segment.                                                                               |
| Discovering timeout (in sec) | **5**             | Period of time when the connector will try to discover BACnet devices.                                           |
| ---                          |                   |                                                                                                                  |


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/bacnet/#advanced-configuration) section.


</div>


![image](/images/gateway/bacnet-connector/bacnet-advanced-application-settings.webp)

## Data mapping

This configuration section contains an array of BACnet devices that can be connected to the connector and send data.
Any BACnet device not included in this array will be rejected by the connector.

To add a new device, click the "**plus**" icon:

![image](/images/gateway/bacnet-connector/bacnet-gateway-configuring-1-ce.webp)

Provide the following fields in the opened model window:
- **Host** - the host of the device;
- **Port** - the port of the device;
- **Device name source** - the source of the device name, can be:
  - **Constant** - the device name is static;
  - **Expression** - the device name is an expression;
- **Device name value / expression** - the device name (you can find detail examples [here](/docs/iot-gateway/config/bacnet/#usage-examples));
- **Device profile source** - the source of the device profile, can be the same as the device name source;
- **Device profile value / expression** - the device profile name (you can find detail examples [here](/docs/iot-gateway/config/bacnet/#usage-examples));
- **Poll period** - the period of time when the connector will try to poll BACnet device;
- **Advanced configuration settings**:
  - **Alternative responses addresses** - the alternative address for responses from the device (you can find detail examples [here](/docs/iot-gateway/config/bacnet/#usage-examples)).
- **Report strategy** - strategy for sending data to SENTIENT:
  - **Report period** - period for sending data to SENTIENT in milliseconds;
  - **Type** - type of the report strategy:
    - **On report period** - sends data to SENTIENT after the report period;
    - **On value change** - sends data to SENTIENT when the value changes;
    - **On value change or report period** - sends data to SENTIENT when the value changes or after the report period;
    - **On received** - sends data to SENTIENT after receiving data from the device (default strategy).


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the
[Advanced configuration](/docs/iot-gateway/config/bacnet/#devices) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/bacnet/#usage-examples) section.

Additional information about the report strategy can be found [here](/docs/iot-gateway/features-overview/report-strategy).


</div>


![image](/images/gateway/bacnet-connector/bacnet-gateway-configuring-2-ce.webp)


### Attributes and Time series

This configuration section includes the parameters for handling incoming data. You can specify which data will be
treated as device attributes and which as time series. Attributes are used for storing static or infrequently changing
data, while time series are used for storing dynamic or frequently changing data.

Configuration in this subsection provides settings for processing data from BACnet device as timeseries and 
attributes on the platform instance.

To add new time series or attribute key, follow these steps:


1. Click “**pencil**” icon of the “**Attributes**” section to add new attribute key;

1. Click “**Add attribute**” in the opened window;

1. Enter the **key name**, select "Object ID" and "Property ID" from the dropdown list. Click “**Apply**”;

1. Now click on the “**pencil**” icon of the “**Time series**” section to add new time series key;

1. Click "**Add time series**" in the opened window;

1. Enter the **key name**, select "Object ID" and "Property ID" from the dropdown list. Click “**Apply**”.


<div class="st-gallery"><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-3-ce.webp" alt="Click “**pencil**” icon of the “**Attributes**” section to add new attribute key;" loading="lazy"><figcaption>Click “**pencil**” icon of the “**Attributes**” section to add new attribute key;</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-4-ce.webp" alt="Click “**Add attribute**” in the opened window;" loading="lazy"><figcaption>Click “**Add attribute**” in the opened window;</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-5-ce.webp" alt="Enter the **key name**, select &quot;Object ID&quot; and &quot;Property ID&quot; from the dropdown list. Click “**Apply**”;" loading="lazy"><figcaption>Enter the **key name**, select "Object ID" and "Property ID" from the dropdown list. Click “**Apply**”;</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-6-ce.webp" alt="Now click on the “**pencil**” icon of the “**Time series**” section to add new time series key;" loading="lazy"><figcaption>Now click on the “**pencil**” icon of the “**Time series**” section to add new time series key;</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-7-ce.webp" alt="Click &quot;**Add time series**&quot; in the opened window;" loading="lazy"><figcaption>Click "**Add time series**" in the opened window;</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-8-ce.webp" alt="Enter the **key name**, select &quot;Object ID&quot; and &quot;Property ID&quot; from the dropdown list. Click “**Apply**”." loading="lazy"><figcaption>Enter the **key name**, select "Object ID" and "Property ID" from the dropdown list. Click “**Apply**”.</figcaption></figure></div>


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the
[Advanced configuration](/docs/iot-gateway/config/bacnet/#device-attributes-and-time-series) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/bacnet/#usage-examples) section.


</div>


#### Filtering (from v.3.7.5 and only in advanced configuration mode)

You can set up filtering for time series and attributes based on Object Type, Object ID and Property ID. This allows 
you to specify which data should be collected and sent to the platform. Let's review each filtering option:

**Object Type Filtering**

This filter allows you to specify the type of BACnet objects from which data should be collected. For example, you can 
choose to collect data only from "**Analog Input**" or "**Binary Output**" object types or both:
- `"objectType": "*"` - will collect data from all [supported object types](/docs/iot-gateway/config/bacnet/#supported-object-types);
- `"objectType": "analogValue"` - will collect data only from Analog Value objects;
- `"objectType": ["analogValue", "binaryInput"]` - will collect data from both "Analog Value" and "Binary Input" objects.

**Object ID Filtering**

This filter allows you to specify particular Object IDs for data collection. You can define a single Object ID or a list
of Object IDs:
- `"objectId": 1234` - will collect data only from the object with ID 1234;
- `"objectId": "*"` - will collect data from all Object IDs;
- `"objectId": "0-10"` - will collect data from Object IDs in the range 0 to 10 (inclusive);
- `"objectId": ["0-10", "12-15"]` - will collect data from Object IDs in the ranges 0 to 10 and 12 to 15 (inclusive).

**Property ID Filtering**

This filter allows you to specify particular Property IDs for data collection. You can define a single Property ID or a list
of Property IDs:
- `"propertyId": "presentValue"` - will read only the "presentValue" property;
- `"propertyId": "*"` - will read all [supported properties](/docs/iot-gateway/config/bacnet/#supported-property-identifiers);
- `"propertyId": ["presentValue", "location"]` - will read both "presentValue" and "location" properties.


<div class="st-callout warn">


<div>
  <p>
    <b style="color:red">WARNING:</b>
    <span style="color:black">It is not allowed to use the Object Types list (except "*") with Object ID range or a list of ranges.</span>
  </p>
</div>


</div>


Example of filtering configuration:

```json
{
  "timeseries": [
    {
      "key": "${objectName} - ${objectType} | ${units}",
      "objectType": "analogInput",
      "objectId": "*",
      "propertyId": ["presentValue", "statusFlags"]
    }
  ]
}
```


<div class="st-callout info">


More usage examples can be found in the [Example usage](/docs/iot-gateway/config/bacnet/#usage-examples) section.


</div>


#### Report strategy

For each time series or attribute, you can enable specific report strategy. This strategy defines how often the 
data will be sent to the SENTIENT server. The following strategies are available:

- **On report period** - sends data to SENTIENT after the report period;
- **On value change** - sends data to SENTIENT when the value changes;
- **On value change or report period** - sends data to SENTIENT when the value changes or after the report period;
- **On received** - sends data to SENTIENT after receiving data from the device (default strategy).

![image](/images/gateway/bacnet-connector/bacnet-gateway-configuring-10-ce.webp)


<div class="st-callout info">


Additional information about the report strategy can be found [here](/docs/iot-gateway/features-overview/report-strategy).


</div>


### Usage examples


<div class="st-tabs">

<div class="st-tab" data-label="Dynamic device name/profile">

BACnet connector allows you to set dynamic device names and profiles using expressions. This is especially useful when 
you have multiple devices with similar configurations and want to differentiate them based on their properties.
In this example, we will configure a BACnet device to have a dynamic device name based on its `objectName` and `address` 
properties and a dynamic device profile based on its `vendorId` property.

Here is an example configuration snippet for a BACnet device with dynamic device name and profile:

```json
{
  "application": {
    "objectName": "TB_gateway",
    "host": "YOUR_HOST",
    "port": 47808,
    "mask": 24,
    "objectIdentifier": 599,
    "maxApduLengthAccepted": 1476,
    "segmentationSupported": "segmentedBoth",
    "vendorIdentifier": 15,
    "deviceDiscoveryTimeoutInSec": 5,
    "devicesDiscoverPeriodSeconds": 30
  },
  "devices": [
    {
      "host": "*",
      "port": "*",
      "pollPeriod": 10000,
      "deviceInfo": {
        "deviceNameExpressionSource": "expression",
        "deviceNameExpression": "${objectName} at ${address}",
        "deviceProfileExpressionSource": "expression",
        "deviceProfileExpression": "${vendorId}_profile"
      },
      "attributes": [],
      "timeseries": "*",
      "attributeUpdates": [],
      "serverSideRpc": []
    }
  ]
}
```


In this configuration:
- The `deviceNameExpression` is set to `${objectName} at ${address}`, which will create a device name that includes the 
  device's object name and address.
- The `deviceProfileExpression` is set to `${vendorId}_profile`, which will create a device profile name based on the vendor ID of the device.

After applying this configuration, the device will be created with a name and profile that reflect its specific 
properties. The screenshot below shows how the device appears in SENTIENT with the dynamic name and profile:

![image](/images/gateway/bacnet-connector/examples/dynamic-device-name-and-profile-overview.webp)

As you can see, the device name is generated based on the `objectName` and `address`, and the device profile is based 
on the `vendorId`.

Device name/profile dynamic expressions provide flexibility in managing multiple BACnet devices with varying 
configurations and can help in organizing devices effectively within SENTIENT.


<div class="st-callout info">


You can find full list of available variables in
the [Advanced configuration](/docs/iot-gateway/config/bacnet/#available-variables-for-device-nameprofile-expressions) section.


</div>


</div>

<div class="st-tab" data-label="Alternative responses addresses">

Alternative response addresses field allows you to specify an alternative IP address for device responses.
It is especially useful when the gateway and the BACnet device are located in different networks.

For example, consider the following network setup:

![image](/images/gateway/bacnet-connector/examples/alternative-responses-addresses-network-setup.webp)

In this setup, the gateway runs inside a Docker container and the BACnet device is located on a local network with IP 
address `192.168.1.200:45606` and is not directly accessible from the Docker container. BACPypes sends APDUs to the 
gateway without including the port number, making it impossible for the connector to determine whether a response came 
from an allowed device. When you configure an alternative response address, the connector uses this IP to correctly 
recognize and validate the device.

To configure the alternative response address, you need to add the `altResponsesAddresses` field to the device 
configuration. Here is an example configuration snippet:

```json
{
  "application": {
    "objectName": "TB_gateway",
    "host": "0.0.0.0",
    "port": 47808,
    "mask": 24,
    "objectIdentifier": 599,
    "maxApduLengthAccepted": 1476,
    "segmentationSupported": "segmentedBoth",
    "vendorIdentifier": 15,
    "deviceDiscoveryTimeoutInSec": 5,
    "devicesDiscoverPeriodSeconds": 30
  },
  "devices": [
    {
      "deviceInfo": {
        "deviceNameExpressionSource": "expression",
        "deviceNameExpression": "BACnet Device ${objectName}",
        "deviceProfileExpressionSource": "constant",
        "deviceProfileExpression": "default"
      },
      "host": "192.168.1.200",
      "port": 45606,
      "altResponsesAddresses": ["192.168.1.200"],
      "pollPeriod": 10000,
      "attributes": [],
      "timeseries": "*",
      "attributeUpdates": [],
      "serverSideRpc": []
    }
  ]
}
```


After applying this configuration, the connector will use the specified alternative response address 
`192.168.1.200:45606` to recognize and validate responses from the BACnet device. This ensures that the connector can
communicate effectively with the device even when they are located in different networks. As a result, you should see 
created device in SENTIENT:

![image](/images/gateway/bacnet-connector/examples/alternative-responses-addresses-overview.webp)


</div>

<div class="st-tab" data-label="Discovering all device(advanced configuration mode only)">

There are situations when there are many devices with the same list of objects, the values of which need to be read.
Copying the configuration for each device is not very convenient, so the BACnet connector allows you to automatically
find all devices on the network and connect them with the same configuration. To do this, you need to specify the host
and port of the device, as well as set templates for the device name and device profile.

Let's look at an example of how to properly configure automatic device discovery. 

Suppose we have two devices with the same list of objects:

| Object Type  | Object ID | Property ID   | Key         |
|--------------|-----------|---------------|-------------|
| Analog Input | 1         | Present Value | temperature |
| Binary Input | 1         | Present Value | relay       |
| Analog Input | 2         | Present Value | humidity    |
| Analog Input | 3         | Present Value | pressure    |
| ---          |           |               |             |

To configure automatic device discovery, use the following BACnet connector configuration:

```json
{
  "application": {
    "objectName": "TB_gateway",
    "host": "YOUR_HOST",
    "port": 47808,
    "objectIdentifier": 599,
    "vendorIdentifier": 15,
    "maxApduLengthAccepted": 1476,
    "segmentationSupported": "segmentedBoth",
    "deviceDiscoveryTimeoutInSec": 5
  },
  "devices": [
    {
      "altResponsesAddresses": [],
      "host": "*",
      "port": "*",
      "deviceInfo": {
        "deviceNameExpression": "${objectName}",
        "deviceProfileExpression": "default",
        "deviceNameExpressionSource": "expression",
        "deviceProfileExpressionSource": "constant"
      },
      "pollPeriod": 10000,
      "timeseries": [
        {
          "key": "temperature",
          "objectType": "analogInput",
          "objectId": 1,
          "propertyId": "presentValue"
        },
        {
          "key": "relay",
          "objectType": "binaryInput",
          "objectId": 1,
          "propertyId": "presentValue"
        },
        {
          "key": "humidity",
          "objectType": "analogInput",
          "objectId": 2,
          "propertyId": "presentValue"
        },
        {
          "key": "pressure",
          "objectType": "analogInput",
          "objectId": 3,
          "propertyId": "presentValue"
        }
      ],
      "attributes": [],
      "attributeUpdates": [],
      "serverSideRpc": []
    }
  ]
}
```


Below are the main parameters that you can use to properly configure automatic device detection. Let's take a closer 
look at them:

- `host` - you need to specify `*`, this is done so that the connector accepts all IAm messages from all devices on the
  network.
- `port` - you need to specify `*`, this is done so that the connector accepts all IAm messages from all devices on the
  network.
- `deviceNameExpression` - This is a template for the device name. `${objectName}` is used to match the device name to
  the object name in the BACnet network.
- `deviceProfileExpression` - This is a template for a device profile. In our case, we use `default` because all devices
  have the same type.

After saving the changes and starting the connector, it will send a WhoIs query to the network and start receiving IAm 
messages from all devices. After receiving the IAm message, the connector will automatically create a device for each 
device found with the specified templates and start reading data from the objects. The screenshot below shows what the 
device list looks like after automatic discovery:

![image](/images/gateway/bacnet-connector/examples/discovered-devices-overview.webp)


</div>

<div class="st-tab" data-label="Reading all device objects(advanced configuration mode only)">

There are situations when a BACnet device has a lot of objects, and you want to read all the objects of the device 
without having to manually add each object to the connector configuration. Or maybe you don't know what objects are in 
the device and want to read all the objects automatically. The BACnet connector supports this functionality and allows 
you to read all the objects of the device by easily configuring just one parameter.

Let's look at an example of how to properly configure reading all device objects.

In order to read all the device objects, you need to decide where exactly the values of these objects will be stored: 
in `telemetry` or `attributes`. Depending on this, you need to put `*` in the corresponding section.

In our case, we will store all objects in time series, so the device configuration will look like this:

```json
{
  "application": {
    "objectName": "TB_gateway",
    "host": "YOUR_HOST",
    "port": 47808,
    "objectIdentifier": 599,
    "vendorIdentifier": 15,
    "maxApduLengthAccepted": 1476,
    "segmentationSupported": "segmentedBoth",
    "deviceDiscoveryTimeoutInSec": 5
  },
  "devices": [
    {
      "altResponsesAddresses": [],
      "host": "YOUR_DEVICE_HOST",
      "port": 47808,
      "deviceInfo": {
        "deviceNameExpression": "${objectName}",
        "deviceProfileExpression": "default",
        "deviceNameExpressionSource": "expression",
        "deviceProfileExpressionSource": "constant"
      },
      "pollPeriod": 10000,
      "timeseries": "*",
      "attributes": [],
      "attributeUpdates": [],
      "serverSideRpc": []
    }
  ]
}
```


As you can see from the configuration above, we have put `*` in the `timeseries` section, which means that all device 
objects will be saved in the telemetry. In the `attributes` section, we have not put `*`, so the attributes will not 
be read.

After saving the changes and starting the connector, you can see that the corresponding device has been added to the 
platform, and its telemetry has started to fill with all the device objects:

![image](/images/gateway/bacnet-connector/examples/device-objects-overview.webp)


</div>

<div class="st-tab" data-label="Filtering objects and properties(advanced configuration mode only)">

There are situations when a BACnet device has a lot of objects, and you want to read only specific objects or 
properties from the device. You can use filtering options to specify which data should be collected and sent to the 
platform. 

Let's look at an example of how to properly configure filtering feature.

In our case, we have a device that have a lot of objects, but we want to read `presentValue` and `units` properties 
from only the first three `Analog Value` objects. In order to do this, we need to configure the filtering options 
in the attributes/timeseries section as shown below:

```json
{
  "application": {
    "objectName": "TB_gateway",
    "host": "YOUR_HOST",
    "port": 47808,
    "mask": "24",
    "objectIdentifier": 599,
    "maxApduLengthAccepted": 1476,
    "segmentationSupported": "segmentedBoth",
    "vendorIdentifier": 15,
    "deviceDiscoveryTimeoutInSec": 5,
    "devicesDiscoverPeriodSeconds": 30
  },
  "devices": [
    {
      "deviceInfo": {
        "deviceNameExpression": "BACnet Device ${objectName}",
        "deviceProfileExpression": "default",
        "deviceNameExpressionSource": "expression",
        "deviceProfileExpressionSource": "constant"
      },
      "altResponsesAddresses": [],
      "host": "YOUR_DEVICE_HOST",
      "port": "YOUR_DEVICE_PORT",
      "pollPeriod": 10000,
      "attributes": [],
      "timeseries": [
        {
          "key": "${objectName} ${objectType}",
          "objectType": "analogValue",
          "objectId": "1-3",
          "propertyId": ["presentValue", "units"]
        }
      ],
      "attributeUpdates": [],
      "serverSideRpc": []
    }
  ]
}
```


As you can see from the configuration above, we have specified `objectType` as `analogValue`, `objectId` as 
`1-3` (which means we want to read objects with IDs from 1 to 3), and `propertyId` as an array containing 
`presentValue` and `units`. This configuration will ensure that only the specified properties from the selected 
objects are read and sent to the platform. Also, we specified `key` as `${objectName} ${objectType}` to have more 
descriptive telemetry keys.

After saving the changes and starting the connector, you can see that the corresponding device has been added to the 
platform, and its telemetry has started to fill with the filtered data. The screenshot below shows an example of how 
the device telemetry looks like after applying the filtering configuration:

![image](/images/gateway/bacnet-connector/examples/filtering-objects-and-properties-overview.webp)


</div>

</div>


## Requests mapping

The Requests mapping section allows you to configure how the SENTIENT platform instance will interact with the 
devices. That is, how the platform will request data from the devices, how it will update device attributes, and how 
it will send RPC commands to the devices.

BACnet connector supports the following requests mapping:

- **Attribute updates** - allows update device objects values from SENTIENT platform instance.
- **RPC methods** - allows sending RPC commands to devices. Using RPC methods, you can get or set values of the BACnet
  device objects values. BACnet connector supports different types of RPC methods, such as:
  - **Reserved GET/SET methods** - these methods are automatically created for each attribute and time series parameter. You
    can use them to get or set values of the BACnet device objects values.
  - **Configurable RPC to device** - these methods allow you to configure custom RPC commands in connector configuration
    that can be sent to the devices.

### Attribute updates

This subsection contains configuration for attribute updates request from SENTIENT platform instance.

SENTIENT allows the provisioning of device attributes and fetches some of them from the device application. 
You can treat this as a remote configuration for devices, enabling them to request shared attributes from 
SENTIENT. See [user guide](/docs/user-guide/attributes/) for more details.

The following parameters are used to configure attribute updates:
- **Key** - the key of the shared attribute in SENTIENT. It can be specified as a static value.
- **Object ID** - the object id in the BACnet device.
- **Object Type** - the object type in the BACnet device.
- **Property ID** - the property id in the BACnet device.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the
[Advanced configuration](/docs/iot-gateway/config/bacnet/#device-attribute-updates) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/bacnet/#usage-examples-1) section.


</div>


![image](/images/gateway/bacnet-connector/attribute-updates-overview.webp)

In order to add new attribute update, follow these steps:


1. Click “**pencil**” icon of the “**Attribute updates**” subsection to add new attribute update;

1. Click “**Add attribute update**” in the opened window;

1. Fill in "**Key**" field, select "**Object ID**" and "**Property ID**" from the dropdown list. Click “**Apply**” button.


<div class="st-gallery"><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-11-ce.webp" alt="Click “**pencil**” icon of the “**Attribute updates**” subsection to add new attribute update;" loading="lazy"><figcaption>Click “**pencil**” icon of the “**Attribute updates**” subsection to add new attribute update;</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-12-ce.webp" alt="Click “**Add attribute update**” in the opened window;" loading="lazy"><figcaption>Click “**Add attribute update**” in the opened window;</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-13-ce.webp" alt="Fill in &quot;**Key**&quot; field, select &quot;**Object ID**&quot; and &quot;**Property ID**&quot; from the dropdown list. Click “**Apply**” button." loading="lazy"><figcaption>Fill in "**Key**" field, select "**Object ID**" and "**Property ID**" from the dropdown list. Click “**Apply**” button.</figcaption></figure></div>


### RPC methods

SENTIENT allows sending [RPC commands](https://sentient.invenia.in/docs/user-guide/rpc/) to devices connected directly to SENTIENT or via Gateway.
The following parameters are used to configure RPC methods:
- **Method** - the RPC method name.
- **Request Type** - “**writeProperty**” to write data and “**readProperty**” to read data.
- **Object ID** - the object id in the BACnet device.
- **Object Type** - the object type in the BACnet device.
- **Property ID** - the property id in the BACnet device.
- **Request Timeout** - timeout in milliseconds for the RPC method execution.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the
[Advanced configuration](/docs/iot-gateway/config/bacnet/#device-rpc-methods) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/bacnet/#usage-examples-1) section.


</div>


![image](/images/gateway/bacnet-connector/rpc-overview.webp)

In order to add a new RPC method, follow these steps:


1. Click “**pencil**” icon of the “**RPC methods**” section to add new RPC;

1. In the opened window click “**Add method**”;

1. Fill in "**Method**" field, select "**Request Type**", "**Object ID**", "**Property ID**" from the dropdown list. Click “**Apply**” button.


<div class="st-gallery"><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-14-ce.webp" alt="Click “**pencil**” icon of the “**RPC methods**” section to add new RPC;" loading="lazy"><figcaption>Click “**pencil**” icon of the “**RPC methods**” section to add new RPC;</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-15-ce.webp" alt="In the opened window click “**Add method**”;" loading="lazy"><figcaption>In the opened window click “**Add method**”;</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/bacnet-gateway-configuring-16-ce.webp" alt="Fill in &quot;**Method**&quot; field, select &quot;**Request Type**&quot;, &quot;**Object ID**&quot;, &quot;**Property ID**&quot; from the dropdown list. Click “**Apply**” button." loading="lazy"><figcaption>Fill in "**Method**" field, select "**Request Type**", "**Object ID**", "**Property ID**" from the dropdown list. Click “**Apply**” button.</figcaption></figure></div>


<div class="st-callout info">


Also, every telemetry and attribute parameter has built-in GET and SET RPC methods out of the box, so you don’t need to configure
it manually. See [the guide](/docs/iot-gateway/guides/how-to-use-get-set-rpc-methods).


</div>


### Usage examples


<div class="st-tabs">

<div class="st-tab" data-label="Attribute Updates">

Attribute updates allow you to update objects values on the BACnet device. You can add new attribute updates in the 
“**Attribute updates**” section of the device configuration page.

As an example, we will use a BACnet controller to which a relay is connected. We also know that the relay has the 
following object ID: `Binary Input:1`. We added this Object ID as a telemetry parameter with the key `relay`. We used 
telemetry so that later it would be convenient for us to see if the value we changed using the attribute update 
has changed. You, also, can add this telemetry datapoint to the device configuration or use the reserved `get` method 
to check the value of the node.

Let’s add an attribute update to our configuration. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created BACnet connector and click on the "**Devices**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Application settings](/docs/iot-gateway/config/bacnet/#application) and [Data mapping](/docs/iot-gateway/config/bacnet/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.

1. Scroll down to the “**Attribute updates**” section and click on the “**Pencil**” icon to edit the attribute updates.

1. Click on the “**Add attribute update**” button. In our case, we will add `relay` attribute update, so the “**Key**” field, enter `relay`, select the “**Object ID**” as **Analog Input** and "**1**", "**Property ID**" as "**Present Value**".

1. Remember to save your changes by clicking the “**Apply**” button and click save connector configuration button.


<div class="st-gallery"><figure><img src="/images/gateway/bacnet-connector/examples/select-created-gateway.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the left sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/select-connector-configuration.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/select-device-configuration.webp" alt="Select the created BACnet connector and click on the &quot;**Devices**&quot; tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Application settings](/docs/iot-gateway/config/bacnet/#application) and [Data mapping](/docs/iot-gateway/config/bacnet/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for." loading="lazy"><figcaption>Select the created BACnet connector and click on the "**Devices**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Application settings](/docs/iot-gateway/config/bacnet/#application) and [Data mapping](/docs/iot-gateway/config/bacnet/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/connector-configuration-attribute-updates-1.webp" alt="Scroll down to the “**Attribute updates**” section and click on the “**Pencil**” icon to edit the attribute updates." loading="lazy"><figcaption>Scroll down to the “**Attribute updates**” section and click on the “**Pencil**” icon to edit the attribute updates.</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/connector-configuration-attribute-updates-2.webp" alt="Click on the “**Add attribute update**” button. In our case, we will add `relay` attribute update, so the “**Key**” field, enter `relay`, select the “**Object ID**” as **Analog Input** and &quot;**1**&quot;, &quot;**Property ID**&quot; as &quot;**Present Value**&quot;." loading="lazy"><figcaption>Click on the “**Add attribute update**” button. In our case, we will add `relay` attribute update, so the “**Key**” field, enter `relay`, select the “**Object ID**” as **Analog Input** and "**1**", "**Property ID**" as "**Present Value**".</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/connector-configuration-attribute-updates-3.webp" alt="Remember to save your changes by clicking the “**Apply**” button and click save connector configuration button." loading="lazy"><figcaption>Remember to save your changes by clicking the “**Apply**” button and click save connector configuration button.</figcaption></figure></div>


Now we can check if the attribute update works. Go to "**Entities**" → "**Devices**" → select a created 
device → "**Attributes**" tab → select "**Shared attributes**" → click on the "**+**" icon and add `relay` attribute 
with type "**Boolean**" set it to "**True**".


<div class="st-gallery"><figure><img src="/images/gateway/bacnet-connector/examples/connector-configuration-attribute-updates-4.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/connector-configuration-attribute-updates-5.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Now, let’s check the value of the relay Object ID. In the selected device, go to the "**Last telemetry**" tab and 
check the value of the `relay` telemetry. It should be `true` since we set the shared attribute to `true`.

![image](/images/gateway/bacnet-connector/examples/connector-configuration-attribute-updates-6.webp)

Try to change the value of the `relay` shared attribute to `false`. After a few seconds, you should see that the
`relay` telemetry value has changed to `false`, which means that the attribute update worked correctly.

Full configuration for BACnet connector for the examples above will look like this 
(**make sure to use the right device host and port**):

```json
{
  "application": {
    "objectName": "TB_gateway",
    "host": "YOUR_HOST",
    "port": 47808,
    "objectIdentifier": 599,
    "vendorIdentifier": 15,
    "maxApduLengthAccepted": 1476,
    "segmentationSupported": "segmentedBoth",
    "networkNumber": 3,
    "deviceDiscoveryTimeoutInSec": 5
  },
  "devices": [
    {
      "altResponsesAddresses": [],
      "host": "YOUR_DEVICE_HOST",
      "port": 47808,
      "networkMask": "",
      "deviceInfo": {
        "deviceNameExpression": "${objectName}",
        "deviceProfileExpression": "default",
        "deviceNameExpressionSource": "expression",
        "deviceProfileExpressionSource": "constant"
      },
      "pollPeriod": 10000,
      "timeseries": [
        {
          "key": "relay",
          "objectType": "binaryInput",
          "objectId": 1,
          "propertyId": "presentValue"
        }
      ],
      "attributes": [],
      "attributeUpdates": [
        {
          "key": "relay",
          "objectType": "binaryInput",
          "objectId": 1,
          "propertyId": "presentValue"
        }
      ],
      "serverSideRpc": []
    }
  ]
}
```


</div>

<div class="st-tab" data-label="RPC to Device">

RPC to Device allows sending RPC commands to the device that is connected to SENTIENT directly 
or via Gateway.

As an example, we will use a BACnet controller with temperature sensor. We also know that the temperature sensor has the
following object ID: `Analog Value:1`, so we will read this value using RPC to Device. To call this method, first, 
we need to configure the BACnet connector to support RPC calls. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created BACnet connector and click on the "**Devices**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Application settings](/docs/iot-gateway/config/bacnet/#application) and [Data mapping](/docs/iot-gateway/config/bacnet/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.

1. Scroll down to the "**RPC methods**" section and click on the "**Pencil**" icon to edit the RPC methods.

1. Click on the "**Add method**" button. Fill in the "**Method**" field with `getTemperature`, select the "**Request Type**" as "**Read Property**", "**Object ID**" as "**Analog Value**" and "**1**", and "**Property ID**" as "**Present Value**".

1. Remember to save your changes by clicking the "**Apply**" button and click save connector configuration button.


<div class="st-gallery"><figure><img src="/images/gateway/bacnet-connector/examples/select-created-gateway.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the left sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/select-connector-configuration.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/select-device-configuration.webp" alt="Select the created BACnet connector and click on the &quot;**Devices**&quot; tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Application settings](/docs/iot-gateway/config/bacnet/#application) and [Data mapping](/docs/iot-gateway/config/bacnet/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for." loading="lazy"><figcaption>Select the created BACnet connector and click on the "**Devices**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Application settings](/docs/iot-gateway/config/bacnet/#application) and [Data mapping](/docs/iot-gateway/config/bacnet/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/rpc-to-device-1.webp" alt="Scroll down to the &quot;**RPC methods**&quot; section and click on the &quot;**Pencil**&quot; icon to edit the RPC methods." loading="lazy"><figcaption>Scroll down to the "**RPC methods**" section and click on the "**Pencil**" icon to edit the RPC methods.</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/rpc-to-device-2.webp" alt="Click on the &quot;**Add method**&quot; button. Fill in the &quot;**Method**&quot; field with `getTemperature`, select the &quot;**Request Type**&quot; as &quot;**Read Property**&quot;, &quot;**Object ID**&quot; as &quot;**Analog Value**&quot; and &quot;**1**&quot;, and &quot;**Property ID**&quot; as &quot;**Present Value**&quot;." loading="lazy"><figcaption>Click on the "**Add method**" button. Fill in the "**Method**" field with `getTemperature`, select the "**Request Type**" as "**Read Property**", "**Object ID**" as "**Analog Value**" and "**1**", and "**Property ID**" as "**Present Value**".</figcaption></figure><figure><img src="/images/gateway/bacnet-connector/examples/rpc-to-device-3.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button and click save connector configuration button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button and click save connector configuration button.</figcaption></figure></div>


We are done with configuration, so let's check how to call the method. In the RPC Debug Terminal widget, run the 
following command:

```bash
getTemperature
```

Response:

![image](/images/gateway/bacnet-connector/examples/rpc-to-device-4.webp)


<div class="st-callout info">


The RPC Debug Terminal is used only for example purpose, so you can use any other widget that supports RPC calls.


</div>


Full configuration for BACnet connector for the example above will look like 
this (**make sure to use the right device host and port**):

```json
{
  "application": {
    "objectName": "TB_gateway",
    "host": "YOUR_HOST",
    "port": 47808,
    "objectIdentifier": 599,
    "vendorIdentifier": 15,
    "maxApduLengthAccepted": 1476,
    "segmentationSupported": "segmentedBoth",
    "deviceDiscoveryTimeoutInSec": 5
  },
  "devices": [
    {
      "altResponsesAddresses": [],
      "host": "YOUR_DEVICE_HOST",
      "port": 47808,
      "deviceInfo": {
        "deviceNameExpression": "${objectName}",
        "deviceProfileExpression": "default",
        "deviceNameExpressionSource": "expression",
        "deviceProfileExpressionSource": "constant"
      },
      "pollPeriod": 10000,
      "timeseries": [
        {
          "key": "some-key",
          "objectType": "binaryInput",
          "objectId": 1,
          "propertyId": "presentValue"
        }
      ],
      "attributes": [],
      "attributeUpdates": [],
      "serverSideRpc": [
        {
          "method": "getTemperature",
          "objectType": "analogValue",
          "objectId": 1,
          "propertyId": "presentValue",
          "timeout": 5000,
          "requestType": "readProperty"
        }
      ]
    }
  ]
}
```


</div>

<div class="st-tab" data-label="Reserved RPCs">

Every telemetry and attribute parameter has `GET` and `SET` RPC methods out of the box, so you don’t need to configure 
them manually.

As an example, we will use a BACnet controller to which a relay is connected. We also know that the relay has the 
following object ID: `Binary Input:1`.

We will use this object ID to read the value of the relay using the `GET` RPC method and to set the value of the relay 
using the `SET` RPC method. The configuration for this telemetry will look like this:

```json
{
  "key": "relay",
  "objectType": "binaryInput",
  "objectId": 1,
  "propertyId": "presentValue"
}
```

Let’s check the value of the relay using the reserved `GET` method. To get the current value of the relay, run the query
in the RPC debug terminal:

```bash
get objectType=binaryInput;objectId=1;propertyId=presentValue;
```

Response:

```json
{"result": {"value":  "inactive"}}
```

![image](/images/gateway/bacnet-connector/examples/reserved-rpc-result-1.webp)

So, the `GET` method returns the current value of the relay, and we can see that the relay is off.


<div class="st-callout info">


The RPC Debug Terminal is used only for example purpose, so you can use any other widget that supports RPC calls.


</div>


To set the value of the relay and turn it on, run the query:

```bash
set objectType=binaryInput;objectId=1;propertyId=presentValue;value=1;
```

Response:

```json
{"result": {"value": 1}}
```

And as you can see, from the screenshot below, the relay telemetry value has changed to `1`:

![image](/images/gateway/bacnet-connector/examples/reserved-rpc-result-2.webp)

Also, let’s check the value of the relay telemetry again:

```bash
get objectType=binaryInput;objectId=1;propertyId=presentValue;
```

Response:

```json
{"result": {"value":  "active"}}
```

![image](/images/gateway/bacnet-connector/examples/reserved-rpc-result-3.webp)

Full configuration for BACnet connector for the examples above will look like this 
(**make sure to use the right device host and port**):

```json
{
  "application": {
    "objectName": "TB_gateway",
    "host": "YOUR_HOST",
    "port": 47808,
    "objectIdentifier": 599,
    "vendorIdentifier": 15,
    "maxApduLengthAccepted": 1476,
    "segmentationSupported": "segmentedBoth",
    "deviceDiscoveryTimeoutInSec": 5
  },
  "devices": [
    {
      "altResponsesAddresses": [],
      "host": "YOUR_DEVICE_HOST",
      "port": 47808,
      "deviceInfo": {
        "deviceNameExpression": "${objectName}",
        "deviceProfileExpression": "default",
        "deviceNameExpressionSource": "expression",
        "deviceProfileExpressionSource": "constant"
      },
      "pollPeriod": 10000,
      "timeseries": [
        {
          "key": "relay",
          "objectType": "binaryInput",
          "objectId": 1,
          "propertyId": "presentValue"
        }
      ],
      "attributes": [],
      "attributeUpdates": [],
      "serverSideRpc": []
    }
  ]
}
```


</div>

</div>


## EDE files parsing (Advanced configuration mode only)

The BACnet connector supports EDE files parsing. EDE (Engineering Data Exchange) files are used to describe the
structure and properties of BACnet devices. By parsing EDE files, the BACnet connector can automatically configure
itself to interact with the devices described in the files.

To use EDE files parsing, you need to provide the path to the EDE file in the connector configuration. The connector
will then read the file and extract the necessary information to communicate with the BACnet devices.
The EDE file should be in CSV format and follow the BACnet EDE schema.

Let’s look at the example of the EDE file parsing configuration.

We will use an EDE file exported from YABE (Yet Another BACnet Explorer) application. The file contains the
description of a BACnet device with several objects. The file looks like this:

![image](/images/gateway/bacnet-connector/ede-file-overview.webp)

Now let’s configure the BACnet connector to use this EDE file. In the advanced configuration mode, paste the following
connector configuration (**make sure to use the correct path to your EDE file**):

```json
{
  "application": {
    "objectName": "TB_gateway",
    "host": "YOUR_HOST",
    "port": 47808,
    "objectIdentifier": 599,
    "vendorIdentifier": 15,
    "maxApduLengthAccepted": 1476,
    "segmentationSupported": "segmentedBoth",
    "deviceDiscoveryTimeoutInSec": 5
  },
  "edeFilePath": "/path/to/your/file.ede"
}
```


<div class="st-callout info">


**Please note**:
- The EDE file parsing is available only in the **Advanced** configuration mode.
- The EDE file should be accessible by the IoT Gateway.


</div>


After applying the configuration, the BACnet connector will parse the EDE file and automatically configure itself to
interact with the BACnet device described in the file. You can then use the connector to read data from the device,
update device attributes, and send RPC commands to the device. As you can see on the screenshot below, the connector
has automatically created the device with the name and profile from the EDE file, as well as all the attributes and time
series from the file:

![image](/images/gateway/bacnet-connector/ede-device-overview.webp)

## Advanced configuration

The advanced configuration section provides a detailed overview of all available parameters for the BACnet connector.

### Application

The application configuration parameters are used to configure the gateway in the BACnet network.

| **Parameter**                                          | **Default value**       | **Description**                                                                                                       |
|:-------------------------------------------------------|:------------------------|-----------------------------------------------------------------------------------------------------------------------|
| application.objectName                                 | **SENTIENT IoT Gateway** | The gateway object name in the BACnet network.                                                                        |
| application.host                                       |                         | The gateway host in the BACnet network                                                                                |
| application.port                                       | **47808**               | The gateway port in the BACnet network.                                                                               |
| application.mask                                       |                         | The gateway mask in the BACnet network.                                                                               |
| application.networkNumber                              |                         | Identifier of the network segment.                                                                                    |
| application.objectIdentifier                           | **599**                 | The gateway object identifier in the BACnet network.                                                                  |
| application.vendorIdentifier                           | **15**                  | The gateway vendor identifier in the BACnet network.                                                                  |
| application.maxApduLengthAccepted                      | **1476**                | Maximal length of the APDU.                                                                                           |
| application.segmentationSupported                      | **segmentedBoth**       | The type of segmentation, can be: **segmentedBoth**, **segmentedTransmit**, **segmentedReceive**, **noSegmentation**. |
| application.deviceDiscoveryTimeoutInSec (in sec)       | **5**                   | Timeout for discovering devices.                                                                                      |
| application.devicesDiscoverPeriodSeconds (in sec)      | **30**                  | Period of time when the connector will try to discover BACnet devices.                                                |
| application.devicesRescanObjectsPeriodSeconds (in sec) | **60**                  | The period of time when the connector will try to reread device objects that it failed to read last time.             |
| application.loadProprietaryDevices *                   | **false**               | Allow dynamically loading proprietary devices from extensions.                                                        |
| ---                                                    |                         |                                                                                                                       |


<div class="st-callout info">


\* -- Feature available from Gateway v.3.8.0 and only in advanced configuration mode. You need to upload your 
proprietary device extension to the `/extensions/bacnet/proprietary` folder of the IoT Gateway installation directory. 
You can also find an example of such a proprietary device [here](https://github.com/sentient/sentient-gateway/blob/master/sentient_gateway/extensions/bacnet/proprietary/desigo_cc.py).


</div>


Example of the application configuration:

```json
{
  "application": {
    "objectName": "TB_gateway",
    "host": "192.168.1.168",
    "port": 47808,
    "objectIdentifier": 599,
    "vendorIdentifier": 15,
    "maxApduLengthAccepted": 1476,
    "segmentationSupported": "segmentedBoth",
    "networkNumber": 3,
    "deviceDiscoveryTimeoutInSec": 5
  }
}
```

### Foreign device (v.3.7.6+)

The foreign device configuration parameters are used to configure the gateway as a foreign device in the BACnet network.
It is useful when the gateway is behind a NAT and needs to register with a BACnet Broadcast Management Device (BBMD).

| **Parameter**              | **Default value** | **Description**                                   |
|:---------------------------|-------------------|---------------------------------------------------|
| foreignDevice.ttl (in sec) | **900**           | Time to live for the foreign device registration. |
| foreignDevice.address      | **0.0.0.0**       | The address of the BBMD to register with.         |
| ---                        |                   |                                                   |

### Devices

The device list contains an array of BACnet devices that can be connected to the connector and interact with them. 
Any BACnet device not included in this array will be rejected by the connector.

| **Parameter**                                      | **Description**                                                                                                                             |
|:---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| devices[].host                                     | The host of the device.                                                                                                                     |
| devices[].port                                     | The port of the device.                                                                                                                     |
| devices[].mask                                     | The mask of the device.                                                                                                                     |
| devices[].networkMask                              | The identifier of the device network segment.                                                                                               |
| devices[].pollPeriod                               | The period of time when the connector will try to poll the BACnet device.                                                                   |
| devices[].altResponsesAddresses[]                  | Array of alternative addresses for device responses (you can find detail examples [here](/docs/iot-gateway/config/bacnet/#usage-examples)). |
| devices[].reportStrategy                           | Report strategy object using for configuring report strategy for device.                                                                    |                                          
| devices[].deviceInfo                               | Device info object using for configuring device name and profile.                                                                           |
| devices[].deviceInfo.deviceNameExpressionSource    | The source of the device name: **constant**, **expression**.                                                                                |
| devices[].deviceInfo.deviceNameExpression          | The device name (you can find detail examples [here](/docs/iot-gateway/config/bacnet/#usage-examples)).                                     |
| devices[].deviceInfo.deviceProfileExpressionSource | The source of the device profile: **constant**, **expression**.                                                                             |
| devices[].deviceInfo.deviceProfileExpression       | The device profile name (you can find detail examples [here](/docs/iot-gateway/config/bacnet/#usage-examples)).                             |
| ---                                                |                                                                                                                                             |

Example of the device mapping configuration:

```json
{
  "devices": [
    {
      "deviceInfo": {
        "deviceNameExpression": "BACnet Device ${objectName}",
        "deviceProfileExpression": "default",
        "deviceNameExpressionSource": "expression",
        "deviceProfileExpressionSource": "constant"
      },
      "host": "192.168.2.110",
      "port": "47808",
      "pollPeriod": 10000,
      "attributes": [],
      "timeseries": [],
      "attributeUpdates": [],
      "serverSideRpc": []
    }
  ]
}
```

#### Available variables for device name/profile expressions

You can use the following parameters for forming device name and profile:
- `${objectName}` - the device object name of the BACnet device.
- `${objectId}` - the device object identifier of the BACnet device.
- `${vendorId}` - the device vendor identifier of the BACnet device.
- `${address}` - the device host address.
- `${routerId}` - the device router identifier.
- `${routerName}` - the device router name.
- `${routerAddress}` - the device router address.
- `${routerVendorId}` - the device router vendor identifier.

You can find detail examples [here](/docs/iot-gateway/config/bacnet/#usage-examples).

#### Device attributes and time series

| **Parameter**                         | **Description**                                                                                                 |
|:--------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| devices[].attributes[]                | This subsection contains parameters of the device data, that will be interpreted as attributes for the device.  |
| devices[].attributes[].key            | The name for time series on the platform.                                                                       |
| devices[].attributes[].objectType     | The object type in the BACnet device.                                                                           |
| devices[].attributes[].objectId       | The object id in the BACnet device.                                                                             |
| devices[].attributes[].propertyId     | The property id in the BACnet device.                                                                           |
| devices[].attributes[].reportStrategy | Report strategy object using for configuring report strategy for device attribute.                              |
| devices[].timeseries[]                | This subsection contains parameters of the device data, that will be interpreted as time series for the device. |
| devices[].timeseries[].key            | The name for time series on the platform.                                                                       |
| devices[].timeseries[].objectType     | The object type in the BACnet device.                                                                           |
| devices[].timeseries[].objectId       | The object id in the BACnet device.                                                                             |
| devices[].timeseries[].propertyId     | The property id in the BACnet device.                                                                           |
| devices[].timeseries[].reportStrategy | Report strategy object using for configuring report strategy for device time series.                            |
| ---                                   |                                                                                                                 |

Example of the device attributes and time series configuration:

```json
{
  "attributes": [
    {
      "key": "location",
      "objectType": "analogValue",
      "objectId": 1,
      "propertyId": "presentValue"
    }
  ],
  "timeseries": [
    {
      "key": "temperature",
      "objectType": "analogInput",
      "objectId": 2,
      "propertyId": "presentValue"
    }
  ]
}
```

#### Device attribute updates

| **Parameter**                                | **Default value** | **Description**                                           |
|:---------------------------------------------|-------------------|-----------------------------------------------------------|
| devices[].attributeUpdates[]                 |                   | List of attributes that will be updated on the device.    |
| devices[].attributeUpdates[].key             |                   | The name of the shared attribute on platform instance.    |
| devices[].attributeUpdates[].objectType      |                   | The object type in the BACnet device.                     |
| devices[].attributeUpdates[].objectId        |                   | The object id in the BACnet device.                       |
| devices[].attributeUpdates[].propertyId      |                   | The property id in the BACnet device.                     |
| devices[].attributeUpdates[].timeout (in ms) | **5000**          | Timeout in milliseconds for the attribute update request. |
| ---                                          |                   |                                                           |

Example of the device attribute updates configuration:

```json
{
  "attributeUpdates": [
    {
      "key": "setpoint",
      "objectType": "analogValue",
      "objectId": 3,
      "propertyId": "presentValue",
      "timeout": 5000
    }
  ]
}
```

#### Device RPC methods

| **Parameter**                             | **Default value** | **Description**                                                               |
|:------------------------------------------|:------------------|-------------------------------------------------------------------------------|
| devices[].serverSideRpc[]                 |                   | List of RPC methods that will be sent to the device.                          |
| devices[].serverSideRpc[].method          |                   | RPC method name.                                                              |
| devices[].serverSideRpc[].requestType     |                   | “**writeProperty**” to write data and “**readProperty**” to read data.        |
| devices[].serverSideRpc[].objectType      |                   | The object type in the BACnet device.                                         |
| devices[].serverSideRpc[].objectId        |                   | The object id in the BACnet device.                                           |
| devices[].serverSideRpc[].propertyId      |                   | The property id in the BACnet device.                                         |
| devices[].serverSideRpc[].priority        |                   | Priority of the value to write (optional, should be an integer from 1 to 16). |
| devices[].serverSideRpc[].timeout (in ms) | **5000**          | Timeout in milliseconds for the RPC method execution.                         |
| ---                                       |                   |                                                                               |

Example of the device RPC methods configuration:

```json
{
  "serverSideRpc": [
    {
      "method": "set_state",
      "requestType": "writeProperty",
      "objectType": "analogValue",
      "objectId": 3,
      "propertyId": "presentValue",
      "timeout": 5000
    }
  ]
}
```

## Additional information

### Supported Object Types

The BACnet connector support the following BACnet object types:

| **BACnet object id** | **SENTIENT object id** |
|----------------------|---------------------------|
| **Binary input**     | **binaryInput**           |
| **Binary Output**    | **binaryOutput**          |
| **Binary Value**     | **binaryValue**           |
| **Analog Input**     | **analogInput**           |
| **Analog Output**    | **analogOutput**          |
| **Analog Value**     | **analogValue**           |
| **Schedule Object**  | **schedule**              |
| ---                  | ---                       |

### Supported Property Identifiers

Property identifiers depend on type of the BACnet object, provided in camelCase, e.g:
- presentValue
- objectName
- objectDescription
- units
- eventState
- outOfService
- priorityArray
- relinquishDefault
- currentCommandPriority
- eventMessageTexts
- eventMessageTextsConfig
- eventAlgorithmInhibitReference
- timeDelayNormal
- weeklySchedule
- listOfObjectPropertyReferences
- location

## Troubleshooting

### Device discovery issues on Linux with Docker Compose

If you are running Gateway via docker compose on Linux, and you have issues with device discovery, make sure that you 
have set the correct network mode in the docker compose file. So you should add the following line to `tb-gateway` 
service in your docker compose file:

```yaml
network_mode: "host"
extra_hosts:
    - "host.docker.internal:host-gateway"
```


### Device discovery issues on Windows with Docker Compose

BACnet connector doesn't support device discovery on Windows OS due to the limitations of the Docker networking stack 
on Windows. Please use installation from source or other installation methods to run Gateway on Windows OS.

## Next steps

Explore guides related to main SENTIENT features:

 - [Data Visualization](/docs/user-guide/visualization/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine/) - how to use rule engine to analyze data from devices.
