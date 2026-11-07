+++
title = "Mail server configuration"
description = "Connect SENTIENT to an SMTP server so it can send activation links, password resets and alarm emails."
aliases = ["/docs/samples/alarms/mail/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT sends email for user activation, password resets, account-lockout warnings, and [notifications](/docs/user-guide/notifications/) such as alarm emails. It needs an SMTP server to send through: your company's mail server, Microsoft 365, Gmail, or a relay on the plant network.

**On an offline plant network** without a mail server, SENTIENT still works: use **Display activation link** and **Set password** for users (see [Users](/docs/user-guide/ui/users/)), and send alarms through other [notification channels](/docs/user-guide/notification-channels/).

The system administrator sets the server under **Settings > Mail server**. A tenant administrator can use the system settings or set the tenant's own server: switch off **Use System Mail Server Settings** on the tenant's mail settings.

## Settings

| Setting | What to enter |
|---|---|
| **Mail From** | The sender address, for example `sentient@yourcompany.com`. Many servers only accept the address of the account you sign in with |
| **SMTP protocol** | `smtp` for most servers |
| **SMTP host** | The mail server, for example `smtp.office365.com` or `smtp.gmail.com` |
| **SMTP port** | `587` for STARTTLS (most common), `465` for implicit TLS, `25` for an unencrypted relay on the local network |
| **Timeout (msec)** | How long to wait for the server. `10000` is a good start |
| **Enable TLS** | On for ports 587 and 465. On port 465 SENTIENT uses implicit TLS, on any other port STARTTLS |
| **TLS version** | Leave empty, or choose `TLSv1.2` or `TLSv1.3` to require at least that version. TLS 1.0 and 1.1 are not supported |
| **Username** / **Password** | The mailbox account. For Gmail and Microsoft 365 with multi-factor sign-in, use an *app password* |
| **Enable proxy** | Sends mail through an HTTP proxy, with its host, port and optional user name and password. Use it when the server reaches the internet only through a proxy |

> **Note for 4.3.0.57:** sign-in to the mail server with OAuth2 (the Microsoft and Google options) is not supported yet. Use a user name and password, or an app password.

Click **Save**, then **Send test mail**. SENTIENT sends a message to your own address. If it fails, the error says why.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| Connection refused or timeout | Wrong host or port, or a firewall blocks outgoing SMTP | Check the host and port; ask IT to allow outgoing port 587 from the SENTIENT server |
| Authentication failed (535) | Wrong user name or password, or the provider blocks password sign-in | Use an app password; check that SMTP sign-in is allowed for the mailbox |
| Sender address rejected | **Mail From** differs from the signed-in account | Use the account's own address, or allow the account to send as that address |
| TLS or certificate error | Port and TLS setting do not match, or the server's TLS is too old | 587 with **Enable TLS** on; 465 with **Enable TLS** on; for an old internal relay, port 25 with TLS off |

## Related

- [Users](/docs/user-guide/ui/users/)
- [Notifications](/docs/user-guide/notifications/)
- [Security settings](/docs/user-guide/ui/security-settings/)
