+++
title = "Installing Edge Behind a Proxy"
description = "Detailed instructions on how to connect SENTIENT Edge to SENTIENT Cloud behind a proxy."

[extra]
status = "imported"
checked = ""
source = "docs/edge/config/edge-behind-proxy.md"
+++
### Overview

Installing **Edge** behind a [proxy](https://en.wikipedia.org/wiki/Proxy_server) means that the **Edge** instance cannot directly access the internet and all communication to **SENTIENT Cloud** or any other external service is routed through a **proxy server**.

Compare:
* **Without Proxy** (direct connection):

![Without Proxy](/images/edge/config/edge-behind-proxy/without-proxy.webp)

* **With Proxy** (indirect connection):

![With Proxy](/images/edge/config/edge-behind-proxy/with-proxy.webp)

Using a proxy server allows enhancing security by filtering and monitoring internet traffic. In restricted environments, direct internet access is often deliberately blocked, making proxy configurations a necessity for maintaining security protocols. 

Beyond security, proxies can cache resources that can substantially reduce overall network consumption and improve performance for distributed systems like SENTIENT Edge.

### The Installation Guide


<div class="st-tabs">

<div class="st-tab" data-label="Debian-based installation">

#### Prerequisites

* Have a proxy server (**HTTP** or **HTTPS**) with its address, port, and credentials (if required).
* Consider the addresses that should bypass the proxy (e.g., internal resources).
* Have **Java 17** installed.
* **SENTIENT Edge** is installed and running.

#### Step 1. Modify Configuration File

To configure **SENTIENT Edge** behind proxy running on debian-based installation (e.g., Ubuntu), modify the **tb-edge.conf** file:

```bash
sudo tee -a /etc/tb-edge/conf/tb-edge.conf > /dev/null <<EOL
#Enable the proxy
export CLOUD_RPC_PROXY_ENABLED=true

#Set the proxy server host and port
export CLOUD_RPC_PROXY_HOST="proxy_host"
export CLOUD_RPC_PROXY_PORT="proxy_port"
EOL
```


* Replace _proxy_host_ and _proxy_port_ with your proxy's hostname and port.
* If there are hosts that should bypass the proxy (e.g., local network addresses), set <non_proxy_hosts> using a format like: localhost|127.0.0.1|yourdomain.com

##### Configure Authentication (If Required)

If your proxy requires authentication, add the following parameters:

```bash
#(Optional) Add authentication if required
export CLOUD_RPC_PROXY_USERNAME="proxy_username"
export CLOUD_RPC_PROXY_PASSWORD="proxy_password"
```


* Replace _proxy_user_ and _proxy_password_ with your actual credentials.

##### Verify the Changes (Optional)

To verify the changes, run the following command:

```bash
cat /etc/tb-edge/conf/tb-edge.conf
```


#### Step 2. Restart SENTIENT Edge

For the changes to take effect, restart the service after modifying the **tb-edge.conf** file:

```bash
sudo service tb-edge restart
```


Once the **Edge** service is started, open the **Edge UI** at [http://localhost:8080](http://localhost:8080). Use the **tenant credentials** to log in.


<div class="st-callout info">


If the Edge HTTP bind port was changed to **18080** during Edge installation, access the **SENTIENT Edge** instance at [http://localhost:18080](http://localhost:18080).


</div>


#### Troubleshooting

**SENTIENT Edge** logs stored in the following directory:

```bash
/var/log/tb-edge
```
To check if there are any errors on the service side:

```bash
cat /var/log/tb-edge/tb-edge.log | grep ERROR
```


Check connectivity:

```bash
curl -x http://proxy_host:proxy_port https://your_tb_cloud_url
```


* Replace _proxy_host_ and _proxy_port_ with your proxy's hostname and port.

Confirm that the service can reach the proxy server:

```bash
ping proxy_host
traceroute proxy_host
```


* Replace _proxy_host_ with your proxy's hostname.

### Next Steps


</div>

<div class="st-tab" data-label="Docker-based installation">

#### Prerequisites

* Have a proxy server (**HTTP** or **HTTPS**) with its address, port, and credentials (if required).
* Have **SENTIENT Edge** installed and running, and **SENTIENT Cloud** accessible.
* Have [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.


<div class="st-callout info">


To proceed with proxy configuration, set the terminal in the directory which contains the **docker-compose.yml** file.


</div>


#### Step 1. Stop Docker Container

Stop the currently running **TB Edge** container (if it’s still running):

```bash
docker compose stop
```


#### Step 2. Modify the .yml File

Update the **docker-compose.yml** file with the proxy settings. 

To open the file, use: 
```bash
sudo nano docker-compose.yml
```


Enter the following lines into the "environment" block within the file:
```yml
      HTTP_PROXY: http://proxy_user:proxy_password@<proxy_host:proxy_port
      HTTPS_PROXY: http://proxy_user:proxy_password@<proxy_host:proxy_port
      NO_PROXY: localhost,127.0.0.1,postgres,PUT_YOUR_CLOUD_IP
```

* Specify the proxy server for **HTTP** and **HTTPS** connections in the **HTTP_PROXY** and **HTTPS_PROXY** lines, correspondingly 
  * _For example: HTTP_PROXY=http://user:password@proxy.example.com:8080_
* List addresses that should bypass the proxy in the **NO_PROXY** line 
  * _For example: NO_PROXY=localhost,127.0.0.1,postgres,sentient.cloud_

The expected result:


<div class="st-gallery"><figure><img src="/images/edge/config/edge-behind-proxy/docker-with-proxy.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### Step 3 Restart the Containers

To start this docker compose, run the following command:

```bash
docker compose up -d && docker compose logs -f mytbedge
```


Once the **Edge** service is started, open the **Edge UI** at [http://localhost:8080](http://localhost:8080). Use the **tenant credentials** to log in.


<div class="st-callout info">


If the Edge HTTP bind port was changed to **18080** during Edge installation, access the **SENTIENT Edge** instance at [http://localhost:18080](http://localhost:18080).


</div>


#### Troubleshooting

Confirm that the proxy environment variables are correctly set in the **docker-compose.yml** file:

```bash
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```


If the variables are not set, check if they are correctly applied in the container:

```bash
docker exec -it container_name printenv | grep -i proxy
```

If missing, ensure that they are properly defined in **docker-compose.yml**.

Once the container is running, verify if it can access the internet via the proxy:

```bash
docker exec -it container_name curl -I https://google.com
```


If the request fails, it may indicate incorrect proxy settings or connectivity issues.

Check Docker container logs for any additional proxy-related errors:

```bash
docker logs container_name
```


Check connectivity:

```bash
curl -x http://proxy_host:proxy_port https://your_tb_cloud_url
```


### Next Steps


</div>

</div>
