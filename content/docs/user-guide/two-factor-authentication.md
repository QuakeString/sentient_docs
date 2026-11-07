+++
title = "Two-factor authentication"
description = "Ask for a one-time code after the password: authenticator app, email, SMS, Telegram, WhatsApp or backup codes."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
With two-factor authentication (2FA), signing in needs a password **and** a 6-digit code that only the user can receive. A stolen password alone is then not enough. Use it at least for administrator accounts, and for every account that can be reached from outside the plant network.

Setting it up has two parts: an administrator chooses which kinds of code are allowed, then each user turns on the ones they want in their own profile.

## Methods

| Method | How the user gets the code | Needs |
|---|---|---|
| **Authenticator app** | An app on the phone (Google Authenticator, Microsoft Authenticator, Authy, Duo…) shows a new code every 30 seconds | Nothing on the server; works without internet |
| **Email** | Sent to the user's email address | [Mail server](/docs/user-guide/ui/mail-settings/) |
| **SMS** | Sent by text message | [SMS provider](/docs/user-guide/ui/sms-provider-settings/) |
| **Telegram** | Sent to the user's linked Telegram account | Telegram set up as a [notification channel](/docs/user-guide/notification-channels/) |
| **WhatsApp** | Sent to the user's linked WhatsApp account | WhatsApp set up as a notification channel |
| **Backup code** | Printed one-time codes, for when the phone is not at hand | Nothing |

**For an offline plant**, use the authenticator app: the phone and the server only need the same time, not a connection to each other. Add backup codes in case a phone is lost.

## Allow methods (administrator)

The system administrator opens **Security > Two-factor authentication** in the left menu. A tenant administrator can use the system settings or set the tenant's own (switch off **Use system two factor auth settings**).

1. Under **Available providers**, add each method you allow, and set its options:
   - **Authenticator app:** the **Issuer name** shown in the app, for example `SENTIENT Plant A`.
   - **Email, SMS, Telegram, WhatsApp:** the **Verification message template** and the **Verification code lifetime (sec)**.
   - **Backup code:** the **Number of codes** each user gets.
2. Under **Verification limitations**, set:
   - **Total allowed time for verification (sec)**: how long the user has to enter a code after the password.
   - **Retry verification code period (sec)**: how soon a user may ask for a new code.
   - **Verification code check rate limit**: how many tries are allowed in a period.
   - **Max verification failures before user lockout**: after this many wrong codes, the account is locked.
3. Click **Save**.

## Turn it on (each user)

1. Click your initials at the bottom of the left menu, choose **Account**, then open the **Security** tab.
2. Under **Two-factor authentication**, switch on a method:
   - **Authenticator app:** scan the QR code with the app, then type the 6-digit code the app shows.
   - **Email, SMS, Telegram or WhatsApp:** enter or confirm where the code goes, click **Send code**, and type the code you receive.
   - **Backup code:** SENTIENT shows the codes once. Download or print them and keep them safe; each works once.
3. With several methods on, choose **Use as main two-factor authentication method** on the one SENTIENT should ask for first. At sign-in you can switch to another.

From the next sign-in, SENTIENT asks for a code after the password.

## When a user loses their phone

- The user signs in with a **backup code**, then turns off the old authenticator on the **Security** tab and sets up the new phone.
- **Without backup codes or another method, the user cannot sign in.** SENTIENT 4.3.0.57 has no button for an administrator to remove another user's 2FA. Give every user backup codes, or a second method such as email, when you turn 2FA on.
- From the next SENTIENT release, the user's details have **Reset two-factor authentication** for administrators: it removes all of the user's methods, so they sign in with their password and set 2FA up again.

## Related

- [Security settings](/docs/user-guide/ui/security-settings/)
- [Users](/docs/user-guide/ui/users/)
