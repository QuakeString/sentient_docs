---
layout: docwithnav-sentient-analytics
assignees:
- vparomskiy
title: SENTIENT ANALYTICS post-installation steps
description: SENTIENT ANALYTICS post-installation steps description
---

* TOC
{:toc}

To make SENTIENT ANALYTICS ready for use, complete the following post-installation setup steps.

## Signing Key

You can read more about signing key [here](/docs/sentient-analytics/settings#signing-key)

### Acquiring Signing Key

Follow these steps to configure the signing key:

1. **Log in to SENTIENT as a System Administrator**  

    ![Login](/images/sentient-analytics/signing-key-4.png)

2. Go to **Security → General**  

   ![Security General Page](/images/sentient-analytics/signing-key-5.png)

3. Scroll to the **JWT Security Settings** section  

   ![JWT Security](/images/sentient-analytics/signing-key-6.png)

4. Copy the value from the **Signing key** field.

### Installation-specific Instructions

**Ubuntu Installation**

1. SSH into the server running SENTIENT ANALYTICS.

2. Open the SENTIENT ANALYTICS configuration file:

   ```bash
   sudo nano /etc/sentient-analytics/conf/sentient-analytics.conf
   ```
   {: .copy-code}

3. Add the signing key to the end of the file:

   ```bash
   export JWT_TOKEN_SIGNING_KEY=<signing-key>
   ```
   {: .copy-code}
   ![Ubuntu Signing Key](/images/sentient-analytics/signing-key-7.png)

4. Save the file and restart the SENTIENT ANALYTICS service.

**Docker Compose Installation**

1. Open your `docker-compose.yml` file.

2. Add a new environment variable under the SENTIENT ANALYTICS service:

   ```yaml
   environment:
     - JWT_TOKEN_SIGNING_KEY=<signing-key>
   ```
   {: .copy-code}
   ![Docker Signing Key](/images/sentient-analytics/signing-key-8.png)

3. Save the file and restart the SENTIENT ANALYTICS container.

### Verifying Successful Installation

To validate that the signing key was installed correctly, you need to:

1. Log in as a **Tenant Administrator**.
2. Go to the **Settings**.

   ![Settings Navigation](/images/sentient-analytics/signing-key-1.png)

3. If everything was done correctly, you will see **Active** status in the **Signing Key** field.  

   ![Signing Key Valid](/images/sentient-analytics/signing-key-3.png)

   
## Required Actions in SENTIENT ANALYTICS Settings

**Note:** These actions affect SENTIENT.

You need to complete the following actions to add all necessary add-ons to SENTIENT:

- **SENTIENT ANALYTICS Widget Bundle:**
    - Click the **Upload bundle** button.
    - You will see *Latest version installed* afterward.
    - Read more about the SENTIENT ANALYTICS Widget Bundle [here](/docs/sentient-analytics/settings#sentient-analytics-widget-bundle).

- **SENTIENT ANALYTICS JS Summary Module:**
    - Click the **Upload module** button.
    - You will see *Latest version installed* afterward.
    - Read more about the SENTIENT ANALYTICS JS Summary Module [here](/docs/sentient-analytics/settings#sentient-analytics-js-summary-module).

## Link to SENTIENT

To simplify the process of adding SENTIENT ANALYTICS views to SENTIENT dashboards, we have introduced the ability to open the dashboard where the view was added in a new tab. 
Configure the link to your SENTIENT instance in Settings to use this feature. Follow these steps:
* Log in to SENTIENT ANALYTICS and navigate to the Settings page.

  ![image](/images/sentient-analytics/signing-key-1.png)

* Enter the URL of your SENTIENT instance (e.g., *https://your-link-to-platform*) in the designated field.

  ![image](/images/sentient-analytics/link-to-tb.png)

After this, you can open your modified or newly created dashboard in a new tab by enabling the Open dashboard in a separate window field.

![image](/images/sentient-analytics/open-dashboard-in-separate-tab.png)
