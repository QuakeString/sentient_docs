+++
title = "OCPP Connector Configuration"
description = "OCPP protocol support for SENTIENT IoT Gateway"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/config/ocpp.md"
+++
This guide will help you get familiar with OCPP Connector configuration for SENTIENT IoT Gateway.
Use [general configuration](/docs/iot-gateway/configuration/) to enable this Connector.
The purpose of this connector is to communicate between Charge Point and Central System using OCPP protocol.

We will describe the connector configuration file below.

## Connector configuration: ocpp.json
Connector configuration is a JSON file that contains information about how to connect to Charge Points, process
the data, and other service features. Let’s review the format of the configuration file using the example below.


<b>Example of OCPP Connector config file.</b>


<table class="includecode"><tr><td>
```conf
{
  "centralSystem": {
    "name": "Central System",
    "host": "127.0.0.1",
    "port": 9000,
    "connection": {
      "type": "insecure"
    },
    "security": [
      {
        "type": "token",
        "tokens": [
          "Bearer ACCESS_TOKEN"
        ]
      },
      {
        "type": "basic",
        "credentials": [
          {
            "username": "admin",
            "password": "admin"
          }
        ]
      }
    ]
  },
  "chargePoints": [
    {
      "idRegexpPattern": "bidon/hello/CP_1",
      "deviceNameExpression": "${Vendor} ${Model}",
      "deviceTypeExpression": "default",
      "attributes": [
        {
          "messageTypeFilter": "MeterValues,",
          "key": "temp1",
          "value": "${meter_value[:].sampled_value[:].value}"
        },
        {
          "messageTypeFilter": "MeterValues,",
          "key": "vendorId",
          "value": "${connector_id}"
        }
      ],
      "timeseries": [
        {
          "messageTypeFilter": "DataTransfer,",
          "key": "temp",
          "value": "${data.temp}"
        }
      ],
      "attributeUpdates": [
        {
          "attributeOnSENTIENT": "shared",
          "valueExpression": "{\"${attributeKey}\":\"${attributeValue}\"}"
        }
      ],
      "serverSideRpc": [
        {
          "methodRPC": "rpc1",
          "withResponse": true,
          "valueExpression": "${params}"
        }
      ]
    }
  ]
}
```


</td></tr></table>


### Section "centralSystem"

This configuration section is used to configure Gateway as a Central System.

| **Parameter** | **Default value**  | **Description**                        |
|:--------------|:-------------------|----------------------------------------|
| name          | **Central System** | Central System name.                   |
| host          | **127.0.0.1**      | Central System hostname or ip address. |
| port          | **9000**           | Central System port.                   |
| ---           |                    |                                        |

#### Connection subsection

This configuration subsection is used for configuring connection type between Central System and Charge Point.
You can choose the next connection type:


<div class="st-tabs">

<div class="st-tab" data-label="InsecureNo security">

Insecure connection type is the simplest option. It is useful for testing purpose but not recommended in production
solution. 

|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| type               | **insecure**                      | Type of connection.      |
|---

Connection subsection in configuration file will look like this: 

```yaml
    "connection": {
      "type": "insecure"
    }
```


</div>

<div class="st-tab" data-label="TLSRecommended">

The table below describes the parameters to configure TLS connection.

|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| key                      | **/etc/sentient-gateway/privateKey.pem**  | Path to private key file.                |
| cert                     | **/etc/sentient-gateway/certificate.pem** | Path to certificate file.                |
| password                 | **YOUR_PASSWORD**                            | **OPTIONAL** Password for TLS connection |
|---    

Connection subsection in configuration file will look like this: 

```yaml
    "connection": {
      "type": "tls",
      "key": "/etc/sentient-gateway/privateKey.pem",
      "cert": "/etc/sentient-gateway/certificate.pem"
    }
```


</div>

</div>

 

#### Security subsection

Security subsection provides configuration for Charge Point authorization at Central System.
You can choose the desired security type:


<div class="st-tabs">

<div class="st-tab" data-label="AnonymousNo security">

Anonymous connection type is the simplest option. It is useful for testing purposes but not recommended in a production
solution.

Security subsection in configuration file will look like this: 

```yaml
    "security": []
```


</div>

<div class="st-tab" data-label="BasicRecommended">

One type of security configuration is basic. 
For authorization, a combination of username/password provided in this section of the config will be used.


|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| type               | **basic**                      | Type of authorization.       |
| credentials        |                                | List of allowed credentials. |
| ... username       | **username**                   | Username for authorization.  |
| ... password       | **password**                   | Password for authorization.  |
|---

Security subsection in configuration file will look like this: 
```yaml
    "security": [
      "type": "basic",
      "credentials": [
        {
          "username": "admin",
          "password": "admin"
        }
      ]
    ]
```


</div>

<div class="st-tab" data-label="TokenRecommended">

One type of security configuration is token.
For authorization, token provided in this section of the config will be used.


|**Parameter**|**Default value**|**Description**|
|:-|:-|-
| type               | **token**                      | Type of authorization.      |
| tokens             | **["Bearer ACCESS_TOKEN"]**    | List of allowed tokens.     |
|---

Security subsection in configuration file will look like this: 

```yaml
    "security": [
      "type": "token",
      "tokens": [
        "Bearer ACCESS_TOKEN"
      ]
    ]
```


</div>

</div>


**Note** You can combine _basic_ and _token_ security types. Security subsection in configuration file will look like this:

```json
    "security": [
      {
        "type": "token",
        "tokens": [
          "Bearer ACCESS_TOKEN"
        ]
      },
      {
        "type": "basic",
        "credentials": [
          {
            "username": "admin",
            "password": "admin"
          }
        ]
      }
    ]
```

### Section "chargePoints"

