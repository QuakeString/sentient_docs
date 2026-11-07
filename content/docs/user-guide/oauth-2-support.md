+++
title = "OAuth 2.0 sign-in"
description = "Let users sign in to SENTIENT with Google, Microsoft Entra ID, GitHub, Keycloak or another OAuth 2.0 / OpenID Connect provider."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
With **OAuth 2.0**, users sign in to SENTIENT with an account they already have, such as their company Microsoft or Google account, instead of a separate SENTIENT password. The sign-in page then shows a button for each provider, for example **Login with Microsoft**. SENTIENT can also create the user's account on first sign-in.

**On an offline plant network**, the user's browser and the SENTIENT server must both reach the provider. Use a provider inside the network, such as Keycloak, or keep password sign-in.

The system administrator sets it up under **Security > OAuth 2.0**, which has two lists: **OAuth 2.0 clients** (the providers) and **Domains** (the addresses where each provider's button appears).

## 1. Register SENTIENT with the provider

In the provider's console (Microsoft Entra admin center, Google Cloud console, Keycloak, and so on), register a new web application and enter this **redirect URI**:

```text
https://sentient.example.com/login/oauth2/code/
```

Use the address users type to reach SENTIENT, with `http` or `https` as they use it, and keep the trailing `/`. The provider gives you a **client ID** and a **client secret**.

## 2. Add the client in SENTIENT

Under **OAuth 2.0 clients**, click **+** and fill in:

| Setting | What to enter |
|---|---|
| **Title** | A name for the list |
| **Login provider** | **Google**, **GitHub**, **Facebook** or **Custom**. The first three fill in the provider's addresses for you. Use **Custom** for Microsoft Entra ID, Keycloak and others |
| **Client ID**, **Client secret** | From step 1 |
| **Provider label** | The text on the button: "Login with *label*" |

Under **Advanced settings**, for a custom provider:

| Setting | Example for Microsoft Entra ID (replace `TENANT` with your directory ID) |
|---|---|
| **Access token URI** | `https://login.microsoftonline.com/TENANT/oauth2/v2.0/token` |
| **Authorization URI** | `https://login.microsoftonline.com/TENANT/oauth2/v2.0/authorize` |
| **JSON Web Key URI** | `https://login.microsoftonline.com/TENANT/discovery/v2.0/keys` |
| **User info URI** | `https://graph.microsoft.com/oidc/userinfo` |
| **Scope** | `openid`, `email`, `profile` |
| **User name attribute key** | `email` |

### Who the user becomes

The **Mapper** decides which SENTIENT user an OAuth sign-in belongs to:

| Setting | What it does |
|---|---|
| **Allow user creation** | Off: only users who already exist in SENTIENT with the same email can sign in; others see "User not found". On: SENTIENT creates the user on first sign-in |
| **Activate user** | Marks a created user as active at once |
| **Email attribute key**, **First name attribute key**, **Last name attribute key** | Where the provider puts these values, usually `email`, `given_name`, `family_name` |
| **Tenant name strategy** | Which tenant a created user goes to: **Domain** (the part of the email after `@`), **Email**, or **Custom** with a **Tenant name pattern** such as `Demo Plant`. If no tenant has that name, SENTIENT creates one |
| **Customer name pattern** | Optional: makes the created user a user of this customer instead of a tenant administrator |
| **Default dashboard name**, **Always fullscreen** | What the created user sees first |

Mapper type **Basic** fits most providers; **GitHub** reads the email from GitHub's own address; **Custom** asks your own web service to decide. Apple sign-in is not supported in 4.3.0.57.

> Users created this way become **tenant administrators** unless you set a customer name pattern. With **Allow user creation** on, limit the provider to your own company's accounts, or anyone with an account there gets administrator rights. With the **Domain** or **Email** strategy, every new email domain or address even gets a tenant of its own. For a plant, use **Custom** with your tenant's exact name.

## 3. Add the domain

Under **Domains**, click **+**, type the host name users reach SENTIENT on (for example `sentient.example.com`, without `https://` and port) and choose the OAuth 2.0 clients whose buttons appear there. A user who opens SENTIENT on another address, for example by IP, sees no buttons.

## When sign-in fails

The sign-in page shows the reason:

| Message | Cause |
|---|---|
| User not found: *email* | **Allow user creation** is off and no SENTIENT user has that email |
| User account is disabled | The SENTIENT user is disabled |
| The provider did not return an email address | Add the `email` scope, or set **Email attribute key** to where the provider puts it |
| Missing attribute '*name*' in the provider's user attributes | **User name attribute key** names an attribute the provider does not send |
| Invalid Client Registration | The client was deleted or is not linked to this domain |
| Unable to login. Please contact your Administrator! | A **Custom** mapper points to an address SENTIENT may not call |
| Cannot determine the tenant for this user | The tenant name strategy gave an empty name |
| An error from the provider, such as `redirect_uri_mismatch` | The redirect URI at the provider differs from the address in step 1 |

## Related

- [Two-factor authentication](/docs/user-guide/two-factor-authentication/)
- [Users](/docs/user-guide/ui/users/)
- [Security settings](/docs/user-guide/ui/security-settings/)
