Define environment variables that you will use in various commands later in this guide.

We assume you are using Linux. Execute the following command:

```bash
export AKS_RESOURCE_GROUP=ST-RMQTTResources
export AKS_LOCATION=eastus
export AKS_GATEWAY=st-rmqtt-gateway
export TB_CLUSTER_NAME=st-rmqtt-cluster
export TB_DATABASE_NAME=st-rmqtt-db
echo "You variables ready to create resource group $AKS_RESOURCE_GROUP in location $AKS_LOCATION 
and cluster in it $TB_CLUSTER_NAME with database $TB_DATABASE_NAME"
```
{: .copy-code}

where:

* ST-RMQTTResources - a logical group in which Azure resources are deployed and managed. We will refer to it later in this guide using **$AKS_RESOURCE_GROUP**;
* eastus - is the location where you want to create resource group. We will refer to it later in this guide using **$AKS_LOCATION**. You can see all locations list by executing `az account list-locations`;
* st-rmqtt-gateway - the name of Azure application gateway;
* st-rmqtt-cluster - cluster name. We will refer to it later in this guide using **$TB_CLUSTER_NAME**;