This subsection contains general settings for the Charge Points and subsections for processing data.

| **Parameter**        | **Default value**      | **Description**                                                                                                                                  |
|:---------------------|:-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| idRegexpPattern      | **charge_points/CP_1** | Regular expression, is used for looking the Charge Point for a current device.                                                                   |
| deviceNameExpression | **${Vendor} ${Model}** | Simple JSON expression, is used for looking up device name in the incoming message (parameter “Vendor + Model” will be used as the device name). |
| deviceTypeExpression | **${Model}**           | Simple JSON expression, is used for looking up device type in the incoming message (parameter “Model” will be used as the device type).          |
| attributes           |                        | Array of objects for processing device attributes.                                                                                               |
| timeseries           |                        | Array of objects for processing device telemetry.                                                                                                |
| attributeUpdates     |                        | Array of objects for processing attributeUpdate requests from SENTIENT.                                                                       |
| serverSideRpc        |                        | Array of objects for processing RPC requests from SENTIENT.                                                                                   |
| ---                  |                        |                                                                                                                                                  |

This part of configuration will look like this:

```json
  "chargePoints": [
    {
      "idRegexpPattern": "charge_points/CP_1",
      "deviceNameExpression": "${Vendor} ${Model}",
      "deviceTypeExpression": "${Model}",
      "attributes": [
        ...
      ],
      "timeseries": [
        ...
      ],
      "attributeUpdates": [
        ...
      ],
      "serverSideRpc": [
        ...
      ]
    }
  ]
```

#### Subsection attributes

This subsection contains general settings for processing data interpreted as attributes.

| **Parameter**         | **Default value**                            | **Description**                                                                                                                                                  |
|:----------------------|:---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attributes            |                                              | This subsection contains parameters of the incoming message, to be interpreted as attributes for the device.                                                     |
| ... messageTypeFilter | **MeterValues,**                             | List of allowed message types divided by comma.                                                                                                                  |
| ... key               | **temp**                                     | Attribute name, to be sent to SENTIENT instance.                                                                                                              |
| ... value             | **${meter_value[:].sampled_value[:].value}** | Simple JSON expression, is used for looking up value in the incoming message, which will then be sent to SENTIENT instance as the value of the key parameter. |
| ---                   |                                              |                                                                                                                                                                  |

This subsection in configuration file looks like:

```json
      "attributes": [
        {
          "messageTypeFilter": "MeterValues,",
          "key": "temp",
          "value": "${meter_value[:].sampled_value[:].value}"
        },
        {
          "messageTypeFilter": "MeterValues,",
          "key": "vendorId",
          "value": "${connector_id}"
        }
      ]
```

#### Subsection time series

This subsection contains general settings for processing data interpreted as time series.

| **Parameter**         | **Default value**                            | **Description**                                                                                                                                                  |
|:----------------------|:---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| timeseries            |                                              | This subsection contains parameters of the incoming message, to be interpreted as telemetry for the device.                                                      |
| ... messageTypeFilter | **MeterValues,**                             | List of allowed message types divided by comma.                                                                                                                  |
| ... key               | **temp**                                     | Telemetry name, to be sent to SENTIENT instance.                                                                                                              |
| ... value             | **${meter_value[:].sampled_value[:].value}** | Simple JSON expression, is used for looking up value in the incoming message, which will then be sent to SENTIENT instance as the value of the key parameter. |
| ---                   |                                              |                                                                                                                                                                  |

This subsection in configuration file looks like:

```json
      "timeseries": [
        {
          "messageTypeFilter": "DataTransfer,",
          "key": "temp",
          "value": "${data.temp}"
        }
      ]
```

#### Attribute updates subsection

This configuration section is optional. SENTIENT allows the provisioning of device attributes and fetches some of them from 
the device application. You can treat this as a remote configuration for devices, enabling them to request 
shared attributes from SENTIENT. See [user guide](/docs/reference/mqtt-api/#attributes-api) for more details.

The “attributeUpdates” configuration allows you to configure the format of the corresponding attribute data that will be 
sent to the Charge Point.

| **Parameter**          | **Default value**                               | **Description**                                                                               |
|:-----------------------|:------------------------------------------------|-----------------------------------------------------------------------------------------------|
| attributeOnSENTIENT | **sharedName**                                  | Shared attribute name.                                                                        |
| valueExpression        | **{\"${attributeKey}\":\"${attributeValue}\"}** | JSON-path expression is used for creating the message data that will be sent to Charge Point. |
| ---                    |                                                 |                                                                                               |

This section in configuration file looks like: 
```json
"attributeUpdates": [
  {
    "attributeOnSENTIENT": "shared",
    "valueExpression": "{\"${attributeKey}\":\"${attributeValue}\"}"
  }
]
```

#### Server side RPC subsection

SENTIENT allows sending RPC commands to the device connected to SENTIENT directly or via Gateway.

Configuration, provided in this section is used for sending RPC requests from SENTIENT to Charge Point.

| **Parameter**   | **Default value** | **Description**                                                                         |
|:----------------|:------------------|-----------------------------------------------------------------------------------------|
| methodRPC       | **rpcMethod1**    | RPC method name.                                                                        |
| withResponse    | **true**          | Boolean value that determines whether to send response back to SENTIENT.             |
| valueExpression | **${params}**     | JSON-path expression uses for creating the message data that will send to Charge Point. |
| ---             |                   |                                                                                         |

This subsection in configuration file looks like:

```json
"serverSideRpc": [
  {
    "methodRPC": "rpc1",
    "withResponse": true,
    "valueExpression": "${params}"
  }
]
```

## Next steps

Explore guides related to main SENTIENT features:

 - [Data Visualization](/docs/user-guide/visualization/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine/) - how to use rule engine to analyze data from devices.
