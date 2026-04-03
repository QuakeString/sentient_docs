### Upgrade from ST-RMQTT CE to ST-RMQTT PE (v2.2.0)

To upgrade your existing **ST-RMQTT Community Edition (CE)** to **ST-RMQTT Professional Edition (PE)**, ensure you are running the latest **ST-RMQTT CE {{site.release.broker_full_ver}}** version before starting the process.
Merge your current configuration with the latest [ST-RMQTT PE K8S scripts](https://github.com/sentient/st-rmqtt-pe-k8s/tree/{{ site.release.broker_branch }}).
Do not forget to [configure the license key](#configure-the-license-key).

Run the following commands, including the upgrade script to migrate PostgreSQL database data from CE to PE:

```bash
./k8s-delete-st-rmqtt.sh
./k8s-upgrade-st-rmqtt.sh --fromVersion=ce
./k8s-deploy-st-rmqtt.sh
```
{: .copy-code}
