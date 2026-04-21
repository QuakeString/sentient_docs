Open the Docker Compose file with SENTIENT services:

```text
docker-compose.yml
```
{: .copy-code}

Make sure that:

* the following services are present in the file:
    * sentient-analytics
    * sentient-analytics-python-executor
    * sentient-analytics-postgres
* the following volumes are present in the file:
    * sentient-analytics-conf
    * sentient-analytics-data
    * sentient-analytics-python-executor-conf
    * sentient-analytics-python-executor-data
    * sentient-analytics-postgres-data

If any of them are missing, update your Docker Compose file according to the [SENTIENT Docker installation instructions](/docs/user-guide/install/pe/docker-windows#step-2-choose-sentient-queue-service).

Your Docker Compose file should be similar to the one shown in the instructions.
