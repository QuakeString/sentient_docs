+++
title = "Slack Settings"
description = "SENTIENT IoT platform Slack settings"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/slack-settings.md"
+++
By integrating Slack with Sentient, users will be able to receive notifications in Slack of events occurring in the Sentient system according to the notification rules you set. For example, to notify about device status or detected issues.


<div class="st-callout info">


**Note:**
<br>
You can send Slack notifications to users from your workspace only


</div>


Tenant administrator is able to setup to distribute alarms produced by [**rule engine**](/docs/user-guide/rule-engine-2-0/re-getting-started/).

## Create an application in Slack. Get Slack API token

To configure Slack settings in Sentient, first register an application in Slack API. To do this, open [get Slack API token](https://api.slack.com/tutorials/tracks/getting-a-token) page. Next, follow these steps:


1. In "How to quickly get and use a Slack API token" page, scroll below and find "Create a pre-configured app";

1. Click "Create app" button;

1. In a new window, select your workspase from drop-down menu, then click "Next";

1. Review summary and click "Create" button to create your app;

1. Welcome to your app`s configurations. Click "Go it";

1. Next step - install your app to your Slack workspace. Click "Install to Workspace" button;

1. App is requesting permission to access your Slack workspace. Click "Allow";

1. Success! Your app is created. Now, navigate to "OAuth & Permissions" page;

1. Copy "Bot User OAuth Token". This is the "Slack API token" we need.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/slack/create-slack-api-token-1.webp" alt="In &quot;How to quickly get and use a Slack API token&quot; page, scroll below and find &quot;Create a pre-configured app&quot;;" loading="lazy"><figcaption>In "How to quickly get and use a Slack API token" page, scroll below and find "Create a pre-configured app";</figcaption></figure><figure><img src="/images/user-guide/ui/slack/create-slack-api-token-2.webp" alt="Click &quot;Create app&quot; button;" loading="lazy"><figcaption>Click "Create app" button;</figcaption></figure><figure><img src="/images/user-guide/ui/slack/create-slack-api-token-3.webp" alt="In a new window, select your workspase from drop-down menu, then click &quot;Next&quot;;" loading="lazy"><figcaption>In a new window, select your workspase from drop-down menu, then click "Next";</figcaption></figure><figure><img src="/images/user-guide/ui/slack/create-slack-api-token-4.webp" alt="Review summary and click &quot;Create&quot; button to create your app;" loading="lazy"><figcaption>Review summary and click "Create" button to create your app;</figcaption></figure><figure><img src="/images/user-guide/ui/slack/create-slack-api-token-5.webp" alt="Welcome to your app`s configurations. Click &quot;Go it&quot;;" loading="lazy"><figcaption>Welcome to your app`s configurations. Click "Go it";</figcaption></figure><figure><img src="/images/user-guide/ui/slack/create-slack-api-token-6.webp" alt="Next step - install your app to your Slack workspace. Click &quot;Install to Workspace&quot; button;" loading="lazy"><figcaption>Next step - install your app to your Slack workspace. Click "Install to Workspace" button;</figcaption></figure><figure><img src="/images/user-guide/ui/slack/create-slack-api-token-7.webp" alt="App is requesting permission to access your Slack workspace. Click &quot;Allow&quot;;" loading="lazy"><figcaption>App is requesting permission to access your Slack workspace. Click "Allow";</figcaption></figure><figure><img src="/images/user-guide/ui/slack/create-slack-api-token-8.webp" alt="Success! Your app is created. Now, navigate to &quot;OAuth & Permissions&quot; page;" loading="lazy"><figcaption>Success! Your app is created. Now, navigate to "OAuth & Permissions" page;</figcaption></figure><figure><img src="/images/user-guide/ui/slack/create-slack-api-token-9.webp" alt="Copy &quot;Bot User OAuth Token&quot;. This is the &quot;Slack API token&quot; we need." loading="lazy"><figcaption>Copy "Bot User OAuth Token". This is the "Slack API token" we need.</figcaption></figure></div>


## Slack settings configuration as System administrator

Login to your SENTIENT UI as a system administrator. Navigate to "Settings" page, "Notification" tab. In "Slack settings" window paste copied Slack API token to "Slack api token" row and click "Save".


<div class="st-gallery"><figure><img src="/images/user-guide/ui/slack/add-slack-api-token-sysadmin-1-ce.webp" alt="Login to your SENTIENT UI as a system administrator. Navigate to &quot;Settings&quot; page, &quot;Notification&quot; tab. In &quot;Slack settings&quot; window paste copied Slack API token to &quot;Slack api token&quot; row and click &quot;Save&quot;." loading="lazy"><figcaption>Login to your SENTIENT UI as a system administrator. Navigate to "Settings" page, "Notification" tab. In "Slack settings" window paste copied Slack API token to "Slack api token" row and click "Save".</figcaption></figure></div>


## Slack settings configuration as Tenant administrator

Login to your SENTIENT UI as a tenant administrator. Navigate to "Settings" page, "Notification" tab. In "Slack settings" window paste copied Slack API token to "Slack api token" row and click "Save".


<div class="st-gallery"><figure><img src="/images/user-guide/ui/slack/add-slack-api-token-tenant-admin-1-ce.webp" alt="Login to your SENTIENT UI as a tenant administrator. Navigate to &quot;Settings&quot; page, &quot;Notification&quot; tab. In &quot;Slack settings&quot; window paste copied Slack API token to &quot;Slack api token&quot; row and click &quot;Save&quot;." loading="lazy"><figcaption>Login to your SENTIENT UI as a tenant administrator. Navigate to "Settings" page, "Notification" tab. In "Slack settings" window paste copied Slack API token to "Slack api token" row and click "Save".</figcaption></figure></div>


<br>
Once you have configured your notifications, you will start receiving notifications in your Slack channel whenever an event is triggered in your Sentient instance according to the notification rules you set. You will also be able to send messages to any of your users.
