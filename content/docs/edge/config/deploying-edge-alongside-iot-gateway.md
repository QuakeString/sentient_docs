+++
title = "Deploying SENTIENT Edge Alongside SENTIENT IoT Gateway"
description = "Deploying SENTIENT Edge alongside SENTIENT IoT Gateway"

[extra]
status = "imported"
checked = ""
source = "docs/edge/config/deploying-edge-alongside-iot-gateway.md"
+++
The [SENTIENT Edge](/docs/edge/getting-started-guides/what-is-edge/) can be run alongside the [SENTIENT IoT Gateway](/docs/iot-gateway/what-is-iot-gateway/). 
This approach can create a robust, decentralized IoT architecture due to **Edge's** ability to process data at its source and **IoT Gateway's** extended list of communication protocols.

## How Does It Work?

**SENTIENT IoT Gateway** collects data locally, translates it into the [SENTIENT-compatible communication protocols](/docs/edge/api/), and transmits it to the **SENTIENT Edge**.
The [Rule Engine](/docs/user-guide/rule-engine-2-0/re-getting-started/) processes the data in real time, enabling immediate visualizations and event responses. Summarised or aggregated data can be sent to the central server for analysis if required.

![image](/images/edge/how-does-it-work.webp)


<div class="st-callout info">


When deployed in remote locations with unreliable internet connections, **Edge** continues operating until connectivity is restored.


</div>


