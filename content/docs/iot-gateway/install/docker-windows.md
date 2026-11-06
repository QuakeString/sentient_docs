+++
title = "Install SENTIENT IoT Gateway using Docker"
aliases = ["/docs/iot-gateway/install/windows/"]

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/install/docker-windows.md"
+++
This guide will help you to install and start SENTIENT IoT Gateway using Docker on Windows.

## Prerequisites

- [Install Docker Compose for Windows](https://docs.docker.com/desktop/setup/install/windows-install/);
- You will need to have access to SENTIENT. The easiest way is to use [SENTIENT Cloud](https://sentient.invenia.in/installations/).
The alternative option is to install the SENTIENT locally using the [installation guide](https://sentient.invenia.in/docs/user-guide/install/installation-options/).

## Download a docker-compose file


1. Go to the "**Entities**" > "**Gateways**" page and click the "**plus**" icon in the upper right corner to add a new gateway.

1. In the opened modal window input the gateway name, specify the "**default**" device profile, and click "**Create**".

1. The "**Launch command**" window will open. Click the "**Download**" button to download a docker-compose file for your gateway.


<div class="st-gallery"><figure><img src="/images/gateway/install/gateway-download-configuration-file-1-ce.webp" alt="Go to the &quot;**Entities**&quot; > &quot;**Gateways**&quot; page and click the &quot;**plus**&quot; icon in the upper right corner to add a new gateway." loading="lazy"><figcaption>Go to the "**Entities**" > "**Gateways**" page and click the "**plus**" icon in the upper right corner to add a new gateway.</figcaption></figure><figure><img src="/images/gateway/install/gateway-download-configuration-file-2-ce.webp" alt="In the opened modal window input the gateway name, specify the &quot;**default**&quot; device profile, and click &quot;**Create**&quot;." loading="lazy"><figcaption>In the opened modal window input the gateway name, specify the "**default**" device profile, and click "**Create**".</figcaption></figure><figure><img src="/images/gateway/install/gateway-download-configuration-file-3-ce.webp" alt="The &quot;**Launch command**&quot; window will open. Click the &quot;**Download**&quot; button to download a docker-compose file for your gateway." loading="lazy"><figcaption>The "**Launch command**" window will open. Click the "**Download**" button to download a docker-compose file for your gateway.</figcaption></figure></div>


## Running

Click the **Docker QuickStart** icon to launch a pre-configured **Docker Toolbox** terminal.

Make sure your have [logged in](https://docs.docker.com/engine/reference/commandline/login/) to docker hub.
Start the Gateway by executing the following command from the folder containing the **docker-compose.yml** file in the command line as administrator:

```
docker compose up
```


<div class="st-gallery"><figure><img src="/images/gateway/install/start-gateway-windows-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Detaching commands

To detach from session (the container will keep running in the background) execute the following command:

```
docker compose up -d
```


To reattach to the command line (to look at Gateway logs) execute the following command:

```
docker attach tb-gateway
```


## Upgrading

In order to update to the latest image, execute the following commands:

```
docker compose down
docker pull sentient/tb-gateway
docker compose up
```


## Next steps

Explore guides related to main SENTIENT features:

 - [Getting Started](/docs/iot-gateway/getting-started/) with SENTIENT IoT Gateway.
 - [Data Visualization](/docs/user-guide/visualization/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine/) - how to use rule engine to analyze data from devices.
