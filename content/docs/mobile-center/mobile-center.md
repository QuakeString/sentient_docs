+++
title = "Mobile center"
description = "Register your own builds of the SENTIENT mobile app, group them in bundles, and set the QR code widget."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
**Mobile center** is for organisations that build their own version of the SENTIENT mobile app, for example with their own name and icon. **The standard SENTIENT app needs nothing here**: install it and sign in, or scan the [QR code](/docs/user-guide/ui/mobile-qr-code/) on the home page.

The system administrator opens **Mobile center** in the left menu. It has three parts:

| Part | Holds |
|---|---|
| [Applications](/docs/mobile-center/applications/) | Each app build: its package name and secret, per platform |
| **Bundles** | An Android and an iOS application that belong together, with the **Layout** of the app's menu (which pages it shows, in which order, and your own pages) and the **OAuth 2.0 clients** offered in the app |
| **QR code widget** | What the QR code card on the home page shows, see [Mobile app QR code](/docs/user-guide/ui/mobile-qr-code/) |

> **Note for 4.3.0.57:** the app does not yet receive the OAuth 2.0 clients of a bundle, so OAuth sign-in in the app is not available. **Enable Self registration** has no effect yet.

## Related

- [Mobile app](/docs/mobile/)
- [Mobile app QR code](/docs/user-guide/ui/mobile-qr-code/)
