+++
title = "Microservices setup using AKS infrastructure"
description = "SENTIENT IoT platform microservices setup with Kubernetes in Azure AKS"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/cluster/azure-microservices-setup.md"
+++
This guide will help you to setup SENTIENT in microservices mode in Azure AKS.

## Prerequisites

### Install and configure tools 

To deploy SENTIENT on EKS cluster you'll need to install [`kubectl`](https://kubernetes.io/docs/tasks/tools/), 
 [`az`](https://docs.microsoft.com/en-us/cli/azure/) tools.

After installation is done you need to login in cli using az login command.

```
az login
```


## Step 1. Clone SENTIENT K8S scripts repository

```bash
git clone -b release- https://github.com/sentient/sentient-ce-k8s.git
cd sentient-ce-k8s/azure/microservices
```


## Step 2. Define environment variables

Define environment variables that you will use in various commands later in this guide.

We assume you are using Linux. Execute the following command:

```bash
export AKS_RESOURCE_GROUP=SENTIENTResources
export AKS_LOCATION=eastus
export AKS_GATEWAY=tb-gateway
export TB_CLUSTER_NAME=tb-cluster
export TB_DATABASE_NAME=tb-db
export TB_REDIS_NAME=tb-redis
echo "You variables ready to create resource group $AKS_RESOURCE_GROUP in location $AKS_LOCATION 
and cluster in it $TB_CLUSTER_NAME with database $TB_DATABASE_NAME"
```


where: 
   - myResourceGroup - a logical group in which Azure resources are deployed and managed. We will refer to it later in this guide using ***AKS_RESOURCE_GROUP*** ;
   - *eastus* - is location where you want to create resource group. We will refer to it later in this guide using ***AKS_LOCATION***;
    You can see all locations list executing *az account list-locations*;
   - *tb-gateway* - the name of Azure application gateway;  
   - *tb-cluster* - cluster name. We will refer to it later in this guide using ***TB_CLUSTER_NAME*** ;
   - *tb-db* is the name of your database server. You may input a different name. We will refer to it later in this guide using TB_DATABASE_NAME;

## Step 3. Configure and create AKS cluster


Before creation AKS cluster we need to create Azure Resource Group, we will use Azure CLI for this 
```
az group create --name $AKS_RESOURCE_GROUP --location $AKS_LOCATION
```


To see more info about `az group` please you can use [this](https://docs.microsoft.com/en-us/cli/azure/group). 

After we created Resource group we can create AKS cluster in it using: 
```
az aks create --resource-group $AKS_RESOURCE_GROUP \
    --name $TB_CLUSTER_NAME \
    --generate-ssh-keys \
    --enable-addons ingress-appgw \
    --appgw-name $AKS_GATEWAY \
    --appgw-subnet-cidr "10.2.0.0/16" \
    --node-vm-size Standard_DS3_v2 \
    --node-count 3
```


`az aks create` has two required parameters - `name` and `resource-group`(we use variable that we set earlier)
and a lot not required parameters(will use defaults values) few of them are:

  - ***node-count*** - Number of nodes in the Kubernetes node pool. After creating a cluster, you can change the size of its node pool with az aks scale (default value is 3);
  - ***enable-addons*** - Enable the Kubernetes addons in a comma-separated list (use az aks addon list to get avaliable addons list );
  - ***node-osdisk-size*** - OS disk type to be used for machines in a given agent pool: Ephemeral or Managed. Defaults to 'Ephemeral' when possible in conjunction with VM size and OS disk size. May not be changed for this pool after creation;
  - ***node-vm-size (or -s)*** - Size of Virtual Machines to create as Kubernetes nodes (default value is Standard_DS2_v2);
  - ***generate-ssh-keys*** - Generate SSH public and private key files if missing. The keys will be stored in the ~/.ssh directory. 

From the command above we add AKS addon for [ApplicationGateway](https://docs.microsoft.com/en-us/azure/application-gateway/). We will use this gateway as Path-Based Load Balancer for Sentient Infrastructure

Full list af `az aks create` options you can see [here](https://docs.microsoft.com/en-us/cli/azure/aks?view=azure-cli-latest#az_aks_create)


Alternatively, you may use [this](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough-portal) guide for custom cluster setup.


## Step 4. Update the context of kubectl

When claster created we can connect kubectl to it using
```
az aks get-credentials --resource-group $AKS_RESOURCE_GROUP --name $TB_CLUSTER_NAME
```


Fot validation you can execute command
```
kubectl get nodes
```


You should see cluster`s nodes list

## Step 5. Provision Databases

### 5.3. Create Azure Database for PostgreSQL servers

You’ll need to set up PostgreSQL on Azure. SENTIENT will use it as a main database to store devices, dashboards, rule chains and device telemetry.

You may follow [this](https://docs.microsoft.com/en-us/azure/postgresql/flexible-server/quickstart-create-server-portal) guide, but take into account the following requirements:
   * Keep your postgresql password in a safe place. We will refer to it later in this guide using YOUR_RDS_PASSWORD;
   * Make sure your Azure Database for PostgreSQL version is latest 16.x;
   * Make sure your Azure Database for PostgreSQL instance is accessible from the SENTIENT cluster;
   * Make sure you use “sentient” as initial database name;
    
and recomendations:
   * Use "High availability" enabled. It enables a lot of useful settings by default;

Another way by which you can create Azure Database for PostgreSQL is use az tool 
(don't forget to replace 'POSTGRESS_USER' and 'POSTGRESS_PASS' with your username and password):

```bash
az postgres flexible-server create --location $AKS_LOCATION --resource-group $AKS_RESOURCE_GROUP \
  --name $TB_DATABASE_NAME --admin-user POSTGRESS_USER --admin-password POSTGRESS_PASS \
  --public-access 0.0.0.0 --storage-size 32 \
  --version 12 -d sentient
```


`az postgres flexible-server create` has a lot of parameters few of them are: 

  - ***location***  - Location. Values from: az account list-locations;
  - ***resource-group*** (or -g) - Name of resource group;
  - ***name*** - Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters; 
  - ***admin-user*** - Administrator username for the server. Once set, it cannot be changed; 
  - ***admin-password***  - The password of the administrator. Minimum 8 characters and maximum 128 characters. Password must contain characters from three of the following categories: English uppercase letters, English lowercase letters, numbers, and non-alphanumeric characters; 
  - ***public-access*** - Determines the public access. Enter single or range of IP addresses to be included in the allowed list of IPs. IP address ranges must be dash-separated and not contain any spaces. Specifying 0.0.0.0 allows public access from any resources deployed within Azure to access your server. Setting it to "None" sets the server in public access mode but does not create a firewall rule;
  - ***storage-size*** - The storage capacity of the server. Minimum is 32 GiB and max is 16 TiB;
  - ***version*** - Server major version. 
  - ***high-availability*** - nable or disable high availability feature. Default value is Disabled. High availability can only be set during flexible server create time (accepted values: Disabled, Enabled. default value: Disabled);
  - ***database-name*** (or -d) - The name of the database to be created when provisioning the database server.

You can see full parameters list [here](https://docs.microsoft.com/en-us/cli/azure/postgres/flexible-server?view=azure-cli-latest#az_postgres_flexible_server_create).

Example of response: 
```
{
  "connectionString": "postgresql://postgres:postgres@$tb-db.postgres.database.azure.com/postgres?sslmode=require",
  "databaseName": "sentient",
  "firewallName": "AllowAllAzureServicesAndResourcesWithinAzureIps_2021-11-17_15-45-6",
  "host": "tb-db.postgres.database.azure.com",
  "id": "/subscriptions/daff3288-1d5d-47c7-abf0-bfb7b738a18c/resourceGroups/myResourceGroup/providers/Microsoft.DBforPostgreSQL/flexibleServers/sentient",
  "location": "East US",
  "password": "postgres",
  "resourceGroup": "myResourceGroup",
  "skuname": "Standard_D2s_v3",
  "username": "postgres",
  "version": "12"
}
```


Note the value of **host** from the command output (*tb-db.postgres.database.azure.com* in our case). 
Also note username and password (*postgres*) from the command.

Edit the database settings file and replace *YOUR_AZURE_POSTGRES_ENDPOINT_URL* with the **host** value,
*YOUR_AZURE_POSTGRES_USER* and *YOUR_AZURE_POSTGRES_PASSWORD* with the correct values:

```bash
nano tb-node-db-configmap.yml
```


### 5.2. Cassandra

Using Cassandra is an optional step. 
We recommend to use Cassandra if you plan to insert more than 5K data points per second or would like to optimize storage space.

#### Provision additional node pools

Provision additional node pools that will be hosting Cassandra instances. 
You may change the machine type. At least 4 vCPUs and 16GB of RAM is recommended.

We will create **3** separate node pools with **1** node per zone. 
Since we plan to use zonal disks, we don't want k8s to launch a pod on the node where the corresponding disk is not available.
Those zones will have the same node label. We will use this label to target deployment of our stateful set.

So,  define **3** node pools in three zones for your location:

```bash
az aks nodepool add --resource-group $AKS_RESOURCE_GROUP --cluster-name $TB_CLUSTER_NAME --name tbcassandra1 --node-count 1 --zones 1 --labels role=cassandra
az aks nodepool add --resource-group $AKS_RESOURCE_GROUP --cluster-name $TB_CLUSTER_NAME --name tbcassandra2 --node-count 1 --zones 2 --labels role=cassandra
az aks nodepool add --resource-group $AKS_RESOURCE_GROUP --cluster-name $TB_CLUSTER_NAME --name tbcassandra3 --node-count 1 --zones 3 --labels role=cassandra
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

Edit the SENTIENT DB settings file and add Cassandra settings:


```bash
echo "  DATABASE_TS_TYPE: cassandra" >> tb-node-db-configmap.yml
echo "  CASSANDRA_URL: cassandra:9042" >> tb-node-db-configmap.yml
echo "  CASSANDRA_LOCAL_DATACENTER: dc1"  >> tb-node-db-configmap.yml
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
                        'dc1' : '3' \
                    };\""
```


## Step 6. Azure Cache for Valkey (optional)

SENTIENT uses cache to improve performance and avoid frequent DB reads.
By default, deployment already uses the local Valkey cache. Azure does not provide a managed Valkey cluster, however, instead of the default deployment, you can set up your own Valkey cluster according to the [Azure documentation](https://learn.microsoft.com/en-us/azure/aks/valkey-overview).


<div class="st-callout info">


Starting with **SENTIENT v4.0.0**, Valkey 8.x is the officially supported version.
Valkey remains compatible with Redis 7.2.x, so the configuration with Redis will work.
However, Redis 7.2.x is only available in the Enterprise or Enterprise Flash SKUs.
The Basic, Standard, and Premium SKUs still only support **Redis 6.x**.
You can find the Redis Enterprise installation guide here:
[Create a Redis Enterprise cache](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/quickstart-create-redis-enterprise)


</div>


Edit the `thirdparty.yml` file, find the StatefulSet section named `tb-valkey`, and set the `spec.replicas` value to 0.

Once your Valkey cluster is ready, you will need to replace the endpoint in the configuration file. 
Edit `tb-cache-configmap.yml` and replace **REDIS_HOST** value with Redis endpoint if you are using standalone Valkey. 
If you have deployed Valkey in cluster mode, replace **REDIS_HOST** with:
```yaml
REDIS_CONNECTION_TYPE: cluster
REDIS_NODES: (Comma-separated list of "host:port" pairs to bootstrap from)
```

## Step 7. Installation

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

Otherwise, please check if you set the PostgreSQL URL in the `tb-node-db-configmap.yml` correctly.

## Step 8. Starting

Execute the following command to deploy SENTIENT services:

```
 ./k8s-deploy-resources.sh
```


After few minutes you may call `kubectl get pods`. If everything went fine, you should be able to see `tb-node-0` pod in the `READY` state.

After few minutes you may call kubectl get pods. If everything went fine, you should be able to see tb-node-0 pod in the READY state.

You should also deploy the transport microservices. Omit the protocols that you don’t use in order to save resources:

***HTTP Transport (optional)***
```
kubectl apply -f transports/tb-http-transport.yml
```

***MQTT transport (optional)***
```
kubectl apply -f transports/tb-mqtt-transport.yml
```

***CoAP transport (optional)***
```
kubectl apply -f transports/tb-coap-transport.yml
```

***LwM2M transport (optional)***
```
kubectl apply -f transports/tb-lwm2m-transport.yml
```

***SNMP transport (optional)***
```
kubectl apply -f transports/tb-snmp-transport.yml
```


## Step 9. Configure Load Balancers

### 9.1. Configure HTTP(S) Load Balancer
Configure HTTP(S) Load Balancer to access web interface of your SENTIENT instance. Basically you have 3 possible options of configuration:

   - http - Load Balancer without HTTPS support. Recommended for development. The only advantage is simple configuration and minimum costs. May be good option for development server but definitely not suitable for production.
   - https - Load Balancer with HTTPS support. Recommended for production. Acts as an SSL termination point. You may easily configure it to issue and maintain a valid SSL certificate. Automatically redirects all non-secure (HTTP) traffic to secure (HTTPS) port.
   
See links/instructions below on how to configure each of the suggested options.

### HTTP Load Balancer

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

Now, you may use the address (the one you see instead of 34.111.24.134 in the command output) to access HTTP web UI (port 80) and connect your devices via HTTP API Use the following default credentials:

- **System Administrator**: sysadmin@sentient.org / sysadmin
- **Tenant Administrator**: tenant@sentient.org / tenant
- **Customer User**: customer@sentient.org / customer

### HTTPS Load Balancer

For using ssl certificates we can add our certificate directly in Azure ApplicationGateWay using command:
```
az network application-gateway ssl-cert create \
   --resource-group $(az aks show --name $TB_CLUSTER_NAME --resource-group $AKS_RESOURCE_GROUP --query nodeResourceGroup | tr -d '"') \
   --gateway-name $AKS_GATEWAY\
   --name SENTIENTHTTPCert \
   --cert-file YOUR_CERT \
   --cert-password YOUR_CERT_PASS
```


After we added certificate to Application Load balancer we can execute: 
```
kubectl apply -f receipts/https-load-balancer.yml
```


The process of load balancer provisioning may take some time. You may periodically check the status of the load balancer using the following command:

```
kubectl get ingress
```


Once provisioned, you should see similar output:
```
NAME                   CLASS    HOSTS   ADDRESS         PORTS   AGE
tb-https-loadbalancer   <none>   *       34.111.24.134   80      7m25s
```


<div class="st-callout warn">


**NOTE**: The load balancer will redirect all HTTP traffic to HTTPS. Devices that do not support HTTPS will not be able to connect to SENTIENT.
If you would like to support such devices, you may either deploy separate load balancer for HTTP transport (recommended)
or disable the redirect behavior by changing the *appgw.ingress.kubernetes.io/ssl-redirect* setting in the *https-load-balancer.yml* file.


</div>


### 9.2. Configure MQTT Load Balancer (Optional)


Configure MQTT load balancer if you plan to use MQTT protocol to connect devices.

Create TCP load balancer using following command:

```bash
kubectl apply -f receipts/mqtt-load-balancer.yml
```


The load balancer will forward all TCP traffic for ports 1883 and 8883.

#### MQTT over SSL

This type of the load balancer requires you to provision and maintain valid SSL certificate on your own.
Follow the generic [MQTT over SSL](/docs/user-guide/mqtt-over-ssl) guide
to configure required environment variables in the *transport/tb-mqtt-transport.yml* file.


### 9.3. Configure CoAP Load Balancer (Optional)


Configure CoAP load balancer if you plan to use CoAP protocol to connect devices.

Create CoAP load balancer using following command:

```bash
kubectl apply -f receipts/coap-load-balancer.yml
```


The load balancer will forward all UDP traffic for the following ports:

 * 5683 - CoAP server non-secure port
 * 5684 - CoAP server secure DTLS port.

#### CoAP over DTLS

This type of the load balancer requires you to provision and maintain valid SSL certificate on your own.
Follow the generic [CoAP over DTLS](/docs/user-guide/coap-over-dtls) guide
to configure required environment variables in the *transport/tb-coap-transport.yml* file.


### 9.4. Configure LwM2M Load Balancer (Optional)


Configure LwM2M load balancer if you plan to use LwM2M protocol to connect devices.

Create LwM2M UDP load balancer using following command:

```bash
kubectl apply -f receipts/lwm2m-load-balancer.yml
```


The load balancer will forward all UDP traffic for the following ports:

 * 5685 - LwM2M server non-secure port.
 * 5686 - LwM2M server secure DTLS port.
 * 5687 - LwM2M bootstrap server DTLS port.
 * 5688 - LwM2M bootstrap server secure DTLS port.

#### LwM2M over DTLS

This type of the load balancer requires you to provision and maintain valid SSL certificate on your own.
Follow the generic [LwM2M over DTLS](/docs/user-guide/ssl/lwm2m-over-dtls/) guide
to configure required environment variables in the *transport/tb-lwm2m-transport.yml* file.


### 9.5. Configure Edge Load Balancer (Optional)

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

## Step 10. Using

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
