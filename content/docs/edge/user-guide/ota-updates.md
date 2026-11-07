+++
title = "Edge Over-the-Air Firmware And Software Updates"
description = "Edge Over-the-Air Firmware And Software Updates Overview"

[extra]
status = "imported"
checked = ""
source = "docs/edge/user-guide/ota-updates.md"
+++
## Overview

The SENTIENT **Over-the-Air (OTA) Update** feature is a powerful way to remotely manage device firmware or software, reducing the need for manual updates and enabling rapid deployment of enhancements or fixes.

The **Edge OTA Update** feature is designed similarly to the **Platform (Cloud) OTA Update**. As a result, the **Edge OTA Update** packages can be deployed in both Device and Device Profile configurations in the same manner as **Platform** Device and Device Profile configurations.
Please refer to the [Platform OTA Updates documentation](/docs/user-guide/ota-updates/) for a general understanding of the **OTA Update** feature.

## Provisioning OTA Packages to the SENTIENT Repository

All **OTA firmware and software packages** are created on the Platform and **automatically propagated** to each **Edge** instance connected to it. No additional actions are required from the Tenant administrator or User.


<div class="st-callout info">


**Please note!** <br>
The **OTA Update packages** are created on the **SENTIENT Platform**. It is **not possible to create, modify, or delete** the OTA Update packages on the **Edge** instance.


</div>


<div class="st-gallery"><figure><img src="/images/edge/user-guide/ota-update/0-cannot-create-on-edge-ce.webp" alt="It is not possible to create, modify, or delete the OTA Update packages on the Edge instance." loading="lazy"><figcaption>It is not possible to create, modify, or delete the OTA Update packages on the Edge instance.</figcaption></figure></div>


### Create the OTA Update Package

To create the **OTA update** package on your **SENTIENT Platform**, navigate to the **Advanced features > OTA updates** section and click the **"+"** icon.
In the pop-up window, fill in the following fields:
* **Title:** Enter the firmware package name.
* **Version:** Enter the firmware package update version number.
* **Version tag:** The field is populated with the relevant information automatically. If a custom tag is entered, it should match the package version reported by the device in question _(optional)_.
* **Device profile:** Select the device profile.
* **Package Type:** Select the package type _(Firmware or Software)_.
* **"Upload binary file"/"Use external URL" radiobutton:** Select the file package source. Depending on the selected option, the following will occur: 
  * **Package file:** Drag-n-drop the package file or browse to it on your computer.
  * **Direct URL:** Enter a direct URL to download the file.
* Click the **"Add"** button. _Please note: once the package is uploaded, the title, version, device profile, and package type cannot be modified_.
* Verify that firmware package has been successfully uploaded.


<div class="st-gallery"><figure><img src="/images/edge/user-guide/ota-update/1-ota-upd-section-ce.webp" alt="To create the OTA updates package on your SENTIENT server, navigate to the Advanced features > OTA updates section and click the &quot;+&quot; icon." loading="lazy"><figcaption>To create the OTA updates package on your SENTIENT server, navigate to the Advanced features > OTA updates section and click the "+" icon.</figcaption></figure><figure><img src="/images/edge/user-guide/ota-update/2-add-package-ce.webp" alt="Fill in all mandatory fields and click the &quot;Add&quot; button to proceed. Please note that once the package is uploaded, the title, version, device profile, and package type cannot be modified." loading="lazy"><figcaption>Fill in all mandatory fields and click the "Add" button to proceed. Please note that once the package is uploaded, the title, version, device profile, and package type cannot be modified.</figcaption></figure><figure><img src="/images/edge/user-guide/ota-update/3-verify-on-server-ce.webp" alt="You can verify that firmware package has been successfully uploaded" loading="lazy"><figcaption>You can verify that firmware package has been successfully uploaded</figcaption></figure></div>


### Verify the OTA Update Package on the Edge Instance

Log in to the **SENTIENT Edge** instance using your credentials and navigate to the **Advanced features > OTA updates** section. This is to confirm that the firmware package has been **successfully provisioned** on the **Edge** instance.
  


<div class="st-gallery"><figure><img src="/images/edge/user-guide/ota-update/4-verify-on-edge-ce.webp" alt="Log in to the SENTIENT Edge instance, go to the Advanced features > OTA updates section and confirm that the firmware package has been successfully provisioned on the Edge instance." loading="lazy"><figcaption>Log in to the SENTIENT Edge instance, go to the Advanced features > OTA updates section and confirm that the firmware package has been successfully provisioned on the Edge instance.</figcaption></figure></div>


## Next steps
