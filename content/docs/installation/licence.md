+++
title = "Activate your licence"
description = "Activate a SENTIENT licence key, check what it allows and keep it valid."
weight = 12

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A new SENTIENT installation does nothing useful until a licence is active. The system administrator can always sign in and open the licence page. Every other request is refused with error code 50 (*No active license*) until a licence is active.

![The License Management page of an installation without a licence](/images/st/sysadmin-licence.webp)

## Get a key

Licence keys look like `INVE-<TYPE>-XXXX-XXXX-…`. You get one in one of these ways:

- **Demo licence:** on the licence page, click **Request demo license**. The licence portal opens, and you receive a free 30-day key by email.
- **Buy a licence:** click **Buy license**, or contact your SENTIENT supplier.
- **Key file:** your supplier may send a `.key` file instead of the text key.

## Activate

1. Sign in as the system administrator.
2. Open **License** in the menu.
3. Paste the key into **License Key** and click **Activate**. If you have a key file, click **Import Key File** instead.

When activation succeeds, the page shows the licence type, who it is licensed to, the expiry date, and every limit next to your current use. The limits cover tenants, users, devices, assets, dashboards, report templates, report schedules, rule chains and integrations.

<div class="st-callout info">

**Activation needs internet access once.** SENTIENT confirms the key with the licence server (`https://license.invenia.in`) and binds the key to this machine. After that, SENTIENT runs without internet access. Plants that are always offline can activate from a laptop connection or through a proxy, then disconnect.

</div>

## What happens after activation

- **Hardware binding.** The key is bound to this machine's hardware fingerprint, which is made of six signals: machine ID, board UUID, board serial, disk serials, network card addresses and CPU. Replacing one part is fine, but moving the installation to other hardware is not. See [Move to a new server](/docs/operations/move-server/).
- **Heartbeat.** About once an hour, SENTIENT reports to the licence server and picks up any change your supplier made to the licence, such as new limits or a new expiry date. A heartbeat that cannot reach the server is only logged and never stops the system.
- **Daily check.** Once a day, SENTIENT checks the licence again on this machine.

## Limits and the grace period

You can go over a limit, for example with more devices than the licence allows. The system keeps working, but a countdown starts:

| Days over the limit | What users see |
|---|---|
| 0 to 7 | A warning: *Your system exceeds the current license limits.* |
| 7 to 15 | A critical warning: *The system will stop working soon if a valid license is not acquired.* |
| After 15 days | **System Blocked.** Nobody can create or change anything. The system administrator can still view, delete entities to get back under the limit, or install a new licence. |

Your licence can set different numbers of days. When you get back under the limits or install a larger licence, the warnings clear.

## Renew or replace a licence

Activate the new key on the same page. It replaces the old one.

To move a licence to another machine, first click **Deactivate** on the old machine. This releases the binding on the licence server, so you can activate the same key on the new machine. If the old machine is gone, ask your supplier to release the binding.

**Force-delete local license** removes the licence from this machine only, without contacting the licence server. The binding stays taken until your supplier releases it, so use it only when **Deactivate** cannot reach the server.

## Licence problems

See [Licence errors](/docs/troubleshooting/licence-errors/) for every licence message and its fix.
