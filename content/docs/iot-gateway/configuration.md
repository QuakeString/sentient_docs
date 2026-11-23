+++
title = "IoT Gateway Configuration"
description = "Installation structure and configuration of SENTIENT IoT Gateway"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/configuration.md"
+++
## Directory structure

Please see default directory structure below for daemon installation.

```
/etc/sentient-gateway/config                   - Configuration folder.
    st_gateway.json                               - Main configuration file for Gateway.
    logs.json                                     - Configuration file for logging.
    modbus.json                                   - Modbus connector configuration.
    mqtt.json                                     - MQTT connector configuration.
    ble.json                                      - BLE connector configuration.
    opcua.json                                    - OPC-UA connector configuration.
    request.json                                  - Request connector configuration.
    can.json                                      - CAN connector configuration. 
    ... 

/var/lib/sentient_gateway/extensions           - Folder for custom connectors/converters.                      
    modbus                                        - Folder for Modbus custom connectors/converters.
    mqtt                                          - Folder for MQTT custom connectors/converters.
        __init__.py                               - Default Python package file, needed for correct imports.
        custom_uplink_mqtt_converter.py           - Custom MQTT converter example.
    ...
    opcua                                         - Folder for OPC-UA custom connectors/converters.
    ble                                           - Folder for BLE custom connectors/converters.
    request                                       - Folder for Request custom connectors/converters.
    can                                           - Folder for CAN custom connectors/converters.

/var/log/sentient-gateway                      - Logs folder.
    connector.log                                 - Connector logs.
    service.log                                   - Main gateway service logs.
    storage.log                                   - Storage logs.
    st_connection.log                             - Logs for connection to the SENTIENT instance.
```

## Environmental variables


<div class="st-callout info">


**Values of environment variables have a higher priority than values of parameters from the configuration file.
This means that the gateway will use the values of the environment variables (if they are set) 
and not the values from the configuration file.**


</div>


The gateway provides the capability to configure essential connection parameters using environment variables. 
For example, let's illustrate how you can configure basic parameters such as the host, port, and access token by using 
environment variables within a Docker Compose file. Here’s how you can achieve this:

```yaml
version: '3.4'
services:
  # SENTIENT IoT Gateway Service Configuration
  st-gateway:
    image: sentient/st-gateway
    container_name: st-gateway
    ...
    # Environment variables
    environment:
      - ST_GW_HOST=host.docker.internal
      - ST_GW_PORT=1883
      - ST_GW_ACCESS_TOKEN=YOUR_ACCESS_TOKEN
    ...
```

In the example above, we set the "**host.docker.internal**" as a host, **1883** as a port and "**YOUR_ACCESS_TOKEN**" 
as an access token for the gateway using the "**ST_GW_HOST**", "**ST_GW_PORT**" and "**ST_GW_ACCESS_TOKEN**" 
environment variables, respectively.

The following environmental variables can be used to configure the SENTIENT IoT Gateway:

| **ENV variable**     | **Default value**             | **Description**                                                                   |
|----------------------|-------------------------------|-----------------------------------------------------------------------------------|
| ST_GW_HOST           | **host.docker.internal**      | Hostname or IP address of SENTIENT server.                                     |
| ST_GW_PORT           | **1883**                      | Port of MQTT service on SENTIENT server.                                       |
| ST_GW_ACCESS_TOKEN   | **YOUR_ACCESS_TOKEN**         | Access token for the gateway from SENTIENT server.                             |
| ST_GW_CA_CERT        |                               | Path to CA certificate file.                                                      |
| ST_GW_PRIVATE_KEY    |                               | Path to private key file.                                                         |
| ST_GW_CERT           |                               | Path to certificate file.                                                         |
| ST_GW_CLIENT_ID      |                               | MQTT client id for the gateway form SENTIENT server.                           |
| ST_GW_USERNAME       |                               | MQTT username for the gateway form SENTIENT server.                            |
| ST_GW_PASSWORD       |                               | MQTT password for the gateway form SENTIENT server.                            |
| ST_GW_RATE_LIMITS    | **15:1,300:60,**              | Messages rate limit to SENTIENT server in `MESSSAGE_COUNT:TIME,` format.       |
| ST_GW_DP_RATE_LIMITS | **15:1,300:60,**              | Data points rate limit to SENTIENT server in `DATA_POINTS_COUNT:TIME,` format. |
| ST_GW_LOGS_PATH      | **/sentient_gateway/logs** | Path to the logs folder.                                                          |

