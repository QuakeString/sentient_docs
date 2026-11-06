+++
title = "Installing SENTIENT using Docker (Windows)"
description = "Installing SENTIENT IoT Platform using Docker (Windows)"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/docker-windows.md"
+++
This guide will help you to install and start SENTIENT using Docker on Windows.


## Prerequisites

- [Install Docker Toolbox for Windows](https://docker-docs.uclv.cu/toolbox/toolbox_install_windows/)

## Running

Running this image requires a server with at least 4GB of RAM (8GB is recommended) and minimum load (few messages per second).

## Choose SENTIENT queue service

SENTIENT platform currently supports two type of messaging brokers for storing the messages and communication between SENTIENT services: In-memory and Kafka-based brokers.
 
 * **In Memory** queue implementation is built-in and default. 
It is useful for development(PoC) environments and is not suitable for production deployments or any sort of cluster deployments.

 * **Kafka** is recommended for production deployments. This queue is used on the most of SENTIENT production environments now. 
It is useful for both on-prem and private cloud deployments. It is also useful if you like to stay independent from your cloud provider.
However, some providers also have managed services for Kafka. See AWS [MSK](https://aws.amazon.com/msk/) for example.

* **Confluent Cloud** is a fully managed streaming platform based on Kafka. Useful for a cloud agnostic deployments.

See corresponding architecture [page](/docs/reference/#message-queues-are-awesome) and rule engine [page](/docs/user-guide/rule-engine-2-5/queues/) for more details.


<div class="st-tabs">

<div class="st-tab" data-label="In Memory (built-in and default)">

**SENTIENT includes In Memory Queue service and use it by default without extra settings.**

Create docker compose file for SENTIENT queue service:

```
notepad docker-compose.yml
```


Add the following lines to the yml file:

```yml
services:
  postgres:
    restart: always
    image: "postgres:16"
    ports:
      - "5432"
    environment:
      POSTGRES_DB: sentient
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres-data:/var/lib/postgresql/data
  sentient-ce:
    restart: always
    image: "sentient/tb-node:"
    ports:
      - "8080:8080"
      - "7070:7070"
      - "1883:1883"
      - "8883:8883"
      - "5683-5688:5683-5688/udp"
    logging:
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "10"
    environment:
      TB_SERVICE_ID: tb-ce-node
      SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/sentient
    depends_on:
      - postgres

volumes:
  postgres-data:
    name: tb-postgres-data
    driver: local
```


</div>

<div class="st-tab" data-label="Kafka (recommended for on-prem, production installations)">


[Apache Kafka](https://kafka.apache.org/) is an open-source stream-processing software platform.

Create docker compose file for SENTIENT queue service:

```
notepad docker-compose.yml
```


Add the following lines to the yml file.

```yml
services:
  postgres:
    restart: always
    image: "postgres:16"
    ports:
      - "5432"
    environment:
      POSTGRES_DB: sentient
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres-data:/var/lib/postgresql/data
  kafka:
    restart: always
    image: bitnamilegacy/kafka:4.0
    ports:
      - 9092:9092 #to localhost:9092 from host machine
      - 9093 #for Kraft
    environment:
      ALLOW_PLAINTEXT_LISTENER: "yes"
      KAFKA_CFG_LISTENERS: "PLAINTEXT://:9092,CONTROLLER://:9093"
      KAFKA_CFG_ADVERTISED_LISTENERS: "PLAINTEXT://:9092"
      KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP: "CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT"
      KAFKA_CFG_INTER_BROKER_LISTENER_NAME: "PLAINTEXT"
      KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE: "false"
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: "1"
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: "1"
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: "1"
      KAFKA_CFG_PROCESS_ROLES: "controller,broker" #KRaft
      KAFKA_CFG_NODE_ID: "0" #KRaft
      KAFKA_CFG_CONTROLLER_LISTENER_NAMES: "CONTROLLER" #KRaft
      KAFKA_CFG_CONTROLLER_QUORUM_VOTERS: "0@kafka:9093" #KRaft
      KAFKA_CFG_LOG_RETENTION_MS: "300000"
      KAFKA_CFG_SEGMENT_BYTES: "26214400"
    volumes:
      - kafka-data:/bitnami
  sentient-ce:
    restart: always
    image: "sentient/tb-node:"
    ports:
      - "8080:8080"
      - "7070:7070"
      - "1883:1883"
      - "8883:8883"
      - "5683-5688:5683-5688/udp"
    logging:
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "10"
    environment:
      TB_SERVICE_ID: tb-ce-node
      SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/sentient
      TB_QUEUE_TYPE: kafka
      TB_KAFKA_SERVERS: kafka:9092
    depends_on:
      - postgres
      - kafka

volumes:
  postgres-data:
    name: tb-postgres-data
    driver: local
  kafka-data:
    name: tb-ce-kafka-data
    driver: local

```


</div>

<div class="st-tab" data-label="Confluent Cloud (Event Streaming Platform based on Kafka)">

#### Confluent Cloud Configuration

To access [Confluent Cloud](https://docs.confluent.io/current/platform.html#what-is-cp) 
you should first create an [account](https://confluent.cloud/login), 
then create a [Kafka cluster](https://docs.confluent.io/current/quickstart/cloud-quickstart/index.html#step-1-create-a-ak-cluster-in-ccloud) 
and get your [API Key](https://docs.confluent.io/current/quickstart/cloud-quickstart/index.html#step-4-create-an-api-key).


Create docker compose file for SENTIENT queue service:

```
notepad docker-compose.yml
```


Add the following line to the yml file. Don’t forget to replace “CLUSTER_API_KEY”, "CLUSTER_API_SECRET" and "localhost:9092" with your real Confluent Cloud bootstrap servers:

```yml
services:
  postgres:
    restart: always
    image: "postgres:16"
    ports:
      - "5432"
    environment:
      POSTGRES_DB: sentient
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres-data:/var/lib/postgresql/data
  sentient-ce:
    restart: always
    image: "sentient/tb-node:"
    ports:
      - "8080:8080"
      - "7070:7070"
      - "1883:1883"
      - "8883:8883"
      - "5683-5688:5683-5688/udp"
    logging:
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "10"
    environment:
      TB_SERVICE_ID: tb-ce-node
      SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/sentient
      TB_QUEUE_TYPE: kafka
      TB_KAFKA_SERVERS: localhost:9092
      TB_QUEUE_KAFKA_REPLICATION_FACTOR: 3
      TB_QUEUE_KAFKA_USE_CONFLUENT_CLOUD: true
      TB_QUEUE_KAFKA_CONFLUENT_SASL_JAAS_CONFIG: 'org.apache.kafka.common.security.plain.PlainLoginModule required username="CLUSTER_API_KEY" password="CLUSTER_API_SECRET";'
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
      # 
      # Based on the use case, you can compromise latency and decrease number of partitions/requests to the queue, if the message load is low.
      # By UI set the parameters - interval (1000) and partitions (1) for Rule Engine queues.
      # Sample parameters to fit into 10 requests per second on a "monolith" deployment: 
      TB_QUEUE_CORE_POLL_INTERVAL_MS: 1000
      TB_QUEUE_CORE_PARTITIONS: 2
      TB_QUEUE_RULE_ENGINE_POLL_INTERVAL_MS: 1000
      TB_QUEUE_TRANSPORT_REQUEST_POLL_INTERVAL_MS: 1000
      TB_QUEUE_TRANSPORT_RESPONSE_POLL_INTERVAL_MS: 1000
      TB_QUEUE_TRANSPORT_NOTIFICATIONS_POLL_INTERVAL_MS: 1000
      TB_QUEUE_VC_INTERVAL_MS: 1000
      TB_QUEUE_VC_PARTITIONS: 1      
    depends_on:
      - postgres

volumes:
  postgres-data:
    name: tb-postgres-data
    driver: local
```


You can update default Rule Engine queues configuration using UI. More about SENTIENT Rule Engine queues see in [documentation](/docs/user-guide/rule-engine-2-5/queues/).


</div>

</div>

 

here: 

- `8080:8080`            - connect local port 8080 to exposed internal HTTP port 8080
- `1883:1883`            - connect local port 1883 to exposed internal MQTT port 1883
- `8883:8883`            - connect local port 8883 to exposed internal MQTT over SSL port 8883
- `7070:7070`            - connect local port 7070 to exposed internal Edge RPC port 7070
- `5683-5688:5683-5688/udp`            - connect local UDP ports 5683-5688 to exposed internal COAP and LwM2M ports
- `tb-postgres-data` - name of the docker volume that stores the PostgreSQL's data
- `sentient-ce`             - friendly local name of the SENTIENT container
- `restart: always`        - automatically start SENTIENT in case of system reboot and restart in case of failure.
- `image: "sentient/tb-node:"`          - SENTIENT docker image and version.


## Initialize database schema & system assets

Before you start SENTIENT, initialize the database schema and load built-in assets by running:   

```bash
docker compose run --rm -e INSTALL_TB=true -e LOAD_DEMO=true sentient-ce
```

Environment variables:

- `INSTALL_TB=true` - Installs the core database schema and system resources (widgets, images, rule chains, etc.).
- `LOAD_DEMO=true` - Loads sample tenant account, dashboards and devices for evaluation and testing.

## Start the platform & tail logs

Bring up all containers in detached mode, then follow the SENTIENT logs (use PowerShell for the command below):

```bash
docker compose up -d; docker compose logs -f sentient-ce
```

After executing this command you can open `http://{your-host-ip}:8080` in you browser (for ex. `http://localhost:8080`). You should see SENTIENT login page.
Use the following default credentials:

- **System Administrator**: sysadmin@sentient.org / sysadmin
- **Tenant Administrator**: tenant@sentient.org / tenant
- **Customer User**: customer@sentient.org / customer
    
You can always change passwords for each account in account profile page.

You can safely detach from the log stream (e.g. Ctrl+C); containers will continue running.

## Inspect logs & control container lifecycle

If something goes wrong, you can stream the SENTIENT container logs in real time:

```bash
docker compose logs -f sentient-ce
```

Bring down every container defined in your Compose file:

```bash
docker compose down
```

Launch all services in detached mode:

```bash
docker compose up -d
```

## Post-installation steps

### Upgrading to new SENTIENT version

**Keep Your Platform Secure and Up-to-Date**

When a new SENTIENT release becomes available, we provide a streamlined update process to ensure your system benefits from the latest features and security patches without any risk to your data.


<div class="st-callout info">


**To maintain database integrity and system stability, please perform upgrades sequentially (e.g., v4.0.2 → v4.1.0 → v4.2.0).**


</div>


Please refer to our official <a href="/docs/user-guide/install/upgrade-instructions/">Upgrade Instructions</a> for detailed steps tailored to your current deployment environment.


## Troubleshooting

### DNS issues

**NOTE** If you observe errors related to DNS issues, for example

```bash
127.0.1.1:53: cannot unmarshal DNS message
```

You may configure your system to use [Google public DNS servers](https://developers.google.com/speed/public-dns/docs/using#windows)

## Next steps
