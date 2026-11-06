+++
title = "Remote Integrations"
description = "Remote Integrations Documentation"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/remote-integrations.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only [**Professional Edition**](/products/sentient-pe/) supports **Platform Integrations** feature.<br>
Use [**SENTIENT Cloud**](/installations/choose-region/) or [**install**](/docs/user-guide/install/pe/installation-options/) your own platform instance.


</div>

Remote Integrations allow reliable data streaming from multiple devices in the local area network (LAN) to the SENTIENT platform in the cloud. 
They are helpful if you have, for example, a local MQTT broker or OPC-UA server with no external IP address and is not reachable from where your SENTIENT platform is installed. 
The remote integration initiates a connection to these servers, pulls the data, stores it locally, and then streams it to the SENTIENT instance.

Although this approach requires some additional steps in the deployment process, it allows integration with servers and devices deployed in the LAN. A separate integration process improves isolation level and performance.

The remote integration approach enables tenants to launch plain [TCP](/docs/user-guide/integrations/tcp/) and [UDP](/docs/user-guide/integrations/udp/) integrations. Those two integrations are unique because they start a server that binds to a specific port. 
Since SENTIENT is a multi-tenant environment, we can't launch TCP and UDP integrations as part of the core service due to possible port collisions between tenants. 
That is why we propose each tenant to launch a TCP/UDP integration as a remote one. The same applies to any custom integration that the tenant creates.

![image](/images/user-guide/integrations/remote/remote-integrations-overview.webp)

It is possible to execute any SENTIENT Integration separately from the SENTIENT instance.

