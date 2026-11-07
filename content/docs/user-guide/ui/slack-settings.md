+++
title = "Slack"
description = "Slack notifications in SENTIENT: their state in 4.3.0.57 and what to use meanwhile."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
> **Note for 4.3.0.57:** messages to Slack are not sent yet. The **Slack settings** card under **Settings > Notifications** saves a bot token, and notification rules let you choose Slack, but SENTIENT does not deliver to Slack. The Slack rule node cannot start either. A later version will add it.

Until then, send alarms by [email, SMS, Telegram or WhatsApp](/docs/user-guide/notification-channels/), which all work. If your team must see alarms in Slack, have SENTIENT email them to the channel's email address (in Slack: channel details › **Integrations** › **Send emails to this channel**).

## Related

- [Notification channels](/docs/user-guide/notification-channels/)
- [Microsoft Teams](/docs/user-guide/ui/microsoft-teams-settings/)
