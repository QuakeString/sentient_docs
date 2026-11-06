+++
title = "SENTIENT setup using AWS infrastructure"
description = "SENTIENT IoT platform setup with Kubernetes in AWS EKS"
aliases = ["/docs/user-guide/install/cluster/aws-cluster-setup", "/docs/user-guide/install/kubernetes/"]

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/cluster/aws-eks-setup.md"
+++
Here you can find scripts for different deployment scenarios using AWS EKS platform:

- [**monolith**](/docs/user-guide/install/cluster/aws-monolith-setup/) - simplistic deployment of SENTIENT with only one service and
  Amazon RDS for PostgreSQL;
- [**microservices**](/docs/user-guide/install/cluster/aws-microservices-setup/) (recommended) - deployment of SENTIENT in a microservices mode 
  with Amazon RDS for PostgreSQL, Amazon MSK for Kafka
  and ElastiCache for Redis;
