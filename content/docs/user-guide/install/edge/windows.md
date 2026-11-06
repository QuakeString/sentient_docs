+++
title = "Installing SENTIENT Edge on Windows"
description = "Installing SENTIENT Edge on Windows"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/edge/windows.md"
+++
<div class="st-callout warn">


<p>Version Compatibility Rules - Read before proceeding
</p>

<p>Before installing SENTIENT Edge, ensure that <b>SENTIENT Server</b> is <a href="/docs/user-guide/install/installation-options/" target="_blank">installed</a> and <a href="/docs/user-guide/install/upgrade-instructions/" target="_blank">updated</a> to the latest version.</p>

<p>Additionally, verify that the <b>SENTIENT Edge and SENTIENT Server versions are compatible</b>.</p>

<p>Compatibility rules:</p>
<ul>
<li>SENTIENT Edge version X.Y.Z works with SENTIENT Server version X.Y.Z and the next <span style="color:red"><strong>two</strong></span> versions.</li><ul>
<li>Example: SENTIENT Edge 3.8.0 works with SENTIENT Server 3.8.0 and <span style="color:red"><strong>two</strong></span> later versions (3.9.0 and 3.9.1). View the <a href="/docs/reference/releases/" target="_blank">SENTIENT Server Release Notes here</a>.</li></ul>
<li>SENTIENT Edge version X.Y.Z <span style="color:red"><strong>does not work</strong></span> with older SENTIENT Server versions.</li><ul>
<li>Example: SENTIENT Edge 3.9.1 <span style="color:red"><strong>does not support</strong></span> SENTIENT Server 3.8.0 or earlier versions. The SENTIENT Server must be <a href="/docs/user-guide/install/upgrade-instructions/" target="_blank">upgraded to the latest version</a> first.</li></ul>
</ul>
<p><strong>Note:</strong> If you run an older version of SENTIENT Edge (e.g., version 3.6.0), the SENTIENT team cannot guarantee the availability or proper functioning of all features.</p>


</div>


<div class="st-callout warn">


**Please consider to use Linux installation option, because Linux is the most stable platform for running SENTIENT. Windows installation will be deprecated in the future. You can find Linux installation guides on [Installation Guide](/docs/user-guide/install/edge/installation-options/) page**.


</div>


This guide provides instructions for installing **SENTIENT Edge** on **Windows**

The steps below apply to:
* 32-bit or 64-bit systems
* Windows versions 11/10


## Prerequisites

To start running **SENTIENT Community Edition Edge**, you will need an active **SENTIENT Community Edition account** that supports **Edge** functionality.


You can install the **SENTIENT** local server. For this, please refer to the [SENTIENT installation guide](/docs/user-guide/install/installation-options/).

