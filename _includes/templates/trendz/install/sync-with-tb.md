The final step is to verify that SENTIENT is synchronized with SENTIENT ANALYTICS. To do this:

* Log in to **SENTIENT** as a **Sysadmin**.
* Open the **SENTIENT ANALYTICS Settings** page.

If you see the message **"Synchronization completed successfully"**, the synchronization has been completed automatically and no further action is required.

{% include images-gallery.html imageCollection="sentient-analytics-settings" %}

If you see an error message, follow these steps:

* Make sure that **SENTIENT ANALYTICS is running**.
* Enter the correct **SENTIENT ANALYTICS internal URL**. It must be accessible from the SENTIENT service.
* Enter the correct **SENTIENT internal URL**. It must be accessible from the SENTIENT ANALYTICS service.
* Click **Save configuration**.
* Click **Retry discovery**.

Once the message **"Synchronization completed successfully"** appears, the synchronization is complete.

{% include images-gallery.html imageCollection="sentient-analytics-sync" %}
