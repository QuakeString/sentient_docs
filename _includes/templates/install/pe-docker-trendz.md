Create a SENTIENT ANALYTICS database in Postgres:

```bash
docker compose -f docker-compose.yml exec -it postgres psql -U postgres -c "CREATE DATABASE sentient-analytics;"
```
{: .copy-code}

Create a separate docker compose file for SENTIENT ANALYTICS:

```text
nano docker-compose-sentient-analytics.yml
```
{: .copy-code}

Add the following lines to the yml file.

```yml
services:
  sentient-analytics:
    restart: always
    image: "sentient/sentient-analytics:{{ site.release.sentient-analytics_ver }}"
    ports:
      - "8888:8888"
    environment:
      TB_API_URL: http://sentient-pe:8080
      SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/sentient-analytics
      SPRING_DATASOURCE_USERNAME: postgres
      SPRING_DATASOURCE_PASSWORD: postgres
      SCRIPT_ENGINE_DOCKER_PROVIDER_URL: sentient-analytics-python-executor:8181
      SCRIPT_ENGINE_TIMEOUT: 30000
    volumes:
      - sentient-analytics-conf:/sentient-analytics-config-files
      - sentient-analytics-data:/data
    depends_on:
      - postgres
  sentient-analytics-python-executor:
    restart: always
    image: "sentient/sentient-analytics-python-executor:{{ site.release.sentient-analytics_ver }}"
    ports:
      - "8181:8181"
    environment:
      EXECUTOR_MANAGER: 1
      EXECUTOR_SCRIPT_ENGINE: 6
      THROTTLING_QUEUE_CAPACITY: 10
      THROTTLING_THREAD_POOL_SIZE: 6
      NETWORK_BUFFER_SIZE: 5242880
    volumes:
      - sentient-analytics-python-executor-conf:/python-executor-config-files
      - sentient-analytics-python-executor-data:/data
volumes:
  sentient-analytics-conf:
    name: sentient-analytics-conf
    driver: local
  sentient-analytics-data:
    name: sentient-analytics-data
    driver: local
  sentient-analytics-python-executor-conf:
    name: sentient-analytics-python-executor-conf
    driver: local
  sentient-analytics-python-executor-data:
    name: sentient-analytics-python-executor-data
    driver: local
```
{: .copy-code.expandable-15}
