+++
title = "Working with telemetry data"
description = "IoT device time-series data collection using various IoT protocols and SENTIENT telemetry feature"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/telemetry.md"
+++
SENTIENT provides a rich set of features related to time-series data:

 - **Collect** data from devices using various [protocols and integrations](/docs/getting-started-guides/connectivity/);
 - **Store** time series data in SQL (PostgreSQL) or NoSQL (Cassandra or Timescale) databases;
 - **Query** the latest time series data values or all data within the specified time range with flexible aggregation;
 - **Subscribe** to data updates using [WebSockets](#websocket-api) for visualization or real-time analytics;
 - **Visualize** time series data using configurable and highly customizable widgets and [dashboards](/docs/user-guide/dashboards/);
 - **Filter and analyze** data using flexible [Rule Engine](/docs/user-guide/rule-engine-2-0/re-getting-started/);
 - **Generate [alarms](/docs/user-guide/alarms/)** based on collected data;
 - **Forward** data to external systems using [External Rule Nodes](/docs/user-guide/rule-engine-2-0/nodes/external/) (e.g. Kafka or RabbitMQ Rule Nodes).

This guide provides an overview of the features listed above, and some useful links to get more details.

## Data points

SENTIENT internally treats time-series data as timestamped key-value pairs. We call single timestamped key-value pair a **data point**. 
Flexibility and simplicity of the key-value format allow easy and seamless integration with almost any IoT device on the market. 
Key is always a string and is basically a data point key name, while the value can be either string, boolean, double, integer or JSON.


<div class="st-callout info">


Examples below use **internal** data format. The device itself may upload data using **various protocols and data formats**. 
See [Time-series data upload API](/docs/user-guide/telemetry/#time-series-data-upload-api) for more details.


</div>


The following JSON contains 5 data points: temperature (double), humidity (integer), hvacEnabled (boolean), hvacState (string) and configuration (JSON):  

```json
{
 "temperature": 42.2, 
 "humidity": 70,
 "hvacEnabled": true,
 "hvacState": "IDLE",
 "configuration": {
    "someNumber": 42,
    "someArray": [1,2,3],
    "someNestedObject": {"key": "value"}
 }
}
```


You may notice that the JSON listed above does not have a timestamp information. In such case, SENTIENT uses current server timestamp. 
However, you may include timestamp information into the message. See example below:

```json
{
  "ts": 1527863043000,
  "values": {
    "temperature": 42.2,
    "humidity": 70
  }
}
```


## Time-series data upload API

You may use built-in transport protocol implementations:

- [MQTT API reference](/docs/reference/mqtt-api/#telemetry-upload-api)
- [CoAP API reference](/docs/reference/coap-api/#telemetry-upload-api)
- [HTTP API reference](/docs/reference/http-api/#telemetry-upload-api)
- [LwM2M API reference](/docs/reference/lwm2m-api/#telemetry-upload-api)

Most of the protocols above support JSON, Protobuf or own data format. For other protocols, please review ["How to connect your device?"](/docs/getting-started-guides/connectivity/) guide.

## Data visualization

We assume you have already pushed time-series data to SENTIENT. Now you may use it in your dashboards. 
We recommend [dashboards overview](/docs/user-guide/dashboards/) to get started.
Once you are familiar how to create dashboards and configure data sources,
you may use widgets to visualize either latest values or real-time changes and historical values.
Good examples of widgets that visualize latest values are [digital](/docs/user-guide/ui/widget-library/#digital-gauges) and [analog](/docs/user-guide/ui/widget-library/#analog-gauges) gauges, or [cards](/docs/user-guide/ui/widget-library/#cards).
[Charts](/docs/user-guide/ui/widget-library/#charts) are used to visualize historical and real-time values and [maps](/docs/user-guide/ui/widget-library/#maps-widgets) to visualize movement of devices and assets.

You may also use [input widgets](/docs/user-guide/ui/widget-library/#input-widgets) to allow dashboard users to input new time-series values using the dashboards.

## Data storage


In SENTIENT, timeseries data can be stored using either a SQL database (PostgreSQL) or a hybrid configuration in which PostgreSQL is paired with Cassandra or TimescaleDB.
Using SQL storage is recommended for small environments with less than 5000 [data points](#data-points) per second.
Storing data in Cassandra makes sense when you have either high throughput or high availability requirements for your solution.

See [SQL vs Hybrid](/docs/reference/#sql-vs-nosql-vs-hybrid-database-approach) for more information.


## Data retention


The data retention policy and mechanism in SENTIENT depends on the selected [data storage](#data-storage). Retention can be configured in several ways:

#### System-wide configuration
Defined in the SENTIENT configuration file and applied across the platform.

- **Cassandra**  
  You can [configure](/docs/user-guide/install/config/) the default TTL using the `TS_KV_TTL` environment variable.  

- **PostgreSQL / TimescaleDB**  
  These databases do not provide built-in mechanism for TTL.  
  Instead, you can [configure](/docs/user-guide/install/config/) a periodic data cleanup routine using the `SQL_TTL_*` environment variables.
  

#### Tenant profile configuration
Tenant profiles include a **TTL settings** section.  
Here, a System Administrator can configure retention periods for multiple data types, such as:

- Default Storage TTL Days. **(Works only when Cassandra is used as the timeseries database)**
- Alarm TTL days.
- Queue stats TTL days.
- Rule Engine exceptions TTL days.
- RPC requests TTL days.

See [Tenant profiles](/docs/user-guide/tenant-profiles/) for details.


#### Tenant attribute
You can set a `TTL` attribute (in seconds) for the Tenant entity.
This value applies to every entity within Tenant as a time-to-live for their timeseries data.
**Works only with PSQL or TimescaleDB.** 


#### Rule node configuration
The **Save Timeseries** rule node allows you to define a TTL for telemetry values saved by that rule node. 
You can also define data retention by including a `TTL` property in the message metadata.
**These work only with Cassandra since it support per-row time-to-live TTL.** 

See [Save Timeseries rule node](/docs/user-guide/rule-engine-2-0/nodes/action/save-timeseries/) for more information.


<div class="st-callout info">


**Note:** Retention settings follow a priority order (highest to lowest):  
1. Message metadata `TTL` property   
2. Rule node configuration   
3. Tenant Profile configuration (Cassandra) or Tenant Attribute (PostgreSQL/TimescaleDB)
4. System-wide configuration


</div>


## Data durability

The device that sends message with time-series data to SENTIENT will receive confirmation 
once the message is successfully stored into the Rule Engine [Queue](/docs/user-guide/rule-engine-2-5/queues/) 
that is configured for particular device [profile](/docs/user-guide/device-profiles/#queue-name).

As a tenant administrator, you may configure [processing strategy](/docs/user-guide/rule-engine-2-5/queues/#queue-processing-strategy) for the queue.
You may configure the queue either to reprocess or ignore the failures of the message processing. 
This allows granular control on the level of durability for the time-series data and all other messages processed by the rule engine. 

## Rule engine

The [Rule Engine](/docs/user-guide/rule-engine-2-0/re-getting-started/) is responsible for processing all sorts of incoming data and event.
You may find most popular scenarios of using attributes within rule engine below:

**Generate alarms based on the logical expressions against time-series values**

Use [alarm rules](/docs/user-guide/device-profiles/#alarm-rules) to configure most common alarm conditions via UI
or use [filter nodes](/docs/user-guide/rule-engine-2-0/nodes/filter/) to configure more specific use cases via custom JS functions.

**Modify incoming time-series data before they are stored in the database**

Use [message type switch](/docs/user-guide/rule-engine-2-0/nodes/filter/message-type-switch/) rule node to filter messages that contain "Post telemetry" request.
Then, use [transformation rule nodes](/docs/user-guide/rule-engine-2-0/nodes/transformation/) to modify a particular message.

**Calculate delta between previous and current time-series value**

Use [calculate delta](/docs/user-guide/rule-engine-2-0/nodes/enrichment/calculate-delta/) rule node to calculate power, water and other consumption based on smart-meter readings.

**Fetch previous time-series values to analyze incoming telemetry from device**

Use [originator telemetry](/docs/user-guide/rule-engine-2-0/nodes/enrichment/originator-telemetry/) rule node to enrich incoming time-series data message with previous time-series data of the device.

**Fetch attribute values to analyze incoming telemetry from device**

Use [enrichment](/docs/user-guide/rule-engine-2-0/nodes/enrichment/) rule nodes to enrich incoming telemetry message with attributes of the device, related asset, customer or tenant.
This is extremely powerful technique that allows to modify processing logic and parameters based on settings stored in the attributes.

**Use analytics rule nodes to aggregate data for related assets**

Use [analytics](/docs/user-guide/rule-engine-2-0/nodes/analytics/) rule nodes to aggregate data from multiple devices or assets.

Useful to calculate total water consumption for the building/district based on data from multiple water meters.     

## Data Query REST API

SENTIENT provides following REST API to fetch entity data:


<div class="st-callout info">


**NOTE:** The API is available via Swagger UI. Please review the general [REST API](/docs/reference/rest-api/) documentation for more details.
The API is backward compatible with TB v1.0+ and this is the main reason why API call URLs contain "plugin".


</div>


### Get time-series data keys for specific entity

You can fetch list of all time-series *data keys* for particular *entity type* and *entity id* using GET request to the following URL  
 
```bash
http(s)://host:port/api/plugins/telemetry/{entityType}/{entityId}/keys/timeseries
```


<div class="st-tabs">

<div class="st-tab" data-label="get-telemetry-keys.sh">


```bash
curl -v -X GET http://localhost:8080/api/plugins/telemetry/DEVICE/ac8e6020-ae99-11e6-b9bd-2b15845ada4e/keys/timeseries \
--header "Content-Type:application/json" \
--header "X-Authorization: $JWT_TOKEN"
```


</div>

<div class="st-tab" data-label="get-telemetry-keys-result.json">


```json
["gas","temperature"]
```


</div>

</div>


Supported entity types are: TENANT, CUSTOMER, USER, DASHBOARD, ASSET, DEVICE, ALARM, ENTITY_VIEW

### Get latest time-series data values for specific entity

You can fetch list of latest values for particular *entity type* and *entity id* using GET request to the following URL  
 
```bash
http(s)://host:port/api/plugins/telemetry/{entityType}/{entityId}/values/timeseries?keys=key1,key2,key3
```


<div class="st-tabs">

<div class="st-tab" data-label="get-latest-telemetry-values.sh">


```bash
curl -v -X GET http://localhost:8080/api/plugins/telemetry/DEVICE/ac8e6020-ae99-11e6-b9bd-2b15845ada4e/values/timeseries?keys=gas,temperature \
--header "Content-Type:application/json" \
--header "X-Authorization: $JWT_TOKEN"
```


</div>

<div class="st-tab" data-label="get-latest-telemetry-values-result.json">


```json
{
  "gas": [
    {
      "ts": 1479735870786,
      "value": "1"
    }
  ],
  "temperature": [
    {
      "ts": 1479735870786,
      "value": "3"
    }
  ]
}
```


</div>

</div>


Supported entity types are: TENANT, CUSTOMER, USER, DASHBOARD, ASSET, DEVICE, ALARM, ENTITY_VIEW

### Get historical time-series data values for specific entity

You can also fetch list of historical values for particular *entity type* and *entity id* using GET request to the following URL  
 
```bash
http(s)://host:port/api/plugins/telemetry/{entityType}/{entityId}/values/timeseries?keys=key1,key2,key3&startTs=1479735870785&endTs=1479735871858&interval=60000&limit=100&agg=AVG
```


The supported parameters are described below:

 - **keys** - comma-separated list of telemetry keys to fetch.
 - **startTs** - Unix timestamp that identifies the start of the interval in milliseconds.
 - **endTs** - Unix timestamp that identifies the end of the interval in milliseconds.
 - **interval** - the aggregation interval, in milliseconds.
 - **agg** - the aggregation function. One of MIN, MAX, AVG, SUM, COUNT, NONE.
 - **limit** - the max amount of data points to return or intervals to process.

SENTIENT will use *startTs*, *endTs*, and *interval* to identify aggregation partitions or sub-queries and execute asynchronous queries to DB that leverage built-in aggregation functions.


<div class="st-tabs">

<div class="st-tab" data-label="get-telemetry-values.sh">


```bash
curl -v -X GET "http://localhost:8080/api/plugins/telemetry/DEVICE/ac8e6020-ae99-11e6-b9bd-2b15845ada4e/values/timeseries?keys=gas,temperature&startTs=1479735870785&endTs=1479735871858&interval=60000&limit=100&agg=AVG" \
--header "Content-Type:application/json" \
--header "X-Authorization: $JWT_TOKEN"
```


</div>

<div class="st-tab" data-label="get-telemetry-values-result.json">


```json
{
  "gas": [
    {
      "ts": 1479735870786,
      "value": "1"
    },
    {
      "ts": 1479735871857,
      "value": "2"
    }
  ],
  "temperature": [
    {
      "ts": 1479735870786,
      "value": "3"
    },
    {
      "ts": 1479735871857,
      "value": "4"
    }
  ]
}
```


</div>

</div>


Supported entity types are: TENANT, CUSTOMER, USER, DASHBOARD, ASSET, DEVICE, ALARM, ENTITY_VIEW

## WebSocket API

WebSockets are actively used by Sentient Web UI. WebSocket API duplicates REST API functionality and provides the ability to subscribe to device data changes.
You can open a WebSocket connection to a telemetry service using the following URL

```bash
ws(s)://host:port/api/ws
```


Once opened, you need to authenticate the session within 10 seconds with auth command:
```json
{
  "authCmd": {
    "cmdId": 0,
    "token": "$JWT_TOKEN"
  }
}
```


Then you can send [subscription commands](https://github.com/sentient/sentient/blob/release-3.6/application/src/main/java/org/sentient/server/service/ws/WsCommandsWrapper.java) 
and receive 
[subscription updates](https://github.com/sentient/sentient/blob/release-3.6/application/src/main/java/org/sentient/server/service/ws/telemetry/sub/TelemetrySubscriptionUpdate.java):

where 

 - **cmdId** - unique command id (within corresponding WebSocket connection)
 - **entityType** - unique entity type. Supported entity types are: TENANT, CUSTOMER, USER, DASHBOARD, ASSET, DEVICE, ALARM
 - **entityId** - unique entity identifier
 - **keys** - a comma-separated list of data keys
 - **timeWindow** - fetch interval for time series subscriptions, in milliseconds. Data will be fetch within following interval **[now()-timeWindow, now()]**
 - **startTs** - start time of fetch interval for historical data query, in milliseconds.
 - **endTs** - end time of fetch interval for historical data query, in milliseconds.
 
### Example 

Replace the following variables with your actual values:
- <code>$YOUR_JWT_TOKEN</code> - the JWT token obtained using the [REST API authentication endpoint](/docs/reference/rest-api/#rest-api-auth).
- <code>$YOUR_DEVICE_ID</code> - the unique identifier of your device.
- <code>$SENTIENT_HOST_PORT</code> — the hostname and port (e.g. `127.0.0.1:8080`) where your SENTIENT instance is running.

 
  


<div class="st-tabs">

<div class="st-tab" data-label="web-socket.html">


```html
<!DOCTYPE HTML>
<html>
<head>

    <script type="text/javascript">
        function WebSocketAPIExample() {
            var token = "$YOUR_JWT_TOKEN";
            var entityId = "$YOUR_DEVICE_ID";
            var webSocket = new WebSocket("ws://$SENTIENT_HOST_PORT/api/ws");

            if (entityId === "$YOUR_DEVICE_ID") {
                alert("Invalid device id!");
                webSocket.close();
            }

            if (token === "$YOUR_JWT_TOKEN") {
                alert("Invalid JWT token!");
                webSocket.close();
            }

            webSocket.onopen = function () {
                var object = {
                    authCmd: {
                        cmdId: 0,
                        token: token
                    },
                    cmds: [
                        {
                            entityType: "DEVICE",
                            entityId: entityId,
                            scope: "LATEST_TELEMETRY",
                            cmdId: 10,
                            type: "TIMESERIES"
                        }
                    ]
                };
                var data = JSON.stringify(object);
                webSocket.send(data);
                alert("Message is sent: " + data);
            };

            webSocket.onmessage = function (event) {
                var received_msg = event.data;
                alert("Message is received: " + received_msg);
            };

            webSocket.onclose = function (event) {
                alert("Connection is closed!");
            };
        }
    </script>

</head>
<body>

<div id="sse">
    <a href="javascript:WebSocketAPIExample()">Run WebSocket</a>
</div>

</body>
</html>
```


</div>

</div>
