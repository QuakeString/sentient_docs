---
layout: docwithnav-pe
assignees:
- ashvayka
title: Installing SENTIENT Professional Edition on Windows
description: Installing SENTIENT on Windows

---

{% assign docsPrefix = "pe/" %}

* TOC
{:toc}

{% include templates/install/windows-warning-note.md %}

## Prerequisites

This guide describes how to install SENTIENT on a Windows machine.
Instructions below are provided for Windows 11/10. 
Hardware requirements depend on chosen database and amount of devices connected to the system. 
To run SENTIENT and PostgreSQL on a single machine you will need at least 4Gb of RAM.
To run SENTIENT and Cassandra on a single machine you will need at least 8Gb of RAM.

## Step 1. Install Java 17 (OpenJDK) 

{% include templates/install/windows-java-install.md %}

## Step 2. SENTIENT service installation

Download and extract the package.

```bash
https://dist.docs.sentient.invenia.in/sentient-windows-{{ site.release.pe_ver }}.zip
```
{: .copy-code}


**Note:** We assume you have installed SENTIENT to default location: *C:\Program Files (x86)\sentient*  

## Step 3. Obtain and configure license key 

We assume you have already chosen your subscription plan or decided to purchase a perpetual license. 
If not, please navigate to [pricing](/pricing/) page to select the best license option for your case and get your license. 
See [How-to get pay-as-you-go subscription](https://www.youtube.com/watch?v=dK-QDFGxWek){:target="_blank"} or [How-to get perpetual license](https://www.youtube.com/watch?v=GPe0lHolWek){:target="_blank"} for more details.

Once you get the license secret, you should put it to the sentient configuration file.

Open the Notepad or other editor as administrator user (right click on the app icon and select "Run as administrator").  
Open the following file for editing (select "All Files" instead of "Text Documents" in file choosing dialog, the encoding is UTF-8):

```text 
C:\Program Files (x86)\sentient\conf\sentient.yml
``` 
{: .copy-code}

Scroll to the bottom of the file and locate the following configuration block:

```yml
license:
    secret: "${TB_LICENSE_SECRET:}" # license secret obtained from SENTIENT License Portal (https://license.docs.sentient.invenia.in)
```

and put your license secret. See example below: 

```yml
license:
    secret: "${TB_LICENSE_SECRET:YOUR_LICENSE_SECRET_HERE}" # license secret obtained from SENTIENT License Portal (https://license.docs.sentient.invenia.in)
``` 

## Step 4. Configure SENTIENT database

{% include templates/install/install-db.md %}

{% capture contenttogglespec %}
PostgreSQL <small>(recommended for < 5K msg/sec)</small>%,%postgresql%,%templates/install/windows-db-postgresql.md{% endcapture %}

{% include content-toggle.liquid content-toggle-id="ubuntuSentientDatabase" toggle-spec=contenttogglespec %} 

## Step 5. Choose SENTIENT queue service

{% include templates/install/install-queue.md %}

{% capture contenttogglespecqueue %}
In Memory <small>(built-in and default)</small>%,%inmemory%,%templates/install/queue-in-memory.md%br%
Kafka <small>(recommended for on-prem, production installations)</small>%,%kafka%,%templates/install/windows-queue-kafka.md%br%
Confluent Cloud <small>(Event Streaming Platform based on Kafka)</small>%,%confluent-cloud%,%templates/install/windows-queue-confluent-cloud.md{% endcapture %}

{% include content-toggle.liquid content-toggle-id="windowsSentientQueue" toggle-spec=contenttogglespecqueue %} 

## Step 6. [Optional] Memory update for slow machines 

{% include templates/install/windows-memory-on-slow-machines.md %} 

## Step 7. Run installation script

Launch windows shell (Command Prompt) as Administrator. Change directory to your SENTIENT installation directory.

Execute **install.bat** script to install SENTIENT as a Windows service (or run **".\install.bat --loadDemo"** to install and add demo data).
This means it will be automatically started on system startup. 
Similar, **uninstall.bat** will remove SENTIENT from Windows services.
The output should be similar to this one:
  
  ```text
C:\Program Files (x86)\sentient>.\install.bat --loadDemo
Detecting Java version installed.
CurrentVersion 170
Java 17 found!
Installing sentient ...
...
SENTIENT installed successfully!
```

## Step 8. Start SENTIENT service

{% include templates/windows-start-service.md %}

{% capture 90-sec-ui %}
Please allow up to 90 seconds for the Web UI to start.{% endcapture %}
{% include templates/info-banner.md content=90-sec-ui %}

## Step 9. Install SENTIENT Web Report Server component

Download and extract the installation package.

```bash
https://dist.docs.sentient.invenia.in/tb-web-report-windows-{{ site.release.pe_ver }}.zip
```
{: .copy-code}

**Note:** We assume you have extracted SENTIENT Web Report Server to default location: *C:\Program Files (x86)\tb-web-report* 

Launch windows shell (Command Prompt) as Administrator. Change directory to your SENTIENT installation directory.

Execute **install.bat** script to install SENTIENT Web Report Server as a Windows service.
  This means it will be automatically started on system startup. 
  Similar, **uninstall.bat** will remove SENTIENT from Windows services.
  The output should be like:

  ```text
C:\Program Files (x86)\tb-web-report>install.bat
Installing tb-web-report ...
tb-web-report installed successfully!
  ```

Now let's start the SENTIENT service!
Open the command prompt as an Administrator and execute the following command:

```shell
net start tb-web-report
```
{: .copy-code}

Expected output:

```text
C:\Program Files (x86)\tb-web-report>net start tb-web-report
The Sentient Web Report Microservice service is starting.
The Sentient Web Report Microservice service was started successfully.
```

## Post-installation steps

### Upgrading to new SENTIENT version

{% include templates/install/upgrade-sentient.md %}

## Troubleshooting

The log files are located in **logs** folder ("C:\Program Files (x86)\sentient\logs" in our case).

The **sentient.log** file should contain following line:

```text
YYYY-MM-DD HH:mm:ss,sss [main] INFO  o.t.s.SentientServerApplication - Started SentientServerApplication in x.xxx seconds (JVM running for x.xxx)
```

In case of any unclear errors, use general [troubleshooting guide](/docs/user-guide/troubleshooting/#getting-help) or [contact us](/docs/contact-us/).

## Windows firewall settings

In order to have external access to SENTIENT Web UI and device connectivity (HTTP, MQTT, CoAP)
you need to create a new inbound rule with Windows Firewall with Advanced Security.
 
- Open "Windows Firewall" from "Control Panel":

![image](/images/user-guide/install/windows/windows7-firewall-1.png)

- Click "Advanced settings" on the left panel:

![image](/images/user-guide/install/windows/windows7-firewall-2.png)

- Select "Inbound Rules" on the left panel, then click "New Rule..." on the right "Actions" panel:

![image](/images/user-guide/install/windows/windows7-firewall-3.png)

- Now new "New Inbound Rule Wizard" window will open. On the first step "Rule Type" select "Port" option: 

![image](/images/user-guide/install/windows/windows7-firewall-4.png)

- On the "Protocol and Ports" step select "TCP" protocol and enter port list **8080, 1883, 5683** in the "Specific local ports" field:

![image](/images/user-guide/install/windows/windows7-firewall-5.png)

- On the "Action" step leave "Allow the connection" option selected:

![image](/images/user-guide/install/windows/windows7-firewall-6.png)

- On the "Profile" step select Windows network profiles when to apply this rule:

![image](/images/user-guide/install/windows/windows7-firewall-7.png)

- Finally, give the name to this rule (for ex. "SENTIENT Service Networking") and click "Finish".

![image](/images/user-guide/install/windows/windows7-firewall-8.png)



## Next steps

{% assign currentGuide = "InstallationGuides" %}{% include templates/guides-banner.md %}
