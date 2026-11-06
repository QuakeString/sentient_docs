+++
title = "Request Connector Configuration"
description = "HTTP protocol support for SENTIENT IoT Gateway"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/config/request.md"
+++
This guide will help you to get familiar with Request Connector configuration for SENTIENT IoT Gateway.  
Use [general configuration guide](/docs/iot-gateway/configuration/) to enable this Connector.  
The purpose of this Connector is to connect to external HTTP(S) API endpoints and get data from them.  
Connector is also able to push data to external HTTP(S) API based on the updates/commands from SENTIENT.    

This connector is useful when you have some HTTP(S) API endpoints in your device or some data in external resource and you would like to push this data to the SENTIENT.    

We will describe connector configuration file below.  

## Connector configuration: request.json

Connector configuration is a JSON file that contains information about how to connect to external API endpoints, what urls to use when reading data and how to process the data.  
Let's review the format of the configuration file using example below.    

<b>Example of Request Connector config file.</b>

Example listed below will connect to server on a localhost with 5000 port.  
Connector will use basic HTTP authorization using username and password.  
Then, connector will read data from a list of endpoints using urls from mapping section. See more info in a description below.  


<table class="includecode"><tr><td>
```conf
{
  "host": "http://127.0.0.1:5000",
  "SSLVerify": true,
  "security": {
    "type": "basic",
    "username": "user",
    "password": "password"
  },
  "mapping": [
    {
      "url": "getdata",
      "httpMethod": "GET",
      "httpHeaders": {
        "ACCEPT": "application/json"
      },
      "allowRedirects": true,
      "timeout": 0.5,
      "scanPeriod": 5,
      "converter": {
        "type": "json",
        "deviceNameJsonExpression": "SD8500",
        "deviceTypeJsonExpression": "SD",
        "attributes": [
          {
            "key": "serialNumber",
            "type": "string",
            "value": "${serial}"
          }
        ],
        "telemetry": [
          {
            "key": "Maintainer",
            "type": "string",
            "value": "${Developer}"
          },
          {
            "key": "Pressure",
            "type": "integer",
            "value": "${press}"
          }
        ]
      }
    },
    {
      "url": "get_info",
      "httpMethod": "GET",
      "httpHeaders": {
        "ACCEPT": "application/json"
      },
      "allowRedirects": true,
      "timeout": 0.5,
      "scanPeriod": 100,
      "converter": {
        "type": "custom",
        "deviceNameJsonExpression": "SD8500",
        "deviceTypeJsonExpression": "SD",
        "extension": "CustomRequestUplinkConverter",
        "extension-config": [
          {
            "key": "Totaliser",
            "type": "float",
            "fromByte": 0,
            "toByte": 4,
            "byteorder": "big",
            "signed": true,
            "multiplier": 1
          },
          {
            "key": "Flow",
            "type": "int",
            "fromByte": 4,
            "toByte": 6,
            "byteorder": "big",
            "signed": true,
            "multiplier": 0.01
          }
        ]
      }
    }
  ],
  "attributeUpdates": [
      {
        "httpMethod": "POST",
        "httpHeaders": {
          "CONTENT-TYPE": "application/json"
        },
        "timeout": 0.5,
        "tries": 3,
        "allowRedirects": true,
        "deviceNameFilter": "SD.*",
        "attributeFilter": "send_data",
        "requestUrlExpression": "sensor/${deviceName}/${attributeKey}",
        "valueExpression": "{\"${attributeKey}\":\"${attributeValue}\"}"
      }
  ],
  "serverSideRpc": [
    {
      "deviceNameFilter": ".*",
      "methodFilter": "echo",
      "requestUrlExpression": "sensor/${deviceName}/request/${methodName}/${requestId}",
      "responseTimeout": 1,
      "httpMethod": "GET",
      "valueExpression": "${params}",
      "timeout": 0.5,
      "tries": 3,
      "httpHeaders": {
        "Content-Type": "application/json"
      }
    },
    {
      "deviceNameFilter": ".*",
      "methodFilter": "no-reply",
      "requestUrlExpression": "sensor/${deviceName}/request/${methodName}/${requestId}",
      "httpMethod": "POST",
      "valueExpression": "${params}",
      "httpHeaders": {
        "Content-Type": "application/json"
      }
    }
  ]
}
```


