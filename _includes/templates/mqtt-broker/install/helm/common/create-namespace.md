It's a good practice to create a dedicated namespace for your ST-RMQTT cluster deployment:

```bash
kubectl create namespace st-rmqtt
```
{: .copy-code}

```bash
kubectl config set-context --current --namespace=st-rmqtt
```
{: .copy-code}

This sets st-rmqtt as the default namespace for your current context, so you don’t need to pass --namespace to every
command.