## General configuration file

The main configuration file that is used for connection to SENTIENT platform instance and enable/disable connectors. 

The example configuration file provided below sets a connection to the SENTIENT instance located at 
sentient.cloud and utilizes memory file storage, which is set up to hold a maximum of 100,000 records. There are 4 
different connectors active. If you prefer to use only one, simply remove the others from the configuration.

<b>Example of main configuration file. Press to show.</b>


<table class="includecode"><tr><td>
```conf
{
  "sentient": {
    "host": "sentient.cloud",
    "port": 1883,
    "remoteShell": false,
    "remoteConfiguration": true,
    "statistics": {
      "enable": true,
      "statsSendPeriodInSeconds": 60
    },
    "deviceFiltering": {
      "enable": false,
      "filterFile": "list.json"
    },
    "maxPayloadSizeBytes": 1024,
    "minPackSendDelayMS": 60,
    "minPackSizeToSend": 500,
    "checkConnectorsConfigurationInSeconds": 10,
    "handleDeviceRenaming": true,
    "security": {
      "type": "accessToken",
      "accessToken": "YOUR_ACCESS_TOKEN"
    },
    "qos": 1,
    "checkingDeviceActivity": {
      "checkDeviceInactivity": false,
      "inactivityTimeoutSeconds": 200,
      "inactivityCheckPeriodSeconds": 500
    }
  },
  "storage": {
    "type": "memory",
    "read_records_count": 100,
    "max_records_count": 10000
  },
  "grpc": {
    "enabled": false,
    "serverPort": 9595,
    "keepaliveTimeMs": 10000,
    "keepaliveTimeoutMs": 5000,
    "keepalivePermitWithoutCalls": true,
    "maxPingsWithoutData": 0,
    "minTimeBetweenPingsMs": 10000,
    "minPingIntervalWithoutDataMs": 5000,
    "keepAliveTimeMs": 10000,
    "keepAliveTimeoutMs": 5000
  },
  "connectors": [
    {
      "type": "mqtt",
      "name": "MQTT Broker Connector",
      "configuration": "mqtt.json"
    },
    {
      "type": "modbus",
      "name": "Modbus Connector",
      "configuration": "modbus.json"
    },
    {
      "type": "modbus",
      "name": "Modbus Serial Connector",
      "configuration": "modbus_serial.json"
    },
    {
      "type": "opcua",
      "name": "OPC-UA Connector",
      "configuration": "opcua.json"
    }
  ]
}
```


</td></tr></table>


### Sections in config file

+ **sentient** -- Configuration for connecting to SENTIENT platform.
  - *security* -- Configuration for type of encryption and authorization.
+ **storage** -- Configuration for local storage of incoming data from devices.
+ **connectors** -- Array of Connectors and their configuration to use.

### Connection to SENTIENT

|**Parameter**             | **Default value**                            | **Description**                                                                         |
|---                       |---                                           |-----------------------------------------------------------------------------------------|
| ***sentient***        |                                              | Configuration for connection to server.                                                 |
| host                     | **sentient.cloud**                        | Hostname or IP address of SENTIENT server.                                           |
| port                     | **1883**                                     | Port of MQTT service on SENTIENT server.                                             |
| qos                      | **1**                                        | QoS levels 0 (at most once) and 1 (at least once).                                      |
| minPackSendDelayMS       | **200**                                      | Delay between sending packets (Decreasing this setting results in increased CPU usage). |
| minPackSizeToSend        | **500**                                      | Minimum size of packs to send.                                                          |

#### Subsection "statistics"

This subsection is used to configure collecting statistics data and sending them to SENTIENT IoT Gateway device attributes.

|**Parameter**|**Default value**| **Description**                                                                |
|:-|:-|--------------------------------------------------------------------------------
| statistics                   |                 | Configuration for enabling statistics collecting.                              |
| ... enable                   | true            | A boolean value that is used to on/off collecting statistics.                  |
| ... statsSendPeriodInSeconds | 3600            | An integer value is utilized for transmitting data at regular intervals.       |
| ... configuration            | statistics.json | Name of a configuration file for additional user statistics data (in seconds). |
|---

