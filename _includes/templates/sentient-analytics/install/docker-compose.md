```yml
services:
  sentient-analytics:
    profiles: ['sentient-analytics']
    restart: always
    image: "sentient/sentient-analytics:{{ site.release.sentient-analytics_ver }}"
    ports:
      - "8888:8888"
    environment:
      SPRING_DATASOURCE_URL: jdbc:postgresql://sentient-analytics-postgres:5432/sentient-analytics
      SPRING_DATASOURCE_USERNAME: postgres
      SPRING_DATASOURCE_PASSWORD: postgres
      SCRIPT_ENGINE_DOCKER_PROVIDER_URL: sentient-analytics-python-executor:8181
      SCRIPT_ENGINE_TIMEOUT: 30000
    volumes:
      - sentient-analytics-conf:/sentient-analytics-config-files
      - sentient-analytics-data:/data
    depends_on:
      - sentient-analytics-postgres
  sentient-analytics-python-executor:
    profiles: ['sentient-analytics']
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
  sentient-analytics-postgres:
    profiles: ['sentient-analytics']
    restart: always
    image: "postgres:16"
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: sentient-analytics
      POSTGRES_PASSWORD: postgres
    volumes:
      - sentient-analytics-postgres-data:/var/lib/postgresql/data
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
  sentient-analytics-postgres-data:
    name: sentient-analytics-postgres-data
    driver: local
```
{: .copy-code}

Where:

- `8888:8888` - connect local port 8888 to exposed internal HTTP port 8888
- `sentient-analytics-conf:/sentient-analytics-config-files` - mounts the volume `sentient-analytics-conf` to SENTIENT ANALYTICS directory with the configuration files
- `sentient-analytics-data:/data` - mounts the volume `sentient-analytics-data` to SENTIENT ANALYTICS data directory
- `sentient-analytics-postgres-data:/var/lib/postgresql/data` - mounts the volume `sentient-analytics-postgres-data` to Postgres data directory
- `sentient-analytics` - name of the SENTIENT ANALYTICS Docker service
- `--restart always` - automatically start SENTIENT ANALYTICS in case of system reboot and restart in case of failure.
- `sentient/sentient-analytics:{{ site.release.sentient-analytics_ver }}` - SENTIENT ANALYTICS docker image
- `sentient/sentient-analytics-python-executor:{{ site.release.sentient-analytics_ver }}` - SENTIENT ANALYTICS python script executor docker image
- `SCRIPT_ENGINE_TIMEOUT` - Python script execution timeout
