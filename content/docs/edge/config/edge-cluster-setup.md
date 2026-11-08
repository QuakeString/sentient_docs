+++
title = "Edge Cluster Setup"
description = "Detailed instructions on how to set up SENTIENT Edge in a cluster"

[extra]
status = "imported"
checked = ""
source = "docs/edge/config/edge-cluster-setup.md"
+++


### Overview

**Edge clustering** refers to connecting and grouping multiple **Edge nodes** to work together at the **edge of the network**. 
Clustering is useful for large-scale industrial IoT, smart cities, factories, or any scenario with thousands of devices in one region. 

Edge-specific considerations:
* All **Edge nodes** connect to the **same database**.
* **Devices** can connect to any node based on load balancing.
* **Edge nodes** share the workload and maintain local failover.
* The **Edge Cluster** syncs aggregated data to **SENTIENT Cloud**.

{{ diagram(name="edge-cluster") }}

For more details, see the [microservices architecture](/docs/reference/msa/) page.

#### Prerequisites

**SENTIENT** microservices run in a **Dockerized environment**. 
Before starting, make sure that [Docker CE](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/) are installed on your system.

Install Docker:
- [for Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [for CentOS](https://docs.docker.com/engine/install/centos/)
- [for MacOS (Docker Desktop)](https://docs.docker.com/desktop/setup/install/mac-install/)


<div class="st-callout warn">


**Don't forget to add your linux user to the docker group. See [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).**


</div>


### Step 1. Pull the SENTIENT Edge image

[Log in](https://docs.docker.com/engine/reference/commandline/login/) to Docker Hub and use the command to pull the image:


```bash
docker pull sentient/sentient-edge:
```


### Step 2. Clone the SENTIENT Edge CE repository

```bash
git clone -b release-4.0 https://github.com/sentient/sentient-gateway.git --depth 1
cd sentient-gateway/docker-edge
```


### Step 3. Configure SENTIENT Edge database and queue service

Before performing the initial installation, configure the type of database to be used with **SENTIENT Edge**. To set the database type, change the value of the **DATABASE** variable in the **environment file (.env)** file.

**SENTIENT Edge** currently supports two messaging systems/brokers for storing the messages:
* **In Memory** queue implementation is not suitable for any sort of cluster deployments.
* **Kafka** is recommended for production deployments and used by default. This queue is used on most of the SENTIENT production environments now.

To edit the **SENTIENT Edge .env** file, run the following command:
```bash
nano .env
```


Check the following lines:
```bash
DATABASE=postgres
SENTIENT_QUEUE_TYPE=kafka

CLOUD_ROUTING_KEY=PUT_YOUR_EDGE_KEY_HERE # e.g. 19ea7ee8-5e6d-e642-4f32-05440a529015
CLOUD_ROUTING_SECRET=PUT_YOUR_EDGE_SECRET_HERE # e.g. bztvkvfqsye7omv9uxlp
CLOUD_RPC_HOST=PUT_YOUR_SENTIENT_SERVER_DOMAIN_OR_IP_HERE # e.g. sentient.cloud
```


View the full **.env** file:
```liquid
# redis or redis-cluster or redis-sentinel
CACHE=redis

DOCKER_REPO=sentient
SENTIENT_EDGE_NODE_DOCKER_NAME=sentient-edge-node
SENTIENT_EDGE_VERSION=latest# Database used by SENTIENT, can be either postgres (PostgreSQL) or hybrid (PostgreSQL for entities database and Cassandra for timeseries database).
# According to the database type corresponding docker service will be deployed (see docker-compose.postgres.yml, docker-compose.hybrid.yml for details).

DATABASE=postgres
SENTIENT_QUEUE_TYPE=kafka

CLOUD_ROUTING_KEY=PUT_YOUR_EDGE_KEY_HERE # e.g. 19ea7ee8-5e6d-e642-4f32-05440a529015
CLOUD_ROUTING_SECRET=PUT_YOUR_EDGE_SECRET_HERE # e.g. bztvkvfqsye7omv9uxlp
CLOUD_RPC_HOST=PUT_YOUR_SENTIENT_SERVER_DOMAIN_OR_IP_HERE # e.g. sentient.cloud
CLOUD_RPC_PORT=7070LOAD_BALANCER_NAME=haproxy-certbot

# If enabled Prometheus and Grafana containers are deployed along with other containers
MONITORING_ENABLED=false

# Limit memory usage for each Java application
JAVA_OPTS="-Xmx2048M -Xms2048M -Xss384k -XX:+AlwaysPreTouch"
```


* **CACHE:** Set the cache type:
  * **redis:** Set the _redis_ value to use the Redis standalone cache (1 node - 1 master).
  * **redis-cluster:** Set the _redis-cluster_ value to use the Redis cluster cache (6 nodes - 3 masters, 3 slaves).
  * **redis-sentinel:** Set the _redis-sentinel_ value to use the Redis sentinel cache (3 nodes - 1 master, 1 slave, 1 sentinel).
* **DATABASE:** Replace the _database_ value with:
  * **postgres:** Set the _postgres_ value to use the **PostgreSQL** database.
  * **hybrid:** Set the _hybrid_ value to use the **PostgreSQL** database for the entities database and **Cassandra** for the time-series database.
* **SENTIENT_QUEUE_TYPE:** Use _kafka_ as the queue type. The _in-memory_ value is not valid for a cluster deployment.
* **CLOUD_ROUTING_KEY:** Put your edge key.
* **CLOUD_ROUTING_SECRET:** Put your edge secret.
* **CLOUD_RPC_HOST:** Use _sentient.cloud_ / _eu.sentient.cloud_ if you connect **Edge** to the [SENTIENT Cloud (North America)](https://sentient.cloud/signup)/[SENTIENT Cloud (Europe)](https://eu.sentient.cloud/signup) correspondingly, or an **IP address** of the machine with the **SENTIENT Professional Edition Platform**.
* **MONITORING_ENABLED:** To start cluster monitoring with [Grafana](https://grafana.com/) and/or [Prometheus](https://prometheus.io/) services, set the variable to _true_. 

  Learn how to **enable downlink messages monitoring** in this [article](/docs/edge/user-guide/troubleshooting/#downlink-messages-from-cloud-to-edge).


<div class="st-callout info">


Once deployed, you can reach **Prometheus** at [http://localhost:9090](http://localhost:9090) and **Grafana** at [http://localhost:3000](http://localhost:3000).
<br>The default credentials for local installation are:
* **Login:** admin 
* **Password:** foobar


</div>


### Step 4. Create and check required host volumes

Execute the following command to create log folders for the services and chown of these folders to the docker container users.
To be able to change user, **chown** command is used, which requires sudo permissions (script will request password for a sudo access):


<div class="st-callout warn">


For Docker Desktop users on MacOS, that utilize [Synchronized file shares feature](https://docs.docker.com/desktop/features/synchronized-file-sharing/) (enabled by default for `/Users` subdirectories):

Please note that you need to omit changing host volume ownership, since it is resolved automatically by virtualization engine.

Use `--skipChown` flag for both create and check scripts:

`./docker-create-log-folders.sh --skipChown`

`./docker-check-log-folders.sh --skipChown`


</div>


```bash
./docker-create-log-folders.sh
```


In order to check if all required volume folders are available and have correct ownership:
```bash
./docker-check-log-folders.sh
```


### Step 5. Install and run SENTIENT Edge

To run the installation, execute the following command:
```bash 
./docker-install.sh
```


To start the service, execute the following command:
```bash 
./docker-start-services.sh
```


<div class="st-callout info">


It will take a few minutes to start the services. Once all services are successfully started, open the **SENTIENT Edge** service
at **```http://{your-host-ip}```** in the browser (_e.g., [http://localhost](http://localhost)_).
To log in, use **the credentials** from the **SENTIENT** account.


</div>


Examine edge service logs for errors in case of any issues. To see **SENTIENT Edge** node logs, execute the following command:
```bash 
docker-compose logs -f sentient-edge1 sentient-edge2 sentient-edge3
```


To see the state of all the containers, use:
```bash
docker-compose ps
```


To inspect the logs of all running services, use:
```bash
docker-compose logs -f
```


See [docker-compose logs](https://docs.docker.com/compose/reference/logs/) command reference for details.

#### Stop and remove docker containers

To stop the services, use:

```bash
./docker-stop-services.sh
```


To stop and completely remove the deployed docker containers, run the command:

```bash
./docker-remove-services.sh
```


### Upgrading

To update a particular or all services (pull newer docker image and rebuild container):
```bash
./docker-update-service.sh [SERVICE...]
```


Where:
* **[SERVICE...]:** The list of services to update (defined in docker-compose configurations). If not specified, all services will be updated.

To upgrade the database, run the following commands:

```bash
./docker-stop-services.sh
./docker-upgrade.sh
./docker-start-services.sh
```


### Generate certificate for HTTPS
We use **HAproxy** to proxy traffic to containers, and for **Web UI** we use **80** and **443** ports by default. To use HTTPS with a valid certificate, run these commands:
```bash
docker exec haproxy-certbot certbot-certonly --domain your_domain --email your_email
docker exec haproxy-certbot haproxy-refresh
```


Valid certificate will only be used if you visit Web UI by domain in URL. 
If you are using IP address to access UI, this would use self-signed certificate.

### Next steps
