---
layout: docwithnav-pe-mqtt-broker
title: Deploy ST-RMQTT PE Cluster on AWS with Kubernetes
description: Deploy ST-RMQTT PE Cluster on AWS with Kubernetes

st-rmqtt-rds-set-up:
  0:
    image: /images/mqtt-broker/install/aws-rds-vpc.png
    title: 'AWS RDS Connectivity - choose VPC with the name of your cluster'
  1:
    image: /images/mqtt-broker/install/aws-rds-vpc-sg.png
    title: 'AWS RDS SG - choose "eksctl-st-rmqtt-cluster-ClusterSharedNodeSecurityGroup-*" security group'
  2:
    image: /images/mqtt-broker/install/aws-rds-default-database.png
    title: 'AWS RDS Additional config - type "sentient_mqtt_broker" for the initial database name'

st-rmqtt-msk-set-up:
  0:
    image: /images/mqtt-broker/install/aws-msk-creation.png
    title: 'AWS MSK - create cluster'

st-rmqtt-msk-configuration:
  0:
    image: /images/mqtt-broker/install/aws-msk-vpc.png
    title: 'AWS MSK - choose ST-RMQTT cluster’s VPC'
  1:
    image: /images/mqtt-broker/install/aws-msk-vpc-sg.png
    title: 'AWS MSK - choose "eksctl-st-rmqtt-cluster-ClusterSharedNodeSecurityGroup-*" security group'
  2:
    image: /images/mqtt-broker/install/aws-msk-security.png
    title: 'AWS MSK - enable Plaintext communication between clients and brokers'

st-rmqtt-redis-set-up:
  0:
    image: /images/mqtt-broker/install/aws-redis-create.png
    title: 'AWS ElastiCache - create Valkey cluster'
  1:
    image: /images/mqtt-broker/install/aws-redis-cluster-settings.png
    title: 'AWS ElastiCache - choose 8.x engine version and appropriate Node type'
  2:
    image: /images/mqtt-broker/install/aws-redis-connectivity.png
    title: 'AWS ElastiCache - choose ST-RMQTT VPC and private subnets'  
  3:
    image: /images/mqtt-broker/install/aws-redis-advanced.png
    title: 'AWS ElastiCache - choose "eksctl-st-rmqtt-cluster-ClusterSharedNodeSecurityGroup-*" security group'

st-rmqtt-rds-link-configure:
  0:
    image: /images/mqtt-broker/install/aws-rds-endpoint.png
    title: 'AWS RDS Details'

st-rmqtt-msk-link-configure:
  0:
    image: /images/mqtt-broker/install/aws-msk-arn.png
    title: 'AWS MSK Details'
    
st-rmqtt-redis-link-configure:
  0:
    image: /images/mqtt-broker/install/aws-redis-result.png
    title: 'AWS ElastiCache Details'

---

{% assign docsPrefix = "pe/" %}
{% assign st-rmqttSuffix = "PE" %}
{% include docs/mqtt-broker/install/cluster/aws-cluster-setup.md %}
