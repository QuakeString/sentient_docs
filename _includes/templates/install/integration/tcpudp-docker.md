Execute the following command to pull the image:

```bash
docker pull sentient/tb-pe-tcp-udp-integration:{{ site.release.pe_full_ver }}
```
{: .copy-code}

Execute the following command to create volume for the integration logs (799 is the user id of SENTIENT non-root docker user):

```bash
mkdir -p ~/.tb-pe-tcp-udp-integration-logs && sudo chown -R 799:799 ~/.tb-pe-tcp-udp-integration-logs
```
{: .copy-code}

Execute the following command to run the integration:

```bash
docker run -it -p 10560:10560 -v ~/.tb-pe-tcp-udp-integration-logs:/var/log/tb-tcp-udp-integration  \
-e "RPC_HOST=sentient.cloud" -e "RPC_PORT=9090" \
-e "INTEGRATION_ROUTING_KEY=YOUR_ROUTING_KEY"  -e "INTEGRATION_SECRET=YOUR_SECRET" \
--name my-tb-pe-tcp-udp-integration --restart always sentient/tb-pe-tcp-udp-integration:{{ site.release.pe_full_ver }}
```
{: .copy-code}

Where: 
    
- `sentient.cloud` - is the host name of your SENTIENT Professional Edition instance;
- `9090` - is the port of your SENTIENT Professional Edition instance. It is configured in sentient.yml using INTEGRATIONS_RPC_PORT env variable;    
- `YOUR_ROUTING_KEY` - placeholder for your **integration key** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `YOUR_SECRET` - placeholder for your **integration secret** obtained on [create remote integration in SENTIENT](#create-remote-integration-in-sentient);
- `docker run`              - run this container;
- `-it`                     - attach a terminal session with current SENTIENT process output;
- `-p 10560:10560` - connect local port 10560 to exposed internal 10560 port for the integration. If the exposed port is UDP, add `/udp` at the end, e.g. `-p 11560:11560/udp` 
- `-v ~/.tb-pe-tcp-udp-integration-logs:/var/log/tb-tcp-udp-integration`   - mounts the host's dir `~/.tb-pe-tcp-udp-integration-logs` to SENTIENT logs directory;
- `--name tb-pe-tcp-udp-integration`             - friendly local name of this machine;
- `--restart always`        - automatically start SENTIENT Integration in case of system reboot and restart in case of failure.;
- `sentient/tb-pe-tcp-udp-integration:{{ site.release.pe_full_ver }}`          - docker image.

After executing this command you can open logs which are located here `~/.tb-pe-tcp-udp-integration-logs`. 
You should see some INFO log messages with your latest Integration configuration that arrived from the server.

{% capture difference %}
You can detach from session terminal with **`Ctrl-p`**+**`Ctrl-q`** - the container will keep running in the background.
{% endcapture %}
{% include templates/info-banner.md content=difference %}

- **Reattaching, stop and start commands**

To reattach to the terminal (to see SENTIENT logs) run:

```
docker attach tb-pe-tcp-udp-integration
```
{: .copy-code}

To stop the container:

```
docker stop tb-pe-tcp-udp-integration
```
{: .copy-code}

To start the container:

```
docker start tb-pe-tcp-udp-integration
```
{: .copy-code}