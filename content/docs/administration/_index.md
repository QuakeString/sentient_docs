+++
title = "Administration"
description = "Manage tenants, users, roles, security, translations and system settings."

aliases = ["/docs/trendz/"]
sort_by = "weight"

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Administration covers who can use SENTIENT and what they may do, how it is secured, and the settings that apply to everyone. Most of it is done by two kinds of administrator:

- The **system administrator** runs the installation: tenants and their limits, mail and SMS servers, security policy, the UI's own texts, and the master key for secrets.
- A **tenant administrator** runs one plant or organisation: its customers, users, roles, entity groups, secrets, translations and home page.

A single-plant installation usually has one tenant. Use several tenants when one SENTIENT serves separate plants or companies whose data must stay apart.

## People and access

| Page | For |
|---|---|
| [Tenants](/docs/user-guide/ui/tenants/) and [Tenant profiles](/docs/user-guide/tenant-profiles/) | Separate organisations and their limits |
| [Customers](/docs/user-guide/ui/customers/) | Your own customers or departments, who see only what you share with them |
| [Users](/docs/user-guide/ui/users/) | Accounts, activation and sign-in |
| [Roles and permissions](/docs/administration/roles/) | What each user may see and do |
| [Entity groups](/docs/administration/entity-groups/) | Sets of devices, assets, dashboards or users to give permissions on and share |

## Security

[Security settings](/docs/user-guide/ui/security-settings/) (password policy and lockout), [two-factor authentication](/docs/user-guide/two-factor-authentication/), [OAuth 2.0](/docs/user-guide/oauth-2-support/) sign-in, [domains](/docs/administration/domains/), [API keys](/docs/user-guide/security/api-keys/), [secrets](/docs/administration/secrets/) and [HTTPS](/docs/user-guide/ssl/http-over-ssl/).

## Running the platform

| Page | For |
|---|---|
| [Translations](/docs/administration/translations/) | Languages for the UI and your own dashboards |
| [Audit log](/docs/user-guide/audit-log/) | Who changed what, and when |
| [API usage and limits](/docs/administration/api-usage/) and [Rate limits](/docs/user-guide/api-limits/) | Monthly quotas and message rates |
| [Version control](/docs/user-guide/version-control/) | Keep configuration in a Git repository |
| [Task manager](/docs/administration/task-manager/) | Background tasks |
| [Home page settings](/docs/administration/home-page/) | What users see after signing in |
| [Mobile app QR code](/docs/user-guide/ui/mobile-qr-code/) | Connect the SENTIENT mobile app |
