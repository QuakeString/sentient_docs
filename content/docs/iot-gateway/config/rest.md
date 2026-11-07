+++
title = "REST Connector Configuration"
description = "REST API enpoints support for SENTIENT IoT Gateway"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/config/rest.md"
+++
This guide will help you to get familiar with REST Connector configuration for SENTIENT IoT Gateway.  
Use [general configuration guide](/docs/iot-gateway/configuration/) to enable this Connector.  
The purpose of this Connector is to create API endpoints and get data from received requests.  
Connector is also able to push data to external HTTP(S) API based on the updates/commands from SENTIENT.    

This connector is useful when you have some HTTP(S) API endpoints in your device or some data in external resource and you would like to push this data to the SENTIENT.    

We will describe connector configuration file below.  

## Connector configuration: rest.json

Connector configuration is a JSON file that contains information about how to create API endpoints and how to process the data.  
Let's review the format of the configuration file using example below.    

<b>Example of REST Connector config file.</b>

Example listed below will create a server on a localhost using 5000 port.  
Connector will use basic HTTP authorization using username and password.  
Then, connector will create endpoints from a list of endpoints using endpoints from mapping section. See more info in a description below.  

```json
{
  "server": {
    "host": "127.0.0.1",
    "port": 5000,
    "SSL": false,
    "security": {
      "cert": "~/ssl/cert.pem",
      "key": "~/ssl/key.pem"
    }
  },
  "mapping": [
    {
      "endpoint": "/test_device",
      "HTTPMethods": [
        "POST"
      ],
      "security": {
        "type": "basic",
        "username": "username",
        "password": "password"
      },
      "converter": {
        "type": "json",
        "deviceInfo": {
          "deviceNameExpression": "Device ${name}",
          "deviceNameExpressionSource": "request",
          "deviceProfileExpressionSource": "constant",
          "deviceProfileExpression": "default"
        },
        "attributes": [
          {
            "key": "model",
            "type": "string",
            "value": "${sensorModel}"
          }
        ],
        "timeseries": [
          {
            "key": "temperature",
            "type": "double",
            "value": "${temp}"
          },
          {
            "key": "humidity",
            "type": "double",
            "value": "${hum}"
          },
          {
            "key": "combine",
            "type": "string",
            "value": "${hum}:${temp}"
          }
        ]
      }
    },
    {
      "endpoint": "/anon2",
      "HTTPMethods": [
        "POST"
      ],
      "security": {
        "type": "anonymous"
      },
      "converter": {
        "type": "custom",
        "deviceInfo": {
          "deviceNameExpression": "SuperAnonDevice",
          "deviceNameExpressionSource": "constant",
          "deviceProfileExpressionSource": "constant",
          "deviceProfileExpression": "default"
        },
        "extension": "CustomRestUplinkConverter",
        "extensionConfig": {
          "key": "Totaliser",
          "datatype": "float",
          "fromByte": 0,
          "toByte": 4,
          "byteorder": "big",
          "signed": true,
          "multiplier": 1
        }
      }
    }
  ],
  "requestsMapping": {
    "attributeRequests": [],
    "attributeUpdates": [],
    "serverSideRpc": []
  }
}
```


### General section


<div class="st-tabs">

<div class="st-tab" data-label="With SSLRecommended">

| **Parameter** | **Default value**                 | **Description**                                           |
|:--------------|:-|-
| host          | **127.0.0.1**                     | Domain address or ip of the server.                       |
| port          | **5000**                          | Port of the server.                                       |
| SSL           | **true**                          | Verify or no SSL certificate on the server if available.  |
| cert          | **path_to_the_pem_file**          | Path to certificate file.                                 |
| key           | **path_to_the_key_file**          | Path to private key file.                                 |
| ---           

Configuration section will look like:

```json
{
  "server": {
    "host": "127.0.0.1",
    "port": 5000,
    "SSL": true,
    "security": {
      "cert": "~/ssl/cert.pem",
      "key": "~/ssl/key.pem"
    }
  }
}
```


</div>

<div class="st-tab" data-label="Without SSLNo security">

| **Parameter** | **Default value**                 | **Description**                                           |
|:--------------|:-|-
| host          | **127.0.0.1**                     | Domain address or ip of the server.                       |
| port          | **5000**                          | Port of the server.                                       |
| SSL           | **false**                         | Verify or no SSL certificate on the server if available.  |
| ---           

