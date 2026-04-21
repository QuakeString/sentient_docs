{% assign current_version = include.version %}

1. Create a dump of your database:
    ```bash
    docker compose exec postgres sh -c "pg_dump -U postgres sentient-analytics > /var/lib/postgresql/data/sentient-analytics_dump"
    ```
    {: .copy-code}

2. Change the version of the `sentient/sentient-analytics` and `sentient/sentient-analytics-python-executor` in the `docker-compose.yml` file to the **{{ current_version }}**.

3. Execute the following commands:
{% if include.skipUpgrade %}
    ```bash
    docker pull sentient/sentient-analytics:{{ current_version }}
    docker compose stop sentient-analytics
    docker compose up -d
    ```
    {: .copy-code}
{% else %}
    ```bash
    docker pull sentient/sentient-analytics:{{ current_version }}
    docker compose stop sentient-analytics
    docker compose run --rm -e UPGRADE_SENTIENT_ANALYTICS=true sentient-analytics
    docker compose up -d
    ```
    {: .copy-code}
{% endif %} 