+++
title = "Sign in for the first time"
description = "Open SENTIENT, sign in as the system administrator, and create your first tenant and tenant administrator."
weight = 3

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT has three kinds of user:

| User | Does |
|---|---|
| **System administrator** | Runs the installation: the licence, tenants, system settings, translations and mail server. Doesn't see plant data. |
| **Tenant administrator** | Runs one tenant, usually one company or one plant. Creates devices, dashboards, rule chains, alarms, users and customers. |
| **Customer user** | Sees only the devices and dashboards that are assigned to their customer. |

## 1. Open SENTIENT

Open `http://<server>:8080` in Chrome, Edge or Firefox. On the server itself, that is `http://localhost:8080`.

![The SENTIENT sign-in page](/images/st/login.webp)

The version at the bottom of the page, for example **SENTIENT 4.3.0.57**, is the release you are running. Use it to pick the matching version of this manual in the version menu at the top. The buttons at the top right switch between the light, automatic and dark themes.

## 2. Sign in as the system administrator

- If you installed with the **Platform Manager**, use the email and password you entered in the wizard's **Administrator** step.
- If you installed with **Docker**, use `admin@sentient.local` with the password `admin123`. Change the password right away: click your initials at the bottom of the menu, choose **Account**, then open the **Security** tab and use **Change password**.

If no licence is active yet, SENTIENT asks for one first. See [Activate your licence](/docs/installation/licence/).

## 3. Create a tenant

1. Open **Tenants** in the menu.
2. Click **+** › **Add tenant**.
3. Enter a title, for example your company or plant name, and click **Add**.

## 4. Create the tenant administrator

1. In the tenant list, click **Manage tenant admins** on the tenant's row.
2. Click **+** › **Add user**, and enter the email address and name.
3. Under **Activation method**, choose one of these:
   - **Send activation mail:** the user gets an email with a link to set their password. This needs a working [mail server](/docs/user-guide/ui/mail-settings/).
   - **Display activation link:** SENTIENT shows the link. Copy it and give it to the user. Use this when no mail server is set up.
4. The user opens the link, sets a password and is signed in.

## 5. Sign in as the tenant administrator

Sign out, then sign in with the tenant administrator's account. This is where the plant work happens. Continue with [First device to dashboard](/docs/getting-started-guides/helloworld/).

## Forgot the password?

Click **Forgot password?** on the sign-in page to receive a reset link. This needs a working [mail server](/docs/user-guide/ui/mail-settings/). Without one, ask an administrator to set up the mail server first.
