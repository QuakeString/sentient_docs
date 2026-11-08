+++
title = "OceanConnect Integration"
description = "Huawei OceanConnect Integration guide"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/integrations/ocean-connect.md"
+++
<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only **Professional Edition** supports **Platform Integrations** feature.<br>
Use **SENTIENT Cloud** or [**install**](/docs/installation/) your own platform instance.


</div>

Huawei OceanConnect Integration allows to stream data from OceanConnect platform to SENTIENT and converts binary device payloads to the SENTIENT format.


{{ diagram(name="ocean-connect-integration") }}

Configuration steps:
  
 - Create new Integration of type "OceanConnect"
 
![image](/images/user-guide/integrations/oceanconnect.webp) 

 - Copy HTTP endpoint URL from the auto-generated field in the form (highlighted with red)
 - Review official OceanConnect [documentation](https://support.huawei.com/enterprise/en/cloud-computing/oceanconnect-platform-pid-22559503)
  to learn how to provision the endpoint URL from the previous step
