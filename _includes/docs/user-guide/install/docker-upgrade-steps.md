{% assign current_version = include.version %}

1. Change the version of the `sentient/tb-node` in the `docker-compose.yml` file to the **{{ current_version }}**.

2. Execute the following commands:

{% if include.skipUpgrade %}

```bash
docker pull sentient/tb-node:{{ current_version }}
docker compose stop sentient-ce 
docker compose up -d
```
{: .copy-code}

{% else %}

```bash
docker pull sentient/tb-node:{{ current_version }}
docker compose stop sentient-ce
docker compose run --rm -e UPGRADE_TB=true sentient-ce 
docker compose up -d
```
{: .copy-code}

{% endif %} 
