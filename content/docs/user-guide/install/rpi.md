+++
title = "Installing SENTIENT on Raspberry Pi"
description = "Installing SENTIENT IoT Platform on Raspberry Pi"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/rpi.md"
+++
## Prerequisites

This guide describes how to install SENTIENT on a Raspberry Pi.
Hardware requirements depend on chosen database and amount of devices connected to the system. 
To run SENTIENT and PostgreSQL you will need at least 4Gb of RAM.
To run SENTIENT and Cassandra you will need at least 8Gb of RAM.


## Step 1. Install Java 17 (OpenJDK) 
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


## Step 2. SENTIENT service installation

Download installation package.

```bash
wget https://github.com/sentient/sentient/releases/download//sentient-.deb
```


Install SENTIENT as a service

```bash
sudo dpkg -i sentient-.deb
```


## Step 3. Configure SENTIENT database


<div class="st-callout info">


SENTIENT team recommends to use PostgreSQL for development and production environments with reasonable load (< 5000 msg/sec).
Many cloud vendors support managed PostgreSQL servers which is a cost-effective solution for most of SENTIENT instances.


</div>


### PostgreSQL Installation

Instructions listed below will help you to install PostgreSQL.

```bash
# install **wget** if not already installed:
sudo apt install -y wget

# import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# add repository contents to your system:
echo "deb https://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" | sudo tee  /etc/apt/sources.list.d/pgdg.list

# install and launch the postgresql service:
sudo apt update
sudo apt -y install postgresql
sudo service postgresql start
```


Once **PostgreSQL** is installed, it is recommended to set the password for the **PostgreSQL main user**.

The following command will switch the current user to the PostgreSQL user and set the password directly in PostgreSQL.
```bash
sudo -u postgres psql -c "\password"
```


Then, **enter and confirm** the password.


Then, connect to the "postgres" database as the "postgres" user:

```bash
psql -U postgres -d postgres -h 127.0.0.1 -W
```


Create the SENTIENT database named "sentient" :
```bash
CREATE DATABASE sentient;
```


Press "Ctrl+D" twice to exit PostgreSQL.


### SENTIENT Configuration

Edit SENTIENT configuration file 

```bash 
sudo nano /etc/sentient/conf/sentient.conf
``` 


Add the following lines to the configuration file. Don't forget **to replace** "PUT_YOUR_POSTGRESQL_PASSWORD_HERE" with your **real postgres user password**:

```bash
# DB Configuration 
export DATABASE_TS_TYPE=sql
export SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/sentient
export SPRING_DATASOURCE_USERNAME=postgres
export SPRING_DATASOURCE_PASSWORD=PUT_YOUR_POSTGRESQL_PASSWORD_HERE
# Specify partitioning size for timestamp key-value storage. Allowed values: DAYS, MONTHS, YEARS, INDEFINITE.
export SQL_POSTGRES_TS_KV_PARTITIONING=MONTHS
```


## Step 4. Choose SENTIENT queue service

SENTIENT uses queue services for API calls between micro-services and able to use next queue services: In Memory (default) and Kafka-based systems.


<div class="st-tabs">

<div class="st-tab" data-label="In Memory (built-in and default)">

**In Memory** queue is built in and enabled by default. No additional configuration is required.

</div>

<div class="st-tab" data-label="Confluent Cloud (Event Streaming Platform based on Kafka)">

#### Confluent Cloud Configuration

To access [Confluent Cloud](https://docs.confluent.io/current/platform.html#what-is-cp) 
you should first create an [account](https://confluent.cloud/login), 
then create a [Kafka cluster](https://docs.confluent.io/current/quickstart/cloud-quickstart/index.html#step-1-create-a-ak-cluster-in-ccloud) 
and get your [API Key](https://docs.confluent.io/current/quickstart/cloud-quickstart/index.html#step-4-create-an-api-key).


##### SENTIENT Configuration

Edit SENTIENT configuration file

```
sudo nano /etc/sentient/conf/sentient.conf
```


Add the following lines to the configuration file. Don't forget to replace "CLUSTER_API_KEY", "CLUSTER_API_SECRET" and "localhost:9092" with your real Confluent Cloud bootstrap servers:**

```bash
export TB_QUEUE_TYPE=kafka
export TB_QUEUE_KAFKA_USE_CONFLUENT_CLOUD=true
export TB_KAFKA_SERVERS=localhost:9092
export TB_QUEUE_KAFKA_REPLICATION_FACTOR=3
export TB_QUEUE_KAFKA_CONFLUENT_SASL_JAAS_CONFIG='org.apache.kafka.common.security.plain.PlainLoginModule required username="CLUSTER_API_KEY" password="CLUSTER_API_SECRET";'

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

export TB_QUEUE_CORE_POLL_INTERVAL_MS=1000
export TB_QUEUE_CORE_PARTITIONS=2
export TB_QUEUE_RULE_ENGINE_POLL_INTERVAL_MS=1000
export TB_QUEUE_TRANSPORT_REQUEST_POLL_INTERVAL_MS=1000
export TB_QUEUE_TRANSPORT_RESPONSE_POLL_INTERVAL_MS=1000
export TB_QUEUE_TRANSPORT_NOTIFICATIONS_POLL_INTERVAL_MS=1000
export TB_QUEUE_VC_INTERVAL_MS=1000
export TB_QUEUE_VC_PARTITIONS=1
```


You can update default Rule Engine queues configuration using UI. More about SENTIENT Rule Engine queues see in [documentation](/docs/user-guide/rule-engine-2-5/queues/).


</div>

</div>

 

## Step 5. Memory update for slow machines (4GB of RAM) 

Edit SENTIENT configuration file 

```bash 
sudo nano /etc/sentient/conf/sentient.conf
``` 


Add the following lines to the configuration file. 

```bash
# Update SENTIENT memory usage and restrict it to 2G in /etc/sentient/conf/sentient.conf
export JAVA_OPTS="$JAVA_OPTS -Xms2G -Xmx2G"
```


We recommend adjusting these parameters depending on your server resources. It should be set to at least 2G (gigabytes), and increased accordingly if there is additional RAM space available. Usually, you need to set it to 1/2 of your total RAM if you do not run any other memory-intensive processes (e.g. Cassandra), or to 1/3 otherwise. 

## Step 6. Run installation script

Once SENTIENT service is installed and DB configuration is updated, you can execute the following script:

```bash
# --loadDemo option will load demo data: users, devices, assets, rules, widgets.
sudo /usr/share/sentient/bin/install/install.sh --loadDemo
```

 


## Step 7. Start SENTIENT service


Execute the following command to start SENTIENT:

```bash
sudo service sentient start
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

The upgrade procedure for Raspberry Pi is identical to the Ubuntu instructions.

**Keep Your Platform Secure and Up-to-Date**

When a new SENTIENT release becomes available, we provide a streamlined update process to ensure your system benefits from the latest features and security patches without any risk to your data.


<div class="st-callout info">


**To maintain database integrity and system stability, please perform upgrades sequentially (e.g., v4.0.2 → v4.1.0 → v4.2.0).**


</div>


Please refer to our official <a href="/docs/user-guide/install/upgrade-instructions/">Upgrade Instructions</a> for detailed steps tailored to your current deployment environment.


## Troubleshooting

SENTIENT logs are stored in the following directory:
 
```bash
/var/log/sentient
```


You can issue the following command in order to check if there are any errors on the backend side:
 
```bash
cat /var/log/sentient/sentient.log | grep ERROR
```


## Next steps
