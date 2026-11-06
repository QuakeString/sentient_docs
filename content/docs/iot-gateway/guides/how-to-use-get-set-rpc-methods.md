+++
title = "How to use built-in GET/SET RPC methods"
description = "How to use built-in GET/SET RPC methods"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/guides/how-to-use-get-set-rpc-methods.md"
+++
Built-in GET/SET RPC methods provide a way to get and set the values of telemetry and attribute parameters values without 
additional configuration. The following connectors support built-in GET/SET RPC methods:


<div class="st-tabs">

<div class="st-tab" data-label="OPC-UA">

Every telemetry and attribute parameter has **GET** and **SET** RPC methods out of the box, so you don't need to configure
them manually.
For example, if you have a telemetry parameter:
```json
"timeseries": [
  {
    "key": "temperature",
    "path": "${ns=3;i=1001}"
  }
]
```

To get the current value of temperature telemetry, run the query:

```bash
get ns=3;i=1001;
```


Response:
```json
{"result":  25.34}
```

To set temperature telemetry value, run the query:

```bash
set ns=3;i=1001; 23
```


![image](/images/gateway/gateway-opc-ua-rpc-1.webp)

<br>
To set new value (T3000) for **"model"** attribute, run this query:

```bash
set ns=3;i=1008; T3000;
```


Response:
```json
{"success":"true","code": 200}
```


![image](/images/gateway/gateway-opc-ua-rpc-2.webp)


</div>

<div class="st-tab" data-label="Modbus">

### GET method

With the GET method you can read the values of Modbus slave registers.

```bash
get type=<type>;functionCode=<functionCode>;objectsCount=<objectsCount>;address=<address>;
```

Where:
- `<type>` - the type of the value to read;
- `<functionCode>` - the Modbus function code;
- `<objectsCount>` - the number of objects to read;
- `<address>` - the address of the register to read.

For example, in our case, we know that we can read 16-bit integer values from the Modbus slave with the address 1, 
which contains the outdoor temperature. To read the value of the register with the address 1, run this query:

```bash
get type=16int;functionCode=3;objectsCount=1;address=1;
```

**Response:**

```json
{"result":{"value":13}}
```


![image](/images/gateway/get-set-connector-rpc/modbus-get-set-rpc-1.webp)


### SET method

With the SET method you can write values to Modbus slave registers.

```bash
set type=<type>;functionCode=<functionCode>;objectsCount=<objectsCount>;address=<address>;value=<value>;
```

Where:
- `<type>` - the type of the value to write;
- `<functionCode>` - the Modbus function code;
- `<objectsCount>` - the number of objects to write;
- `<address>` - the address of the register to write;
- `<value>` - the value to write.

For example, in our case, we know that we can write 16-bit integer values to the Modbus slave with the address 2 
that contains room light level. To write the value of the register with the address 2, run the following query:

```bash
set type=16int;functionCode=6;objectsCount=1;address=2;value=80;
```

**Response:**

```json
{"result":{"value":"80"}}
```


![image](/images/gateway/get-set-connector-rpc/modbus-get-set-rpc-2.webp)


Let's check the result. To read the value of the register with the address 2, run this query:

```bash
get type=16int;functionCode=3;objectsCount=1;address=2;
```

**Response:**

```json
{"result":{"value":80}}
```


![image](/images/gateway/get-set-connector-rpc/modbus-get-set-rpc-3.webp)


As you can see, the value has been successfully written.


</div>

<div class="st-tab" data-label="MQTT">

### GET method

With the GET method you can subscribe to MQTT topic and receive message from it.

```bash
get requestTopicExpression=<requestTopicExpression>;responseTopicExpression=<responseTopicExpression>;value=<value>;
```


Where:
- `<requestTopicExpression>` - the topic to publish the request;
- `<responseTopicExpression>` - the topic to subscribe to response;
- `<value>` - the value to send.

For example, in our case, we know that we can read the value of the room light level from the MQTT topic 
**"data/light_level"**. Also, we need to subscribe to the **"data/response"** topic to receive the response.
To read the value of the room light level, run this query:

```bash
get requestTopicExpression=data/get_light_level;responseTopicExpression=data/response;value=${params};
```


Also, let's take a look at the data received from the MQTT topic **"data/response"**:


![image](/images/gateway/get-set-connector-rpc/mqtt-get-set-rpc-1.webp)


### SET method

With the SET method you can publish a message to MQTT topic.

```bash
set requestTopicExpression=data/set_light_level;value=${params};
```


