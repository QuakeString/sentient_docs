+++
title = "Slack"
description = "Send SENTIENT notifications and rule chain messages to Slack channels and users."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
> **From the release after 4.3.0.57.** In 4.3.0.57, Slack messages are not delivered. Until you update, send alarms by [email, SMS, Telegram or WhatsApp](/docs/user-guide/notification-channels/), or email them to the Slack channel's own address (channel details › **Integrations** › **Send emails to this channel**).

SENTIENT posts to Slack through a Slack app (a bot) in your workspace.

## 1. Make a Slack app

1. At **api.slack.com/apps**, click **Create New App**, **From scratch**, and choose your workspace.
2. Under **OAuth & Permissions**, add the bot scopes `chat:write`, `channels:read`, `groups:read` and `users:read`, then click **Install to Workspace**.
3. Copy the **Bot User OAuth Token** (it starts with `xoxb-`).
4. In each private channel that should receive messages, invite the app: `/invite @<app name>`.

## 2. Save the token in SENTIENT

As the system administrator (for every tenant) or a tenant administrator (for your tenant), open **Settings > Notifications**, paste the token into **Slack settings** › **Slack API token**, and save. The token is shown masked afterwards. Saving again without touching it keeps it.

## 3. Send notifications to Slack

In the [notification center](/docs/user-guide/notifications/):

1. Under **Recipients**, click **+**, choose **Slack**, then the **Slack channel type** (**Public channel**, **Private channel** or **Direct message**) and the **Conversation** from the list.
2. In a template, tick **Slack** and write the Slack message.
3. Use the recipient in a rule, or under **Send notification**.

## From a rule chain

The **Send to Slack** rule node posts a message from a rule chain:

| Field | Value |
|---|---|
| **Message template** | The text. `${key}` puts in a metadata value, `$[key]` a value from the message data |
| Token | **Use system slack settings**, or the node's own **Slack API token** |
| **Slack channel type**, **Conversation** | Where the message goes |

If Slack refuses the message, the node sends it out on **Failure**, with the reason in the `error` metadata key.

## Related

- [Microsoft Teams](/docs/user-guide/ui/microsoft-teams-settings/)
- [Notification center](/docs/user-guide/notifications/)
