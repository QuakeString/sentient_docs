+++
title = "Tenants"
description = "Create separate, isolated workspaces on one SENTIENT server and give each its administrators and limits."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **tenant** is a separate workspace on a SENTIENT server, with its own devices, dashboards, rule chains, users and data. Tenants cannot see each other. Most plants need only one tenant; use several when one server hosts different companies or must keep business units fully apart.

Only the **system administrator** manages tenants. Sign in as the system administrator and open **Tenants** in the left menu.

## The tenants list

The list shows each tenant's **Created time**, **Title**, **Tenant profile**, **Email**, **Country** and **City**. Each row has buttons to reach the tenant's contents:

| Button | Opens |
|---|---|
| **Manage tenant admins** | The tenant's administrators |
| **Manage tenant customers** | Its customers |
| **Manage tenant assets** | Its assets |
| **Manage tenant devices** | Its devices |

## Add a tenant

1. Click **+**, then **Add new tenant**.
2. Type a **Title**, and optionally the contact details.
3. Choose a **Tenant profile**. The profile sets the tenant's limits (devices, rate limits, storage time) and which queues it uses. See [Tenant profiles](/docs/user-guide/tenant-profiles/).
4. Optionally choose a **Home dashboard** for its users.
5. Click **Add**.

Then add the first administrator: click **Manage tenant admins** in the tenant's row, click **+**, and fill in the email. Choose **Display activation link** when the server has no mail settings and send the link yourself. See [Users](/docs/user-guide/ui/users/).

The licence limits apply to the whole server, across all tenants. See [Activate your licence](/docs/installation/licence/).

## Tenant details

Click a tenant to open its details: **Details**, **Attributes**, **Latest telemetry**, **Alarms**, **Events** and **Relations**. The buttons at the top are **Open details page**, **Manage tenant admins** and **Delete tenant**.

## Delete a tenant

Click the bin in the tenant's row. Everything in the tenant is deleted: its users, customers, devices, assets, dashboards, rule chains and data. It cannot be undone. Take a [backup](/docs/operations/backup-restore/) first if there is any chance you need the data.

## Related

- [Tenant profiles](/docs/user-guide/tenant-profiles/)
- [Users](/docs/user-guide/ui/users/)
- [Customers](/docs/user-guide/ui/customers/)
