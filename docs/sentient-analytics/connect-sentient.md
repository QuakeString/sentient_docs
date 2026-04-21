---
layout: docwithnav-sentient-analytics
assignees:
- vparomskiy
title: Connect SENTIENT ANALYTICS to the SENTIENT
description: Connect SENTIENT ANALYTICS platform to the SENTIENT
---

* TOC
{:toc}

## SENTIENT ANALYTICS with SENTIENT 4.2.1 or Older

This guide explains how to connect SENTIENT ANALYTICS with SENTIENT 4.2.1 or older. We strongly recommend updating SENTIENT
to the latest version to access all SENTIENT ANALYTICS and SENTIENT features.

To install SENTIENT ANALYTICS for SENTIENT 4.2.1 or older:

1. Start from step 1 of the installation guide.
2. Before the `Start SENTIENT ANALYTICS service` step, configure `SENTIENT_ANALYTICS_LICENSE_SECRET` and `TB_API_URL`.
3. Complete all other steps, except for `Sync SENTIENT With SENTIENT ANALYTICS`.
4. Perform [post-installation steps](/docs/sentient-analytics/post-installation-steps).

### Configure License Secret

To interact with SENTIENT 4.2.1 or older, you need a SENTIENT ANALYTICS license secret key. If you do not have one, obtain it from the [SENTIENT support team](/docs/contact-us).

Edit the SENTIENT ANALYTICS configuration file:

```bash
sudo nano /etc/sentient-analytics/conf/sentient-analytics.conf
```

Add the following line and replace `YOUR_LICENSE_SECRET_HERE` with your license key:

```bash
export SENTIENT_ANALYTICS_LICENSE_SECRET=YOUR_LICENSE_SECRET_HERE
```

For Docker installations, update the `SENTIENT_ANALYTICS_LICENSE_SECRET` environment variable with the correct value.

### Configure TB_API_URL

By default, SENTIENT ANALYTICS assumes SENTIENT is hosted on the same instance and accessible at:

```
http://localhost:9090
```

If SENTIENT is hosted on a different instance or port, update the configuration accordingly:

```bash
sudo nano /usr/share/sentient-analytics/conf/sentient-analytics.conf
```

Set the correct URL:

```yml
export TB_API_URL=http://localhost:9090
```

For Docker installations, update the `TB_API_URL` environment variable with the correct value.


## Next Steps

{% assign currentGuide = "InstallationOptions" %}{% include templates/trndz-guides-banner.md %}