You can define additional parameter "configuration" and provide your own command for collecting some additional data.
This configuration file can look like the example below:
```json
[
  {
    "timeout": 100,
    "command": ["/bin/sh", "-c", "ps -A -o cpu,%mem | awk '{cpu += $1}END{print cpu}'"],
    "attributeOnGateway": "CPU"
  },
  {
    "timeout": 100,
    "command": ["/bin/sh", "-c", "ps -A -o %cpu,%mem | awk '{mem += $2}END{print mem}'"],
    "attributeOnGateway": "Memory"
  },
  {
    "timeout": 100,
    "command": ["/bin/sh", "-c", "ipconfig getifaddr en0"],
    "attributeOnGateway": "IP address"
  },
  {
    "timeout": 100,
    "command": ["/bin/sh", "-c", "sw_vers -productName"],
    "attributeOnGateway": "OS"
  },
  {
    "timeout": 100,
    "command": ["/bin/sh", "-c", "uptime"],
    "attributeOnGateway": "Uptime"
  },
  {
    "timeout": 100,
    "command": ["/bin/sh", "-c", "system_profiler SPUSBDataType"],
    "attributeOnGateway": "USBs"
  }
]
```
Also, you can find example files for different OS (Linux, macOS, Windows) in `/config/statistics/` folder.

#### Subsection "deviceFiltering"

This subsection is optional and used to filter allowed devices to send data to SENTIENT.

The Device Filtering feature allows you to define rules for filtering devices based on specific criteria.

| **Parameter**                    | **Default value** | **Description**                                       |
|:---------------------------------|:------------------|------------------------------------------------------- 
| deviceFiltering                  |                   | Configuration for device filtering                    |
| ... enable                       | **false**         | Boolean value that is used to on/off device filtering |
| ... filterFile                   | **list.json**     | Name of a configuration file                          |
| ---                              

Configuration file can look like the example below:
```json
{
  "deny": {
    "MQTT Broker Connector": [
      "Temperature Device",
      "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)"
    ],
    "Modbus Connector": [
      "My Modbus Device"
    ]
  },
  "allow": {
    "MQTT Broker Connector": [
      "My Temperature Sensor"
    ]
  }
}
```
The configuration above consists of two main properties: "deny" and "allow". Each property contains a 
set of connector types as keys, with corresponding arrays of device names as their values.

The "deny" property is used to specify devices that should be denied access to certain connector names. 
The devices listed under each connector name will be blocked from accessing the specified connector.

The structure of the "deny" property is as follows:
```json
"deny": {
  "<Connector Name>": [
    "<Device Name 1>",
    "<Device Name 2>",
    ...
  ],
  ...
}
```
Example:
```json
"deny": {
  "MQTT Broker Connector": [
    "Temperature Device",
    "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)"
  ],
  "Modbus Connector": [
    "My Modbus Device"
  ]
}
```

In the above example, the following rules are defined:
* The device named "Temperature Device" and any device with an email address format are denied access to the "MQTT Broker Connector".
* The device named "My Modbus Device" is denied access to the "Modbus Connector".

The "allow" property is used to specify devices that should be explicitly allowed to access certain connector names. 
The devices listed under each connector name will have unrestricted access to the specified connector.

The structure of the "allow" property is as follows:
```json
"allow": {
  "<Connector Name>": [
    "<Device Name 1>",
    "<Device Name 2>",
    ...
  ],
  ...
}
```

Example:
```json
"allow": {
  "MQTT Broker Connector": [
    "My Temperature Sensor"
  ]
}
```

In the above example, the following rule is defined:
* The device named "My Temperature Sensor" is allowed access to the "MQTT Broker Connector".

The Device Filtering feature provides a flexible way to define rules for allowing or denying access 
to connector types based on device names. By using the "deny" and "allow" properties, you can easily control device 
access within your gateway.


#### Subsection “checkingDeviceActivity”

This subsection is optional and used to monitor the activity of each connected device. 

If you define this section, the Gateway will check the activity of each device every n second that means, if the device 
is inactive for n seconds, it will disconnect it.

|**Parameter**|**Default value**|**Description**|
|:-|:-|- 
| checkingDeviceActivity           |              | Configuration for checking devices activity                   |
| ... checkDeviceInactivity        | **false**    | Boolean value that is used to on/off checking device activity |
| ... inactivityTimeoutSeconds     | **120**      | Inactivity device time after whose Gateway will disconnect it |
| ... inactivityCheckPeriodSeconds | **10**       | Periodicity of device activity check                          |
|---

