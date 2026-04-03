To customize your ST-RMQTT deployment, first download the default `values.yaml` file from the chart:

```bash
helm show values st-rmqtt-helm-chart/st-rmqtt-cluster > values.yaml
```
{: .copy-code}

{% capture installation-option %}

Do not modify `installation.installDbSchema` directly in the `values.yaml`.
This parameter is only required during the first installation to initialize the ST-RMQTT database schema.
Instead, we will pass it explicitly using `--set` option in the `helm install` command.

{% endcapture %}
{% include templates/info-banner.md content=installation-option %}