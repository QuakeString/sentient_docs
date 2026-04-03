{% capture peRuleNodeContent %}
Only [**Professional Edition**](/products/sentient-pe/) supports **{{ rulenode }}** Rule Node.<br>
Use [**SENTIENT Cloud**](https://{{hostName}}/signup) or [**install**](/docs/user-guide/install/pe/installation-options/) your own platform instance.
{% endcapture %}
{% include templates/info-banner.md title="Professional Rule Node" content=peRuleNodeContent %}