Configuration section will look like:
```json
{
  "server": {
    "host": "127.0.0.1",
    "port": 5000,
    "SSL": false,
    "security": {
      "cert": "~/ssl/cert.pem",
      "key": "~/ssl/key.pem"
    }
  }
}
```


</div>

</div>

  

### Mapping section

This configuration section contains array of objects with endpoints that the gateway will create.  
Also this section contains settings about processing incoming messages (converter).  
After request receiving, the message from the request is analyzed to extract device name, type and data (attributes and/or timeseries values).  
By default, the gateway uses Json converter, but it is possible to provide custom converter.

**Note**: You can specify multiple mapping objects inside the array.

| **Parameter** | **Default value**                     | **Description**                                             |
|:--------------|:-|-------------------------------------------------------------
| endpoint      | **/test_device**                      | Url address of the endpoint.                                |
| HTTPMethods   | **GET**                               | HTTP methods allowed for endpoint (**GET**, **POST** etc.). |
| ---           

#### Security section

This section provides configuration for client authorization at the gateway for every endpoint.
 


<div class="st-tabs">

<div class="st-tab" data-label="BasicRecommended">


One type of security configuration is Basic authentication.
The REST Connector waits for HTTP requests with the Authorization header that contains the word Basic word followed by a space and a base64-encoded string username:password.

|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| type               | **basic**                      | Type of authorization.      |
| username           | **username**                   | Username for authorization. |
| password           | **password**                   | Password for authorization. |
|---

Security section in configuration file will look like this: 

```json
{
  "security": {
    "type": "basic",
    "username": "username",
    "password": "password"
  }
}
```


Also, make sure that your request have `Authorization` header with provided credentials.

If you are using cURL, the request will look like:
```bash
curl --user username:password -H "Content-Type: application/json" -X POST \
    -d '{"name": "SN-001", "sensorModel": "example"}' http://127.0.0.1:5000/test_device
```

Or if you are using Postman or Insomnia, simply enable Basic auth.


</div>

<div class="st-tab" data-label="AnonymousNo security">


 
Anonymous auth is the most simple option. It is useful for testing.  


|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| type               | **anonymous**                      | Type of authorization.      |
|---

Security subsection in configuration file will look like this: 

```json
{
  "security": {
    "type": "anonymous"
  }
}
```


</div>

</div>


#### Converter subsection

This subsection contains configuration for processing incoming messages.  

Types of request converters:  
1. json -- Default converter  
2. custom -- Custom converter (You can write it by yourself, and it will use to convert incoming data.)  


<div class="st-callout info">


**Connector won't pass the None value from the converter**  


</div>


<div class="st-tabs">

<div class="st-tab" data-label="jsonRecommended if json will be received in the request">

Json converter is default converter, it looks for deviceName, deviceType, attributes and telemetry in the incoming request from the client, with rules, described in this subsection:

