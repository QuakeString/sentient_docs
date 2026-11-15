+++
title = "Secrets"
description = "Store passwords, tokens and key files once, encrypted, and refer to them by name in rule chains, integrations, AI models and settings."
weight = 171

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **secret** is a password, token or file (for example a client certificate) stored once, encrypted, and referred to by name. Configuration holds only the reference, `${secret:<name>}`, so the value never shows in a form, an export or a version control commit, and changing it in one place updates every configuration that uses it.

Open **Security > Secrets** in the left menu. Tenant administrators manage their tenant's secrets; the system administrator manages the system's secrets, used in system settings such as the mail server and SMS provider.

## Add a secret

1. Click **+**.
2. Enter a **Name**: letters, digits, `_`, `-` or `.`, no spaces. Below it the dialog shows the reference to use, for example `${secret:mqtt-password}`, with a copy button.
3. Choose the **Type**:
   - **Text** for a password, token or API key. The value is hidden while you type; the eye icon shows it.
   - **File** for multi-line content such as a PEM certificate or private key. Paste it, or click the upload icon to **Load from a file**.
4. Enter the **Value** and an optional **Description**, then click **Save**.

To change a value, edit the secret and enter the new value. Leave **Value** empty to keep the current one.

> **Renaming breaks references.** Configuration finds a secret by its name, so a renamed or deleted secret stops working wherever the old name is used, until you change the configuration or add the secret again.

## Use a secret

Type the reference in any configuration field instead of the value, for example in an MQTT integration's password field:

```text
${secret:mqtt-password}
```

The reference also works inside a longer value, for example `Bearer ${secret:api-token}`. In the table, the **Copy reference** button on each row copies it.

References are resolved when the configuration is used, against the tenant that owns it:

- Rule chain node configuration
- Integrations
- AI models
- Mail server, SMS provider, Telegram and other notification channel settings
- OAuth 2.0 clients
- Version control repository settings

A reference is resolved only in configuration, never in text built from message data, so a device cannot read a secret by sending `${secret:…}` in its telemetry. Values are cached for one minute; saving or deleting a secret clears its cached value at once.

## Passwords typed straight into configuration

You do not have to use secrets for every password. A password, token or key typed directly into a configuration field (a rule node, an integration, the mail server, an OAuth 2.0 client, an AI model) is also encrypted when it is saved, and shown masked as `••••••••` when the form opens again. Save the form with the mask unchanged to keep the stored value.

Use a secret when the same value is used in several places, or when you want to change it without opening each configuration.

## The master key

Secrets and stored passwords are encrypted with AES-256-GCM using a **master key**. The key comes from:

- the `SENTIENT_SECRETS_KEY` environment variable (base64 of 32 bytes), or otherwise
- the key file named by `SECRETS_KEY_FILE`, created on first start. In Docker it is `/var/lib/sentient/secrets.key`.

> **Back up the key file with the database.** A database backup restored without its key cannot open any secret or stored password. They have to be entered again.

The system administrator sees the key on **Security > Secrets > Master key** (the key icon above the table): its source, the key file path, and a **Fingerprint** that identifies the key without revealing it. Use the fingerprint to match a saved key file to a server.

### Rotate the master key

**Rotate key** creates a new key and re-encrypts every secret and stored password with it.

1. Click **Rotate key**, read the warning, then **Rotate now**.
2. The dialog reports how many secrets and configurations were re-encrypted.
3. Back up the new key file. Keep the old key file with any backup made before the rotation: those backups need it.

If a value was changed while the rotation ran, the old key is kept and the dialog asks you to rotate again; **Finish rotation** completes it. Values that no key could open are left as they are and counted; enter them again where they are used.

A key set through `SENTIENT_SECRETS_KEY` cannot be rotated from this page. Move it into the key file first.

## Related

- [Roles and permissions](/docs/administration/roles/)
- [Version control](/docs/user-guide/version-control/)
