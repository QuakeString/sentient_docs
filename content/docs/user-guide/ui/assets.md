+++
title = "Assets"
description = "Sentient IoT Asset management"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/assets.md"
+++
**Asset** is an abstract entity in the IoT system of SENTIENT that represents any physical object, space, or organizational unit. 
Examples include a building, room, production area, field, streetlight, substation, or vehicle.

**Key characteristics of an asset:**
- **Does not generate telemetry** on its own but can be associated with devices that do.
- **Can have its own attributes**, such as location, type, or responsible personnel.
- **Used for grouping** devices and other entities.
- **Can be part of a hierarchy**, e.g., Substation &#10230; Line &#10230; Streetlight.
- **Participates in SENTIENT business logic**, such as rule chains, alarms, and dashboards.

Assets help logically and efficiently structure your IoT project, making it easier to manage and scale.

> SENTIENT supports asset management functions via both the web UI and the [REST API](/docs/reference/rest-api/).

<br><b><font size="4">Practical video course 🎥</font></b>

Watch this practical video course to learn how to configure and manage SENTIENT dashboards, resources, and devices, and how to use them in real-world scenarios.


<div id="video">  
    <div id="video_wrapper">
        <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/65SoFceFDBE" frameborder="0" allowfullscreen></iframe>
    </div>
</div>

## How to create, edit, and delete asset

Tenant administrators and users with appropriate [permissions](/docs/user-guide/rbac/) can create, edit, or delete assets in SENTIENT.

### Creating asset

To create a new asset:
- Navigate to **Entities** &#10230; **Assets**. 
- Click the "**+**" icon in the upper-right corner and select "**Add new asset**" from drop-down menu.
- In the asset creation form, fill in the required fields:
  - **Name** – a unique name for the asset.
  - **[Asset profile](/docs/user-guide/asset-profiles/)** – by default, the profile is set to "**default**", but you can choose a different profile if needed.
    
- Optional fields such as **Label** or **Description** can be filled in if needed.
- Click "**Add**".

The asset has been successfully created and is now available in the list.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/assets/creating-asset-1-ce.webp" alt="Navigate to &quot;Entities&quot; &#8702; &quot;Assets&quot;. Click the &quot;+&quot; icon in the upper-right corner and select &quot;Add new asset&quot; from drop-down menu." loading="lazy"><figcaption>Navigate to "<b>Entities</b>" &#8702; "<b>Assets</b>". Click the "<b>+</b>" icon in the upper-right corner and select "<b>Add new asset</b>" from drop-down menu.</figcaption></figure><figure><img src="/images/user-guide/ui/assets/creating-asset-2-ce.webp" alt="In the asset creation form, fill in the required fields: Name – a unique name for the asset; Asset profile – by default, the profile is set to &quot;default&quot;, but you can choose a different profile if needed. Click &quot;Add&quot;." loading="lazy"><figcaption>In the asset creation form, fill in the required fields: <b>Name</b> – a unique name for the asset; <b>Asset profile</b> – by default, the profile is set to "<b>default</b>", but you can choose a different profile if needed. Click "<b>Add</b>".</figcaption></figure><figure><img src="/images/user-guide/ui/assets/creating-asset-3-ce.webp" alt="The asset has been successfully created and is now available in the list." loading="lazy"><figcaption>The asset has been successfully created and is now available in the list.</figcaption></figure></div>


### Editing asset

To edit an existing asset:
- In the **Assets** list, locate and click on the desired asset.
- Click the "**pencil**" (✏️ **Edit**) icon on the right.
- In the edit window, you can modify the following fields:
  - **Name**
  - **Label**
  - **Asset profile**
  - **Description**
- After making the necessary changes, click "**Apply changes**" to save.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/assets/editing-asset-1-ce.webp" alt="In the assets list, locate and click on the desired asset, then click the &quot;pencil&quot; (✏️ Edit) icon on the right to open the edit form." loading="lazy"><figcaption>In the assets list, locate and click on the desired asset, then click the "<b>pencil</b>" (✏️ <b>Edit</b>) icon on the right to open the edit form.</figcaption></figure><figure><img src="/images/user-guide/ui/assets/editing-asset-2-ce.webp" alt="In the edit window, you can modify the following fields: name, label, asset profile and description. After making the necessary changes, click &quot;Apply changes&quot; to save." loading="lazy"><figcaption>In the edit window, you can <b>modify</b> the following fields: name, label, asset profile and description. After making the necessary changes, click "<b>Apply changes</b>" to save.</figcaption></figure></div>