| **Parameter**                 | **Default value**     | **Description**                                                                                                                                                                                                                                          |
|:------------------------------|:----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| type                          | **json**              | Provides information to connector that default converter will be used for converting data from the incoming request.                                                                                                                                     | 
| deviceNameExpression          | **Device ${name}**    | JSON expression used to build the device name. In this example, the connector takes the name field from the incoming request payload and produces a device name like Device SensorA                                                                      |
| deviceNameExpressionSource    | **request**           | Defines where the connector should take values for **deviceNameExpression** from: `request` means read from the incoming request payload; `constant` means treat the expression as a fixed value (no payload parsing).                                   |
| deviceProfileExpressionSource | **request**           | Defines where the connector should take values for **deviceProfileExpression** from: `request` means read from the incoming request payload; `constant` means use the expression as a fixed value.                                                       |
| deviceProfileExpression       | **default**           | JSON expression used to resolve the device profile name. With `default`, the connector will assign the device to the default profile (or use the payload field if **deviceProfileExpressionSource** is `request` and the expression references a field). |
| attributes                    |                       | This subsection contains parameters of the incoming requests, that will be interpreted as attributes for the device.                                                                                                                                     |
| ... type                      | **string**            | Type of incoming data for a current attribute.                                                                                                                                                                                                           |
| ... key                       | **model**             | Simple JSON expression, uses for looking key in the incoming data, that will send to SENTIENT instance as attribute key.                                                                                                                              |
| ... value                     | **${sensorModel}**    | Simple JSON expression, uses for looking value in the incoming data, that will send to SENTIENT instance as value of key parameter.                                                                                                                   |
| timeseries                    |                       | This subsection contains parameters of the incoming message, that will be interpreted as telemetry for the device.                                                                                                                                       |
| ... type                      | **double**            | Type of incoming data for a current telemetry.                                                                                                                                                                                                           |
| ... key                       | **temperature**       | Simple JSON expression, uses for looking key in the incoming message, that will send to SENTIENT instance as attribute key.                                                                                                                           |
| ... value                     | **${temp}**           | Simple JSON expression, uses for looking value in the incoming message, that will send to SENTIENT instance as value of key parameter.                                                                                                                |
| ... tsField                   | **${timestampField}** | **Optional.** JSON-path expression for field that carries a datetime string. If not present, the `ts` or `timestamp` properties from incoming message will be used as timestamp for data entry.                                                          |                                                                                                                     
| ... dayfirst                  | **false**             | **Optional.** Points out that the first number is the **day** (`DD.MM.YY HH:mm:ss.SSS`).<br>• `false` → `10.11.24 10:10:10.252` → **11 Oct 2024 10:10:10.252** <br>• `true`  → `10.11.24 10:10:10.252` → **10 Nov 2024 10:10:10.252**                    |
| ... yearfirst                 | **false**             | **Optional.** Points out that the first number is the **year** (`DD.MM.YY HH:mm:ss.SSS`).<br>• `false` → follows `dayfirst` rule<br>• `true`  → `10.11.24 10:10:10.252` → **24 Nov 2010 10:10:10.252**                                                   |
| ---                           


<div class="st-callout info">


**Parameters in attributes and telemetry section may differ from those presented above, but will have the same structure.**  


</div>


In addition, you can send **multipart/form-data** requests while still using the `json` converter - no additional configuration is required. 
The REST connector merges multipart fields into a single key-value object, so you can reference them the same way as with **application/json**.

Below are two equivalent requests. The first one sends data as `application/json`:

```json
{
  "name": "SensorA",
  "sensorModel": "TX100",
  "temp": 23.5,
  "hum": 56.2,
  "timestampField": "10.11.24 14:30:00.000"
}
```
Send this request to the `/test_device` endpoint with the POST method, using Basic Auth with credentials (user / passwd):

```bash
curl -X POST http://127.0.0.1:5000/test_device \
  -H "Content-Type: application/json" \
  -u username:password \
  -d '{
        "name": "SensorA",
        "sensorModel": "TX100",
        "temp": 23.5,
        "hum": 56.2,
        "timestampField": "10.11.24 14:30:00.000"
      }'
```


You can achieve the same result using a `multipart/form-data` request, where each field is sent as a separate part.
Note: when using `curl -F`, `curl` automatically sets the `Content-Type: multipart/form-data; boundary=...` header.

```bash
curl -X POST "http://127.0.0.1:5000/test_device" \
  -u "username:password" \
  -F 'name=SensorA' \
  -F 'sensorModel=TX100' \
  -F 'temp=23.5' \
  -F 'hum=56.2' \
  -F 'timestampField=10.11.24 14:30:00.000'
```


<div class="st-callout info">


**Notes:**
1. **File uploads are not supported** for device attributes or telemetry. If a multipart request contains file parts, the gateway will ignore them and log an info message.
2. **Multipart form fields are received as strings.** Values will be converted to boolean, integer, or double according to the configured field type in the `json` converter.


</div>


This is how the mapping subsection for both examples above looks like:

```json
 {
  "endpoint": "/test_device",
  "HTTPMethods": [
    "POST"
  ],
  "security": {
    "type": "basic",
    "username": "username",
    "password": "password"
  },
  "converter": {
    "type": "json",
    "deviceInfo": {
      "deviceNameExpression": "Device ${name}",
      "deviceNameExpressionSource": "request",
      "deviceProfileExpressionSource": "request",
      "deviceProfileExpression": "default"
    },
    "attributes": [
      {
        "key": "model",
        "type": "string",
        "value": "${sensorModel}"
      }
    ],
    "timeseries": [
      {
        "key": "temperature",
        "type": "double",
        "value": "${temp}"
      },
      {
        "key": "humidity",
        "type": "double",
        "value": "${hum}",
        "tsField": "${timestampField}",
        "dayfirst": true
      }
    ]
  }
}
```


