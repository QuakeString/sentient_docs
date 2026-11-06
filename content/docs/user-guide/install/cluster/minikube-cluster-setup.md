+++
title = "Cluster setup using Minikube"
description = "SENTIENT IoT platform cluster setup with Kubernetes and Minikube guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/cluster/minikube-cluster-setup.md"
+++
This guide will help you to setup SENTIENT in cluster mode using Minikube tool. 

## Prerequisites

SENTIENT Microservices run on the Kubernetes cluster. You need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster. 
If you don't have Minikube installed, please follow [these instructions](https://kubernetes.io/docs/setup/learning-environment/minikube/).

### Enable ingress addon

By default ingress addon is disabled in the Minikube, and available only in cluster providers.
To enable ingress, please execute the following command:

```
minikube addons enable ingress
```


## Step 1. Review the architecture page

Starting SENTIENT v2.2, it is possible to install SENTIENT cluster using new microservices architecture and docker containers. 
See [**microservices**](/docs/reference/msa/) architecture page for more details.

## Step 2. Clone SENTIENT Kubernetes scripts repository

```bash
git clone -b release- https://github.com/sentient/sentient-ce-k8s.git --depth 1
cd sentient-ce-k8s/minikube
```


## Step 3. Configure SENTIENT database

Before performing initial installation you can configure the type of database to be used with SENTIENT.
In order to set database type change the value of `DATABASE` variable in `.env` file to one of the following:

- `postgres` - use PostgreSQL database;
- `hybrid` - use PostgreSQL for entities database and Cassandra for timeseries database;

**NOTE**: According to the database type corresponding kubernetes resources will be deployed (see `postgres.yml` and `cassandra.yml` for details).


<div class="st-callout info">


If you selected `cassandra` as `DATABASE` you can also configure the number of Cassandra nodes (`StatefulSet.spec.replicas` property in `cassandra.yml` config file) and the `CASSANDRA_REPLICATION_FACTOR` in `.env` file. 
If you want to configure `CASSANDRA_REPLICATION_FACTOR` please read Cassandra documentation first.  

It is recommended to have 3 Cassandra nodes with `CASSANDRA_REPLICATION_FACTOR` equal to 2.


</div>


## Step 4. Running

Execute the following command to run installation:

```
./k8s-install-tb.sh --loadDemo
```


Where:

- `--loadDemo` - optional argument. Whether to load additional demo data.

Execute the following command to deploy third-party resources:

```
./k8s-deploy-thirdparty.sh
```


Type **'yes'** when prompted, if you are running SENTIENT in `high-availability` `DEPLOYMENT_TYPE` for the first time or don't have configured Redis cluster.


Execute the following command to deploy SENTIENT resources:

```
./k8s-deploy-resources.sh
```


After a while when all resources will be successfully started you can open `http://{your-cluster-ip}` in your browser (for ex. `http://192.168.99.101`).
You can see your cluster IP using command:

```
minikube ip
```


You should see SENTIENT login page.

Use the following default credentials:

- **System Administrator**: sysadmin@sentient.org / sysadmin

If you installed DataBase with demo data (using `--loadDemo` flag) you can also use the following credentials:

- **Tenant Administrator**: tenant@sentient.org / tenant
- **Customer User**: customer@sentient.org / customer

In case of any issues you can examine service logs for errors.
For example to see SENTIENT node logs execute the following command:

1) Get the list of the running tb-node pods:

```
kubectl get pods -l app=tb-node
```


2) Fetch logs of the tb-node pod:

```
kubectl logs -f [tb-node-pod-name]
```


Where:

- `tb-node-pod-name` - tb-node pod name obtained from the list of the running tb-node pods.

Or use `kubectl get pods` to see the state of all the pods.
Or use `kubectl get services` to see the state of all the services.
Or use `kubectl get deployments` to see the state of all the deployments.
See [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) command reference for details.

Execute the following command to delete all SENTIENT microservices:

```
./k8s-delete-resources.sh
```


Execute the following command to delete all third-party microservices:

```
./k8s-delete-thirdparty.sh
```


Execute the following command to delete all resources (including database):

```
./k8s-delete-all.sh
```


## Upgrading

In case you would like to upgrade, please pull the *latest* changes from `master` branch:
```bash
git pull origin master
```


Then, execute the following commands:

```bash
./k8s-delete-resources.sh
./k8s-upgrade-tb.sh
./k8s-deploy-resources.sh
```


Note, that you have to upgrade versions one by one (for example 4.0.0 -> 4.0.1 -> 4.1.0 etc).


<div class="st-callout info">


<code style="color:black">"--fromVersion"</code> flag is required for earlier upgrade versions (prior to 3.9.1), for example:

`# upgrading to v3.9.0...`<br>
`./k8s-upgrade-tb.sh --fromVersion=3.8.1`

See [Upgrade Instructions](/docs/user-guide/install/upgrade-instructions) for valid <code style="color:black">"fromVersion"</code> values.


</div>


### Migration to Professional Edition

You can also migrate from Community Edition (CE) to Professional Edition (PE) using `./k8s-upgrade-tb.sh` script:

1. Upgrade to the latest CE version.

2. Stop the SENTIENT resources executing the following command:
    ```bash
    ./k8s-delete-resources.sh
    ```
    

3. Merge your configuration with [the latest PE Minikube scripts](https://github.com/sentient/sentient-pe-k8s/tree/release-/minikube). Do not forget to [configure the license key](/docs/user-guide/install/pe/cluster/minikube-cluster-setup/#step-3-obtain-your-license-key).

4. Run the following upgrade script to migrate database data from CE to PE:
    ```bash
    ./k8s-upgrade-tb.sh --fromVersion=CE
    ```
    

5. Execute the following command to deploy SENTIENT resources:
    ```bash
    ./k8s-deploy-resources.sh
    ```
    

## Next steps