### Deleting asset

To delete an asset:


1. Find the asset in the list and click the "<b>trash bin</b>" icon next to it.

1. Confirm the deletion in the popup dialog.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/assets/deleting-asset-1-ce.webp" alt="Find the asset in the list and click the &quot;trash bin&quot; icon next to it." loading="lazy"><figcaption>Find the asset in the list and click the "<b>trash bin</b>" icon next to it.</figcaption></figure><figure><img src="/images/user-guide/ui/assets/deleting-asset-2-ce.webp" alt="Confirm the deletion in the popup dialog." loading="lazy"><figcaption>Confirm the deletion in the popup dialog.</figcaption></figure></div>


> **Note**: Deleting an asset **does not delete** the devices or other entities linked to it, but it **will break all existing relations** (such as links to devices, alarms, dashboards, etc.).


## Make asset public

You can make an asset public so that all its data is accessible to everyone. 
This is ideal for creating public demo dashboards that require access to asset data or for open data use cases.    

- Click the "**Make asset public**" icon next to the asset you want to share.
- Confirm your action in the popup dialog.

The asset is now public.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/assets/make-asset-public-1-ce.webp" alt="Click the &quot;Make asset public&quot; icon next to the asset you want to share." loading="lazy"><figcaption>Click the "<b>Make asset public</b>" icon next to the asset you want to share.</figcaption></figure><figure><img src="/images/user-guide/ui/assets/make-asset-public-2-ce.webp" alt="Confirm your action in the popup dialog." loading="lazy"><figcaption>Confirm your action in the popup dialog.</figcaption></figure><figure><img src="/images/user-guide/ui/assets/make-asset-public-3-ce.webp" alt="The asset is now public. Its data is accessible without authentication and can be used in public dashboards or shared externally." loading="lazy"><figcaption>The asset is now public. Its data is accessible without authentication and can be used in public dashboards or shared externally.</figcaption></figure></div>


<br>
To revoke public access and make the asset private again:


1. Click the "<b>Make asset private</b>" icon next to the asset.

1. Confirm your action in the popup dialog.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/assets/make-asset-private-1-ce.webp" alt="Click the &quot;Make asset private&quot; icon next to the asset." loading="lazy"><figcaption>Click the "<b>Make asset private</b>" icon next to the asset.</figcaption></figure><figure><img src="/images/user-guide/ui/assets/make-asset-private-2-ce.webp" alt="Confirm your action in the popup dialog." loading="lazy"><figcaption>Confirm your action in the popup dialog.</figcaption></figure></div>


> Once the asset is made private, it will no longer be publicly accessible, and any **public [dashboards](/docs/user-guide/dashboards/)** referencing it will lose access to its data.

## Assigning asset to customer

You can assign an asset to a specific [customer](/docs/user-guide/ui/customers/). This ensures that only users associated with that customer will have access to the asset and its data.

> This step is crucial for ensuring data access control. Each customer user will only see their own assets and will not have access to assets or data assigned to other customers.

To assign an asset to a customer:
- Locate the desired asset in the list.
- Click the "**Assign to customer**" icon.
- Select the target customer from the dropdown list.
- Click "**Assign**" to confirm the action.

The selected customer now has access to the asset and its data.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/assets/assign-asset-to-customer-1-ce.webp" alt="Locate the desired asset in the list, and click the &quot;Assign to customer&quot; icon." loading="lazy"><figcaption>Locate the desired asset in the list, and click the "<b>Assign to customer</b>" icon.</figcaption></figure><figure><img src="/images/user-guide/ui/assets/assign-asset-to-customer-2-ce.webp" alt="Select the target customer from the dropdown list. Click &quot;Assign&quot; to confirm the action." loading="lazy"><figcaption><b>Select the target customer</b> from the dropdown list. Click "<b>Assign</b>" to confirm the action.</figcaption></figure><figure><img src="/images/user-guide/ui/assets/assign-asset-to-customer-3-ce.webp" alt="The selected customer now has access to the asset and its data." loading="lazy"><figcaption>The selected customer now has access to the asset and its data.</figcaption></figure></div>


<br>
You can later unassign the asset or reassign it to another customer if needed.


1. Click the "<b>Unassign from customer</b>" icon.

1. Confirm your action in the popup dialog.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/assets/unassign-asset-from-customer-1-ce.webp" alt="Click the &quot;Unassign from customer&quot; icon." loading="lazy"><figcaption>Click the "<b>Unassign from customer</b>" icon.</figcaption></figure><figure><img src="/images/user-guide/ui/assets/unassign-asset-from-customer-2-ce.webp" alt="Confirm your action in the popup dialog." loading="lazy"><figcaption>Confirm your action in the popup dialog.</figcaption></figure></div>