<div class="st-callout info">


**Note**: In **Mapping subsection** configuration section for `humidity` timeseries key illustrates how to use the `tsField` and
`dayfirst` options.


</div>


Also, you can combine values from HTTP request in attributes, telemetry and serverSideRpc section, for example:

```json
{
  "endpoint": "/test_device",
  "HTTPMethods": [
    "POST"
  ],
  "security": {
    "type": "basic",
    "username": "username",
    "password": "password"
  },
  "converter": {
    "type": "json",
    "deviceInfo": {
      "deviceNameExpression": "Device ${name}",
      "deviceNameExpressionSource": "request",
      "deviceProfileExpressionSource": "request",
      "deviceProfileExpression": "default"
    },
    "attributes": [
      {
        "key": "model",
        "type": "string",
        "value": "${sensorModel}"
      }
    ],
    "timeseries": [
      {
        "key": "temperature",
        "type": "double",
        "value": "${temp}"
      },
      {
        "key": "humidity",
        "type": "double",
        "value": "${hum}"
      },
      {
        "key": "combine",
        "type": "string",
        "value": "${hum}:${temp}"
      }
    ]
  }
}
```


</div>

<div class="st-tab" data-label="customRecommended if bytes or anything else will be received in the request">

A custom converter is converter written for some device:


| **Parameter**                 | **Default value**             | **Description**                                                                                                                 |
|:------------------------------|:------------------------------|---------------------------------------------------------------------------------------------------------------------------------
| type                          | **custom**                    | Provides information to connector that custom converter will be uses for converting data from request.                          |
| deviceNameExpression          | **SuperAnonDevice**           | Device name.                                                                                                                    |
| deviceNameExpressionSource    | **constant**                  | Device name source.                                                                                                             |
| deviceProfileExpressionSource | **constant**                  | Device profile source. It can be constant or request.                                                                           |
| deviceProfileExpression       | **default**                   | Device profile name. It can be constant or request.                                                                                                           |
| extension                     | **CustomRESTUplinkConverter** | Name of custom converter class.                                                                                                 |
| extension-config              |                               | Configuration, for custom converter (You can put anything, there. It will be passed to the converter object on initialization). |
| key                           | **Totaliser**                 |                                                                                                                                 |
| datatype                      | **float**                     |                                                                                                                                 |
| fromByte                      | **0**                         |                                                                                                                                 |
| toByte                        | **4**                         |                                                                                                                                 |
| byteorder                     | **big**                       |                                                                                                                                 |
| signed                        | **true**                      |                                                                                                                                 |
| multiplier                    | **1**                         |                                                                                                                                 | 
| ---                           

  

<div class="st-callout info">


  
**Custom converter usually needed if you want to collect data from some device with not regular structure in response or when the data needs some processing before sending it to the SENTIENT.**  


</div>

  

**Notate: Everything, you placed in the "converter" section will be passed to the custom converter as a configuration.**  

Mapping subsection in the configuration looks like:  

```json
"converter": {
    "type": "custom",
    "deviceInfo": {
      "deviceNameExpression": "SuperAnonDevice",
      "deviceNameExpressionSource": "constant",
      "deviceProfileExpressionSource": "constant",
      "deviceProfileExpression": "default"
    },
    "extension": "CustomRestUplinkConverter",
    "extensionConfig": {
      "key": "Totaliser",
      "datatype": "float",
      "fromByte": 0,
      "toByte": 4,
      "byteorder": "big",
      "signed": true,
      "multiplier": 1
    }
  }
```


</div>

</div>


<div class="st-callout info">


**It is also may to parse query parameters from the URL if you are using a GET request.**  


</div>


##### Response

Response in REST Connector can have 3 variants of configuration:
1. Default response (without extra configuration, return only HTTP Status Code);
2. Hardcoded response body, for this option you have to specify a new section and 2 new optional parameters as in the example below:

    | **Parameter**                 | **Default value**                                     | **Description**                                                       |
    |:-|:-|-
    | response                      |                                                       | The response that will be returned on every request to the server     |
    | ... successResponse           | **OK**                                                | Only if the response status is 200                                    |
    | ... unsuccessfulResponse      | **Error**                                             | Only if the response status different from 200                        |
    |---

