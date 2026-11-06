+++
title = "Monolith setup using GCP infrastructure"
description = "SENTIENT IoT platform monolith setup with Kubernetes in GKE"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/cluster/gcp-monolith-setup.md"
+++
This guide will help you to set up SENTIENT in monolith mode in GKE. 

## Prerequisites

### Install and configure tools 

To deploy SENTIENT on GKE cluster you'll need to install
[`kubectl`](https://kubernetes.io/docs/tasks/tools/) and [`gcloud`](https://cloud.google.com/sdk/downloads) tools.
See [before you begin](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster#before_you_begin) guide for more info.

Create new Google Cloud Platform project (recommended) or choose existing one. 

Make sure you have selected correct project by executing the following command:

```bash
gcloud init
```


### Enable GCP services

Enable the GKE and SQL services for your project by executing the following command:

```bash
gcloud services enable container.googleapis.com sql-component.googleapis.com sqladmin.googleapis.com
```


## Step 1. Clone SENTIENT K8S scripts repository

Clone the repository and change the working directory to GCP scripts.

```bash
git clone -b release- https://github.com/sentient/sentient-сe-k8s.git
cd sentient-сe-k8s/gcp/monolith
```


## Step 2. Define environment variables


Define environment variables that you will use in various commands later in this guide.

We assume you are using Linux. Execute the following command:

```bash
export GCP_PROJECT=$(gcloud config get-value project)
export GCP_REGION=us-central1
export GCP_ZONE=us-central1-a
export GCP_NETWORK=default
export TB_CLUSTER_NAME=tb-ce
export TB_DATABASE_NAME=tb-db
echo "You have selected project: $GCP_PROJECT, region: $GCP_REGION, network: $GCP_NETWORK zone: $GCP_ZONE, cluster: $TB_CLUSTER_NAME and database: $TB_DATABASE_NAME"
```


where:

* first line uses gcloud command to fetch your current GCP project id. We will refer to it later in this guide using **GCP_PROJECT**;
* *us-central1* is one of the available compute [regions](https://cloud.google.com/compute/docs/regions-zones#available). We will refer to it later in this guide using **GCP_REGION**;
* *us-central1-a* is one of the available compute [zones](https://cloud.google.com/compute/docs/regions-zones#available). Should match the selected region. We will refer to it later in this guide using **GCP_ZONE**;
* *default* is a default GCP network name; We will refer to it later in this guide using **;GCP_NETWORK**;
* *tb-ce* is the name of your cluster. You may input a different name. We will refer to it later in this guide using **$TB_CLUSTER_NAME**;
* *tb-db* is the name of your database server. You may input a different name. We will refer to it later in this guide using **TB_DATABASE_NAME**;

## Step 3. Configure and create GKE cluster

Create a zonal cluster with **1** node of **e2-standard-4** machine type.

Execute the following command (recommended):

```bash
gcloud container clusters create $TB_CLUSTER_NAME \
--release-channel stable \
--zone $GCP_ZONE \
--node-locations $GCP_ZONE \
--network=$GCP_NETWORK \
--enable-ip-alias \
--num-nodes=1 \
--node-labels=role=main \
--machine-type=e2-standard-4
```


Alternatively, you may use [this](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster) guide for custom cluster setup.

## Step 4. Update the context of kubectl


Update the context of kubectl using command:

```
gcloud container clusters get-credentials $TB_CLUSTER_NAME --zone $GCP_ZONE
```


## Step 5. Provision Databases

### Step 5.1 Google Cloud SQL (PostgreSQL) Instance


#### 5.1 Prerequisites

Enable service networking to allow your K8S cluster connect to the DB instance:

```bash
gcloud services enable servicenetworking.googleapis.com --project=$GCP_PROJECT

gcloud compute addresses create google-managed-services-$GCP_NETWORK \
--global \
--purpose=VPC_PEERING \
--prefix-length=16 \
--network=projects/$GCP_PROJECT/global/networks/$GCP_NETWORK

gcloud services vpc-peerings connect \
--service=servicenetworking.googleapis.com \
--ranges=google-managed-services-$GCP_NETWORK \
--network=$GCP_NETWORK \
--project=$GCP_PROJECT
    
```


#### 5.2 Create database server instance

Create the PostgreSQL instance with database version "**PostgreSQL 16**" and the following recommendations:

* use the same region where your K8S cluster **GCP_REGION** is located;
* use the same VPC network where your K8S cluster **GCP_REGION** is located;
* use private IP address to connect to your instance and disable public IP address;
* use highly available DB instance for production and single zone instance for development clusters;
* use at least 2 vCPUs and 7.5 GB RAM, which is sufficient for most of the workloads. You may scale it later if needed;

Execute the following command:

```bash

gcloud beta sql instances create $TB_DATABASE_NAME \
--database-version=POSTGRES_16 \
--region=$GCP_REGION --availability-type=regional \
--no-assign-ip --network=projects/$GCP_PROJECT/global/networks/$GCP_NETWORK \
--cpu=2 --memory=7680MB
```


Alternatively, you may follow [this](https://cloud.google.com/sql/docs/postgres/create-instance) guide to configure your database.

Note your IP address (**YOUR_DB_IP_ADDRESS**) from command output. Successful command output should look similar to this:

```
Created [https://sqladmin.googleapis.com/sql/v1beta4/projects/YOUR_PROJECT_ID/instances/$TB_DATABASE_NAME].
NAME                        DATABASE_VERSION  LOCATION       TIER              PRIMARY_ADDRESS  PRIVATE_ADDRESS  STATUS
$TB_DATABASE_NAME           POSTGRES_16       us-central1-f  db-custom-2-7680  35.192.189.68    -                RUNNABLE
```

#### 5.3 Set database password

Set password for your new database server instance:

```bash
gcloud sql users set-password postgres \
--instance=$TB_DATABASE_NAME \
--password=secret
```


where:

* *instance* is the name of your database server instance;
* *secret* is the password. You **should** input a different password. We will refer to it later in this guide using **YOUR_DB_PASSWORD**;

#### 5.4 Create database

Create "sentient" database inside your postgres database server instance:

```bash
gcloud sql databases create sentient --instance=$TB_DATABASE_NAME
```


where, *sentient* is the name of your database. You may input a different name. We will refer to it later in this guide using **YOUR_DB_NAME**;

### Step 5.2 Cassandra (optional)

Using Cassandra is an optional step. 
We recommend to use Cassandra if you plan to insert more than 5K data points per second or would like to optimize storage space.

#### Provision additional node groups

Provision additional node groups that will be hosting Cassandra instances. 
You may change the machine type. At least 4 vCPUs and 16GB of RAM is recommended.

We will create **3** separate node pools with **1** node per zone. 
Since we plan to use zonal disks, we don't want k8s to launch a pod on the node where the corresponding disk is not available.
Those zones will have the same node label. We will use this label to target deployment of our stateful set.

```bash
gcloud container node-pools create cassandra1 --cluster=$TB_CLUSTER_NAME --zone=$GCP_ZONE --node-locations=$GCP_ZONE1 \
--node-labels=role=cassandra --num-nodes=1 --min-nodes=1 --max-nodes=1 --machine-type=e2-standard-4
gcloud container node-pools create cassandra2 --cluster=$TB_CLUSTER_NAME --zone=$GCP_ZONE --node-locations=$GCP_ZONE2 \
--node-labels=role=cassandra --num-nodes=1 --min-nodes=1 --max-nodes=1 --machine-type=e2-standard-4
gcloud container node-pools create cassandra3 --cluster=$TB_CLUSTER_NAME --zone=$GCP_ZONE --node-locations=$GCP_ZONE3 \
--node-labels=role=cassandra --num-nodes=1 --min-nodes=1 --max-nodes=1 --machine-type=e2-standard-4
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

Edit the SENTIENT DB settings file and add Cassandra settings


```bash
echo "  DATABASE_TS_TYPE: cassandra" >> tb-node-db-configmap.yml
echo "  CASSANDRA_URL: cassandra:9042" >> tb-node-db-configmap.yml
echo "  CASSANDRA_LOCAL_DATACENTER: $GCP_REGION"  >> tb-node-db-configmap.yml
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
                        'us-central1' : '3' \
                    };\""
```


## Step 6. Installation

Edit "tb-node-db-configmap.yml" and replace **YOUR_DB_IP_ADDRESS** and **YOUR_DB_PASSWORD** with the values you have obtained during [step 5](#step-5-provision-google-cloud-sql-postgresql-instance).

```bash
nano tb-node-db-configmap.yml
```


Execute the following command to run installation:

```bash
./k8s-install-tb.sh --loadDemo
```


where:

- `--loadDemo` - optional argument. Whether to load additional demo data.

After this command finish you should see the next line in the console:

```
Installation finished successfully!
```


## Step 7. Starting

Execute the following command to deploy resources:

```
./k8s-deploy-resources.sh
```


After few minutes you may call `kubectl get pods`. If everything went fine, you should be able to
see `tb-node-0` pod in the `READY` state.

## Step 8. Configure Load Balancers

### 8.1 Configure HTTP(S) Load Balancer


Configure HTTP(S) Load Balancer to access web interface of your SENTIENT instance. Basically you have 3 possible options of configuration:

* http - Load Balancer without HTTPS support. Recommended **for development.**
  The only advantage is simple configuration and minimum costs. May be good option for development server but definitely not suitable for production.
* https - Load Balancer with HTTPS support. Recommended **for production.** Acts as an SSL termination point.
  You may easily configure it to issue and maintain a valid SSL certificate. Automatically redirects all non-secure (HTTP) traffic to secure (HTTPS) port.
* transparent - Load Balancer that simply forwards traffic to http and https ports of the SENTIENT. Requires you to provision and maintain valid SSL certificate.
  Useful for production environments that can't tolerate the LB to be an SSL termination point.

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


The process of configuring the load balancer using Google-managed SSL certificates is described on the official [documentation page](https://cloud.google.com/kubernetes-engine/docs/how-to/managed-certs).
The instructions below are extracted from the official documentation. Make sure you read [prerequisites](https://cloud.google.com/kubernetes-engine/docs/how-to/managed-certs#prerequisites) carefully before proceeding.

```bash
gcloud compute addresses create sentient-http-lb-address --global
```


Replace the *PUT_YOUR_DOMAIN_HERE* with valid domain name in the *https-load-balancer.yml* file:

```bash
nano receipts/https-load-balancer.yml
```


Execute the following command to deploy secure http load balancer:

```bash
 kubectl apply -f receipts/https-load-balancer.yml
```


The process of load balancer provisioning may take some time. You may periodically check the status of the load balancer using the following command:

```bash
kubectl get ingress
```


Once provisioned, you should see similar output:

```
NAME                   CLASS    HOSTS   ADDRESS         PORTS   AGE
tb-https-loadbalancer   <none>   *       34.111.24.134   80      7m25s
```

Now, **assign the domain name** you have used to the load balancer IP address (the one you see instead of 34.111.24.134 in the command output).

Check that the domain name is configured correctly using dig:

```bash
dig YOUR_DOMAIN_NAME
```


Sample output:

```
; <<>> DiG 9.11.3-1ubuntu1.16-Ubuntu <<>> YOUR_DOMAIN_NAME
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12513
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;YOUR_DOMAIN_NAME.	IN	A

;; ANSWER SECTION:
YOUR_DOMAIN_NAME. 36 IN	A	34.111.24.134

;; Query time: 0 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Fri Nov 19 13:00:00 EET 2021
;; MSG SIZE  rcvd: 74

```

Once assigned, wait for the Google-managed certificate to finish provisioning. This might take up to 60 minutes. You can check the status of the certificate using the following command:

```bash
kubectl describe managedcertificate managed-cert
```


Certificate will be eventually provisioned if you have configured domain records properly.

Once provisioned, you may use your domain name to access Web UI (over https) and connect your devices via [HTTP API](/docs/reference/http-api/).


<div class="st-callout warn">


**NOTE**: The load balancer will redirect all HTTP traffic to HTTPS. Devices that do not support HTTPS will not be able to connect to SENTIENT.
If you would like to support such devices, you may either deploy separate load balancer for HTTP transport (recommended)
or disable the redirect behavior by changing the *redirectToHttps* setting in the *https-load-balancer.yml* file.


</div>


#### Transparent Load Balancer

This type of the load balancer requires you to provision and maintain valid SSL certificate on your own.
Follow the generic [HTTP over SSL](/docs/user-guide/ssl/http-over-ssl/#ssl-configuration-using-pem-certificates-file) guide
to configure required environment variables in the *tb-node.yml* file.

Afterwards, setup TCP load balancer to forward traffic from 443 port to corresponding services port 8080.
This version of setup does not support an automatic redirect of http port 80 to https port 443.

```bash
 kubectl apply -f receipts/transparent-http-load-balancer.yml
```

 
### 8.2. Configure MQTT Load Balancer (Optional)


Configure MQTT load balancer if you plan to use MQTT protocol to connect devices.

Create TCP load balancer using following command:

```bash
kubectl apply -f receipts/mqtt-load-balancer.yml
```


The load balancer will forward all TCP traffic for ports 1883 and 8883.

#### MQTT over SSL

This type of the load balancer requires you to provision and maintain valid SSL certificate on your own.
Follow the generic [MQTT over SSL](/docs/user-guide/mqtt-over-ssl) guide
to configure required environment variables in the *tb-node.yml* file.


### 8.3. Configure UDP Load Balancer (Optional)

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
to configure required environment variables in the *tb-node.yml* file.

#### LwM2M over DTLS

This type of the load balancer requires you to provision and maintain valid SSL certificate on your own.
Follow the generic [LwM2M over DTLS](/docs/user-guide/ssl/lwm2m-over-dtls/) guide
to configure required environment variables in the *tb-node.yml* file.


### 8.4. Configure Edge Load Balancer (Optional)

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

## Step 9. Using

Now you can open SENTIENT web interface in your browser using IP address of the load balancer.

You can see DNS name (the `ADDRESS` column) of the HTTP load-balancer using command:
```
kubectl get ingress
```

You should see the similar picture:

![image](/images/install/cloud/application-loadbalancers.webp)

To connect to the cluster via MQTT or COAP you'll need to get corresponding service, you can do it with command:

```
kubectl get service
```


You should see the similar picture:

![image](/images/install/cloud/network-loadbalancers.webp)

There are two load-balancers:
- tb-mqtt-loadbalancer - for TCP (MQTT) protocol
- tb-udp-loadbalancer - for UDP (COAP/LwM2M) protocol

Use `EXTERNAL-IP` field of the load-balancers to connect to the cluster.

Use the following default credentials:

- **System Administrator**: sysadmin@sentient.org / sysadmin

If you installed database with demo data (using `--loadDemo` flag) you can also use the following credentials:

- **Tenant Administrator**: tenant@sentient.org / tenant
- **Customer User**: customer@sentient.org / customer

In case of any issues you can examine service logs for errors. For example to see SENTIENT node logs execute the following command:

```
kubectl logs -f tb-node-0
```

Or use `kubectl get pods` to see the state of the pod.
Or use `kubectl get services` to see the state of all the services.
Or use `kubectl get deployments` to see the state of all the deployments.
See [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) command reference for details.

Execute the following command to delete **tb-node** and **load-balancers**:

```
./k8s-delete-resources.sh
```

Execute the following command to delete all data (including database):

```
./k8s-delete-all.sh
```

## Upgrading


In case when database upgrade is needed, execute the following commands:

```
 ./k8s-delete-resources.sh
 ./k8s-upgrade-tb.sh --fromVersion=[FROM_VERSION]
 ./k8s-deploy-resources.sh
```

Where:

- `FROM_VERSION` - from which version upgrade should be started. See [Upgrade Instructions](/docs/user-guide/install/upgrade-instructions) for valid `fromVersion` values. Note, that you have to upgrade versions one by one (for example 3.6.1 -> 3.6.2 -> 3.6.3 etc). 

## Next steps