## Asset details

Clicking on an asset opens a window where you can access and manage various aspects of that asset.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/assets/asset-details-page-1-ce.webp" alt="Clicking on an asset opens a window where you can access and manage various aspects of that asset." loading="lazy"><figcaption>Clicking on an asset opens a window where you can access and manage various aspects of that asset.</figcaption></figure></div>


<b><font size="3">Copy asset ID</font></b>   
Allows you to quickly retrieve the asset’s unique UUID. Click Copy asset Id to copy it to your clipboard. The ID is used in API calls, integrations, and scripts.

<b><font size="3">Attributes</font></b>

This tab displays client, server, and shared [attributes](/docs/user-guide/attributes/) — static or semi-static key-value pairs related to the asset. Examples include location, category, configuration parameters, and other metadata.

<b><font size="3">Latest telemetry</font></b>

Shows the [latest telemetry](/docs/user-guide/telemetry/) values associated with the asset. Telemetry may come from linked devices or be added manually for modeling purposes.
- **Adding telemetry:** Click the "**+**" icon, enter the key name, value type, and value.
- **Deleting telemetry:** Click the trash icon, choose the deletion mode (all data, latest value, all except latest, or by time period), and confirm.

<b><font size="3">Calculated fields</font></b>   
Displays fields whose values are computed from existing attributes or telemetry using formulas. This allows you to define derived parameters without modifying the device firmware. Learn more about Calculated fields [here](/docs/user-guide/calculated-fields/).

<b><font size="3">Alarm rules</font></b>   
Contains the alarm rules configured for the asset. You can review thresholds, triggering logic, and configured alarm actions that apply to this asset. Learn more about configuring alarm rules [here](/docs/user-guide/alarm-rules/).

<b><font size="3">Alarms</font></b>    
Shows all active and historical [alarms](/docs/user-guide/alarms/) related to the asset. Allows tracking of warnings, operational issues, and critical events affecting the asset.

<b><font size="3">Events</font></b>   
Displays system events associated with the asset, such as logs, warnings, errors, and other lifecycle-related activity. Useful for diagnostics and operational analysis.

<b><font size="3">Relations</font></b>   
Shows all directed [relations](/docs/user-guide/entities-and-relations/#relations) between this asset and other entities, such as devices, dashboards, assets, and rule chains. Helps understand how the asset interacts within the system structure.

<b><font size="3">Audit logs</font></b>   
Provides a [record of user actions](/docs/user-guide/audit-log/) related to the asset — creation, updates, configuration changes, and deletions. Used for auditing and change tracking.

<b><font size="3">Version control</font></b>   
Enables exporting and restoring asset-related entities using the Git-backed [version control](/docs/user-guide/version-control/) service. Supports backup, collaboration, and configuration versioning.

<hr>


## Managing asset relations. How to add, view, edit, delete

From the Assets page, you can create, view, edit, and delete relations between an asset and other entities (assets, devices, customers, etc.). See details about [Entities and relations](/docs/user-guide/entities-and-relations/).

**To manage relations between an asset and other entities for a specific asset:** 
- Open the [asset details](#asset-details) ➜ go to the **Relations** tab.

**Add a new relation:**
- In the Direction selector, choose **From** (outbound) or **To** (inbound).
- Click "**+**" icon (Add).
- In **Add relation** window, set **Relation type** (e.g., _Contains_, _Manages_) and choose the **To entity** (Entity type and target entities).
- Click **Add** to confirm.


<div class="st-callout info">


**Note:** Relations are directional. Use "**From**" to define relations originating from the current asset, or "**To**" to show relations to this asset.


</div>


**View & filter relations:**
- Switch **Direction** between "**From**" and "**To**" to see outbound/inbound relations.
- Use the **search** icon to filter by relation type or entity.

**Edit a relation:**
- In the list, click the "**pencil**" icon to change the relation type or target entity, then **Save**.

**Delete a relation:**
- Click the "**trash can**" icon next to a relation and confirm deleting.


<div class="st-callout info">


**Note:** Deleting a relation does **not** delete the related entities; it only deletes the relation.


</div>


<hr>

## Next steps


<hr>

## Your feedback

Don&#39;t hesitate to star SENTIENT on [github](https://github.com/sentient/sentient) to help us spread the word.
If you have any questions about this sample, please [contact us](/docs/contact-us/).
