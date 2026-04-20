Set the terminal in the directory which contains the "docker-compose.yml" file, and run the following command to stop and remove the currently running TB Edge container (if it's still running):
```
docker compose stop mytbedge
```
{: .copy-code}

Modify the main docker compose file (docker-compose.yml) for **SENTIENT Edge** and update the image version:

```text
sed -i 's|sentient/tb-edge-pe:{{previousVersion}}|sentient/tb-edge-pe:{{versionName}}|' docker-compose.yml
```
{: .copy-code}

{% include templates/edge/install/info-patch-upgrade.md %}

Start the docker compose:
```bash
docker compose up -d && docker compose logs -f mytbedge
```
{: .copy-code}

