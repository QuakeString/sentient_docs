**Note**: You may optionally stop the ST-RMQTT pods while you run the upgrade of the database with the below command.

```bash
./k8s-delete-st-rmqtt.sh
```
{: .copy-code}

This will cause downtime, but will make sure that the DB state will be consistent after the update.
Most of the updates do not require the ST-RMQTT to be stopped.

Once completed, execute deployment of the resources again. This will cause rollout restart of the ST-RMQTT with the newest version.

```bash
./k8s-deploy-st-rmqtt.sh
```
{: .copy-code}