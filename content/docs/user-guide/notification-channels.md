+++
title = "Notification channels"
description = "Deliver notifications in SENTIENT, by email, SMS, Telegram, WhatsApp and mobile push: what each channel needs and how users link their accounts."
weight = 82

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **notification** always appears in the bell at the top of SENTIENT. Notification rules can also send it out through other **channels**, so that the right people hear about an alarm when they are not looking at a screen. See [Notification center](/docs/user-guide/notifications/) for the rules themselves.

## Channels

| Channel | Who sets it up | Where the user receives it | Works without internet |
|---|---|---|---|
| **Web** | Always on | The bell in SENTIENT, at once, without reloading the page | Yes |
| **Email** | System administrator, or a tenant with its own server: [Mail server](/docs/user-guide/ui/mail-settings/) | The email address of the user | With a mail server on the plant network |
| **SMS** | System administrator: [SMS provider](/docs/user-guide/ui/sms-provider-settings/) | The phone number in the user's profile | No, unless the SMS service has a server on your network |
| **Telegram** | System administrator, below | The user's linked Telegram account | No |
| **WhatsApp** | System administrator, below | The user's linked WhatsApp number | No |
| **Mobile app** | System administrator, below | A push message on the phone | No |
| **Slack**, **Microsoft Teams** | | From the release after 4.3.0.57, see [Slack](/docs/user-guide/ui/slack-settings/) and [Microsoft Teams](/docs/user-guide/ui/microsoft-teams-settings/) | |

**For an offline plant**, rely on the web channel on control-room screens, and on email through a mail server inside the plant network.

The system administrator sets up SMS, Telegram, WhatsApp and the mobile app under **Settings > Notifications**. Each card has its own **Save** button.

## Telegram

You need a Telegram bot. In Telegram, talk to **@BotFather**, send `/newbot`, and copy the token it gives you.

![Telegram settings: bot token, bot username and how bot updates arrive](/images/st/sysadmin-telegram-settings.webp)

1. In the **Telegram settings** card, switch on **Enable Telegram channel**.
2. Paste the **Bot token**. **Bot username** fills itself in when you save.
3. Under **Receive bot updates via**, keep **Long-polling**. It works behind a firewall, since SENTIENT asks Telegram for new messages. Choose **Webhook** only if Telegram can reach SENTIENT at a public HTTPS address, and enter that **Webhook URL**.
4. Click **Save**, link your own Telegram account (below), then click **Send test message** to receive one.

## WhatsApp

WhatsApp only delivers messages from businesses through an approved provider, and alarm and code messages must use **templates** that WhatsApp has approved. Set them up with your provider first.

1. In the **WhatsApp settings** card, switch on **Enable WhatsApp channel**.
2. Choose the **Provider** and enter its credentials:
   - **Meta Cloud API (official):** **Phone number ID**, **Access token**, the **Alarm template name**, the **Verification template name** (an *Authentication* template with one value, the code) and the **Default template language**.
   - **Twilio:** **Account SID**, **Auth token**, the **WhatsApp-enabled from number**, a **Verify Service SID** for codes, and the **Alarm Content SID** of the approved alarm template.
   - **Gupshup:** **API key**, **App ID** and **App name**.
   - **360dialog:** **API key** and **Template namespace**.
3. Click **Test credentials**, then **Save**.

Switching provider keeps the credentials of the others; only the selected one is used.

## Mobile app push

Push messages to the SENTIENT mobile app go through Google Firebase. In the **Mobile settings** part of the page, upload the **Firebase service account file** (a JSON file from the Firebase console of the app's project) and click **Save**.

## Link a Telegram or WhatsApp account (each user)

SENTIENT can only message users who have linked their account:

![Linked notification accounts on the user's account page, with Link Telegram and Link WhatsApp](/images/st/account-linked-accounts.webp)

1. Click your initials at the bottom of the left menu, choose **Account**, then open the **Notification settings** tab.
2. Under **Linked notification accounts**:
   - **Link Telegram:** click **Open in Telegram** on the phone or computer where Telegram is installed, and press **Send** in the chat that opens. On a computer without Telegram, open the bot yourself and send the command shown. The window closes once the account is linked.
   - **Link WhatsApp:** type your WhatsApp number, click **Send code**, and type the 6-digit code you receive.

**Unlink** removes a linked account. A linked account can also receive [two-factor authentication](/docs/user-guide/two-factor-authentication/) codes.

## Related

- [Notification center](/docs/user-guide/notifications/)
- [Alarm rules](/docs/user-guide/alarm-rules/)
