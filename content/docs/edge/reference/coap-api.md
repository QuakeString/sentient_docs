+++
title = "CoAP Device API Reference"

[extra]
status = "imported"
checked = ""
source = "docs/edge/reference/coap-api.md"
+++
[CoAP](https://en.wikipedia.org/wiki/Constrained_Application_Protocol) is a lightweight, UDP-based protocol designed for constrained IoT devices.
Although it follows a request–response model similar to HTTP, CoAP is optimized for low-power and low-bandwidth networks.   
You can find more information about CoAP [here](https://tools.ietf.org/html/rfc7252).

CoAP Observe [Option](https://tools.ietf.org/html/rfc7641) allows subscription to resources and receiving notifications on resource change.

SENTIENT server nodes act as a CoAP Server that supports both regular and observe requests.

<hr>

## Client libraries setup

Many CoAP client libraries are available for different platforms and languages.

The examples in this guide are based on [CoAP cli](https://www.npmjs.com/package/coap-cli), a command-line CoAP client.

**Install CoAP CLI (Linux/macOS)**
```bash
npm install coap-cli -g
```


<div class="st-callout info">


**Note**: CoAP CLI does not support query parameters. If your use case requires query parameters, use [coap-client](https://manpages.ubuntu.com/manpages/focal/man5/coap-client.5.html) instead.


</div>


**Install coap-client**
- **Ubuntu 20.04+** 
  ```bash
  sudo apt install libcoap2-bin
  ```
  

- for **Ubuntu 18.04**
  ```bash
  sudo apt install libcoap1-bin
  ```
  

<hr>

## Authentication methods

SENTIENT supports two authentication mechanisms to secure COAP connections.

**Supported methods**:
- [Access token](/docs/edge/user-guide/ssl/coap-access-token/). Uses a unique device access token included as a path parameter in each CoAP request.
- [X.509 certificates](/docs/edge/user-guide/ssl/coap-x509-certificates/). Uses digital certificates to authenticate devices and establish secure communication based on **public key infrastructure (PKI)**.

> The examples in this guide use **access token–based authentication**.

**Possible error codes and their reasons:**
- **4.00 Bad Request** - Invalid URL, parameters, or payload
- **4.01 Unauthorized** - Invalid **access token**
- **4.04 Not Found** - Requested resource does not exist

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


However, it is also possible to send data via [Protocol Buffers](https://developers.google.com/protocol-buffers).
Please refer to the [CoAP transport type](/docs/edge/user-guide/device-profiles/#coap-transport-type) configuration section in device profile article for more details.

Using custom binary format or some serialization framework is also possible. See [protocol customization](#protocol-customization) for more details.

<hr>

## Telemetry upload API

In order to publish telemetry data to SENTIENT server node, send POST request.

First, select the authentication method:


<div class="st-tabs">

<div class="st-tab" data-label="Access token">

Send POST request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry
```


> ⚠️ Don&#39;t forget to replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

</div>

<div class="st-tab" data-label="X.509 Certificate">

Send POST request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/telemetry
```


> ⚠️ Don&#39;t forget to replace <code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.


</div>

</div>


The simplest supported data formats are:

```json
{"key1":"value1", "key2":"value2"}
```

or

```json
[{"key1":"value1"}, {"key2":"value2"}]
```


<div class="st-callout info">


**Please note** 
<br>
that in this case, the server-side timestamp will be assigned to uploaded data!


</div>


In case your device is able to get the client-side timestamp, you can use following format:

```json
{"ts":1451649600512, "values":{"key1":"value1", "key2":"value2"}}
```

Where **1451649600512** is a [unix timestamp](https://en.wikipedia.org/wiki/Unix_time) with milliseconds precision. For example, the value '1451649600512' corresponds to 'Fri, 01 Jan 2016 12:00:00.512 GMT'.

<br><b><font size="3">Examples</font></b>   
Below are examples of commands for publishing different types of telemetry data.

> ⚠️ Don&#39;t forget to replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

**Example 1**.   
Publish data as an object without timestamp (server-side timestamp will be used) using data from [telemetry-data-as-object.json](/docs/reference/resources/telemetry-data-as-object.json) file.


<div class="st-tabs">

<div class="st-tab" data-label="Execute the command:">


```bash
cat telemetry-data-as-object.json | coap post coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry
```


</div>

</div>


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


**Example 2**.   
Publish data as an array of objects without timestamp (server-side timestamp will be used) using data from [telemetry-data-as-array.json](/docs/reference/resources/telemetry-data-as-array.json) file.


<div class="st-tabs">

<div class="st-tab" data-label="Execute the command:">


```bash
cat telemetry-data-as-array.json | coap post coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry
```


</div>

</div>


The content of the JSON file:

```json
[{"key1":"value1"}, {"key2":true}]
```


**Example 3**.   
Publish data as an object with timestamp (telemetry timestamp will be used) using data from [telemetry-data-with-ts.json](/docs/reference/resources/telemetry-data-with-ts.json) file.


<div class="st-tabs">

<div class="st-tab" data-label="Execute the command:">


```bash
cat telemetry-data-with-ts.json | coap post coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/telemetry
```


</div>

</div>


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

* Upload [client-side](/docs/edge/user-guide/attributes/#attribute-types) device attributes to the server.
* Request [client-side](/docs/edge/user-guide/attributes/#attribute-types) and [shared](/docs/edge/user-guide/attributes/#attribute-types) device attributes from the server.
* Subscribe to [shared](/docs/edge/user-guide/attributes/#attribute-types) device attributes from the server.

<hr>

### Publish attribute update to the server

In order to publish client-side device attributes to SENTIENT server node, send POST request.

First, select the authentication method:


<div class="st-tabs">

<div class="st-tab" data-label="Access token">

Send POST request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes
```


> ⚠️ Don&#39;t forget to replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

Publish client-side attributes update using data from [new-attributes-values.json](/docs/reference/resources/new-attributes-values.json) file.

The content of the **"new-attributes-values.json"** file:

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

**Execute the command:**


```bash
cat new-attributes-values.json | coap post coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes
```


</div>

<div class="st-tab" data-label="X.509 Certificate">

Send POST request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/attributes
```


> ⚠️ Don&#39;t forget to replace <code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.


Publish client-side attributes update using data from [new-attributes-values.json](/docs/reference/resources/new-attributes-values.json) file.

The content of the **"new-attributes-values.json"** file:

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

**Execute the command:**


```bash
cat new-attributes-values.json | coap post coap://$SENTIENT_EDGE_HOST_NAME/api/v1/attributes
```


</div>

</div>


<hr>

### Request attribute values from the server

In order to request client-side or shared device attributes to SENTIENT server node, send GET request.

First, select the authentication method:


<div class="st-tabs">

<div class="st-tab" data-label="Access token">

Send GET request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes?clientKeys=attribute1,attribute2&sharedKeys=shared1,shared2
```


> ⚠️ Don&#39;t forget to replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.


<div class="st-callout info">


**Note**: This example shown with the coap-client instead of CoAP cli since CoAP cli does not support query parameters. Please refer to [Client libraries setup](#docsContent).


</div>


**Execute the command:**


```bash
coap-client -m get "coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes?clientKeys=attribute1,attribute2&sharedKeys=shared1,shared2"
```


</div>

<div class="st-tab" data-label="X.509 Certificate">

Send GET request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/attributes?clientKeys=attribute1,attribute2&sharedKeys=shared1,shared2
```


> ⚠️ Don&#39;t forget to replace <code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.


<div class="st-callout info">


**Note**: This example shown with the coap-client instead of CoAP cli since CoAP cli does not support query parameters. Please refer to [Client libraries setup](#docsContent).


</div>


**Execute the command:**


```bash
coap-client -m get "coap://$SENTIENT_EDGE_HOST_NAME/api/v1/attributes?clientKeys=attribute1,attribute2&sharedKeys=shared1,shared2"
```


</div>

</div>


Result:

```bash
{"client":{"attribute1":"value1","attribute2":true}}
```


<div class="st-callout info">


**Please note:**
<br>
the intersection of client-side and shared device attribute keys is a bad practice! 
However, it is still possible to have same keys for client, shared or even server-side attributes.


</div>


<hr>

### Subscribe to attribute updates from the server

In order to subscribe to shared device attribute changes, send GET request with Observe option.

First, select the authentication method:


<div class="st-tabs">

<div class="st-tab" data-label="Access token">

Send GET request with Observe option to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes
```


> ⚠️ Don&#39;t forget to replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

Once shared attribute will be changed by one of the server-side components (REST API or Rule Chain) the client will receive the following update:

**Execute the command:**


```bash
coap get -o coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes
```


</div>

<div class="st-tab" data-label="X.509 Certificate">

Send GET request with Observe option to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/attributes
```


> ⚠️ Don&#39;t forget to replace <code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.


Once shared attribute will be changed by one of the server-side components (REST API or Rule Chain) the client will receive the following update:

**Execute the command:**


```bash
coap get -o coap://$SENTIENT_EDGE_HOST_NAME/api/v1/attributes
```


</div>

</div>


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

In order to subscribe to RPC commands from the server, send GET request with observe flag.

First, select the authentication method:


<div class="st-tabs">

<div class="st-tab" data-label="Access token">

Send GET request with observe flag to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc
```


> Where    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is your device&#39;s access token.

Once subscribed, a client may receive RPC requests. An example of RPC request body is shown below:

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

To reply to an RPC request, send a POST request to the following URL


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc/{$id}
```


> Where <code>$id</code> is an integer request identifier.

**Example**

- Use **RPC debug terminal** widget in your SENTIENT instance.
- Subscribe to RPC commands from the server using the command below. To do this, in the first terminal window send GET request with observe flag:


```bash
coap-client -m get coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc -s 100 -B 100
```


<div class="st-callout info">


The "`s`" option stands for subscribe and the value has to be specified in seconds.

The "`B`" options stands for break (the operation will be break after desired timeout) and the value has to be specified in seconds


</div>


- Send an RPC request "connect" to the device using **RPC debug terminal** widget.
- Save the [rpc-response.json](/docs/reference/resources/rpc-response.json) file to your PC.
- In the second terminal window simulate sending a response from the device to the server:


```bash
coap-client -f rpc-response.json -m post coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc/1
```


> ⚠️ Replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

You should receive a response from the device:

```bash
{"result":"ok"}
```


</div>

<div class="st-tab" data-label="X.509 Certificate">

Send GET request with observe flag to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/rpc
```


> ⚠️ Where <code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.


Once subscribed, a client may receive RPC requests. An example of RPC request body is shown below:

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

To reply to an RPC request, send a POST request to the following URL


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/rpc/{$id}
```


> Where <code>$id</code> is an integer request identifier.

<br>

**Example**

- Use **RPC debug terminal** widget in your SENTIENT instance;
- Subscribe to RPC commands from the server using the command below. To do this, in the first terminal window send GET request with observe flag.


```bash
coap-client -m get coap://$SENTIENT_EDGE_HOST_NAME/api/v1/rpc -s 100 -B 100
```


<div class="st-callout info">


The "`s`" option stands for subscribe and the value has to be specified in seconds.

The "`B`" options stands for break (the operation will be break after desired timeout) and the value has to be specified in seconds


</div>


- Send an RPC request "connect" to the device using **RPC debug terminal** widget.
- Save the [rpc-response.json](/docs/reference/resources/rpc-response.json) file to your PC.
- In the second terminal window simulate sending a response from the device to the server:


```bash
coap-client -f rpc-response.json -m post coap://$SENTIENT_EDGE_HOST_NAME/api/v1/rpc/1
```


> ⚠️ Replace <code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.


- You should receive a response from the device:

```bash
{"result":"ok"}
```


</div>

</div>


<hr>

### Client-side RPC

In order to send RPC commands to the server, send POST request.

First, select the authentication method:


<div class="st-tabs">

<div class="st-tab" data-label="Access token">

Send POST request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc
```


> Where    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> is your device&#39;s access token.

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
cat rpc-client-request.json | coap post coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc
```


> ⚠️ Replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

- You should receive a response from the server:

```bash
{"time":"Thursday, February 5, 2026, 9:08:22 AM Coordinated Universal Time"}
```


</div>

<div class="st-tab" data-label="X.509 Certificate">

Send POST request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/rpc
```


> ⚠️ Where <code>$SENTIENT_EDGE_HOST_NAME</code> is your SENTIENT Edge hostname or IP address.


Both request and response body should be valid JSON documents. The content of the documents is specific to the rule node that will handle your request.

<br>
**Example**

- In the **Edge** **Root Rule Chain** add two nodes: [transformation script](/docs/user-guide/rule-engine-2-0/nodes/transformation/script) and [rpc call reply](/docs/user-guide/rule-engine-2-0/nodes/action/rpc-call-reply). Connect them to "[Log RPC from Device](/docs/user-guide/rule-engine-2-0/nodes/action/log)" action node with "**Success**" link.
- In the **script** node enter the function:

```bash
return {msg: {time:String(new Date())}, metadata: metadata, msgType: msgType};
```


- Save the [rpc-client-request.json](/docs/reference/resources/rpc-client-request.json) file to your PC;
- Now, send request to the server using the command below:


```bash
cat rpc-client-request.json | coap post coap://$SENTIENT_EDGE_HOST_NAME/api/v1/rpc
```


> ⚠️ Replace <code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.


- You should receive a response from the server:

```bash
{"time":"2016 11 21 12:54:44.287"}
```


</div>

</div>


<hr>

## Claiming devices

The Device Claiming feature allows end users to securely associate a device with their account after the device has been deployed and connected to SENTIENT.
For a detailed explanation of the device claiming workflow and supported scenarios, refer to the [Claiming devices](/docs/user-guide/claiming-devices) documentation.

In order to initiate claiming device, send POST request.

First, select the authentication method:


<div class="st-tabs">

<div class="st-tab" data-label="Access token">

Send POST request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/claim
```


> ⚠️ Don&#39;t forget to replace    
&#8194;&#8226;&#8194;<code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.   
&#8194;&#8226;&#8194;<code>$ACCESS_TOKEN</code> with your device&#39;s access token.

</div>

<div class="st-tab" data-label="X.509 Certificate">

Send POST request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/claim
```


> ⚠️ Don&#39;t forget to replace <code>$SENTIENT_EDGE_HOST_NAME</code> with your SENTIENT Edge hostname or IP address.


</div>

</div>


The supported data format is:

```json
{"secretKey":"value", "durationMs":60000}
```


<div class="st-callout info">


**Please note** 
<br>
that the above fields are optional. In case the **secretKey** is not specified, the empty string as a default value is used.
In case the **durationMs** is not specified, the system parameter **device.claim.duration** is used (in the file **/etc/sentient/conf/sentient.yml**).


</div>


<hr>

## Device provisioning

Device provisioning allows devices to be registered dynamically without manual creation in the SENTIENT UI.
For a detailed explanation of the provisioning process and supported scenarios, refer to the [Device provisioning](/docs/user-guide/device-provisioning) documentation.

**Provisioning request**   
To initiate device provisioning, send POST request to the following URL:


```bash
coap://$SENTIENT_EDGE_HOST_NAME/api/v1/provision
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

Select the authentication method:


<div class="st-tabs">

<div class="st-tab" data-label="Access token">

The CoAP client has to issue the GET request to


```bash
coap get coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/firmware?title=$TITLE&version=$VERSION
```


Where
- **$SENTIENT_HOST_NAME** is your localhost, or the platform address
- **$ACCESS_TOKEN** is device access token
- **$TITLE** is the firmware title
- **$VERSION** is the version of the target firmware


</div>

<div class="st-tab" data-label="X.509 Certificate">

The CoAP client has to issue the GET request to


```bash
coap get coap://$SENTIENT_EDGE_HOST_NAME/api/v1/firmware?title=$TITLE&version=$VERSION
```


Where
- **$SENTIENT_HOST_NAME** is your localhost, or the platform address;
- **$TITLE** is the firmware title;
- **$VERSION** is the version of the target firmware.


</div>

</div>


<hr>

## Protocol customization

CoAP transport can be fully customized for specific use-case by changing the corresponding [module](https://github.com/sentient/sentient/tree/master/transport/coap).

<hr>

## Next steps
