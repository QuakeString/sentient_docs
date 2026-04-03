---
layout: docwithnav-pe
title: Installing SENTIENT Professional Edition on DigitalOcean 
description: Installing SENTIENT Professional Edition on DigitalOcean

---

This guide describes how to install SENTIENT Professional Edition on DigitalOcean. 
Using this guide you will install "Bring Your Own License" version of the product.
Basically, you get the license directly from SENTIENT, Inc, but purchase corresponding server instances and infrastructure from DigitalOcean.       

{% assign docsPrefix = "pe/" %}

* TOC
{:toc}


{% include templates/install/digital-ocean-droplet.md %} 

## Step 4. Use regular installation instruction for Ubuntu

Please navigate to the SENTIENT Professional Edition [**installation instruction**](/docs/user-guide/install/pe/ubuntu/) 
for Ubuntu and complete the installation steps.

**Note:** Use your droplet IP address instead of "localhost" to access the instance WEB UI.

## Post-installation steps

### Configure HAProxy to enable HTTPS

{% include templates/install/ubuntu-haproxy-postinstall.md %}

### Upgrading to new SENTIENT version

{% include templates/install/upgrade-sentient.md %}

## Troubleshooting

{% include templates/install/troubleshooting.md %}

## Next steps

{% assign currentGuide = "InstallationGuides" %}{% include templates/guides-banner.md %}




