+++
title = "IoT Gateway Pip installation."

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/install/pip-installation.md"
+++
## Package manager installation

To install SENTIENT IoT Gateway as python module, you should follow steps below:  

**1. Install required libraries to the system with apt:**  

```bash
sudo apt install python3-dev python3-pip libglib2.0-dev 
```


**2. Install SENTIENT IoT Gateway module with pip:**  

```bash
sudo pip3 install sentient-gateway
```


**3. Download example of configs, create log folder:**  

- Downloading configs example:  

  ```bash
  wget https://github.com/sentient/sentient-gateway/releases/latest/download/configs.tar.gz
  ```
  

- Make directory for configs:  
  ```bash
  sudo mkdir /etc/sentient-gateway
  ```
  

- Make directory for logs:  
  ```bash
  sudo mkdir /var/log/sentient-gateway
  ```
  

- Unpack configs:
  ```bash
  sudo tar -xvzf configs.tar.gz -C /etc/sentient-gateway
  ```
  


**4. Set permission to the folders:**

- For logs folder:
  ```bash
  sudo chown YOUR_USER:YOUR_USER -R /var/log/sentient-gateway
  ```
  

- For configs folder:
  ```bash
  sudo chown YOUR_USER:YOUR_USER -R /etc/sentient-gateway
  ```
  

- For tmp folder:
  ```bash
  sudo chown YOUR_USER:YOUR_USER /tmp
  ```
  

Where `YOUR_USER` is a user who will run the gateway.

**5. Configure gateway:**

First, add a gateway device to your SENTIENT instance by following these steps:


1. Go to the "**Entities**" > "**Gateways**" page and click the "**plus**" icon in the upper right corner to add a new gateway.

1. In the opened modal window input the gateway name(e.g., "My Gateway"), specify the "**default**" device profile, and click "**Create**".


<div class="st-gallery"><figure><img src="/images/gateway/dashboard/gateway-getting-started-1-ce.webp" alt="Go to the &quot;**Entities**&quot; > &quot;**Gateways**&quot; page and click the &quot;**plus**&quot; icon in the upper right corner to add a new gateway." loading="lazy"><figcaption>Go to the "**Entities**" > "**Gateways**" page and click the "**plus**" icon in the upper right corner to add a new gateway.</figcaption></figure><figure><img src="/images/gateway/dashboard/gateway-getting-started-2-ce.webp" alt="In the opened modal window input the gateway name(e.g., &quot;My Gateway&quot;), specify the &quot;**default**&quot; device profile, and click &quot;**Create**&quot;." loading="lazy"><figcaption>In the opened modal window input the gateway name(e.g., "My Gateway"), specify the "**default**" device profile, and click "**Create**".</figcaption></figure></div>


Now, we have to configure gateway using right host, port and credentials, for this purpose use the following steps:

- Click the "**General configuration**" button, and copy **Access token** on the "**General**" tab;
- Open Terminal and execute the following command:

```
nano /etc/sentient-gateway/config/tb_gateway.json
```


- Paste copied access token and replace platform's host and port with yours;
- Save changes and exit from nano.


<div class="st-gallery"><figure><img src="/images/gateway/install/configure-gateway-1-ce.webp" alt="Click the &quot;**General configuration**&quot; button;" loading="lazy"><figcaption>Click the "**General configuration**" button;</figcaption></figure><figure><img src="/images/gateway/install/configure-gateway-2-ce.webp" alt="Copy **Access token** on the &quot;**General**&quot; tab;" loading="lazy"><figcaption>Copy **Access token** on the "**General**" tab;</figcaption></figure><figure><img src="/images/gateway/install/configure-gateway-3-ce.webp" alt="Open Terminal and execute the following command: `nano /etc/sentient-gateway/config/tb_gateway.json`. Paste copied access token and replace platform&#39;s host and port with yours. Save changes and exit from nano." loading="lazy"><figcaption>Open Terminal and execute the following command: `nano /etc/sentient-gateway/config/tb_gateway.json`. Paste copied access token and replace platform&#39;s host and port with yours. Save changes and exit from nano.</figcaption></figure></div>


**6. Configure logging:**

- Click the "**General configuration**" button;
- Navigate to the "**Logs**" tab and replace the "**File path**" field value to:

```
/var/log/sentient-gateway 
```


- Repeat the previous step for all tabs in the "**Local logging**" section;
- Click "**Save**".


<div class="st-gallery"><figure><img src="/images/gateway/install/configure-gateway-4-ce.webp" alt="Click the &quot;**General configuration**&quot; button;" loading="lazy"><figcaption>Click the "**General configuration**" button;</figcaption></figure><figure><img src="/images/gateway/install/configure-gateway-5-ce.webp" alt="Navigate to the &quot;**Logs**&quot; tab and replace the &quot;**File path**&quot; field value to `/var/log/sentient-gateway` in all tabs. Then, click &quot;**Save**&quot;." loading="lazy"><figcaption>Navigate to the "**Logs**" tab and replace the "**File path**" field value to `/var/log/sentient-gateway` in all tabs. Then, click "**Save**".</figcaption></figure></div>


**7. You can check installation with this command**. *For configuration please use [Configuration guide](/docs/iot-gateway/configuration/):*

```bash
sentient-gateway
```


- If everything is done correctly, you will see the gateway status set to `Active`.


<div class="st-gallery"><figure><img src="/images/gateway/install/configure-gateway-6-ce.webp" alt="If everything is done correctly, you will see the gateway status set to `Active`." loading="lazy"><figcaption>If everything is done correctly, you will see the gateway status set to `Active`.</figcaption></figure></div>


## Next steps

Explore guides related to main SENTIENT features:

 - [Getting Started](/docs/iot-gateway/getting-started/) with SENTIENT IoT Gateway.
 - [Data Visualization](/docs/user-guide/visualization/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine/) - how to use rule engine to analyze data from devices.
