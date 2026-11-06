+++
title = "Microservices setup using AWS EKS"
description = "SENTIENT IoT platform microservices setup with Kubernetes in AWS EKS"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/cluster/aws-microservices-setup.md"
+++
This guide will help you to setup SENTIENT in microservices mode using AWS EKS. 
See [microservices](/docs/reference/msa/) architecture page for more details about each component that will be installed.
We will use Amazon RDS for managed PostgreSQL, Amazon MSK for managed Kafka and Amazon ElastiCache for managed Redis.

## Prerequisites

### Install and configure tools 

To deploy SENTIENT on EKS cluster you'll need to install [`kubectl`](https://kubernetes.io/docs/tasks/tools/), 
 [`eksctl`](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html) and 
 [`awscli`](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) tools.

Afterwards you need to configure Access Key, Secret Key and default region. 
To get Access and Secret keys please follow [this](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html) guide.
The default region should be the ID of the region where you'd like to deploy the cluster.

```
aws configure
```


## Step 1. Clone SENTIENT K8S scripts repository

```bash
git clone -b release- https://github.com/sentient/sentient-ce-k8s.git
cd sentient-ce-k8s/aws/microservices
```


## Step 2. Configure and create EKS cluster


In the `cluster.yml` file you can find suggested cluster configuration.
Here are the fields you can change depending on your needs:
- `region` - should be the AWS region where you want your cluster to be located (the default value is `us-east-1`)
- `availabilityZones` - should specify the exact IDs of the region's availability zones
  (the default value is `[us-east-1a,us-east-1b,us-east-1c]`)
- `instanceType` - the type of the instance with TB node (the default value is `m5.xlarge`)

**Note**: if you don't make any changes to `instanceType` and `desiredCapacity` fields, the EKS will deploy **3** nodes of type **m5.xlarge**.


<div class="st-callout info">