Where:
- `<requestTopicExpression>` - the topic to publish request;
- `<value>` - the value to send.

For example, in our case, we know that we can set the value of the room light level to the MQTT topic
**"sata/light_level"**. To set the value of the room light level, run the following query:

```bash
set requestTopicExpression=data/set_light_level;value=80;
```


On the screenshot below, you can see that we have successfully sent the SET request to the MQTT topic **"data/set_light_level"**:


![image](/images/gateway/get-set-connector-rpc/mqtt-get-set-rpc-2.webp)


Also, let's take a look at the result after SET method in the **"data/light_level"** MQTT topic by sending Two way GET RPC request.
To read the value of the room light level to make sure the room light level is really updated, run this query:

```bash
get requestTopicExpression=data/get_light_level;responseTopicExpression=data/response;value=${params};
```


On the screenshot below, you can see that the room light level value is updated to 80 after the SET request:


![image](/images/gateway/get-set-connector-rpc/mqtt-get-set-rpc-3.webp)


</div>

<div class="st-tab" data-label="BACnet">

### GET method

With the GET method you can read some data from the FTP device.

```bash
get objectType=<objectType>;objectId=<objectId>;propertyId=<propertyId>;
```

Where:
- `<objectType>` - the type of the object to read;
- `<objectId>` - the ID of the object to read;
- `<propertyId>` - the ID of the property to read.

For example, in our case, we know that we can read the value of the room light level from the BACnet device.
To read the value of the room light level, run this query:

```bash
get objectType=analogValue;objectId=1;propertyId=presentValue;
```

**Response:**

```json
{"result": "30.5"}
```


![image](/images/gateway/get-set-connector-rpc/bacnet-get-set-rpc-1.webp)


# SET method

With the SET method you can write data to the BACnet device.

```bash
set objectType=<objectType>;objectId=<objectId>;propertyId=<propertyId>;priority=<priority>;value=<value>;
```

Where:
- `<objectType>` - the type of the object to read;
- `<objectId>` - the ID of the object to read;
- `<propertyId>` - the ID of the property to read;
- `<priority>` - the priority of the value to write (optional);
- `<value>` - the value to write (optional, should be an integer from 1 to 16).

If value is none, BACnet connector will send relinquish command with Null value.
Also, SET RPC should contain value or priority, or both.

For example, in our case, we know that we can set the value of the room light level to the BACnet device.
To set the value of the room light level, run the following query:

```bash
set objectType=analogValue;objectId=1;propertyId=presentValue;value=30.9;
```

**Response:**

```json
{"result": "{\"status\":\"ok\"}"}
```


![image](/images/gateway/get-set-connector-rpc/bacnet-get-set-rpc-2.webp)


Also, let's check the value of the room light level after setting it using the GET method. To do this, simply
run the GET RPC method, described above:

```bash
get objectType=analogValue;objectId=1;propertyId=presentValue;
```

**Response:**

```json
{"result": "30.9"}
```


![image](/images/gateway/get-set-connector-rpc/bacnet-get-set-rpc-3.webp)


</div>

<div class="st-tab" data-label="REST">

### GET method

With the GET method you can send a GET request to the REST API.

```bash
get requestUrlExpression=<requestUrlExpression>;value=<value>;
```

Where:
- `<requestUrlExpression>` - the URL of the REST API;
- `<value>` - the value to send.

For example, in our case, we know that we can get the room light level from the REST API with the URL
**"http://127.0.0.1:8000/light-level"**. To get the value of the room light level, run the query:

```bash
get requestUrlExpression=http://127.0.0.1:8000/light-level;value=${params};
```

**Response:**

```json
{"result":  {"light-level":30}}
```


![image](/images/gateway/get-set-connector-rpc/rest-get-set-rpc-1.webp)


### SET method

With the SET method you can send a POST request to the REST API.

```bash
set requestUrlExpression=<requestUrlExpression>;value=<value>;HTTPMethod=<HTTPMethod>;
```

Where:
- `<requestUrlExpression>` - the URL of the REST API;
- `<value>` - the value to send.
- `<HTTPMethod>` - the HTTP method to use.

For example, in our case, we know that we can set the room light level to the REST API with the URL
**"http://127.0.0.1:8000/light-level"**. To set the value of the room light level, run the following query:

```bash
set requestUrlExpression=http://127.0.0.1:8000/light-level;value=80;HTTPMethod=POST;
```

**Response:**

```json
{"result":  {"status":"ok"}}
```


![image](/images/gateway/get-set-connector-rpc/rest-get-set-rpc-2.webp)


