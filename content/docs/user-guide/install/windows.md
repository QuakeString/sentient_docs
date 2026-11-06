+++
title = "Installing SENTIENT on Windows"
description = "Installing SENTIENT on Windows"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/windows.md"
+++
<div class="st-callout warn">


**Please consider to use Linux installation option, because Linux is the most stable platform for running SENTIENT. Windows installation will be deprecated in the future. You can find Linux installation guides on [Installation Guide](/docs/user-guide/install/installation-options/) page**.


</div>


## Prerequisites

This guide describes how to install SENTIENT on a Windows machine.
Instructions below are provided for Windows 11/10. 
Hardware requirements depend on chosen database and amount of devices connected to the system. 
To run SENTIENT and PostgreSQL on a single machine you will need at least 4Gb of RAM.
To run SENTIENT and Cassandra on a single machine you will need at least 8Gb of RAM.

## Step 1. Install Java 17 (OpenJDK) 

SENTIENT service is running on Java 17. Follow this instructions to install OpenJDK 17.

 * Visit [Open JDK Download Page](https://adoptium.net). Go to "Other platforms and versions", select "Operating System" as "Windows", "Architecture" as "x64", "Version" as "17 - LTS" and download **JDK .msi** package. 
 * Run the downloaded MSI package and follow the instructions. 
 Make sure you have selected "**Add to PATH**" and "**Set JAVA_HOME variable**" options to "Will be installed on local hard drive" state.
 * Visit [PostgreSQL JDBC Download Page](https://jdbc.postgresql.org/download/) to download PostgreSQL JDBC Driver. Choose the latest available option.
 * Create the folder **C:\Program Files\JDBC** and copy downloaded file there. Then, add a new global variable - run PowerShell as an administrator and execute the following command. Do not forget to change "postgresql-42.2.18.jar" in the command to match the downloaded version.
 ```powershell
[System.Environment]::SetEnvironmentVariable("CLASSPATH", '.;"C:\Program Files\JDBC\postgresql-42.2.18.jar"', [System.EnvironmentVariableTarget]::Machine)
```


You can check the installation using the following command (using Command Prompt):

```bash
java -version
```


Expected command output is:

```
C:\Users\User>java -version
openjdk version "17.x.xx" 
OpenJDK Runtime Environment Temurin-17.x.xx (...)
OpenJDK 64-Bit Server VM Temurin-17.x.xx (...)
```


## Step 2. SENTIENT service installation

Download and extract the package.

```bash
https://github.com/sentient/sentient/releases/download//sentient-windows-.zip
```


**Note:** We assume you have extracted SENTIENT package to default location: *C:\Program Files (x86)\sentient*  

## Step 3. Configure SENTIENT database

SENTIENT is able to use SQL or hybrid database approach. See corresponding architecture [page](/docs/reference/#sql-vs-nosql-vs-hybrid-database-approach) for more details.  


<div class="st-tabs">

<div class="st-tab" data-label="PostgreSQL (recommended for ">


<div class="st-callout info">


SENTIENT team recommends to use PostgreSQL for development and production environments with reasonable load (< 5000 msg/sec).
Many cloud vendors support managed PostgreSQL servers which is a cost-effective solution for most of SENTIENT instances.


</div>


##### PostgreSQL Installation

Download the installation file (PostgreSQL 15 or newer releases) [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows) and follow the installation instructions.

During PostgreSQL installation, you will be prompted for superuser (postgres) password.
Don't forget this password. It will be used later. For simplicity, we will substitute it with "postgres".

##### Create SENTIENT Database

Once installed, launch the "pgAdmin" software and login as superuser (postgres). 
Open your server and create database "sentient" with owner "postgres".

##### SENTIENT Configuration

In case you have specified the PostgreSQL superuser password as "postgres", you can skip this step. 

Open the Notepad or other editor as administrator user (right click on the app icon and select "Run as administrator").  
Open the following file for editing (select "All Files" instead of "Text Documents" in file choosing dialog, the encoding is UTF-8):

```
C:\Program Files (x86)\sentient\conf\sentient.yml
``` 


and locate "# SQL DAO Configuration" block. Don't forget to replace "postgres" with your real postgres user password:

```yml
# SQL DAO Configuration
spring:
  data:
    jpa:
      repositories:
        enabled: "true"
  jpa:
    open-in-view: "false"
    hibernate:
      ddl-auto: "none"
  datasource:
    driverClassName: "${SPRING_DRIVER_CLASS_NAME:org.postgresql.Driver}"
    url: "${SPRING_DATASOURCE_URL:jdbc:postgresql://localhost:5432/sentient}"
    username: "${SPRING_DATASOURCE_USERNAME:postgres}"
    password: "${SPRING_DATASOURCE_PASSWORD:YOUR_POSTGRES_PASSWORD_HERE}"
    hikari:
      maximumPoolSize: "${SPRING_DATASOURCE_MAXIMUM_POOL_SIZE:16}"
``` 


locate "SQL_POSTGRES_TS_KV_PARTITIONING" parameter in order to override the default value for timestamp key-value storage partitioning size:

```yml
    sql:
      postgres:
        # Specify partitioning size for timestamp key-value storage. Example: DAYS, MONTHS, YEARS, INDEFINITE.
        ts_key_value_partitioning: "${SQL_POSTGRES_TS_KV_PARTITIONING:MONTHS}"
```

</div>

</div>

 

## Step 4. Choose SENTIENT queue service

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

**In Memory** queue is built in and enabled by default. No additional configuration is required.

</div>

<div class="st-tab" data-label="Kafka (recommended for on-prem, production installations)">

#### Kafka Installation

[Apache Kafka](https://kafka.apache.org/) is an open-source stream-processing software platform.

##### Install Kafka

Use the instructions below for installing Kafka in a Docker container.

```
nano docker-compose-kafka.yml
```


Add the following lines to the docker-compose-kafka.yml file:
```yml
services:
  kafka:
    restart: always
    image: bitnamilegacy/kafka:4.0
    ports:
      - 9092:9092 #to localhost:9092 from host machine
      - 9093 #for Kraft
      - 9094 #to kafka:9094 from within Docker network
    environment:
      ALLOW_PLAINTEXT_LISTENER: "yes"
      KAFKA_CFG_LISTENERS: "OUTSIDE://:9092,CONTROLLER://:9093,INSIDE://:9094"
      KAFKA_CFG_ADVERTISED_LISTENERS: "OUTSIDE://localhost:9092,INSIDE://kafka:9094"
      KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP: "INSIDE:PLAINTEXT,OUTSIDE:PLAINTEXT,CONTROLLER:PLAINTEXT"
      KAFKA_CFG_INTER_BROKER_LISTENER_NAME: "INSIDE"
      KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE: "false"
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: "1"
      KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: "1"
      KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: "1"
      KAFKA_CFG_PROCESS_ROLES: "controller,broker" #KRaft
      KAFKA_CFG_NODE_ID: "0" #KRaft
      KAFKA_CFG_CONTROLLER_LISTENER_NAMES: "CONTROLLER" #KRaft
      KAFKA_CFG_CONTROLLER_QUORUM_VOTERS: "0@kafka:9093" #KRaft
    volumes:
      - kafka-data:/bitnami
volumes:
  kafka-data:
    driver: local
```


Start the container:
```
docker compose -f docker-compose-kafka.yml up -d
```


##### SENTIENT Configuration

Open the Notepad or other editor as administrator user (right click on the app icon and select "Run as administrator").  
Open the following file for editing (select "All Files" instead of "Text Documents" in file choosing dialog, the encoding is UTF-8):

```
C:\Program Files (x86)\sentient\conf\sentient.yml
``` 


and locate "queue:" block. Make sure the queue type is "kafka", and **don't forget** to replace "localhost:9092" with your real Kafka bootstrap servers:

```yml
queue:
  type: "${TB_QUEUE_TYPE:kafka}"
...
  kafka:
    bootstrap.servers: "${TB_KAFKA_SERVERS:localhost:9092}"
    acks: "${TB_KAFKA_ACKS:all}"
    retries: "${TB_KAFKA_RETRIES:1}"
    batch.size: "${TB_KAFKA_BATCH_SIZE:16384}"
    linger.ms: "${TB_KAFKA_LINGER_MS:1}"
    buffer.memory: "${TB_BUFFER_MEMORY:33554432}"
    replication_factor: "${TB_QUEUE_KAFKA_REPLICATION_FACTOR:1}"
```


</div>

<div class="st-tab" data-label="Confluent Cloud (Event Streaming Platform based on Kafka)">

#### Confluent Cloud Configuration

To access [Confluent Cloud](https://docs.confluent.io/current/platform.html#what-is-cp) 
you should first create an [account](https://confluent.cloud/login), 
then create a [Kafka cluster](https://docs.confluent.io/current/quickstart/cloud-quickstart/index.html#step-1-create-a-ak-cluster-in-ccloud) 
and get your [API Key](https://docs.confluent.io/current/quickstart/cloud-quickstart/index.html#step-4-create-an-api-key).


##### SENTIENT Configuration

Open the Notepad or other editor as administrator user (right click on the app icon and select "Run as administrator").  
Open the following file for editing (select "All Files" instead of "Text Documents" in file choosing dialog, the encoding is UTF-8):

```
C:\Program Files (x86)\sentient\conf\sentient.yml
``` 


and locate "queue:" block. Make sure the queue type is "kafka", replication factor is "3" and use confluent cloud is "true".

**Don't forget** to replace "CLUSTER_API_KEY", "CLUSTER_API_SECRET" and "localhost:9092" with your real Confluent Cloud bootstrap servers:

```yml
queue:
  type: "${TB_QUEUE_TYPE:kafka}"
...
  kafka:
    bootstrap.servers: "${TB_KAFKA_SERVERS:localhost:9092}"
...
    replication_factor: "${TB_QUEUE_KAFKA_REPLICATION_FACTOR:3}"
...
    use_confluent_cloud: "${TB_QUEUE_KAFKA_USE_CONFLUENT_CLOUD:true}"
...
      sasl.config: "${TB_QUEUE_KAFKA_CONFLUENT_SASL_JAAS_CONFIG:org.apache.kafka.common.security.plain.PlainLoginModule required username=\"CLUSTER_API_KEY\" password=\"CLUSTER_API_SECRET\";}"
```

**These params affect the number of requests per second from each partitions per each queue.**

Number of requests to particular Message Queue calculated based on the formula:

((Number of Rule Engine and Core Queues) * (Number of partitions per Queue) + 
(Number of transport queues) + (Number of microservices) + (Number of JS executors)) * 1000 / POLL_INTERVAL_MS

For example, number of requests based on default parameters is:

Rule Engine queues:

Main **10** partitions + HighPriority **10** partitions + SequentialByOriginator **10** partitions = **30**

Core queue **10** partitions

Transport request Queue + response Queue = **2**

Rule Engine Transport notifications Queue + Core Transport notifications Queue = **2**

Total = **44**

Number of requests per second = **44 * 1000 / 25 = 1760** requests

Based on the use case, you can compromise latency and decrease number of partitions/requests to the queue, if the message load is low.

By UI set the parameters - interval (1000) and partitions (1) for Rule Engine queues.

Sample parameters to fit into **10** requests per second on a "monolith" deployment:

```yml
queue:
...
  transport_api:
    request_poll_interval: "${TB_QUEUE_TRANSPORT_REQUEST_POLL_INTERVAL_MS:1000}"
    response_poll_interval: "${TB_QUEUE_TRANSPORT_RESPONSE_POLL_INTERVAL_MS:1000}"
...
  core:
    poll-interval: "${TB_QUEUE_CORE_POLL_INTERVAL_MS:1000}"
    partitions: "${TB_QUEUE_CORE_PARTITIONS:2}"
...
  vc:
    partitions: "${TB_QUEUE_VC_PARTITIONS:1}"
    poll-interval: "${TB_QUEUE_VC_INTERVAL_MS:1000}"
...
  js:
    response_poll_interval: "${REMOTE_JS_RESPONSE_POLL_INTERVAL_MS:1000}"
...
  rule-engine:
    poll-interval: "${TB_QUEUE_RULE_ENGINE_POLL_INTERVAL_MS:1000}"
...
  transport:
    poll_interval: "${TB_QUEUE_TRANSPORT_NOTIFICATIONS_POLL_INTERVAL_MS:1000}"
```

You can update default Rule Engine queues configuration using UI. More about SENTIENT Rule Engine queues see in [documentation](/docs/user-guide/rule-engine-2-5/queues/).


</div>

</div>

 

## Step 5. [Optional] Memory update for slow machines (4GB of RAM) 

Open the Notepad or other editor as administrator user (right click on the app icon and select "Run as administrator").  
Open the following file for editing (select "All Files" instead of "Text Documents" in file choosing dialog, the encoding is UTF-8):

```
C:\Program Files (x86)\sentient\sentient.xml
``` 


Locate the following lines to the configuration file. 

```xml
<startargument>-Xms512m</startargument>
<startargument>-Xmx1024m</startargument>
```


and change them to 

```xml
<startargument>-Xms2048m</startargument>
<startargument>-Xmx2048m</startargument>
```

change "2048m" to approximately 1/3rd of your total RAM (in MB)
 

## Step 6. Run installation script

Launch windows shell (Command Prompt) as Administrator. Change directory to your SENTIENT installation directory.

Execute **install.bat** script to install SENTIENT as a Windows service (or run **".\install.bat --loadDemo"** to install and add demo data).
This means it will be automatically started on system startup. 
Similar, **uninstall.bat** will remove SENTIENT from Windows services.
The output should be similar to this one:
  
  ```
C:\Program Files (x86)\sentient>.\install.bat --loadDemo
Detecting Java version installed.
CurrentVersion 170
Java 17 found!
Installing sentient ...
...
SENTIENT installed successfully!
```

## Step 7. Start SENTIENT service

Now let's start the SENTIENT service!
Open the command prompt as an Administrator and execute the following command:

```bash
net start sentient
```


Expected output:

```
The SENTIENT Server Application service is starting.
The SENTIENT Server Application service was started successfully.
```

In order to restart the SENTIENT service you can execute following commands:

```bash
net stop sentient
net start sentient
```


Once started, you will be able to open Web UI using the following link:

```bash
http://localhost:8080/
```


The following default credentials are available if you have specified *--loadDemo* during execution of the installation script:

- **System Administrator**: sysadmin@sentient.org / sysadmin
- **Tenant Administrator**: tenant@sentient.org / tenant
- **Customer User**: customer@sentient.org / customer

You can always change passwords for each account in account profile page.


<div class="st-callout info">


Please allow up to 90 seconds for the Web UI to start.

</div>


## Post-installation steps

### Upgrading to new SENTIENT version

**Keep Your Platform Secure and Up-to-Date**

When a new SENTIENT release becomes available, we provide a streamlined update process to ensure your system benefits from the latest features and security patches without any risk to your data.


<div class="st-callout info">


**To maintain database integrity and system stability, please perform upgrades sequentially (e.g., v4.0.2 → v4.1.0 → v4.2.0).**


</div>


Please refer to our official <a href="/docs/user-guide/install/upgrade-instructions/">Upgrade Instructions</a> for detailed steps tailored to your current deployment environment.


## Troubleshooting

The log files are located in **logs** folder ("C:\Program Files (x86)\sentient\logs" in our case).

The **sentient.log** file should contain following line:

```
YYYY-MM-DD HH:mm:ss,sss [main] INFO  o.t.s.SentientServerApplication - Started SentientServerApplication in x.xxx seconds (JVM running for x.xxx)
```

In case of any unclear errors, use general [troubleshooting guide](/docs/user-guide/troubleshooting/#getting-help) or [contact us](/docs/contact-us/).

## Windows firewall settings

In order to have external access to SENTIENT Web UI and device connectivity (HTTP, MQTT, CoAP)
you need to create a new inbound rule with Windows Firewall with Advanced Security.
 
- Open "Windows Firewall" from "Control Panel":

![image](/images/user-guide/install/windows/windows7-firewall-1.webp)

- Click "Advanced settings" on the left panel:

![image](/images/user-guide/install/windows/windows7-firewall-2.webp)

- Select "Inbound Rules" on the left panel, then click "New Rule..." on the right "Actions" panel:

![image](/images/user-guide/install/windows/windows7-firewall-3.webp)

- Now new "New Inbound Rule Wizard" window will open. On the first step "Rule Type" select "Port" option: 

![image](/images/user-guide/install/windows/windows7-firewall-4.webp)

- On the "Protocol and Ports" step select "TCP" protocol and enter port list **8080, 1883, 5683** in the "Specific local ports" field:

![image](/images/user-guide/install/windows/windows7-firewall-5.webp)

- On the "Action" step leave "Allow the connection" option selected:

![image](/images/user-guide/install/windows/windows7-firewall-6.webp)

- On the "Profile" step select Windows network profiles when to apply this rule:

![image](/images/user-guide/install/windows/windows7-firewall-7.webp)

- Finally, give the name to this rule (for ex. "SENTIENT Service Networking") and click "Finish".

![image](/images/user-guide/install/windows/windows7-firewall-8.webp)


## Next steps
