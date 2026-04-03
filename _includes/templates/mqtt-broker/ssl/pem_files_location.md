{% capture st-rmqtt_pem_files_location %}
**Make sure the certificate files are reachable by ST-RMQTT process:**

* Docker Compose: mount or use existing volume to */config* folder of the container; Use full file path, e.g. */config/server.pem*;
* K8S: mount separate volume to */https-config* or similar folder. Use full file path, e.g. */https-config/server.pem*.

{% endcapture %}
{% include templates/warn-banner.md content=st-rmqtt_pem_files_location %}
