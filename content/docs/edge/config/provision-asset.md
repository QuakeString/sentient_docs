+++
title = "Edge Assets"
description = "Edge Assets Overview"

[extra]
status = "imported"
checked = ""
source = "docs/edge/config/provision-asset.md"
+++
## Overview

The **Asset entity** is an abstract entity that helps group and manage the IoT ecosystem. **Assets** represent real-world objects such as factories, vehicles, warehouses,  etc., and establish a relational hierarchy between these objects and other entities.
**Edge Assets** enable grouping of Edge entities and visualizing the data they send. This approach applies whenever the devices or transmitted data are specific to a particular Edge.

**Edge Assets** are designed in the same way as the **Cloud Assets**. Please refer to the [Assets documentation](/docs/user-guide/ui/assets/) to gain a general understanding of its functionality.

## Edge Asset Management

The **Asset entity** can be created and configured locally on the **Edge** instance, in the same way as on the **Cloud**. If the **Asset entity** has been created on the **Cloud**, it must be [assigned](/docs/edge/config/provision-asset/#provisioning-from-cloud) to the **Edge** instance before use.

### Creating a New Asset

To create the **Asset entity** on the **Edge**, log in to your instance and go to the **Entities > Assets** section.


1. Click the <b>"+"</b> button and select the <b>“Add new asset”</b> option.<ul><li>The <b>"Import assets"</b> option allows <a href="/docs/user-guide/bulk-provisioning/#bulk-provisioning-overview" target="_blank">bulk deployment</a> using the CSV file.</li></ul>

1. In the <b>“Add asset”</b> pop-up window: <ul><li>Enter the asset name in the <b>“Name”</b> field.</li><li>Select the <a href="/docs/user-guide/asset-profiles/" target="_blank">asset profile</a> in the <b>“Asset profile”</b> field (default: "default").</li><li>Other fields are optional.</li><li>Click the <b>“Add”</b> button.</li></ul>

1. Once created, the <b>Asset</b> will be <b>automatically provisioned</b> to the Cloud.


<div class="st-gallery"><figure><img src="/images/edge/config/edge-asset-ce/1-add-new-asset.webp" alt="Click the &quot;+&quot; button and select the “Add new asset” option.The &quot;Import assets&quot; option allows bulk deployment using the CSV file." loading="lazy"><figcaption>Click the <b>"+"</b> button and select the <b>“Add new asset”</b> option.<ul><li>The <b>"Import assets"</b> option allows <a href="/docs/user-guide/bulk-provisioning/#bulk-provisioning-overview" target="_blank">bulk deployment</a> using the CSV file.</li></ul></figcaption></figure><figure><img src="/images/edge/config/edge-asset-ce/2-fill-in-required-fields.webp" alt="In the “Add asset” pop-up window: Enter the asset name in the “Name” field.Select the asset profile in the “Asset profile” field (default: &quot;default&quot;).Other fields are optional.Click the “Add” button." loading="lazy"><figcaption>In the <b>“Add asset”</b> pop-up window: <ul><li>Enter the asset name in the <b>“Name”</b> field.</li><li>Select the <a href="/docs/user-guide/asset-profiles/" target="_blank">asset profile</a> in the <b>“Asset profile”</b> field (default: "default").</li><li>Other fields are optional.</li><li>Click the <b>“Add”</b> button.</li></ul></figcaption></figure><figure><img src="/images/edge/config/edge-asset-ce/3-asset-provisioned-to-cloud.webp" alt="Once created, the Asset will be automatically provisioned to the Cloud." loading="lazy"><figcaption>Once created, the <b>Asset</b> will be <b>automatically provisioned</b> to the Cloud.</figcaption></figure></div>


### Creating Relations

Several parameters define the [relation hierarchy](/docs/user-guide/entities-and-relations/#relations) between the entities:
* **Direction:** Describes how the entities are associated with each other.
  * **"Outbound relation - From":** Indicates that the **relation originates from the entity (the entity is a source)**.
  * **"Inbound relation - To":** Indicates that the **relation points to the entity (the entity is a recipient)**. 
* **Relation type:** Describes the nature of the connection between the entities.
  * **"Contains":** Indicates that the entity **is a part of another entity** (e.g., _Device A is the part of Asset A_).
  * **"Manages":** Indicates that the entity **is responsible for another entity** (e.g., _Asset A manages Device A_).

To **construct relations** between the Asset and another entity (e.g., _device_), go to the **Entities > Assets** section and do the following:


1. Click on the asset to open the <b>"Asset details"</b> page and select the <b>"Relations"</b> tab. Then, select the <b>"Outbound relation - Direction: From"</b> option.

1. To add the relation, click the <b>"+"(Add)</b> button.<ul><li>On the <b>"Add relation"</b> pop-up window, fill out the following fields:</li><ul><li><b>Relation type:</b> Select the <b>"Manages"</b> option.</li><li><b>To entity:</b> select <b>"Device"</b> as the type and add the corresponding device(s) from the drop-down menu.</li></ul><li>Click the <b>"Add"</b> button.</li></ul>

1. The newly created relations will appear in the <b>"Relations"</b> tab.


<div class="st-gallery"><figure><img src="/images/edge/config/edge-asset-ce/4-relation-tab.webp" alt="Click on the asset to open the &quot;Asset details&quot; page and select the &quot;Relations&quot; tab. Then, select the &quot;Outbound relation - Direction: From&quot; option." loading="lazy"><figcaption>Click on the asset to open the <b>"Asset details"</b> page and select the <b>"Relations"</b> tab. Then, select the <b>"Outbound relation - Direction: From"</b> option.</figcaption></figure><figure><img src="/images/edge/config/edge-asset-ce/5-add-relation.webp" alt="To add the relation, click the &quot;+&quot;(Add) button.On the &quot;Add relation&quot; pop-up window, fill out the following fields:Relation type: Select the &quot;Manages&quot; option.To entity: select &quot;Device&quot; as the type and add the corresponding device(s) from the drop-down menu.Click the &quot;Add&quot; button." loading="lazy"><figcaption>To add the relation, click the <b>"+"(Add)</b> button.<ul><li>On the <b>"Add relation"</b> pop-up window, fill out the following fields:</li><ul><li><b>Relation type:</b> Select the <b>"Manages"</b> option.</li><li><b>To entity:</b> select <b>"Device"</b> as the type and add the corresponding device(s) from the drop-down menu.</li></ul><li>Click the <b>"Add"</b> button.</li></ul></figcaption></figure><figure><img src="/images/edge/config/edge-asset-ce/6-confirm-relations.webp" alt="The newly created relations will appear in the &quot;Relations&quot; tab." loading="lazy"><figcaption>The newly created relations will appear in the <b>"Relations"</b> tab.</figcaption></figure></div>


### Using Relations in Dashboards

Once the relations between the entities are established, they can be **reflected on a dashboard**. Transmitted data from asset-related devices can be **dynamically filtered by relation type** with [aliases](/docs/user-guide/ui/aliases/).

To configure an **alias**, go to the **Dashboards** section and enter the **Edit mode** for a new or existing dashboard. Read on **how to create the dashboard** [here](/docs/edge/user-guide/db-overview/#the-edge-dashboard-creation-and-management).


1. Within the dashboard <b>"Edit mode"</b>, click the <b>"Entity aliases"</b> button to create the alias. In the <b>"Entity aliases"</b> pop-up window, click the <b>"Add alias"</b> button.

1. On the <b>"Add alias"</b> pop-up window, fill out the following fields:<ul><li><b>Alias name:</b> Enter the alias name.</li><li><b>Filter Type:</b> Select the <b>"Relations query"</b> option.</li><p><b>Root entity</b> block:</p><li><b>Type:</b> Select the <b>"Asset"</b> entity.</li><li><b>Asset:</b> Select the asset from the drop-down menu (e.g., <i>"Asset A"</i>).</li><li><b>Direction:</b> Select the <b>"From"</b> option.</li><li><b>Max relation level:</b> Enter the number representing the depth of the entity relations.</li></ul>

1. Scroll down to create the filter in the <b>Relation filters</b> block:<ul><li>Click the <b>"Add filter"</b> button to add conditions to filter data.</li><li><b>Relation type:</b> Select the <b>"Manages"</b> option.</li><li><b>Entity types:</b> Select the <b>"Device"</b> entity type.</li></ul><p>In this way, the data from the devices that are managed by the asset will be displayed on the dashboard.</p><p>Click the <b>"Add"</b> button to add the alias.</p>

1. To save the alias, click the <b>"Save"</b> button.


<div class="st-gallery"><figure><img src="/images/edge/config/edge-asset-ce/7-create-alias.webp" alt="Within the dashboard &quot;Edit mode&quot;, click the &quot;Entity aliases&quot; button to create the alias. In the &quot;Entity aliases&quot; pop-up window, click the &quot;Add alias&quot; button." loading="lazy"><figcaption>Within the dashboard <b>"Edit mode"</b>, click the <b>"Entity aliases"</b> button to create the alias. In the <b>"Entity aliases"</b> pop-up window, click the <b>"Add alias"</b> button.</figcaption></figure><figure><img src="/images/edge/config/edge-asset-ce/8.1-add-alias.webp" alt="On the &quot;Add alias&quot; pop-up window, fill out the following fields:Alias name: Enter the alias name.Filter Type: Select the &quot;Relations query&quot; option.Root entity block:Type: Select the &quot;Asset&quot; entity.Asset: Select the asset from the drop-down menu (e.g., &quot;Asset A&quot;).Direction: Select the &quot;From&quot; option.Max relation level: Enter the number representing the depth of the entity relations." loading="lazy"><figcaption>On the <b>"Add alias"</b> pop-up window, fill out the following fields:<ul><li><b>Alias name:</b> Enter the alias name.</li><li><b>Filter Type:</b> Select the <b>"Relations query"</b> option.</li><p><b>Root entity</b> block:</p><li><b>Type:</b> Select the <b>"Asset"</b> entity.</li><li><b>Asset:</b> Select the asset from the drop-down menu (e.g., <i>"Asset A"</i>).</li><li><b>Direction:</b> Select the <b>"From"</b> option.</li><li><b>Max relation level:</b> Enter the number representing the depth of the entity relations.</li></ul></figcaption></figure><figure><img src="/images/edge/config/edge-asset-ce/8-add-alias.webp" alt="Scroll down to create the filter in the Relation filters block:Click the &quot;Add filter&quot; button to add conditions to filter data.Relation type: Select the &quot;Manages&quot; option.Entity types: Select the &quot;Device&quot; entity type.In this way, the data from the devices that are managed by the asset will be displayed on the dashboard.Click the &quot;Add&quot; button to add the alias." loading="lazy"><figcaption>Scroll down to create the filter in the <b>Relation filters</b> block:<ul><li>Click the <b>"Add filter"</b> button to add conditions to filter data.</li><li><b>Relation type:</b> Select the <b>"Manages"</b> option.</li><li><b>Entity types:</b> Select the <b>"Device"</b> entity type.</li></ul><p>In this way, the data from the devices that are managed by the asset will be displayed on the dashboard.</p><p>Click the <b>"Add"</b> button to add the alias.</p></figcaption></figure><figure><img src="/images/edge/config/edge-asset-ce/9-save-alias.webp" alt="To save the alias, click the &quot;Save&quot; button." loading="lazy"><figcaption>To save the alias, click the <b>"Save"</b> button.</figcaption></figure></div>


Continue with the configuration of a widget. Within the **"Edit mode"**, click the **"Add widget"** button to add the widget. Select the **Charts > Time series chart** widget. Read more about **how to add and configure a new widget** [here](/docs/user-guide/widgets/#adding-a-widget-to-the-dashboard).


1. Select the <b>"Entity alias"</b> tab. Select the <b>newly created alias</b> from the drop-down menu as the <b>Datasource</b>. Click the <b>"Add"</b> button.

1. The widget will display real-time data from the associated devices.


<div class="st-gallery"><figure><img src="/images/edge/config/edge-asset-ce/10-widget-configuration.webp" alt="Select the &quot;Entity alias&quot; tab. Select the newly created alias from the drop-down menu as the Datasource. Click the &quot;Add&quot; button." loading="lazy"><figcaption>Select the <b>"Entity alias"</b> tab. Select the <b>newly created alias</b> from the drop-down menu as the <b>Datasource</b>. Click the <b>"Add"</b> button.</figcaption></figure><figure><img src="/images/edge/config/edge-asset-ce/11-result.webp" alt="The widget will display real-time data from the associated devices." loading="lazy"><figcaption>The widget will display real-time data from the associated devices.</figcaption></figure></div>


## Provisioning From Cloud

To provision the **Asset entity** from the **SENTIENT Cloud** to the **Edge** instance, log in to the **Cloud** and go to the **Edge management > Instances** section:


1. Click the <b>"Manage assets"</b> button.

1. On the <b>Edge assets</b> page, click the <b>"+"</b> button and select the assets to assign from the drop-down menu in the <b>"Assign Asset(s) To Edge"</b> pop-up window. Click the <b>"Assign"</b> button.

1. To verify that the assigned asset is on the Edge, go to the <b>Entities > Assets</b> section.


<div class="st-gallery"><figure><img src="/images/edge/config/edge-asset-ce/12-instances-on-cloud.webp" alt="Click the &quot;Manage assets&quot; button." loading="lazy"><figcaption>Click the <b>"Manage assets"</b> button.</figcaption></figure><figure><img src="/images/edge/config/edge-asset-ce/13-edge-assets.webp" alt="On the Edge assets page, click the &quot;+&quot; button and select the assets to assign from the drop-down menu in the &quot;Assign Asset(s) To Edge&quot; pop-up window. Click the &quot;Assign&quot; button." loading="lazy"><figcaption>On the <b>Edge assets</b> page, click the <b>"+"</b> button and select the assets to assign from the drop-down menu in the <b>"Assign Asset(s) To Edge"</b> pop-up window. Click the <b>"Assign"</b> button.</figcaption></figure><figure><img src="/images/edge/config/edge-asset-ce/14-confirm.webp" alt="To verify that the assigned asset is on the Edge, go to the Entities > Assets section." loading="lazy"><figcaption>To verify that the assigned asset is on the Edge, go to the <b>Entities > Assets</b> section.</figcaption></figure></div>


### Next Steps
