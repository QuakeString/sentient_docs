+++
title = "Installing SENTIENT Edge on Ubuntu Server"
description = "Installing SENTIENT Edge on Ubuntu Server"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/edge/deb-installation.md"
+++
<div class="st-callout warn">


<p>Version Compatibility Rules - Read before proceeding
</p>

<p>Before installing SENTIENT Edge, ensure that <b>SENTIENT Server</b> is <a href="/docs/user-guide/install/installation-options/" target="_blank">installed</a> and <a href="/docs/user-guide/install/upgrade-instructions/" target="_blank">updated</a> to the latest version.</p>

<p>Additionally, verify that the <b>SENTIENT Edge and SENTIENT Server versions are compatible</b>.</p>

<p>Compatibility rules:</p>
<ul>
<li>SENTIENT Edge version X.Y.Z works with SENTIENT Server version X.Y.Z and the next <span style="color:red"><strong>two</strong></span> versions.</li><ul>
<li>Example: SENTIENT Edge 3.8.0 works with SENTIENT Server 3.8.0 and <span style="color:red"><strong>two</strong></span> later versions (3.9.0 and 3.9.1). View the <a href="/docs/reference/releases/" target="_blank">SENTIENT Server Release Notes here</a>.</li></ul>
<li>SENTIENT Edge version X.Y.Z <span style="color:red"><strong>does not work</strong></span> with older SENTIENT Server versions.</li><ul>
<li>Example: SENTIENT Edge 3.9.1 <span style="color:red"><strong>does not support</strong></span> SENTIENT Server 3.8.0 or earlier versions. The SENTIENT Server must be <a href="/docs/user-guide/install/upgrade-instructions/" target="_blank">upgraded to the latest version</a> first.</li></ul>
</ul>
<p><strong>Note:</strong> If you run an older version of SENTIENT Edge (e.g., version 3.6.0), the SENTIENT team cannot guarantee the availability or proper functioning of all features.</p>


</div>


This guide provides step-by-step instructions for installing **SENTIENT Edge** on **Ubuntu 22.04 LTS and 24.04 LTS**.


## Prerequisites

To start running **SENTIENT Community Edition Edge**, you will need an active **SENTIENT Community Edition account** that supports **Edge** functionality.


You can install the **SENTIENT** local server. For this, please refer to the [SENTIENT installation guide](/docs/user-guide/install/installation-options/).