Also, let's take a look at light level after setting it using GET method. To do this, simply run the GET RPC method, 
described above:

```bash
get requestUrlExpression=http://127.0.0.1:8000/light-level;value=${params};
```

**Response:**

```json
{"result":  {"light-level":80}}
```


![image](/images/gateway/get-set-connector-rpc/rest-get-set-rpc-3.webp)


</div>

<div class="st-tab" data-label="Request">

### GET method

With the GET method you can send a GET request to the external API.

```bash
get requestUrlExpression=<requestUrlExpression>;
```

Where:
- `<requestUrlExpression>` - the URL of the external API.

For example, in our case, we know that we can get the room light level from the external API with the URL
**"http://127.0.0.1:8000/light-level"**. To get the value of the room light level, run the following query:

```bash
get requestUrlExpression=light-level;
```

**Response:**

```json
{"result":"{\"light-level\":30}"}
```


![image](/images/gateway/get-set-connector-rpc/request-get-set-rpc-1.webp)


### SET method

With the SET method you can send a POST request to the external API.

```bash
get requestUrlExpression=<requestUrlExpression>;value=<value>;HTTPMethod=<HTTPMethod>;
```

Where:
- `<requestUrlExpression>` - the URL of the external API;
- `<value>` - the value to send;
- `<HTTPMethod>` - the HTTP method to use.

For example, in our case, we know that we can set the room light level to the external API with the URL
**"http://127.0.0.1:8000/light-level"**. To set the value of the room light level, run this query:

```bash
set requestUrlExpression=light-level;value=80;httpMethod=POST;
```

**Response:**

```json
{"result":"{\"status\":\"ok\"}"}
```


![image](/images/gateway/get-set-connector-rpc/request-get-set-rpc-2.webp)


Also, let's take a look at light level after setting it using GET method. To do this, simply run the GET RPC method,
described above:

```bash
get requestUrlExpression=light-level;
```

**Response:**

```json
{"result":  {"light-level":80}}
```


![image](/images/gateway/get-set-connector-rpc/request-get-set-rpc-3.webp)


</div>

<div class="st-tab" data-label="FTP">

### GET method

With the GET method you can read some data from the FTP server.

```bash
get filePath=<filePath>;
```

Where:
- `<filePath>` - the path to the file on the FTP server.

For example, in our case, we know that **light_level.txt** file stores the room light level on the FTP server. 
To read the value of the room light level, run the following query:

```bash
get filePath=./light_level.txt;
```

**Response:**

```json
{"result":  30}
```


![image](/images/gateway/get-set-connector-rpc/ftp-get-set-rpc-1.webp)


### SET method

With the SET method you can write data to the FTP server.

```bash
set filePath=<filePath>;value=<value>;
```

Where:
- `<filePath>` - the path to the file on the FTP server;
- `<value>` - the value to write.

For example, in our case, we know that **light_level.txt** file stores the room light level on the FTP server.
To write the value of the room light level, run the following query:

```bash
set filePath=./light_level.txt;value=80;
```

**Response:**

```json
{"result":  "{\"success\": true}"}
```


![image](/images/gateway/get-set-connector-rpc/ftp-get-set-rpc-2.webp)


Also, let's check the value of the room light level after setting it using the GET method. To do this, simply 
run the GET RPC method, described above:

```bash
get filePath=./light_level.txt;
```

**Response:**

```json
{"result":  80}
```


![image](/images/gateway/get-set-connector-rpc/ftp-get-set-rpc-3.webp)


</div>

<div class="st-tab" data-label="Socket">

### SET method

With the SET method you can send a data to the socket.

```bash
set address=<address>;port=<port>;value=<value>;
```

Where:
- `<address>` - the address of the socket;
- `<port>` - the port of the socket;
- `<value>` - the value to send.

For example, in our case, we know that we can send the room light level to the sensor that has TCP connection and 
is listening on port 50003. To send the value of the room light level to the sensor, run the query:

```bash
set address=192.168.0.200;port=50003;value=80;
```

**Response:**

```json
{"result":  "ok"}
```


![image](/images/gateway/get-set-connector-rpc/socket-get-set-rpc-1.webp)


Also, let's see the result on the sensor's side:


![image](/images/gateway/get-set-connector-rpc/socket-get-set-rpc-2.webp)


</div>

</div>


## Next steps

Explore guides related to main SENTIENT features:

 - [Data Visualization](/docs/user-guide/visualization/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine/) - how to use rule engine to analyze data from devices.
