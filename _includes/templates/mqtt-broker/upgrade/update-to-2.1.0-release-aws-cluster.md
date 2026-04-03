ST-RMQTT v2.1.0 introduces enhancements, including a new Integration Executor microservice and bumped versions for third-party services.

#### Add Integration Executor microservice

This release adds support for external integrations via the new [Integration Executor](/docs/{{docsPrefix}}mqtt-broker/integrations/) microservice.

To retrieve the latest configuration files, including those for Integration Executors, pull the updates from the release branch. 
Follow the steps outlined in the [run upgrade instructions](#run-upgrade) up to the execution of the upgrade script (do not execute **.sh** commands yet).

The `cluster.yml` file has been updated to include the new managed node group specifically for Integration Executor pods.

```yaml
  - name: st-rmqtt-ie
    instanceType: m7a.large
    desiredCapacity: 2
    maxSize: 2
    minSize: 1
    labels: { role: st-rmqtt-ie }
    ssh:
      allow: true
      publicKeyName: 'dlandiak' # Note, use your own public key name here
```

To create it, execute the following command:

```shell
eksctl create nodegroup --config-file=cluster.yml
```
{: .copy-code}

You may choose to skip creating dedicated instances for Integration Executors. 
If so, you can skip this step, but you must update the **nodeSelector** section in the `st-rmqtt-ie.yml` file accordingly.

```yaml
  nodeSelector:
    role: st-rmqtt-ie
```

Change the role from **"st-rmqtt-ie"** to **"st-rmqtt"** to deploy Integration Executor pods on the same AWS EC2 instances as the ST-RMQTT pods.

#### Update third-party services

{% include templates/mqtt-broker/upgrade/upgrade-third-parties-for-2.1.0-release-aws-cluster.md %}
