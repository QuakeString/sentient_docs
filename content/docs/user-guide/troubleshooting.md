+++
title = "Troubleshooting"
description = "SENTIENT IoT Platform troubleshooting"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/troubleshooting.md"
+++
## Possible performance issues

Here we will describe different possible scenarios of what may go wrong.


<div class="st-tabs">

<div class="st-tab" data-label="No Message Processing">

If you are using <code>RETRY_ALL, RETRY_FAILED, RETRY_TIMED_OUT</code> or <code>RETRY_FAILED_AND_TIMED_OUT</code> strategy for some rule-engine queue, it is possible that some failed node could block the whole processing of the messages in this queue.

Here what you can do to find the reason of the issue:

- Analyze [Rule Engine Statistics Dashboard](/docs/user-guide/rule-engine-2-0/overview/#rule-engine-statistics). Here you can find out if some of your messages failed or timed-out.
Also in the bottom side of the dashboard you can find description of the exceptions inside the rule-engine with the name of the problematic rule-node.

- After finding out what rule-node is failing you can [enable DEBUG](/docs/user-guide/rule-engine-2-0/overview/#debugging) and see what messages cause the failure of the rule-node and look at the detailed error description.

**Tip:** Separate unstable and test use-cases from other rule-engine by creating a separate queue. In this case failure will only affect the processing of this separate queue, and not the whole system.
You can configure this logic to happen automatically for the device by using [Device Profile](/docs/user-guide/device-profiles/#queue-name) feature. 

**Tip:** Handle <b>Failure</b> events for all rule-nodes that connect to some external service (REST API call, Kafka, MQTT etc).
This way you guaranty that your rule-engine processing won't stop in case of some failure on the side of external system.
You can store failed message in DB, send some notification or just <b>log</b> message.

</div>

<div class="st-tab" data-label="Growing Latency For Messages">

Sometimes you can experience growing latency of message processing inside the rule-engine. Here are the steps you can take to discover the reason for the issue:
- Check if there are timeouts in [Rule Engine Statistics Dashboard](/docs/user-guide/rule-engine-2-0/overview/#rule-engine-statistics). Timeouts in rule-nodes slow down the processing of the queue and can lead to latency.
- [Check CPU usage](#cpumemory-usage) for the following services:
    - SENTIENT services (sentient-nodes, sentient-rule-engine and sentient-core nodes, transport nodes). High CPU load on some services means that you need to scale up that part of the system.
    - PostgreSQL and pgpool (if you are in <b>high-availability</b> mode). High load on Postgres can lead to slow processing of all Postgres-related rule-nodes (saving attributes, reading attributes etc), and the system in general.
    - Cassandra (if you are using Cassandra as storage for timeseries data). High load on Cassandra can lead to slow processing of all Cassandra-related rule-nodes (saving timeseries etc).
    - Queue. Regardless of the queue type, make sure that it always has enough resources.
- Check [consumer-group lag](#consumer-group-message-lag-for-kafka-queue) (if you are using Kafka as queue).
- Enable [Message Pack Processing Log](#message-pack-processing-log). It will allow you to see the name of the slowest rule-node.
- Separate your use-cases by different queues. If some group of your devices should be processed separately from other devices, you should [configure](/docs/user-guide/device-profiles/#queue-name) the separate rule-engine queue for this group. Also, you can just separate messages based on some logic to different queues inside of the Root rule-engine. By doing this you guaranty that slow processing of one use-case will not affect the processing of the other use-case.


</div>

</div>


## Troubleshooting instruments and tips

### Rule Engine Statistics Dashboard
You can see if there are any Failures, Timeouts or Exceptions during the processing of your rule-chain. More detailed information you can find [here](/docs/user-guide/rule-engine-2-0/overview/#rule-engine-statistics).

### Consumer group message lag for Kafka Queue

**Note:** This method can be used only if Kafka is selected as a queue.

With this log you can identify if there's some issue with processing of your messages (since Queue is used for all messaging inside the system you can analyze not only rule-engine queues but also <b>transport</b>, <b>core</b> etc).
For more detailed information about troubleshooting rule-engine processing using consumer-group lag click [here](/docs/user-guide/rule-engine-2-0/overview/#troubleshooting).

### CPU/Memory Usage

Sometimes the problem is that you don't have enough resources for some service. You can view CPU and Memory usage by logging into your server/container/pod and executing <code>top</code> linux command.

For the more convenient monitoring it is better to have configured Prometheus and Grafana.

If you see that some services sometimes use 100% of the CPU, you should either scale the service horizontally by creating new nodes in cluster or scale it vertically by increasing the total amount of CPU.

### Message Pack Processing Log

You can enable logging of the slowest and most frequently called rule-nodes.
To do this you need to [update your logging configuration](#enable-certain-logs) with the following <i>logger</i>:

```bash
<logger name="org.sentient.server.service.queue.MsgPackProcessingContext" level="DEBUG" />
```

After this you can find the following messages in your [logs](#logs):

```bash
2021-03-24 17:01:21,023 [sentient-rule-engine-consumer-24-thread-3] DEBUG o.s.s.s.q.MsgPackProcessingContext - Top Rule Nodes by max execution time:
2021-03-24 17:01:21,024 [sentient-rule-engine-consumer-24-thread-3] DEBUG o.s.s.s.q.MsgPackProcessingContext - [Main][3f740670-8cc0-11eb-bcd9-d343878c0c7f] max execution time: 1102. [RuleChain: Thermostat|RuleNode: Device Profile Node(3f740670-8cc0-11eb-bcd9-d343878c0c7f)]
2021-03-24 17:01:21,024 [sentient-rule-engine-consumer-24-thread-3] DEBUG o.s.s.s.q.MsgPackProcessingContext - [Main][3f6debf0-8cc0-11eb-bcd9-d343878c0c7f] max execution time: 1. [RuleChain: Thermostat|RuleNode: Message Type Switch(3f6debf0-8cc0-11eb-bcd9-d343878c0c7f)]
2021-03-24 17:01:21,024 [sentient-rule-engine-consumer-24-thread-3] INFO  o.s.s.s.q.MsgPackProcessingContext - Top Rule Nodes by avg execution time:
2021-03-24 17:01:21,024 [sentient-rule-engine-consumer-24-thread-3] INFO  o.s.s.s.q.MsgPackProcessingContext - [Main][3f740670-8cc0-11eb-bcd9-d343878c0c7f] avg execution time: 604.0. [RuleChain: Thermostat|RuleNode: Device Profile Node(3f740670-8cc0-11eb-bcd9-d343878c0c7f)]
2021-03-24 17:01:21,025 [sentient-rule-engine-consumer-24-thread-3] INFO  o.s.s.s.q.MsgPackProcessingContext - [Main][3f6debf0-8cc0-11eb-bcd9-d343878c0c7f] avg execution time: 1.0. [RuleChain: Thermostat|RuleNode: Message Type Switch(3f6debf0-8cc0-11eb-bcd9-d343878c0c7f)]
2021-03-24 17:01:21,025 [sentient-rule-engine-consumer-24-thread-3] INFO  o.s.s.s.q.MsgPackProcessingContext - Top Rule Nodes by execution count:
2021-03-24 17:01:21,025 [sentient-rule-engine-consumer-24-thread-3] INFO  o.s.s.s.q.MsgPackProcessingContext - [Main][3f740670-8cc0-11eb-bcd9-d343878c0c7f] execution count: 2. [RuleChain: Thermostat|RuleNode: Device Profile Node(3f740670-8cc0-11eb-bcd9-d343878c0c7f)]
2021-03-24 17:01:21,028 [sentient-rule-engine-consumer-24-thread-3] INFO  o.s.s.s.q.MsgPackProcessingContext - [Main][3f6debf0-8cc0-11eb-bcd9-d343878c0c7f] execution count: 1. [RuleChain: Thermostat|RuleNode: Message Type Switch(3f6debf0-8cc0-11eb-bcd9-d343878c0c7f)]
```

### Clearing Redis/Valkey Cache

**Note:** This can be used only if Redis or Valkey is selected as a cache.

It is possible that the data inside the cache has become corrupted. Regardless of the reason, it is always safe to clear the cache — SENTIENT will simply refill it at runtime. To clear the cache, you need to log into the server/container/pod where it is deployed, open the application command-line tool (<code>redis-cli</code> for Redis and <code>valkey-cli</code> for Valkey), and run the <code>FLUSHALL</code>command. To clear the cache in Sentinel mode, access the master container and execute the cache-clearing command.

So if you are struggling with identifying the reason of some problem, you can safely clear cache to make sure it isn't the reason of the issue.


## Logs

### Read logs

Regardless of the deployment type, SENTIENT logs are stored on the same server/container as SENTIENT Server/Node itself in the following directory:

```bash
/var/log/sentient
```

Different deployment tools provide different ways to view logs:


<div class="st-tabs">

<div class="st-tab" data-label="Standalone Deployment">

View last logs in runtime:
 
```bash
tail -f /var/log/sentient/sentient.log
```

You can use <b>grep</b> command to show only the output with desired string in it. 
For example you can use the following command in order to check if there are any errors on the backend side:

```bash
cat /var/log/sentient/sentient.log | grep ERROR
```

</div>

<div class="st-tab" data-label="Docker-Compose Deployment">

View last logs in runtime:
 
```bash
docker compose logs -f sentient-core1 sentient-core2 sentient-rule-engine1 sentient-rule-engine2
```


<div class="st-callout info">


If you still rely on Docker Compose as docker-compose (with a hyphen) execute next command:

**docker-compose logs -f sentient-core1 sentient-core2 sentient-rule-engine1 sentient-rule-engine2**


</div>


If you suspect the issue is related only to rule-engine, you can filter and view only the rule-engine logs:

```bash
docker compose logs -f sentient-rule-engine1 sentient-rule-engine2
```


<div class="st-callout info">


If you still rely on Docker Compose as docker-compose (with a hyphen) execute next command:

**docker-compose logs -f sentient-rule-engine1 sentient-rule-engine2**


</div>


You can use <b>grep</b> command to show only the output with desired string in it. 
For example you can use the following command in order to check if there are any errors on the backend side:

```bash
docker compose logs sentient-core1 sentient-core2 sentient-rule-engine1 sentient-rule-engine2 | grep ERROR
```


<div class="st-callout info">


If you still rely on Docker Compose as docker-compose (with a hyphen) execute next command:

**docker-compose logs sentient-core1 sentient-core2 sentient-rule-engine1 sentient-rule-engine2 \| grep ERROR**


</div>


**Tip:** you can redirect logs to file and then analyze with any text editor:

```bash
docker compose logs -f sentient-rule-engine1 sentient-rule-engine2 > rule-engine.log
```


<div class="st-callout info">


If you still rely on Docker Compose as docker-compose (with a hyphen) execute next command:

**docker-compose logs -f sentient-rule-engine1 sentient-rule-engine2 > rule-engine.log**


</div>


**Note:** you can always log into the SENTIENT container and view logs there:

```bash
docker ps
docker exec -it NAME_OF_THE_CONTAINER bash
```


</div>

<div class="st-tab" data-label="Kubernetes Deployment">

View all pods of the cluster:

```bash
kubectl get pods
```

View last logs for the desired pod:
 
```bash
kubectl logs -f POD_NAME
```

To view SENTIENT node logs use command:

```bash
kubectl logs -f sentient-node-0
```

You can use <b>grep</b> command to show only the output with desired string in it. 
For example you can use the following command in order to check if there are any errors on the backend side:

```bash
kubectl logs -f sentient-node-0 | grep ERROR
```

If you have multiple nodes you could redirect logs from all nodes to files on you machine and then analyze them: 

```bash
kubectl logs -f sentient-node-0 > sentient-node-0.log
kubectl logs -f sentient-node-1 > sentient-node-1.log
```


**Note:** you can always log into the SENTIENT container and view logs there:

```bash
kubectl exec -it sentient-node-0 -- bash
cat /var/log/sentient/sentient-node-0/sentient.log
```


</div>

</div>


### Enable certain logs

SENTIENT provides the ability to enable/disable logging for certain parts of the system depending on what information do you need for troubleshooting.

You can do this by modifying <b>logback.xml</b> file. As logs itself, it is stored on the same server/container as SENTIENT Server/Node in the following directory:

```bash
/usr/share/sentient/conf
```

Here's an example of the <b>logback.xml</b> configuration:

```bash
<!DOCTYPE configuration>
<configuration scan="true" scanPeriod="10 seconds">

    <appender name="fileLogAppender"
              class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>/var/log/sentient/sentient.log</file>
        <rollingPolicy
                class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <fileNamePattern>/var/log/sentient/sentient.%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <maxFileSize>100MB</maxFileSize>
            <maxHistory>30</maxHistory>
            <totalSizeCap>3GB</totalSizeCap>
        </rollingPolicy>
        <encoder>
            <pattern>%d{ISO8601} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <logger name="org.sentient.server" level="INFO" />
    <logger name="org.sentient.js.api" level="TRACE" />
    <logger name="com.microsoft.azure.servicebus.primitives.CoreMessageReceiver" level="OFF" />

    <root level="INFO">
        <appender-ref ref="fileLogAppender"/>
    </root>
</configuration>
```

The most useful for the troubleshooting parts of the config files are <i>loggers</i>.
They allow you to enable/disable logging for the certain class or group of classes.
In the example above the default logging level is <b>INFO</b> (it means that logs will contain only general information, warnings and errors), but for the package <code>org.sentient.js.api</code> we enabled the most detailed level of logging.
There's also a possibility to completely disable logs for some part of the system, in the example above we did it to <code>com.microsoft.azure.servicebus.primitives.CoreMessageReceiver</code> class using <b>OFF</b> log-level.

To enable/disable logging for some part of the system you need to add proper <code></logger></code> configuration and wait up to 10 seconds.

Different deployment tools provide different ways to update logs:


<div class="st-tabs">

<div class="st-tab" data-label="Standalone Deployment">

For standalone deployment you need to update <code>/usr/share/sentient/conf/logback.xml</code> in order to change logging configuration.

</div>

<div class="st-tab" data-label="Docker-Compose Deployment">

For docker-compose deployment we are mapping <code>/config</code> folder to your local system (<code>./sentient-node/conf</code> folder).
So in order to change logging configuration you need to update <code>./sentient-node/conf/logback.xml</code> file.

</div>

<div class="st-tab" data-label="Kubernetes Deployment">

For kubernetes deployment we are using <b>ConfigMap</b> kubernetes entity to provide sentient-nodes with logback configuration.
So in order to update <b>logback.xml</b> you need to do the following:

 ```bash
edit common/sentient-node-configmap.yml
kubectl apply -f common/sentient-node-configmap.yml
 ```

After 10 seconds the changes should be applied to logging configuration.

</div>

</div>


## Metrics

You may enable prometheus metrics by setting environment variables `METRICS_ENABLED` to value `true` and `METRICS_ENDPOINTS_EXPOSE` to value `prometheus` in the configuration file.
If you are running SENTIENT as microservices with separate services for MQTT and COAP transport, you also need to set environment variables `WEB_APPLICATION_ENABLE` to value `true`, 
`WEB_APPLICATION_TYPE` to value `servlet` and `HTTP_BIND_PORT` to value `8081` for MQTT and COAP services in order to enable web-server with Prometheus metrics.

These metrics are exposed at the path: `https://<yourhostname>/actuator/prometheus` which can be scraped by prometheus (No authentication required).

## Prometheus metrics

Some internal state metrics can be exposed by the Spring Actuator using Prometheus.

Here's the list of metrics SENTIENT pushes to Prometheus.

### <b>sentient-node</b> metrics
- <i>attributes_queue_${index_of_queue}</i> (statsNames - <i>totalMsgs, failedMsgs, successfulMsgs</i>): stats about writing <b>attributes</b> to the database. 
Note that there are several queues (threads) for persisting attributes in order to reach maximum performance.
- <i>ruleEngine_${name_of_queue}</i> (statsNames - <i>totalMsgs, failedMsgs, successfulMsgs, tmpFailed, failedIterations, successfulIterations, timeoutMsgs, tmpTimeout</i>): 
  stats about processing of the messages inside of the Rule Engine. They are persisted for each queue (e.g. Main, HighPriority, SequentialByOriginator etc).
  Some stats descriptions:
  - <i>tmpFailed</i>: number of messages that failed and got reprocessed later
  - <i>tmpTimeout</i>: number of messages that timed out and got reprocessed later
  - <i>timeoutMsgs</i>: number of messages that timed out and were discarded afterwards
  - <i>failedIterations</i>: iterations of processing messages pack where at least one message wasn't processed successfully
- <i>ruleEngine_${name_of_queue}_seconds</i> (for each present <i>tenantId</i>): stats about the time message processing took for different queues.
- <i>core</i> (statsNames - <i>totalMsgs, toDevRpc, coreNfs, sessionEvents, subInfo, subToAttr, subToRpc, deviceState, getAttr, claimDevice, subMsgs</i>): 
  stats about processing of the internal system messages.
  Some stats descriptions:
  - <i>toDevRpc</i>: number of processed RPC responses from Transport services
  - <i>sessionEvents</i>: number of session events from Transport services
  - <i>subInfo</i>: number of subscription infos from Transport services
  - <i>subToAttr</i>: number of subscribes to attribute updates from Transport services
  - <i>subToRpc</i>: number of subscribes to RPC from Transport services
  - <i>getAttr</i>: number of 'get attributes' requests from Transport services
  - <i>claimDevice</i>: number of Device claims from Transport services
  - <i>deviceState</i>: number of processed changes to Device State
  - <i>subMsgs</i>: number of processed subscriptions
  - <i>coreNfs</i>: number of processed specific 'system' messages
- <i>jsInvoke</i> (statsNames - <i>requests, responses, failures</i>): stats about total, successful and failed requests to the JS executors
- <i>attributes_cache</i> (results - <i>hit, miss</i>): stats about how much attribute requests went to the cache


### <b>transport</b> metrics
- <i>transport</i> (statsNames - <i>totalMsgs, failedMsgs, successfulMsgs</i>): stats about requests received by Transport from SENTIENT nodes 
- <i>ruleEngine_producer</i> (statsNames - <i>totalMsgs, failedMsgs, successfulMsgs</i>): stats about pushing messages from Transport to the Rule Engine.
- <i>core_producer</i> (statsNames - <i>totalMsgs, failedMsgs, successfulMsgs</i>): stats about pushing messages from Transport to the SENTIENT node Device actor.
- <i>transport_producer</i> (statsNames - <i>totalMsgs, failedMsgs, successfulMsgs</i>): stats about requests from Transport to SENTIENT.


<b>Some metrics depends on the type of the database you are using to persist timeseries data.</b>

### PostgreSQL-specific metrics
- <i>ts_latest_queue_${index_of_queue}</i> (statsNames - <i>totalMsgs, failedMsgs, successfulMsgs</i>): stats about writing <b>latest telemetry</b> to the database. 
Note that there are several queues (threads) in order to reach maximum performance.
- <i>ts_queue_${index_of_queue}</i> (statsNames - <i>totalMsgs, failedMsgs, successfulMsgs</i>): stats about writing <b>telemetry</b> to the database. 
Note that there are several queues (threads) in order to reach maximum performance.

### Cassandra-specific metrics
- <i>rateExecutor_currBuffer</i>: number of messages that are currently being persisted inside the Cassandra.
- <i>rateExecutor_tenant</i> (for each present <i>tenantId</i>): number of requests that got rate-limited
- <i>rateExecutor</i> (statsNames - <i>totalAdded, totalRejected, totalLaunched, totalReleased, totalFailed, totalExpired, totalRateLimited</i>)
Stats descriptions:
    - <i>totalAdded</i>: number messages that were submitted for persisting
    - <i>totalRejected</i>: number messages that were rejected while trying to submit for persisting
    - <i>totalLaunched</i>: number messages sent to the Cassandra
    - <i>totalReleased</i>: number successfully persisted messages
    - <i>totalFailed</i>: number of messages that were not persisted
    - <i>totalExpired</i>: number of expired messages that were not sent to the Cassandra
    - <i>totalRateLimited</i>: number of messages that were not processed because of the Tenant's rate-limits
    
## Grafana Dashboards


You can import preconfigured Grafana dashboards from [here](https://github.com/sentient/sentient/tree/master/docker/monitoring/grafana/provisioning/dashboards).


> **Note:** Depending on the cluster configuration, you may need to make changes to the dashboards.

You can also view Grafana dashboards after deploying the SENTIENTs docker-compose cluster configuration (for more information, please follow [this guide](/docs/user-guide/install/cluster/docker-compose-setup/)).
Make sure that `MONITORING_ENABLED` environment variable is set to `true`. Once deployed, you can access Prometheus at [http://localhost:9090](http://localhost:9090) and Grafana at [http://localhost:3000](http://localhost:3000) (by default, the username is `admin` and the password is `foobar`).

Here are the screenshots of the default preconfigured Grafana dashboards:


<div class="st-gallery"><figure><img src="/images/user-guide/troubleshooting/attributes-cache-grafana.webp" alt="Statistics about Attributes cache efficiency." loading="lazy"><figcaption>Statistics about Attributes cache efficiency.</figcaption></figure><figure><img src="/images/user-guide/troubleshooting/core-and-js-metrics-grafana.webp" alt="Statistics about requests to SENTIENT core and JS processors." loading="lazy"><figcaption>Statistics about requests to SENTIENT core and JS processors.</figcaption></figure><figure><img src="/images/user-guide/troubleshooting/db-metrics-grafana.webp" alt="Statistics about `attributes` and `timeseries` persistence to the PostgreSQL." loading="lazy"><figcaption>Statistics about `attributes` and `timeseries` persistence to the PostgreSQL.</figcaption></figure><figure><img src="/images/user-guide/troubleshooting/rule-engine-latency-grafana.webp" alt="Statistics about time it took to process messages inside of the Rule Engine." loading="lazy"><figcaption>Statistics about time it took to process messages inside of the Rule Engine.</figcaption></figure><figure><img src="/images/user-guide/troubleshooting/rule-engine-metrics-grafana.webp" alt="Statistics about processing of the message inside of the Rule Engine." loading="lazy"><figcaption>Statistics about processing of the message inside of the Rule Engine.</figcaption></figure><figure><img src="/images/user-guide/troubleshooting/single-service-metrics-grafana.webp" alt="Separate statistics for each service. You can choose the service in the upper left corner." loading="lazy"><figcaption>Separate statistics for each service. You can choose the service in the upper left corner.</figcaption></figure><figure><img src="/images/user-guide/troubleshooting/transport-metrics-grafana.webp" alt="Statistics about messages in Transport services." loading="lazy"><figcaption>Statistics about messages in Transport services.</figcaption></figure></div>


## OAuth2

Sometimes after configuring OAuth you can not see the button for logging in with OAuth provider. This happens when “Domain name” and “Redirect URI Template” contain faulty values, they need to be the same you use for accessing your SENTIENT web page.

Example:

| Base URL |  Domain name     |  Redirect URI Template                    |
|-----------------|----------------- |----------------------------------         |
|http://mycompany.com:8080    |mycompany.com:8080     | http://mycompany.com:8080/login/oauth2/code  |
|https://mycompany.com          |mycompany.com          | https://mycompany.com/login/oauth2/code       |

Base URL in "HOME" section should not contain "/" or other characters.

> Go to your SENTIENT as a System Administrator. Check the General
> Settings -> Base URL should not contain “/” at the end (e.g. “https://
> mycompany.com ” instead of “https://mycompany.com/”).

For OAuth2 configuration click [here](/docs/user-guide/oauth-2-support/).

## Getting help

<section id="talkToUs">
    <div id="gettingHelp">
        <a href="https://github.com/sentient/sentient">
            <span class="phrase-heading">Github Project</span>
            <p>Check out the project and consider contributing.</p>
        </a>
        <a href="https://stackoverflow.com/questions/tagged/sentient">
            <span class="phrase-heading">Stack Overflow</span>
            <p>The SENTIENT team will also monitor posts tagged sentient. If there aren’t any existing questions that help, please ask a new one!</p>
        </a>
    </div>
</section>

If your problem isn't answered by any of the guides above, feel free to contact SENTIENT team.

Contact us
