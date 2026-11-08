+++
title = "API keys"
description = "Managing API keys"
aliases = ["docs/user-guide/ui/api-keys"]

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/security/api-keys.md"
+++


API keys provide a simpler alternative to password-based authentication for the SENTIENT API.   
Unlike JWT tokens that require login and periodically expire, API keys are long-lived credentials that remain valid until their configured expiration date or until they are manually revoked.

<hr>

<b><font size="4">Key features</font></b>

- **No login required:** API keys work immediately without exchanging a username and password.
- **Long-lived:** They stay valid until the expiration date you set.
- **Permission inheritance:** The key inherits the exact same rights as the user it was created for.
- **Easy management:** You can enable, disable, or delete a key at any time.
- **Simple integration:** Perfect for third-party apps where you want to avoid complex authentication code.

<hr>

## Creating API Keys

API keys can be created for **your own account** or for **other platform users**, depending on your permissions.

### Creating API Key for Your Account

To create an API key for your own account:
- In the top-right corner, click the ***three-dot*** menu and select **Account**.
- Navigate to the **Security** tab.
- In the **API keys** section, click the **Manage** button.
- Click the **+ Generate** button.
- Enter a **description** for the API key (e.g., *Production server*, *Testing environment*).
- Select the expiration period.
- Click **Generate**.

**Important:** Copy and save the generated API key - it will not be displayed again.


<div class="st-gallery"><figure><img src="/images/user-guide/security/api-keys/creating-api-key-for-our-account-1-ce.webp" alt="In the top-right corner, click the three-dot menu and select Account." loading="lazy"><figcaption>In the top-right corner, click the <b>three-dot</b> menu and select <b>Account</b>.</figcaption></figure><figure><img src="/images/user-guide/security/api-keys/creating-api-key-for-our-account-2-ce.webp" alt="Navigate to the Security tab. In the API keys section, click the Manage button." loading="lazy"><figcaption>Navigate to the <b>Security</b> tab. In the <b>API keys</b> section, click the <b>Manage</b> button.</figcaption></figure><figure><img src="/images/user-guide/security/api-keys/creating-api-key-for-our-account-3-ce.webp" alt="Click the + Generate button." loading="lazy"><figcaption>Click the <b>+ Generate</b> button.</figcaption></figure><figure><img src="/images/user-guide/security/api-keys/creating-api-key-for-our-account-4-ce.webp" alt="Enter a description for the API key, select the expiration period, and click Generate." loading="lazy"><figcaption>Enter a <b>description</b> for the API key, select the expiration period, and click <b>Generate</b>.</figcaption></figure><figure><img src="/images/user-guide/security/api-keys/creating-api-key-for-our-account-5-ce.webp" alt="Copy and save the generated API key — it will not be displayed again." loading="lazy"><figcaption><b>Copy and save</b> the generated API key — it will not be displayed again.</figcaption></figure><figure><img src="/images/user-guide/security/api-keys/creating-api-key-for-our-account-6-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<hr>

### Creating API Key for Another User

API keys can also be created directly from the user’s details page.
A system administrator can create API keys for any users available to them (tenant users), and a tenant administrator can create API keys for their customer users.
In the user details view, the API keys tab provides full access to API key management for that specific user.