The local server can be accessed via [http://localhost:8080](http://localhost:8080). Throughout this tutorial, we will refer to this URL as **SERVER_URL.** Log in with:
* **Username:** tenant@sentient.org
* **Password:** tenant


### Edge Hardware Requirements

The hardware requirements for **SENTIENT Edge** are determined by the number of connected devices and the intensity of interactions with the platform interface.
To ensure optimal performance, we recommend the following:
* **At least 1GB of RAM (Light workload):** It is suitable for minimal interactions with the platform interface, such as dashboards and device management, and fewer than 100 connected devices.
* **At least 4GB of RAM (Heavy workload):** This configuration is suitable for intense platform interactions and 100+ devices connected to a single machine.

### Deploying a New Edge Instance

To create a new **Edge**:


1. Sign in to your **SENTIENT** instance and navigate to the **Edge Management > Instances** section. Click the **"+"** icon in the top right corner and select the **"Add new edge"** option.

1. Enter a name for the Edge you are creating. For example, "My New Edge". Click the **"Add"** button to confirm the addition of the **Edge instance**.

1. Your new **Edge** is created and will appear at the top of the list, as entries are sorted by creation time by default.


<div class="st-gallery"><figure><img src="/images/edge/installation-add-edge-item-1.webp" alt="Sign in to your **SENTIENT** instance and navigate to the **Edge Management > Instances** section. Click the **&quot;+&quot;** icon in the top right corner and select the **&quot;Add new edge&quot;** option." loading="lazy"><figcaption>Sign in to your **SENTIENT** instance and navigate to the **Edge Management > Instances** section. Click the **"+"** icon in the top right corner and select the **"Add new edge"** option.</figcaption></figure><figure><img src="/images/edge/installation-add-edge-item-2.webp" alt="Enter a name for the Edge you are creating. For example, &quot;My New Edge&quot;. Click the **&quot;Add&quot;** button to confirm the addition of the **Edge instance**." loading="lazy"><figcaption>Enter a name for the Edge you are creating. For example, "My New Edge". Click the **"Add"** button to confirm the addition of the **Edge instance**.</figcaption></figure><figure><img src="/images/edge/installation-add-edge-item-3.webp" alt="Your new **Edge** is created and will appear at the top of the list, as entries are sorted by creation time by default." loading="lazy"><figcaption>Your new **Edge** is created and will appear at the top of the list, as entries are sorted by creation time by default.</figcaption></figure></div>


## Installation and Configuration

### Step 1. Install Java 17 (OpenJDK) 

SENTIENT service is running on Java 17. Follow this instructions to install OpenJDK 17.

 * Visit [Open JDK Download Page](https://adoptium.net). Go to "Other platforms and versions", select "Operating System" as "Windows", "Architecture" as "x64", "Version" as "17 - LTS" and download **JDK .msi** package. 
 * Run the downloaded MSI package and follow the instructions. 
 Make sure you have selected "**Add to PATH**" and "**Set JAVA_HOME variable**" options to "Will be installed on local hard drive" state.
 * Visit [PostgreSQL JDBC Download Page](https://jdbc.postgresql.org/download/) to download PostgreSQL JDBC Driver. Choose the latest available option.
 * Create the folder **C:\Program Files\JDBC** and copy downloaded file there. Then, add a new global variable - run PowerShell as an administrator and execute the following command. Do not forget to change "postgresql-42.2.18.jar" in the command to match the downloaded version.
 ```powershell
[System.Environment]::SetEnvironmentVariable("CLASSPATH", '.;"C:\Program Files\JDBC\postgresql-42.2.18.jar"', [System.EnvironmentVariableTarget]::Machine)
```


You can check the installation using the following command (using Command Prompt):

```bash
java -version
```


Expected command output is:

```
C:\Users\User>java -version
openjdk version "17.x.xx" 
OpenJDK Runtime Environment Temurin-17.x.xx (...)
OpenJDK 64-Bit Server VM Temurin-17.x.xx (...)
```


### Step 2. Configure PostgreSQL

SENTIENT Edge uses PostgreSQL database as a local storage. 

#### PostgreSQL Installation

Download the installation file (PostgreSQL 12.17 or newer releases) [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows) and follow the installation instructions.

During PostgreSQL installation, you will be prompted for superuser (postgres) password.
Don't forget this password. It will be used later. For simplicity, we will substitute it with "postgres".

#### Create SENTIENT Edge Database

Once installed, launch the "pgAdmin" software and login as superuser (postgres). 
Open your server and create database **tb_edge** with owner "postgres".


### Step 3. SENTIENT Edge service installation

Download and extract the package.

```bash
https://github.com/sentient/sentient-gateway/releases/download//tb-edge-windows-.zip
```


**Note:** We assume you have unzipped package to default location: *C:\Program Files (x86)\tb-edge*

### Step 4. Configure SENTIENT Edge


Open the Notepad or other editor as administrator user (right click on the app icon and select "Run as administrator").  
Open the following file for editing (select "All Files" instead of "Text Documents" in file choosing dialog, the encoding is UTF-8):

```
C:\Program Files (x86)\tb-edge\conf\tb-edge.yml
``` 


#### Database configuration

In the file "tb-edge.yml" from the previous step locate "# SQL DAO Configuration" block. 

Don't forget to **replace YOUR_POSTGRES_PASSWORD_HERE** with your real postgres user password:

```yml
# SQL DAO Configuration
spring:
  data:
    jpa:
      repositories:
        enabled: "true"
  jpa:
    hibernate:
      ddl-auto: "none"
  datasource:
    driverClassName: "${SPRING_DRIVER_CLASS_NAME:org.postgresql.Driver}"
    url: "${SPRING_DATASOURCE_URL:jdbc:postgresql://localhost:5432/tb_edge}"
    username: "${SPRING_DATASOURCE_USERNAME:postgres}"
    password: "${SPRING_DATASOURCE_PASSWORD:YOUR_POSTGRES_PASSWORD_HERE}"
``` 
#### Configure cloud connectivity

Click on **Copy Edge Key** and **Copy Edge Secret** in the edge details section.
This will copy your edge credentials to your clipboard.
Be sure to store them in a secure location, as these values will be needed in the following steps.


<div class="st-gallery"><figure><img src="/images/edge/installation-copy-edge-credentials-item-1.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Locate "# Cloud configuration" block and replace **PUT_YOUR_EDGE_KEY_HERE** and **PUT_YOUR_EDGE_SECRET_HERE** with Edge **key and secret** respectively. 

Please replace **PUT_YOUR_CLOUD_IP** with an IP address of the machine where SENTIENT version is running:

* Use **localhost** in case edge is running on the same machine where cloud instance is running. 
* Use **X.X.X.X** IP address in case edge is connecting to the cloud instance in the same network or in the docker.


```yml
# Cloud configuration
cloud:
    routingKey: "${CLOUD_ROUTING_KEY:PUT_YOUR_EDGE_KEY_HERE}"
    secret: "${CLOUD_ROUTING_SECRET:PUT_YOUR_EDGE_SECRET_HERE}"
    rpc:
      host: "${CLOUD_RPC_HOST:PUT_YOUR_CLOUD_IP}"
```


<div class="st-callout info">


If SENTIENT Edge is set to run on the same machine where the **SENTIENT** server is operating, you need to update additional configuration parameters to prevent port collision between the SENTIENT server and SENTIENT Edge.

Please locate and change next parameters in SENTIENT Edge configuration file (**C:\Program Files (x86)\tb-edge\conf\tb-edge.yml**):
<br>
<br>**...**
<br>**port: "${HTTP_BIND_PORT:18080}"**
<br>**...**
<br>**bind_port: "${MQTT_BIND_PORT:11883}"**
<br>**...**
<br>**bind_port: "${COAP_BIND_PORT:15683}"**
<br>**...**
<br>**bind_port: "${LWM2M_ENABLED:false}"**
<br>**...**

Ensure that the ports listed above (18080, 11883, 15683) are not being used by any other application.


</div>


### Step 5. Run installation script


Launch windows shell (Command Prompt) as Administrator. Change directory to your SENTIENT Edge installation directory.

Execute **install.bat** script to install SENTIENT Edge as a Windows service.
This means it will be automatically started on system startup. 
Similar, **uninstall.bat** will remove SENTIENT Edge from Windows services.
The output should be similar to this one:

  ```
C:\Program Files (x86)\tb-edge\install.bat
Detecting Java version installed.
CurrentVersion 110
Java 11 found!
Installing Sentient Edge...
...
SENTIENT Edge installed successfully!
```
 

### Step 6. Start SENTIENT Edge service

Now let's start the SENTIENT Edge service!
Open the command prompt as an Administrator and execute the following command:

```bash
net start tb-edge
```


Expected output:

```
The SENTIENT Edge Server Application service is starting.
The SENTIENT Edge Server Application service was started successfully.
```

In order to restart the SENTIENT Edge service you can execute following commands:

```bash
net stop tb-edge
net start tb-edge
```


### Step 7. Open SENTIENT Edge UI


Once the **Edge** service is started, open the **Edge UI** at [http://localhost:8080](http://localhost:8080).


<div class="st-callout info">


If the Edge **HTTP bind port** was changed to **18080** during Edge installation, access the **SENTIENT Edge** instance at [http://localhost:18080](http://localhost:18080).


</div>


Please use your tenant credentials from **SENTIENT Server** to log in to the **SENTIENT Edge**. 

## Troubleshooting

The log files are located in **logs** folder ("C:\Program Files (x86)\tb-edge\logs" in our case).

The **tb-edge.log** file should contain following line:

```
YYYY-MM-DD HH:mm:ss,sss [main] INFO  o.t.server.TbEdgeApplication - Started TbEdgeApplication in x.xxx seconds (JVM running for x.xxx)
```

In case of any unclear errors, use general [troubleshooting guide](/docs/user-guide/troubleshooting/#getting-help) or [contact us](/docs/contact-us/).

## Windows firewall settings

In order to have external access to SENTIENT Web UI and device connectivity (HTTP, MQTT, CoAP)
you need to create a new inbound rule with Windows Firewall with Advanced Security.
 
- Open "Windows Firewall" from "Control Panel":

![image](/images/user-guide/install/windows/windows7-firewall-1.webp)

- Click "Advanced settings" on the left panel:

![image](/images/user-guide/install/windows/windows7-firewall-2.webp)

- Select "Inbound Rules" on the left panel, then click "New Rule..." on the right "Actions" panel:

![image](/images/user-guide/install/windows/windows7-firewall-3.webp)

- Now new "New Inbound Rule Wizard" window will open. On the first step "Rule Type" select "Port" option: 

![image](/images/user-guide/install/windows/windows7-firewall-4.webp)

- On the "Protocol and Ports" step select "TCP" protocol and enter port list **8080, 1883, 5683** in the "Specific local ports" field:

![image](/images/user-guide/install/windows/windows7-firewall-5.webp)

- On the "Action" step leave "Allow the connection" option selected:

![image](/images/user-guide/install/windows/windows7-firewall-6.webp)

- On the "Profile" step select Windows network profiles when to apply this rule:

![image](/images/user-guide/install/windows/windows7-firewall-7.webp)

- Finally, give the name to this rule (for ex. "SENTIENT Service Networking") and click "Finish".

![image](/images/user-guide/install/windows/windows7-firewall-8.webp)


## Next Steps

Congratulations! You have successfully provisioned, installed and connected SENTIENT **Edge** to SENTIENT server.

You can continue with **Getting started guide** to get the basic knowledge of SENTIENT **Edge** or you can jump directly to more advanced topics:
