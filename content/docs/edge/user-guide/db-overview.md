+++
title = "Edge Dashboards Overview"
description = "Edge Dashboards Overview"

[extra]
status = "imported"
checked = ""
source = "docs/edge/user-guide/db-overview.md"
+++
## Overview

The **Edge Dashboards** are robust and effective tools for local monitoring and management of IoT data. They can function and display data in real time, even when there is no connection to the Cloud. The data can be synchronized with the server when the connection is restored.

The **Edge Dashboards** are designed in the same way as the [Platform (Cloud) Dashboards](/docs/user-guide/dashboards/). Please read the Platform Dashboard documentation for a general understanding of its functionality.

## Dashboard Provision to SENTIENT Edge

The dashboards can be created and managed on the **SENTIENT server**, and then [provisioned](/docs/edge/getting-started/#step-5-provision-dashboard-to-sentient-gateway) to the **Edge instance**. This approach enables the simultaneous deployment of changes to all Edge instances.

You can verify that the Dashboard is provisioned: 


1. Ensure that you have previously created and configured Dashboards on the <b>SENTIENT Server</b> and then go to the <b>Edge management > Instances</b> section and open the <b>"Manage dashboard"</b> page. View all Dashboards already deployed, or click the <b>"+"</b> icon to deploy the Dashboard to the <b>Edge</b> instance.

1. To verify that the Dashboards are available, log in to your <b>Edge</b> instance and go to the <b>Dashboards</b> section.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/dashboards/1-server-edge-dashboards.webp" alt="Ensure that you have previously created and configured Dashboards on the SENTIENT Server and then go to the Edge management > Instances section and open the &quot;Manage dashboard&quot; page. View all Dashboards already deployed, or click the &quot;+&quot; icon to deploy the Dashboard to the Edge instance." loading="lazy"><figcaption>Ensure that you have previously created and configured Dashboards on the <b>SENTIENT Server</b> and then go to the <b>Edge management > Instances</b> section and open the <b>"Manage dashboard"</b> page. View all Dashboards already deployed, or click the <b>"+"</b> icon to deploy the Dashboard to the <b>Edge</b> instance.</figcaption></figure><figure><img src="/images/edge/user-guide/dashboards/2-edge-edge-dashboards.webp" alt="To verify that the Dashboards are available, log in to your Edge instance and go to the Dashboards section." loading="lazy"><figcaption>To verify that the Dashboards are available, log in to your <b>Edge</b> instance and go to the <b>Dashboards</b> section.</figcaption></figure></div>


## The Edge Dashboard Creation And Management

You can also create and manage **Dashboards** right from the **Edge** itself. All changes are automatically propagated to the Platform when connected. 

To **create** the Edge Dashboard on your **SENTIENT Edge** instance, do the following:


1. Log in to your <b>SENTIENT Edge</b> instance and navigate to the <b>“Dashboards”</b> section, then click the <b>“+”</b> icon and select the <b>“Create new dashboard”</b> option.

1. In the pop-up window, enter a dashboard <b>title</b>. Other fields are optional. Click the <b>"Add"</b> button to proceed

1. Once you have created the dashboard, it will be automatically opened. You can configure it by adding widgets. Click the <b>"Save"</b> button to save the changes.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/dashboards/5-create-new-dashboard.webp" alt="Log in to your SENTIENT Edge instance and navigate to the “Dashboards” section, then click the “+” icon and select the “Create new dashboard” option." loading="lazy"><figcaption>Log in to your <b>SENTIENT Edge</b> instance and navigate to the <b>“Dashboards”</b> section, then click the <b>“+”</b> icon and select the <b>“Create new dashboard”</b> option.</figcaption></figure><figure><img src="/images/edge/user-guide/dashboards/6-new-dashboard-dialog.webp" alt="In the pop-up window, enter a dashboard title. Other fields are optional. Click the &quot;Add&quot; button to proceed" loading="lazy"><figcaption>In the pop-up window, enter a dashboard <b>title</b>. Other fields are optional. Click the <b>"Add"</b> button to proceed</figcaption></figure><figure><img src="/images/edge/user-guide/dashboards/7-add-widgets-and-save.webp" alt="Once you have created the dashboard, it will be automatically opened. You can configure it by adding widgets. Click the &quot;Save&quot; button to save the changes." loading="lazy"><figcaption>Once you have created the dashboard, it will be automatically opened. You can configure it by adding widgets. Click the <b>"Save"</b> button to save the changes.</figcaption></figure></div>


You can learn about **Widgets** [here](/docs/user-guide/widgets/).

Read more about the **Dashboard toolbar** [here](/docs/user-guide/dashboards/#dashboard-toolbar).

To verify that the changes are successfully propagated: 


1. Create, configure or make any changes to the Dashboard on the <b>Edge</b> instance.

1. Log in to your <b>SENTIENT Server</b> and go to the <b>Dashboards</b> section to see that the changes have been applied to the <b>SENTIENT Server</b>. Make sure you are connected to the internet.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/dashboards/3-new-dashboard-on-edge.webp" alt="Create, configure or make any changes to the Dashboard on the Edge instance." loading="lazy"><figcaption>Create, configure or make any changes to the Dashboard on the <b>Edge</b> instance.</figcaption></figure><figure><img src="/images/edge/user-guide/dashboards/4-new-dashboard-on-server.webp" alt="Log in to your SENTIENT Server and go to the Dashboards section to see that the changes have been applied to the SENTIENT Server. Make sure you are connected to the internet." loading="lazy"><figcaption>Log in to your <b>SENTIENT Server</b> and go to the <b>Dashboards</b> section to see that the changes have been applied to the <b>SENTIENT Server</b>. Make sure you are connected to the internet.</figcaption></figure></div>


If you have multiple instances of **SENTIENT Edge**, you can delete the Dashboard on one of them *without affecting* it on the other instances. To delete the **Dashboard** from all **SENTIENT Edge** instances *at once*, delete it from your SENTIENT platform.

### Assign/Remove Customers

Before you assign customers to the Dashboard, make sure that you have assigned them to the **SENTIENT Edge** instance first. You can read more about Customers [here](/docs/user-guide/ui/customers/).

To **assign/unassign** customers to the **Edge Dashboard**, do the following:


1. Log in to your <b>SENTIENT Edge</b> instance and go to the <b>Dashboards</b> section. Click the <b>“Manage assigned customers”</b> button for the dashboard you want to assign a customer to.

1. Select the customers from the drop-down list to assign them or click the <b>“x”</b> icon to remove them from the dashboard. Click the <b>"Update"</b> button to confirm the assignment or removal.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/dashboards/8-assign-customers.webp" alt="Log in to your SENTIENT Edge instance and go to the Dashboards section. Click the “Manage assigned customers” button for the dashboard you want to assign a customer to." loading="lazy"><figcaption>Log in to your <b>SENTIENT Edge</b> instance and go to the <b>Dashboards</b> section. Click the <b>“Manage assigned customers”</b> button for the dashboard you want to assign a customer to.</figcaption></figure><figure><img src="/images/edge/user-guide/dashboards/9-add-customers-dialog.webp" alt="Select the customers from the drop-down list to assign them or click the “x” icon to remove them from the dashboard. Click the &quot;Update&quot; button to confirm the assignment or removal." loading="lazy"><figcaption>Select the customers from the drop-down list to assign them or click the <b>“x”</b> icon to remove them from the dashboard. Click the <b>"Update"</b> button to confirm the assignment or removal.</figcaption></figure></div>


## Next Steps
