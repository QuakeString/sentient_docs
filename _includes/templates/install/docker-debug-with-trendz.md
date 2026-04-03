If something goes wrong, you can stream the SENTIENT container logs in real time:

```bash
docker compose -f docker-compose.yml -f docker-compose-sentient-analytics.yml logs -f sentient-pe
```
{: .copy-code}

Stream the SENTIENT ANALYTICS container logs in real time:

```bash
docker compose -f docker-compose.yml -f docker-compose-sentient-analytics.yml logs -f sentient-analytics
```
{: .copy-code}

Bring down every container defined in your Compose files:

```bash
docker compose -f docker-compose.yml -f docker-compose-sentient-analytics.yml down
```
{: .copy-code}

Launch all services in detached mode:

```bash
docker compose -f docker-compose.yml -f docker-compose-sentient-analytics.yml up -d
```
{: .copy-code}
