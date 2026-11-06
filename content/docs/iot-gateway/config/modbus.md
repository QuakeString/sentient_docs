+++
title = "Modbus Connector Configuration"
description = "Modbus protocol support for SENTIENT IoT Gateway"


[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/config/modbus.md"
+++
## Overview

This documentation will help you set up the Modbus connector for the SENTIENT IoT Gateway. We’ll explain the
configuration parameters in simple terms to make it easy for you to understand and follow. The Modbus is a widely used
protocol for industrial automation and control systems, allowing devices to communicate with each other over a network,
and this connector allows seamless integration with the SENTIENT platform. Use
[general configuration](/docs/iot-gateway/configuration/) to enable this extension.

Also, if you are new to SENTIENT IoT Gateway, we recommend you to read the
[Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus)
guide to understand the basic concepts of SENTIENT IoT Gateway and how it works with Modbus protocol.

The connector can be configured via the user interface form, which helps you set up a connection to the Modbus server,
collect data and write data to slaves (devices). Let’s look at all the available settings and explain each one clearly. This will
help you understand how everything works.


<div id="video">
    <div id="video_wrapper">
        <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/kBMcsg7YEcQ" frameborder="0" allowfullscreen></iframe>
    </div>
</div>


<div class="st-callout info">


**Please note**:
Connect the gateway before creating the connector. Otherwise, the UI will display the old configuration fields for
backward compatibility.


</div>


## Configuration modes

The Modbus connector can be configured in two modes: **Basic** and **Advanced**.

- **Basic** mode is designed for users who are new to SENTIENT IoT Gateway and want to quickly set up the connector
  with minimal configuration. It provides a simplified interface with essential settings.
- **Advanced** mode is intended for experienced users who need more control over the configuration. It offers additional
  options and flexibility for advanced use cases.


<div class="st-callout info">


**Please note:**
If you are new to IoT Gateway, use the "Basic" configuration mode. If you are familiar with configuring IoT Gateway,
you can use the "Advanced" configuration mode.


</div>


You can switch between these modes using the toggle button at the top of the configuration page:

![image](/images/gateway/modbus-connector/modbus-modes-toggle.webp)

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


![image](/images/gateway/modbus-connector/modbus-general-basic-section-1-ce.webp)


<div class="st-callout info">


The general tab is the same for both the basic and advanced configurations.


</div>


## Master connections (Gateway as a Master) settings

A Modbus Master is used to query data from Modbus servers (slaves). In order to configure servers for data retrieving,
you need to specify list of slaves.

![image](/images/gateway/modbus-connector/gateway-as-a-master.webp)

### Servers (Slaves) settings

A Modbus Slave is a device that responds to requests from a Modbus Master. In this section, you can configure the
Modbus slaves that the master will query data from. You can add multiple slaves to the list, and each slave can have
its own configuration.

The following parameters are used to configure the slave device, its name and profile, as well as for 
report strategy:

- **Unit ID** - ID of the Modbus slave.
- **Device name** - name of the device on the platform.
- **Device profile** - device profile name on the platform.
- **Report strategy**  strategy for sending data to SENTIENT:
  - **Report period** - period for sending data to SENTIENT in milliseconds;
  - **Type** - type of the report strategy: 
    - **On report period** - sends data to SENTIENT after the report period;
    - **On value change** - sends data to SENTIENT when the value changes;
    - **On value change or report period** - sends data to SENTIENT when the value changes or after the report period;
    - **On received** - sends data to SENTIENT after receiving data from the device (default strategy).


<div class="st-callout info">


Additional information about the report strategy can be found [here](/docs/iot-gateway/features-overview/report-strategy).

All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/modbus/#device-mapping) section.


</div>


To add a new configuration for connection to server, navigate to the "**Master Connections**" tab and click the 
"**plus**" icon:

![image](/images/gateway/modbus-connector/add-new-server-connection-1-ce.webp)

### Connection settings

Due to the nature of preferred way of communication between Modbus master there are 3 options how to configure this 
part: if using TCP, UDP or via Serial port.


<div class="st-callout info">

 
All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/modbus/#device-mapping) section.


</div>


<div class="st-tabs">

<div class="st-tab" data-label="TCP">

The following parameters are used to configure TCP connection for the slave:

- **Host** - hostname or IP address of the Modbus server.
- **Port** - port of the Modbus server for connection.
- **Method** - type of a framer, either **Socket** or **RTU**.

![image](/images/gateway/modbus-connector/tcp-server-connection-section.webp)


</div>

<div class="st-tab" data-label="UDP">

The following parameters are used to configure UDP connection for the slave:

- **Host** - hostname or IP address of the Modbus server.
- **Port** - port of the Modbus server for connection.
- **Method** - type of a framer, either **Socket** or **RTU**.

![image](/images/gateway/modbus-connector/udp-server-connection-section.webp)

</div>

<div class="st-tab" data-label="Serial">

The following parameters are used to configure serial connection for the slave:

- **Port** - port of the Modbus server for connection.
- **Method** - type of a framer, either **ASCII** or **RTU**.
- **Baudrate** - The baud rate to use for the serial device.
- **Bytesize** - The number of bits in a byte of serial data. This can be one of **5**, **6**, **7**, or **8**.
- **Stopbits** - The number of bits sent after each character in a message to indicate the end of the byte.
- **Parity** - The type of checksum to use to verify data integrity. This can be one of the following: (**E**)ven, (**O**)dd, (**N**)one.

![image](/images/gateway/modbus-connector/serial-server-connection-section.webp)


</div>

</div>


### Advanced connection settings

You can configure additional settings like: TLS connection, polling time, byte order and word order, and other. 
The table below describes the parameters for this purpose:

| **Parameter**                   | **Default value** | **Description**                                                               |
|:--------------------------------|:------------------|-------------------------------------------------------------------------------|
| Connection timeout (s)          | **35**            | Timeout in seconds for connecting to Modbus server                            |
| Byte order                      | **LITTLE**        | Order of bytes to read                                                        |
| Word order                      | **LITTLE**        | The order of words when reading several registers                             |
| Retries                         | **true**          | Retrying sending data to the master. The values can be either: true or false  |
| Retries on empty                | **true**          | Retrying sending data to the master if it is empty                            |
| Retries on invalid              | **true**          | Retrying sending data to the master if it is failed                           |
| Poll period (ms)                | **5000**          | Period in milliseconds to check the attributes and the telemetry on the slave |
| Connect attempt time (ms)       | **5000**          | A waiting period in milliseconds before connecting to the master              |
| Connect attempt count           | **5**             | The number of connection attempts made through the SENTIENT gateway        |
| Wait after failed attempts (ms) | **300000**        | A waiting period in milliseconds before trying to send data to the master     |
| ---                             |                   |                                                                               |


1. Click on the "**Advanced connection settings**" subsection to open it;

1. Make the necessary settings.


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/advanced-connection-settings-1-ce.webp" alt="Click on the &quot;**Advanced connection settings**&quot; subsection to open it;" loading="lazy"><figcaption>Click on the "**Advanced connection settings**" subsection to open it;</figcaption></figure><figure><img src="/images/gateway/modbus-connector/advanced-connection-settings-2-ce.webp" alt="Make the necessary settings." loading="lazy"><figcaption>Make the necessary settings.</figcaption></figure></div>


Also, you can configure TLS connection (**can be used only for TCP/UDP connection type**). The table below describes the 
parameters required to configure TLS connection:

| **Parameter**                   | **Description**                                             |
|:--------------------------------|:------------------------------------------------------------|
| Path to client certificate file | Path to certificate file in filesystem with gateway         |
| Path to private key file        | Path to private key file                                    | 
| Password                        | Server password                                             |
| Server hostname                 | Server hostname (Should match with hostname in certificate) |
| ---                             |                                                             |

![image](/images/gateway/modbus-connector/tls-connection.webp)


### Data mapping

In the data mapping, you can specify how the Modbus master will interact with the slaves. This includes reading data from 
the slaves. You can also use this section to configure which data will be sent as device attributes or telemetry. 
Data mapping contains all the necessary settings for flexible data management.

#### Attributes and time series

The configuration in this unit provides settings for processing data on Modbus server. These settings will be 
interpreted in SENTIENT platform instance as attributes/time series of the device. The following parameters are used 
to configure device attributes and time series:

- **Key** - key of the attribute or time series on the platform.
- **Type** - data type of the Modbus register.
- **Function code** - Modbus function code for reading the register.
- **Objects count** - number of registers to read.
- **Address** - address of the register on the Modbus server.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/modbus/#device-mapping) section.


</div>


![image](/images/gateway/modbus-connector/attributes-and-timeseries-overview.webp)

For adding a new attribute or time series, use the following steps:


1. Click on "**pencil**" icon in the "Attributes" or "**Time series**" section (depends on the selected section);

1. In the opened window click "**Add attribute**" or "**Add time series**" (depends on selected section);

1. Fill in key, type, function code, objects count and address fields. Click "Apply".


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/attributes-1-ce.webp" alt="Click on &quot;**pencil**&quot; icon in the &quot;Attributes&quot; or &quot;**Time series**&quot; section (depends on the selected section);" loading="lazy"><figcaption>Click on "**pencil**" icon in the "Attributes" or "**Time series**" section (depends on the selected section);</figcaption></figure><figure><img src="/images/gateway/modbus-connector/attributes-2-ce.webp" alt="In the opened window click &quot;**Add attribute**&quot; or &quot;**Add time series**&quot; (depends on selected section);" loading="lazy"><figcaption>In the opened window click "**Add attribute**" or "**Add time series**" (depends on selected section);</figcaption></figure><figure><img src="/images/gateway/modbus-connector/attributes-3-ce.webp" alt="Fill in key, type, function code, objects count and address fields. Click &quot;Apply&quot;." loading="lazy"><figcaption>Fill in key, type, function code, objects count and address fields. Click "Apply".</figcaption></figure></div>


##### Report strategy

You can enable a specific report strategy for each time series or attribute. This strategy defines how often
data is sent to the SENTIENT server. The following strategies are available:

- **On report period** - sends data to SENTIENT after the report period;
- **On value change** - sends data to SENTIENT when the value changes;
- **On value change or report period** - sends data to SENTIENT when the value changes or after the report period;
- **On received** - sends data to SENTIENT after receiving data from the device (default strategy).


<div class="st-callout info">


Additional information about the report strategy can be found [here](/docs/iot-gateway/features-overview/report-strategy).


</div>


##### Enum mapping


<div class="st-callout info">


Feature available since SENTIENT IoT Gateway v.3.8.1 and only in advanced configuration mode.


</div>


You can map register values to human-readable strings using the enum mapping feature. This is particularly 
useful for registers where value denotes a state of the device instead of a "sensor value". Enum mapping works with 
all register types. Uplink `RPC to Device` calls can use enum mapping to get interpreted values.
Also, enum mapping works with batch reading as expected.

In order to set up enum mapping for a specific attribute or time series, you need to define the `variants` parameter in the
configuration. This parameter is an object where each key represents a possible register value, and the corresponding
value is the human-readable string that describes that register value.

Example of enum mapping configuration:
```json
{
  "tag": "status",
  "type": "16int",
  "address": 1,
  "objectsCount": 1,
  "functionCode": 3,
  "variants": {
    "0": "Stopped",
    "1": "Booting",
    "2": "Running"
  }
}
```

Example of enum mapping configuration for coil register:
```json
{
  "tag": "relay",
  "type": "bits",
  "address": 1,
  "objectsCount": 1,
  "functionCode": 1,
  "bitTargetType": "int",
  "variants": {
    "0": "Disable",
    "1": "Enable"
  }
}
```

Example of enum mapping configuration for `RPC to Device` call:
```json
{
  "method": "getStatus",
  "type": "16int",
  "address": 1,
  "objectsCount": 1,
  "functionCode": 3,
  "variants": {
    "0": "Stopped",
    "1": "Booting",
    "2": "Running"
  }
}
```


<div class="st-callout info">


More usage examples can be found in the [Example usage](/docs/iot-gateway/config/modbus/#usage-examples) section.


</div>


##### Modifier

**modifier** for attribute/time series value can be applied using the following settings:

| **Parameter** | **Description**                                                                                                                                                                  |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type          | **multiplier** - the result of reading will be multiplied by the value of this parameter. <br>**divider** - the result of reading will be divided by the value of this parameter |
| Value         | The value that will be used to modify the read value                                                                                                                             | 
| ---           |                                                                                                                                                                                  |


<div class="st-callout info">


More usage examples can be found in the [Example usage](/docs/iot-gateway/config/modbus/#usage-examples) section.


</div>


![image](/images/gateway/modbus-connector/modifier.webp)

##### Batch reading


<div class="st-callout info">


Feature available since SENTIENT IoT Gateway v.3.7.9 and only in advanced configuration mode.


</div>


To optimize the reading process, you can group multiple registers into a single batch read request. This approach 
reduces the number of requests sent to the Modbus server, which can enhance performance and decrease network traffic.
Take attention that the registers in a batch read request must be of the same type and function code.

Two parameters are important for group reading configuration: `address` and `tag`. Let's look at them in more detail:

- **address** - is the address of the starting register and the address of the ending register, separated by a `-`
  character. For example, `0-10` means that the group read starts with the register at address `0` and ends at the
  register at address `10`, inclusive.
- **tag** - is a unique identifier for each register within a group read. It is used to identify a specific register within
  a given address range. The tag name can be formed using an expression using the following variables:
    - `${address}` - register address within group read.
    - `${unitId}` - slave ID.
    - `${functionCode}` - function code.
    - `${type}` - data type of register.
    - `${objectsCount}` - number of objects.

Also, `divider` and `multiplier` parameters work as expected.

Example of group reading configuration:

```json
{
  "tag": "${unitId} - ${type} - ${address}",
  "type": "16int",
  "functionCode": 3,
  "objectsCount": 1,
  "address": "0-10"
}
```


<div class="st-callout info">


More usage examples can be found in the [Example usage](/docs/iot-gateway/config/modbus/#usage-examples) section.


</div>


#### Usage examples


<div class="st-tabs">

<div class="st-tab" data-label="Reading attributes/time series">

As an example, we will use SENTIENT Modbus Demo Server, which can be run using Docker and the following command:

```bash
docker run -it -p 5021:5021 sentient/tb-gw-modbus-server:latest
```


The server available at `0.0.0.0:5021`. The server has the following structure:

| Variable Name  | Register Type   | Data Type  | Address    |
|:---------------|:----------------|------------|:-----------|
| Temperature    | Holding         | 16int      | 0          |
| Humidity       | Holding         | 16int      | 1          |
| Power          | Holding         | 16int      | 2          |
| Pressure       | Holding         | 16int      | 3          |
| Relay          | Coil            | bits       | 1          |
| -------------- | --------------- | ---------- | ---------- |

We are interested in register `1`, which contains the relay state value (off/on).
To read the value of this register, we need to add this register as attribute/telemetry in the device configuration. 
To do this, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created Modbus connector and click on the "**Master Connections**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.

1. Scroll down to the "**Attributes** or **Time series**" section and click on the "**Pencil**" icon to edit the attributes and telemetry.

1. Click on the "**Add attribute**" or "**Add telemetry**" button. In our case, we will add `relay` time series, so fill in the "**Key**" field with `relay`, select the "**Type**" as **bits**, select "**Function code**" field as "**01 - Read Coils**", select "**Bit target type**" as "**Boolean**", and in the "**Address**" field enter `1`. This is the address of the Modbus register we want to read.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/examples/select-created-gateway.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the left sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/select-connector-configuration.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/select-device-configuration.webp" alt="Select the created Modbus connector and click on the &quot;**Master Connections**&quot; tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for." loading="lazy"><figcaption>Select the created Modbus connector and click on the "**Master Connections**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/reading-attributes-and-time-series-1.webp" alt="Scroll down to the &quot;**Attributes** or **Time series**&quot; section and click on the &quot;**Pencil**&quot; icon to edit the attributes and telemetry." loading="lazy"><figcaption>Scroll down to the "**Attributes** or **Time series**" section and click on the "**Pencil**" icon to edit the attributes and telemetry.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/reading-attributes-and-time-series-2.webp" alt="Click on the &quot;**Add attribute**&quot; or &quot;**Add telemetry**&quot; button. In our case, we will add `relay` time series, so fill in the &quot;**Key**&quot; field with `relay`, select the &quot;**Type**&quot; as **bits**, select &quot;**Function code**&quot; field as &quot;**01 - Read Coils**&quot;, select &quot;**Bit target type**&quot; as &quot;**Boolean**&quot;, and in the &quot;**Address**&quot; field enter `1`. This is the address of the Modbus register we want to read." loading="lazy"><figcaption>Click on the "**Add attribute**" or "**Add telemetry**" button. In our case, we will add `relay` time series, so fill in the "**Key**" field with `relay`, select the "**Type**" as **bits**, select "**Function code**" field as "**01 - Read Coils**", select "**Bit target type**" as "**Boolean**", and in the "**Address**" field enter `1`. This is the address of the Modbus register we want to read.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/reading-attributes-and-time-series-3.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


Now we can check if the attribute/telemetry works. Go to "**Entities**" → "**Devices**" → select a created
device → "**Last telemetry**" tab and check the value of the `relay` telemetry. It should be `false` since the 
default value of the relay is off.

![image](/images/gateway/modbus-connector/examples/reading-attributes-and-time-series-4.webp)

Full configuration for Modbus connector for the example above will look like this:

```json
{
  "master": {
    "slaves": [
      {
        "host": "0.0.0.0",
        "port": 5021,
        "method": "socket",
        "unitId": 1,
        "deviceName": "Demo Device",
        "deviceType": "default",
        "timeout": 35,
        "byteOrder": "LITTLE",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "connectAttemptTimeMs": 500,
        "connectAttemptCount": 5,
        "waitAfterFailedAttemptsMs": 30000,
        "type": "tcp",
        "attributes": [],
        "timeseries": [
          {
            "tag": "relay",
            "type": "bits",
            "address": 1,
            "objectsCount": 1,
            "functionCode": 1,
            "bitTargetType": "bool"
          }
        ],
        "attributeUpdates": [],
        "rpc": []
      }
    ]
  }
}
```


</div>

<div class="st-tab" data-label="Multiplierin attributes/time series">

As an example, we will use SENTIENT Modbus Demo Server, which can be run using Docker and the following command:

```bash
docker run -it -p 5021:5021 sentient/tb-gw-modbus-server:latest
```


The server available at `0.0.0.0:5021`. The server has the following structure:

| Variable Name  | Register Type   | Data Type  | Address    |
|:---------------|:----------------|------------|:-----------|
| Temperature    | Holding         | 16int      | 0          |
| Humidity       | Holding         | 16int      | 1          |
| Power          | Holding         | 16int      | 2          |
| Pressure       | Holding         | 16int      | 3          |
| Relay          | Coil            | bits       | 1          |
| -------------- | --------------- | ---------- | ---------- |

A fairly common practice when using Modbus devices is when the values we get from registers need to be multiplied by a
certain number to get the correct value. For example, if we read the power from a register and the value in
the register is `2534`, and we need to get `253400` watts, then we need to multiply the value by 100.
To implement this in the device configuration, we can use the "**Multiplier**" field in the attributes and telemetry settings.
To read the register value with a multiplier, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created Modbus connector and click on the "**Master Connections**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.

1. Scroll down to the "**Attributes** or **Time series**" section and click on the "**Pencil**" icon to edit the attributes and telemetry.

1. Click on the "**Add attribute**" or "**Add telemetry**" button. In our case, we will add `power` time series, so fill in the "**Key**" field with `power`, select the "**Type**" as **16int**, select "**Function code**" field as "**03 - Read Holding Registers**", in the "**Address**" field enter `2`, enable "**Modifier**" toggle, select "**Multiplier**" as "**Type**" and enter `10` in "**Value**" field.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/examples/select-created-gateway.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the left sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/select-connector-configuration.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/select-device-configuration.webp" alt="Select the created Modbus connector and click on the &quot;**Master Connections**&quot; tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for." loading="lazy"><figcaption>Select the created Modbus connector and click on the "**Master Connections**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/reading-attributes-and-time-series-1.webp" alt="Scroll down to the &quot;**Attributes** or **Time series**&quot; section and click on the &quot;**Pencil**&quot; icon to edit the attributes and telemetry." loading="lazy"><figcaption>Scroll down to the "**Attributes** or **Time series**" section and click on the "**Pencil**" icon to edit the attributes and telemetry.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/multiplier-attributes-and-time-series-1.webp" alt="Click on the &quot;**Add attribute**&quot; or &quot;**Add telemetry**&quot; button. In our case, we will add `power` time series, so fill in the &quot;**Key**&quot; field with `power`, select the &quot;**Type**&quot; as **16int**, select &quot;**Function code**&quot; field as &quot;**03 - Read Holding Registers**&quot;, in the &quot;**Address**&quot; field enter `2`, enable &quot;**Modifier**&quot; toggle, select &quot;**Multiplier**&quot; as &quot;**Type**&quot; and enter `10` in &quot;**Value**&quot; field." loading="lazy"><figcaption>Click on the "**Add attribute**" or "**Add telemetry**" button. In our case, we will add `power` time series, so fill in the "**Key**" field with `power`, select the "**Type**" as **16int**, select "**Function code**" field as "**03 - Read Holding Registers**", in the "**Address**" field enter `2`, enable "**Modifier**" toggle, select "**Multiplier**" as "**Type**" and enter `10` in "**Value**" field.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/multiplier-attributes-and-time-series-2.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


Now we can check if the telemetry with the multiplier works. Go to "**Entities**" → "**Devices**" → select a created 
device → "**Last telemetry**" tab and check the value of the `power` telemetry.

![image](/images/gateway/modbus-connector/examples/multiplier-attributes-and-time-series-3.webp)

Full configuration for Modbus connector for the example above will look like this:

```json
{
  "master": {
    "slaves": [
      {
        "host": "0.0.0.0",
        "port": 5021,
        "method": "socket",
        "unitId": 1,
        "deviceName": "Demo Device",
        "deviceType": "default",
        "timeout": 35,
        "byteOrder": "LITTLE",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "connectAttemptTimeMs": 500,
        "connectAttemptCount": 5,
        "waitAfterFailedAttemptsMs": 30000,
        "type": "tcp",
        "attributes": [],
        "timeseries": [
          {
            "tag": "power",
            "type": "16int",
            "address": 2,
            "objectsCount": 1,
            "functionCode": 3,
            "multiplier": 10
          }
        ],
        "attributeUpdates": [],
        "rpc": []
      }
    ]
  }
}
```


</div>

<div class="st-tab" data-label="Dividerin attributes/time series">

As an example, we will use SENTIENT Modbus Demo Server, which can be run using Docker and the following command:

```bash
docker run -it -p 5021:5021 sentient/tb-gw-modbus-server:latest
```


The server available at `0.0.0.0:5021`. The server has the following structure:

| Variable Name  | Register Type   | Data Type  | Address    |
|:---------------|:----------------|------------|:-----------|
| Temperature    | Holding         | 16int      | 0          |
| Humidity       | Holding         | 16int      | 1          |
| Power          | Holding         | 16int      | 2          |
| Pressure       | Holding         | 16int      | 3          |
| Relay          | Coil            | bits       | 1          |
| -------------- | --------------- | ---------- | ---------- |

A fairly common practice when using Modbus devices is when the values we get from registers need to be divided by a 
certain number to get the correct value. For example, if we read the temperature from a register and the value in 
the register is `2534`, and we need to get `25.34` degrees, then we need to divide the value by 100.
To implement this in the device configuration, we can use the "Divider" field in the attributes and telemetry settings.
To read the register value with a divider, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created Modbus connector and click on the "**Master Connections**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.

1. Scroll down to the "**Attributes** or **Time series**" section and click on the "**Pencil**" icon to edit the attributes and telemetry.

1. Click on the "**Add attribute**" or "**Add telemetry**" button. In our case, we will add `temperature` time series, so fill in the "**Key**" field with `temperature`, select the "**Type**" as **16int**, select "**Function code**" field as "**03 - Read Holding Registers**", in the "**Address**" field enter `0`, enable "**Modifier**" toggle, select "**Divider**" as "**Type**" and enter `10` in "**Value**" field.

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/examples/select-created-gateway.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the left sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/select-connector-configuration.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/select-device-configuration.webp" alt="Select the created Modbus connector and click on the &quot;**Master Connections**&quot; tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for." loading="lazy"><figcaption>Select the created Modbus connector and click on the "**Master Connections**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/reading-attributes-and-time-series-1.webp" alt="Scroll down to the &quot;**Attributes** or **Time series**&quot; section and click on the &quot;**Pencil**&quot; icon to edit the attributes and telemetry." loading="lazy"><figcaption>Scroll down to the "**Attributes** or **Time series**" section and click on the "**Pencil**" icon to edit the attributes and telemetry.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/divider-attributes-and-time-series-1.webp" alt="Click on the &quot;**Add attribute**&quot; or &quot;**Add telemetry**&quot; button. In our case, we will add `temperature` time series, so fill in the &quot;**Key**&quot; field with `temperature`, select the &quot;**Type**&quot; as **16int**, select &quot;**Function code**&quot; field as &quot;**03 - Read Holding Registers**&quot;, in the &quot;**Address**&quot; field enter `0`, enable &quot;**Modifier**&quot; toggle, select &quot;**Divider**&quot; as &quot;**Type**&quot; and enter `10` in &quot;**Value**&quot; field." loading="lazy"><figcaption>Click on the "**Add attribute**" or "**Add telemetry**" button. In our case, we will add `temperature` time series, so fill in the "**Key**" field with `temperature`, select the "**Type**" as **16int**, select "**Function code**" field as "**03 - Read Holding Registers**", in the "**Address**" field enter `0`, enable "**Modifier**" toggle, select "**Divider**" as "**Type**" and enter `10` in "**Value**" field.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/divider-attributes-and-time-series-2.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


Now we can check if the telemetry with the divider works. Go to "**Entities**" → "**Devices**" → select a created 
device → "**Last telemetry**" tab and check the value of the `temperature` telemetry.

![image](/images/gateway/modbus-connector/examples/divider-attributes-and-time-series-3.webp)

Full configuration for Modbus connector for the example above will look like this:

```json
{
  "master": {
    "slaves": [
      {
        "host": "0.0.0.0",
        "port": 5021,
        "method": "socket",
        "unitId": 1,
        "deviceName": "Demo Device",
        "deviceType": "default",
        "timeout": 35,
        "byteOrder": "BIG",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "connectAttemptTimeMs": 500,
        "connectAttemptCount": 5,
        "waitAfterFailedAttemptsMs": 30000,
        "type": "tcp",
        "attributes": [],
        "timeseries": [
          {
            "tag": "temperature",
            "type": "16int",
            "address": 0,
            "objectsCount": 1,
            "functionCode": 3,
            "divider": 10
          }
        ],
        "attributeUpdates": [],
        "rpc": []
      }
    ]
  }
}
```


</div>

<div class="st-tab" data-label="Batch reading(advanced configuration mode only)">

As an example, we will use SENTIENT Modbus Demo Server, which can be run using Docker and the following command:

```bash
docker run -it -p 5021:5021 sentient/tb-gw-modbus-server:latest
```


The server available at `0.0.0.0:5021`. The server has the following structure:

| Variable Name  | Register Type   | Data Type  | Address    |
|:---------------|:----------------|------------|:-----------|
| Temperature    | Holding         | 16int      | 0          |
| Humidity       | Holding         | 16int      | 1          |
| Power          | Holding         | 16int      | 2          |
| Pressure       | Holding         | 16int      | 3          |
| Relay          | Coil            | bits       | 1          |
| -------------- | --------------- | ---------- | ---------- |

For optimizing the number of requests sent to the Modbus server, you can use the **Batch reading** feature available 
in the advanced configuration mode. This feature allows reading multiple registers in a single request, which can 
significantly reduce the load on the Modbus server and improve performance.

Let’s look at an example of how to properly configure batch reading to read the `temperature`, `humidity`, `power`, 
and `pressure` registers from the Modbus server.

From the table above, we can see that all the required registers are of the same type (`16int`) and have the same
function code (`03 - Read Holding Registers`). This means that we can group them into a single batch read request.
We need to read registers from address `0` to address `3`, so our address range will be `0-3`. 
Also, you need to use, for examples `${address}` variable in the `tag` field to uniquely identify each register within 
the batch read. In our case, we will use the following expression for the `tag` field: 
`${unitId}.${type}.${address}` (you can find more information about variables in the corresponding [section of 
the documentation](/docs/iot-gateway/config/modbus/#batch-reading-advanced-configuration-mode-only)).

Copy and paste the following configuration into the Modbus connector advanced configuration mode:

```json
{
  "master": {
    "slaves": [
      {
        "host": "0.0.0.0",
        "port": 5021,
        "type": "tcp",
        "method": "socket",
        "timeout": 35,
        "byteOrder": "BIG",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "unitId": 1,
        "deviceName": "Demo Device",
        "deviceType": "default",
        "sendDataOnlyOnChange": true,
        "connectAttemptTimeMs": 5000,
        "connectAttemptCount": 5,
        "waitAfterFailedAttemptsMs": 300000,
        "attributes": [],
        "timeseries": [
          {
            "tag": "${unitId}.${type}.${address}",
            "type": "16int",
            "functionCode": 3,
            "objectsCount": 1,
            "address": "0-3",
            "divider": 10
          }
        ],
        "attributeUpdates": [],
        "rpc": []
      }
    ]
  }
}
```


After saving the changes and starting the connector, you see that the corresponding telemetry is being updated 
correctly:

![image](/images/gateway/modbus-connector/examples/batch-reading-overview.webp)


</div>

<div class="st-tab" data-label="Enum mapping(advanced configuration mode only)">

Modbus devices can have registers that represent enumerated values, for example operational modes, status codes, or
error states. To make these values more understandable, you can map them to human-readable strings using the enum
mapping feature in SENTIENT IoT Gateway Modbus connector. This feature works for all register types and can be used
in both uplink data (attributes and time series) and uplink RPC to Device calls. Let's explore how to set up enum
mapping in your Modbus connector configuration.

As an example, we will use SENTIENT Modbus Demo Server, which can be run using Docker and the following command:

```bash
docker run -it -p 5021:5021 sentient/tb-gw-modbus-server:latest
```


The server available at `0.0.0.0:5021`. The server has the following structure:

| Variable Name    | Register Type   | Data Type  | Address    |
|:-----------------|:----------------|------------|:-----------|
| Temperature      | Holding         | 16int      | 0          |
| Humidity         | Holding         | 16int      | 1          |
| Power            | Holding         | 16int      | 2          |
| Pressure         | Holding         | 16int      | 3          |
| Operational Mode | Holding         | 16int      | 4          |
| Relay            | Coil            | bits       | 1          |
| --------------   | --------------- | ---------- | ---------- |

We are interested in mapping the `Operational Mode` and `Relay` registers to human-readable strings. The `Operational Mode` register can have the following values:
- `1`: Normal Mode
- `2`: Service Mode
- `3`: Calibration Mode

And the `Relay` register can have the following values:
- `0`: OFF
- `1`: ON

To set up enum mapping for these registers, you need to define the `variants` parameter in the configuration for each 
register. This parameter is an object where each key represents a possible register value, and the corresponding value 
is the human-readable string that describes that register value.

Copy and paste the following configuration into the Modbus connector advanced configuration mode:
```json
{
  "master": {
    "slaves": [
      {
        "host": "0.0.0.0",
        "port": 5021,
        "method": "socket",
        "unitId": 1,
        "deviceName": "Demo Device",
        "deviceType": "default",
        "timeout": 35,
        "byteOrder": "BIG",
        "wordOrder": "BIG",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "connectAttemptTimeMs": 500,
        "connectAttemptCount": 5,
        "waitAfterFailedAttemptsMs": 1000,
        "type": "tcp",
        "attributes": [],
        "timeseries": [
          {
            "tag": "operational_mode",
            "type": "16int",
            "address": 4,
            "objectsCount": 1,
            "functionCode": 3,
            "variants": {
              "1": "Normal Mode",
              "2": "Service Mode",
              "3": "Calibration Mode"
            }
          },
          {
            "tag": "relay",
            "type": "bits",
            "address": 1,
            "objectsCount": 1,
            "functionCode": 1,
            "bitTargetType": "int",
            "variants": {
              "0": "OFF",
              "1": "ON"
            }
          }
        ],
        "attributeUpdates": [],
        "rpc": []
      }
    ]
  }
}
```


After applying this configuration, the `operational_mode` and `relay` registers will be mapped to their respective 
human-readable strings in uplink data. This makes it easier to interpret the data received from the Modbus device:

![image](/images/gateway/modbus-connector/examples/enum-mapping-overview.webp)


</div>

</div>


### Requests mapping

The Requests mapping section allows you to configure how the SENTIENT platform instance will interact with the
devices. That is, how the platform will request data from the devices, how it will update device attributes, and how
it will send RPC commands to the devices.

Modbus connector supports the following requests mapping:

- **Attribute updates** - allows update device nodes values from SENTIENT platform instance.
- **RPC methods** - allows sending RPC commands to devices. Using RPC methods, you can get or set values of the Modbus
  registers. Modbus connector supports different types of RPC methods, such as:
    - **Reserved GET/SET methods** - these methods are automatically created for each attribute and time series
      parameter.
      You can use them to get or set values of the Modbus registers.
    - **Configurable RPC methods to device** - these methods allow you to configure custom RPC commands in connector
      configuration that can be sent to the devices.

#### Subsection "Attribute updates"

This subsection contains configuration for attribute updates request from SENTIENT platform instance.

SENTIENT allows provisioning device attributes and fetches some of them from the device application. You can treat
this as a remote configuration for devices. Your devices are able to request shared attributes from SENTIENT.
See [user guide](https://sentient.invenia.in/docs/user-guide/attributes/) for more details.

The following parameters are used to configure attribute updates:

- **Key** - shared attribute name.
- **Type** - [type](/docs/iot-gateway/config/modbus/#data-types) of value, which is used to identify the data type of
  the value that is being received.
- **Function code** - function to use for data processing,
  specifically [Modbus functions](/docs/iot-gateway/config/modbus/#modbus-functions).
- **Objects count** - count of objects to write or read, which specifies how many registers will be processed in the
  request.
- **Address** - object address, which is used to identify the specific object in the Modbus protocol.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the
[Advanced configuration](/docs/iot-gateway/config/modbus/#device-attributes-updates) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/modbus/#usage-examples-2) section.


</div>


![image](/images/gateway/modbus-connector/attribute-updates-overview.webp)

In order to add new attribute update, follow these steps:


1. Navigate to the "**Attribute updates**" section and click the "**pencil**" icon;

1. In the opened window click "**Add attribute update**";

1. Set an attribute key name, type, function code, objects count, and address. Then, click "**Apply**".


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/attribute-updates-1-ce.webp" alt="Navigate to the &quot;**Attribute updates**&quot; section and click the &quot;**pencil**&quot; icon;" loading="lazy"><figcaption>Navigate to the "**Attribute updates**" section and click the "**pencil**" icon;</figcaption></figure><figure><img src="/images/gateway/modbus-connector/attribute-updates-2-ce.webp" alt="In the opened window click &quot;**Add attribute update**&quot;;" loading="lazy"><figcaption>In the opened window click "**Add attribute update**";</figcaption></figure><figure><img src="/images/gateway/modbus-connector/attribute-updates-3-ce.webp" alt="Set an attribute key name, type, function code, objects count, and address. Then, click &quot;**Apply**&quot;." loading="lazy"><figcaption>Set an attribute key name, type, function code, objects count, and address. Then, click "**Apply**".</figcaption></figure></div>


#### Subsection "RPC requests"

SENTIENT allows sending [RPC commands](https://sentient.invenia.in/docs/user-guide/rpc/) to the device that is connected
to SENTIENT directly or via Gateway.
Configuration, provided in this section is used for sending RPC requests from SENTIENT to device. The following
parameters are used to configure RPC methods:

- **Method name** - RPC method name, which is used to identify the request.
- **Type** - [data type](/docs/iot-gateway/config/modbus/#data-types) of value, which is used to identify the data type of
  the value that is being received.
- **Function code** - function to use for data processing,
  specifically [Modbus functions](/docs/iot-gateway/config/modbus/#modbus-functions).
- **Objects count** - count of objects to write or read, which specifies how many registers will be processed in the
  request.
- **Address** - object address, which is used to identify the specific object in the Modbus protocol.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the
[Advanced configuration](/docs/iot-gateway/config/modbus/#device-rpc-methods) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/modbus/#usage-examples-2) section.


</div>


![image](/images/gateway/modbus-connector/rpc-requests-overview.webp)

In order to add a new RPC method, follow these steps:


1. Navigate to the "**RPC requests**" section and click the "**pencil**" icon;

1. In the opened window click the "**Add request**";

1. Fill in key, type, function code, objects count and address fields. Click "**Apply**".


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/rpc-requests-1-ce.webp" alt="Navigate to the &quot;**RPC requests**&quot; section and click the &quot;**pencil**&quot; icon;" loading="lazy"><figcaption>Navigate to the "**RPC requests**" section and click the "**pencil**" icon;</figcaption></figure><figure><img src="/images/gateway/modbus-connector/rpc-requests-2-ce.webp" alt="In the opened window click the &quot;**Add request**&quot;;" loading="lazy"><figcaption>In the opened window click the "**Add request**";</figcaption></figure><figure><img src="/images/gateway/modbus-connector/rpc-requests-3-ce.webp" alt="Fill in key, type, function code, objects count and address fields. Click &quot;**Apply**&quot;." loading="lazy"><figcaption>Fill in key, type, function code, objects count and address fields. Click "**Apply**".</figcaption></figure></div>


<div class="st-callout info">


Also, every telemetry and attribute parameter has built-in GET and SET RPC methods out of the box, so you don’t need to
configure
it manually. See [the guide](/docs/iot-gateway/guides/how-to-use-get-set-rpc-methods).


</div>


#### Usage examples


<div class="st-tabs">

<div class="st-tab" data-label="Attribute Updates">

Attribute updates allow you to update register values in the Modbus server. You can add new attribute updates in the 
“**Attribute updates**” section of the device configuration page.

As an example, we will use SENTIENT Modbus Demo Server, which can be run using Docker and the following command:

```bash
docker run -it -p 5021:5021 sentient/tb-gw-modbus-server:latest
```


The server available at `0.0.0.0:5021`. The server has the following structure:

| Variable Name  | Register Type   | Data Type  | Address    |
|:---------------|:----------------|------------|:-----------|
| Temperature    | Holding         | 16int      | 0          |
| Humidity       | Holding         | 16int      | 1          |
| Power          | Holding         | 16int      | 2          |
| Pressure       | Holding         | 16int      | 3          |
| Relay          | Coil            | bits       | 1          |
| -------------- | --------------- | ---------- | ---------- |

We are interested in register “**1**”, we added this register as a telemetry parameter with the key `relay`. We used 
telemetry so that later it would be convenient for us to see if the value we changed using the attribute update 
has changed. You, also, can add this telemetry datapoint to the device configuration or use the reserved `get` method 
to check the value of the node.

Let’s add an attribute update to our configuration. For this purpose, follow these steps:


1. Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created Modbus connector and click on the "**Master Connections**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.

1. Scroll down to the “**Attribute updates**” section and click on the “**Pencil**” icon to edit the attribute updates.

1. Click on the “**Add attribute update**” button. In our case, we will add `relay` attribute update, so the “**Key**” field, enter `relay`, select the “**Type**” as **bits**, "**Function code**" as "**05 - Write Single Coil**", fill in the "**Objects count**" field with `1`, select "**Bit target type**" as "**Boolean**" and in the "**Address**" field enter "**1**".

1. Remember to save your changes by clicking the “**Apply**” button.


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/examples/select-created-gateway.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the left sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/select-connector-configuration.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/select-device-configuration.webp" alt="Select the created Modbus connector and click on the &quot;**Master Connections**&quot; tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for." loading="lazy"><figcaption>Select the created Modbus connector and click on the "**Master Connections**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/connector-configuration-attribute-updates-1.webp" alt="Scroll down to the “**Attribute updates**” section and click on the “**Pencil**” icon to edit the attribute updates." loading="lazy"><figcaption>Scroll down to the “**Attribute updates**” section and click on the “**Pencil**” icon to edit the attribute updates.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/connector-configuration-attribute-updates-2.webp" alt="Click on the “**Add attribute update**” button. In our case, we will add `relay` attribute update, so the “**Key**” field, enter `relay`, select the “**Type**” as **bits**, &quot;**Function code**&quot; as &quot;**05 - Write Single Coil**&quot;, fill in the &quot;**Objects count**&quot; field with `1`, select &quot;**Bit target type**&quot; as &quot;**Boolean**&quot; and in the &quot;**Address**&quot; field enter &quot;**1**&quot;." loading="lazy"><figcaption>Click on the “**Add attribute update**” button. In our case, we will add `relay` attribute update, so the “**Key**” field, enter `relay`, select the “**Type**” as **bits**, "**Function code**" as "**05 - Write Single Coil**", fill in the "**Objects count**" field with `1`, select "**Bit target type**" as "**Boolean**" and in the "**Address**" field enter "**1**".</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/connector-configuration-3.webp" alt="Remember to save your changes by clicking the “**Apply**” button." loading="lazy"><figcaption>Remember to save your changes by clicking the “**Apply**” button.</figcaption></figure></div>


Now we can check if the attribute update works. Go to "**Entities**" → "**Devices**" → select a created 
device → "**Attributes**" tab → select "**Shared attributes**" → click on the "**+**" icon and add `relay` attribute 
with type "**Boolean**" set it to "**True**".


<div class="st-gallery"><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-4.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/gateway/opc-ua-connector/examples/attribute-updates-relative-path-5.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Now, let’s check the value of the relay register. In the selected device, go to the "**Last telemetry**" tab and 
check the value of the `relay` telemetry. It should be `true` since we set the shared attribute to `true`.

![image](/images/gateway/modbus-connector/examples/result-device-overview-1.webp)

Try to change the value of the `relay` shared attribute to `false`. After a few seconds, you should see that the
`relay` telemetry value has changed to `false`, which means that the attribute update worked correctly.

Full configuration for Modbus connector for the examples above will look like this:

```json
{
  "master": {
    "slaves": [
      {
        "host": "0.0.0.0",
        "port": 5021,
        "method": "socket",
        "unitId": 1,
        "deviceName": "Demo Device",
        "deviceType": "default",
        "timeout": 35,
        "byteOrder": "LITTLE",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "connectAttemptTimeMs": 500,
        "connectAttemptCount": 5,
        "waitAfterFailedAttemptsMs": 30000,
        "type": "tcp",
        "attributes": [],
        "timeseries": [
          {
            "tag": "relay",
            "type": "bits",
            "address": 1,
            "objectsCount": 1,
            "functionCode": 1,
            "bitTargetType": "bool"
          }
        ],
        "attributeUpdates": [
          {
            "tag": "relay",
            "type": "bits",
            "address": 1,
            "objectsCount": 1,
            "functionCode": 5,
            "bitTargetType": "bool"
          }
        ],
        "rpc": []
      }
    ]
  }
}
```


</div>

<div class="st-tab" data-label="RPC to Device">

RPC to Device allows sending RPC commands to the device that is connected to SENTIENT directly 
or via Gateway.

As an example, we will use SENTIENT Modbus Demo Server, which can be run using Docker and the following command:

```bash
docker run -it -p 5021:5021 sentient/tb-gw-modbus-server:latest
```


The server available at `0.0.0.0:5021`. The server has the following structure:

| Variable Name  | Register Type   | Data Type  | Address    |
|:---------------|:----------------|------------|:-----------|
| Temperature    | Holding         | 16int      | 0          |
| Humidity       | Holding         | 16int      | 1          |
| Power          | Holding         | 16int      | 2          |
| Pressure       | Holding         | 16int      | 3          |
| Relay          | Coil            | bits       | 1          |
| -------------- | --------------- | ---------- | ---------- |

We are interested to get temperature value from our demo device using RPC to Device.
To call this method, first, we need to configure the Modbus connector to support RPC calls. For this purpose, follow
these steps:


1. Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.

1. Click on the "**Connectors configuration**" button on the right side menu.

1. Select the created Modbus connector and click on the "**Master Connections**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.

1. Scroll down to the "**RPC requests**" section and click on the "**Pencil**" icon to edit the RPC methods.

1. Click on the "**Add request**" button. Fill in the "**Method**" field with `getTemperature`, select the "Type" as "16int", "**Function code**" as "**03 - Read Multiple Holding Registers**", fill in the "Objects count" field with `1`, and in the "**Address**" field enter "**0**".

1. Remember to save your changes by clicking the "**Apply**" button.


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/examples/select-created-gateway.webp" alt="Go to &quot;**Entities**&quot; → &quot;**Gateways**&quot; in the left sidebar and select your gateway." loading="lazy"><figcaption>Go to "**Entities**" → "**Gateways**" in the left sidebar and select your gateway.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/select-connector-configuration.webp" alt="Click on the &quot;**Connectors configuration**&quot; button on the right side menu." loading="lazy"><figcaption>Click on the "**Connectors configuration**" button on the right side menu.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/select-device-configuration.webp" alt="Select the created Modbus connector and click on the &quot;**Master Connections**&quot; tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for." loading="lazy"><figcaption>Select the created Modbus connector and click on the "**Master Connections**" tab. Make sure you have configured and connected device (if you don’t know how to do it, see [Getting Started](/docs/iot-gateway/getting-started/?connectorsCreation=modbus) guide or [Connection settings](/docs/iot-gateway/config/modbus/#connection-settings) and [Data mapping](/docs/iot-gateway/config/modbus/#data-mapping) sections of this guide). Click on the “**Pencil**” icon on a device you want to configure attribute updates for.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/rpc-to-device-1.webp" alt="Scroll down to the &quot;**RPC requests**&quot; section and click on the &quot;**Pencil**&quot; icon to edit the RPC methods." loading="lazy"><figcaption>Scroll down to the "**RPC requests**" section and click on the "**Pencil**" icon to edit the RPC methods.</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/rpc-to-device-2.webp" alt="Click on the &quot;**Add request**&quot; button. Fill in the &quot;**Method**&quot; field with `getTemperature`, select the &quot;Type&quot; as &quot;16int&quot;, &quot;**Function code**&quot; as &quot;**03 - Read Multiple Holding Registers**&quot;, fill in the &quot;Objects count&quot; field with `1`, and in the &quot;**Address**&quot; field enter &quot;**0**&quot;." loading="lazy"><figcaption>Click on the "**Add request**" button. Fill in the "**Method**" field with `getTemperature`, select the "Type" as "16int", "**Function code**" as "**03 - Read Multiple Holding Registers**", fill in the "Objects count" field with `1`, and in the "**Address**" field enter "**0**".</figcaption></figure><figure><img src="/images/gateway/modbus-connector/examples/rpc-to-device-3.webp" alt="Remember to save your changes by clicking the &quot;**Apply**&quot; button." loading="lazy"><figcaption>Remember to save your changes by clicking the "**Apply**" button.</figcaption></figure></div>


We are done with configuration, so let's check how to call the method. In the RPC Debug Terminal widget, run the 
following command:

```bash
getTemperature
```

Response:

![image](/images/gateway/modbus-connector/examples/rpc-to-device-4.webp)

Full configuration for Modbus connector for the example above will look like this:

```json
{
  "master": {
    "slaves": [
      {
        "host": "0.0.0.0",
        "port": 5021,
        "method": "socket",
        "unitId": 1,
        "deviceName": "Demo Device",
        "deviceType": "default",
        "timeout": 35,
        "byteOrder": "LITTLE",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "connectAttemptTimeMs": 500,
        "connectAttemptCount": 5,
        "waitAfterFailedAttemptsMs": 30000,
        "type": "tcp",
        "attributes": [],
        "timeseries": [
          {
            "tag": "some_key",
            "type": "16int",
            "address": 0,
            "objectsCount": 1,
            "functionCode": 3
          }
        ],
        "attributeUpdates": [],
        "rpc": [
          {
            "tag": "getTemperature",
            "type": "16int",
            "address": 0,
            "objectsCount": 1,
            "functionCode": 3
          }
        ]
      }
    ]
  }
}
```


</div>

<div class="st-tab" data-label="Reserved RPCs">

Every telemetry and attribute parameter has `GET` and `SET` RPC methods out of the box, so you don’t need to configure 
them manually.

As an example, we will use SENTIENT Modbus Demo Server, which can be run using Docker and the following command:

```bash
docker run -it -p 5021:5021 sentient/tb-gw-modbus-server:latest
```


The server available at `0.0.0.0:5021`. The server has the following structure:

| Variable Name  | Register Type   | Data Type  | Address    |
|:---------------|:----------------|------------|:-----------|
| Temperature    | Holding         | 16int      | 0          |
| Humidity       | Holding         | 16int      | 1          |
| Power          | Holding         | 16int      | 2          |
| Pressure       | Holding         | 16int      | 3          |
| Relay          | Coil            | bits       | 1          |
| -------------- | --------------- | ---------- | ---------- |

We are interested in register `1`, which is a coil register. We will use this register to set the value of the
telemetry parameter. The register is of type `bits`, so we will use `bits` type for the telemetry parameter. The 
configuration for this telemetry will look like this:

```json
{
    "tag": "relay",
    "type": "bits",
    "address": 1,
    "objectsCount": 1,
    "functionCode": 1,
    "bitTargetType": "bool"
}
```

Let’s check the value of the relay register using the reserved `get` method. To get the current value of relay 
register, run the query in RPC debug terminal:

```bash
get type=bits;functionCode=1;objectsCount=1;address=1;
```

Response:

```json
{"result":{"value":false}}
```

![image](/images/gateway/modbus-connector/examples/reserved-rpc-result-1.webp)

So, the `get` method returns the current value of the relay register, and we can see that the relay is off.


<div class="st-callout info">


The RPC Debug Terminal is used only for example purpose, so you can use any other widget that supports RPC calls.


</div>


To set the value of the relay register and turn it on, run the query:

```bash
set type=bits;functionCode=5;objectsCount=1;address=1;value=1;
```

Response:

```json
{"result":{"value":"1"}}
```

And as you can see, from the screenshot below, the relay telemetry value has changed to `1`:

![image](/images/gateway/modbus-connector/examples/reserved-rpc-result-2.webp)

Also, let’s check the value of the relay telemetry again: it is `true` 
now because, in the Modbus connector, booleans come from integers — `0` = `false`, `1` = `true` 
(any non-zero is `true`) — so a register value of `1` is reported as `true`.

```bash
get type=bits;functionCode=3;objectsCount=1;address=1;
```

Response:

```json
{"result":{"value":true}}
```

![image](/images/gateway/modbus-connector/examples/reserved-rpc-result-3.webp)

Full configuration for Modbus connector for the examples above will look like this:

```json
{
  "master": {
    "slaves": [
      {
        "host": "0.0.0.0",
        "port": 5021,
        "method": "socket",
        "unitId": 1,
        "deviceName": "Demo Device",
        "deviceType": "default",
        "timeout": 35,
        "byteOrder": "LITTLE",
        "wordOrder": "LITTLE",
        "retries": true,
        "retryOnEmpty": true,
        "retryOnInvalid": true,
        "pollPeriod": 1000,
        "connectAttemptTimeMs": 500,
        "connectAttemptCount": 5,
        "waitAfterFailedAttemptsMs": 30000,
        "type": "tcp",
        "attributes": [],
        "timeseries": [
          {
            "tag": "relay",
            "type": "bits",
            "address": 1,
            "objectsCount": 1,
            "functionCode": 1,
            "bitTargetType": "bool"
          }
        ],
        "attributeUpdates": [],
        "rpc": []
      }
    ]
  }
}
```


</div>

</div>


### Advanced configuration

The advanced configuration section provides a detailed overview of all available parameters for the Master section 
configuration.

#### Master

Gateway can run as a Modbus master. This configuration section for the Modbus master, which is used to query data from
Modbus servers (slaves).

##### Slaves

The Slaves list is used to specify the list of Modbus slaves that the master will query data from.

| **Parameter**                                     | **Default value** | **Description**                                                                                                                                               |
|:--------------------------------------------------|:------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server.slaves[].unitId                            |                   | Unit ID of Modbus slave.                                                                                                                                      |
| server.slaves[].deviceName                        |                   | Device name on the platform.                                                                                                                                  |
| server.slaves[].deviceType                        | **default**       | (Optional) Device profile name on the platform.                                                                                                               |
| server.slaves[].pollPeriod (in ms)                |                   | Period in milliseconds to check the attributes and the telemetry on the slave.                                                                                |
| server.slaves[].delayBetweenRequestsMs            | **0**             | (Optional) Delay between reading and writing requests. Useful for devices that implement Modbus RTU over TCP internally consist of a TCP-to-Serial converter. |
| server.slaves[].timeout (in sec)                  | **35**            | (Optional) Timeout in seconds for connecting to Modbus server.                                                                                                |
| server.slaves[].retries                           | **true**          | (Optional) Retrying sending data to the master. The values can be either: true or false.                                                                      |
| server.slaves[].retryOnEmpty                      | **true**          | (Optional) Retrying sending data to the master if it is empty.                                                                                                |
| server.slaves[].retryOnInvalid                    | **true**          | (Optional) Retrying sending data to the master if it is failed.                                                                                               |
| server.slaves[].connectAttemptTimeMs (in ms)      | **5000**          | (Optional) A waiting period in milliseconds before connecting to the master.                                                                                  |
| server.slaves[].connectAttemptCount               | **5**             | (Optional) The number of connection attempts made through the SENTIENT gateway.                                                                            |
| server.slaves[].waitAfterFailedAttemptsMs (in ms) | **300000**        | (Optional) A waiting period in milliseconds before trying to send data to the master.                                                                         |
| server.slaves[].byteOrder                         | **LITTLE**        | Order of bytes to read.                                                                                                                                       |
| server.slaves[].wordOrder                         | **LITTLE**        | The order of words when reading several registers.                                                                                                            |
| server.slaves[].reportStrategy                    |                   | (Optional) Report strategy object using for configuring report strategy for device.                                                                           |
| ---                                               |                   |                                                                                                                                                               |

Example of the slave configuration:

```json
"master": {
  "slaves": [
    {
      "timeout": 35,
      "byteOrder": "LITTLE",
      "wordOrder": "LITTLE",
      "retries": true,
      "retryOnEmpty": true,
      "retryOnInvalid": true,
      "pollPeriod": 5000,
      "sendDataOnlyOnChange": true,
      "connectAttemptTimeMs": 5000,
      "connectAttemptCount": 5,
      "waitAfterFailedAttemptsMs": 300000,
      "deviceName": "Demo Device",
      "deviceType": "default",
      "unitId": 1, 
      ...
    }
  ]
}
```

##### Slave connection types

The Modbus connector supports three types of connections to the Modbus slave:
- **TCP** - connection to the Modbus slave over TCP/IP protocol.
- **UDP** - connection to the Modbus slave over UDP protocol.
- **Serial** - connection to the Modbus slave over serial port (RS-232, RS-485, etc.).

###### TCP/UDP

| **Parameter**          | **Default value** | **Description**                                    |
|:-----------------------|:------------------|----------------------------------------------------|
| master.slaves[].type   |                   | Type of connection to Modbus device.               |
| master.slaves[].host   | **localhost**     | Hostname or ip address of Modbus server.           |
| master.slaves[].port   | **5021**          | Port of Modbus server for connection.              |
| master.slaves[].method | **socket**        | Type of a framer **Socket** or **RTU**, if needed. |
| ---                    |                   |                                                    |

Example of the TCP/UDP slave configuration:

```json
"master": {
    "slaves": [
        {
            "host": "127.0.0.1",
            "port": 5021,
            "method": "socket",
            ...
        }
    ]
}
```

###### Serial

| **Parameter**                   | **Default value** | **Description**                                                                                                                      |
|:--------------------------------|:------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| master.slaves[].type            | **serial**        | Type of connection to Modbus device.                                                                                                 |
| master.slaves[].port            |                   | Port of Modbus slave for connection.                                                                                                 |
| master.slaves[].method          | **socket**        | Type of a framer Socket or RTU, if needed.                                                                                           |
| master.slaves[].baudrate        | **19200**         | Baud rate for serial connection.                                                                                                     |
| master.slaves[].stopbits        | **1**             | (Optional) The number of bits sent after each character in a message to indicate the end of the byte.                                |
| master.slaves[].parity          | **None**          | (Optional) The type of checksum to use to verify data integrity. This can be on of the following: (**E**)ven, (**O**)dd, (**N**)one. |
| master.slaves[].bytesize        | **8**             | (Optional) The number of bits in a byte of serial data. This can be one of **5**, **6**, **7**, or **8**.                            |
| master.slaves[].strict          | **true**          | (Optional) Use Inter char timeout for baud rates <= 19200                                                                            |
| master.slaves[].repack          | **false**         | (Optional) Repack data to remove padding bytes.                                                                                      |
| master.slaves[].handleLocalEcho | **false**         | (Optional) Handle local echo for serial connections. This is useful for devices that echo back the data sent to them.                |
| ---                             |                   |                                                                                                                                      |

Example of the serial slave configuration:

```json
"master": {
    "slaves": [
        {
            "method": "ascii",
            "baudrate": 4800,
            "stopbits": 1,
            "bytesize": 5,
            "parity": "N",
            "strict": true,
            ...
        }
    ]
}
```

##### Device attributes and time series

| **Parameter**                              | **Description**                                                                                                                                                    |
|:-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| server.slaves[].attributes[]               | List of attributes that will be sent to the SENTIENT platform instance.                                                                                         |
| server.slaves[].attributes[].tag           | Key name of the attribute in SENTIENT. It can be specified as a static value.                                                                                   |
| server.slaves[].attributes[].type          | [Data type](/docs/iot-gateway/config/modbus/#data-types) of value.                                                                                                 |
| server.slaves[].attributes[].functionCode  | [Function code](/docs/iot-gateway/config/modbus/#modbus-functions) to use for reading the attribute value from the Modbus slave.                                   |
| server.slaves[].attributes[].objectsCount  | Number of objects to read from the Modbus slave.                                                                                                                   |
| server.slaves[].attributes[].address       | Address of the object in the Modbus slave. Can be configured for [batch reading](/docs/iot-gateway/config/modbus/#batch-reading-advanced-configuration-mode-only). |
| server.slaves[].attributes[].divider       | (Optional) Divider for the value. If not specified, the value will be sent as is.                                                                                  |
| server.slaves[].attributes[].multiplier    | (Optional) Multiplier for the value. If not specified, the value will be sent as is.                                                                               |
| server.slaves[].attributes[].bitTargetType | The response type can be either an integer (0/1) or a boolean (True/False). **Used only with type `bits`**.                                                        |
| mapping[].attributes[].reportStrategy      | (Optional) Report strategy for the attributes data. If not specified, the device report strategy will be used.                                                     |
| server.slaves[].timeseries[]               | List of time series that will be sent to the SENTIENT platform instance.                                                                                        |
| server.slaves[].timeseries[].tag           | Key name of the time series in SENTIENT. It can be specified as a static value.                                                                                 |
| server.slaves[].timeseries[].type          | [Data type](/docs/iot-gateway/config/modbus/#data-types) of value.                                                                                                 |
| server.slaves[].timeseries[].functionCode  | [Function code](/docs/iot-gateway/config/modbus/#modbus-functions) to use for reading the time series value from the Modbus slave.                                 |
| server.slaves[].timeseries[].objectsCount  | Number of objects to read from the Modbus slave.                                                                                                                   |
| server.slaves[].timeseries[].address       | Address of the object in the Modbus slave. Can be configured for [batch reading](/docs/iot-gateway/config/modbus/#batch-reading-advanced-configuration-mode-only). |
| server.slaves[].timeseries[].divider       | (Optional) Divider for the value. If not specified, the value will be sent as is.                                                                                  |
| server.slaves[].timeseries[].multiplier    | (Optional) Multiplier for the value. If not specified, the value will be sent as is.                                                                               |
| server.slaves[].timeseries[].bitTargetType | The response type can be either an integer (0/1) or a boolean (True/False). **Used only with type `bits`**.                                                        |
| mapping[].attributes[].reportStrategy      | (Optional) Report strategy for the time series data. If not specified, the device report strategy will be used.                                                    |
| ---                                        |                                                                                                                                                                    |

Example of the attributes and telemetry configuration:

```json
"attributes": [
  {
    "tag": "string_read",
    "type": "string",
    "functionCode": 4,
    "objectsCount": 4,
    "address": 1
  }
],
"timeseries": [
  {
    "tag": "16uint_read",
    "type": "16uint",
    "functionCode": 4,
    "objectsCount": 2,
    "address": 18
  },
]
```

##### Device attributes updates

| **Parameter**                                      | **Description**                                                                                                                  |
|:---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| server.slaves[].attributeUpdates[]                 | List of attributes that will be updated on the device.                                                                           |
| server.slaves[].attributeUpdates[].tag             | Key name of the shared attribute in SENTIENT. It can be specified as a static value.                                          |
| server.slaves[].attributeUpdates[].type            | [Data type](/docs/iot-gateway/config/modbus/#data-types) of value.                                                               |
| server.slaves[].attributeUpdates[].functionCode    | [Function code](/docs/iot-gateway/config/modbus/#modbus-functions) to use for reading the attribute value from the Modbus slave. |
| server.slaves[].attributeUpdates[].objectsCount    | Number of objects to read from the Modbus slave.                                                                                 |
| server.slaves[].attributeUpdates[].address         | Address of the object in the Modbus slave.                                                                                       |
| server.slaves[].attributeUpdates[].timeout (in ms) | (Optional) Timeout for the request in milliseconds. If not specified, the default timeout is used (5 sec).                       |
| server.slaves[].attributeUpdates[].bitTargetType   | The response type can be either an integer (0/1) or a boolean (True/False). **Used only with type `bits`**.                      |
| ---                                                |                                                                                                                                  |

Example of the attributes updates configuration:

```json
{
    "tag": "relay",
    "type": "bits",
    "functionCode": 5,
    "objectsCount": 1,
    "bitTargetType": "int",
    "address": 29
}
```

##### Device RPC methods

| **Parameter**                         | **Description**                                                                                                                   |
|:--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| server.slaves[].rpc[]                 | List of RPC methods that will be available on the device.                                                                         |
| server.slaves[].rpc[].tag             | Name of the RPC method. It can be specified as a static value.                                                                    |
| server.slaves[].rpc[].type            | [Data type](/docs/iot-gateway/config/modbus/#data-types) of value.                                                                |
| server.slaves[].rpc[].functionCode    | [Function code](/docs/iot-gateway/config/modbus/#modbus-functions) to use for reading the RPC method value from the Modbus slave. |
| server.slaves[].rpc[].objectsCount    | Number of objects to read from the Modbus slave.                                                                                  |
| server.slaves[].rpc[].address         | Address of the object in the Modbus slave.                                                                                        |
| server.slaves[].rpc[].timeout (in ms) | (Optional) Timeout for the request in milliseconds. If not specified, the default timeout is used (5 sec).                        |
| server.slaves[].rpc[].bitTargetType   | The response type can be either an integer (0/1) or a boolean (True/False). **Used only with type `bits`**.                       |
| ---                                   |                                                                                                                                   |

Example of the RPC methods configuration:

```json
"rpc": [
  {
    "tag": "setValue",
    "type": "16int",
    "functionCode": 6,
    "objectsCount": 1,
    "address": 31
  }
]
```

## Server (Gateway as a Slave) settings

Gateway can run as a Modbus slave. Gateway as a slave can store data, send updates to the platform when changes occur 
or at fixed intervals, also, user can change storing data via RPCs or shared attribute updates.

### Enabling Gateway as a Slave and sending data to the platform

To enable the Gateway as a Modbus slave, you need to toggle "**Enable**" button in the "**Server configuration**" 
section. Please note that this option will only create a modbus slave, but it will not send any data to the platform 
automatically:

![image](/images/gateway/modbus-connector/enable-gateway-as-a-slave.webp)

To send data to the platform, you need to enable "**Send data to the platform**" toggle in the 
"**Server configuration**", which will enable sending data to the platform when changes occur or at fixed intervals:

![image](/images/gateway/modbus-connector/send-data-gateway-as-a-slave.webp)

### Connection settings

Due to the nature of preferred way of communication between Modbus master there are 3 options how to configure this 
part: TCP, UDP or via Serial port.

![image](/images/gateway/modbus-connector/server-slave-configuration-basic.webp)


<div class="st-tabs">

<div class="st-tab" data-label="TCP">

The following parameters are used to configure TCP connection for Gateway as a Slave:

- **Host** - hostname or IP address of the Modbus server.
- **Port** - port of the Modbus server for connection.
- **Method** - type of a framer, either **Socket** or **RTU**.
- **Unit ID** - ID of the current slave on Modbus.
- **Device name** - name of the current slave. **Don't use "Gateway" as the value of "Device name" parameter!**
- **Device profile** - device profile of the current slave.
- **Poll period (ms)** - period in milliseconds for checking the attributes and telemetry.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/modbus/#device-rpc-methods) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/modbus/#usage-examples-2) section.


</div>


![image](/images/gateway/modbus-connector/tcp-server-configuration-section-1-ce.webp)


</div>

<div class="st-tab" data-label="UDP">

The following parameters are used to configure UDP connection for Gateway as a Slave:

- **Host** - hostname or IP address of the Modbus server.
- **Port** - port of the Modbus server for connection.
- **Method** - type of a framer, either **Socket** or **RTU**.
- **Unit ID** - ID of the current slave on Modbus.
- **Device name** - name of the current slave. **Don't use "Gateway" as the value of "Device name" parameter!**
- **Device profile** - device profile of the current slave.
- **Poll period (ms)** - period in milliseconds for checking the attributes and telemetry.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/modbus/#device-rpc-methods) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/modbus/#usage-examples-2) section.


</div>


![image](/images/gateway/modbus-connector/udp-server-configuration-section-1-ce.webp)


</div>

<div class="st-tab" data-label="Serial">

The following parameters are used to configure serial connection for Gateway as a Slave:

- **Port** - port of the Modbus server for connection.
- **Method** - type of application data unit, either **ASCII** or **RTU**.
- **Baudrate** - baud rate to use for the serial device.
- **Strict** - use inter-character timeout for baud rates <= 19200.
- **Unit ID** - ID of the current slave on Modbus.
- **Device name** - name of the current slave. **Don't use "Gateway" as the value of "Device name" parameter!**.
- **Device profile** - device profile of the current slave.
- **Poll period (ms)** - period in milliseconds for checking the attributes and telemetry.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/modbus/#device-rpc-methods) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/modbus/#usage-examples-2) section.


</div>


![image](/images/gateway/modbus-connector/serial-server-configuration-section-1-ce.webp)


</div>

</div>


### Advanced connection settings

You can configure additional settings like: TLS connection, byte order, word order, and other. The following parameters 
are used to configure advanced connection settings:

- **Byte order** - byte order for the Modbus connection, either **LITTLE** or **BIG**.
- **Word order** - word order for the Modbus connection, either **LITTLE** or **BIG**.
- **Vendor name** - name of the vendor for the Modbus connection.
- **Product code** - product code for the Modbus connection.
- **Vendor URL** - URL of the vendor for the Modbus connection.
- **Product name** - name of the product for the Modbus connection.
- **Model name** - model name for the Modbus connection.
- **TLS** - enable or disable TLS connection for the Modbus connection (**Only for TCP and UDP connections**):
  - **Path to client certificate** - path to the client certificate file.
  - **Path to client private key** - path to the client private key file.
  - **Password** - password for the client private key file.


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/modbus/#device-rpc-methods) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/modbus/#usage-examples-2) section.


</div>


To configure advanced connection settings, follow these steps:


1. Click on the "**Advanced connection settings**" subsection to open it;

1. Make the necessary settings.


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/advanced-connection-settings-basic-1-ce.webp" alt="Click on the &quot;**Advanced connection settings**&quot; subsection to open it;" loading="lazy"><figcaption>Click on the "**Advanced connection settings**" subsection to open it;</figcaption></figure><figure><img src="/images/gateway/modbus-connector/advanced-connection-settings-basic-2-ce.webp" alt="Make the necessary settings." loading="lazy"><figcaption>Make the necessary settings.</figcaption></figure></div>


### Data mapping

In this section, you can specify initial values for registers and coils. Each value refers to a specific type of
register. There are:

1. Holding registers
2. Coils initializer
3. Input registers
4. Discrete inputs

For each register type, you can configure the value types that will be used to read/write data.
According to the data type you select, the gateway will use the appropriate Modbus function code to
read or write data.

To configure the value types for reading, use the attributes and telemetry sections. To write data, use the RPC methods 
and shared attributes sections. Also note that each value type is configured similarly to the corresponding data types 
in the attributes and telemetry, RPC methods, and shared attributes sections. The only exception is that
you need to set an initial value in the "**Value**" field.

Depending on which value the register belongs to, you should add it to the appropriate array.

Select basic or advanced Modbus configuration:

![image](/images/gateway/modbus-connector/values-subsection-1-ce.webp)


<div class="st-callout info">


All configuration parameters list, and their detailed description can be found in the 
[Advanced configuration](/docs/iot-gateway/config/modbus/#device-rpc-methods) section.

More usage examples can be found in the [Example usage](/docs/iot-gateway/config/modbus/#usage-examples-2) section.


</div>


To add new value to the gateway slave, use the following steps:


1. Click on "**pencil**" icon in the row of the selected section;

1. In the opened window click "**Add attribute**" or other (depends on selected section);

1. Fill in key, type, function code, objects count, address and value fields. Click "Apply".


<div class="st-gallery"><figure><img src="/images/gateway/modbus-connector/add-new-value-to-gateway-slave-1-ce.webp" alt="Click on &quot;**pencil**&quot; icon in the row of the selected section;" loading="lazy"><figcaption>Click on "**pencil**" icon in the row of the selected section;</figcaption></figure><figure><img src="/images/gateway/modbus-connector/add-new-value-to-gateway-slave-2-ce.webp" alt="In the opened window click &quot;**Add attribute**&quot; or other (depends on selected section);" loading="lazy"><figcaption>In the opened window click "**Add attribute**" or other (depends on selected section);</figcaption></figure><figure><img src="/images/gateway/modbus-connector/add-new-value-to-gateway-slave-3-ce.webp" alt="Fill in key, type, function code, objects count, address and value fields. Click &quot;Apply&quot;." loading="lazy"><figcaption>Fill in key, type, function code, objects count, address and value fields. Click "Apply".</figcaption></figure></div>


### Advanced configuration

The advanced configuration section provides a detailed overview of all available parameters for the Gateway as a Slave 
configuration section.

#### Slave

Gateway can run as a Modbus slave. This configuration section for the Modbus slave, which is used to store data and
send updates to the platform when changes occur or at fixed intervals.

| **Parameter**               | **Default value** | **Description**                                                                                                 |
|:----------------------------|:------------------|-----------------------------------------------------------------------------------------------------------------|
| slave.byteOrder             | **LITTLE**        | The order of bytes to read.                                                                                     |
| slave.wordOrder             | **LITTLE**        | The order of words when reading several registers.                                                              |
| slave.pollPeriod (in ms)    | **5000**          | Period in milliseconds to read and send the attributes and the telemetry to the platform.                       |
| slave.sendDataToSENTIENT | **true**          | If set to **TRUE**, the Gateway will perform autoconfiguration and send values to SENTIENT every poll period |
| slave.unitId                |                   | ID of current gateway slave on Modbus.                                                                          |
| slave.deviceName            |                   | Device name on the platform.                                                                                    |
| slave.deviceType            | **default**       | (Optional) Device profile name on the platform.                                                                 |
| ---                         |                   |                                                                                                                 |

Example of the slave configuration:

```json
"slave": {
  "type": "tcp",
  "host": "127.0.0.1",
  "port": 5026,
  "method": "socket",
  "deviceName": "Modbus Slave Example",
  "deviceType": "default",
  "pollPeriod": 5000,
  "sendDataToSENTIENT": false,
  "byteOrder": "LITTLE",
  "wordOrder": "LITTLE",
  "unitId": 0,
  ...
}
```

#### Slave connection types

The Modbus connector supports three types of connections to the Modbus slave:
- **TCP** - connection to the Modbus slave over TCP/IP protocol.
- **UDP** - connection to the Modbus slave over UDP protocol.
- **Serial** - connection to the Modbus slave over serial port (RS-232, RS-485, etc.).

##### TCP/UDP

| **Parameter** | **Description**                                                  |
|:--------------|------------------------------------------------------------------|
| slave.type    | Type of connection to Modbus device, can be: **tpc** or **udp**. |
| slave.host    | Hostname or ip address of Modbus server.                         |
| slave.port    | Port of Modbus server for connection.                            |
| slave.method  | Type of a framer **Socket** or **RTU**, if needed.               |
| ---           |                                                                  |

Example of the TPC/UDP configuration:

```json
"slave": {
  "type": "tcp",
  "host": "127.0.0.1",
  "port": 5026,
  "method": "socket",
  ...
}
```

##### Serial

| **Parameter**         | **Default value** | **Description**                                                                                                                       |
|:----------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| slave.type            | **serial**        | Type of connection to Modbus device, can be: **tpc** or **udp**.                                                                      |
| slave.port            |                   | Port of Modbus slave for connection.                                                                                                  |
| slave.method          | **rtu**           | Type of a framer **Socket** or **RTU**, if needed.                                                                                    |
| slave.baudrate        | **19200**         | (Optional) Baud rate for serial connection.                                                                                           |
| slave.stopbits        | **1**             | (Optional) The number of bits sent after each character in a message to indicate the end of the byte.                                 |
| slave.parity          | **N**             | (Optional) The type of checksum to use to verify data integrity. This can be on of the following: (**E**) ven, (**O**)dd, (**N**)one. |
| slave.bytesize        | **8**             | (Optional) The number of bits in a byte of serial data. This can be one of **5**, **6**, **7**, or **8**.                             |
| slave.strict          | **true**          | (Optional) Use Inter char timeout for baud rates <= 19200.                                                                            |
| slave.handleLocalEcho | **false**         | (Optional) Handle local echo for serial connections. This is useful for devices that echo back the data sent to them.                 |
| ---                   |                   |                                                                                                                                       |

Example of the serial configuration:

```json
"slave": {
  "type": "serial",
  "port": 5026,
  "method": "rtu",
  "baudrate": 4800,
  "stopbits": 1,
  "bytesize": 5,
  "parity": "N",
  "strict": true,
  "handleLocalEcho": false,
  ...
}
```

##### Security

The Gateway as a Salve supports security configuration. This configuration is used to secure the
connection to the Modbus slave and to authenticate the connection. **Available only for the TCP and UDP connections.**

| **Parameter**           | **Description**                                    |
|:------------------------|----------------------------------------------------|
| slave.security          | Security object.                                   |
| slave.security.keyfile  | Hostname or ip address of Modbus server.           |
| slave.security.certfile | Port of Modbus server for connection.              |
| slave.security.password | Type of a framer **Socket** or **RTU**, if needed. |
| ---                     |                                                    |

Example of the security configuration:

```json
"slave": {
  "type": "tcp",
  "host": "127.0.0.1",
  "port": 5026,
  "method": "socket",
  "security": {
      "keyfile": "/path/to/keyfile.pem",
      "certfile": "/path/to/certfile.pem",
      "password": "your_password"
  }
  ...
}
```

#### Values

The Values list is used to specify the initial values for registers and coils. Each value refers to a specific type of
register. There are:

1. Holding registers
2. Coils initializer
3. Input registers
4. Discrete inputs

For each register type, you can configure the value types that will be used to read/write data.
According to the data type you select, the gateway will use the appropriate Modbus function code to
read or write data.

##### Attributes and timeseries

| **Parameter**                                               | **Description**                                                                                             |
|:------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| slave.values[].`<register_type>`.attributes[]               | The list of attributes.                                                                                     |
| slave.values[].`<register_type>`.attributes[].tag           | Key name of the attribute on the platform.                                                                  |
| slave.values[].`<register_type>`.attributes[].address       | Object address.                                                                                             |
| slave.values[].`<register_type>`.attributes[].type          | Type of value.                                                                                              |
| slave.values[].`<register_type>`.attributes[].objectsCount  | Count of objects to write.                                                                                  |
| slave.values[].`<register_type>`.attributes[].value         | Initial register value.                                                                                     |
| slave.values[].`<register_type>`.attributes[].bitTargetType | The response type can be either an integer (0/1) or a boolean (True/False). **Used only with type `bits`**. |
| slave.values[].`<register_type>`.timeseries[]               | The list of timeseries.                                                                                     |
| slave.values[].`<register_type>`.timeseries[].tag           | Key name of the timeseries on the platform.                                                                 |
| slave.values[].`<register_type>`.timeseries[].address       | Object address.                                                                                             |
| slave.values[].`<register_type>`.timeseries[].type          | Type of value.                                                                                              |
| slave.values[].`<register_type>`.timeseries[].objectsCount  | Count of objects to write.                                                                                  |
| slave.values[].`<register_type>`.timeseries[].value         | Initial register value.                                                                                     |
| slave.values[].`<register_type>`.timeseries[].bitTargetType | The response type can be either an integer (0/1) or a boolean (True/False). **Used only with type `bits`**. |
| ---                                                         |                                                                                                             |

Example of the attributes and timeseries configuration:

```json
"slave": {
  ...
  "values": {
    "holding_registers": {
      "attributes": [
        {
          "address": 1,
          "type": "string",
          "tag": "sm",
          "objectsCount": 1,
          "value": "ON"
        }
      ],
      "timeseries": [
        {
          "address": 2,
          "type": "16int",
          "tag": "smm",
          "objectsCount": 1,
          "value": 12334
        }
      ],
    }
  }
}
```

##### Attribute updates

| **Parameter**                                                     | **Description**                                                                                             |
|:------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| slave.values[].`<register_type>`.attributeUpdates[]               | The list of attribute updates.                                                                              |
| slave.values[].`<register_type>`.attributeUpdates[].tag           | Key name of the attribute on the platform.                                                                  |
| slave.values[].`<register_type>`.attributeUpdates[].address       | Object address.                                                                                             |
| slave.values[].`<register_type>`.attributeUpdates[].type          | Type of value.                                                                                              |
| slave.values[].`<register_type>`.attributeUpdates[].functionCode  | Function code to write value.                                                                               |
| slave.values[].`<register_type>`.attributeUpdates[].objectsCount  | Count of objects to write.                                                                                  |
| slave.values[].`<register_type>`.attributeUpdates[].value         | Initial register value.                                                                                     |
| slave.values[].`<register_type>`.attributeUpdates[].bitTargetType | The response type can be either an integer (0/1) or a boolean (True/False). **Used only with type `bits`**. |
| ---                                                               |                                                                                                             |

Example of the attribute updates configuration:

```json
"slave": {
  ...
  "values": {
    "holding_registers": {
      "attributeUpdates": [
        {
          "tag": "shared_attribute_write",
          "type": "32int",
          "functionCode": 6,
          "objectsCount": 2,
          "address": 29,
          "value": 1243
        }
      ],
    }
  }
}
```

##### RPC methods

| **Parameter**                                        | **Description**                                                                                             |
|:-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| slave.values[].`<register_type>`.rpc[]               | The list of attribute updates.                                                                              |
| slave.values[].`<register_type>`.rpc[].tag           | Key name of the attribute on the platform.                                                                  |
| slave.values[].`<register_type>`.rpc[].address       | Object address.                                                                                             |
| slave.values[].`<register_type>`.rpc[].type          | Type of value.                                                                                              |
| slave.values[].`<register_type>`.rpc[].functionCode  | Function code to write value.                                                                               |
| slave.values[].`<register_type>`.rpc[].objectsCount  | Count of objects to write.                                                                                  |
| slave.values[].`<register_type>`.rpc[].value         | Initial register value.                                                                                     |
| slave.values[].`<register_type>`.rpc[].bitTargetType | The response type can be either an integer (0/1) or a boolean (True/False). **Used only with type `bits`**. |
| ---                                                  |                                                                                                             |

Example of the RPC methods configuration:

```json
"slave": {
  ...
  "values": {
    "holding_registers": {
      "rpc": [
        {
          "tag": "setValue",
          "type": "16int",
          "functionCode": 5,
          "objectsCount": 1,
          "address": 31,
          "value": 22
        }
      ]
    }
  }
}
```

## Additional information

Here's more details regarding Modbus functions and the supported data types.

### Modbus functions

The Modbus connector supports the following Modbus functions:

| **Modbus function code** | **Description**                 |
|:-------------------------|---------------------------------|
| *Read data*              |                                 |
| **1**                    | Read Coils                      |
| **2**                    | Read Discrete Inputs            |
| **3**                    | Read Multiple Holding Registers |
| **4**                    | Read Input Registers            |
| *Write data:*            |                                 |
| **5**                    | Write Coil                      |
| **6**                    | Write Register                  |
| **15**                   | Write Coils                     |
| **16**                   | Write Registers                 |
| ---                      |                                 |

### Data types

A list and description of the supported data types for reading/writing data.

| **Type**    | **Function code** | **Objects count** | **Note**                                                                                                                         |
|:------------|-------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **string**  | 3-4               | 1-...             | Read bytes from registers and decode it ('UTF-8' coding).                                                                        |
| **bytes**   | 3-4               | 1-...             | Read bytes from registers.                                                                                                       |
| **bits**    | 1-4               | 1-...             | Read coils. If the objects count is 1, result will be interpreted as a boolean. Otherwise the result will be an array with bits. |
| **16int**   | 3-4               | 1                 | Integer 16 bit.                                                                                                                  |
| **16uint**  | 3-4               | 1                 | Unsigned integer 16 bit.                                                                                                         |
| **16float** | 3-4               | 1                 | Float 16 bit.                                                                                                                    |
| **32int**   | 3-4               | 2                 | Integer 32 bit.                                                                                                                  |
| **32uint**  | 3-4               | 2                 | Unsigned integer 32 bit.                                                                                                         |
| **32float** | 3-4               | 2                 | Float 32 bit.                                                                                                                    |
| **64int**   | 3-4               | 4                 | Integer 64 bit.                                                                                                                  |
| **64uint**  | 3-4               | 4                 | Unsigned integer 64 bit.                                                                                                         |
| **64float** | 3-4               | 4                 | Float 64 bit.                                                                                                                    |
| ---         |                   |                   |                                                                                                                                  |

## Next steps

Explore guides related to main SENTIENT features:

- [How to connect Modbus device to SENTIENT using SENTIENT IoT Gateway](/docs/iot-gateway/guides/how-to-connect-modbus-device/)
- [Data Visualization](/docs/user-guide/dashboards/) - how to visualize collected data.
- [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
- [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
- [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
- [Rule Engine](/docs/user-guide/rule-engine-2-0/overview/) - how to use rule engine to analyze data from devices.