This guide contains step-by-step instructions on how to launch MQTT remote integration that connects to the local MQTT Broker and pushes data to the [SENTIENT Cloud](https://localhost/signup).

You can find additional information about the SENTIENT Platform integrations feature [here](/docs/user-guide/integrations/).

## SENTIENT configuration

We assume you already have a tenant administrator account on your own [SENTIENT Professional Edition instance](/docs/user-guide/install/pe/installation-options/) or [SENTIENT Cloud](https://localhost/signup).

### Create remote integration in SENTIENT

Let's create remote integration in SENTIENT that will connect to the local broker using port 1883 and subscribe to all topics.

- Go to the "**Integrations center**" section -> "**Integrations**" page and click "plus" icon to add a new integration. Name it "**MQTT remote integration**", select type "**MQTT**";

![image](/images/user-guide/integrations/remote/remote-integration-1-paas.webp)

- The next step is to add a default uplink converter. The new converter will contain necessary code to convert incoming data. Click "**Next**";

![image](/images/user-guide/integrations/remote/remote-integration-2-paas.webp)

- You can create a new downlink converter at the step of adding a downlink converter. But for now, leave the "Downlink data converter" field empty. Click "**Skip**";

![image](/images/user-guide/integrations/remote/remote-integration-3-paas.webp)

- Specify **host**: "**localhost**" and **port**: "**1883**" at the connection step;
- Subscribe to all **topics**;
- You can also select an MQTT **QoS** level. We use MQTT QoS level 0 (At most once) by default;
- Copy and save the "**Integration key**" and "**Integration secret**". We will use this values later;

![image](/images/user-guide/integrations/remote/remote-integration-4-paas.webp)

- Go to the **advanced settings**. It is better to uncheck the "**Clean session**" parameter. Many brokers do not support sticky sessions, so will silently close the connection if you try to connect with this option enabled;
- Click the "**Add**" button to create the integration.

![image](/images/user-guide/integrations/remote/remote-integration-5-paas.webp)

<br>
Now let's proceed to the steps for installation remote integration.

## Choose your platform and install

One can install SENTIENT Integration via Docker, Debian or RPM packages.
Please use one of the next steps.

 * [Docker on Linux or Mac OS](#docker-on-linuxmac)
 * [Docker on Windows](#docker-on-windows)
 * [Ubuntu](#ubuntu-server)
 * [CentOS/RHEL Server](#centosrhel-server)

### Docker on Linux/Mac

- **[Install Docker CE](https://docs.docker.com/engine/installation/)**
- **Choose Integration to install**


<div class="st-tabs">

<div class="st-tab" data-label="HTTP Integrations(HTTP, Sigfox, ThingPark, OceanConnect and  T-Mobile IoT CDP)">

Execute the following command to pull the image:

```bash
docker pull sentient/tb-pe-http-integration:
```


Execute the following command to create volume for the integration logs (799 is the user id of SENTIENT non-root docker user):

```bash
mkdir -p ~/.tb-pe-http-integration-logs && sudo chown -R 799:799 ~/.tb-pe-http-integration-logs
```


Execute the following command to run the integration:

```bash
docker run -it -p 8082:8082 -v ~/.tb-pe-http-integration-logs:/var/log/tb-http-integration \
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" \
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" \
--name my-tb-pe-http-integration --restart always sentient/tb-pe-http-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-v ~/.tb-pe-http-integration-logs:/var/log/tb-http-integration`   - mounts the host's dir `~/.tb-pe-http-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-http-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-http-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-http-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-http-integration
```


To stop the container:

```
docker stop tb-pe-http-integration
```


To start the container:

```
docker start tb-pe-http-integration
```


</div>

<div class="st-tab" data-label="MQTT Integrations(MQTT, AWS IoT, IBM Watson, The Things Stack Community)">

Execute the following command to pull the image:

```bash
docker pull sentient/tb-pe-mqtt-integration:
```


Execute the following command to create volume for the integration logs (799 is the user id of SENTIENT non-root docker user):

```bash
mkdir -p ~/.tb-pe-mqtt-integration-logs && sudo chown -R 799:799 ~/.tb-pe-mqtt-integration-logs
```


Execute the following command to run the integration:

```bash
docker run -it -v ~/.tb-pe-mqtt-integration-logs:/var/log/tb-mqtt-integration \
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" \
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" \
--name my-tb-pe-mqtt-integration --restart always sentient/tb-pe-mqtt-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-v ~/.tb-pe-mqtt-integration-logs:/var/log/tb-mqtt-integration`   - mounts the host's dir `~/.tb-pe-mqtt-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-mqtt-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-mqtt-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-mqtt-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-mqtt-integration
```


To stop the container:

```
docker stop tb-pe-mqtt-integration
```


To start the container:

```
docker start tb-pe-mqtt-integration
```


</div>

<div class="st-tab" data-label="AWS SQS Integration">

Execute the following command to pull the image:

```bash
docker pull sentient/tb-pe-aws-integration:
```


Execute the following command to create volume for the integration logs (799 is the user id of SENTIENT non-root docker user):

```bash
mkdir -p ~/.tb-pe-aws-integration-logs && sudo chown -R 799:799 ~/.tb-pe-aws-integration-logs
```


Execute the following command to run the integration:

```bash
docker run -it -v ~/.tb-pe-aws-integration-logs:/var/log/tb-aws-integration \
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" \
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" \
--name my-tb-pe-aws-integration --restart always sentient/tb-pe-aws-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-v ~/.tb-pe-aws-integration-logs:/var/log/tb-aws-integration`   - mounts the host's dir `~/.tb-pe-aws-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-aws-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-aws-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-aws-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-aws-integration
```


To stop the container:

```
docker stop tb-pe-aws-integration
```


To start the container:

```
docker start tb-pe-aws-integration
```


</div>

<div class="st-tab" data-label="Azure Event HubIntegration">

Execute the following command to pull the image:

```bash
docker pull sentient/tb-pe-azure-integration:
```


Execute the following command to create volume for the integration logs (799 is the user id of SENTIENT non-root docker user):

```bash
mkdir -p ~/.tb-pe-azure-integration-logs && sudo chown -R 799:799 ~/.tb-pe-azure-integration-logs
```


Execute the following command to run the integration:

```bash
docker run -it -v ~/.tb-pe-azure-integration-logs:/var/log/tb-azure-integration \
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" \
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" \
--name my-tb-pe-azure-integration --restart always sentient/tb-pe-azure-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-v ~/.tb-pe-azure-integration-logs:/var/log/tb-azure-integration`   - mounts the host's dir `~/.tb-pe-azure-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-azure-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-azure-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-azure-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-azure-integration
```


To stop the container:

```
docker stop tb-pe-azure-integration
```


To start the container:

```
docker start tb-pe-azure-integration
```


</div>

<div class="st-tab" data-label="OPC UA Integration">

Execute the following command to pull the image:

```bash
docker pull sentient/tb-pe-opc-ua-integration:
```


Execute the following command to create volume for the integration logs (799 is the user id of SENTIENT non-root docker user):

```bash
mkdir -p ~/.tb-pe-opc-ua-integration-logs && sudo chown -R 799:799 ~/.tb-pe-opc-ua-integration-logs
```


Execute the following command to run the integration:

```bash
docker run -it -v ~/.tb-pe-opc-ua-integration-logs:/var/log/tb-opc-ua-integration \
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" \
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" \
--name my-tb-pe-opc-ua-integration --restart always sentient/tb-pe-opc-ua-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-v ~/.tb-pe-opc-ua-integration-logs:/var/log/tb-opc-ua-integration`   - mounts the host's dir `~/.tb-pe-opc-ua-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-opc-ua-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-opc-ua-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-opc-ua-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-opc-ua-integration
```


To stop the container:

```
docker stop tb-pe-opc-ua-integration
```


To start the container:

```
docker start tb-pe-opc-ua-integration
```


</div>

<div class="st-tab" data-label="TCP/UDP Integration">

Execute the following command to pull the image:

```bash
docker pull sentient/tb-pe-tcp-udp-integration:
```


Execute the following command to create volume for the integration logs (799 is the user id of SENTIENT non-root docker user):

```bash
mkdir -p ~/.tb-pe-tcp-udp-integration-logs && sudo chown -R 799:799 ~/.tb-pe-tcp-udp-integration-logs
```


Execute the following command to run the integration:

```bash
docker run -it -p 10560:10560 -v ~/.tb-pe-tcp-udp-integration-logs:/var/log/tb-tcp-udp-integration  \
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" \
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" \
--name my-tb-pe-tcp-udp-integration --restart always sentient/tb-pe-tcp-udp-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-p 10560:10560` - connect local port 10560 to exposed internal 10560 port for the integration. If the exposed port is UDP, add `/udp` at the end, e.g. `-p 11560:11560/udp` 
- `-v ~/.tb-pe-tcp-udp-integration-logs:/var/log/tb-tcp-udp-integration`   - mounts the host's dir `~/.tb-pe-tcp-udp-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-tcp-udp-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-tcp-udp-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-tcp-udp-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-tcp-udp-integration
```


To stop the container:

```
docker stop tb-pe-tcp-udp-integration
```


To start the container:

```
docker start tb-pe-tcp-udp-integration
```


</div>

<div class="st-tab" data-label="CoAP Integration">

Execute the following command to pull the image:

```bash
docker pull sentient/tb-pe-coap-integration:
```


Execute the following command to create volume for the integration logs (799 is the user id of SENTIENT non-root docker user):

```bash
mkdir -p ~/.tb-pe-coap-integration-logs && sudo chown -R 799:799 ~/.tb-pe-coap-integration-logs
```


Execute the following command to run the integration:

```bash
docker run -it -p 5683:5683/udp -v ~/.tb-pe-coap-integration-logs:/var/log/tb-coap-integration  \
-e "RPC_HOST=localhost" -e "RPC_PORT=9090" \
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" \
--name my-tb-pe-coap-integration --restart always sentient/tb-pe-coap-integration:
```


Where: 
    
- `localhost` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-p 5683:5683/udp` - connect local udp port 5683 to exposed internal 5683 udp port for the integration.
- `-v ~/.tb-pe-coap-integration-logs:/var/log/tb-coap-integration`   - mounts the host's dir `~/.tb-pe-coap-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-coap-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-coap-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-coap-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-coap-integration
```


To stop the container:

```
docker stop tb-pe-coap-integration
```


To start the container:

```
docker start tb-pe-coap-integration
```


</div>

</div>


 - **Advanced configuration**

See configuration yml file below for a list of possible configuration parameters, corresponding environment variables and their default values.
For example, default client id of the integration, that is used in integration debug messages is *"remote"* and can be altered by setting *"RPC_CLIENT_ID"* environment variable.


```bash
server:
  # Server bind address
  address: "${HTTP_BIND_ADDRESS:0.0.0.0}"
  # Server bind port
  port: "${HTTP_BIND_PORT:8082}"

integration:
  routingKey: "${INTEGRATION_ROUTING_KEY:PUT_YOUR_ROUTING_KEY_HERE}"
  secret: "${INTEGRATION_SECRET:PUT_YOUR_SECRET_HERE}"
  # Allows connection to the localhost resources. For example, local MQTT broker, etc.
  allow_local_network_hosts: "${INTEGRATION_ALLOW_LOCAL_NETWORK_HOSTS:true}"
  statistics:
    # Enable/disable integration statistics
    enabled: "${INTEGRATION_STATISTICS_ENABLED:true}"
    # Send statistics interval. Dfault value is once per hour
    persist_frequency: "${INTEGRATION_STATISTICS_PERSIST_FREQUENCY:3600000}"

storage:
  # Location of the folder to store data files
  data_folder_path: "${INTEGRATION_STORAGE_DATA_FOLDER_PATH:./}"
  # Max amount of data files to maintain
  max_file_count: "${INTEGRATION_STORAGE_MAX_FILE_COUNT:100}"
  # Max records per data file
  max_records_per_file: "${INTEGRATION_STORAGE_MAX_RECORDS_PER_FILE:30}"
  # Max records between persistence of data file
  max_records_between_fsync: "${INTEGRATION_STORAGE_MAX_RECORDS_BETWEEN_FSYNC:100}"
  # Size of the upload chunk
  max_read_records_count: "${INTEGRATION_STORAGE_MAX_READ_RECORDS_COUNT:50}"
  # Sleep interval while no new records
  no_read_records_sleep: "${INTEGRATION_STORAGE_NO_READ_RECORDS_SLEEP:1000}"

executors:
  # Size of the thread pool to handle incoming messages and tasks
  thread_pool_size: "${EXECUTORS_SIZE:1}"
  # Timeout to reconnect to SENTIENT
  reconnect_timeout: "${EXECUTORS_RECONNECT_TIMEOUT:3000}" # in milliseconds

rpc:
  # Host of the SENTIENT server
  host: "${RPC_HOST:sentient.cloud}"
  # Port of the SENTIENT server
  port: "${RPC_PORT:9090}"
  # No reply timeout
  timeout: "${RPC_TIMEOUT:5}" # Timeout in seconds for channel termination
  # ID of the RPC client
  client_id: "${RPC_CLIENT_ID:remote}"
  ssl:
    # SSL enabled/disabled
    enabled: "${RPC_SSL_ENABLED:false}"
    # SSL certificate
    cert: "${RPC_SSL_CERT:roots.pem}"

js:
  evaluator: "${JS_EVALUATOR:local}"
  # Built-in JVM JavaScript environment properties
  local:
    # Use Sandboxed (secured) JVM JavaScript environment
    use_js_sandbox: "${USE_LOCAL_JS_SANDBOX:true}"
    # Specify thread pool size for JavaScript sandbox resource monitor
    monitor_thread_pool_size: "${LOCAL_JS_SANDBOX_MONITOR_THREAD_POOL_SIZE:4}"
    # Maximum CPU time in milliseconds allowed for script execution
    max_cpu_time: "${LOCAL_JS_SANDBOX_MAX_CPU_TIME:5000}"
    # Maximum allowed JavaScript execution errors before JavaScript will be blacklisted
    max_errors: "${LOCAL_JS_SANDBOX_MAX_ERRORS:3}"

service:
  type: "${TB_SERVICE_TYPE:tb-integration}"
```  

- **Troubleshooting**

**NOTE** If you observe errors related to DNS issues, for example

```bash
127.0.1.1:53: cannot unmarshal DNS message
```

You may configure your system to use Google public DNS servers.
See corresponding [Linux](https://developers.google.com/speed/public-dns/docs/using#linux) and [Mac OS](https://developers.google.com/speed/public-dns/docs/using#mac_os) instructions.

### Docker on Windows

- **[Install Docker Toolbox for Windows](https://docker-docs.uclv.cu/toolbox/toolbox_install_windows/)**
- **Choose Integration to install**


<div class="st-tabs">

<div class="st-tab" data-label="HTTP Integrations(HTTP, Sigfox, ThingPark, OceanConnect and  T-Mobile IoT CDP)">

Windows users should use docker managed volume for remote integration logs. 
Create docker volume (for ex. `tb-http-integration-logs`) before executing docker run command:
Open "Docker Quickstart Terminal". Execute the following command to create docker volume:

``` 
docker volume create tb-pe-http-integration-logs
```


Execute the following command to run this docker directly:

```bash
docker run -it -v tb-pe-http-integration-logs:/var/log/tb-http-integration `
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" `
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" `
--name my-tb-pe-http-integration --restart always sentient/tb-pe-http-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-v tb-pe-http-integration-logs:/var/log/tb-http-integration`   - mounts the host's dir `~/.tb-pe-http-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-http-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-http-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-http-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-http-integration
```


To stop the container:

```
docker stop tb-pe-http-integration
```


To start the container:

```
docker start tb-pe-http-integration
```


</div>

<div class="st-tab" data-label="MQTT Integrations(MQTT, AWS IoT, IBM Watson, The Things Network)">

Windows users should use docker managed volume for remote integration logs. 
Create docker volume (for ex. `tb-mqtt-integration-logs`) before executing docker run command:
Open "Docker Quickstart Terminal". Execute the following command to create docker volume:

``` 
docker volume create tb-pe-mqtt-integration-logs
```

Execute the following command to run this docker directly:

```bash
docker run -it -v tb-pe-mqtt-integration-logs:/var/log/tb-mqtt-integration `
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" `
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" `
--name my-tb-pe-mqtt-integration --restart always sentient/tb-pe-mqtt-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-v tb-pe-mqtt-integration-logs:/var/log/tb-mqtt-integration`   - mounts the host's dir `~/.tb-pe-mqtt-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-mqtt-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-mqtt-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-mqtt-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-mqtt-integration
```


To stop the container:

```
docker stop tb-pe-mqtt-integration
```


To start the container:

```
docker start tb-pe-mqtt-integration
```


</div>

<div class="st-tab" data-label="AWS SQS Integration">

Windows users should use docker managed volume for remote integration logs. 
Create docker volume (for ex. `tb-aws-integration-logs`) before executing docker run command:
Open "Docker Quickstart Terminal". Execute the following command to create docker volume:

``` 
docker volume create tb-pe-aws-integration-logs
```


Execute the following command to run this docker directly:

```bash
docker run -it -v tb-pe-aws-integration-logs:/var/log/tb-aws-integration `
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" `
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" `
--name my-tb-pe-aws-integration --restart always sentient/tb-pe-aws-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-v tb-pe-aws-integration-logs:/var/log/tb-aws-integration`   - mounts the host's dir `~/.tb-pe-aws-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-aws-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-aws-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-aws-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-aws-integration
```


To stop the container:

```
docker stop tb-pe-aws-integration
```


To start the container:

```
docker start tb-pe-aws-integration
```


</div>

<div class="st-tab" data-label="Azure Event HubIntegration">

Windows users should use docker managed volume for remote integration logs. 
Create docker volume (for ex. `tb-azure-integration-logs`) before executing docker run command:
Open "Docker Quickstart Terminal". Execute the following command to create docker volume:

``` 
docker volume create tb-pe-azure-integration-logs
```


Execute the following command to run this docker directly:

```bash
docker run -it -v tb-pe-azure-integration-logs:/var/log/tb-azure-integration `
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" `
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" `
--name my-tb-pe-azure-integration --restart always sentient/tb-pe-azure-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-v tb-pe-azure-integration-logs:/var/log/tb-azure-integration`   - mounts the host's dir `~/.tb-pe-azure-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-azure-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-azure-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-azure-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-azure-integration
```


To stop the container:

```
docker stop tb-pe-azure-integration
```


To start the container:

```
docker start tb-pe-azure-integration
```


</div>

<div class="st-tab" data-label="OPC UA Integration">

Windows users should use docker managed volume for remote integration logs. 
Create docker volume (for ex. `tb-opc-ua-integration-logs`) before executing docker run command:
Open "Docker Quickstart Terminal". Execute the following command to create docker volume:

``` 
docker volume create tb-pe-opc-ua-integration-logs
```


Execute the following command to run this docker directly:

```bash
docker run -it -v tb-pe-opc-ua-integration-logs:/var/log/tb-opc-ua-integration `
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" `
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" `
--name my-tb-pe-opc-ua-integration --restart always sentient/tb-pe-opc-ua-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-v tb-pe-opc-ua-integration-logs:/var/log/tb-opc-ua-integration`   - mounts the host's dir `~/.tb-pe-opc-ua-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-opc-ua-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-opc-ua-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-opc-ua-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-opc-ua-integration
```


To stop the container:

```
docker stop tb-pe-opc-ua-integration
```


To start the container:

```
docker start tb-pe-opc-ua-integration
```


</div>

<div class="st-tab" data-label="TCP/UDP Integration">

Windows users should use docker managed volume for remote integration logs. 
Create docker volume (for ex. `tb-tcp-udp-integration-logs`) before executing docker run command:
Open "Docker Quickstart Terminal". Execute the following command to create docker volume:

``` 
docker volume create tb-pe-tcp-udp-integration-logs
```


Execute the following command to run this docker directly:

```bash
docker run -it -p 10560:10560 -v tb-pe-tcp-udp-integration-logs:/var/log/tb-tcp-udp-integration `
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" `
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" `
--name my-tb-pe-tcp-udp-integration --restart always sentient/tb-pe-tcp-udp-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-p 10560:10560` - connect local port 10560 to exposed internal 10560 port for the integration
- `-v tb-pe-tcp-udp-integration-logs:/var/log/tb-tcp-udp-integration`   - mounts the host's dir `~/.tb-pe-tcp-udp-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-tcp-udp-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-tcp-udp-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-tcp-udp-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-tcp-udp-integration
```


To stop the container:

```
docker stop tb-pe-tcp-udp-integration
```


To start the container:

```
docker start tb-pe-tcp-udp-integration
```


</div>

<div class="st-tab" data-label="CoAP Integration">

Windows users should use docker managed volume for remote integration logs. 
Create docker volume (for ex. `tb-coap-integration-logs`) before executing docker run command:
Open "Docker Quickstart Terminal". Execute the following command to create docker volume:

``` 
docker volume create tb-pe-coap-integration-logs
```


Execute the following command to run this docker directly:

```bash
docker run -it -p 5683:5683/udp -v tb-pe-coap-integration-logs:/var/log/tb-coap-integration `
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" `
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" `
--name my-tb-pe-coap-integration --restart always sentient/tb-pe-coap-integration:
```


Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-p 5683:5683/udp` - connect local udp port 5683 to exposed internal 5683 udp port for the integration.
- `-v tb-pe-coap-integration-logs:/var/log/tb-coap-integration`   - mounts the host's dir `~/.tb-pe-coap-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-coap-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-coap-integration:`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-coap-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


<div class="st-callout info">


You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.


</div>


- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-coap-integration
```


To stop the container:

```
docker stop tb-pe-coap-integration
```


To start the container:

```
docker start tb-pe-coap-integration
```


</div>

</div>


 - **Advanced configuration**

See configuration yml file below for a list of possible configuration parameters, corresponding environment variables and their default values.
For example, default client id of the integration, that is used in integration debug messages is *"remote"* and can be altered by setting *"RPC_CLIENT_ID"* environment variable.


```bash
server:
  # Server bind address
  address: "${HTTP_BIND_ADDRESS:0.0.0.0}"
  # Server bind port
  port: "${HTTP_BIND_PORT:8082}"

integration:
  routingKey: "${INTEGRATION_ROUTING_KEY:PUT_YOUR_ROUTING_KEY_HERE}"
  secret: "${INTEGRATION_SECRET:PUT_YOUR_SECRET_HERE}"
  # Allows connection to the localhost resources. For example, local MQTT broker, etc.
  allow_local_network_hosts: "${INTEGRATION_ALLOW_LOCAL_NETWORK_HOSTS:true}"
  statistics:
    # Enable/disable integration statistics
    enabled: "${INTEGRATION_STATISTICS_ENABLED:true}"
    # Send statistics interval. Dfault value is once per hour
    persist_frequency: "${INTEGRATION_STATISTICS_PERSIST_FREQUENCY:3600000}"

storage:
  # Location of the folder to store data files
  data_folder_path: "${INTEGRATION_STORAGE_DATA_FOLDER_PATH:./}"
  # Max amount of data files to maintain
  max_file_count: "${INTEGRATION_STORAGE_MAX_FILE_COUNT:100}"
  # Max records per data file
  max_records_per_file: "${INTEGRATION_STORAGE_MAX_RECORDS_PER_FILE:30}"
  # Max records between persistence of data file
  max_records_between_fsync: "${INTEGRATION_STORAGE_MAX_RECORDS_BETWEEN_FSYNC:100}"
  # Size of the upload chunk
  max_read_records_count: "${INTEGRATION_STORAGE_MAX_READ_RECORDS_COUNT:50}"
  # Sleep interval while no new records
  no_read_records_sleep: "${INTEGRATION_STORAGE_NO_READ_RECORDS_SLEEP:1000}"

executors:
  # Size of the thread pool to handle incoming messages and tasks
  thread_pool_size: "${EXECUTORS_SIZE:1}"
  # Timeout to reconnect to SENTIENT
  reconnect_timeout: "${EXECUTORS_RECONNECT_TIMEOUT:3000}" # in milliseconds

rpc:
  # Host of the SENTIENT server
  host: "${RPC_HOST:sentient.cloud}"
  # Port of the SENTIENT server
  port: "${RPC_PORT:9090}"
  # No reply timeout
  timeout: "${RPC_TIMEOUT:5}" # Timeout in seconds for channel termination
  # ID of the RPC client
  client_id: "${RPC_CLIENT_ID:remote}"
  ssl:
    # SSL enabled/disabled
    enabled: "${RPC_SSL_ENABLED:false}"
    # SSL certificate
    cert: "${RPC_SSL_CERT:roots.pem}"

js:
  evaluator: "${JS_EVALUATOR:local}"
  # Built-in JVM JavaScript environment properties
  local:
    # Use Sandboxed (secured) JVM JavaScript environment
    use_js_sandbox: "${USE_LOCAL_JS_SANDBOX:true}"
    # Specify thread pool size for JavaScript sandbox resource monitor
    monitor_thread_pool_size: "${LOCAL_JS_SANDBOX_MONITOR_THREAD_POOL_SIZE:4}"
    # Maximum CPU time in milliseconds allowed for script execution
    max_cpu_time: "${LOCAL_JS_SANDBOX_MAX_CPU_TIME:5000}"
    # Maximum allowed JavaScript execution errors before JavaScript will be blacklisted
    max_errors: "${LOCAL_JS_SANDBOX_MAX_ERRORS:3}"

service:
  type: "${TB_SERVICE_TYPE:tb-integration}"
```  

- **Troubleshooting**

**NOTE** If you observe errors related to DNS issues, for example

```bash
127.0.1.1:53: cannot unmarshal DNS message
```

You may configure your system to use [Google public DNS servers](https://developers.google.com/speed/public-dns/docs/using#windows)

### Ubuntu Server

 - Install Java 17 (OpenJDK) 

SENTIENT service is running on Java 17. To install OpenJDK 17, follow these instructions

```bash
sudo apt update && sudo apt install openjdk-17-jdk-headless
```


Configure your operating system to use **OpenJDK 17 by default**.
You can configure the default version by running the following command:

```bash
sudo update-alternatives --config java
```


To check the installed Java version on your system, use the following command:

```bash
java -version
```


The expected result is:

```
openjdk version "17.x.xx" 
OpenJDK Runtime Environment (...)
OpenJDK 64-Bit Server VM (...)
```


 - **Choose Integration package to install**
 


<div class="st-tabs">

<div class="st-tab" data-label="HTTP Integrations(HTTP, Sigfox, ThingPark, OceanConnect and  T-Mobile IoT CDP)">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-http-integration-.deb
```


Install integration as a service:

```bash
sudo dpkg -i tb-http-integration-.deb
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-http-integration/conf/tb-http-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start integration:

```bash
sudo service tb-http-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-http-integration/conf/tb-http-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-http-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="MQTT Integrations(MQTT, AWS IoT, IBM Watson, The Things Network)">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-mqtt-integration-.deb
```


Install integration as a service:

```bash
sudo dpkg -i tb-mqtt-integration-.deb
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-mqtt-integration/conf/tb-mqtt-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start integration:

```bash
sudo service tb-mqtt-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-mqtt-integration/conf/tb-mqtt-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-mqtt-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="AWS SQS Integration">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-aws-integration-.deb
```


Install integration as a service:

```bash
sudo dpkg -i tb-aws-integration-.deb
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-aws-integration/conf/tb-aws-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start integration:

```bash
sudo service tb-aws-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-aws-integration/conf/tb-aws-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-aws-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="Azure Event HubIntegration">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-azure-integration-.deb
```


Install integration as a service:

```bash
sudo dpkg -i tb-azure-integration-.deb
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-azure-integration/conf/tb-azure-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start integration:

```bash
sudo service tb-azure-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-azure-integration/conf/tb-azure-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-azure-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="OPC UA Integration">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-opc-ua-integration-.deb
```


Install integration as a service:

```bash
sudo dpkg -i tb-opc-ua-integration-.deb
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-opc-ua-integration/conf/tb-opc-ua-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start integration:

```bash
sudo service tb-opc-ua-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-opc-ua-integration/conf/tb-opc-ua-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-opc-ua-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="TCP/UDP Integration">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-tcp-udp-integration-.deb
```


Install integration as a service:

```bash
sudo dpkg -i tb-tcp-udp-integration-.deb
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-tcp-udp-integration/conf/tb-tcp-udp-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start integration:

```bash
sudo service tb-tcp-udp-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-tcp-udp-integration/conf/tb-tcp-udp-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-tcp-udp-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="CoAP Integration">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-coap-integration-.deb
```


Install integration as a service:

```bash
sudo dpkg -i tb-coap-integration-.deb
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-coap-integration/conf/tb-coap-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start integration:

```bash
sudo service tb-coap-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-coap-integration/conf/tb-coap-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-coap-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

</div>

 

### CentOS/RHEL Server

 - Install Java 17 (OpenJDK) 

SENTIENT service is running on Java 17. Follow this instructions to install OpenJDK 17:

```bash
sudo dnf install java-17-openjdk-headless
```


Please don't forget to configure your operating system to use OpenJDK 17 by default. 
You can configure which version is the default using the following command:

```bash
sudo update-alternatives --config java
```


You can check the installation using the following command:

```bash
java -version
```


Expected command output is:

```
openjdk version "17.x.xx"
OpenJDK Runtime Environment (...)
OpenJDK 64-Bit Server VM (build ...)
```


 - **Choose Integration package to install**
 


<div class="st-tabs">

<div class="st-tab" data-label="HTTP Integrations(HTTP, Sigfox, ThingPark, OceanConnect and  T-Mobile IoT CDP)">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-http-integration-.rpm
```


Install integration as a service:

```bash
sudo rpm -Uvh tb-http-integration-.rpm
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-http-integration/conf/tb-http-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start SENTIENT:

```bash
sudo service tb-http-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-http-integration/conf/tb-http-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-http-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="MQTT Integrations(MQTT, AWS IoT, IBM Watson, The Things Network)">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-mqtt-integration-.rpm
```


Install integration as a service:

```bash
sudo rpm -Uvh tb-mqtt-integration-.rpm
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-mqtt-integration/conf/tb-mqtt-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start SENTIENT:

```bash
sudo service tb-mqtt-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-mqtt-integration/conf/tb-mqtt-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-mqtt-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="AWS SQS Integration">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-aws-integration-.rpm
```


Install integration as a service:

```bash
sudo rpm -Uvh tb-aws-integration-.rpm
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-aws-integration/conf/tb-aws-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start SENTIENT:

```bash
sudo service tb-aws-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-aws-integration/conf/tb-aws-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-aws-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="Azure Event HubIntegration">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-azure-integration-.rpm
```


Install integration as a service:

```bash
sudo rpm -Uvh tb-azure-integration-.rpm
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-azure-integration/conf/tb-azure-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start SENTIENT:

```bash
sudo service tb-azure-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-azure-integration/conf/tb-azure-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-azure-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="OPC UA Integration">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-opc-ua-integration-.rpm
```


Install integration as a service:

```bash
sudo rpm -Uvh tb-opc-ua-integration-.rpm
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-opc-ua-integration/conf/tb-opc-ua-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start SENTIENT:

```bash
sudo service tb-opc-ua-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-opc-ua-integration/conf/tb-opc-ua-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-opc-ua-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="TCP/UDP Integration">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-tcp-udp-integration-.rpm
```


Install integration as a service:

```bash
sudo rpm -Uvh tb-tcp-udp-integration-.rpm
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-tcp-udp-integration/conf/tb-tcp-udp-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start SENTIENT:

```bash
sudo service tb-tcp-udp-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-tcp-udp-integration/conf/tb-tcp-udp-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-tcp-udp-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

<div class="st-tab" data-label="CoAP Integration">

Download installation package:

```bash
wget https://dist.sentient.invenia.in/tb-coap-integration-.rpm
```


Install integration as a service:

```bash
sudo rpm -Uvh tb-coap-integration-.rpm
```


Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-coap-integration/conf/tb-coap-integration.conf
``` 


Locate the following configuration block:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
# export RPC_HOST=sentient.cloud
# export RPC_PORT=9090
# export INTEGRATION_ROUTING_KEY=YOUR_INTEGRATION_KEY
# export INTEGRATION_SECRET=YOUR_INTEGRATION_SECRET
```

and put your configuration parameters. Please don't forget to uncomment the export statement. See example below:

```bash
# UNCOMMENT NEXT LINES AND PUT YOUR CONNECTION PARAMETERS:
export RPC_HOST=sentient.cloud
export RPC_PORT=9090
export INTEGRATION_ROUTING_KEY=b75**************************34d
export INTEGRATION_SECRET=vna**************mik
```

Execute the following command to start SENTIENT:

```bash
sudo service tb-coap-integration start
```


 - **Advanced configuration**

Once can lookup additional configuration parameters inside the yml configuration file.

Open the file for editing using the following command:

```bash 
sudo nano /etc/tb-coap-integration/conf/tb-coap-integration.conf
``` 
 

After executing this command you can open logs which are located here `/var/log/tb-coap-integration/`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.


</div>

</div>

 

## Remote integration configuration

Remote integration configuration is done via SENTIENT UI and there is no specific steps.
Explore guides and video tutorials related to specific integrations:

 - [HTTP](/docs/user-guide/integrations/http/)
 - [MQTT](/docs/user-guide/integrations/mqtt/)
 - [CoAP](/docs/user-guide/integrations/coap/)
 - [Kafka](/docs/user-guide/integrations/kafka/)
 - [OPC-UA](/docs/user-guide/integrations/opc-ua/)
 - [Actility ThingPark](/docs/user-guide/integrations/thingpark/)
 - [TheThingsStack](/docs/user-guide/integrations/ttn/)
 - [TheThingsIndustries](/docs/user-guide/integrations/tti/)
 - [KPN Things](/docs/user-guide/integrations/kpn-things/)
 - [LORIOT](/docs/user-guide/integrations/loriot/)
 - [ChirpStack](/docs/user-guide/integrations/chirpstack/)
 - [AWS IoT](/docs/user-guide/integrations/aws-iot/)
 - [AWS Kinesis](/docs/user-guide/integrations/aws-kinesis/)
 - [IBM Watson IoT](/docs/user-guide/integrations/ibm-watson-iot/)
 - [Azure Event Hub](/docs/user-guide/integrations/azure-event-hub/)
 - [Azure Service Bus](/docs/user-guide/integrations/azure-service-bus/)
 - [Azure IoT Hub](/docs/user-guide/integrations/azure-iot-hub/)
 - [SigFox](/docs/user-guide/integrations/sigfox/)
 - [OceanConnect](/docs/user-guide/integrations/ocean-connect/)
 - [TCP](/docs/user-guide/integrations/tcp/)
 - [UDP](/docs/user-guide/integrations/udp/)
 - [Tuya](/docs/user-guide/integrations/tuya/)
 - [Custom](/docs/user-guide/integrations/custom/)
  
## Remote integration troubleshooting

Please review the log files. Their location is specific to the platform and installation package you have used and is mentioned in the installation steps. 

## Next steps
