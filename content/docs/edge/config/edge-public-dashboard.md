+++
title = "Edge Public Dashboard Configuration Guide"
description = "Detailed configuration instructions for the public dashboard on SENTIENT Edge"

[extra]
status = "imported"
checked = ""
source = "docs/edge/config/edge-public-dashboard.md"
+++
### Overview

**Public dashboard configuration** allows access to the dashboard without authentication, i.e., the dashboard can be viewed by anyone who has the URL link. 

In **SENTIENT Edge**, **public dashboards** work similarly to how they do on the **SENTIENT Server**. 

**Edge-Specific Considerations:**

* **Edge public dashboards** remain available within the local network, even if the internet is unavailable or restricted.
* **Edge public dashboards** is accessible through the Edge's **local URL link**. The public URL will typically be in the format:
```bash
http://Edge-IP:8080/dashboards/dashboard-id
```
* Even if the connection to the **SENTIENT Server** is lost, the **public dashboard** will continue to operate using real-time device data from the **Edge**.
* **Edge** will synchronize any updates or changes with the central **SENTIENT Server**, once connectivity is restored.

Read more about **Edge Dashboards creation and management** [here](/docs/edge/user-guide/db-overview/).

Read more about **Dashboard widgets** [here](/docs/user-guide/widgets/).


### Making Dashboard Public


<div class="st-callout info">


To have access to the data of the devices, assets and entity views through the public link, make these entities public as well.


</div>


1. Log in to the <b>ThingsBord Edge</b> and go to the <b>Dashboards</b> section. Create and configure a dashboard. To make the dashboard public, click the <b>"Make public"</b> button.

1. The dashboard is now public. To share the dashboard, click the <b>"Copy public link"</b> button.

1. Next time you can find the link in the <b>Dashboard details</b> window.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/public-dashboard/1-dashboard-section.webp" alt="Log in to the ThingsBord Edge and go to the Dashboards section. Create and configure a dashboard. To make the dashboard public, click the &quot;Make public&quot; button." loading="lazy"><figcaption>Log in to the <b>ThingsBord Edge</b> and go to the <b>Dashboards</b> section. Create and configure a dashboard. To make the dashboard public, click the <b>"Make public"</b> button.</figcaption></figure><figure><img src="/images/edge/user-guide/public-dashboard/2-copy-the-link.webp" alt="The dashboard is now public. To share the dashboard, click the &quot;Copy public link&quot; button." loading="lazy"><figcaption>The dashboard is now public. To share the dashboard, click the <b>"Copy public link"</b> button.</figcaption></figure><figure><img src="/images/edge/user-guide/public-dashboard/3-dashboard-details.webp" alt="Next time you can find the link in the Dashboard details window." loading="lazy"><figcaption>Next time you can find the link in the <b>Dashboard details</b> window.</figcaption></figure></div>


#### Making Dashboard Private


1. Log in to the <b>ThingsBord Edge</b> and go to the <b>Dashboards</b> section. To make the dashboard private, click the <b>"Make private"</b> button.

1. To confirm the change, click the <b>"Yes"</b> button in the pop-up window.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/public-dashboard/4-dashboard-section.webp" alt="Log in to the ThingsBord Edge and go to the Dashboards section. To make the dashboard private, click the &quot;Make private&quot; button." loading="lazy"><figcaption>Log in to the <b>ThingsBord Edge</b> and go to the <b>Dashboards</b> section. To make the dashboard private, click the <b>"Make private"</b> button.</figcaption></figure><figure><img src="/images/edge/user-guide/public-dashboard/5-confirm-going-private.webp" alt="To confirm the change, click the &quot;Yes&quot; button in the pop-up window." loading="lazy"><figcaption>To confirm the change, click the <b>"Yes"</b> button in the pop-up window.</figcaption></figure></div>


### Next steps