## Prerequisites
* Have [Docker](https://docs.docker.com/engine/install/) installed
* The **SENTIENT Cloud** Account (Demo, Professional edition, or Community edition)
* Any Linux-based **IoT Gateway** device

## Step 1. Creating a New Edge Instance


1. Log in to your <b>Cloud account</b> and navigate to the <b>Edge Management > Instances</b> section. Click the <b>“+”</b> button and select the <b>“Add new edge”</b> option.

1. In the <b>"Add Edge"</b> pop-up window, enter a name for your Edge in the <b>"Name"</b> field, and click the <b>"Add"</b> button.

1. The <b>Edge instance</b> is displayed at the top of the list, as entries are sorted by creation time by default.


<div class="st-gallery"><figure><img src="/images/devices-library/edge/recomputer-r1000/installation-add-edge-item-1.webp" alt="Log in to your Cloud account and navigate to the Edge Management > Instances section. Click the “+” button and select the “Add new edge” option." loading="lazy"><figcaption>Log in to your <b>Cloud account</b> and navigate to the <b>Edge Management > Instances</b> section. Click the <b>“+”</b> button and select the <b>“Add new edge”</b> option.</figcaption></figure><figure><img src="/images/devices-library/edge/recomputer-r1000/installation-add-edge-item-2.webp" alt="In the &quot;Add Edge&quot; pop-up window, enter a name for your Edge in the &quot;Name&quot; field, and click the &quot;Add&quot; button." loading="lazy"><figcaption>In the <b>"Add Edge"</b> pop-up window, enter a name for your Edge in the <b>"Name"</b> field, and click the <b>"Add"</b> button.</figcaption></figure><figure><img src="/images/devices-library/edge/recomputer-r1000/installation-add-edge-item-3.webp" alt="The Edge instance is displayed at the top of the list, as entries are sorted by creation time by default." loading="lazy"><figcaption>The <b>Edge instance</b> is displayed at the top of the list, as entries are sorted by creation time by default.</figcaption></figure></div>


## Step 2. Installing Edge on the Gateway Device

To install the **Edge instance** on the **IoT Gateway** device, initiate the **SSH (Secure Shell)** connection to the **device** through the terminal:

```bash
ssh username@ip_address
```


* **username:** Enter the actual username with access to the Gateway device;
* **ip_address:** Enter the actual IP address of the Gateway device;
* **password:** The terminal will request the authentication credentials.


<div class="st-callout info">


If the **SSH** server runs on a non-default port, specify it with the **-p** command.<br>
Example: _ssh -p 2222 username@ip_address_


</div>


Once connected, create a new directory:

```bash
mkdir tb_edge
```


Create a docker-compose file for the **SENTIENT Edge** service within this directory:

```bash
nano docker-compose.yml
```


Configure this file:


1. Go to the <b>Edge Management > Instances</b> section, and click on the <b>Edge instance</b>. On the <b>Edge details"</b> page, click the <b>"Install & Connect Instructions"</b> button.

1. In the <b>"Install & Connect Instructions"</b> pop-up window, select the <b>"Docker"</b> tab and copy the configuration lines.

1. Paste the copied lines into the <b>docker-compose.yml</b> file in the terminal and save it. To close the file, press <b>CTRL+X</b>.


<div class="st-gallery"><figure><img src="/images/devices-library/edge/recomputer-r1000/1.2-instrucrions-button.webp" alt="Go to the Edge Management > Instances section, and click on the Edge instance. On the Edge details&quot; page, click the &quot;Install & Connect Instructions&quot; button." loading="lazy"><figcaption>Go to the <b>Edge Management > Instances</b> section, and click on the <b>Edge instance</b>. On the <b>Edge details"</b> page, click the <b>"Install & Connect Instructions"</b> button.</figcaption></figure><figure><img src="/images/devices-library/edge/recomputer-r1000/1.3-docker.webp" alt="In the &quot;Install & Connect Instructions&quot; pop-up window, select the &quot;Docker&quot; tab and copy the configuration lines." loading="lazy"><figcaption>In the <b>"Install & Connect Instructions"</b> pop-up window, select the <b>"Docker"</b> tab and copy the configuration lines.</figcaption></figure><figure><img src="/images/edge/config/paste-yml-terminal.webp" alt="Paste the copied lines into the docker-compose.yml file in the terminal and save it. To close the file, press CTRL+X." loading="lazy"><figcaption>Paste the copied lines into the <b>docker-compose.yml</b> file in the terminal and save it. To close the file, press <b>CTRL+X</b>.</figcaption></figure></div>


To run the **Edge instance** on the **IoT Gateway device**, execute the following commands:

```bash
docker compose up -d
docker compose logs -f mytbedge
```


<div class="st-callout info">


The command must be executed in the same directory in which the **docker-compose.yml** file is saved.


</div>


To configure a **local port forwarding via SSH**, open **another terminal tab** and execute the following command:

```bash
ssh -N -L 8080:127.0.0.1:8080 username@ip_address
```


* **8080:** The port on your local machine;
* **127.0.0.1:** The target remote host accessible by the IoT Gateway device;
* **8080:** The port to access the IoT Gateway device.
* **username:** Enter the actual username with access to the Gateway device;
* **ip_address:** Enter the actual IP address of the Gateway device;

Any connection to **localhost:8080** on your local machine will be forwarded to **127.0.0.1:8080** on the **IoT Gateway device**. The **SENTIENT Edge** instance is available at [**http://127.0.0.1:8080**](http://127.0.0.1:8080). Use your credentials to log in.

## Step 3. Provisioning the SENTIENT IoT Gateway on Edge

To provision the **SENTIENT IoT Gateway** on **Edge** instance:


1. Log into your Cloud, navigate to the <b>Edge Management > Instances</b> section, and click the <b>“Manage dashboards”</b> button.

1. Click the <b>“+”</b> button. Select the <b>“SENTIENT IoT Gateways”</b> dashboard from the drop-down menu in the pop-up window. Click the <b>“Assign”</b> button to assign it to the <b>Edge instance</b>. The <b>“SENTIENT IoT Gateways”</b> dashboard is one of the pre-created, out-of-the-box dashboards available.

1. Use <a href="http://127.0.0.1:8080" target="_blank">http://127.0.0.1:8080</a> to open the <b>Edge instance</b>, log in with your credentials, and go to the <b>Dashboards</b> section to open the <b>“SENTIENT IoT Gateways”</b> dashboard.

1. Click the <b>“+”</b> button to add a new <b>IoT Gateway</b> device. Enter the gateway name in the <b>“Name”</b> field, and select the <b>“default”</b> device profile. Click the <b>“Create”</b> button.

1. Download the <b>docker-compose.yml</b> file for your IoT Gateway device from the <b>“Launch command”</b> pop-up window.


<div class="st-gallery"><figure><img src="/images/devices-library/edge/recomputer-r1000/1-instances-section.webp" alt="Log into your Cloud, navigate to the Edge Management > Instances section, and click the “Manage dashboards” button." loading="lazy"><figcaption>Log into your Cloud, navigate to the <b>Edge Management > Instances</b> section, and click the <b>“Manage dashboards”</b> button.</figcaption></figure><figure><img src="/images/devices-library/edge/recomputer-r1000/2-assign-dashboard.webp" alt="Click the “+” button. Select the “SENTIENT IoT Gateways” dashboard from the drop-down menu in the pop-up window. Click the “Assign” button to assign it to the Edge instance. The “SENTIENT IoT Gateways” dashboard is one of the pre-created, out-of-the-box dashboards available." loading="lazy"><figcaption>Click the <b>“+”</b> button. Select the <b>“SENTIENT IoT Gateways”</b> dashboard from the drop-down menu in the pop-up window. Click the <b>“Assign”</b> button to assign it to the <b>Edge instance</b>. The <b>“SENTIENT IoT Gateways”</b> dashboard is one of the pre-created, out-of-the-box dashboards available.</figcaption></figure><figure><img src="/images/devices-library/edge/recomputer-r1000/3-login-to-edge.webp" alt="Use http://127.0.0.1:8080 to open the Edge instance, log in with your credentials, and go to the Dashboards section to open the “SENTIENT IoT Gateways” dashboard." loading="lazy"><figcaption>Use <a href="http://127.0.0.1:8080" target="_blank">http://127.0.0.1:8080</a> to open the <b>Edge instance</b>, log in with your credentials, and go to the <b>Dashboards</b> section to open the <b>“SENTIENT IoT Gateways”</b> dashboard.</figcaption></figure><figure><img src="/images/devices-library/edge/recomputer-r1000/4-add-gw.webp" alt="Click the “+” button to add a new IoT Gateway device. Enter the gateway name in the “Name” field, and select the “default” device profile. Click the “Create” button." loading="lazy"><figcaption>Click the <b>“+”</b> button to add a new <b>IoT Gateway</b> device. Enter the gateway name in the <b>“Name”</b> field, and select the <b>“default”</b> device profile. Click the <b>“Create”</b> button.</figcaption></figure><figure><img src="/images/edge/config/launch-command.webp" alt="Download the docker-compose.yml file for your IoT Gateway device from the “Launch command” pop-up window." loading="lazy"><figcaption>Download the <b>docker-compose.yml</b> file for your IoT Gateway device from the <b>“Launch command”</b> pop-up window.</figcaption></figure></div>


## Step 4. Installing the SENTIENT IoT Gateway Software on the Gateway Device

Once the **docker-compose.yml** file has been downloaded, open the terminal and initiate the **SSH** connection to the **IoT Gateway device**:

```bash
ssh username@ip_address
```


* **username:** Enter the actual username with access to the Gateway device;
* **ip_address:** Enter the actual IP address of the Gateway device;
* **password:** The terminal will request the authentication credentials.

To install **SENTIENT IoT Gateway**, create a new directory:

```bash
mkdir iot_gateway
```


Create the docker-compose file for your **SENTIENT IoT Gateway** within this directory:

```bash
nano docker-compose.yml
```


Copy the content of the previously downloaded **docker-compose.yml** file and paste it into the new one via the terminal:


<div class="st-gallery"><figure><img src="/images/devices-library/edge/recomputer-r1000/10-copy-paste-configs.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Save the changes in the **docker-compose.yml** file. To close it, press **CTRL+X**.

To start the **SENTIENT IoT Gateway**, execute the following command in the terminal:

```bash
docker compose up -d
docker compose logs -f
```


Once the **SENTIENT Edge** and **SENTIENT IoT Gateway** are running on the **IoT Gateway device**, you can connect IoT devices and sensors to transfer data. Read [this real-life example of visualizing data from IoT devices on a Dashboard](/docs/edge/device-library/recomputer-r1000/#visualize-incoming-data-with-the-dashboard) when **SENTIENT Edge** and **Gateway** are deployed on the same **IoT Gateway device**. 

## Next Steps
