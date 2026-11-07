+++
title = "Mobile app QR code"
description = "Sign in to the SENTIENT mobile app by scanning a QR code on the home page, and set what the QR code widget shows."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
The home page of SENTIENT shows a **QR code**. Scanned with a phone, it signs the user in to the SENTIENT mobile app with their own account, without typing the server address or password.

## Get the app

The SENTIENT mobile app is for Android. It is not in Google Play: download the APK named `SENTIENT-mobile-app-<version>` from the [SENTIENT releases page](https://github.com/QuakeString/sentient-release/releases), open it on the phone and allow the installation when Android asks. See [Mobile app](/docs/mobile/).

> **Note for 4.3.0.57:** the QR code widget shows **Google Play** and **App Store** badges and, scanned without the app installed, leads to a store. Ignore them and install the APK as above.

## Sign in with the QR code

1. Sign in to SENTIENT in a browser and open **Home**. The **Connect mobile app** card shows the QR code.
2. Open the SENTIENT app on the phone and choose to scan a QR code, or scan it with the phone's camera.
3. The app opens signed in as the same user.

The code changes regularly and each one works for **2 minutes**. The phone must reach SENTIENT at the address in the browser: on a plant network, connect the phone to the plant Wi-Fi.

## QR code widget settings

The system administrator sets the widget under **Mobile center > QR code widget**; a tenant administrator can use those settings or switch off **Use system settings** to set the tenant's own.

| Setting | What it does |
|---|---|
| **Appearance on Home page** | Shows or hides the card on the home page |
| **Applications** | **Default** uses the SENTIENT app. **Custom** names your own app build, set up under **Mobile center > Applications** |
| **Badges** | Shows the Android and iOS store badges, on the right or left |
| **Label** | The card's title, for example `Connect mobile app` |

**Preview** shows the result; **Save** applies it.

## Related

- [Mobile app](/docs/mobile/)
- [Security settings](/docs/user-guide/ui/security-settings/)
