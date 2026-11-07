+++
title = "Licence errors"
description = "Licence messages and error codes 50, 51 and 52: what they mean and how to fix them."
weight = 187

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Licence errors appear as a dialog in the web UI or as an API error with an `errorCode`. Find your message below.

## No active license (code 50)

Error ID: [ST-LIC-001](/docs/troubleshooting/errors/st-lic-001/)

```
No active license. Please activate a license to continue.
```

**HTTP 402.** No licence is installed. This is normal right after installation, and it also happens after a licence is deactivated.

**Fix:** sign in as the system administrator and activate a key. See [Activate your licence](/docs/installation/licence/).

## License has expired (code 50)

Error ID: [ST-LIC-002](/docs/troubleshooting/errors/st-lic-002/)

```
License has expired. Please renew your license to continue.
```

**HTTP 402.** The expiry date has passed. The system administrator can still view, delete and open the licence page, but nobody can create or change anything.

**Fix:** activate the renewed key on the **License** page. The licence page warns you 30 days before expiry, so plan renewals early.

## License limit exceeded (code 51)

Error ID: [ST-LIC-003](/docs/troubleshooting/errors/st-lic-003/)

**HTTP 400.** You tried to create something beyond a licence limit, for example one device more than the licence allows. Nothing was created.

**Fix:** delete what you no longer need, or ask your supplier for a larger licence. The **License** page lists every limit next to its current use.

## Over the licence limits (warnings)

Error ID: [ST-LIC-004](/docs/troubleshooting/errors/st-lic-004/)

```
Your system exceeds the current license limits. Please acquire a license to continue using all features.
Your system has been over license limits for an extended period. The system will stop working soon if a valid license is not acquired.
```

The system has more of something than the licence allows, so the grace period is running: a warning for the first 7 days, then a critical warning until day 15.

**Fix:** get back under the limits, or activate a larger licence, before the grace period ends. The dialog lists what is over the limit.

## System blocked (code 52)

Error ID: [ST-LIC-005](/docs/troubleshooting/errors/st-lic-005/)

```
System blocked: license grace period has ended. Please acquire a license to continue.
```

**HTTP 403.** The grace period ended while the system was over its limits. Nothing can be created or changed. The system administrator can still sign in, view, delete and manage the licence.

**Fix:** delete entities until you are under every limit, or activate a licence with higher limits. The block clears straight away.

## License runtime blocked

Error ID: [ST-LIC-006](/docs/troubleshooting/errors/st-lic-006/)

```
License runtime blocked: Hardware fingerprint disagrees with this license (N/6 match). This license was activated on a different machine…
```

**HTTP 403.** The hardware no longer matches the machine where the key was activated. Usually the installation was copied or moved to new hardware, or a virtual machine or Docker host changed its identity.

**Fix:**

- If you moved the installation on purpose, deactivate the key on the old machine (or ask your supplier to release it), then activate it on this one. See [Move to a new server](/docs/operations/move-server/).
- On a Linux Docker host, mount `/etc/machine-id` into the container so the fingerprint survives rebuilds. See [Install with Docker](/docs/installation/docker/#linux-hosts-keep-the-licence-bound).
- On Windows, install with [Platform Manager](/docs/installation/windows/), which pins the identity for you.

The same message can also come from the licence server when your supplier has revoked the key. In that case, contact your supplier.

## Failed to activate license

Error ID: [ST-LIC-007](/docs/troubleshooting/errors/st-lic-007/)

```
Failed to activate license. Please check your license key.
Invalid license key format. License key must be in INVE format (INVE-TYPE-XXXX-XXXX-...).
```

**Fix:**

- Paste the whole key, starting with `INVE-` and with no spaces or line breaks added.
- Check that this machine can reach `https://license.invenia.in`. Activation needs internet access once.
- If the key was already activated on another machine, deactivate it there first.
