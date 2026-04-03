To ensure high availability and proper scheduling in your EKS-based ST-RMQTT cluster,
you must assign ST-RMQTT components to specific node groups using the `nodeSelector` field in your Helm `values.yml`.

Your `cluster.yml` already defines dedicated node groups with role-based labels.
For example for `st-rmqtt-node` mananged node group you have:

```yaml
labels: { role: st-rmqtt }
```

You must map each component to the appropriate node group using these labels.

Here’s how to explicitly assign each component:

- ST-RMQTT Broker:

```yaml
st-rmqtt:
  nodeSelector:
    role: st-rmqtt
```
{: .copy-code}

- ST-RMQTT Integration Executor:

```yaml
st-rmqtt-ie:
  nodeSelector:
    role: st-rmqtt-ie
```
{: .copy-code}

- Kafka Controller Nodes:

```yaml
kafka:
  controller:
    nodeSelector:
      role: kafka
```
{: .copy-code}

- Redis Cluster Nodes:

```yaml
redis-cluster:
  redis:
    nodeSelector:
      role: redis
```
{: .copy-code}

- PostgreSQL (if not using external DB):

```yaml
postgresql:
  primary:
    nodeSelector:
      role: postgresql

  backup:
    cronjob:
      nodeSelector:
        role: postgresql
```
{: .copy-code}