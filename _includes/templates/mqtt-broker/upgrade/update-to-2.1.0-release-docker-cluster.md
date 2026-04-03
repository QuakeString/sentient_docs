ST-RMQTT v2.1.0 introduces enhancements, including a new Integration Executor microservice and bumped versions for third-party services.

#### Add Integration Executor microservice

This release adds support for external integrations via the new [Integration Executor](/docs/{{docsPrefix}}mqtt-broker/integrations/) microservice.

For the complete updated `docker-compose.yml`, see the [official example here](https://github.com/sentient/st-rmqtt/blob/release-2.1.0/docker/docker-compose.yml).

To retrieve the latest configuration files, including those for Integration Executors, pull the updates from the release branch. 
Follow the steps outlined in the [run upgrade instructions](#run-upgrade) up to the execution of the upgrade script (do not execute **.sh** commands yet).

After successfully pulling the updates, create Docker volumes to store Integration Executor logs by running:

```bash
./scripts/docker-create-volumes.sh
```
{: .copy-code}

Upon running the command, you should see output similar to the following:

```text
user@user:~/st-rmqtt/docker$ ./scripts/docker-create-volumes.sh

st-rmqtt-ie1-logs
st-rmqtt-ie2-logs
st-rmqtt-ie-config
```

#### Update third-party services

{% include templates/mqtt-broker/upgrade/upgrade-third-parties-for-2.1.0-release-cluster.md %}