- Navigate to the **Customers**/**Users** section.
- Click on the desired user to open their **details**.
- Go to the **API keys** tab.
- Click the **+ Generate** button.
- Enter a **description** for the API key (e.g., *Production server*, *Testing environment*).
- Select the expiration period.
- Click **Generate**.

**Important:** Copy and save the generated API key — it will not be displayed again.

**Note:** The API key inherits all permissions of the user for whom it was created.


<div class="st-gallery"><figure><img src="/images/user-guide/security/api-keys/creating-api-key-for-another-user-1-ce.webp" alt="Navigate to the Customers section.Click on the desired user to open their details.Navigate to the API keys tab and click the + Generate button." loading="lazy"><figcaption>Navigate to the <b>Customers</b> section.<br>Click on the desired user to open their <b>details</b>.<br>Navigate to the <b>API keys</b> tab and click the <b>+ Generate</b> button.</figcaption></figure><figure><img src="/images/user-guide/security/api-keys/creating-api-key-for-another-user-2-ce.webp" alt="Enter a description for the API key, select the expiration period, and click Generate." loading="lazy"><figcaption>Enter a <b>description</b> for the API key, select the expiration period, and click <b>Generate</b>.</figcaption></figure><figure><img src="/images/user-guide/security/api-keys/creating-api-key-for-another-user-3-ce.webp" alt="Copy and save the generated API key — it will not be displayed again." loading="lazy"><figcaption><b>Copy and save</b> the generated API key — it will not be displayed again.</figcaption></figure><figure><img src="/images/user-guide/security/api-keys/creating-api-key-for-another-user-4-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<hr>

## Using API Keys

### In API requests

Include the API key in the **X-Authorization** header with the **ApiKey** prefix:

```
X-Authorization: ApiKey $YOUR_API_KEY_VALUE
```


&#42; Replace **$YOUR_API_KEY_VALUE** with the API key.

<br>Example:

```
curl -X GET --header 'Accept: application/json' \
            --header 'X-Authorization: ApiKey tb_4xpayYjwrKCv5n15CvvS6IUb8vVZe55D-aoXcn_-hl9foOCxlEbtWYoy8bhhMqGt' \
            'https://sentient.cloud/api/auth/user'
```


<div class="st-callout info">


**Security note**: Always use HTTPS in production environments. Executing commands over insecure HTTP connections will send your API key unencrypted, making it vulnerable to interception.


</div>


<hr>

### In Swagger UI

When using [Swagger UI](https://swagger.io/), you can authenticate with an API key:

- Open **Swagger UI**.
- Click the **Authorize** button.
- In the **API key form (apiKey)** section, enter your **API key value** with the **ApiKey** prefix:
  ```
  ApiKey YOUR_API_KEY_VALUE
  ```
  
- Click **Authorize**.


<div class="st-callout info">


**Note:** If both JWT and API key are authenticated, **JWT** takes precedence.


</div>


<div class="st-gallery"><figure><img src="/images/user-guide/security/api-keys/authentication-in-swagger-ui-1.webp" alt="You can manually authenticate or authorize as another user by clicking the Authorize button on the right side of the Swagger page." loading="lazy"><figcaption>You can manually authenticate or authorize as another user by clicking the <b>Authorize</b> button on the right side of the Swagger page.</figcaption></figure><figure><img src="/images/user-guide/security/api-keys/swagger-ui-2.webp" alt="Paste your API key In the API key form (apiKey) section.Then, click &quot;Authorize&quot;." loading="lazy"><figcaption>Paste your API key In the API key form (apiKey) section.<br>Then, click "Authorize".</figcaption></figure></div>


<hr>

## Managing API keys

In the API keys table, each key displays the following information:
- **Created time:** When the API key was generated
- **Description:** A custom description assigned to the key
- **Status:** Indicates whether the key is active or disabled
- **Expiration time:** The date and time when the key will expire


<div class="st-gallery"><figure><img src="/images/user-guide/security/api-keys/managing-api-keys-1-ce.webp" alt="In the API keys table, each key displays its creation time, description, status, and expiration date." loading="lazy"><figcaption>In the API keys table, each key displays its creation time, description, status, and expiration date.</figcaption></figure></div>


Additionally, the following actions are available for each API key:
- **Enable/disable API keys** — Use the toggle switch next to each API key to temporarily disable or re-enable it without deleting the key.
- **Delete API keys** — Click the delete (trash) icon to permanently remove a key. This action cannot be undone.
- **Edit description** — Click the edit (pencil) icon next to the **description** to update the API key’s description.


<div class="st-gallery"><figure><img src="/images/user-guide/security/api-keys/managing-api-keys-2-ce.webp" alt="For each API key, the following actions are available: enable or disable the key, delete the key, or edit its description." loading="lazy"><figcaption>For each API key, the following actions are available: enable or disable the key, delete the key, or edit its description.</figcaption></figure></div>