#### Subsection "security"


There are 3 variants of security subsection:


<div class="st-tabs">

<div class="st-tab" data-label="Access TokenBasic security">


One type of security configuration is accessToken, 
to get it you should login into your SENTIENT platform instance, 
go to DEVICE tab, press the plus icon, 
fill the values and check the "Is gateway" option, 
open this device and press the "COPY ACCESS TOKEN" button and replace default with your value 


|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| accessToken              | **PUT_YOUR_GW_ACCESS_TOKEN_HERE**                     | Access token for the gateway from SENTIENT server.|
|---

Security subsection in configuration file will look like this: 

```json
...
"security": {
  "accessToken": "YOUR_ACCESS_TOKEN"
},
...
```


</div>

<div class="st-tab" data-label="Username and passwordBasic security">

One type of security configuration is using clientId, username, and password, to get them you should login into your 
SENTIENT platform instance, go to DEVICE tab, press the plus icon, fill the values and check the “Is gateway” option,
press "Next: Credentials", check "Add credentials", select credentials type "MQTT Basic" and replace default 
with your value.

|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| clientId                | **clientId**      | MQTT client id for the gateway form SENTIENT server     |
| username                | **admin**         | MQTT username for the gateway form SENTIENT server      |
| password                | **admin**         | MQTT password for the gateway form SENTIENT server      |
|---


```json
...
"security": {
  "clientId": "YOUR_CLIENT_ID",
  "username": "YOUR_USERNAME",
  "password": "YOUR_PASSWORD"
},
...
```

</div>

<div class="st-tab" data-label="TLS + Access TokenAdvanced security">

In table below described parameters to configure authorization of IoT gateway on SENTIENT platform.  

|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| accessToken              | **PUT_YOUR_GW_ACCESS_TOKEN_HERE**               | Access token for the gateway from SENTIENT server.       |
| caCert                   | **/etc/sentient-gateway/mqttserver.pub.pem** | Path to CA certificate file.                                |
|---    

Security subsection in configuration file will look like this: 

```json
...
"security": {
  "accessToken": "PUT_YOUR_GW_ACCESS_TOKEN_HERE",
  "caCert": "/etc/sentient-gateway/mqttserver.pub.pem"
},
...
```


</div>

<div class="st-tab" data-label="TLS + Private KeyAdvanced security">

In table below described parameters to configure authorization of IoT gateway on SENTIENT platform.  

|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| caCert                   | **/etc/sentient-gateway/ca.pem**          | Path to CA file.                                                      |
| privateKey               | **/etc/sentient-gateway/privateKey.pem**  | Path to private key file.                                             |
| cert                     | **/etc/sentient-gateway/certificate.pem** | Path to certificate file.                                             |
| checkCertPeriod          | **86400**                                    | The period in seconds when the certificate will be checked            |
| certificateDaysLeft      | **3**                                        | Days until the certificate expires, when a new one will be generated  |
|---    

Security subsection in configuration file will look like this: 

```json
...
"security": {
  "caCert": "/etc/sentient-gateway/ca.pem",
  "privateKey": "/etc/sentient-gateway/privateKey.pem",
  "cert": "/etc/sentient-gateway/certificate.pem",
  "checkCertPeriod": 86400,
  "certificateDaysLeft": 3
},
...
```


</div>

</div>


#### Subsection "provisioning"


There are 4 options of provisioning configuration (you can read more about provisioning in [the official documentation](/docs/user-guide/device-provisioning/)):


<div class="st-tabs">

<div class="st-tab" data-label="AutoServer generated access token">

Using the following config, you can configure Gateway to use auto-generated Access Token by server provisioning strategy:

| **Parameter**         | **Default value** | **Description**                                                                    |
|:----------------------|:------------------|------------------------------------------------------------------------------------
| type                  | **AUTO**          | Type of provisioning strategy.                                                     |
| provisionDeviceKey    | **DEVICE_KEY**    | Provisioning device key, you should take it from configured device profile.        |
| provisionDeviceSecret | **DEVICE_SECRET** | Provisioning device secret, you should take it from configured device profile.     |
| ---                   

