+++
title = "Security settings"
description = "Account lockout, link lifetimes, password rules and sign-in token lifetimes."
aliases = ["/docs/user-guide/ui/jwt-security-settings/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
The system administrator sets platform-wide sign-in security under **Settings > Security settings**. The page has three parts: **General policy**, **Password policy** and **JWT security settings**.

## General policy

| Setting | Default | What it does |
|---|---|---|
| **Maximum number of failed login attempts, before account is locked** | 5 | After this many wrong passwords in a row, the account is locked for 5 minutes. It unlocks by itself; the user does not need an administrator |
| **In case user account lockout, send notification to email** | `admin@sentient.local` | Who is told when an account locks. Change it to a mailbox someone reads; it needs working [mail settings](/docs/user-guide/ui/mail-settings/) |
| **User activation link TTL in hours** | 24 | How long a new user's activation link works. See [Users](/docs/user-guide/ui/users/) |
| **Password reset link TTL in hours** | 24 | How long a **Forgot password?** link works |
| **Mobile secret key length** | 32 | Length of the secret used by the mobile app's QR sign-in |

## Password policy

The password policy holds the rules for user passwords: minimum and maximum length, how many uppercase letters, lowercase letters, digits and special characters a password needs, whether spaces are allowed, how many days a password stays valid, and how soon an old password may be reused.

> **Note for 4.3.0.57:** the server does not yet check passwords against these fields. Whatever the policy says, SENTIENT requires a password of **8 to 72 characters** that contains at least **three of**: a lowercase letter, an uppercase letter, a digit, a special character. A password such as `Plant2025` meets it; `plant2025` does not.
>
> The same rule applies when a user activates their account, resets a password, or an administrator uses **Set password**.

**Force to reset password if not valid** is meant to make users whose password breaks the policy set a new one through a reset email. Like the policy fields, it has no effect yet in 4.3.0.57.

## JWT security settings

After sign-in, the browser holds a token instead of the password. These settings control those tokens.

| Setting | Default | What it does |
|---|---|---|
| **Issuer name** | `sentient` | Written into every token |
| **Signing key** | Generated at installation | The secret that signs tokens. Keep it secret. **Generate key** makes a new one |
| **Token expiration time (sec)** | 9000 (2.5 hours) | How long a token is valid before the browser renews it |
| **Refresh token expiration time (sec)** | 604800 (7 days) | How long a user stays signed in without activity. After this, they sign in again |

**Changing the signing key signs everyone out**, including API clients and the mobile app, once the server restarts: the server reads the key when it starts. Do it after a suspected leak, at a quiet time, and restart SENTIENT afterwards.

> **Note for 4.3.0.57:** the server does not yet apply the two expiration fields. Sign-in tokens last 15 minutes and are renewed silently, and a user stays signed in for 7 days without activity, whatever the fields say.

## Recommendations for plants

- Keep the lockout on. Five attempts stop password guessing without bothering operators.
- Use [two-factor authentication](/docs/user-guide/two-factor-authentication/) for administrator accounts that can be reached from outside the plant network.

## Related

- [Users](/docs/user-guide/ui/users/)
- [Two-factor authentication](/docs/user-guide/two-factor-authentication/)
- [API error codes](/docs/troubleshooting/error-codes/)
