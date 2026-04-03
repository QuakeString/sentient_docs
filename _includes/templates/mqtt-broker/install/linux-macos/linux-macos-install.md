{% if docsPrefix == null %}

```shell
wget https://raw.githubusercontent.com/sentient/st-rmqtt/{{ site.release.broker_branch }}/msa/st-rmqtt/configs/st-rmqtt-install-and-run.sh &&
sudo chmod +x st-rmqtt-install-and-run.sh && ./st-rmqtt-install-and-run.sh
```
{: .copy-code}

{% else %}

```shell
wget https://raw.githubusercontent.com/sentient/st-rmqtt-pe-docker-compose/{{ site.release.broker_branch }}/basic/st-rmqtt-install-and-run.sh &&
sudo chmod +x st-rmqtt-install-and-run.sh && ./st-rmqtt-install-and-run.sh
```
{: .copy-code}

{% endif %}
