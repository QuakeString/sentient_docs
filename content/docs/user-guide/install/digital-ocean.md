+++
title = "Installing SENTIENT on DigitalOcean"
description = "Installing SENTIENT on DigitalOcean"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/install/digital-ocean.md"
+++
This guide describes how to install SENTIENT on DigitalOcean. 

## Prerequisites

- Active [DigitalOcean](https://cloud.digitalocean.com/) account

## Step 1. Launch Ubuntu 18.04 on DigitalOcean

### Step 1.1 Create DigitalOcean Droplet

- Login to your DigitalOcean account.
- Click the "Droplets" menu item and then the "Create Droplet" button (see image below).   

![image](/images/user-guide/install/digital-ocean-pe/create-droplet.webp)

### Step 1.2 Select your plan

- Once "Create Droplets" page is loaded, select "Ubuntu 18.04 x64" as your image (see image below).
- Choose your plan. For beginners we would like to recommend 2CPUs and 4GB of RAM plan. 

  Note: Advanced SENTIENT users may choose the plan that suites their workload best. 
    
![image](/images/user-guide/install/digital-ocean-pe/choose-plan.webp)

### Step 1.3 Choose Region

- Scroll down to select datacenter region from the available list (see image below).
- [Optional] Enable backups. Although this is optional we highly recommend to do this. 
- [Optional] Add block storage

![image](/images/user-guide/install/digital-ocean-pe/choose-region.webp)

### Step 1.4 Authentication

- Use existing or create new SSH Key that will be used to connect to your instance. Make sure you have access to the SSH Key you have chosen. We will use this key later in the guide to connect to this instance. 
- Put a meaningful hostname
- Add "sentient" tag, just-in-case, we are not going to use it in this instruction.
- Finally, click the "Create Droplet" button.

![image](/images/user-guide/install/digital-ocean-pe/create-final.webp)

- Once droplet is created, copy the IP address of your droplet to a safe place. We will use it later in the guide. 

![image](/images/user-guide/install/digital-ocean-pe/droplet-created.webp)

## Step 2. Configure Firewall Rules

Now we need to configure Firewall rules to allow MQTT, CoAP and HTTP traffic. See images below:

![image](/images/user-guide/install/digital-ocean-pe/create-firewall.webp)

- Give your Firewall a meaningful name;
- Configure HTTP, HTTPS and three custom rules as set on the screen below. 

![image](/images/user-guide/install/digital-ocean-pe/firewall-config.webp)

- Leave outbound rules as-is;
- Select your droplet or tag to assign this firewall;
- Finally click "Create Firewall" button.

![image](/images/user-guide/install/digital-ocean-pe/firewall-final.webp)

## Step 3. Connect to your instance using SSH

Please use the [official guide](https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/) 
and the SSH Key we have created during [Step 1.4](/docs/user-guide/install/pe/digital-ocean/#step-14-authentication).
 

## Step 4. Use regular installation instruction for Ubuntu

Please navigate to the SENTIENT [**installation instruction**](/docs/user-guide/install/ubuntu/) 
for Ubuntu and complete the installation steps.

**Note:** Use your droplet IP address instead of "localhost" to access the instance WEB UI.

## Post-installation steps

### Configure HAProxy to enable HTTPS

You may want to configure HTTPS access using HAProxy. 
This is possible in case you are hosting SENTIENT in the cloud and have a valid DNS name assigned to your instance.
Please follow this [guide](/docs/user-guide/install/pe/add-haproxy-ubuntu) to install HAProxy and generate valid SSL certificate using Let's Encrypt.


### Upgrading to new SENTIENT version

**Keep Your Platform Secure and Up-to-Date**

When a new SENTIENT release becomes available, we provide a streamlined update process to ensure your system benefits from the latest features and security patches without any risk to your data.


<div class="st-callout info">


**To maintain database integrity and system stability, please perform upgrades sequentially (e.g., v4.0.2 → v4.1.0 → v4.2.0).**


</div>


Please refer to our official <a href="/docs/user-guide/install/upgrade-instructions/">Upgrade Instructions</a> for detailed steps tailored to your current deployment environment.


## Troubleshooting

SENTIENT logs are stored in the following directory:
 
```bash
/var/log/sentient
```


You can issue the following command in order to check if there are any errors on the backend side:
 
```bash
cat /var/log/sentient/sentient.log | grep ERROR
```


## Next steps