Provisioning subsection in configuration file will look like this:
```json
...
"provisioning": {
  "type": "AUTO",
  "provisionDeviceKey": "PUT_YOUR_DEVICE_KEY_HERE",
  "provisionDeviceSecret": "PUT_YOUR_DEVICE_SECRET_HERE"
},
...
```


</div>

<div class="st-tab" data-label="Access TokenPredefined access token">

Using the following config, you can configure Gateway to use Access Token provisioning strategy:

| **Parameter**         | **Default value**        | **Description**                                                                    |
|:----------------------|:-------------------------|------------------------------------------------------------------------------------
| type                  | **ACCESS_TOKEN**         | Type of provisioning strategy.                                                     |
| provisionDeviceKey    | **DEVICE_KEY**           | Provisioning device key, you should take it from configured device profile.        |
| provisionDeviceSecret | **DEVICE_SECRET**        | Provisioning device secret, you should take it from configured device profile.     |
| ---                   

Provisioning subsection in configuration file will look like this:
```yaml
...
  provisioning:
    type: ACCESS_TOKEN
    provisionDeviceKey: PUT_YOUR_DEVICE_KEY_HERE
    provisionDeviceSecret: PUT_YOUR_DEVICE_SECRET_HERE
...
```


</div>

<div class="st-tab" data-label="Basic MQTTBasic MQTT Credentials">

Using the following config, you can configure Gateway to use MQTT Basic provisioning strategy:

| **Parameter**         | **Default value**   | **Description**                                                                    |
|:----------------------|:--------------------|------------------------------------------------------------------------------------
| type                  | **MQTT_BASIC**      | Type of provisioning strategy.                                                     |
| provisionDeviceKey    | **DEVICE_KEY**      | Provisioning device key, you should take it from configured device profile.        |
| provisionDeviceSecret | **DEVICE_SECRET**   | Provisioning device secret, you should take it from configured device profile.     |
| ---                   

Provisioning subsection in configuration file will look like this:
```json
...
"provisioning": {
  "type": "MQTT_BASIC",
  "provisionDeviceKey": "PUT_YOUR_DEVICE_KEY_HERE",
  "provisionDeviceSecret": "PUT_YOUR_DEVICE_SECRET_HERE"
},
...
```


</div>

<div class="st-tab" data-label="X.509 Certificate">

Using the following config, you can configure Gateway to use X.509 Certificate provisioning strategy:

| **Parameter**         | **Default value**        | **Description**                                                                |
|:----------------------|:-------------------------|--------------------------------------------------------------------------------
| type                  | **X509_CERTIFICATE**     | Type of provisioning strategy.                                                 |
| provisionDeviceKey    | **DEVICE_KEY**           | Provisioning device key, you should take it from configured device profile.    |
| provisionDeviceSecret | **DEVICE_SECRET**        | Provisioning device secret, you should take it from configured device profile. |
| caCert                | **ca-root.pem**  | Public key X509 for device in SENTIENT.                                     |
| ---                   

Provisioning subsection in configuration file will look like this:
```yaml
...
"provisioning": {
  "type": "X509_CERTIFICATE",
  "provisionDeviceKey": "PUT_YOUR_DEVICE_KEY_HERE",
  "provisionDeviceSecret": "PUT_YOUR_DEVICE_SECRET_HERE",
  "caCert": "/etc/sentient-gateway/ca.pem"
},
...
```


</div>

</div>


### Storage configuration

Configs in storage subsection provides configuration for saving incoming data before it will be send to SENTIENT platform.
  
There are 3 variants for this section: memory or file.
1. **Memory** storage - Received data saving to the RAM memory.
2. **File** storage - Received data saving to the hard drive.
3. **SQLite** storage - Received data saving to the .db files.


<div class="st-tabs">

<div class="st-tab" data-label="Memory storage (use for development or low-volume data when disk space is limited)">

|---
| **Parameter**            | **Default value**                            | **Description**                                                |
|:-|:-|-
| type                     | **memory**                                   | Storage type (Saving data to RAM, no save to hard drive).      |
| read_records_count       | **10**                                       | Count of messages to get from storage and send to SENTIENT. |
| max_records_count *      | **100**                                      | Maximum count of data in storage before send to SENTIENT.   |
|---


\* -- If receive data when storage has already counted, described in this parameter, new data will lose.

Storage section of configuration file will look like:

```json
...
"storage": {
  "type": "memory",
  "read_records_count": 10,
  "max_records_count": 100
},
...
```

</div>