</td></tr></table>


### General section

| **Parameter** | **Default value**                 | **Description**                                           |
|:-|:-|-
| host          | **http://127.0.0.1:5000**         | Domain address or ip of the server.                       |
| SSLVerify     | **true**                          | Verify or no SSL certificate on the server if available.  |
|---


### Security section

This section provides configuration for client authorization at the external server.
 


<div class="st-tabs">

<div class="st-tab" data-label="BasicRecommended">


One type of security configuration is Basic authentication.
The Request Connector sends HTTP requests with the Authorization header that contains the word Basic word followed by a space and a base64-encoded string username:password.

|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| type               | **basic**                      | Type of authorization.      |
| username           | **username**                   | Username for authorization. |
| password           | **password**                   | Password for authorization. |
|---

Security section in configuration file will look like this: 

```yaml
    "security": {
      "type": "basic",
      "username": "username",
      "password": "password"
    }
```

Since SENTIENT IoT Gateway version 3.8.3, environment variables can be specified for username and password fields. 
This allows you to avoid hardcoding sensitive information in the configuration file and provide it securely at runtime.

To use ENV variables for username and password, you can set them in your environment or define them in 
your `docker-compose.yml` file.

The following ENV variables are used for Basic authentication configuration:

- `REQUEST_BASIC_USERNAME`
- `REQUEST_BASIC_PASSWORD`

Make attention that if you specify ENV variables for username and password, the values from the configuration file 
will be ignored, and the connector will use the values from the ENV variables instead.


</div>

<div class="st-tab" data-label="AnonymousNo security">


 
Anonymous auth is the most simple option. It is useful for testing.  


|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| type               | **anonymous**                      | Type of authorization.      |
|---

Security subsection in configuration file will look like this: 

```yaml
    "security": {
      "type": "anonymous"
    }
```


</div>

</div>


### Mapping section

