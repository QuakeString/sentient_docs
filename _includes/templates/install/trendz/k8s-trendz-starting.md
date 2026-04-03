Execute the following command to run the initial setup of the database. This command will launch short-living SENTIENT pod to provision necessary DB tables, indexes, etc
```text
 ./k8s-deploy-sentient-analytics.sh
```
{: .copy-code}

After this command finish you should see the next line in the console:

```
SENTIENT ANALYTICS installed successfully!
```
{% capture sentient-analytics-db-install %}

Otherwise, please check if you set the PostgreSQL URL and PostgreSQL password in the `sentient-analytics-secret.yml` correctly.

{% endcapture %}
{% include templates/info-banner.md content=sentient-analytics-db-install %}