The following command will create new VPC for your SENTIENT cluster. This guide assumes you will create new VPC.
Although it is fine to use existing VPC and subnets as well.
You can find more information about configuring VPC for `eksctl` [here](https://eksctl.io/usage/vpc-networking/).


</div>


Command to create AWS cluster:

```
eksctl create cluster -f cluster.yml
```


## Step 3. Create AWS load-balancer controller

Once the cluster is ready you must create AWS load-balancer controller.
You can do it by following [this](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html) guide.
The cluster provisioning scripts will create several load balancers:

* "tb-http-loadbalancer" - AWS ALB that is responsible for the web UI, REST API and HTTP transport;
* "tb-mqtt-loadbalancer" - AWS NLB that is responsible for the MQTT transport;
* "tb-coap-loadbalancer" - AWS NLB that is responsible for the CoAP transport;
* "tb-edge-loadbalancer" - AWS NLB that is responsible for the Edge instances connectivity;

Provisioning of the AWS load-balancer [controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html)
is a **very important step** that is required for those load balancers to work properly. 

## Step 4. Provision Databases

### Step 4.1 Amazon PostgreSQL DB Configuration

You'll need to set up PostgreSQL on Amazon RDS. SENTIENT will use it as a main database to store devices, dashboards, rule chains and device telemetry.
You may follow [this](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html) guide,
but take into account the following requirements:

* Keep your postgresql password in a safe place. We will refer to it later in this guide using **YOUR_RDS_PASSWORD**.
* Make sure your PostgreSQL version is latest 16.x;
* Make sure your PostgreSQL RDS instance is accessible from the SENTIENT cluster;
  The easiest way to achieve this is to deploy the PostgreSQL RDS instance in the same VPC
  and use 'eksctl-sentient-cluster-ClusterSharedNodeSecurityGroup-*' security group.
  We assume you locate it in the same VPC in this guide;
* Make sure you use **"sentient"** as initial database name. If you do not specify a database name, Amazon RDS does not create a database;

And recommendations:

* Use 'Production' template for high availability. It enables a lot of useful settings by default;
* Use 'Provisioned IOPS' for better performance;
* Consider creation of custom parameters group for your RDS instance. It will make change of DB parameters easier;
* Consider deployment of the RDS instance into private subnets. This way it will be nearly impossible to accidentally expose it to the internet.


<div class="st-gallery"><figure><img src="/images/install/cloud/aws/rds-1.webp" alt="Make sure your PostgreSQL version is latest 16.x." loading="lazy"><figcaption>Make sure your PostgreSQL version is latest 16.x.</figcaption></figure><figure><img src="/images/install/cloud/aws/rds-2.webp" alt="Keep your PostgreSQL master password in a safe place. We will refer to it later in this guide using YOUR_RDS_PASSWORD." loading="lazy"><figcaption>Keep your PostgreSQL master password in a safe place. We will refer to it later in this guide using YOUR_RDS_PASSWORD.</figcaption></figure><figure><img src="/images/install/cloud/aws/rds-3.webp" alt="Use &quot;Provisioned IOPS&quot; for better performance." loading="lazy"><figcaption>Use "Provisioned IOPS" for better performance.</figcaption></figure><figure><img src="/images/install/cloud/aws/rds-4.webp" alt="Make sure your PostgreSQL RDS instance is accessible from the SENTIENT cluster; The easiest way to achieve this is to deploy the PostgreSQL RDS instance in the same VPC and use &quot;eksctl-sentient-cluster-ClusterSharedNodeSecurityGroup-*&quot; security group." loading="lazy"><figcaption>Make sure your PostgreSQL RDS instance is accessible from the SENTIENT cluster; The easiest way to achieve this is to deploy the PostgreSQL RDS instance in the same VPC and use "eksctl-sentient-cluster-ClusterSharedNodeSecurityGroup-*" security group.</figcaption></figure><figure><img src="/images/install/cloud/aws/rds-5.webp" alt="Make sure you use &quot;sentient&quot; as initial database name." loading="lazy"><figcaption>Make sure you use "sentient" as initial database name.</figcaption></figure><figure><img src="/images/install/cloud/aws/rds-6.webp" alt="Disable &quot;auto minor version update&quot;." loading="lazy"><figcaption>Disable "auto minor version update".</figcaption></figure></div>


Once the database switch to the 'Available' state, navigate to the 'Connectivity and Security' and copy the endpoint value.


<div class="st-gallery"><figure><img src="/images/install/cloud/aws/rds-endpoint-url.webp" alt="Once the database switch to the &quot;Available&quot; state, navigate to the &quot;Connectivity and Security&quot; and copy the endpoint value. We will refer to it later in this guide using **YOUR_RDS_ENDPOINT_URL**." loading="lazy"><figcaption>Once the database switch to the "Available" state, navigate to the "Connectivity and Security" and copy the endpoint value. We will refer to it later in this guide using **YOUR_RDS_ENDPOINT_URL**.</figcaption></figure></div>


Edit "tb-node-db-configmap.yml" and replace **YOUR_RDS_ENDPOINT_URL** and **YOUR_RDS_PASSWORD**.


### Step 4.2 Cassandra

Using Cassandra is an optional step. 
We recommend to use Cassandra if you plan to insert more than 5K data points per second or would like to optimize storage space.

#### Provision additional node groups

Provision additional node groups that will be hosting Cassandra instances. 
You may change the machine type. At least 4 vCPUs and 16GB of RAM is recommended.

We will create **3** separate node pools with **1** node per zone. 
Since we plan to use ebs disks, we don't want k8s to launch a pod in the zone where the corresponding disk is not available.
Those zones will have the same node label. We will use this label to target deployment of our stateful set.

Deploy **3** nodes of type **m5.xlarge** in different zones. You may change the zones to correspond to your region:

```bash
eksctl create nodegroup --config-file=<path> --include='cassandra-*'
```


#### Deploy Cassandra stateful set

Create SENTIENT namespace:

```bash
kubectl apply -f tb-namespace.yml
kubectl config set-context $(kubectl config current-context) --namespace=sentient
```

Deploy Cassandra to new node groups:

```bash
kubectl apply -f receipts/cassandra.yml
```


The startup of Cassandra cluster may take few minutes. You may monitor the process using:

```bash
kubectl get pods
```


#### Update DB settings

Edit the SENTIENT DB settings file and add Cassandra settings. Don't forget to replace *YOUR_AWS_REGION* with the name of your AWS region. 


```bash
echo "  DATABASE_TS_TYPE: cassandra" >> tb-node-db-configmap.yml
echo "  CASSANDRA_URL: cassandra:9042" >> tb-node-db-configmap.yml
echo "  CASSANDRA_LOCAL_DATACENTER: YOUR_AWS_REGION"  >> tb-node-db-configmap.yml
```


Check that the settings are updated:

```bash
cat tb-node-db-configmap.yml | grep DATABASE_TS_TYPE
```


Expected output:

```
  DATABASE_TS_TYPE: cassandra
```

#### Create keyspace

Create *sentient* keyspace using following command:

```bash
    kubectl exec -it cassandra-0 -- bash -c "cqlsh -e \
                    \"CREATE KEYSPACE IF NOT EXISTS sentient \
                    WITH replication = { \
                        'class' : 'NetworkTopologyStrategy', \
                        'us-east' : '3' \
                    };\""
```


## Step 5. Amazon MSK Configuration (optional)

SENTIENT uses **Kafka as an external queue** for exchanging data between microservices, storing unprocessed messages, and more. 
Kafka is useful for **handling peak loads and failures**, ensuring that all messages from devices are processed reliably. 
By default, the deployment uses **local Kafka**, but SENTIENT is also compatible with **managed services such as Amazon MSK**.

Here are the steps to create a **basic Kafka MSK cluster**:

- Open the **AWS console**, go to [MSK](https://console.aws.amazon.com/msk) and click the "**Create Cluster**" button.
- Select "**Custom creation**" method.
- Specify a **name for your cluster** and select "**Cluster type**" - "**Provisioned**", which will allow you to specify the **number of brokers and storage volume**.
- Select **Apache Kafka version 3.8.x** to use **Express brokers** or **version 4.0.x** for **Standard brokers**.
- Choose **kafka.m7.large** or similar instance types.
- Select the **storage size** for the broker (with the default SENTIENT partition settings, Kafka can use up to **100 GB**).
- Make sure your **MSK instance is accessible** from the **SENTIENT cluster**. The easiest way to achieve this is by **deploying the MSK instance in the same VPC**.
  We also recommend using **private subnets**, as this will make it virtually impossible to accidentally expose the instance to the **Internet**.
- Use the **default security settings**. Make sure that "**Plaintext" mode** is enabled.
- Use either the "**Basic monitoring**" or "**Enhanced topic-level monitoring**" settings.


<div class="st-gallery"><figure><img src="/images/install/cloud/aws/msk-1.webp" alt="Open the AWS console, go to MSK and click the &quot;Create Cluster&quot; button. Select &quot;Custom creation&quot; method. Specify a name for your cluster and select &quot;Cluster type&quot; - &quot;Provisioned&quot;, which will allow you to specify the number of brokers and storage volume. Select Apache Kafka version 3.8.x to use Express brokers or version 4.0.x for Standard brokers." loading="lazy"><figcaption>Open the <b>AWS console</b>, go to <b>MSK</b> and click the "<b>Create Cluster</b>" button. Select "<b>Custom creation</b>" method. Specify a <b>name for your cluster</b> and select "<b>Cluster type</b>" - "<b>Provisioned</b>", which will allow you to specify the <b>number of brokers and storage volume</b>. Select <b>Apache Kafka version 3.8.x</b> to use <b>Express brokers</b> or <b>version 4.0.x</b> for <b>Standard brokers</b>.</figcaption></figure><figure><img src="/images/install/cloud/aws/msk-2.webp" alt="Choose kafka.m7.large or similar instance types." loading="lazy"><figcaption>Choose <b>kafka.m7.large</b> or similar instance types.</figcaption></figure><figure><img src="/images/install/cloud/aws/msk-3.webp" alt="Select the storage size for the broker (with the default SENTIENT partition settings, Kafka can use up to 100 GB)." loading="lazy"><figcaption>Select the <b>storage size</b> for the broker (with the default SENTIENT partition settings, Kafka can use up to <b>100 GB</b>).</figcaption></figure><figure><img src="/images/install/cloud/aws/msk-4.webp" alt="Make sure your MSK instance is accessible from the SENTIENT cluster. The easiest way to achieve this is by deploying the MSK instance in the same VPC. We also recommend using private subnets, as this will make it virtually impossible to accidentally expose the instance to the Internet." loading="lazy"><figcaption>Make sure your <b>MSK instance is accessible</b> from the <b>SENTIENT cluster</b>. The easiest way to achieve this is by <b>deploying the MSK instance in the same VPC</b>. We also recommend using <b>private subnets</b>, as this will make it virtually impossible to accidentally expose the instance to the <b>Internet</b>.</figcaption></figure><figure><img src="/images/install/cloud/aws/msk-5.webp" alt="Use the default security settings. Make sure that &quot;Plaintext&quot; mode is enabled." loading="lazy"><figcaption>Use the <b>default security settings</b>. Make sure that "<b>Plaintext" mode</b> is enabled.</figcaption></figure><figure><img src="/images/install/cloud/aws/msk-6.webp" alt="Use either the &quot;Basic monitoring&quot; or &quot;Enhanced topic-level monitoring&quot; settings." loading="lazy"><figcaption>Use either the "<b>Basic monitoring</b>" or "<b>Enhanced topic-level monitoring</b>" settings.</figcaption></figure></div>


Once the <b>MSK cluster</b> switches to the "<b>Active</b>" state, navigate to "<b>Details</b>" and click "<b>View client information</b>".   
Copy the <b>bootstrap server information in plaintext</b> – this is your <b>Kafka endpoint</b>.


<div class="st-gallery"><figure><img src="/images/install/cloud/aws/msk-connection-params-1.webp" alt="Once the MSK cluster switches to the &quot;Active&quot; state, navigate to &quot;Details&quot; and click &quot;View client information&quot;." loading="lazy"><figcaption>Once the <b>MSK cluster</b> switches to the "<b>Active</b>" state, navigate to "<b>Details</b>" and click "<b>View client information</b>".</figcaption></figure><figure><img src="/images/install/cloud/aws/msk-connection-params-2.webp" alt="Copy the bootstrap server information in plaintext – this is your Kafka endpoint." loading="lazy"><figcaption>Copy the <b>bootstrap server information in plaintext</b> – this is your <b>Kafka endpoint</b>.</figcaption></figure></div>


Edit the `tb-kafka.yml` file, find the **StatefulSet section** named `tb-kafka`, and set the `spec.replicas` value to **0** to disable the default local **Kafka deployment**.

Edit `tb-kafka-configmap.yml` and replace **TB_KAFKA_SERVERS** value with **MSK endpoint**.

## Step 6. Amazon ElastiCache Configuration (optional)

SENTIENT uses **cache** to improve performance and reduce frequent database reads. By default, the deployment uses a **local Valkey cache**. 
However, SENTIENT is also compatible with managed services such as **Amazon ElastiCache**.

Here are the steps to create a **basic ElastiCache Valkey cluster**:
- Open AWS console and navigate to [ElastiCache Valkey caches](https://console.aws.amazon.com/elasticache#/valkey) and click the "**Create**" button.
- You can choose the Deployment option **Serverless** or **Design your own cache**.
- Specify **Valkey Engine version 8.x** and node type with at least 1 GB of RAM.
- Make sure your **Valkey cluster** is accessible from the **SENTIENT cluster**. The easiest way to achieve this is by **deploying the Valkey cluster in the same VPC**. We also recommend using **private subnets**. Use your **group ID**.
- Disable the "**Enable automatic backups**" option.


<div class="st-gallery"><figure><img src="/images/install/cloud/aws/valkey-1.webp" alt="Specify Valkey Engine version 8.x and node type with at least 1 GB of RAM." loading="lazy"><figcaption>Specify <b>Valkey Engine version 8.x</b> and node type with at least 1 GB of RAM.</figcaption></figure><figure><img src="/images/install/cloud/aws/valkey-3.webp" alt="Make sure your Valkey cluster is accessible from the SENTIENT cluster. The easiest way to achieve this is by deploying the Valkey cluster in the same VPC. We also recommend using private subnets. Use your group ID." loading="lazy"><figcaption>Make sure your <b>Valkey cluster</b> is accessible from the <b>SENTIENT cluster</b>. The easiest way to achieve this is by <b>deploying the Valkey cluster in the same VPC</b>. We also recommend using <b>private subnets</b>. Use your <b>group ID</b>.</figcaption></figure><figure><img src="/images/install/cloud/aws/valkey-2.webp" alt="Disable the &quot;Enable automatic backups&quot; option." loading="lazy"><figcaption>Disable the "<b>Enable automatic backups</b>" option.</figcaption></figure></div>


Once the **Valkey cluster** switches to the "**Available" state**, navigate to the "**Details**" section and copy the "**Endpoint**" field **without the ":6379" port suffix** – this is the **Valkey endpoint** for SENTIENT.


<div class="st-gallery"><figure><img src="/images/install/cloud/aws/valkey-4.webp" alt="Once the Valkey cluster switches to the &quot;Available&quot; state, navigate to the &quot;Details&quot; section and copy the &quot;Endpoint&quot; field without the &quot;:6379&quot; port suffix – this is the Valkey endpoint for SENTIENT." loading="lazy"><figcaption>Once the <b>Valkey cluster</b> switches to the "<b>Available" state</b>, navigate to the "<b>Details</b>" section and copy the "<b>Endpoint</b>" field <b>without the ":6379" port suffix</b> – this is the <b>Valkey endpoint</b> for SENTIENT.</figcaption></figure></div>


Edit the `tb-valkey.yml` file, locate the **StatefulSet section** named `tb-valkey`, and set the `spec.replicas` value to **0** to disable the default local Valkey deployment.

Then, edit `tb-cache-configmap.yml` and replace the **REDIS_HOST** value with your **Valkey endpoint**.

## Step 7. CPU and Memory resources allocation

The scripts have preconfigured values of resources for each service. You can change them in `.yml` files under `resources` submenu.

**Note**: if you want to allocate more resources you'll need to increase the number of Amazon nodes or use larger machines. 

Recommended CPU/memory resources allocation:
- TB Node: 1.0 CPU / 2Gi memory
- TB HTTP Transport: 0.5 CPU / 0.5Gi memory
- TB MQTT Transport: 0.5 CPU / 0.5Gi memory
- TB COAP Transport: 0.5 CPU / 0.5Gi memory
- TB Web UI: 0.1 CPU / 100Mi memory
- JS Executor: 0.1 CPU / 100Mi memory
- Zookeeper: 0.1 CPU / 0.5Gi memory

## Step 8. Installation

Execute the following command to run the initial setup of the database. This command will launch short-living SENTIENT pod to provision necessary DB tables, indexes, etc
```
 ./k8s-install-tb.sh --loadDemo
```


Where:

- `--loadDemo` - optional argument. Whether to load additional demo data.

After this command finish you should see the next line in the console:

```
Installation finished successfully!
```


<div class="st-callout info">


Otherwise, please check if you set the PostgreSQL URL and PostgreSQL password in the `tb-node-db-configmap.yml` correctly.


</div>


## Step 9. Starting

Execute the following command to deploy SENTIENT services:

```
 ./k8s-deploy-resources.sh
```


After few minutes you may call `kubectl get pods`. If everything went fine, you should be able to see:

* 5x `tb-pe-js-executor`
* 2x `tb-pe-web-ui`
* 1x `tb-pe-node`
* 1x `tb-pe-web-report`
* 3x `zookeeper`.
  
Every pod should be in the `READY` state.

You should also deploy the transport microservices. Omit the protocols that you don't use in order to save resources:

### HTTP Transport (optional)

```
kubectl apply -f transports/tb-http-transport.yml
```


### MQTT transport (optional)

```
kubectl apply -f transports/tb-mqtt-transport.yml
```


### CoAP transport (optional)

```
kubectl apply -f transports/tb-coap-transport.yml
```


### LwM2M transport (optional)

```
kubectl apply -f transports/tb-lwm2m-transport.yml
```


### SNMP transport (optional)

```
kubectl apply -f transports/tb-snmp-transport.yml
```


## Step 10. Configure Load Balancers

### 10.1 Configure HTTP(S) Load Balancer


Configure HTTP(S) Load Balancer to access web interface of your SENTIENT instance. Basically you have 2 possible options of configuration:

* http - Load Balancer without HTTPS support. Recommended **for development.**
  The only advantage is simple configuration and minimum costs. May be good option for development server but definitely not suitable for production.
* https - Load Balancer with HTTPS support. Recommended **for production.** Acts as an SSL termination point.
  You may easily configure it to issue and maintain a valid SSL certificate. Automatically redirects all non-secure (HTTP) traffic to secure (HTTPS) port.

See links/instructions below on how to configure each of the suggested options.

#### HTTP Load Balancer

Execute the following command to deploy plain http load balancer:

```bash
kubectl apply -f receipts/http-load-balancer.yml
```


The process of load balancer provisioning may take some time. You may periodically check the status of the load balancer using the following command:

```bash
kubectl get ingress
```


Once provisioned, you should see similar output:

```
NAME                   CLASS    HOSTS   ADDRESS         PORTS   AGE
tb-http-loadbalancer   <none>   *       34.111.24.134   80      7m25s
```

Now, you may use the address (the one you see instead of 34.111.24.134 in the command output) to access HTTP web UI (port 80) and connect your devices via [HTTP API](/docs/reference/http-api/)
Use the following default credentials:

- **System Administrator**: sysadmin@sentient.org / sysadmin
- **Tenant Administrator**: tenant@sentient.org / tenant
- **Customer User**: customer@sentient.org / customer

#### HTTPS Load Balancer

Use [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) to create or import SSL certificate. Note your certificate ARN.

Edit the load balancer configuration and replace *YOUR_HTTPS_CERTIFICATE_ARN* with your certificate ARN:

```bash
nano receipts/https-load-balancer.yml
```


Execute the following command to deploy plain https load balancer:

```bash
kubectl apply -f receipts/https-load-balancer.yml
```


### 10.2. Configure MQTT Load Balancer (Optional)


Configure MQTT load balancer if you plan to use MQTT protocol to connect devices.

Create TCP load balancer using following command:

```bash
kubectl apply -f receipts/mqtt-load-balancer.yml
```


The load balancer will forward all TCP traffic for ports 1883 and 8883.

#### One-way TLS

The simplest way to configure MQTTS is to make your MQTT load balancer (AWS NLB) to act as a TLS termination point.
This way we setup the one-way TLS connection, where the traffic between your devices and load balancers is encrypted, and the traffic between your load balancer and MQTT Transport is not encrypted.
There should be no security issues, since the ALB/NLB is running in your VPC.
The only major disadvantage of this option is that you can't use "X.509 certificate" MQTT client credentials, since information about client certificate is not transferred from the load balancer to the SENTIENT MQTT Transport service.

To enable the **one-way TLS**:

Use [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) to create or import SSL certificate. Note your certificate ARN.

Edit the load balancer configuration and replace *YOUR_MQTTS_CERTIFICATE_ARN* with your certificate ARN:

```bash
nano receipts/mqtts-load-balancer.yml
```


Execute the following command to deploy plain https load balancer:

```bash
kubectl apply -f receipts/mqtts-load-balancer.yml
```


#### Two-way TLS

The more complex way to enable MQTTS is to obtain valid (signed) TLS certificate and configure it in the MQTT Transport. The main advantage of this option is that you may use it in combination with "X.509 certificate" MQTT client credentials.

To enable the **two-way TLS**:

Follow [this guide](/docs/user-guide/mqtt-over-ssl/) to create a **.pem** file with the SSL certificate.
Store the file as *server.pem* in the working directory.

You'll need to create a config-map with your PEM file, you can do it by calling command:

```
kubectl create configmap tb-mqtts-config \
 --from-file=server.pem=YOUR_PEM_FILENAME \
 --from-file=mqttserver_key.pem=YOUR_PEM_KEY_FILENAME \
 -o yaml --dry-run=client | kubectl apply -f -
```


* where **YOUR_PEM_FILENAME** is the name of your **server certificate file**.
* where **YOUR_PEM_KEY_FILENAME** is the name of your **server certificate private key file**. 

Then, uncomment all sections in the 'tb-services.yml' file that are marked with "Uncomment the following lines to enable two-way MQTTS".

Execute command to apply changes:

```
kubectl apply -f tb-services.yml
```


Finally, deploy the "transparent" load balancer:

```bash
kubectl apply -f receipts/mqtt-load-balancer.yml
```


### 10.3. Configure UDP Load Balancer (Optional)

Configure UDP load balancer if you plan to use CoAP or LwM2M protocol to connect devices.

Create UDP load balancer using following command:

```bash
kubectl apply -f receipts/udp-load-balancer.yml
```


The load balancer will forward all UDP traffic for the following ports:

 * 5683 - CoAP server non-secure port
 * 5684 - CoAP server secure DTLS port.
 * 5685 - LwM2M server non-secure port.
 * 5686 - LwM2M server secure DTLS port.
 * 5687 - LwM2M bootstrap server DTLS port.
 * 5688 - LwM2M bootstrap server secure DTLS port.

#### CoAP over DTLS

This type of the load balancer requires you to provision and maintain valid SSL certificate on your own.
Follow the generic [CoAP over DTLS](/docs/user-guide/coap-over-dtls) guide
to configure required environment variables in the *tb-services.yml* file.

#### LwM2M over DTLS

This type of the load balancer requires you to provision and maintain valid SSL certificate on your own.
Follow the generic [LwM2M over DTLS](/docs/user-guide/ssl/lwm2m-over-dtls/) guide
to configure required environment variables in the *tb-services.yml* file.


### 10.4. Configure Edge Load Balancer (Optional)

Configure the Edge load balancer if you plan to connect Edge instances to your SENTIENT server.

To create a TCP Edge load balancer, apply the provided YAML file using the following command:

```bash
kubectl apply -f receipts/edge-load-balancer.yml
```


The load balancer will forward all TCP traffic on port 7070.

After the Edge load balancer is provisioned, you can connect Edge instances to your SENTIENT server.

Before connecting Edge instances, you need to obtain the external IP address of the Edge load balancer. To retrieve this IP address, execute the following command:

```bash
kubectl get services | grep "EXTERNAL-IP\|tb-edge-loadbalancer"
```


You should see output similar to the following:

```
NAME                   TYPE           CLUSTER-IP    EXTERNAL-IP      PORT(S)          AGE
tb-edge-loadbalancer   LoadBalancer   10.44.5.255   104.154.29.225   7070:30783/TCP   85m
```

Make a note of the external IP address and use it later in the Edge connection parameters as **CLOUD_RPC_HOST**.

## Step 11. Validate the setup

### Validate Web UI access

Now you can open SENTIENT web interface in your browser using DNS name of the load balancer.

You can see DNS name (the `ADDRESS` column) of the HTTP load-balancer using command:

```bash
kubectl get ingress
```


You should see the similar picture:

![image](/images/install/cloud/aws-application-loadbalancers.webp)

Use the following default credentials:

- **System Administrator**: sysadmin@sentient.org / sysadmin

If you installed DataBase with demo data (using `--loadDemo` flag) you can also use the following credentials:

- **Tenant Administrator**: tenant@sentient.org / tenant
- **Customer User**: customer@sentient.org / customer

### Validate MQTT/CoAP access

To connect to the cluster via MQTT or COAP you'll need to get corresponding service, you can do it with command:

```bash
kubectl get service
```


You should see the similar picture:

![image](/images/install/cloud/aws-network-loadbalancers.webp)


There are two load-balancers:
- tb-mqtt-loadbalancer-external - for MQTT protocol
- tb-coap-loadbalancer-external - for COAP protocol

Use `EXTERNAL-IP` field of the load-balancers to connect to the cluster.

### Troubleshooting

In case of any issues you can examine service logs for errors.
For example to see SENTIENT node logs execute the following command:

```bash
kubectl logs -f tb-node-0
```


Or use `kubectl get pods` to see the state of the pods.
Or use `kubectl get services` to see the state of all the services.
Or use `kubectl get deployments` to see the state of all the deployments.
See [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) command reference for details.

Merge your local changes with the latest release branch from the repo you have used in the [Step 1](#step-1-clone-sentient-ce-k8s-scripts-repository).


In case when database upgrade is needed, execute the following commands:

```bash
 ./k8s-upgrade-tb.sh --fromVersion=[FROM_VERSION]
```


Where:

- `FROM_VERSION` - from which version upgrade should be started. See [Upgrade Instructions](/docs/user-guide/install/upgrade-instructions) for valid `fromVersion` values. Note, that you have to upgrade versions one by one (for example 3.6.1 -> 3.6.2 -> 3.6.3 etc). 

Note: You may optionally stop the tb-node pods while you run the upgrade of the database. This will cause downtime, but will make sure that the DB state will be consistent after the update.
Most of the updates do not require the tb-nodes to be stopped.

Once completed, execute deployment of the resources again. This will cause rollout restart of the sentient components with the newest version.

```yaml
./k8s-deploy-resources.sh
```


## Cluster deletion

Execute the following command to delete all SENTIENT pods:

```bash
./k8s-delete-resources.sh
```


Execute the following command to delete all SENTIENT pods and configmaps:

```bash
./k8s-delete-all.sh
```


Execute the following command to delete EKS cluster (you should change the name of the cluster and zone):

```bash
eksctl delete cluster -r us-east-1 -n sentient -w
```


## Next steps
