* TOC
{:toc}

This guide will help you set up ST-RMQTT {{st-rmqttSuffix}} in cluster mode using Minikube.

## Prerequisites

You need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
If you don't have Minikube installed, please follow [these instructions](https://kubernetes.io/docs/setup/learning-environment/minikube/).

{% if docsPrefix == null %}
## Clone ST-RMQTT repository

```bash
git clone -b {{ site.release.broker_branch }} https://github.com/sentient/st-rmqtt.git
cd st-rmqtt/k8s/minikube
```
{: .copy-code}

{% else %}
## Clone ST-RMQTT PE K8S repository

```bash
git clone -b {{ site.release.broker_branch }} https://github.com/sentient/st-rmqtt-pe-k8s.git
cd st-rmqtt-pe-k8s/minikube
```
{: .copy-code}
{% endif %}

## Installation

To install ST-RMQTT {{st-rmqttSuffix}}, execute the following command:

```bash
./k8s-install-st-rmqtt.sh
```
{: .copy-code}

{% include templates/mqtt-broker/install/cluster-common/configure-license-key.md %}

## Running

Execute the following command to deploy ST-RMQTT {{st-rmqttSuffix}}:

```bash
./k8s-deploy-st-rmqtt.sh
```
{: .copy-code}

After a while when all resources will be successfully started you can open `http://{your-cluster-ip}:30001` in your browser (e.g. **http://192.168.49.2:30001**).
You can check your cluster IP using the following command:

```bash
minikube ip
```
{: .copy-code}

{% include templates/mqtt-broker/login.md %}

## Logs, delete statefulsets and services

In case of any issues, you can examine service logs for errors.
For example, to see ST-RMQTT node logs execute the following commands:

1) Get the list of the running st-rmqtt pods:

```bash
kubectl get pods -l app=st-rmqtt
```
{: .copy-code}

2) Fetch logs of the st-rmqtt pod:

```bash
kubectl logs -f ST-RMQTT_POD_NAME
```
{: .copy-code}

Where:

- `ST-RMQTT_POD_NAME` - st-rmqtt pod name obtained from the list of the running st-rmqtt pods.

Or use the next command to see the state of all the pods.

```bash
kubectl get pods
```
{: .copy-code}

Use the next command to see the state of all the services.

```bash
kubectl get services
```
{: .copy-code}

Use the next command to see the state of all the deployments.

```bash
kubectl get deployments
```
{: .copy-code}

Use the next command to see the state of all the statefulsets.

```bash
kubectl get statefulsets
```
{: .copy-code}

See [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) command reference for more details.

Execute the following command to delete ST-RMQTT nodes:

```bash
./k8s-delete-st-rmqtt.sh
```
{: .copy-code}

Execute the following command to delete all resources (including the databases):

```bash
./k8s-delete-all.sh
```
{: .copy-code}

## Upgrading

{% include templates/mqtt-broker/upgrade/upgrading.md %}

### Backup and restore (Optional)

While backing up your PostgreSQL database is highly recommended, it is optional before proceeding with the upgrade.
{% if docsPrefix == null %} For further guidance, follow the [next instructions](https://github.com/sentient/st-rmqtt/blob/main/k8s/minikube/backup-restore/README.md).
{% else %} For further guidance, follow the [next instructions](https://github.com/sentient/st-rmqtt-pe-k8s/blob/master/minikube/backup-restore/README.md).
{% endif %}

{% if docsPrefix == null %}

### Upgrade to 2.2.0

In this release, the MQTT authentication mechanism was migrated from YAML/env configuration into the database.
During upgrade, ST-RMQTT needs to know which authentication providers are enabled in your deployment.
This information is provided through environment variables passed to the **upgrade pod**.

The upgrade script requires a file named **`database-setup.yml`** that explicitly defines these variables.
Environment variables from your `tb-broker.yml` file are not applied during the upgrade — only the values in `database-setup.yml` will be used.

> **Tips**
> If you use only Basic authentication, set `SECURITY_MQTT_SSL_ENABLED=false`.
> If you use only X.509 authentication, set `SECURITY_MQTT_BASIC_ENABLED=false` and `SECURITY_MQTT_SSL_ENABLED=true`.

**Supported variables**

* `SECURITY_MQTT_BASIC_ENABLED` (`true|false`)
* `SECURITY_MQTT_SSL_ENABLED` (`true|false`)
* `SECURITY_MQTT_SSL_SKIP_VALIDITY_CHECK_FOR_CLIENT_CERT` (`true|false`) — usually `false`.

Once the file is prepared and the values verified, proceed with the [upgrade process](#run-upgrade).

### Upgrade to 2.1.0

{% include templates/mqtt-broker/upgrade/update-to-2.1.0-release-cluster.md %}

### Run upgrade

In case you would like to upgrade, please pull the recent changes from the latest release branch:

```bash
git pull origin {{ site.release.broker_branch }}
```
{: .copy-code}

{% include templates/mqtt-broker/upgrade/upgrade-to-custom-release.md %}

**Note**: Make sure custom changes of yours if available are not lost during the merge process.

{% include templates/mqtt-broker/install/upgrade-hint.md %}

After that, execute the following command:

{% capture tabspec %}st-rmqtt-upgrade
st-rmqtt-upgrade-without-from-version,Since v2.1.0,shell,resources/upgrade-options/k8s-upgrade-st-rmqtt-without-from-version.sh,/docs/{{docsPrefix}}mqtt-broker/install/cluster/resources/upgrade-options/k8s-upgrade-st-rmqtt-without-from-version.sh
st-rmqtt-upgrade-with-from-version,Before v2.1.0,markdown,resources/upgrade-options/k8s-upgrade-st-rmqtt-with-from-version.md,/docs/{{docsPrefix}}mqtt-broker/install/cluster/resources/upgrade-options/k8s-upgrade-st-rmqtt-with-from-version.md{% endcapture %}
{% include tabs.html %}

{% include templates/mqtt-broker/upgrade/stop-st-rmqtt-pods-before-upgrade.md %}

{% else %}

{% include templates/mqtt-broker/install/cluster-common/k8s-type-upgrade-ce-to-pe.md %}

{% endif %}

## Next steps

{% assign currentGuide = "InstallationGuides" %}{% include templates/mqtt-broker-guides-banner.md %}
