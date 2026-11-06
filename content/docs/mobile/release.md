+++
title = "Build and release SENTIENT Mobile Application"

[extra]
status = "imported"
checked = ""
source = "docs/mobile/release.md"
+++
This guide walks you through creating and releasing the SENTIENT mobile app version **1.7.x** for **iOS** and **Android**.


<div class="st-callout info">


If you need to publish a version earlier than **1.7.x**, please use the [legacy guide](/docs/mobile/release-before-v1.7/) for pre‑1.7 releases.


</div>


<br><b><font size="5">Before you start</font></b>

It assumes you [created an app bundle](/docs/mobile/getting-started/#step-1-create-a-bundle-in-the-mobile-center) in the [Mobile center](/docs/mobile-center/mobile-center/) and downloaded the generated **configs.json** file.

If you need to change any settings:
  - Update them in Mobile center.
  - Re‑download configs.json.
  - Replace the file in your project.


<div class="st-callout info">


Do not edit **configs.json** manually. Always manage settings in **Mobile center** to keep all environments in sync and reduce misconfigurations.


</div>


  


<div class="st-gallery"><figure><img src="/images/mobile/release-redownload-config-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/mobile/release-redownload-config-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## iOS — Build & Release

When preparing a release version of your app for publishing on the [App Store](https://developer.apple.com/app-store/submissions/) and [TestFlight](https://developer.apple.com/testflight/), follow the official ["Build and release an IOS app"](https://docs.flutter.dev/deployment/ios) guide.


<div class="st-callout info">


**Important Notice:** While preparing the app for release, for example, when producing a build archive, you must provide the `--no-tree-shake-icons` flag to your build command as well as the `--dart-define-from-file` flag with your config file:


</div>


Flutter build command:

```bash
flutter build ipa --no-tree-shake-icons --dart-define-from-file configs.json
```


## Android — Build & Release

When preparing a release version of your app for publishing on [Google Play](https://support.google.com/googleplay/android-developer/answer/9859152?hl=en), follow the official ["Build and release an Android app"](https://docs.flutter.dev/deployment/android) guide.


<div class="st-callout info">


**Important Notice:** While preparing the app for release, for example, when producing a build archive, you must provide the `--no-tree-shake-icons` flag to your build command as well as the `--dart-define-from-file` flag with your config file:


</div>


Flutter build command:

```bash
flutter build appbundle --no-tree-shake-icons --dart-define-from-file configs.json
```


## Build flags explanation

**`--no-tree-shake-icons`**   
    Prevents Flutter from removing unused icons during the build process, this will allow mobile application to display any icon, that was set to notification in the notification center.

**`--dart-define-from-file configs.json`**   
    Loads SENTIENT Mobile Application configuration from the JSON file downloaded from the Mobile center, ensuring your app uses the correct settings for production.
