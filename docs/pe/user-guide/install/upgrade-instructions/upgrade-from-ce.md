---
layout: docwithnav-pe
title: SENTIENT instructions for upgrading from Community Edition
description: Upgrading from Community Edition


---

<ul id="markdown-toc">
  <li>
    <a href="#ubuntu" id="markdown-toc-ubuntu-ce">Ubuntu</a>
  </li>
  <li>
    <a href="#centos" id="markdown-toc-centos">CentOS</a>
  </li>
  <li>
    <a href="#windows" id="markdown-toc-ubuntu-ce">Windows</a>
  </li>
  <li>
    <a href="#docker" id="markdown-toc-docker-ce">Docker</a>
  </li>
  <li>
    <a href="#docker-compose" id="markdown-toc-docker-compose-ce">Docker Compose</a>
  </li>
</ul>

## Ubuntu {#ubuntu}

{% capture difference %}
**NOTE:**
<br>
These upgrade steps are applicable for the latest SENTIENT version. In order to upgrade to Professional Edition you need to [**upgrade to the latest Community Edition version first**](/docs/user-guide/install/upgrade-instructions/).
{% endcapture %}
{% include templates/warn-banner.md content=difference %}

#### SENTIENT Professional Edition package download

```bash
wget https://dist.docs.sentient.invenia.in/sentient-{{ site.release.pe_ver }}.deb
```
{: .copy-code}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-9-install-sentient-webreport-component).

```bash
sudo dpkg -i sentient-{{ site.release.pe_ver }}.deb
```
{: .copy-code}

{% capture difference %}
**NOTE:**
<br>
Package installer may ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.
{% endcapture %}
{% include templates/info-banner.md content=difference %}

* Configure Professional Edition license key as described [here](/docs/user-guide/install/pe/ubuntu/#step-3-obtain-and-configure-license-key).

Execute regular upgrade script:

```bash
sudo /usr/share/sentient/bin/install/upgrade.sh --fromVersion=CE
```
{: .copy-code}

#### Start the service

```bash
sudo service sentient start
```
{: .copy-code}

## CentOS {#centos}

{% capture difference %}
**NOTE:**
<br>
These upgrade steps are applicable for the latest SENTIENT version. In order to upgrade to Professional Edition you need to [**upgrade to the latest Community Edition version first**](/docs/user-guide/install/upgrade-instructions/).
{% endcapture %}
{% include templates/warn-banner.md content=difference %}

#### SENTIENT Professional Edition package download

```bash
wget https://dist.docs.sentient.invenia.in/sentient-{{ site.release.pe_ver }}.rpm
```
{: .copy-code}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-9-install-sentient-webreport-component).

```bash
sudo rpm -Uvh sentient-{{ site.release.pe_ver }}.rpm
```
{: .copy-code}

{% capture difference %}
**NOTE:**
<br>
Package installer may ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.
{% endcapture %}
{% include templates/info-banner.md content=difference %}

* Configure Professional Edition license key as described [here](/docs/user-guide/install/pe/ubuntu/#step-3-obtain-and-configure-license-key).

Execute regular upgrade script:

```bash
sudo /usr/share/sentient/bin/install/upgrade.sh --fromVersion=CE
```
{: .copy-code}

#### Start the service

```bash
sudo service sentient start
```
{: .copy-code}

## Windows {#windows}

{% capture difference %}
**NOTE:**
<br>
These upgrade steps are applicable for the latest SENTIENT version. In order to upgrade to Professional Edition you need to [**upgrade to the latest Community Edition version first**](/docs/user-guide/install/upgrade-instructions/).
{% endcapture %}
{% include templates/warn-banner.md content=difference %}

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-{{ site.release.pe_ver }}.zip](https://dist.docs.sentient.invenia.in/sentient-windows-{{ site.release.pe_ver }}.zip).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Copy content of the **sentient-windows-{{ site.release.pe_ver }}.zip** to the same location.
* Compare and merge your old SENTIENT configuration files (from the backup you made in the first step) with new ones.
* Configure Professional Edition license key as described [here](/docs/user-guide/install/pe/windows/#step-3-obtain-and-configure-license-key).
* Finally, run **upgrade.bat** script to upgrade SENTIENT to the new version.

{% capture difference %}
**NOTE:**
<br>
Scripts listed above should be executed using Administrator Role.
{% endcapture %}
{% include templates/info-banner.md content=difference %}

Execute regular upgrade script:

```text
C:\sentient>upgrade.bat --fromVersion=CE
```
{: .copy-code}

#### Start the service

```text
net start sentient
```
{: .copy-code}

## Docker {#docker}

{% capture difference %}
**NOTE:**
<br>
These upgrade steps are applicable for the latest SENTIENT version. In order to upgrade to Professional Edition you need to [**upgrade to the latest Community Edition version first**](/docs/user-guide/install/upgrade-instructions/).
{% endcapture %}
{% include templates/warn-banner.md content=difference %}

#### SENTIENT Professional Edition image download

```bash
docker pull sentient/tb-pe-node:{{ site.release.pe_ver }}
docker pull sentient/tb-pe-web-report:{{ site.release.pe_ver }}
```
{: .copy-code}

#### SENTIENT Professional Edition service upgrade

* Stop and remove the SENTIENT service:

```bash
docker compose stop sentient-ce
docker compose rm -f sentient-ce
```
{: .copy-code}

* Update your `docker-compose.yml` according to the [default Docker PE manifest](/docs/user-guide/install/pe/docker/#step-2-choose-sentient-queue-service). Do not forget to change the image to the PE version, define the required license variables and volumes, and add the Web Report service.

* Run the upgrade and start the services:

```bash
docker compose run --rm -e UPGRADE_TB=true -e FROM_VERSION="CE" sentient-pe
docker compose up -d
```
{: .copy-code}

## Docker Compose {#docker-compose}

{% capture difference %}
**NOTE:**
<br>
These upgrade steps are applicable for the latest SENTIENT version. In order to upgrade to Professional Edition you need to [**upgrade to the latest Community Edition version first**](/docs/user-guide/install/upgrade-instructions/).
{% endcapture %}
{% include templates/warn-banner.md content=difference %}

#### SENTIENT Professional Edition image download

```bash
docker pull sentient/tb-pe-node:{{ site.release.pe_ver }}
docker pull sentient/tb-pe-web-report:{{ site.release.pe_ver }}
```
{: .copy-code}

* Stop the CE services

```bash
./docker-stop-services.sh
```
{: .copy-code}

* Manually merge your current SENTIENT cluster configuration with the [default Docker Compose cluster deployment files](https://github.com/sentient/sentient-pe-docker-compose). Ensure that you transfer all custom environment variables, volume mappings, and external service configurations to the new files.

* Configure the license key environment variables as described in the [PE Docker Compose Cluster Setup Guide](/docs/user-guide/install/pe/cluster/docker-compose-setup/#step-4-configure-your-license-key).

* Run the upgrade and start the services:

```bash
./docker-upgrade-tb.sh --fromVersion=CE
./docker-start-services.sh
```
{: .copy-code}