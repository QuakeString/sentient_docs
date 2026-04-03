{% assign current_version = include.version %}

1. Change the version of the `sentient/tb-pe-node` and `sentient/tb-pe-web-report` in the `docker-compose.yml` file to the **{{ current_version }}**.

2. Execute the following commands:

{% if include.skipUpgrade %}

```bash
docker pull sentient/tb-pe-node:{{ current_version }}
docker pull sentient/tb-pe-web-report:{{ current_version }}
docker compose stop sentient-pe
docker compose up -d
```
{: .copy-code}

{% else %}

```bash
docker pull sentient/tb-pe-node:{{ current_version }}
docker pull sentient/tb-pe-web-report:{{ current_version }}
docker compose stop sentient-pe
docker compose run --rm -e UPGRADE_TB=true sentient-pe
docker compose up -d
```
{: .copy-code}

{% endif %}
