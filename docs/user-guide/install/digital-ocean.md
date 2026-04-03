---
layout: docwithnav
title: Installing SENTIENT on DigitalOcean 
description: Installing SENTIENT on DigitalOcean

---

This guide describes how to install SENTIENT on DigitalOcean. 

* TOC
{:toc}

{% include templates/install/digital-ocean-droplet.md %} 

## Step 4. Use regular installation instruction for Ubuntu

Please navigate to the SENTIENT [**installation instruction**](/docs/user-guide/install/ubuntu/) 
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




