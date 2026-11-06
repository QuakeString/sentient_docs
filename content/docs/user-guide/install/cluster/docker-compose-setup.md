+++
title = "Cluster setup with Docker Compose"
description = "SENTIENT IoT platform cluster setup with Docker Compose guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/cluster/docker-compose-setup.md"
+++
This guide will help you to setup SENTIENT in cluster mode using Docker Compose tool. 

## Prerequisites

SENTIENT Microservices are running in dockerized environment.
Before starting please make sure Docker Engine and Docker Compose are installed in your system. 

Install Docker:
- [for Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [for CentOS](https://docs.docker.com/engine/install/centos/)
- [for MacOS (Docker Desktop)](https://docs.docker.com/desktop/setup/install/mac-install/)


<div class="st-callout warn">


**Don't forget to add your linux user to the docker group. See [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).**


</div>


## Step 1. Pull SENTIENT Images

Make sure your have [logged in](https://docs.docker.com/engine/reference/commandline/login/) to docker hub using command line.

```bash
docker pull sentient/tb-node:
docker pull sentient/tb-web-ui:
docker pull sentient/tb-js-executor:
docker pull sentient/tb-http-transport:
docker pull sentient/tb-mqtt-transport:
docker pull sentient/tb-coap-transport:
docker pull sentient/tb-lwm2m-transport:
docker pull sentient/tb-snmp-transport:
```

## Step 2. Review the architecture page

Starting SENTIENT v2.2, it is possible to install SENTIENT cluster using new microservices architecture and docker containers. 
See [**microservices**](/docs/reference/msa/) architecture page for more details.

## Step 3. Clone SENTIENT repository

```bash
git clone -b  https://github.com/sentient/sentient.git --depth 1
cd sentient/docker
```


## Step 4. Configure SENTIENT database

Before performing initial installation you can configure the type of database to be used with SENTIENT.
In order to set database type change the value of `DATABASE` variable in `.env` file: 

```bash
nano .env
```


to one of the following:

- `postgres` - use PostgreSQL database;
- `hybrid` - use PostgreSQL for entities database and Cassandra for time series database;

**NOTE**: According to the database type corresponding docker service will be deployed (see `docker-compose.postgres.yml`, `docker-compose.hybrid.yml` for details).

## Step 5. Choose SENTIENT queue service 

SENTIENT currently supports two messaging systems/brokers for storing the messages: In-memory and Kafka-based systems.

**In Memory** queue implementation is not suitable for any sort of cluster deployments.

* **Kafka** is recommended for production deployments and used by default. This queue is used on the most of SENTIENT production environments now.
  It is useful for both on-prem and private cloud deployments. It is also useful if you like to stay independent from your cloud provider.
  However, some providers also have managed services for Kafka. See AWS [MSK](https://aws.amazon.com/msk/) for example.

* **Confluent Cloud** is a fully managed streaming platform based on Kafka. Useful for a cloud agnostic deployments.

See corresponding architecture [page](/docs/reference/#message-queues-are-awesome) and rule engine [page](/docs/user-guide/rule-engine-2-5/queues/) for more details.


<div class="st-tabs">

<div class="st-tab" data-label="Kafka (default, recommended for on-prem, production installations)">

[Apache Kafka](https://kafka.apache.org/) is an open-source stream-processing software platform.

Configure SENTIENT environment file:

```
nano .env
```


Check following line:

```bash
TB_QUEUE_TYPE=kafka
```


</div>

<div class="st-tab" data-label="Confluent Cloud (Event Streaming Platform based on Kafka)">

#### Confluent Cloud Configuration

To access [Confluent Cloud](https://docs.confluent.io/current/platform.html#what-is-cp) 
you should first create an [account](https://confluent.cloud/login), 
then create a [Kafka cluster](https://docs.confluent.io/current/quickstart/cloud-quickstart/index.html#step-1-create-a-ak-cluster-in-ccloud) 
and get your [API Key](https://docs.confluent.io/current/quickstart/cloud-quickstart/index.html#step-4-create-an-api-key).


Configure SENTIENT environment file:

```
nano .env
```


Check following line:

```bash
TB_QUEUE_TYPE=confluent
```


Configure Confluent Cloud environment file for SENTIENT queue service:

```
nano queue-confluent-cloud.env
```


Don’t forget to replace "CLUSTER_API_KEY", "CLUSTER_API_SECRET" and "confluent.cloud:9092" with your real Confluent Cloud bootstrap servers:

```bash
TB_QUEUE_TYPE=kafka

TB_KAFKA_SERVERS=confluent.cloud:9092
TB_QUEUE_KAFKA_REPLICATION_FACTOR=3

TB_QUEUE_KAFKA_USE_CONFLUENT_CLOUD=true
TB_QUEUE_KAFKA_CONFLUENT_SSL_ALGORITHM=https
TB_QUEUE_KAFKA_CONFLUENT_SASL_MECHANISM=PLAIN
TB_QUEUE_KAFKA_CONFLUENT_SASL_JAAS_CONFIG='org.apache.kafka.common.security.plain.PlainLoginModule required username="CLUSTER_API_KEY" password="CLUSTER_API_SECRET";'
TB_QUEUE_KAFKA_CONFLUENT_SECURITY_PROTOCOL=SASL_SSL
TB_QUEUE_KAFKA_CONFLUENT_USERNAME=CLUSTER_API_KEY
TB_QUEUE_KAFKA_CONFLUENT_PASSWORD=CLUSTER_API_SECRET

TB_QUEUE_KAFKA_RE_TOPIC_PROPERTIES=retention.ms:604800000;segment.bytes:52428800;retention.bytes:1048576000
TB_QUEUE_KAFKA_CORE_TOPIC_PROPERTIES=retention.ms:604800000;segment.bytes:52428800;retention.bytes:1048576000
TB_QUEUE_KAFKA_TA_TOPIC_PROPERTIES=retention.ms:604800000;segment.bytes:52428800;retention.bytes:1048576000
TB_QUEUE_KAFKA_NOTIFICATIONS_TOPIC_PROPERTIES=retention.ms:604800000;segment.bytes:52428800;retention.bytes:1048576000
TB_QUEUE_KAFKA_JE_TOPIC_PROPERTIES=retention.ms:604800000;segment.bytes:52428800;retention.bytes:104857600

# These params affect the number of requests per second from each partitions per each queue.
# Number of requests to particular Message Queue is calculated based on the formula:
# ((Number of Rule Engine and Core Queues) * (Number of partitions per Queue) + (Number of transport queues)
#  + (Number of microservices) + (Number of JS executors)) * 1000 / POLL_INTERVAL_MS
# For example, number of requests based on default parameters is:

# Rule Engine queues:
# Main 10 partitions + HighPriority 10 partitions + SequentialByOriginator 10 partitions = 30
# Core queue 10 partitions
# Transport request Queue + response Queue = 2
# Rule Engine Transport notifications Queue + Core Transport notifications Queue = 2
# Total = 44
# Number of requests per second = 44 * 1000 / 25 = 1760 requests

# Based on the use case, you can compromise latency and decrease number of partitions/requests to the queue, if the message load is low.
# By UI set the parameters - interval (1000) and partitions (1) for Rule Engine queues.
# Sample parameters to fit into 10 requests per second on a "monolith" deployment: 

TB_QUEUE_CORE_POLL_INTERVAL_MS=1000
TB_QUEUE_CORE_PARTITIONS=2
TB_QUEUE_RULE_ENGINE_POLL_INTERVAL_MS=1000
TB_QUEUE_TRANSPORT_REQUEST_POLL_INTERVAL_MS=1000
TB_QUEUE_TRANSPORT_RESPONSE_POLL_INTERVAL_MS=1000
TB_QUEUE_TRANSPORT_NOTIFICATIONS_POLL_INTERVAL_MS=1000
TB_QUEUE_VC_INTERVAL_MS=1000
TB_QUEUE_VC_PARTITIONS=1
```


You can update default Rule Engine queues configuration using UI. More about SENTIENT Rule Engine queues see in [documentation](/docs/user-guide/rule-engine-2-5/queues/).


</div>

</div>

 

## Step 6. Enable monitoring (optional)

In order to start cluster monitoring - Grafana and Prometheus services, please edit configuration file:

```bash
nano .env
```


You'll need to make sure that `MONITORING_ENABLED` variable set to `true`:

```bash
MONITORING_ENABLED=true
```

After deployment, you will be able to reach Prometheus at `http://localhost:9090` and Grafana at `http://localhost:3000` (default login is `admin` and password `foobar`).

## Step 7. Running

### Create and check required host volumes
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


### Install and run SENTIENT

Execute the following command to run installation:

```bash
./docker-install-tb.sh --loadDemo
```


Where:

- `--loadDemo` - optional argument. Whether to load additional demo data.

Execute the following command to start services:

```bash
./docker-start-services.sh
```


After a while when all services will be successfully started you can open `http://{your-host-ip}` in you browser (for ex. `http://localhost`).
You should see SENTIENT login page.

Use the following default credentials:

- **System Administrator**: sysadmin@sentient.org / sysadmin

If you installed DataBase with demo data (using `--loadDemo` flag) you can also use the following credentials:

- **Tenant Administrator**: tenant@sentient.org / tenant
- **Customer User**: customer@sentient.org / customer

In case of any issues you can examine service logs for errors.
For example to see SENTIENT node logs execute the following command:

```bash
docker compose logs -f tb-core1 tb-rule-engine1
```


<div class="st-callout info">


If you still rely on Docker Compose as docker-compose (with a hyphen) execute next command:

**docker-compose logs -f tb-core1 tb-rule-engine1**


</div>


Or use the following command to see the state of all the containers:

```bash
docker compose ps
```


<div class="st-callout info">


If you still rely on Docker Compose as docker-compose (with a hyphen) execute next command:

**docker-compose ps**


</div>


Use the following command to inspect the logs of all running services:

```bash
docker compose logs -f
```


<div class="st-callout info">


If you still rely on Docker Compose as docker-compose (with a hyphen) execute next command:

**docker-compose logs -f**


</div>


See [docker-compose logs](https://docs.docker.com/compose/reference/logs/) command reference for details.

Execute the following command to stop services:

```bash
./docker-stop-services.sh
```


Execute the following command to stop and completely remove deployed docker containers:

```bash
./docker-remove-services.sh
```


Execute the following command to update particular or all services (pull newer docker image and rebuild container):

```bash
./docker-update-service.sh [SERVICE...]
```


Where:

- `[SERVICE...]` - list of services to update (defined in docker-compose configurations). If not specified all services will be updated.


## Post-installation steps

### Generate certificate for HTTPS
We using HAproxy for proxying traffic to containers and for web UI by default we using 80 and 443 ports. For using HTTPS with a valid certificate, execute these commands:
```
docker exec haproxy-certbot certbot-certonly --domain your_domain --email your_email
docker exec haproxy-certbot haproxy-refresh
```

**NOTE**: Valid certificate used only, when you visit web UI by domain in URL. If you using IP address for access to UI, this would be used self-signed certificate. 

### Upgrading to new SENTIENT version

**Keep Your Platform Secure and Up-to-Date**

When a new SENTIENT release becomes available, we provide a streamlined update process to ensure your system benefits from the latest features and security patches without any risk to your data.


<div class="st-callout info">


**To maintain database integrity and system stability, please perform upgrades sequentially (e.g., v4.0.2 → v4.1.0 → v4.2.0).**


</div>


Please refer to our official <a href="/docs/user-guide/install/upgrade-instructions/">Upgrade Instructions</a> for detailed steps tailored to your current deployment environment.


## Next steps