3. **ADVANCED** the remote response that will return by SENTIENT.
   1. To configure that variant you have to specify a new section in the config file as in the example below:

       | **Parameter**                 | **Default value**                                     | **Description**                                                       |
       |:-|:-|-
       | response                      |                                                       | Boolean value for on/off returning a response                         |
       | ... responseExpected          | **true**                                              | Timeout for request.                                                  |
       | ... timeout                   | **120**                                               | Only if the response status different from 200                        |
       | ... responseAttribute         | **result**                                            | Shared attribute name which response will be return                   |
       |---

   2. Configure RuleChain in SENTIENT:
      ![image](/images/gateway/custom-response-rule-chain-config.webp)
      Finally, you have to configure rule node:
      1. Yellow Rule Node
          ![image](/images/gateway/custom-response-yellow-rule-node.webp)
      2. Blue Rule Node
          ![image](/images/gateway/custom-response-blue-rule-node.webp)

### Attribute request section
Configuration in this section are optional.

In order to request client-side or shared device attributes to SENTIENT server node, Gateway allows sending 
attribute requests.

| **Parameter**                 | **Default value**                                     | **Description**                                                       |
|:-|:-|-
| endpoint                      | **/sharedAttributes**                                 | Url address of the endpoint.                                          |
| type                          | **shared**                                            | The type of requested attribute can be “shared” or “client”.          |
| HTTPMethods                   | **[”POST”]**                                          | Allowed methods                                                       |
| security                      |                                                       | Security for request:                                                 |
| ... type                      | **basic**                                             | Security type for request to the server (**basic** or **anonymous**). |
| ... username                  | **user**                                              | Username for basic type of the security.                              |
| ... password                  | **passwd**                                            | Password for basic type of the security.                              |
| timeout                       | **10.0**                                              | Timeout for request.                                                  |
| deviceNameExpression          | **${deviceName}**                                     | JSON-path expression, for looking the device name.                    |
| attributeNameExpression       | **${attribute}**                                      | JSON-path expression, for looking the attribute name.                 |
|---

The **attributeRequests** section will look like:
```json
"attributeRequests": [
  {
    "endpoint": "/sharedAttributes",
    "type": "shared",
    "HTTPMethods": [
      "POST"
    ],
    "security": {
      "type": "anonymous"
    },
    "timeout": 10.0,
    "deviceNameExpression": "${deviceName}",
    "attributeNameExpression": "${attribute}"
  }
]
```


Also, you can request multiple attributes at once. Simply add one more JSON-path to 
attributeNameExpression parameter. For example, we want to request two shared attributes in one request, our config 
will look like:
```json
"attributeRequests": [
  {
    "endpoint": "/sharedAttributes",
    "type": "shared",
    "HTTPMethods": [
      "POST"
    ],
    "security": {
      "type": "anonymous"
    },
    "timeout": 10.0,
    "deviceNameExpression": "${deviceName}",
    "attributeNameExpression": "${pduAttribute}, ${versionAttribute}"
  }
]
```


### Attribute update section

Configuration in this section are optional.  
SENTIENT allows to provision device attributes and fetch some of them from the device application.
You can treat this as a remote configuration for devices. Your devices are able to request shared attributes from SENTIENT.
See [user guide](/docs/user-guide/attributes/) for more details.

The "**attributeUpdates**" configuration allows configuring the format of the corresponding attribute update messages. 