This configuration section contains array of objects with endpoints that the gateway will try to read after connecting to the server.  
Also this section contains settings about processing incoming messages (converter).  
After request, each response from that url is analyzed to extract device name, type and data (attributes and/or timeseries values).  
By default, the gateway uses Json converter, but it is possible to provide custom converter. See [example](https://github.com/sentient/sentient-gateway/blob/master/sentient_gateway/extensions/request/custom_request_uplink_converter.py) in the source code.  

**Note**: You can specify multiple mapping objects inside the array.

| **Parameter**     | **Default value**                     | **Description**                                                   |
|:-|:-|-
| url               | **getdata**                           | Url address for sending request.                                  |
| httpMethod        | **GET**                               | HTTP method for request (**GET**, **POST** etc.).                 |
| httpHeaders       | **{ "ACCEPT": "application/json" }**  | Object contains additional HTTP headers for request.              |
| allowRedirects    | **true**                              | Allow request redirection.                                        |
| timeout           | **0.5**                               | Timeout for request.                                              |
| scanPeriod        | **5**                                 | Rescan rate.                                                      |
|---


#### Converter subsection

This subsection contains configuration for processing incoming messages.  

Types of request converters:  
1. json -- Default converter  
2. custom -- Custom converter (You can write it by yourself, and it will use to convert incoming data from the response.)  


<div class="st-tabs">

<div class="st-tab" data-label="jsonRecommended if json will be received in response">

Json converter is default converter, it looks for deviceName, deviceType, attributes and telemetry in the incoming message from the broker, with rules, described in this subsection:

| **Parameter**             | **Default value**     | **Description**                                                                                                                                                                                                                       |
|:--------------------------|:----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| type                      | **json**              | Provides information to connector that default converter will be uses for converting data from response.                                                                                                                              |
| deviceNameJsonExpression  | **SD8500**            | Simple JSON expression, uses for looking device name in the incoming message (string "SD8500" will be used as device name).                                                                                                           |
| deviceTypeJsonExpression  | **SD**                | Simple JSON expression, uses for looking device type in the incoming message (string "SD" will be used as device type).                                                                                                               |
| timeout                   | **60000**             | Timeout for triggering "Device Disconnected" event                                                                                                                                                                                    |
| attributes                |                       | This subsection contains parameters of the incoming message, that will be interpreted as attributes for the device.                                                                                                                   |
| ... type                  | **string**            | Type of incoming data for a current attribute.                                                                                                                                                                                        |
| ... key                   | **serialNumber**      | Attribute name, that will sends to SENTIENT instance.                                                                                                                                                                              |
| ... value                 | **${serial}**         | Simple JSON expression, uses for looking value in the incoming message, that will send to SENTIENT instance as value of key parameter.                                                                                             |
| timeseries                |                       | This subsection contains parameters of the incoming message, that will be interpreted as telemetry for the device.                                                                                                                    |
| ... type                  | **string**            | Type of incoming data for a current telemetry.                                                                                                                                                                                        |
| ... key                   | **Maintainer**        | Telemetry name, that will sends to SENTIENT instance.                                                                                                                                                                              |
| ... value                 | **${Developer}**      | Simple JSON expression, uses for looking value in the incoming message, that will send to SENTIENT instance as value of key parameter.                                                                                             |
| ... type                  | **integer**           | Type of incoming data for a current telemetry.                                                                                                                                                                                        |
| ... key                   | **Pressure**          | Telemetry name, that will sends to SENTIENT instance.                                                                                                                                                                              |
| ... value                 | **${press}**          | Simple JSON expression, uses for looking value in the incoming message, that will send to SENTIENT instance as value of key parameter.                                                                                             |
| ... tsField               | **${timestampField}** | **Optional.** JSON-path expression for field that carries a datetime string. If not present, the `ts` or `timestamp` properties from incoming message will be used as timestamp for data entry.                                       |                                                                                                                     
| ... dayfirst              | **false**             | **Optional.** Points out that the first number is the **day** (`DD.MM.YY HH:mm:ss.SSS`).<br>• `false` → `10.11.24 10:10:10.252` → **11 Oct 2024 10:10:10.252** <br>• `true`  → `10.11.24 10:10:10.252` → **10 Nov 2024 10:10:10.252** |
| ... yearfirst             | **false**             | **Optional.** Points out that the first number is the **year** (`DD.MM.YY HH:mm:ss.SSS`).<br>• `false` → follows `dayfirst` rule<br>• `true`  → `10.11.24 10:10:10.252` → **24 Nov 2010 10:10:10.252**                                |
| ---                       


<div class="st-callout info">


**Parameters in attributes and telemetry section may differ from those presented above, but will have the same structure.**  


</div>


Mapping subsection will look like:

```json
    {
      "url": "getdata",
      "httpMethod": "GET",
      "httpHeaders": {
        "ACCEPT": "application/json"
      },
      "allowRedirects": true,
      "timeout": 0.5,
      "scanPeriod": 5,
      "converter": {
        "type": "json",
        "deviceNameJsonExpression": "SD8500",
        "deviceTypeJsonExpression": "SD",
        "attributes": [
          {
            "key": "serialNumber",
            "type": "string",
            "value": "${serial}"
          }
        ],
        "telemetry": [
          {
            "key": "Maintainer",
            "type": "string",
            "value": "${Developer}"
          },
          {
            "key": "Pressure",
            "type": "integer",
            "value": "${press}",
            "tsField": "${timestampField}",
            "dayfirst": true
          }
        ]
      }
    }
```


<div class="st-callout info">


**Note**: In **Mapping subsection** configuration section for `Pressure` timeseries key illustrates how to use the `tsField` and `dayfirst` options.


</div>


Also, you can combine values from HTTP request in attributes, telemetry and serverSideRpc section, for example:
```json
{
      "url": "getdata",
      "httpMethod": "GET",
      "httpHeaders": {
        "ACCEPT": "application/json"
      },
      "allowRedirects": true,
      "timeout": 0.5,
      "scanPeriod": 5,
      "converter": {
        "type": "json",
        "deviceNameJsonExpression": "SD8500",
        "deviceTypeJsonExpression": "SD",
        "attributes": [],
        "telemetry": [
          {
            "type": "double",
            "key": "temperature",
            "value": "${temp}"
          },
          {
            "type": "double",
            "key": "humidity",
            "value": "${hum}"
          },
          {
            "type": "string",
            "key": "combine",
            "value": "${hum}:${temp}"
          }
        ]
      }
    }
```


</div>

<div class="st-tab" data-label="customRecommended if bytes or anything else will be received in response">

A custom converter is converter written for some device:


|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| type                        | **custom**                         | Provides information to connector that custom converter will be uses for converting data from response.                                  |
| extension                   | **CustomRequestUplinkConverter**   | Name of custom converter class.                                                                                                       |
| extension-config            |                                    | This subsection is a configuration for the custom converter. In default example it contains setting for parsing response string.      |
| key                         | **Totaliser**                      | In this example value "Totaliser" will be interpreted as a telemetry key in SENTIENT instance.                                     |
| type                        | **float**                          | In this example type of the data.                                                                                                     |
| fromByte                    | **0**                              | In this example start byte position in the response string.                                                                           |
| toByte                      | **4**                              | In this example start byte position in the response string.                                                                           |
| byteorder                   | **big**                            | In this example byteorder for response string.                                                                                        |
| signed                      | **true**                           | In this example using to indicate is the data in response signed.                                                                     |
| multiplier                  | **1**                              | In this example every data from in response should be multiplied to some coefficient.                                                 | 
|--- 


<div class="st-callout info">


<br>
  
**Custom converter usually needed if you want to collect data from some device with not regular structure in response or when the data needs some processing before sending it to the SENTIENT.**  


</div>


Mapping subsection in the configuration will look like:
```json
    {
      "url": "get_info",
      "httpMethod": "GET",
      "httpHeaders": {
        "ACCEPT": "application/json"
      },
      "allowRedirects": true,
      "timeout": 0.5,
      "scanPeriod": 100,
      "converter": {
        "type": "custom",
        "deviceNameJsonExpression": "SD8500",
        "deviceTypeJsonExpression": "SD",
        "extension": "CustomRequestUplinkConverter",
        "extension-config": [
          {
            "key": "Totaliser",
            "type": "float",
            "fromByte": 0,
            "toByte": 4,
            "byteorder": "big",
            "signed": true,
            "multiplier": 1
          },
          {
            "key": "Flow",
            "type": "int",
            "fromByte": 4,
            "toByte": 6,
            "byteorder": "big",
            "signed": true,
            "multiplier": 0.01
          }
        ]
      }
    }
```


</div>

</div>


### Attribute update section

Configuration in this section are optional.  
SENTIENT allows to provision device attributes and fetch some of them from the device application.
You can treat this as a remote configuration for devices. Your devices are able to request shared attributes from SENTIENT.
See [user guide](/docs/user-guide/attributes/) for more details.

The "**attributeRequests**" configuration allows configuring the format of the corresponding attribute request and response messages. 

| **Parameter**                 | **Default value**                                     | **Description**                                                                                    |
|:-|:-|-
| httpMethod                    | **GET**                                               | HTTP method for request (**GET**, **POST** etc.).                                                  |
| httpHeaders                   | **{ "CONTENT-TYPE": "application/json" }**            | Object contains additional HTTP headers for request.                                               |
| timeout                       | **0.5**                                               | Timeout for request.                                                                               |
| tries                         | **3**                                                 | Count of tries to send data                                                                        |
| allowRedirects                | **true**                                              | Allow request redirection.                                                                         |
| deviceNameFilter              | **SD.\***                                             | Regular expression device name filter, uses to determine, which function to execute.               |
| attributeFilter               | **send_data**                                         | Regular expression attribute name filter, uses to determine, which function to execute.            |
| requestUrlExpression          | **sensor/${deviceName}/${attributeKey}**              | JSON-path expression uses for creating url address to send a message.                              |
| valueExpression               | **{\\"${attributeKey}\\":\\"${attributeValue}\\"}**   | JSON-path expression uses for creating the message data that will send to url.                     |
|---

The **attributeUpdates** section will look like:

```json

  "attributeUpdates": [
      {
        "httpMethod": "POST",
        "httpHeaders": {
          "CONTENT-TYPE": "application/json"
        },
        "timeout": 0.5,
        "tries": 3,
        "allowRedirects": true,
        "deviceNameFilter": "SD.*",
        "attributeFilter": "send_data",
        "requestUrlExpression": "sensor/${deviceName}/${attributeKey}",
        "valueExpression": "{\"${attributeKey}\":\"${attributeValue}\"}"
      }
  ]

```

### Server side RPC section

SENTIENT allows sending [RPC commands](/docs/user-guide/rpc/) to the device that is connected to SENTIENT directly or via Gateway.
 
Configuration, provided in this section uses for sending RPC requests from SENTIENT to device.

| **Parameter**                 | **Default value**                                                 | **Description**                                                                       |
|:-|:-|-
| deviceNameFilter              | **SmartMeter.\***                                                 | Regular expression device name filter, uses to determine, which function to execute.  |
| methodFilter                  | **echo**                                                          | Regular expression method name filter, uses to determine, which function to execute.  |
| requestUrlExpression          | **sensor/${deviceName}/request/${methodName}/${requestId}**       | JSON-path expression, uses to create url address to send RPC request.                 |
| responseTimeout               | **0.5**                                                           | Timeout for request.                                                                  |
| httpMethod                    | **GET**                                                           | HTTP method for request (**GET**, **POST** etc.).                                     |
| valueExpression               | **${params}**                                                     | JSON-path expression, uses for creating data for sending to the external endpoint.    |
| timeout                       | **0.5**                                                           | Timeout for request.                                                                  |
| tries                         | **3**                                                             | Count of tries to send data                                                           |
| httpHeaders                   | **{ "CONTENT-TYPE": "application/json" }**                        | Object contains additional HTTP headers for request.                                  |
|---


<div class="st-callout info">


**There are 2 types of the RPC calls:**  
1. With reply, after sending request the gateway will wait for response and send it to SENTIENT.
2. With no reply, after sending request the gateway will not wait for response.

Examples for both methods provided below.


</div>


```json
  "serverSideRpc": [
    {
      "deviceNameFilter": ".*",
      "methodFilter": "echo",
      "requestUrlExpression": "sensor/${deviceName}/request/${methodName}/${requestId}",
      "responseTimeout": 1,
      "httpMethod": "GET",
      "valueExpression": "${params}",
      "timeout": 0.5,
      "tries": 3,
      "httpHeaders": {
        "Content-Type": "application/json"
      }
    },
    {
      "deviceNameFilter": ".*",
      "methodFilter": "no-reply",
      "requestUrlExpression": "sensor/${deviceName}/request/${methodName}/${requestId}",
      "httpMethod": "POST",
      "valueExpression": "${params.hum}",
      "httpHeaders": {
        "Content-Type": "application/json"
      }
    }
  ]
```

## Next steps

Explore guides related to main SENTIENT features:

 - [Data Visualization](/docs/user-guide/dashboards/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine-2-0/overview/) - how to use rule engine to analyze data from devices.
