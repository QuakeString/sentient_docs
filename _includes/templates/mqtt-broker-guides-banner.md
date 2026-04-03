{% if currentGuide != "GettingStartedGuide" %}
- [**Getting started guide**](/docs/{{docsPrefix}}mqtt-broker/getting-started/) - This guide provide quick overview of ST-RMQTT.
{% endif %}
{% if currentGuide != "InstallationGuides" %}
- [**Installation guides**](/docs/{{docsPrefix}}mqtt-broker/install/installation-options/) - Learn how to set up ST-RMQTT using Docker or deploy it in K8S environments on AWS, GCP, and Azure.
{% endif %}
{% if currentGuide != "SecurityGuide" %}
- [**Security guide**](/docs/{{docsPrefix}}mqtt-broker/security/overview/) - Learn how to enable authentication and authorization for MQTT clients.
{% endif %}
{% if currentGuide != "ConfigurationGuide" %}
- [**Configuration guide**](/docs/{{docsPrefix}}mqtt-broker/install/config/) - Learn about ST-RMQTT configuration files and parameters.
{% endif %}
{% if currentGuide != "MQTTClientTypeGuide" %}
- [**MQTT client type guide**](/docs/{{docsPrefix}}mqtt-broker/user-guide/mqtt-client-type/) - Learn about ST-RMQTT client types.
{% endif %}
{% if currentGuide != "TBIntegrationGuide" %}
- [**Integration with SENTIENT**](/docs/{{docsPrefix}}mqtt-broker/user-guide/integrations/how-to-connect-sentient-to-st-rmqtt/) - Learn about how to integrate ST-RMQTT with SENTIENT.
{% endif %}
