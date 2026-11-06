+++
title = "Edge Alarms"
description = "Edge Alarms Overview"

[extra]
status = "imported"
checked = ""
source = "docs/edge/user-guide/alarms.md"
+++
## Overview

The **SENTIENT Alarm** is an essential feature for monitoring and responding to entity events and conditions. 
For a comprehensive understanding of the **SENTIENT Alarm** feature, please refer to the [Working with Alarms](/docs/user-guide/alarms/) documentation.

Although the **Alarm** feature for the **Edge** is designed similarly to that of the **Cloud**, it includes several notable additions: 
* Alarms are processed locally on the **Edge** and focused on the immediate conditions for alarm triggering without relying on connectivity.
* The Alarm data can be pushed from the **Edge** to the **Cloud** and can also be sent back from the **Cloud** to the **Edge**. This setup enables real-time monitoring and management of alarms across different locations.
* Edge Alarms can be integrated with other local systems or software solutions for further processing, notifications, or actions.

In essence, the **SENTIENT Edge Alarms** provide real-time, localized alarm management that can operate independently of **Cloud** connectivity.

## Create an Alarm on the Edge Instance

The **Edge Alarms** are created and configured in the same way as the **Cloud Alarms**. Therefore, it is necessary to define the **parameters and the rules** according to which the alarm is to be triggered. 

