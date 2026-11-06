+++
title = "IoT Gateway Upgrade Instructions"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/install/upgrade-instructions.md"
+++
<div class="st-tabs">

<div class="st-tab" data-label="Ubuntu Server/Raspberry PI">

### Step 1. Download the `.deb` file

Download installation `.deb` package.

```bash
wget https://github.com/sentient/sentient-gateway/releases/latest/download/python3-sentient-gateway.deb
````


### Step 2. Install the new `.deb` file

Run the following command in the terminal to install the updated package:

```bash
sudo apt install ./python3-sentient-gateway.deb -y
```


<div class="st-callout info">


This will automatically upgrade your existing Gateway installation without removing your configuration and 
extension files **(from Gateway version 3.7.6)**.


</div>


### Step 3. Restart the Gateway

After the upgrade, restart the Gateway service to apply the changes:

```bash
sudo systemctl restart sentient-gateway
```


### Step 4. Verify the Upgrade

To ensure the upgrade was successful, check the Gateway status and logs by running:

```bash
sudo systemctl status sentient-gateway
```


### Configuration File Preservation

During the upgrade, **all user configuration files will be preserved.** This includes customizations made to:
- Connector configuration files.
- Custom user extensions.
- `tb_gateway.json` file.

The upgrade process also automatically creates a backup of your current configuration directory to ensure 
recoverability in case of any issues. The backups are stored under the following paths:

- For connector configurations:
  ```
  /etc/sentient-gateway/configs_backup.tar.gz
  ```

- For user extensions:
  ```
  /var/lib/sentient_gateway/extensions_backup.tar.gz
  ```

### Notes

- This upgrade procedure applies only to .deb package-based installations. If you are using Docker or pip-based 
  installations, please refer to the appropriate guide that you can find on the top of this page.
- Always test the Gateway after the upgrade to ensure connectors and extensions operate as expected.


</div>

<div class="st-tab" data-label="AlmaLinux/RHEL Server">

### Step 1. Download the `.rpm` file

Download installation `.rpm` package.

```bash
wget https://github.com/sentient/sentient-gateway/releases/latest/download/python3-sentient-gateway.rpm
````


### Step 2. Install the new `.rpm` file

Run the following command in the terminal to install the updated package:

```bash
sudo dnf install -y ./python3-sentient-gateway.rpm
```


<div class="st-callout info">


This will automatically upgrade your existing Gateway installation without removing your configuration and 
extension files **(from Gateway version 3.7.6)**.


</div>


<div class="st-callout warn">


If you are upgrading from a gateway version lower than 3.7.6, make backups of your configuration and extension files.


</div>


### Step 3. Restart the Gateway

After the upgrade, restart the Gateway service to apply the changes:

```bash
sudo systemctl restart sentient-gateway
```


### Step 4. Verify the Upgrade

To ensure the upgrade was successful, check the Gateway status and logs by running:

```bash
sudo systemctl status sentient-gateway
```


### Configuration File Preservation

During the upgrade, **all user configuration files will be preserved.** This includes customizations made to:
- Connector configuration files.
- Custom user extensions.
- `tb_gateway.json` file.

The upgrade process also automatically creates a backup of your current configuration directory to ensure 
recoverability in case of any issues. The backups are stored under the following paths:

- For connector configurations:
  ```
  /etc/sentient-gateway/configs_backup.tar.gz
  ```

- For user extensions:
  ```
  /var/lib/sentient_gateway/extensions_backup.tar.gz
  ```

### Notes

- This upgrade procedure applies only to .rpm package-based installations. If you are using Docker or pip-based 
  installations, please refer to the appropriate guide that you can find on the top of this page.
- Always test the Gateway after the upgrade to ensure connectors and extensions operate as expected.


</div>

<div class="st-tab" data-label="Docker (Linux/Mac OS/Windows)">

### Step 1. Stop and Remove Existing Containers

First, stop the currently running Gateway containers:

```bash
docker compose down
```


This will gracefully shut down the gateway and remove the containers, without deleting any volumes or configuration data.

### Step 2. Pull the Latest Gateway Image

Fetch the latest version of the SENTIENT IoT Gateway Docker image:

```bash
docker pull sentient/tb-gateway
```


### Step 3. Start the Updated Gateway

Recreate and start the containers with the updated image:

```bash
docker compose up -d
```


The `-d` flag runs the containers in detached mode.

### Step 4. Verify the Upgrade

To ensure the upgrade was successful, check the Gateway logs by running:

```bash
docker compose logs -f
```


This will display the logs in real-time, allowing you to confirm that the Gateway is running correctly with the new version.

### Notes

- This method is compatible with any version of the Gateway as long as your `docker-compose.yml` and volume mappings are correctly configured.
- To automate future upgrades, consider version pinning or tagging in your Compose file and keeping track of official image changelogs.

</div>

<div class="st-tab" data-label="Python (pip)">

### Step 1. Stop the Gateway

If the Gateway is running as a background service or a systemd service, stop it first:

```bash
sudo systemctl stop sentient-gateway
```


Or if you are running it manually in a terminal, stop it using `Ctrl + C`.

### Step 2. Upgrade the SENTIENT IoT Gateway Package via pip

Run the following command in your Python environment:

```bash
pip install --upgrade sentient-gateway
```


<div class="st-callout info">


You may need to use pip3 or python3 -m pip depending on your environment. Add `--user` if it's a user-level installation.


</div>


### Step 3. Restart the Gateway

Once the upgrade completes, start the Gateway again:

```bash
sudo systemctl start sentient-gateway
```


Or, if you run it manually:

```bash
sentient-gateway
```


### Notes

- If running in a virtual environment, ensure the `pip install` and service control commands are executed within that environment.
- If you installed Gateway via systemd service, the service file may need to point to the correct environment or executable path.


</div>

</div>
