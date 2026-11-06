+++
title = "Edge Attributes"
description = "Edge Attributes overview"

[extra]
status = "imported"
checked = ""
source = "docs/edge/user-guide/edge-attributes.md"
+++
## Overview

**Custom attributes** are the structured data that can be assigned to the entities. They are stored in the database and can be used for visualization, analysis, logic configuration, and integration with other services.

In **SENTIENT Edge**, attributes work similarly to the **SENTIENT** platform. For a comprehensive understanding of the **SENTIENT Attributes**, please refer to the [Working with IoT Attributes](/docs/user-guide/attributes/) documentation.

## Assigning Attributes to the Edge Entities

**Custom attributes** can be managed from the **Edge** instance. They are stored and processed locally for immediate use. 

To add an attribute to any Edge [entity](/docs/user-guide/entities-and-relations/): 
* Go to the **Entity section** (e.g. **Entities > Devices** section) and click on the entity. On the **Entity details** page, select the **"Attributes"** tab and select the **"Server attributes"** option in the **"Entity attributes scope"** drop-down menu. 
* Click the **"Add"** button. In the **"Add attribute"** window, enter the attribute name in the **"Key"** field. Then, select the **attribute value** (_String, Integer, Double, Boolean, JSON_) type and input an **attribute value** in the corresponding fields. Click the **"Add"** button.
* Once the attribute is added, you can see it in the list


<div class="st-gallery"><figure><img src="/images/edge/user-guide/attributes/1-devices.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/2-add-attribute.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/3-confirm-attribute.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


