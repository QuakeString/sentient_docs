+++
title = "Installing SENTIENT on CentOS/RHEL"
description = "Installing SENTIENT on CentOS/RHEL"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/rhel.md"
+++
## Prerequisites

This guide describes how to install SENTIENT on RHEL 8/9, CentOS 8/9, or their derivatives (Alma, Rocky, Oracle, etc). 
Hardware requirements depend on chosen database and amount of devices connected to the system. 
To run SENTIENT and PostgreSQL on a single machine you will need at least 4Gb of RAM.
To run SENTIENT and Cassandra on a single machine you will need at least 8Gb of RAM.

Before continue to installation execute the following commands in order to install necessary tools:

**For CentOS 8:**

```bash
# Install wget
sudo dnf install -y nano wget
# Add latest EPEL release for CentOS 8
sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```


**For CentOS 9:**

```bash
# Install wget
sudo dnf install -y nano wget
# Add latest EPEL release for CentOS 9
sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
```


To ensure proper installation process, execute the following command to install the necessary system fonts:

```bash
sudo dnf install -y harfbuzz fontconfig dejavu-sans-fonts
```


## Step 1. Install Java 17 (OpenJDK) 

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
 

## Step 2. SENTIENT service installation

Download installation package.

```bash
wget https://github.com/sentient/sentient/releases/download//sentient-.rpm
```


Install SENTIENT as a service

```bash
sudo rpm -Uvh sentient-.rpm
```


## Step 3. Configure SENTIENT database

