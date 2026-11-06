+++
title = "Installing SENTIENT Edge using Docker (Windows)"
description = "Installing SENTIENT Edge using Docker (Windows)"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/edge/docker-windows.md"
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


This guide provides step-by-step instructions for installing **SENTIENT Edge** on **Windows** using **Docker**.


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


### Docker installation

- [Install Docker Toolbox for Windows](https://docker-docs.uclv.cu/toolbox/toolbox_install_windows/)

## Installation and Configuration

### Step 1. Running SENTIENT Edge

Here you can find SENTIENT Edge docker image: 


* [sentient/tb-edge](https://hub.docker.com/r/sentient/tb-edge)


Windows users should use docker managed volume for SENTIENT Edge DataBase. 
Create docker volume (for ex. `mytb-edge-data`) before executing docker run command:
Open "Docker Quickstart Terminal". Execute the following command to create docker volume:

``` 
docker volume create mytb-edge-data
docker volume create mytb-edge-logs
docker volume create mytb-edge-data-db
```


Click on **Copy Edge Key** and **Copy Edge Secret** in the edge details section.
This will copy your edge credentials to your clipboard.
Be sure to store them in a secure location, as these values will be needed in the following steps.


<div class="st-gallery"><figure><img src="/images/edge/installation-copy-edge-credentials-item-1.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


Create docker compose file for SENTIENT Edge service:

```
docker-compose.yml
```


```yml
version: '3.8'
services:
  mytbedge:
    restart: always
    image: "sentient/tb-edge:"
    ports:
      - "8080:8080"
      - "1883:1883"
      - "5683-5688:5683-5688/udp"
    environment:
      SPRING_DATASOURCE_URL: jdbc:postgresql://postgres:5432/tb-edge
      CLOUD_ROUTING_KEY: PUT_YOUR_EDGE_KEY_HERE # e.g. 19ea7ee8-5e6d-e642-4f32-05440a529015
      CLOUD_ROUTING_SECRET: PUT_YOUR_EDGE_SECRET_HERE # e.g. bztvkvfqsye7omv9uxlp
      CLOUD_RPC_HOST: PUT_YOUR_CLOUD_IP # e.g. 192.168.1.1
    volumes:
      - mytb-edge-data:/data
      - mytb-edge-logs:/var/log/tb-edge
  postgres:
    restart: always
    image: "postgres:16"
    ports:
      - "5432"
    environment:
      POSTGRES_DB: tb-edge
      POSTGRES_PASSWORD: postgres
    volumes:
      - mytb-edge-data-db:/var/lib/postgresql/data
volumes:
  mytb-edge-data:
    external: true
  mytb-edge-logs:
    external: true
  mytb-edge-data-db:
    external: true
```


Where:    
- **restart: always:** SENTIENT Edge automatically starts on system reboot or after a failure.
- **8080:8080:** Connect local port 8080 to the container's internal HTTP port 8080.
- **1883:1883:** Connect local port 1883 to the container's internal MQTT port 1883.
- **5683-5688:5683-5688/udp:** Connect local UDP ports 5683–5688 to the container’s internal CoAP and LwM2M ports.
- **sentient/tb-edge::** The SENTIENT Edge Docker image.
- **CLOUD_ROUTING_KEY:** Enter the actual Edge key.
- **CLOUD_ROUTING_SECRET:** Enter the actual Edge secret.
- **CLOUD_RPC_HOST:** he IP address or hostname of the machine running the SENTIENT platform.


<div class="st-callout info">


Please set **CLOUD_RPC_HOST** with an IP address of the machine where SENTIENT version is running:
* DO NOT use **'localhost'** - **'localhost'** is the ip address of the edge service in the docker container.
* Use **X.X.X.X** IP address if the Edge is connected to the Cloud instance in the same network or Docker environment.


</div>


<div class="st-callout info">


If **SENTIENT Edge** is set to run on the **same machine** where the **SENTIENT** server is operating, you need to update port configuration to prevent port collision between the SENTIENT server and SENTIENT Edge.

Ensure that the ports **18080, 11883, 15683-15688** are not used by any other application.


</div>


To update the port configuration in the **docker-compose.yml** file, run:

```bash
sed -i 's/8080:8080/18080:8080/; s/1883:1883/11883:1883/; s/5683-5688:5683-5688\/udp/15683-15688:5683-5688\/udp/' docker-compose.yml
```


Set the terminal in the directory which contains the `docker-compose.yml` file and execute the following commands to up this docker compose directly:

```
docker compose up -d && docker compose logs -f mytbedge
```


Where:
- `C:\Program Files\Oracle\VirtualBox` - path to your VirtualBox installation directory

### Step 2. Open SENTIENT Edge UI


Once the **Edge** service is started, open the **Edge UI** at [http://localhost:8080](http://localhost:8080).


<div class="st-callout info">


If the Edge **HTTP bind port** was changed to **18080** during Edge installation, access the **SENTIENT Edge** instance at [http://localhost:18080](http://localhost:18080).


</div>


Please use your tenant credentials from **SENTIENT Server** to log in to the **SENTIENT Edge**.

### Step 3. Detaching, stop and start commands


You can detach from session terminal using `Ctrl-p` `Ctrl-q` key sequence - the container will keep running in the background.

In case of any issues you can examine service logs for errors.
For example to see SENTIENT Edge container logs execute the following command:

```
docker compose logs -f mytbedge
```


To stop the container:

```
docker compose stop mytbedge
```


To start the container:

```
docker compose start mytbedge
```


<div class="st-callout info">


Docker Compose as docker-compose (with a hyphen) is deprecated. It is recommended to use Docker Compose V2 instead.
<br>If you still rely on docker compose as standalone here is the list of the above commands:
<br>**docker-compose logs -f mytbedge**
<br>**docker-compose stop mytbedge**
<br>**docker-compose start mytbedge**


</div>


## Troubleshooting

### DNS issues

**NOTE** If you observe errors related to DNS issues, for example

```bash
127.0.1.1:53: cannot unmarshal DNS message
```

You may configure your system to use [Google public DNS servers](https://developers.google.com/speed/public-dns/docs/using#windows)

## Next Steps

Congratulations! You have successfully provisioned, installed and connected SENTIENT **Edge** to SENTIENT server.

You can continue with **Getting started guide** to get the basic knowledge of SENTIENT **Edge** or you can jump directly to more advanced topics:
