+++
title = "Rule Chain templates"
description = "Rule Chain templates"

[extra]
status = "imported"
checked = ""
source = "docs/edge/rule-engine/rule-chain-templates.md"
+++
### What Is an Edge Rule Chain Template?

An **Edge Rule Chain template** is a predefined [Rule Chain](/docs/user-guide/rule-engine-2-0/overview/#rule-chain) in **SENTIENT**, designed specifically for use with **SENTIENT Edge**. 
The **Rule Chain template** does not run on the **Server**. 
Instead, it serves merely as a template. 

For the **older versions of SENTIENT Edge**, the **Rule chain** has to be assigned to an **Edge** instance before use. Only then will it work and process data from devices according to its configuration.

Starting with **Edge version 4.0**, the **Rule chain** can be created and edited right on the **Edge** instance.

### Creating Rule Chain Template on the Edge




1. Sign in to your <b>SENTIENT Edge CE</b> instance and go to the <b>Rule chains</b> section. To add a new <b>Rule chain</b>, click the <b>"+"</b> button in the top right corner, and choose the <b>"Create new rule chain"</b> option.

1. In the pop-up window, enter a <b>name</b> for the new rule chain and click the <b>"Add"</b> button to continue configuring the rule chain.

1. The rule chain is now listed, usually at the top. Click it to begin editing.

1. Configure your <a href="/docs/user-guide/rule-engine-2-0/overview/#rule-node" target="_blank">rule nodes</a> and flow. Once the configuration is complete, click the <b>"Apply changes"</b> button.


<div class="st-gallery"><figure><img src="/images/edge/rule-engine/1-edge-rule-chain.webp" alt="Sign in to your SENTIENT Edge CE instance and go to the Rule chains section. To add a new Rule chain, click the &quot;+&quot; button in the top right corner, and choose the &quot;Create new rule chain&quot; option." loading="lazy"><figcaption>Sign in to your <b>SENTIENT Edge CE</b> instance and go to the <b>Rule chains</b> section. To add a new <b>Rule chain</b>, click the <b>"+"</b> button in the top right corner, and choose the <b>"Create new rule chain"</b> option.</figcaption></figure><figure><img src="/images/edge/rule-engine/2-create-rule-chain-template.webp" alt="In the pop-up window, enter a name for the new rule chain and click the &quot;Add&quot; button to continue configuring the rule chain." loading="lazy"><figcaption>In the pop-up window, enter a <b>name</b> for the new rule chain and click the <b>"Add"</b> button to continue configuring the rule chain.</figcaption></figure><figure><img src="/images/edge/rule-engine/3-in-the-list.webp" alt="The rule chain is now listed, usually at the top. Click it to begin editing." loading="lazy"><figcaption>The rule chain is now listed, usually at the top. Click it to begin editing.</figcaption></figure><figure><img src="/images/edge/rule-engine/4-configure-and-safe.webp" alt="Configure your rule nodes and flow. Once the configuration is complete, click the &quot;Apply changes&quot; button." loading="lazy"><figcaption>Configure your <a href="/docs/user-guide/rule-engine-2-0/overview/#rule-node" target="_blank">rule nodes</a> and flow. Once the configuration is complete, click the <b>"Apply changes"</b> button.</figcaption></figure></div>


### Creating Rule Chain Template on the Server


1. Sign in to your <b>SENTIENT</b> instance and go to the <b>Edge Management > Rule chain templates</b> section. To add a new <b>Rule chain</b>, click the <b>"+"</b> button in the top right corner and choose the <b>"Create new rule chain"</b> option.

1. Enter a name for your rule chain, such as <b>"Remote Farm"</b>. Click <b>"Add"</b> to confirm the creation of your new rule chain template.

1. The rule chain template is now listed, usually at the top. Click it to begin editing.

1. Within the template, configure your <a href="/docs/user-guide/rule-engine-2-0/overview/#rule-node" target="_blank">rule nodes</a> and flow. Once the configuration is complete, click the <b>"Apply changes"</b> button. <i>Note: This step does not activate the rule chain on the server, it simply prepares it for deployment to an Edge.</i>


<div class="st-gallery"><figure><img src="/images/edge/rule-engine/create-rule-chain-template-step-1.webp" alt="Sign in to your SENTIENT instance and go to the Edge Management > Rule chain templates section. To add a new Rule chain, click the &quot;+&quot; button in the top right corner and choose the &quot;Create new rule chain&quot; option." loading="lazy"><figcaption>Sign in to your <b>SENTIENT</b> instance and go to the <b>Edge Management > Rule chain templates</b> section. To add a new <b>Rule chain</b>, click the <b>"+"</b> button in the top right corner and choose the <b>"Create new rule chain"</b> option.</figcaption></figure><figure><img src="/images/edge/rule-engine/create-rule-chain-template-step-2.webp" alt="Enter a name for your rule chain, such as &quot;Remote Farm&quot;. Click &quot;Add&quot; to confirm the creation of your new rule chain template." loading="lazy"><figcaption>Enter a name for your rule chain, such as <b>"Remote Farm"</b>. Click <b>"Add"</b> to confirm the creation of your new rule chain template.</figcaption></figure><figure><img src="/images/edge/rule-engine/create-rule-chain-template-step-3.webp" alt="The rule chain template is now listed, usually at the top. Click it to begin editing." loading="lazy"><figcaption>The rule chain template is now listed, usually at the top. Click it to begin editing.</figcaption></figure><figure><img src="/images/edge/rule-engine/create-rule-chain-template-step-4.webp" alt="Within the template, configure your rule nodes and flow. Once the configuration is complete, click the &quot;Apply changes&quot; button. Note: This step does not activate the rule chain on the server, it simply prepares it for deployment to an Edge." loading="lazy"><figcaption>Within the template, configure your <a href="/docs/user-guide/rule-engine-2-0/overview/#rule-node" target="_blank">rule nodes</a> and flow. Once the configuration is complete, click the <b>"Apply changes"</b> button. <i>Note: This step does not activate the rule chain on the server, it simply prepares it for deployment to an Edge.</i></figcaption></figure></div>


### Assigning the Rule Chain Template to the Edge


1. Go to the <b>Edge management > Instances</b> section and lick the <b>"Manage edge rule chains"</b> button.

1. To assign the Rule chain template to the Edge, click the <b>"+"</b> button.

1. In the pop-up window, select the rule chain from the drop-down menu and click the <b>"Assign"</b> button.

1. The assigned rule chain template now appears at the top of the list. Assigning the rule chain template to the Edge instance enables the rule chain to process data from Edge devices according to the template configurations.


<div class="st-gallery"><figure><img src="/images/edge/rule-engine/assign-rule-chain-template-step-1.webp" alt="Go to the Edge management > Instances section and lick the &quot;Manage edge rule chains&quot; button." loading="lazy"><figcaption>Go to the <b>Edge management > Instances</b> section and lick the <b>"Manage edge rule chains"</b> button.</figcaption></figure><figure><img src="/images/edge/rule-engine/assign-rule-chain-template-step-2.webp" alt="To assign the Rule chain template to the Edge, click the &quot;+&quot; button." loading="lazy"><figcaption>To assign the Rule chain template to the Edge, click the <b>"+"</b> button.</figcaption></figure><figure><img src="/images/edge/rule-engine/assign-rule-chain-template-step-3.webp" alt="In the pop-up window, select the rule chain from the drop-down menu and click the &quot;Assign&quot; button." loading="lazy"><figcaption>In the pop-up window, select the rule chain from the drop-down menu and click the <b>"Assign"</b> button.</figcaption></figure><figure><img src="/images/edge/rule-engine/assign-rule-chain-template-step-4.webp" alt="The assigned rule chain template now appears at the top of the list. Assigning the rule chain template to the Edge instance enables the rule chain to process data from Edge devices according to the template configurations." loading="lazy"><figcaption>The assigned rule chain template now appears at the top of the list. Assigning the rule chain template to the Edge instance enables the rule chain to process data from Edge devices according to the template configurations.</figcaption></figure></div>


## Verify Assigned Rule Chain on the Edge


1. Sign in to your <b>SENTIENT Edge PE</b> instance and go to the <b>Rule chains</b> section. To view the Rule chain configuration, click on the rule chain.

1. Verify that all settings and configurations are accurately reflected.


<div class="st-gallery"><figure><img src="/images/edge/rule-engine/verify-rule-chain-template-step-1.webp" alt="Sign in to your SENTIENT Edge PE instance and go to the Rule chains section. To view the Rule chain configuration, click on the rule chain." loading="lazy"><figcaption>Sign in to your <b>SENTIENT Edge PE</b> instance and go to the <b>Rule chains</b> section. To view the Rule chain configuration, click on the rule chain.</figcaption></figure><figure><img src="/images/edge/rule-engine/verify-rule-chain-template-step-2.webp" alt="Verify that all settings and configurations are accurately reflected." loading="lazy"><figcaption>Verify that all settings and configurations are accurately reflected.</figcaption></figure></div>


## Next Steps