SENTIENT is able to use SQL or hybrid database approach. See corresponding architecture [page](/docs/reference/#sql-vs-nosql-vs-hybrid-database-approach) for more details.  


<div class="st-tabs">

<div class="st-tab" data-label="PostgreSQL (recommended for ">


<div class="st-callout info">


SENTIENT team recommends to use PostgreSQL for development and production environments with reasonable load (< 5000 msg/sec).
Many cloud vendors support managed PostgreSQL servers which is a cost-effective solution for most of SENTIENT instances.


</div>


##### PostgreSQL Installation

Instructions listed below will help you to install PostgreSQL.

```bash
# Update your system
sudo dnf update
```


Install the repository.

**For CentOS/RHEL 8:**

```bash
# Install the repository RPM:
sudo dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```


**For CentOS/RHEL 9:**

```bash
# Install the repository RPM:
sudo dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```


Install the package.

```bash
# Install packages
sudo dnf -qy module disable postgresql
sudo dnf -y install postgresql16 postgresql16-server postgresql16-contrib
# Initialize your PostgreSQL DB
sudo /usr/pgsql-16/bin/postgresql-16-setup initdb
sudo systemctl start postgresql-16
# Optional: Configure PostgreSQL to start on boot
sudo systemctl enable --now postgresql-16
```


Once **PostgreSQL** is installed, it is recommended to set the password for the **PostgreSQL main user**.

The following command will switch the current user to the PostgreSQL user and set the password directly in PostgreSQL.
```bash
sudo -u postgres psql -c "\password"
```


Then, **enter and confirm** the password.


After configuring the password, connect to the database to create sentient DB:

```bash
psql -U postgres -d postgres -h 127.0.0.1 -W
```


Execute create database statement

```bash
CREATE DATABASE sentient;
```


Then, press "Ctrl+D" twice to exit PostgreSQL.


##### SENTIENT Configuration

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


</div>

<div class="st-tab" data-label="Hybrid PostgreSQL+Cassandra(recommended for &gt; 5K msg/sec)">


<div class="st-callout info">


SENTIENT team recommends to use Hybrid database approach if you do plan to have 1M+ devices in production or high data ingestion rate (> 5000 msg/sec).
In this case, SENTIENT will be storing timeseries data in Cassandra while continue to use PostgreSQL for main entities (devices/assets/dashboards/customers).  


</div>


##### PostgreSQL Installation

Instructions listed below will help you to install PostgreSQL.

```bash
# Update your system
sudo dnf update
```


Install the repository.

**For CentOS/RHEL 8:**

```bash
# Install the repository RPM:
sudo dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```


**For CentOS/RHEL 9:**

```bash
# Install the repository RPM:
sudo dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```


Install the package.

```bash
# Install packages
sudo dnf -qy module disable postgresql
sudo dnf -y install postgresql16 postgresql16-server postgresql16-contrib
# Initialize your PostgreSQL DB
sudo /usr/pgsql-16/bin/postgresql-16-setup initdb
sudo systemctl start postgresql-16
# Optional: Configure PostgreSQL to start on boot
sudo systemctl enable --now postgresql-16
```


Once **PostgreSQL** is installed, it is recommended to set the password for the **PostgreSQL main user**.

The following command will switch the current user to the PostgreSQL user and set the password directly in PostgreSQL.
```bash
sudo -u postgres psql -c "\password"
```


Then, **enter and confirm** the password.


After configuring the password, connect to the database to create sentient DB:

```bash
psql -U postgres -d postgres -h 127.0.0.1 -W
```


Execute create database statement

```bash
CREATE DATABASE sentient;
```


Then, press "Ctrl+D" twice to exit PostgreSQL.


##### Cassandra Installation

The following commands will install Apache Cassandra and its command-line tools:

```bash
# Import GPG key
sudo rpm --import https://downloads.apache.org/cassandra/KEYS 
# Add Cassandra repository
sudo tee /etc/yum.repos.d/cassandra.repo > /dev/null <<EOF
[cassandra]
name=Apache Cassandra
baseurl=https://redhat.cassandra.apache.org/50x/
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://downloads.apache.org/cassandra/KEYS
EOF

# Install packages
sudo dnf -y update
sudo dnf -y install cassandra cassandra-tools chkconfig
# Start service
sudo systemctl daemon-reexec
sudo systemctl start cassandra.service
# Configure Cassandra to start on boot
sudo chkconfig cassandra on
```


To verify that Cassandra is running correctly, use the following commands to check both the node status and the system service state:

```bash
nodetool status
sudo systemctl status cassandra.service 
```


The status column in the output should report `UN` which stands for "Up/Normal"; you may need to wait a few moments for Cassandra to initialize. Example output:

```
$ nodetool status
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address    Load        Tokens  Owns (effective)  Host ID                               Rack 
UN  127.0.0.1  136.29 KiB  16      100.0%            60ae50fd-8914-44a1-a397-b716b7d4b37c  rack1

$ sudo systemctl status cassandra.service 
● cassandra.service - LSB: distributed storage system for structured data
     Loaded: loaded (/etc/rc.d/init.d/cassandra; generated)
     Active: active (running) since Thu 2025-04-24 12:22:11 UTC; 11min ago
       Docs: man:systemd-sysv-generator(8)
    Process: 34716 ExecStart=/etc/rc.d/init.d/cassandra start (code=exited, status=0/SUCCESS)
   Main PID: 34819 (java)
      Tasks: 62 (limit: 50538)
     Memory: 4.3G
        CPU: 17.792s
     CGroup: /system.slice/cassandra.service
             └─34819 /usr/lib/jvm/java-17-openjdk-17.0.14.0.7-2.el9.x86_64/bin/java -ea -da:net.openhft... -XX:+UseThreadPriorities -XX:+HeapDumpOnOutOfMemoryError -Xss256k -XX:+AlwaysPreTo>
...
```

You can use Astra DB Cloud instead of installing your own Cassandra.
See how to [connect SENTIENT to Astra DB](/docs/user-guide/install/pe/cassandra-cloud-astra-db/)


##### SENTIENT Configuration

Edit SENTIENT configuration file 

```bash 
sudo nano /etc/sentient/conf/sentient.conf
``` 


Add the following lines to the configuration file. Don't forget **to replace** "PUT_YOUR_POSTGRESQL_PASSWORD_HERE" with your **real postgres user password**:

```bash
# DB Configuration 
export DATABASE_TS_TYPE=cassandra
export SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/sentient
export SPRING_DATASOURCE_USERNAME=postgres
export SPRING_DATASOURCE_PASSWORD=PUT_YOUR_POSTGRESQL_PASSWORD_HERE
``` 


You can optionally add the following parameters to reconfigure your SENTIENT instance to connect to external Cassandra nodes:

```bash
export CASSANDRA_CLUSTER_NAME=Sentient Cluster
export CASSANDRA_KEYSPACE_NAME=sentient
export CASSANDRA_URL=127.0.0.1:9042
export CASSANDRA_USE_CREDENTIALS=false
export CASSANDRA_USERNAME=
export CASSANDRA_PASSWORD=
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

#### Docker installation

Install Docker for [CentOS/RHEL](https://docs.docker.com/engine/install/centos/)


<div class="st-callout warn">


**Don't forget to add your linux user to the docker group. See [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).**


</div>


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

Edit SENTIENT configuration file

```
sudo nano /etc/sentient/conf/sentient.conf
```


Add the following line to the configuration file. **Don't forget** to replace "localhost:9092" with your real Kafka bootstrap servers:

```bash
export TB_QUEUE_TYPE=kafka
export TB_KAFKA_SERVERS=localhost:9092
```


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

 

## Step 5. [Optional] Memory update for slow machines (4GB of RAM) 

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

SENTIENT UI is accessible on 8080 port by default. 
Make sure that your 8080 port is accessible via firewall.
In order to open 8080 port execute the following command:

```bash
sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
```
   


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

### Configure HAProxy to enable HTTPS

You may want to configure HTTPS access using HAProxy. 
This is possible in case you are hosting SENTIENT in the cloud and have a valid DNS name assigned to your instance.
Please follow this [guide](/docs/user-guide/install/pe/add-haproxy-rhel) to install HAProxy and generate valid SSL certificate using Let's Encrypt.


### Upgrading to new SENTIENT version

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
