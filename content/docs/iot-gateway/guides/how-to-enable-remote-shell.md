+++
title = "How to enable remote shell feature on SENTIENT IoT Gateway"
description = "How to enable remote shell feature on SENTIENT IoT Gateway"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/guides/how-to-enable-remote-shell.md"
+++
This guide will help you to enable a remote shell feature and control the operating system with SENTIENT IoT Gateway
from your SENTIENT platform instance. With this functionality, you can access the underlying machine, execute
commands, and perform maintenance tasks directly from the platform. It provides a convenient way to monitor system
health, troubleshoot issues, and automate administrative operations without needing direct physical access. Before
proceeding, ensure that you have the necessary permissions and have configured your gateway according to the
prerequisites outlined in this documentation.


<div class="st-callout warn">


<div>
  <p>
    <b style="color:red">WARNING:</b>
    <span style="color:black">This feature may introduce security vulnerabilities. It is strongly recommended to use SSL encryption when enabling it, and to keep it disabled unless required.</span>
  </p>
</div>


</div>


## Prerequisites

1. Ensure that the SENTIENT server is up and running. The simplest approach is to use [SENTIENT Cloud](https://sentient.invenia.in/installations/). Alternatively, you can install SENTIENT manually by following the steps outlined in the [Installation Guide](/docs/user-guide/install/installation-options/).
2. Installed and configured SENTIENT IoT Gateway ([Installation guide](/docs/iot-gateway/installation/), [Getting Started](/docs/iot-gateway/getting-started/)).

## Step 1. Remote shell activation

To enable the remote shell feature, configure the corresponding parameter in the Gateway UI using the following steps:


1. Go to the **Entities** > **Gateways** tab and click on the desired gateway.

1. Click on the **"General configuration"** button on the right panel.

1. In the opened window, navigate to the **General** tab and enable the **"Remote shell"** option. Click on the **"Save"** button to apply the changes.


<div class="st-gallery"><figure><img src="/images/gateway/remote-shell/remote-shell-1.webp" alt="Go to the **Entities** > **Gateways** tab and click on the desired gateway." loading="lazy"><figcaption>Go to the **Entities** > **Gateways** tab and click on the desired gateway.</figcaption></figure><figure><img src="/images/gateway/remote-shell/remote-shell-2.webp" alt="Click on the **&quot;General configuration&quot;** button on the right panel." loading="lazy"><figcaption>Click on the **"General configuration"** button on the right panel.</figcaption></figure><figure><img src="/images/gateway/remote-shell/remote-shell-3.webp" alt="In the opened window, navigate to the **General** tab and enable the **&quot;Remote shell&quot;** option. Click on the **&quot;Save&quot;** button to apply the changes." loading="lazy"><figcaption>In the opened window, navigate to the **General** tab and enable the **"Remote shell"** option. Click on the **"Save"** button to apply the changes.</figcaption></figure></div>


## Step 2. Try out the remote shell

To navigate to the remote shell, follow these steps:


1. On the selected gateway page, click on the **"Remote shell"** button on the right panel.

1. Now you can see the shell interface (_connection setups automatically_).


<div class="st-gallery"><figure><img src="/images/gateway/remote-shell/remote-shell-4.webp" alt="On the selected gateway page, click on the **&quot;Remote shell&quot;** button on the right panel." loading="lazy"><figcaption>On the selected gateway page, click on the **"Remote shell"** button on the right panel.</figcaption></figure><figure><img src="/images/gateway/remote-shell/remote-shell-5.webp" alt="Now you can see the shell interface (_connection setups automatically_)." loading="lazy"><figcaption>Now you can see the shell interface (_connection setups automatically_).</figcaption></figure></div>


For example, we run **ls** command to get the list of files and directories in the current directory:

![](/images/gateway/remote-shell/remote-shell-6.webp)
## Next steps

Explore guides related to main SENTIENT features:

 - [Data Visualization](/docs/user-guide/visualization/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine/) - how to use rule engine to analyze data from devices.