The local server can be accessed via [http://localhost:8080](http://localhost:8080). Throughout this tutorial, we will refer to this URL as **SERVER_URL.** Log in with:
* **Username:** tenant@sentient.org
* **Password:** tenant


### Edge Hardware Requirements

The hardware requirements for **SENTIENT Edge** are determined by the number of connected devices and the intensity of interactions with the platform interface.
To ensure optimal performance, we recommend the following:
* **At least 1GB of RAM (Light workload):** It is suitable for minimal interactions with the platform interface, such as dashboards and device management, and fewer than 100 connected devices.
* **At least 4GB of RAM (Heavy workload):** This configuration is suitable for intense platform interactions and 100+ devices connected to a single machine.

### Deploying a New Edge Instance

To create a new **Edge**:


1. Sign in to your **SENTIENT** instance and navigate to the **Edge Management > Instances** section. Click the **"+"** icon in the top right corner and select the **"Add new edge"** option.

1. Enter a name for the Edge you are creating. For example, "My New Edge". Click the **"Add"** button to confirm the addition of the **Edge instance**.

1. Your new **Edge** is created and will appear at the top of the list, as entries are sorted by creation time by default.


<div class="st-gallery"><figure><img src="/images/edge/installation-add-edge-item-1.webp" alt="Sign in to your **SENTIENT** instance and navigate to the **Edge Management > Instances** section. Click the **&quot;+&quot;** icon in the top right corner and select the **&quot;Add new edge&quot;** option." loading="lazy"><figcaption>Sign in to your **SENTIENT** instance and navigate to the **Edge Management > Instances** section. Click the **"+"** icon in the top right corner and select the **"Add new edge"** option.</figcaption></figure><figure><img src="/images/edge/installation-add-edge-item-2.webp" alt="Enter a name for the Edge you are creating. For example, &quot;My New Edge&quot;. Click the **&quot;Add&quot;** button to confirm the addition of the **Edge instance**." loading="lazy"><figcaption>Enter a name for the Edge you are creating. For example, "My New Edge". Click the **"Add"** button to confirm the addition of the **Edge instance**.</figcaption></figure><figure><img src="/images/edge/installation-add-edge-item-3.webp" alt="Your new **Edge** is created and will appear at the top of the list, as entries are sorted by creation time by default." loading="lazy"><figcaption>Your new **Edge** is created and will appear at the top of the list, as entries are sorted by creation time by default.</figcaption></figure></div>


## Guided installation using pre-configured instructions in the Server UI


Once the **Edge** instance has been created, the installation instructions will be available for use. 
Each **Edge** has preset configurations that contain important credentials, such as **Edge Secret**, **Edge Key**, etc.  To access these configurations:


1. Click on the **Edge** entity to open its details.

1. Click the **"Install & Connection Instructions"** button.

1. Follow the instructions to install **Edge** and connect it to the server.


<div class="st-gallery"><figure><img src="/images/edge/installation/prepared-instructions-install-item-1-ce.webp" alt="Click on the **Edge** entity to open its details." loading="lazy"><figcaption>Click on the **Edge** entity to open its details.</figcaption></figure><figure><img src="/images/edge/installation/prepared-instructions-install-item-2-ce.webp" alt="Click the **&quot;Install & Connection Instructions&quot;** button." loading="lazy"><figcaption>Click the **"Install & Connection Instructions"** button.</figcaption></figure><figure><img src="/images/edge/installation/prepared-instructions-install-item-3-ce.webp" alt="Follow the instructions to install **Edge** and connect it to the server." loading="lazy"><figcaption>Follow the instructions to install **Edge** and connect it to the server.</figcaption></figure></div>


## Manual Installation and Configuration

If for any reason you are unable to use the prepared **SENTIENT Server Instructions** above, please follow the steps below.
These steps will guide you through installing and configuring the **Edge** by yourself.

### Step 1. Install Java 17 (OpenJDK) 

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


### Step 2. Configure the SENTIENT Edge database

**SENTIENT Edge** supports **SQL** and **hybrid** database approaches. See the architecture [page](/docs/reference/#sql-vs-nosql-vs-hybrid-database-approach) for details.


<div class="st-tabs">

<div class="st-tab" data-label="PostgreSQL (recommended for ">


<div class="st-callout info">


The SENTIENT team recommends using **PostgreSQL** for development and production environments with **moderate load (less than 5000 msg/sec)**.
Many cloud providers offer managed **PostgreSQL** services, making it a cost-effective solution for most SENTIENT deployments.


</div>


**SENTIENT Edge** uses **PostgreSQL** database as a local storage.

To install the **PostgreSQL** database, run these commands:

```bash
# Automated repository configuration:
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh

# install and launch the postgresql service:
sudo apt update
sudo apt -y install postgresql-16
sudo service postgresql start
```


Once **PostgreSQL** is installed, it is recommended to set the password for the **PostgreSQL main user**.

The following command will switch the current user to the PostgreSQL user and set the password directly in PostgreSQL.
```bash
sudo -u postgres psql -c "\password"
```


Then, **enter and confirm** the password.


Finally, create a new PostgreSQL database named **tb_edge** by running the following command:

```bash
echo "CREATE DATABASE tb_edge;" | psql -U postgres -d postgres -h 127.0.0.1 -W
```


</div>

<div class="st-tab" data-label="Hybrid PostgreSQL+Cassandra(recommended for &gt; 5K msg/sec)">


<div class="st-callout info">


The SENTIENT team recommends using a **hybrid database approach** if you plan to manage 1M+ devices in production or handle **high data ingestion rate (more than 5000 msg/sec)**.
In this case, **SENTIENT Edge** stores time-series data in Cassandra while continuing to use PostgreSQL for primary entities such as devices, assets, dashboards, and customers.  


</div>


##### PostgreSQL Installation

To install the **PostgreSQL** database, run these commands:

```bash
# Automated repository configuration:
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh

# install and launch the postgresql service:
sudo apt update
sudo apt -y install postgresql-16
sudo service postgresql start
```


Once **PostgreSQL** is installed, it is recommended to set the password for the **PostgreSQL main user**.

The following command will switch the current user to the PostgreSQL user and set the password directly in PostgreSQL.
```bash
sudo -u postgres psql -c "\password"
```


Then, **enter and confirm** the password.


To create a new PostgreSQL database named **tb_edge**, use the following command:

```bash
echo "CREATE DATABASE tb_edge;" | psql -U postgres -d postgres -h 127.0.0.1 -W
```


Press **"Ctrl+D"** twice to quit PostgreSQL.

##### Cassandra Installation

The instructions listed below will help you to install **Cassandra**.

```bash
# Add cassandra repository
echo "deb https://debian.cassandra.apache.org 41x main" | sudo tee /etc/apt/sources.list.d/cassandra.sources.list
curl https://downloads.apache.org/cassandra/KEYS | sudo apt-key add -
sudo apt-get update
## Cassandra installation
sudo apt-get install cassandra
## Tools installation
sudo apt-get install cassandra-tools
```

In order to run Cassandra, install **Java 11**.

```bash
sudo apt install openjdk-11-jdk-headless
```


Set **Java 17** as the default version (required for **SENTIENT Edge**):
```bash
sudo update-alternatives --config java
```


Edit the Cassandra **configuration file**:
```
sudo sed -i 's|#JAVA_HOME=/usr/local/jdk6|JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64|' /usr/share/cassandra/cassandra.in.sh
```


Then, restart **Cassandra**:
```bash
sudo service cassandra stop && sudo service cassandra start
```


##### SENTIENT Edge Configuration

Edit **SENTIENT Edge** configuration file:

```bash 
sudo nano /etc/tb-edge/conf/tb-edge.conf
``` 


Add the following lines to the configuration file. Don't forget **to replace** "PUT_YOUR_POSTGRESQL_PASSWORD_HERE" with your **real postgres user password**:

```bash
# DB Configuration 
export DATABASE_TS_TYPE=cassandra
export SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/tb_edge
export SPRING_DATASOURCE_USERNAME=postgres
export SPRING_DATASOURCE_PASSWORD=PUT_YOUR_POSTGRESQL_PASSWORD_HERE
``` 


You can optionally add the following parameters to reconfigure your Edge instance to connect to external Cassandra nodes:

```bash
export CASSANDRA_CLUSTER_NAME=Edge Cluster
export CASSANDRA_KEYSPACE_NAME=sentient
export CASSANDRA_URL=127.0.0.1:9042
export CASSANDRA_USE_CREDENTIALS=false
export CASSANDRA_USERNAME=
export CASSANDRA_PASSWORD=
```


</div>

</div>


### Step 3. Select the Queue service

**SENTIENT Edge** can use different messaging systems and brokers for storing messages and enabling communication between its services. Choose the appropriate queue implementation based on your specific business needs:

* **In Memory**: The built-in and default queue implementation. It is useful for development or proof-of-concept (PoC) environments, but is not recommended for production or any type of clustered deployments due to limited scalability.
* **Kafka**: Recommended for production deployments. This queue is used in most of the SENTIENT production environments now.


<div class="st-tabs">

<div class="st-tab" data-label="In Memory (built-in and default)">

**In Memory** queue is built in and enabled by default. No additional configuration is required.

</div>

<div class="st-tab" data-label="Kafka (recommended for on-prem, production installations)">

### Docker installation

Install Docker for [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)


<div class="st-callout warn">


**Don't forget to add your linux user to the docker group. See [Manage Docker as a non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).**


</div>


#### Kafka Installation

[Apache Kafka](https://kafka.apache.org/) is an open source stream processing platform.

To install **Kafka in a [Docker container](https://docs.docker.com/engine/install/)**, run the command below.
It creates **docker-compose-kafka.yml**, fills it with configuration lines, and starts the container.

```
cat > docker-compose-kafka.yml <<EOF && docker compose -f docker-compose-kafka.yml up -d
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
EOF
```


##### SENTIENT Edge Configuration

Edit the **SENTIENT Edge** configuration file (tb-edge.conf):

```
echo -e "export TB_QUEUE_TYPE=kafka\nexport TB_KAFKA_SERVERS=localhost:9092" | sudo tee -a /etc/tb-edge/conf/tb-edge.conf > /dev/null
```


**Make sure** to replace "localhost:9092" with your real Kafka bootstrap servers if necessary


</div>

</div>


### Step 4. SENTIENT Edge service installation

Download the installation package:

```bash
wget https://github.com/sentient/sentient-gateway/releases/download//tb-edge-.deb
```


Go to the download repository and install SENTIENT Edge service

```bash
sudo dpkg -i tb-edge-.deb
```


### Step 5. Configure the SENTIENT Edge


Click on **Copy Edge Key** and **Copy Edge Secret** in the edge details section.
This will copy your edge credentials to your clipboard.
Be sure to store them in a secure location, as these values will be needed in the following steps.


<div class="st-gallery"><figure><img src="/images/edge/installation-copy-edge-credentials-item-1.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Edit the **SENTIENT Edge** configuration file.


```bash
sudo sh -c 'cat <<EOL >> /etc/tb-edge/conf/tb-edge.conf
export CLOUD_ROUTING_KEY=<PUT_YOUR_EDGE_KEY_HERE>
export CLOUD_ROUTING_SECRET=<PUT_YOUR_EDGE_SECRET_HERE>
export CLOUD_RPC_HOST=<PUT_YOUR_RPC_HOST>
export CLOUD_RPC_PORT=7070
export CLOUD_RPC_SSL_ENABLED=false
export HTTP_BIND_PORT=18080
export MQTT_BIND_PORT=11883
export COAP_BIND_PORT=15683
export LWM2M_ENABLED=false
export SNMP_ENABLED=false
EOL'
```


* **PUT_YOUR_EDGE_KEY_HERE:** Replace with your **actual Edge Key**.
* **PUT_YOUR_EDGE_SECRET_HERE:** Replace with your **actual Edge Secret**.
* **PUT_YOUR_RPC_HOST:**
  * Use **localhost** if the Edge is running on the same machine as the Server instance.
  * Use an **X.X.X.X** IP address if the Edge is connecting to the Server instance in the same network or in a Docker container.

#### Configure PostgreSQL (Optional)

If you changed PostgreSQL default datasource settings, use the following command:

```bash
sudo sh -c 'cat <<EOL >> /etc/tb-edge/conf/tb-edge.conf
export SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/tb_edge
export SPRING_DATASOURCE_USERNAME=postgres
export SPRING_DATASOURCE_PASSWORD=<PUT_YOUR_POSTGRESQL_PASSWORD_HERE>
EOL'
```


* **PUT_YOUR_POSTGRESQL_PASSWORD_HERE:** Replace with your actual **PostgreSQL user password**.

### Step 6. Run the installation Script


Once **SENTIENT Edge** is installed and configured please execute the following installation script:

```bash
sudo /usr/share/tb-edge/bin/install/install.sh
```


<div class="st-callout info">


Make sure you run this script from the root. To change the current directory to the root directory, run the command **cd /**.


</div>


 

### Step 7. Start the SENTIENT Edge service

```bash
sudo service tb-edge start
```


### Step 8. Open the SENTIENT Edge UI


Once the **Edge** service is started, open the **Edge UI** at [http://localhost:8080](http://localhost:8080).


<div class="st-callout info">


If the Edge **HTTP bind port** was changed to **18080** during Edge installation, access the **SENTIENT Edge** instance at [http://localhost:18080](http://localhost:18080).


</div>


Please use your tenant credentials from **SENTIENT Server** to log in to the **SENTIENT Edge**. 

## Troubleshooting

The **SENTIENT Edge** logs are stored in the following directory:
 
```bash
/var/log/tb-edge
```
To check for errors on the service side, run the following command:
 
```bash
cat /var/log/tb-edge/tb-edge.log | grep ERROR
```


Start the **SENTIENT Edge** service:
```bash
sudo service tb-edge start
```


Stop the **SENTIENT Edge** service:
```bash
sudo service tb-edge stop
```


Restart the **SENTIENT Edge** service:
```bash
sudo service tb-edge restart
```


Check the status of the **SENTIENT Edge** service:
```bash
sudo service tb-edge status
```

 

## Next Steps

Congratulations! You have successfully provisioned, installed and connected SENTIENT **Edge** to SENTIENT server.

You can continue with **Getting started guide** to get the basic knowledge of SENTIENT **Edge** or you can jump directly to more advanced topics:
