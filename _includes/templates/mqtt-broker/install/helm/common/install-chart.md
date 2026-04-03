Now you’re ready to install ST-RMQTT using the Helm chart.
Make sure you're in the same directory as your customized `values.yaml` file.

```bash
helm install my-st-rmqtt-cluster st-rmqtt-helm-chart/st-rmqtt-cluster \
  -f values.yaml \
  --set installation.installDbSchema=true
```
{: .copy-code}

{% capture installation-tip %}

`my-st-rmqtt-cluster` is the Helm release name. You can change it to any name of your choice, which will be used to reference this deployment in future Helm commands.

{% endcapture %}
{% include templates/info-banner.md content=installation-tip %}

Once the deployment process is completed, you should see output similar to the following:

```bash
NAME: my-st-rmqtt-cluster
LAST DEPLOYED: Wed Mar 26 17:42:49 2025
NAMESPACE: st-rmqtt
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
ST-RMQTT Cluster my-st-rmqtt-cluster will be deployed in few minutes.
Info:
Namespace: st-rmqtt
```