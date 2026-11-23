+++
title = "Microsoft Teams"
description = "Send SENTIENT notifications and rule chain messages to Microsoft Teams channels through a webhook."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
> **From the release after 4.3.0.57.** In 4.3.0.57, Teams messages are not delivered. Until you update, send alarms by [email, SMS, Telegram or WhatsApp](/docs/user-guide/notification-channels/), or email them to the channel (the channel's **⋯** menu › **Get email address**).

SENTIENT posts to a Teams channel through the channel's **webhook URL**. Nothing needs to be set up in SENTIENT's settings.

## 1. Get the channel's webhook URL

In Teams, open the channel's **⋯** menu › **Workflows**, choose **Post to a channel when a webhook request is received**, finish the steps, and copy the URL it shows. An older **Incoming Webhook** connector URL works too.

## 2. Send notifications to Teams

In the [notification center](/docs/user-guide/notifications/):

1. Under **Recipients**, click **+**, choose **Microsoft Teams**, and paste the **Webhook URL**. **Channel name** is for your own reference. Tick **Use deprecated Webhook connectors** only for an Incoming Webhook URL.
2. In a template, tick **Microsoft Teams** and write the message. An **Action button** adds a button with a link, for example to the alarm's dashboard, and **Theme color** sets the card's accent.
3. Use the recipient in a rule, or under **Send notification**.

## From a rule chain

The **Microsoft Teams** rule node posts a card from a rule chain:

| Field | Value |
|---|---|
| **Teams webhook URL** | Required. The channel's Workflows webhook URL, or an older Incoming Webhook URL |
| **Title** | The card's title |
| **Message template** | Required. `${key}` puts in a metadata value, `$[key]` a value from the message data |
| **Button text**, **Button link** | An optional button |
| **Card format** | **Automatic (from the webhook URL)**, **Adaptive Card (Workflows)** or **MessageCard (Incoming Webhook)** |
| **Accent colour** | A hex colour, for MessageCard only |

If Teams refuses the message, the node sends it out on **Failure**, with the reason in the `error` metadata key.

## Related

- [Slack](/docs/user-guide/ui/slack-settings/)
- [Notification center](/docs/user-guide/notifications/)
