+++
title = "HTTP Device API Reference"
description = "Supported HTTP API Reference for IoT Devices"

[extra]
status = "imported"
checked = ""
source = "docs/edge/reference/http-api.md"
+++
[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is a general-purpose network protocol that can be used in IoT applications. 
You can find more information about HTTP [here](https://www.w3.org/Protocols/rfc2616/rfc2616.txt).
HTTP protocol is TCP based and uses request-response model.  

SENTIENT server nodes act as an HTTP Server that supports both HTTP and HTTPS protocols.

<hr>

## Client libraries setup

Many HTTP client libraries are available for different platforms and languages.
The examples in this article will be based on [curl](https://en.wikipedia.org/wiki/CURL).

**Install curl for Linux**
```bash
sudo apt-get install curl
```


> Starting with Windows 10 build 17063 and macOS 10.2 6C115 (Jaguar), cURL is available by default.

<hr>

## HTTP authentication method

SENTIENT supports [access token](/docs/user-guide/ssl/http-access-token/)-based authentication to secure HTTP connections. For each HTTP request, the client must include the access token as part of the request URL.

> The examples in this guide use **access token–based authentication**.

**Possible error codes and their reasons:**
- **400 Bad Request** - Invalid URL, request parameters or body
- **401 Unauthorized** - Invalid **access token**
- **404 Not Found** - Requested resource does not exist

<hr>

## Key-value format

By default, SENTIENT supports key-value content in JSON. Key is always a string, while value can be either string, boolean, double, long or JSON.
For example:

```json
{
 "stringKey":"value1", 
 "booleanKey":true, 
 "doubleKey":42.0, 
 "longKey":73, 
 "jsonKey": {
    "someNumber": 42,
    "someArray": [1,2,3],
    "someNestedObject": {"key": "value"}
 }
}
```


Using custom binary format or some serialization framework is also possible. See [protocol customization](#protocol-customization) for more details.

<hr>

## Telemetry upload API

In order to publish telemetry data to SENTIENT server node, send POST request to the following URL:


```bash
http(s)://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry
```


> ⚠️ Where    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is the device&#39;s access token.

The simplest supported data formats are:

```json
{"key1":"value1", "key2":"value2"}
```

or

```json
[{"key1":"value1"}, {"key2":"value2"}]
```

In this case, the server-side timestamp will be assigned to uploaded data!

In case your device is able to get the client-side timestamp, you can use following format:

```json
{"ts":1451649600512, "values":{"key1":"value1", "key2":"value2"}}
```

Where **1451649600512** is a [unix timestamp](https://en.wikipedia.org/wiki/Unix_time) with milliseconds precision.
For example, the value '1451649600512' corresponds to 'Fri, 01 Jan 2016 12:00:00.512 GMT'

<br>
Below are the examples of commands for publishing different types of telemetry data.

> ⚠️ Don&#39;t forget to replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is your device&#39;s access token.

**Example 1**.   
Publish data as an object without timestamp (server-side timestamp will be used).

Execute the command:


```bash
curl -v -X POST --data "{"temperature":42,"humidity":73}" http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
```


Telemetry data:

```json
{"temperature":42,"humidity":73}
```

**Example 2**.   
Publish data as an object without timestamp (server-side timestamp will be used) using data from [telemetry-data-as-object.json](/docs/reference/resources/telemetry-data-as-object.json) file.

Execute the command:


```bash
curl -v -X POST -d @telemetry-data-as-object.json http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
```


The content of the JSON file:

```json
{
  "stringKey": "value1",
  "booleanKey": true,
  "doubleKey": 42.0,
  "longKey": 73,
  "jsonKey": {
    "someNumber": 42,
    "someArray": [1,2,3],
    "someNestedObject": {"key": "value"}
  }
}
```

**Example 3**.   
Publish data as an array of objects without timestamp (server-side timestamp will be used) using data from [telemetry-data-as-array.json](/docs/reference/resources/telemetry-data-as-array.json) file.

Execute the command:


```bash
curl -v -X POST -d @telemetry-data-as-array.json http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
```


The content of the JSON file:

```json
[{"key1":"value1"}, {"key2":true}]
```

**Example 4**. Publish data as an object with timestamp (telemetry timestamp will be used) using data from [telemetry-data-with-ts.json](/docs/reference/resources/telemetry-data-with-ts.json) file.

Execute the command:


```bash
curl -v -X POST -d @telemetry-data-with-ts.json http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry --header "Content-Type:application/json"
```


The content of the JSON file:

```json
{
  "ts": 1451649600512,
  "values": {
    "stringKey": "value1",
    "booleanKey": true,
    "doubleKey": 42.0,
    "longKey": 73,
    "jsonKey": {
      "someNumber": 42,
      "someArray": [1, 2, 3],
      "someNestedObject": {
        "key": "value"
      }
    }
  }
}
```

<hr>

## Attributes API

SENTIENT attributes API allows devices to

* Upload [client-side](/docs/user-guide/attributes/#attribute-types) device attributes to the server.
* Request [client-side](/docs/user-guide/attributes/#attribute-types) and [shared](/docs/user-guide/attributes/#attribute-types) device attributes from the server.
* Subscribe to [shared](/docs/user-guide/attributes/#attribute-types) device attributes from the server.

<hr>

### Publish attribute update to the server

In order to publish client-side device attributes to SENTIENT server node, send POST request to the following URL:


```bash
http(s)://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes
```


> Where    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is the device&#39;s access token.
<br>

Below are the examples of commands for publishing different types of telemetry data.

**Example 1**.   
Publish client-side attributes update


```bash
curl -v -X POST --data "{"attribute1": "value1", "attribute2":true, "attribute3": 43.0}" http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes --header "Content-Type:application/json"
```


**Example 2**.   
Publish client-side attributes update from the [new-attributes-values.json](/docs/reference/resources/new-attributes-values.json) file.


```bash
curl -v -X POST -d @new-attributes-values.json http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes --header "Content-Type:application/json"
```


The content of the JSON file:

```json
{
  "attribute1": "value1",
  "attribute2": true,
  "attribute3": 42.0,
  "attribute4": 73,
  "attribute5": {
    "someNumber": 42,
    "someArray": [1,2,3],
    "someNestedObject": {"key": "value"}
  }
}
```


<hr>

### Request attribute values from the server

In order to request client-side or shared device attributes to SENTIENT server node, send GET request to the following URL:


```bash
http(s)://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes?clientKeys=attribute1,attribute2&sharedKeys=shared1,shared2
```


> Where    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is the device&#39;s access token.

<br>


```bash
curl -v -X GET http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes?clientKeys=attribute1,attribute2&sharedKeys=shared1,shared2
```


Result:
```bash
{"client":{"attribute1":"value1","attribute2":true}}
```


<div class="st-callout info">


**Please note**
<br>
the intersection of client-side and shared device attribute keys is a bad practice! 
However, it is still possible to have same keys for client, shared or even server-side attributes.


</div>


<hr>

### Subscribe to attribute updates from the server

In order to subscribe to shared device attribute changes, send GET request with optional "timeout" request parameter to the following URL:


```bash
http(s)://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes/updates
```


> Where    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is the device&#39;s access token.

Once shared attribute will be changed by one of the server-side components (REST API or Rule Chain) the client will receive the following update: 


```bash
curl -v -X GET http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes/updates?timeout=20000
```


Result:
```bash
{"client":{"attribute1":"value1","attribute2":true}}
```

<hr>

## JSON value support

We have added support of JSON data structures to telemetry and attributes API to simplify work with device configuration.
JSON support allows you to both upload from the device, and push nested objects to the device.
You can store one configuration JSON as a shared attribute and push it to the device. You can also process the JSON data in the rule engine and raise alarms, etc.

Therefore, this improvement minimizes the number of Database operations when SENTIENT stores the data.
For example, “temperature” and “humidity” would be stored as separate rows in SQL or NoSQL databases in order to efficiently aggregate this data for visualization.
Since there is no need to aggregate JSON data, we can store all the content as one row instead of separate rows for each configuration item.
In some of our environments, it is possible to decrease the number of database operations more than 10 times by aggregating multiple parameters within one JSON.

Learn more about JSON value support with the [video](https://www.youtube.com/watch?v=ErV5Krwhak0&ab_channel=SENTIENT).

<hr>

## RPC API

### Server-side RPC

In order to subscribe to RPC commands from the server, send GET request with optional "timeout" request parameter to the following URL:


```bash
http(s)://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc
```


> Where    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is the device&#39;s access token.

Once subscribed, a client may receive rpc request or a timeout message if there are no requests to a particular device.
An example of RPC request body is shown below:

```json
{
  "id": "1",
  "method": "setGpio",
  "params": {
    "pin": "23",
    "value": 1
  }
}
```

> Where   
&#8194;&#8226;&#8194;**id** - request id, integer request identifier   
&#8194;&#8226;&#8194;**method** - RPC method name, string   
&#8194;&#8226;&#8194;**params** - RPC method params, custom json object

It is possible to reply to them using POST request to the following URL:


```bash
http(s)://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc/{$id}
```


> Where <code>$id</code> is an integer request identifier.

<br>
**Let&#39;s look at an example**:

- Use **RPC debug terminal** widget in your SENTIENT instance;
- Subscribe to RPC commands from the server using the command below. To do this, in the first terminal window send GET request with observe flag.


```bash
curl -v -X GET http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc?timeout=20000
```


> Where    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is the device&#39;s access token.

- Send an RPC request "connect" to the device using **RPC debug terminal** widget;
- Save the [rpc-response.json](/docs/reference/resources/rpc-response.json) file to your PC;
- In the second terminal window simulate sending a response from the device to the server:


```bash
curl -v -X POST -d @rpc-response.json http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc/1 --header "Content-Type:application/json"
```


You should receive a response from the device:

```bash
{"result":"ok"}
```


<hr>

### Client-side RPC

In order to send RPC commands to the server, send POST request to the following URL:


```bash
http(s)://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc
```


> Where    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is the device&#39;s access token.

Both request and response body should be valid JSON documents. The content of the documents is specific to the rule node that will handle your request.

<br>

**Example**
- In the **Edge** **Root Rule Chain** add two nodes: [transformation script](/docs/user-guide/rule-engine-2-0/nodes/transformation/script) and [rpc call reply](/docs/user-guide/rule-engine-2-0/nodes/action/rpc-call-reply). Connect them to "[Log RPC from Device](/docs/user-guide/rule-engine-2-0/nodes/action/log)" action node with "**Success**" link.
- In the **script** node enter the function:

```bash
return {msg: {time: new Date()}, metadata: metadata, msgType: msgType};
```


- Save the [rpc-client-request.json](/docs/reference/resources/rpc-client-request.json) file to your PC;
- Now, send request to the server using the command below:


```bash
curl -X POST -d @rpc-client-request.json http://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc --header "Content-Type:application/json"
```


You should receive a response from the server:

```bash
{"time":"Thursday, February 5, 2026, 9:08:22 AM Coordinated Universal Time"}
```


<hr>

## Claiming devices

The Device Claiming feature allows end users to securely associate a device with their account after the device has been deployed and connected to SENTIENT.
For a detailed explanation of the device claiming workflow and supported scenarios, refer to the [Claiming devices](/docs/user-guide/claiming-devices) documentation.

**Claiming request**   
To initiate the device claiming process, the device must send a POST request to the following endpoint:


```bash
http(s)://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/claim
```


> Where    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is the device&#39;s access token.

**Request payload**   
The request body must contain the following JSON structure:

```json
{"secretKey":"value", "durationMs":60000}
```

**Payload fields**
- **secretKey** — a secret value used to authorize the claiming process
- **durationMs** — the time window (in milliseconds) during which the device can be claimed


<div class="st-callout info">


**Please note** that the above fields are optional. In case the **secretKey** is not specified, the empty string as a default value is used.
In case the **durationMs** is not specified, the system parameter **device.claim.duration** is used (in the file **/etc/sentient/conf/sentient.yml**).


</div>


<hr>

## Device provisioning

Device provisioning allows devices to be registered dynamically without manual creation in the SENTIENT UI.
For a detailed explanation of the provisioning process and supported scenarios, refer to the [Device provisioning](/docs/user-guide/device-provisioning) documentation.

**Provisioning request**
To initiate device provisioning, send a POST request to the following endpoint:


```bash
http(s)://$SENTIENT_EDGE_HOST_NAME/api/v1/provision
```


Where **$SENTIENT_EDGE_HOST_NAME** is your SENTIENT Edge hostname or IP address.


**Request Payload**   
The provisioning request must use the following JSON format:

```json
{
  "deviceName": "DEVICE_NAME",
  "provisionDeviceKey": "u7piawkboq8v32dmcmpp",
  "provisionDeviceSecret": "jpmwdn8ptlswmf4m29bw"
}
```

**Payload fields**   
- **deviceName** — the name of the device to be provisioned.
- **provisionDeviceKey** — the provisioning key configured in SENTIENT.
- **provisionDeviceSecret** — the provisioning secret associated with the provisioning key.

If the provided credentials are valid, SENTIENT automatically creates the device (if it does not already exist) and returns the device credentials, allowing the device to start communicating with the platform.

<hr>

## Firmware API

When SENTIENT initiates the firmware update over HTTP it sets the _fw_title_, _fw_version_, _fw_checksum_, _fw_checksum_algorithm_ shared attributes.

To receive firmware update information and download the firmware, the device must send a GET request to the following endpoint:


```bash
http(s)://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/firmware?title=$TITLE&version=$VERSION
```


Parameters   
&#8194;&#8226;&#8194;**$SENTIENT_EDGE_HOST_NAME** is your SENTIENT Edge hostname or IP address   
&#8194;&#8226;&#8194;**$ACCESS_TOKEN** is your device&#39;s access token   
&#8194;&#8226;&#8194;**$TITLE** - the firmware title   
&#8194;&#8226;&#8194;**$VERSION** - the target firmware version

<hr>

## Protocol customization

HTTP transport can be fully customized for specific use-case by changing the corresponding [module](https://github.com/sentient/sentient/tree/master/transport/http).

<hr>

## Next steps
