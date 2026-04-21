Bring up all containers (including SENTIENT ANALYTICS containers) as a single Compose project in detached mode, then follow the SENTIENT logs:

```bash
docker compose -f docker-compose.yml -f docker-compose-sentient-analytics.yml up -d
docker compose -f docker-compose.yml -f docker-compose-sentient-analytics.yml logs -f sentient-pe
```
{: .copy-code}