The easiest way to create an Alarm is to use the [Alarm Rules within the Device profile](/docs/user-guide/device-profiles/#alarm-rules). The majority of tasks can be configured with **Alarm Rules** with minimal effort.

If more complex logic is required, we suggest using the alternative option, namely the ["Create Alarm"](/docs/user-guide/rule-engine-2-0/nodes/action/create-alarm/) and ["Clear Alarm"](/docs/user-guide/rule-engine-2-0/nodes/action/clear-alarm/) rule nodes in the [Rule Engine](/docs/user-guide/rule-engine-2-0/re-getting-started/). This is a more advanced option that requires a certain level of programming expertise. Please refer to the [corresponding example](/docs/user-guide/rule-engine-2-0/tutorials/create-clear-alarms/).

## Alarms Pushing from the Cloud to the Edge

The **SENTIENT system** allows for pushing **Alarms** from the **Cloud** to the **Edge** to enhance operational efficiency and reduce reliance on **Cloud** resources.


<div class="st-callout info">


Determine the **Rule Chain** you intend to use in advance, as this will have a significant impact on the configuration process.


</div>


### Guidelines

To push Alarms from the **Cloud** to the **Edge**, follow these steps:


1. Log in to the <b>SENTIENT Cloud</b> and go to the <b>Profiles > Device profiles</b> section to create or modify the Device profile. Select the appropriate <b>Default rule chain</b>. Then, configure the <b>Alarm Rule</b>.

1. Go to the <b>Entities > Devices</b> section. You can create a new <b>Device</b> or edit the existing one. On the <b>"Device details"</b> page, assign newly created (or updated) <b>Device profile</b> to this <b>Device</b>. Click the <b>“Apply changes”</b> button.

1. Go the <b>Edge management > Instances</b> section, select the <b>“Manage devices”</b> option and assign this device to the <b>Edge</b> instance.

1. Go to the <b>Rule Chains</b> section, to modify the <b>Rule Chain</b> you have assigned to the <b>Device profile</b>.

1. On the <b>Rule Chain</b> edit page, in the Node search bar find the <b>"push to edge"</b> node. It pushes messages from Cloud to Edge. Once message arrives to this node it will be converted into Edge event and saved to the local database. Drag and drop the node onto the <b>Rule Chain sheet</b>. Then, in the <b>"Add rule node"</b> pop-up window enter the node title and select the <b>"Server attributes"</b> option in the <b>"Entity attributes scope"</b> field. Click the <b>"Add"</b> button to proceed.

1. Connect the <b>“device profile”</b> node to the <b>"push to edge"</b> node and set the <b>“Alarm Created”</b>, <b>“Alarm Updated”</b>, <b>“Alarm Severity Updated”</b>, and <b>“Alarm Cleared”</b> link labels. Click the <b>“Apply changes”</b> button in the <b>Rule Chain sheet</b>.

1. To test if the rule and node are working, navigate to the <b>Entities > Devices</b> section, find your <b>Device</b> and open the <b>"Device details"</b> page. Click the <b>"Check connectivity"</b> button. Trigger the <b>Alarm Rule</b> by executing the corresponding command in the terminal.

1. To verify the received Alarm notification, go to the <b>Entities > Devices</b> section, open the <b>"Device details"</b> page and select the <b>“Alarm”</b> tab. You also can view the incoming Alarm notification in the Notification center.

1. To verify that the notification is propagated to the <b>Edge</b>, log in to the <b>Edge</b> instance and go to the <b>Entities > Devices</b> section, open the <b>"Device details"</b> page and select the <b>“Alarm”</b> tab.

1. Make sure to <b>Acknowledge</b> and <b>Clear</b> the notification after you received it. You can do it on either the <b>Cloud</b> or the <b>Edge</b>. If the <b>Uncleared Alarm</b> exists, it will be updated, instead of being created.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/manage-alarms/push-from-cloud-to-edge/0-device-profile-create-rule.webp" alt="Log in to the SENTIENT Cloud and go to the Profiles > Device profiles section to create or modify the Device profile. Select the appropriate Default rule chain. Then, configure the Alarm Rule." loading="lazy"><figcaption>Log in to the <b>SENTIENT Cloud</b> and go to the <b>Profiles > Device profiles</b> section to create or modify the Device profile. Select the appropriate <b>Default rule chain</b>. Then, configure the <b>Alarm Rule</b>.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-cloud-to-edge/1-assign-the-profile.webp" alt="Go to the Entities > Devices section. You can create a new Device or edit the existing one. On the &quot;Device details&quot; page, assign newly created (or updated) Device profile to this Device. Click the “Apply changes” button." loading="lazy"><figcaption>Go to the <b>Entities > Devices</b> section. You can create a new <b>Device</b> or edit the existing one. On the <b>"Device details"</b> page, assign newly created (or updated) <b>Device profile</b> to this <b>Device</b>. Click the <b>“Apply changes”</b> button.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-cloud-to-edge/2-assign-device-toEdge.webp" alt="Go the Edge management > Instances section, select the “Manage devices” option and assign this device to the Edge instance." loading="lazy"><figcaption>Go the <b>Edge management > Instances</b> section, select the <b>“Manage devices”</b> option and assign this device to the <b>Edge</b> instance.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-cloud-to-edge/3-rule-chain-section.webp" alt="Go to the Rule Chains section, to modify the Rule Chain you have assigned to the Device profile." loading="lazy"><figcaption>Go to the <b>Rule Chains</b> section, to modify the <b>Rule Chain</b> you have assigned to the <b>Device profile</b>.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-cloud-to-edge/4-push-node.webp" alt="On the Rule Chain edit page, in the Node search bar find the &quot;push to edge&quot; node. It pushes messages from Cloud to Edge. Once message arrives to this node it will be converted into Edge event and saved to the local database. Drag and drop the node onto the Rule Chain sheet. Then, in the &quot;Add rule node&quot; pop-up window enter the node title and select the &quot;Server attributes&quot; option in the &quot;Entity attributes scope&quot; field. Click the &quot;Add&quot; button to proceed." loading="lazy"><figcaption>On the <b>Rule Chain</b> edit page, in the Node search bar find the <b>"push to edge"</b> node. It pushes messages from Cloud to Edge. Once message arrives to this node it will be converted into Edge event and saved to the local database. Drag and drop the node onto the <b>Rule Chain sheet</b>. Then, in the <b>"Add rule node"</b> pop-up window enter the node title and select the <b>"Server attributes"</b> option in the <b>"Entity attributes scope"</b> field. Click the <b>"Add"</b> button to proceed.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-cloud-to-edge/5-select-link-labels.webp" alt="Connect the “device profile” node to the &quot;push to edge&quot; node and set the “Alarm Created”, “Alarm Updated”, “Alarm Severity Updated”, and “Alarm Cleared” link labels. Click the “Apply changes” button in the Rule Chain sheet." loading="lazy"><figcaption>Connect the <b>“device profile”</b> node to the <b>"push to edge"</b> node and set the <b>“Alarm Created”</b>, <b>“Alarm Updated”</b>, <b>“Alarm Severity Updated”</b>, and <b>“Alarm Cleared”</b> link labels. Click the <b>“Apply changes”</b> button in the <b>Rule Chain sheet</b>.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-cloud-to-edge/6-telemetry.webp" alt="To test if the rule and node are working, navigate to the Entities > Devices section, find your Device and open the &quot;Device details&quot; page. Click the &quot;Check connectivity&quot; button. Trigger the Alarm Rule by executing the corresponding command in the terminal." loading="lazy"><figcaption>To test if the rule and node are working, navigate to the <b>Entities > Devices</b> section, find your <b>Device</b> and open the <b>"Device details"</b> page. Click the <b>"Check connectivity"</b> button. Trigger the <b>Alarm Rule</b> by executing the corresponding command in the terminal.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-cloud-to-edge/7-verify-alarm-on-cloud.webp" alt="To verify the received Alarm notification, go to the Entities > Devices section, open the &quot;Device details&quot; page and select the “Alarm” tab. You also can view the incoming Alarm notification in the Notification center." loading="lazy"><figcaption>To verify the received Alarm notification, go to the <b>Entities > Devices</b> section, open the <b>"Device details"</b> page and select the <b>“Alarm”</b> tab. You also can view the incoming Alarm notification in the Notification center.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-cloud-to-edge/8-verify-alarm-on-edge.webp" alt="To verify that the notification is propagated to the Edge, log in to the Edge instance and go to the Entities > Devices section, open the &quot;Device details&quot; page and select the “Alarm” tab." loading="lazy"><figcaption>To verify that the notification is propagated to the <b>Edge</b>, log in to the <b>Edge</b> instance and go to the <b>Entities > Devices</b> section, open the <b>"Device details"</b> page and select the <b>“Alarm”</b> tab.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-cloud-to-edge/9-acknowledge-clear.webp" alt="Make sure to Acknowledge and Clear the notification after you received it. You can do it on either the Cloud or the Edge. If the Uncleared Alarm exists, it will be updated, instead of being created." loading="lazy"><figcaption>Make sure to <b>Acknowledge</b> and <b>Clear</b> the notification after you received it. You can do it on either the <b>Cloud</b> or the <b>Edge</b>. If the <b>Uncleared Alarm</b> exists, it will be updated, instead of being created.</figcaption></figure></div>


## Alarms Pushing from the Edge to the Cloud

**SENTIENT** also allows for pushing alarms from the **Edge** to the **Cloud**.


<div class="st-callout info">


**Please note!** <br>
If you use **earlier versions** of Edge, you **cannot** create or edit a **Rule Chain** on the **Edge** itself. It must be configured as a template in the **Cloud (Server)**, and then assigned to the **Edge** instance. 

Starting with **Edge version 4.0**, you can create and edit a **Rule Chain** on the **Edge**.


</div>


### Guidelines

To push Alarms from the **Edge** to the **Cloud**, follow these steps:


1. Log in to the <b>SENTIENT Edge</b> and go to the <b>Profiles > Device profiles</b> section to create or edit the <b>Device profile</b>. Select the appropriate <b>Default rule chain</b>. Set the <b>Alarm Rule</b>.

1. Go to the <b>Entities > Devices</b> section. You can create a new device or edit the existing one. On the <b>"Device details"</b> page, assign newly created (or updated) <b>Device profile</b> to this device. Click the <b>“Apply changes”</b> button.

1. Log in to the <b>SENTIENT Cloud</b> and go to the <b>Edge management > Rule chain templates</b> section to modify the <b>Rule Chain</b> you have assigned to the <b>Device profile</b>. <i>Note: If you use <b>Edge version 4.0</b>, you can proceed with <b>Rule Chain</b> configurations on the <b>Edge</b> instance.</i>

1. On the <b>Rule Chain</b> edit page, in the Node search bar find the <b>"push to cloud"</b> node. It pushes messages from <b>Edge</b> to <b>Cloud</b>. Once message arrives to this node it will be converted into Cloud event and saved to the local database. Drag and drop the node onto the <b>Rule Chain sheet</b>. Then, in the <b>"Add rule node"</b> pop-up window enter the node title and select the <b>"Server attributes"</b> option in the <b>"Entity attributes scope"</b> field. Click the <b>"Add"</b> button to proceed.

1. Connect the <b>“device profile”</b> node to the <b>"push to edge"</b> node and set the <b>“Alarm Created”</b>, <b>“Alarm Updated”</b>, <b>“Alarm Severity Updated”</b>, and <b>“Alarm Cleared”</b> link labels. Click the <b>“Apply changes”</b> button in the <b>Rule Chain sheet</b>.

1. To test if the rule and node are working, log in to your <b>Edge</b> instance and navigate to the <b>Entities > Devices</b> section. Find your device and open the <b>"Device details"</b> page. Click the <b>"Check connectivity"</b> button. Trigger the <b>Alarm Rule</b> by executing the corresponding command in the terminal.

1. To verify the received alarm notification, go to the <b>Entities > Devices</b> section, open the <b>"Device details"</b> page and select the <b>“Alarm”</b> tab. You also can view the incoming alarm notification in the <b>Notification center</b>.

1. To verify that the notification is propagated to the <b>Cloud</b>, log in to the <b>SENTIENT Cloud (Server)</b> and go to the <b>Entities > Devices</b> section, open the <b>"device details"</b> page and select the <b>“Alarm”</b> tab.

1. Make sure to <b>Acknowledge</b> and <b>Clear</b> the notification after you received it. You can do it on either the <b>Cloud</b> or the <b>Edge</b>. If the <b>Uncleared Alarm</b> exists, it will be updated, instead of being created.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/manage-alarms/push-from-edge-to-cloud/0-device-profile.webp" alt="Log in to the SENTIENT Edge and go to the Profiles > Device profiles section to create or edit the Device profile. Select the appropriate Default rule chain. Set the Alarm Rule." loading="lazy"><figcaption>Log in to the <b>SENTIENT Edge</b> and go to the <b>Profiles > Device profiles</b> section to create or edit the <b>Device profile</b>. Select the appropriate <b>Default rule chain</b>. Set the <b>Alarm Rule</b>.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-edge-to-cloud/1-assign-profile.webp" alt="Go to the Entities > Devices section. You can create a new device or edit the existing one. On the &quot;Device details&quot; page, assign newly created (or updated) Device profile to this device. Click the “Apply changes” button." loading="lazy"><figcaption>Go to the <b>Entities > Devices</b> section. You can create a new device or edit the existing one. On the <b>"Device details"</b> page, assign newly created (or updated) <b>Device profile</b> to this device. Click the <b>“Apply changes”</b> button.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-edge-to-cloud/2-rule-chain-template.webp" alt="Log in to the SENTIENT Cloud and go to the Edge management > Rule chain templates section to modify the Rule Chain you have assigned to the Device profile. Note: If you use Edge version 4.0, you can proceed with Rule Chain configurations on the Edge instance." loading="lazy"><figcaption>Log in to the <b>SENTIENT Cloud</b> and go to the <b>Edge management > Rule chain templates</b> section to modify the <b>Rule Chain</b> you have assigned to the <b>Device profile</b>. <i>Note: If you use <b>Edge version 4.0</b>, you can proceed with <b>Rule Chain</b> configurations on the <b>Edge</b> instance.</i></figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-edge-to-cloud/3-push-to-cloud-settings.webp" alt="On the Rule Chain edit page, in the Node search bar find the &quot;push to cloud&quot; node. It pushes messages from Edge to Cloud. Once message arrives to this node it will be converted into Cloud event and saved to the local database. Drag and drop the node onto the Rule Chain sheet. Then, in the &quot;Add rule node&quot; pop-up window enter the node title and select the &quot;Server attributes&quot; option in the &quot;Entity attributes scope&quot; field. Click the &quot;Add&quot; button to proceed." loading="lazy"><figcaption>On the <b>Rule Chain</b> edit page, in the Node search bar find the <b>"push to cloud"</b> node. It pushes messages from <b>Edge</b> to <b>Cloud</b>. Once message arrives to this node it will be converted into Cloud event and saved to the local database. Drag and drop the node onto the <b>Rule Chain sheet</b>. Then, in the <b>"Add rule node"</b> pop-up window enter the node title and select the <b>"Server attributes"</b> option in the <b>"Entity attributes scope"</b> field. Click the <b>"Add"</b> button to proceed.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-edge-to-cloud/4-push-to-cloud-node.webp" alt="Connect the “device profile” node to the &quot;push to edge&quot; node and set the “Alarm Created”, “Alarm Updated”, “Alarm Severity Updated”, and “Alarm Cleared” link labels. Click the “Apply changes” button in the Rule Chain sheet." loading="lazy"><figcaption>Connect the <b>“device profile”</b> node to the <b>"push to edge"</b> node and set the <b>“Alarm Created”</b>, <b>“Alarm Updated”</b>, <b>“Alarm Severity Updated”</b>, and <b>“Alarm Cleared”</b> link labels. Click the <b>“Apply changes”</b> button in the <b>Rule Chain sheet</b>.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-edge-to-cloud/5-send-telemetry-command.webp" alt="To test if the rule and node are working, log in to your Edge instance and navigate to the Entities > Devices section. Find your device and open the &quot;Device details&quot; page. Click the &quot;Check connectivity&quot; button. Trigger the Alarm Rule by executing the corresponding command in the terminal." loading="lazy"><figcaption>To test if the rule and node are working, log in to your <b>Edge</b> instance and navigate to the <b>Entities > Devices</b> section. Find your device and open the <b>"Device details"</b> page. Click the <b>"Check connectivity"</b> button. Trigger the <b>Alarm Rule</b> by executing the corresponding command in the terminal.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-edge-to-cloud/6-check-alarm-on-edge.webp" alt="To verify the received alarm notification, go to the Entities > Devices section, open the &quot;Device details&quot; page and select the “Alarm” tab. You also can view the incoming alarm notification in the Notification center." loading="lazy"><figcaption>To verify the received alarm notification, go to the <b>Entities > Devices</b> section, open the <b>"Device details"</b> page and select the <b>“Alarm”</b> tab. You also can view the incoming alarm notification in the <b>Notification center</b>.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-edge-to-cloud/7-check-alarm-on-cloud.webp" alt="To verify that the notification is propagated to the Cloud, log in to the SENTIENT Cloud (Server) and go to the Entities > Devices section, open the &quot;device details&quot; page and select the “Alarm” tab." loading="lazy"><figcaption>To verify that the notification is propagated to the <b>Cloud</b>, log in to the <b>SENTIENT Cloud (Server)</b> and go to the <b>Entities > Devices</b> section, open the <b>"device details"</b> page and select the <b>“Alarm”</b> tab.</figcaption></figure><figure><img src="/images/edge/user-guide/manage-alarms/push-from-edge-to-cloud/8-acknowledge-clear.webp" alt="Make sure to Acknowledge and Clear the notification after you received it. You can do it on either the Cloud or the Edge. If the Uncleared Alarm exists, it will be updated, instead of being created." loading="lazy"><figcaption>Make sure to <b>Acknowledge</b> and <b>Clear</b> the notification after you received it. You can do it on either the <b>Cloud</b> or the <b>Edge</b>. If the <b>Uncleared Alarm</b> exists, it will be updated, instead of being created.</figcaption></figure></div>

 

## Next steps