If an attribute is assigned to an entity on the **SENTIENT Server**, and the entity is then assigned to an **Edge** instance, the **attribute** is automatically assigned as well. 
Read about **how to assign entities to the Edge** instance [here](/docs/edge/config/management/#entities-management).

## Using Attributes to Visualize Data on the Dashboard

In visualization data process, **entity attributes** can be used to provide context for telemetry data, display static or dynamic metadata about devices, and act as configuration parameters to filter or annotate dashboards. 

To display **attributes** on the Dashboard, create the [Entity alias](/docs/user-guide/ui/aliases/) and bind it to the widget. Widgets like [Cards](/docs/user-guide/ui/widget-library/#cards), [Input widgets](/docs/user-guide/ui/widget-library/#input-widgets), or [Entity Tables](/docs/user-guide/ui/entity-table-widget/) are ideal for displaying attributes.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/attributes/4-attributes-dasboard.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Read more about **Edge Dashboards configuration** [here](/docs/edge/user-guide/db-overview/).

## Syncing Attribute Updates

To ensure that any changes to the **attributes** are synchronized between the **Server** and **Edge** instances, adjust the **Rule Chains**. 

If the changes occurred on the **SENTIENT Server** and must be propagated to the **Edge** instance:
* Log in to the **SENTIENT Server**, go to the **Rule chains** section and click on the **Rule Chain**.
* On the **Rule Chain** edit page, find the **"push to edge"** node using the **Node search** bar. Drag and drop the node onto the **Rule Chain** sheet. Then, in the **"Add rule node"** pop-up window enter the node title and select the **"Server attributes"** option in the **"Entity attributes scope"** field. Click the **"Add"** button to proceed.
* Connect the **“message type switch”** node and the **"push to edge"** node with the **"Attributes Deleted"** and **"Attributes Updated"** link labels. Click the **“Apply changes”** button on the **Rule Chain** sheet.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/attributes/5-rule-chains-section.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/6-push-to-edge.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/7-connect-and-save.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


To keep the **SENTIENT Server** up to date with any attribute changes that have occurred on the **Edge**:
* Log in to the **SENTIENT Server**, go to the **Edge management > Rule chains templates** section and click on the **Rule Chain**.
* On the **Rule Chain** edit page, find the **"push to cloud"** node using the **Node search** bar. Drag and drop the node onto the **Rule Chain** sheet. Then, in the **"Add rule node"** pop-up window enter the node title and select the **"Server attributes"** option in the **"Entity attributes scope"** field. Click the **"Add"** button to proceed.
* Connect the **“message type switch”** node and the **"push to cloud"** node with the **"Attributes Deleted"** and **"Attributes Updated"** link labels. Click the **“Apply changes”** button on the **Rule Chain** sheet.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/attributes/8-14-19-rule-chain-templates-section.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/9-push-to-cloud.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/10-connect-and-save.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<div class="st-callout info">


Starting with **Edge 4.0**, you can create and edit a **Rule Chain** on the **Edge**. 


</div>


Read about how to **subscribe to device attributes change** [here](/docs/edge/config/subscribe-to-attribute/#step-3-subscribe-to-device-attributes-change-and-publish-device-attributes-message).

## Custom Attributes for Edge Instance

Starting with the 3.9.0 release, **custom attributes** can be assigned to the **Edge** instance and used as placeholders in the **Rule Chains**. This allows each **Edge** instance to dynamically replace placeholders with its specific attributes in real time. In this way, one **Edge Rule Chain** template can be used for multiple instances, eliminating the need to create a separate **Rule Chain template** for each **Edge** instance.
The retrieved **Edge attributes** can be used for metadata enrichment, authentication and tagging, analysis, and contextualization of transmitted data. This approach streamlines the management of multiple **Edge** instances and supports efficient scaling while minimizing errors and simplifying maintenance. 

To assign a custom attribute to the **Edge** instance, follow these steps:

* Log in to the **SENTIENT Server**, go to the **Edge management > Instances** section and click on the **Edge** instance. On the **"Edge details"** page, select the **"Attributes"** tab. 
* Click the **“Add”** button and add a new custom attribute (_e.g. edgeAccessToken_).
* Confirm the assigned attribute.
* Select the **"Relations"** tab and click the **“Add”** button to add a new relation (_e.g. the relation between the Edge and the Device(s)_). Click the **“Add”** button.
* The newly created relations will appear in the **"Relations"** tab.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/attributes/11-edge-section.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/12-edge-token.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/12-confirm-1.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/13-edge-manages-devices.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/13-confirm-1.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


To use **Edge** attributes as placeholders in the **Rule Chain template**:
* Go to the **SENTIENT Server**, the **Edge management > Rule chains templates** section and click the appropriate **Rule Chain**.
  * If you're using **Edge 4.0** or later, stay in your **Edge** instance and go to the **Rule chains** section. To edit a rule chain, click the appropriate **Rule Chain**.
* On the **Rule Chain** edit page, find the **"related entity data"** node using the **Node search** bar. Drag and drop the node onto the **Rule Chain sheet**. Fill in the following fields in the pop-up window:
  * **Name:** Enter the node name.
  * **Direction:** Select the relation direction (_From originator/To originator_).
  * **Relation type:** Select the relation type (_Contains/Manages_).
  * **Entity types:** Add the entity type.
* Scroll down and continue with the configuration. In the **"Data to fetch"** configuration block, select the **"Attributes"** tab and enter the **"Attributes mapping"** parameters:
  * **Source attribute key:** Enter the entity attribute key you want to track.
  * **Target key:** Enter the target key name. Click the **"Add"** button.
* Then, find the **"rest api call"** node using the **Node search** bar. Drag and drop the node onto the **Rule Chain sheet**. In the pop-up window, enter the **node name** and click the **"Add"** button.
  * **Name:** Enter the node name.
  * **Headers:** Enter the request header and value. The header or value can be a static string, or pattern that is resolved using Message Metadata properties.
  * Click the **"Add"** button. Read more about the **REST API Call node configuration** [here](/docs/user-guide/rule-engine-2-0/nodes/external/rest-api-call/).
* Connect the **"message type switch"** and **"related entity data"** nodes with the **“Post telemetry”** link label. Then, connect the **"related entity data"** and **"rest api call"** nodes with the **"Success"** link label. Click the **“Apply changes”** button on the **Rule Chain sheet**.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/attributes/8-14-19-rule-chain-templates-section.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/15-related-entity-data.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/15-related-entity-data-1.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/16-rest-api-call.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/17-save-rule-chain.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Using Attributes in Edge Rule Chains

In **SENTIENT Edge**, **Rule Chains** can leverage **edge attributes** to create dynamic, real-time data processing logic. 

Let's consider a situation in which it is necessary to be notified whenever any device attribute undergoes a change. 

Before configuring the alarm notifications, have these steps completed: 
* [Add a Device](/docs/edge/config/create-device/#creating-device-on-edge-instance).
* Add a new custom device attribute.
* [Create an Asset](/docs/edge/config/provision-asset/#creating-relations).
* [Set a relation](/docs/edge/config/provision-asset/#creating-relations) between the **Asset** and **Device**.

Follow these steps to configure the alarm notifications:
* Log in to the **SENTIENT Server**, go to the **Edge management > Rule chains templates** section and click the appropriate **Rule Chain**.
  * If you're using **Edge 4.0** or later, stay in your **Edge** instance and go to the **Rule chains** section. To edit a rule chain, click the appropriate **Rule Chain**.
* On the **Rule Chain** edit page, find the **"related entity data"** node using the **Node search** bar. Drag and drop the node onto the **Rule Chain sheet**. Fill in the following fields in the pop-up window:
  * **Name:** Enter the node name.
  * **Direction:** Select the relation direction (_From originator/To originator_).
  * **Relation type:** Select the relation type (_Contains/Manages_).
  * **Entity types:** Add the entity type.
* Scroll down and continue with the configuration. In the **"Data to fetch"** configuration block, select the **"Attributes"** tab and enter the **"Attributes mapping"** parameters:
  * **Source attribute key:** Enter the entity attribute key you want to track.
  * **Target key:** Enter the target key name. Click the **"Add"** button.
* Then, find the **"create alarm"** node using the **Node search** bar. Drag and drop the node onto the **Rule Chain sheet**. In the pop-up window, enter the **node name** and click the **"Add"** button.
* Connect the **"message type switch"** and **"related entity data”** nodes with the **“Attributes Updated”** and **“Attributes Deleted”** link labels. Then, connect the **“related entity data”** and **"create alarm"** nodes with the **"Success"** link label. Click the **“Apply changes”** button on the **Rule Chain sheet**.
* To verify if the **Alarm** notification will be sent, go to the **Entities > Devices** section, and open the **"Attributes"** tab on the **"Device details"** page. Change the attribute you added to the **"related entity data"** node.
* Confirm the received **Alarm** notification.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/attributes/8-14-19-rule-chain-templates-section.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/20-related-entity-data-node-1.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/21-related-entity-data-node-2.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/22-create-alarm-node.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/23-save.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/24-change-attribute.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/edge/user-guide/attributes/25-alarm-notification.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<div class="st-callout info">


Be sure to **Acknowledge** and **Clear** the notification when you receive it. You can do this either in the Cloud or on the Edge. If the unacknowledged alarm exists, it will be updated rather than created.


</div>


## Next Steps