<div class="st-tab" data-label="SQLite storage (high-performance on-disk persistence — recommended for most production setups)">

|---
| **Parameter**               | **Default value**                            | **Description** |
|:-|:-|-
| type                        | **sqlite**                                   | Storage type (Saving data to .db files).|
| data_file_path              | **./data/**                                  | Path to the directory that will contain database files (no filename). A trailing path separator is required.|
| max_read_records_count      | **1000**                                     | Maximum number of messages to get from storage and send to SENTIENT.|
| size_limit *                | **1024**                                     | Maximum size of each SQLite file in megabytes. When exceeded, triggers rotation to a new DB file.|
| max_db_amount *             | **10**                                       | Maximum number of rotated DB files to keep on disk. When reached, further writes are dropped until cleanup.|    
| oversize_check_period       | **1**                                        | How frequently (in minutes) to check the current DB’s file size against *size_limit*.|
| writing_batch_size          | **1000**                                     | Maximum number of messages collected before writing to the DB during single write request.|
| messages_ttl_check_in_hours | **1**                                        | How often will Gateway check data for obsolescence.|
| messages_ttl_in_days        | **7**                                        | How many days to retain messages in each DB before automatic deletion.|
|---


\* –- If the number of DB files reaches *max_db_amount* and last database exceeds *size_limit*, new data will be lost until previous data be read from databases and delivered to the platform.
Please note: the default database filename is **data.db**.<br>


Storage section of configuration file will look like:

```json
...
"storage": {
  "type": "sqlite",
  "data_file_path": "./data/", 
  "max_read_records_count": 1000,
  "size_limit": 1024,
  "max_db_amount": 10,
  "oversize_check_period": 1,
  "writing_batch_size": 1000,
  "messages_ttl_check_in_hours": 1,
  "messages_ttl_in_days": 7
},
...
```


</div>

<div class="st-tab" data-label="File storage (simple on-disk persistence — good for small/medium workloads) (Legacy)">

|---
| **Parameter**            | **Default value**                            | **Description**                                                |
|:-|:-|-
| type                     | **file**                                     | Storage type (Saving data to hard drive)                       |
| data_folder_path         | **./data/**                                  | Path to folder, that will contains data (Relative or Absolute).|
| max_read_records_count   | **6**                                        | Count of messages to get from storage and send to SENTIENT. |
| max_file_count *         | **5**                                        | Maximum count of file that will be saved.                      |
| max_records_per_file *   | **14**                                       | Maximum count of records that will be stored in one file.      |
|---


\* -- If receive data when storage has already counted this amount, described in this parameter, new data will lose.

Storage section of configuration file will look like:

```json
...
"storage": {
  "type": "file",
  "data_folder_path": "./data/",
  "max_file_count": 5,
  "max_read_records_count": 6,
  "max_records_per_file": 14
},
...
```


</div>

</div>


### Connectors configuration

Configs in connectors section configuration for connecting to devices by implemented protocols.
Config for every connector in this section must have parameters as in table below:  
 
|**Parameter**|**Default value**|**Description**|
|:-|:-|- 
| useGRPC                  | **true**                                     | **OPTIONAL** parameter that is used to on/off GRPC transport for default connector realisation |
| name                     | **MQTT Broker Connector**                    | Name of connector to broker.                                                                   |
| type                     | **mqtt**                                     | Type of connector, must be like a name of folder, contained configuration file.                |
| configuration            | **mqtt.json**                                | Name of the file with configuration in config folder.*                                         |
|---

\* -- Folder with this configuration file.  

Section connectors in your configuration file may differ from shown below, but they should have structure like this:  

```json
...
"connectors": [
  {
    "type": "mqtt",
    "name": "MQTT Broker Connector",
    "configuration": "mqtt.json"
  },
  {
    "type": "modbus",
    "name": "Modbus Connector",
    "configuration": "modbus.json"
  },
  {
    "type": "modbus",
    "name": "Modbus Serial Connector",
    "configuration": "modbus_serial.json"
  },
  {
    "type": "opcua",
    "name": "OPC-UA Connector",
    "configuration": "opcua.json"
  }
]
...
```

**Note:** You can use several similar connectors at same time, but you should provide different names and configuration files to them. 

If you need different type of connector, you can implement it using [customization guide](/docs/iot-gateway/custom/) or email us: <info@sentient.invenia.in>.
