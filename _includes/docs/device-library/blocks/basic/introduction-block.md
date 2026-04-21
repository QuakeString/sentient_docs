{% if page.docsPrefix == "pe/edge/" or page.docsPrefix == "edge/" %}
In this guide, you will learn how to [install SENTIENT Edge on a {{deviceName}}](#starting-edge-on-device), [create a device](#create-device-on-sentient-gateway), 
[install the required libraries and tools](#install-required-libraries-and-tools).  
After this, we will [modify our code and upload it to the device](#connect-device-to-sentient-gateway), 
and [check the results of our coding and check data on SENTIENT Edge using imported dashboard](#check-data-on-sentient-gateway).
The device will synchronize with SENTIENT Edge using [client and shared attributes requests functionality](#synchronize-device-state-using-client-and-shared-attribute-requests).      
Additionally, you’ll learn how to control the device using platform features such as [shared attributes](#control-device-using-shared-attributes) and [RPC requests](#control-device-using-rpc).

### Prerequisites

Before proceeding, ensure you have the following requirements in place:  
{{ prerequisites }} {% if page.docsPrefix == "pe/edge/" %}
- SENTIENT Cloud account in ([Europe](https://eu.sentient.cloud/signup){: target="_blank"} or [North America](https://sentient.cloud/signup){: target="_blank"}), or a [local server](/docs/user-guide/install/pe/installation-options/){: target="_blank"} installed on-premises
{% else %}
- [SENTIENT Cloud](https://sentient.invenia.in/installations/){: target="_blank"} account or a [local server](/docs/user-guide/install/installation-options/){: target="_blank"} installed on-premises
{% endif %}

{% else %}

In this guide, we will learn how to [create device on Sentient](#create-device-on-sentient), 
[install required libraries and tools](#install-required-libraries-and-tools).  
After this we will [modify our code and upload it to the device](#connect-device-to-sentient), 
and [check the results of our coding and check data on SENTIENT using imported dashboard](#check-data-on-sentient).
Our device will synchronize with SENTIENT using [client and shared attributes requests functionality](#synchronize-device-state-using-client-and-shared-attribute-requests).      
Of course, we will control our device using provided functionality like [shared attributes](#control-device-using-shared-attributes) or [RPC requests](#control-device-using-rpc).  

### Prerequisites

To continue with this guide, we will need the following:  
{{ prerequisites }} {% if page.docsPrefix == "pe/" %}
- [SENTIENT Cloud (Europe)](https://eu.sentient.cloud/signup){: target="_blank"} or [SENTIENT Cloud (America)](https://sentient.cloud/signup){: target="_blank"}
{% else %}
- [SENTIENT Cloud](https://sentient.invenia.in/installations/){: target="_blank"} account or a [local server](/docs/user-guide/install/installation-options/){: target="_blank"} installed on-premises
{% endif %}

{% endif %}

