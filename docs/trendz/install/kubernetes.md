---
layout: docwithnav-sentient-analytics
assignees:
- vparomskiy
title: Installing SENTIENT SENTIENT ANALYTICS on Kubernetes
description: Installing SENTIENT SENTIENT ANALYTICS on Kubernetes

sentient-analytics-settings:
  0:
    image: /images/sentient-analytics/install/sync/sentient-analytics-settings-1.png
    title: "Log in to <b>SENTIENT</b> as a <b>Sysadmin</b>."
  1:
    image: /images/sentient-analytics/install/sync/sentient-analytics-settings-2.png
    title: "Open the <b>SENTIENT ANALYTICS Settings</b> page."
  2:
    image: /images/sentient-analytics/install/sync/sentient-analytics-settings-3.png
    title: "If you see the message <b>\"Synchronization completed successfully\"</b>, the synchronization has been completed automatically and no further action is required."
sentient-analytics-sync:
  0:
    image: /images/sentient-analytics/install/sync/sentient-analytics-sync-1.png
    title: "If you see an error message, follow these steps."
  1:
    image: /images/sentient-analytics/install/sync/sentient-analytics-sync-2.png
    title: "Enter the correct <b>SENTIENT ANALYTICS internal URL</b> and <b>SENTIENT internal URL</b>."
  2:
    image: /images/sentient-analytics/install/sync/sentient-analytics-sync-3.png
    title: "Click <b>Save configuration</b>."
  3:
    image: /images/sentient-analytics/install/sync/sentient-analytics-sync-4.png
    title: "Click <b>Retry discovery</b>."
  4:
    image: /images/sentient-analytics/install/sync/sentient-analytics-sync-5.png
    title: "Once the message <b>\"Synchronization completed successfully\"</b> appears, the synchronization is complete."

---
* TOC
{:toc}

This guide describes how to setup SENTIENT ANALYTICS cluster with Kubernetes and Minikube.

## Prerequisites

{% include templates/sentient-analytics/install/sentient-requirements.md %}

You need to have a Kubernetes cluster, and the `kubectl` command-line tool must be configured to communicate with your cluster.
If you don't have Minikube installed, please follow [these instructions](https://kubernetes.io/docs/setup/learning-environment/minikube/).

Configure your cluster by designating a node for the SENTIENT ANALYTICS instance and labeling it with a custom label. Utilize affinity settings to instruct Kubernetes to deploy the SENTIENT ANALYTICS instance on the specified node.
Ensure that the node meets specific CPU and RAM requirements, with the typical usage being around 4 CPU and 8GB RAM. While you can set your own limits, we advise adhering to or exceeding the recommended specifications mentioned earlier.

## Installation Steps

### Step 1. Clone SENTIENT ANALYTICS Kubernetes scripts

```bash
git clone https://github.com/sentient/sentient-analytics-k8s.git --depth 1
cd sentient-analytics-k8s
```
{: .copy-code}

### Step 2. Configure SENTIENT ANALYTICS database

Set up an external Postgresql database instance with an empty database named "sentient-analytics." This instance can be hosted on services like RDS (AWS) or as your stateful deployment.
Ensure you have the following information:

- URL (Example: jdbc:postgresql://sentient-analytics-db-service:5432/sentient-analytics)
- Username (Example: postgres)
- Password (Example: postgres)

Now we can configure the SENTIENT ANALYTICS database by editing the sentient-analytics-secret.yml file:

```bash
nano sentient-analytics-secret.yml
```
{: .copy-code}

```
  SPRING_DATASOURCE_URL: jdbc:postgresql://sentient-analytics-db-service:5432/sentient-analytics
  SPRING_DATASOURCE_USERNAME: postgres
  SPRING_DATASOURCE_PASSWORD: postgres

```

### Step 3. Running

```bash
kubectl apply -f sentient-analytics-namespace.yml
kubectl apply -f sentient-analytics-app-config.yml
kubectl apply -f sentient-analytics-app-db-config.yml
kubectl apply -f sentient-analytics-app-pvc.yml
kubectl apply -f sentient-analytics-app-deployment.yml
kubectl apply -f sentient-analytics-python-executor-config.yml
kubectl apply -f sentient-analytics-python-executor-deployment.yml

```
{: .copy-code}

### Step 4. Check the logs

Now check the logs and be sure that the instance is started successfully.
There should be a next line:

```bash
kubectl logs -f [sentient-analytics-pod-name]

Started SENTIENT ANALYTICSApplication in 5.654 seconds (JVM running for 6.229)
```

Where:

* `sentient-analytics-pod-name` - sentient-analytics pod name obtained from the list of the running sentient-analytics pods.

### Step 5. Set up a load balancer

The last thing is to set up a load balancer to route requests to the SENTIENT ANALYTICS instance. Just update your current load balancer config using reference from the `sentient-analytics-ingress.yml` file.

**Do not apply this file, it is just an example.**
Different environments have different requirements for these configurations, so you need to adjust these settings to your environment.

### Step 6. Sync SENTIENT With SENTIENT ANALYTICS

{% include templates/sentient-analytics/install/sync-with-tb.md %}

## Authentication

{% include templates/sentient-analytics/install/authentication.md %}

## Next steps

{% assign currentGuide = "InstallationOptions" %}{% include templates/trndz-guides-banner.md %}
