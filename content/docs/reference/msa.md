+++
title = "SENTIENT Microservices architecture"
description = "SENTIENT architecture"

[extra]
status = "imported"
checked = ""
source = "docs/reference/msa.md"
+++
Since SENTIENT v2.2, the platform supports microservices deployment mode. 
This article consist of high level diagram, description of data flow between various services and some architecture choices made.       

## Architecture diagram

 <object width="80%" data="/images/reference/msa-architecture.svg"></object> 
  
## Transport Microservices

SENTIENT provides MQTT, HTTP and CoAP based APIs that are available for your device applications/firmware. 
Each of the protocol APIs are provided by a separate server component and is part of SENTIENT "Transport Layer". 
The full list of components and corresponding documentation pages are listed below:

* HTTP Transport microservice provides device APIs described [here](/docs/reference/http-api/); 
* MQTT Transport microservice provides device APIs described [here](/docs/reference/mqtt-api/)
and also enables gateway APIs described [here](/docs/reference/gateway-mqtt-api/);
* CoAP Transport microservice provides device APIs described [here](/docs/reference/coap-api/);
* LwM2M Transport microservice provides device APIs described [here](/docs/reference/lwm2m-api/).

Each of the transport servers listed above communicates with the main SENTIENT Node microservices using Kafka. 
[Apache Kafka](https://kafka.apache.org) is a distributed, reliable and scalable persistent message queue and streaming platform.

The messages that are sent to Kafka are serialized using [protocol buffers](https://developers.google.com/protocol-buffers/) 
with the messages definition available [here](https://github.com/sentient/sentient/blob/master/common/proto/src/main/proto/transport.proto).

**Note**: Starting v2.5, SENTIENT Professional Edition is going to support alternative queue implementation: Amazon DynamoDB. See [roadmap](/docs/reference/roadmap) for more details.
 
There are two main topics that are used by the transport layer microservices.

First topic "tb.transport.api.requests" is used to execute short-living API requests to check device credentials or create device on behalf of the gateway.
Responses to this requests are sent to the topic that is specific for each transport microservice. The prefix of such "callback" topic is "tb.transport.api.responses" by default.

Second topic "tb.rule-engine" is used to store all incoming telemetry messages from devices until they are not processed by the rule engine. In case the rule engine node(s) are down
, messages will be persisted and available for later processing.

You can see a part of configuration file to specify those properties below:   

```yaml
transport:
  type: "${TRANSPORT_TYPE:local}" # local or remote
  remote:
    transport_api:
      requests_topic: "${TB_TRANSPORT_API_REQUEST_TOPIC:tb.transport.api.requests}"
      responses_topic: "${TB_TRANSPORT_API_RESPONSE_TOPIC:tb.transport.api.responses}"
    rule_engine:
      topic: "${TB_RULE_ENGINE_TOPIC:tb.rule-engine}"
```    

Since SENTIENT uses very simple communication protocol between transport and core services, 
it is quite easy to implement support of custom transport protocol, for example: CSV over plain TCP, binary payloads over UDP, etc.
We suggest to review existing transports [implementation](https://github.com/sentient/sentient/tree/master/common/transport/mqtt) to get started or [contact us](/docs/contact-us/) if you need any help.

## Web UI Microservices

SENTIENT provides a lightweight component written using Express.js framework to host static web ui content. Those components are completely stateless and no much configuration available. 

## JavaScript Executor Microservices

SENTIENT rule engine allows users to specify custom javascript functions to parse, filter and transform messages. 
Since those functions are user defined, we need to execute them in an isolated context to avoid impact on main processing.
SENTIENT provides a lightweight component written using Node.js to execute user defined JavaScript functions remotely to isolate them from the core rule engine components.

**Note**: SENTIENT monolith app executes user defined functions in a java embedded JS engine, which does not allow to isolate resource consumption.    
 
We recommend to launch 20+ separate JavaScript Executors that will allow certain concurrency level and load balancing of JS execution requests. 
Each microservice will subscribe to "js.eval.requests" kafka topic as part of single consumer group to enable load balancing. 
Requests for the same script are forwarded to the same JS executor using built-in Kafka partitioning by key (key is a script/rule node id).

It is possible to define max amount of pending JS execution requests and max request timeout to avoid single JS execution blocking the JS exector microservice.
Each SENTIENT core service has individual blacklist for JS functions and will not invoke blocked function more then 3(by default) times.

## SENTIENT Node

SENTIENT node is a core service written in Java that is responsible for handling:
 
 * [REST API](/docs/reference/rest-api/) calls;
 * WebSocket [subscriptions](/docs/user-guide/telemetry/#websocket-api) on entity telemetry and attribute changes;
 * Processing messages via [rule engine](/docs/user-guide/rule-engine-2-0/re-getting-started/);
 * Monitoring device [connectivity state](/docs/user-guide/device-connectivity-status/) (active/inactive).
 
**Note**: moving rule engine to a separate microservice is scheduled for SENTIENT v2.5. See [roadmap](/docs/reference/roadmap) for more details. 
 
SENTIENT node uses Actor System to implement tenant, device, rule chains and rule node actors. 
Platform nodes can join the cluster, where each node is equal. Service discovery is done via Zookeeper. 
SENTIENT nodes route messages between each other using consistent hashing algorithm based on entity id. 
So, messages for the same entity are processed on the same SENTIENT node. Platform uses [gRPC](https://grpc.io/) to send messages between SENTIENT nodes.

**Note**: SENTIENT authors consider moving from gRPC to Kafka in the future releases for exchanging messages between SENTIENT nodes. 
The main idea is to sacrifice small performance/latency penalties in favor of persistent and reliable message delivery and automatic load balancing provided by Kafka consumer groups. 

## Third-party  

### Kafka

[Apache Kafka](https://kafka.apache.org/) is an open-source stream-processing software platform. SENTIENT uses Kafka to persist incoming telemetry from HTTP/MQTT/CoAP transpots 
until it is processed by the rule engine. SENTIENT also uses Kafka for some API calls between micro-services.

### Cache database

SENTIENT caches assets, entity views, devices, device credentials, device sessions and entity relations.

##### Redis
[Redis](https://redis.io/) is source-available (under [RSALv2](https://redis.io/legal/rsalv2-agreement/) and [SSPLv1](https://redis.io/legal/server-side-public-license-sspl/)) in-memory data structure store used by SENTIENT for caching.

##### Valkey
[Valkey](https://valkey.io/) is an open-source (BSD licensed), in-memory data structure store that could be used as a drop-in replacement for Redis.

### Zookeeper

[Zookeeper](https://zookeeper.apache.org/) is an open-source server which enables highly reliable distributed coordination. 
SENTIENT uses Zookeeper to address requests processing from a single entity (device,asset,tenant) to a certain SENTIENT server 
and guarantee that only one server process data from particular device at a single point in time. 

**Note**: Zookeeper is also used by Kafka, so there was almost no reasons to use two different coordination services (Consul, etcd) in parallel.      

### HAProxy (or other LoadBalancer)

We recommend to use HAProxy for load balancing. 
You can find the reference [haproxy.cfg](https://github.com/sentient/sentient/blob/release-2.5/docker/haproxy/config/haproxy.cfg) 
configuration that corresponds to the architecture diagram below: 

<figure class="highlight"><pre><code class="language-conf" data-lang="conf"><span class="c">#HA Proxy Config
</span><span class="n">global</span>
 <span class="n">ulimit</span>-<span class="n">n</span> <span class="m">500000</span>
 <span class="n">maxconn</span> <span class="m">99999</span>
 <span class="n">maxpipes</span> <span class="m">99999</span>
 <span class="n">tune</span>.<span class="n">maxaccept</span> <span class="m">500</span>

 <span class="n">log</span> <span class="m">127</span>.<span class="m">0</span>.<span class="m">0</span>.<span class="m">1</span> <span class="n">local0</span>
 <span class="n">log</span> <span class="m">127</span>.<span class="m">0</span>.<span class="m">0</span>.<span class="m">1</span> <span class="n">local1</span> <span class="n">notice</span>

 <span class="n">ca</span>-<span class="n">base</span> /<span class="n">etc</span>/<span class="n">ssl</span>/<span class="n">certs</span>
 <span class="n">crt</span>-<span class="n">base</span> /<span class="n">etc</span>/<span class="n">ssl</span>/<span class="n">private</span>

 <span class="n">ssl</span>-<span class="n">default</span>-<span class="n">bind</span>-<span class="n">ciphers</span> <span class="n">ECDH</span>+<span class="n">AESGCM</span>:<span class="n">DH</span>+<span class="n">AESGCM</span>:<span class="n">ECDH</span>+<span class="n">AES256</span>:<span class="n">DH</span>+<span class="n">AES256</span>:<span class="n">ECDH</span>+<span class="n">AES128</span>:<span class="n">DH</span>+<span class="n">AES</span>:<span class="n">ECDH</span>+<span class="m">3</span><span class="n">DES</span>:<span class="n">DH</span>+<span class="m">3</span><span class="n">DES</span>:<span class="n">RSA</span>+<span class="n">AESGCM</span>:<span class="n">RSA</span>+<span class="n">AES</span>:<span class="n">RSA</span>+<span class="m">3</span><span class="n">DES</span>:!<span class="n">aNULL</span>:!<span class="n">MD5</span>:!<span class="n">DSS</span>
 <span class="n">ssl</span>-<span class="n">default</span>-<span class="n">bind</span>-<span class="n">options</span> <span class="n">no</span>-<span class="n">sslv3</span>

<span class="n">defaults</span>

 <span class="n">log</span> <span class="n">global</span>

 <span class="n">mode</span> <span class="n">http</span>

 <span class="n">timeout</span> <span class="n">connect</span> <span class="m">5000</span><span class="n">ms</span>
 <span class="n">timeout</span> <span class="n">client</span> <span class="m">50000</span><span class="n">ms</span>
 <span class="n">timeout</span> <span class="n">server</span> <span class="m">50000</span><span class="n">ms</span>
 <span class="n">timeout</span> <span class="n">tunnel</span>  <span class="m">1</span><span class="n">h</span>    <span class="c"># timeout to use with WebSocket and CONNECT
</span>
 <span class="n">default</span>-<span class="n">server</span> <span class="n">init</span>-<span class="n">addr</span> <span class="n">none</span>

<span class="c">#enable resolving throught docker dns and avoid crashing if service is down while proxy is starting
</span><span class="n">resolvers</span> <span class="n">docker_resolver</span>
  <span class="n">nameserver</span> <span class="n">dns</span> <span class="m">127</span>.<span class="m">0</span>.<span class="m">0</span>.<span class="m">11</span>:<span class="m">53</span>

<span class="n">listen</span> <span class="n">stats</span>
 <span class="n">bind</span> *:<span class="m">9999</span>
 <span class="n">stats</span> <span class="n">enable</span>
 <span class="n">stats</span> <span class="n">hide</span>-<span class="n">version</span>
 <span class="n">stats</span> <span class="n">uri</span> /<span class="n">stats</span>
 <span class="n">stats</span> <span class="n">auth</span> <span class="n">admin</span>:<span class="n">admin</span>@<span class="m">123</span>

<span class="n">listen</span> <span class="n">mqtt</span>-<span class="n">in</span>
 <span class="n">bind</span> *:${<span class="n">MQTT_PORT</span>}
 <span class="n">mode</span> <span class="n">tcp</span>
 <span class="n">option</span> <span class="n">clitcpka</span> <span class="c"># For TCP keep-alive
</span> <span class="n">timeout</span> <span class="n">client</span> <span class="m">3</span><span class="n">h</span>
 <span class="n">timeout</span> <span class="n">server</span> <span class="m">3</span><span class="n">h</span>
 <span class="n">option</span> <span class="n">tcplog</span>
 <span class="n">balance</span> <span class="n">leastconn</span>
 <span class="n">server</span> <span class="n">stRmqtt1</span> <span class="n">tb</span>-<span class="n">mqtt</span>-<span class="n">transport1</span>:<span class="m">1883</span> <span class="n">check</span> <span class="n">inter</span> <span class="m">5</span><span class="n">s</span> <span class="n">resolvers</span> <span class="n">docker_resolver</span> <span class="n">resolve</span>-<span class="n">prefer</span> <span class="n">ipv4</span>
 <span class="n">server</span> <span class="n">stRmqtt2</span> <span class="n">tb</span>-<span class="n">mqtt</span>-<span class="n">transport2</span>:<span class="m">1883</span> <span class="n">check</span> <span class="n">inter</span> <span class="m">5</span><span class="n">s</span> <span class="n">resolvers</span> <span class="n">docker_resolver</span> <span class="n">resolve</span>-<span class="n">prefer</span> <span class="n">ipv4</span>

<span class="n">frontend</span> <span class="n">http</span>-<span class="n">in</span>
 <span class="n">bind</span> *:${<span class="n">HTTP_PORT</span>}

 <span class="n">option</span> <span class="n">forwardfor</span>

 <span class="n">reqadd</span> <span class="n">X</span>-<span class="n">Forwarded</span>-<span class="n">Proto</span>:\ <span class="n">http</span>

 <span class="n">acl</span> <span class="n">acl_static</span> <span class="n">path_beg</span> /<span class="n">static</span>/ /<span class="n">index</span>.<span class="n">html</span>
 <span class="n">acl</span> <span class="n">acl_static</span> <span class="n">path</span> /
 <span class="n">acl</span> <span class="n">acl_static_rulenode</span> <span class="n">path_beg</span> /<span class="n">static</span>/<span class="n">rulenode</span>/

 <span class="n">acl</span> <span class="n">transport_http_acl</span> <span class="n">path_beg</span> /<span class="n">api</span>/<span class="n">v1</span>/
 <span class="n">acl</span> <span class="n">letsencrypt_http_acl</span> <span class="n">path_beg</span> /.<span class="n">well</span>-<span class="n">known</span>/<span class="n">acme</span>-<span class="n">challenge</span>/

 <span class="n">redirect</span> <span class="n">scheme</span> <span class="n">https</span> <span class="n">if</span> !<span class="n">letsencrypt_http_acl</span> !<span class="n">transport_http_acl</span> { <span class="n">env</span>(<span class="n">FORCE_HTTPS_REDIRECT</span>) -<span class="n">m</span> <span class="n">str</span> <span class="n">true</span> }

 <span class="n">use_backend</span> <span class="n">letsencrypt_http</span> <span class="n">if</span> <span class="n">letsencrypt_http_acl</span>
 <span class="n">use_backend</span> <span class="n">tb</span>-<span class="n">http</span>-<span class="n">backend</span> <span class="n">if</span> <span class="n">transport_http_acl</span>
 <span class="n">use_backend</span> <span class="n">tb</span>-<span class="n">web</span>-<span class="n">backend</span> <span class="n">if</span> <span class="n">acl_static</span> !<span class="n">acl_static_rulenode</span>

 <span class="n">default_backend</span> <span class="n">tb</span>-<span class="n">api</span>-<span class="n">backend</span>

<span class="n">frontend</span> <span class="n">https_in</span>
  <span class="n">bind</span> *:${<span class="n">HTTPS_PORT</span>} <span class="n">ssl</span> <span class="n">crt</span> /<span class="n">usr</span>/<span class="n">local</span>/<span class="n">etc</span>/<span class="n">haproxy</span>/<span class="n">default</span>.<span class="n">pem</span> <span class="n">crt</span> /<span class="n">usr</span>/<span class="n">local</span>/<span class="n">etc</span>/<span class="n">haproxy</span>/<span class="n">certs</span>.<span class="n">d</span> <span class="n">ciphers</span> <span class="n">ECDHE</span>-<span class="n">RSA</span>-<span class="n">AES256</span>-<span class="n">SHA</span>:<span class="n">RC4</span>-<span class="n">SHA</span>:<span class="n">RC4</span>:<span class="n">HIGH</span>:!<span class="n">MD5</span>:!<span class="n">aNULL</span>:!<span class="n">EDH</span>:!<span class="n">AESGCM</span>

  <span class="n">option</span> <span class="n">forwardfor</span>

  <span class="n">reqadd</span> <span class="n">X</span>-<span class="n">Forwarded</span>-<span class="n">Proto</span>:\ <span class="n">https</span>

  <span class="n">acl</span> <span class="n">transport_http_acl</span> <span class="n">path_beg</span> /<span class="n">api</span>/<span class="n">v1</span>/

  <span class="n">acl</span> <span class="n">acl_static</span> <span class="n">path_beg</span> /<span class="n">static</span>/ /<span class="n">index</span>.<span class="n">html</span>
  <span class="n">acl</span> <span class="n">acl_static</span> <span class="n">path</span> /
  <span class="n">acl</span> <span class="n">acl_static_rulenode</span> <span class="n">path_beg</span> /<span class="n">static</span>/<span class="n">rulenode</span>/

  <span class="n">use_backend</span> <span class="n">tb</span>-<span class="n">http</span>-<span class="n">backend</span> <span class="n">if</span> <span class="n">transport_http_acl</span>
  <span class="n">use_backend</span> <span class="n">tb</span>-<span class="n">web</span>-<span class="n">backend</span> <span class="n">if</span> <span class="n">acl_static</span> !<span class="n">acl_static_rulenode</span>

  <span class="n">default_backend</span> <span class="n">tb</span>-<span class="n">api</span>-<span class="n">backend</span>

<span class="n">backend</span> <span class="n">letsencrypt_http</span>
  <span class="n">server</span> <span class="n">letsencrypt_http_srv</span> <span class="m">127</span>.<span class="m">0</span>.<span class="m">0</span>.<span class="m">1</span>:<span class="m">8080</span>

<span class="n">backend</span> <span class="n">tb</span>-<span class="n">web</span>-<span class="n">backend</span>
  <span class="n">balance</span> <span class="n">leastconn</span>
  <span class="n">option</span> <span class="n">tcp</span>-<span class="n">check</span>
  <span class="n">option</span> <span class="n">log</span>-<span class="n">health</span>-<span class="n">checks</span>
  <span class="n">server</span> <span class="n">tbWeb1</span> <span class="n">tb</span>-<span class="n">web</span>-<span class="n">ui1</span>:<span class="m">8080</span> <span class="n">check</span> <span class="n">inter</span> <span class="m">5</span><span class="n">s</span> <span class="n">resolvers</span> <span class="n">docker_resolver</span> <span class="n">resolve</span>-<span class="n">prefer</span> <span class="n">ipv4</span>
  <span class="n">server</span> <span class="n">tbWeb2</span> <span class="n">tb</span>-<span class="n">web</span>-<span class="n">ui2</span>:<span class="m">8080</span> <span class="n">check</span> <span class="n">inter</span> <span class="m">5</span><span class="n">s</span> <span class="n">resolvers</span> <span class="n">docker_resolver</span> <span class="n">resolve</span>-<span class="n">prefer</span> <span class="n">ipv4</span>
  <span class="n">http</span>-<span class="n">request</span> <span class="n">set</span>-<span class="n">header</span> <span class="n">X</span>-<span class="n">Forwarded</span>-<span class="n">Port</span> %[<span class="n">dst_port</span>]

<span class="n">backend</span> <span class="n">tb</span>-<span class="n">http</span>-<span class="n">backend</span>
  <span class="n">balance</span> <span class="n">leastconn</span>
  <span class="n">option</span> <span class="n">tcp</span>-<span class="n">check</span>
  <span class="n">option</span> <span class="n">log</span>-<span class="n">health</span>-<span class="n">checks</span>
  <span class="n">server</span> <span class="n">tbHttp1</span> <span class="n">tb</span>-<span class="n">http</span>-<span class="n">transport1</span>:<span class="m">8081</span> <span class="n">check</span> <span class="n">inter</span> <span class="m">5</span><span class="n">s</span> <span class="n">resolvers</span> <span class="n">docker_resolver</span> <span class="n">resolve</span>-<span class="n">prefer</span> <span class="n">ipv4</span>
  <span class="n">server</span> <span class="n">tbHttp2</span> <span class="n">tb</span>-<span class="n">http</span>-<span class="n">transport2</span>:<span class="m">8081</span> <span class="n">check</span> <span class="n">inter</span> <span class="m">5</span><span class="n">s</span> <span class="n">resolvers</span> <span class="n">docker_resolver</span> <span class="n">resolve</span>-<span class="n">prefer</span> <span class="n">ipv4</span>

<span class="n">backend</span> <span class="n">tb</span>-<span class="n">api</span>-<span class="n">backend</span>
  <span class="n">balance</span> <span class="n">leastconn</span>
  <span class="n">option</span> <span class="n">tcp</span>-<span class="n">check</span>
  <span class="n">option</span> <span class="n">log</span>-<span class="n">health</span>-<span class="n">checks</span>
  <span class="n">server</span> <span class="n">tbApi1</span> <span class="n">tb1</span>:<span class="m">8080</span> <span class="n">check</span> <span class="n">inter</span> <span class="m">5</span><span class="n">s</span> <span class="n">resolvers</span> <span class="n">docker_resolver</span> <span class="n">resolve</span>-<span class="n">prefer</span> <span class="n">ipv4</span>
  <span class="n">server</span> <span class="n">tbApi2</span> <span class="n">tb2</span>:<span class="m">8080</span> <span class="n">check</span> <span class="n">inter</span> <span class="m">5</span><span class="n">s</span> <span class="n">resolvers</span> <span class="n">docker_resolver</span> <span class="n">resolve</span>-<span class="n">prefer</span> <span class="n">ipv4</span>
  <span class="n">http</span>-<span class="n">request</span> <span class="n">set</span>-<span class="n">header</span> <span class="n">X</span>-<span class="n">Forwarded</span>-<span class="n">Port</span> %[<span class="n">dst_port</span>]</code></pre></figure>

### Databases

See "[SQL vs NoSQL vs Hybrid?](/docs/reference/#sql-vs-nosql-vs-hybrid-database-approach)" for more details. 

## Deployment

You can find the reference [docker-compose.yml](https://github.com/sentient/sentient/blob/master/docker/docker-compose.yml)
and corresponding [documentation](https://github.com/sentient/sentient/blob/master/docker/README.md) that will help you to run SENTIENT containers in a cluster mode 
(although on a single host machine)
