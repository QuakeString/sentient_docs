+++
title = "Mobile applications"
description = "Register a custom build of the SENTIENT mobile app in Mobile center: package name, secret, store links and versions."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Register each build of your own mobile app under **Mobile center > Applications**, one entry per platform. The standard SENTIENT app needs no entry.

Click **+** and fill in:

| Setting | What to enter |
|---|---|
| **Application package** | The Android application ID or the iOS bundle identifier of your build, for example `com.example.plantapp` |
| **Application title** | A name for the list |
| **Application Secret** | Click **Generate application secret**, and put the same value in your app's build settings. It must be at least 512 bits, Base64-encoded |
| **Status** | Whether the entry is in use |
| **Store information** | The Google Play or App Store link, used by the QR code widget |
| **Version information** | **Min version** and **Latest version** with release notes. In 4.3.0.57 these are stored but not enforced: the app is not asked to update |

Then add the application to a **bundle** under **Mobile center > Bundles** to give it a menu layout. See [Mobile center](/docs/mobile-center/mobile-center/).

## Related

- [Mobile center](/docs/mobile-center/mobile-center/)
- [Mobile app QR code](/docs/user-guide/ui/mobile-qr-code/)