| **Parameter**                 | **Default value**                                     | **Description**                                                                                    |
|:-|:-|-
| httpMethod                    | **POST**                                              | HTTP method for request (**GET**, **POST** etc.).                                                  |
| SSLVerify                     | **false**                                             | Verify or no SSL certificate on the server if available.                                           |
| httpHeaders                   | **{ "CONTENT-TYPE": "application/json" }**            | Object contains additional HTTP headers for request.                                               |
| security                      |                                                       | Security for request:                                                                              |
|   type                        | **basic**                                             | Security type for request to the server (**basic** or **anonymous**).                              |
|   username                    | **user**                                              | Username for basic type of the security.                                                           |
|   password                    | **passwd**                                            | Password for basic type of the security.                                                           |   
| timeout                       | **0.5**                                               | Timeout for request.                                                                               |
| tries                         | **3**                                                 | Count of tries to send data                                                                        |
| allowRedirects                | **true**                                              | Allow request redirection.                                                                         |
| deviceNameFilter              | **.\*REST$**                                          | Regular expression device name filter, uses to determine, which function to execute.               |
| attributeFilter               | **data**                                              | Regular expression attribute name filter, uses to determine, which function to execute.            |
| requestUrlExpression          | **sensor/${deviceName}/${attributeKey}**              | JSON-path expression uses for creating url address to send a message.                              |
| valueExpression               | **{\\"${attributeKey}\\":\\"${attributeValue}\\"}**   | JSON-path expression uses for creating the message data that will send to url.                     |
|---

The **attributeUpdates** section will look like:

```json
  "attributeUpdates": [
      {
        "HTTPMethod": "POST",
        "SSLVerify": false,
        "httpHeaders": {
          "CONTENT-TYPE": "application/json"
        },
        "security": {
          "type": "basic",
          "username": "user",
          "password": "passwd"
        },
        "timeout": 0.5,
        "tries": 3,
        "allowRedirects": true,
        "deviceNameFilter": ".*REST$",
        "attributeFilter": "data",
        "requestUrlExpression": "sensor/${deviceName}/${attributeKey}",
        "valueExpression": "{\"${attributeKey}\":\"${attributeValue}\"}"
      }
  ],
```


### Server side RPC section


SENTIENT allows sending [RPC commands](/docs/user-guide/rpc/) to the device that is connected to SENTIENT directly or via Gateway.
 
Configuration, provided in this section uses for sending RPC requests from SENTIENT to device.

| **Parameter**                 | **Default value**                                                 | **Description**                                                                       |
|:-|:-|-
| deviceNameFilter              | **.\***                                                           | Regular expression device name filter, uses to determine, which function to execute.  |
| methodFilter                  | **echo**                                                          | Regular expression method name filter, uses to determine, which function to execute.  |
| requestUrlExpression          | **http://127.0.0.1:5001/${deviceName}**                           | JSON-path expression, uses to create url address to send RPC request.                 |
| responseTimeout               | **1**                                                             | Timeout for request.                                                                  |
| httpMethod                    | **GET**                                                           | HTTP method for request (**GET**, **POST** etc.).                                     |
| valueExpression               | **${params}**                                                     | JSON-path expression, uses for creating data for sending.                             |
| timeout                       | **0.5**                                                           | Timeout for request.                                                                  |
| tries                         | **3**                                                             | Count of tries to send data                                                           |
| httpHeaders                   | **{ "CONTENT-TYPE": "application/json" }**                        | Object contains additional HTTP headers for request.                                  |
| security                      |                                                                   | Security for request:                                                                 |
|   type                        | **anonymous**                                                     | Security type for request to the server (**basic** or **anonymous**).                 |
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
      "requestUrlExpression": "http://127.0.0.1:5001/${deviceName}",
      "responseTimeout": 1,
      "HTTPMethod": "GET",
      "valueExpression": "${params}",
      "timeout": 0.5,
      "tries": 3,
      "httpHeaders": {
        "Content-Type": "application/json"
      },
      "security": {
        "type": "anonymous"
      }
    },
    {
      "deviceNameFilter": ".*",
      "methodFilter": "no-reply",
      "requestUrlExpression": "sensor/${deviceName}/request/${methodName}/${requestId}",
      "HTTPMethod": "POST",
      "valueExpression": "${params.hum}",
      "httpHeaders": {
        "Content-Type": "application/json"
      }
    }
  ]
```


Also, every telemetry and attribute parameter has built-in GET and SET RPC methods out of the box, so you don’t need to configure
it manually. To use them, make sure you set all required parameters (in the case of REST Connector, these are the following:
**requestUrlExpression**, **responseTimeout**, **HTTPMethod**, **valueExpression**). 
See [the guide](/docs/iot-gateway/guides/how-to-use-get-set-rpc-methods).

## Next steps

Explore guides related to main SENTIENT features:

 - [Data Visualization](/docs/user-guide/dashboards/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine-2-0/overview/) - how to use rule engine to analyze data from devices.
