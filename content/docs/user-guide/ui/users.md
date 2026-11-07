+++
title = "Users"
description = "Add users, activate them, set or reset their password and control what they see first."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Every person who signs in to SENTIENT has a **user** account, identified by an email address. There are three levels:

| Level | Created by | Sees |
|---|---|---|
| **System administrator** | Installation | Tenants, licence and platform settings, not plant data |
| **Tenant administrator** | System administrator, under **Tenants** | Everything in their tenant |
| **Customer user** | Tenant administrator, under **Customers** | Only what belongs to their customer |

What a user may do within their level is set by the **groups** they belong to and the roles of those groups. See [Roles](/docs/administration/roles/).

The tenant administrator manages users under **Users** in the left menu. Customer users are also reached from a customer's **Manage customer users** button.

## The users list

The list shows each user's **Created time**, **First name**, **Last name**, **Email**, **Customer** (for customer users) and **Groups**.

## Add a user

1. Click **+**, then **Add new user**.
2. Type the **Email**, and optionally the first and last name, phone and description.
3. Choose the **groups** the user belongs to.
4. Choose an **Activation method**:
   - **Send activation mail**: SENTIENT emails a link. Needs working [mail settings](/docs/user-guide/ui/mail-settings/).
   - **Display activation link**: SENTIENT shows the link for you to copy and send yourself. Use this on an offline server or when mail is not set up.
5. Click **Add**.

The user opens the link, chooses a password and signs in. Until then the account is not active. The link is valid for 24 hours; **Resend activation** in the user's details sends or shows a new one.

## Set or reset a password

The user can reset their own password from **Forgot password?** on the sign-in page, when mail is set up.

Without mail, an administrator opens the user and clicks **Set password**. The new password must meet the password policy in [Security settings](/docs/user-guide/ui/security-settings/). Tell the user to change it after signing in.

## What the user sees first

In the user's details:

- **Default dashboard** opens right after sign-in instead of the home page.
- **Always fullscreen** shows that dashboard without the menu, for wall screens and control-room displays.

A customer's own **Home dashboard** applies to all its users who have no default dashboard of their own.

## Disable a user

**Disable User Account** in the user's details stops the user from signing in, without deleting anything. **Enable User Account** lets them in again. Use it for staff who leave or for shared accounts that are no longer needed.

## Sign in as another user

The system administrator can click **Login as Tenant Admin** on a tenant administrator, and a tenant administrator can click **Login as Customer User** on a customer user. You then see SENTIENT exactly as that user does, which helps when a user reports something missing. To return, sign out and sign in again with your own account.

## Delete a user

Click the bin in the user's row. The user can no longer sign in. Dashboards and devices they created stay. It cannot be undone.

## Related

- [Customers](/docs/user-guide/ui/customers/)
- [Security settings](/docs/user-guide/ui/security-settings/)
- [Sign in for the first time](/docs/getting-started-guides/first-login/)
