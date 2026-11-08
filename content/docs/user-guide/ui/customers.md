+++
title = "Customers"
description = "Give a client, a site team or a department its own users, devices and dashboards."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **customer** is a group of users who see only what you give them: their own devices, assets and dashboards. Use customers for:

- **End clients** of a system integrator, each seeing only their own plant.
- **Sites or departments** of one company, for example *Pune plant* and *Chennai plant*.
- **Read-only viewers** such as operators or managers who need dashboards but must not change anything.

A customer can contain **sub-customers**, for example *Pune plant* under *Acme Industries*, so a hierarchy of companies, sites and teams can be modelled.

Customers belong to a tenant. The tenant administrator creates them and decides what each one sees. Open **Customers** in the left menu.

## The customers list

The list shows each customer's **Created time**, **Title**, **Email**, **Country**, **City**, its **Parent Customer** when it is a sub-customer, and its **Groups**.

Each row has buttons to manage what the customer owns:

| Button | Opens |
|---|---|
| **Manage customer users** | The users who sign in as this customer |
| **Manage customers** | Its sub-customers |
| **Manage customer assets** | Assets the customer owns |
| **Manage customer devices** | Devices the customer owns |
| **Manage customer entity views** | Entity views the customer owns |
| **Manage customer dashboards** | Dashboards the customer can open |

## Add a customer

1. Click **+**, then **Add new customer**.
2. Type a **Title**. It must be unique in the tenant.
3. Optionally fill in the contact details, and choose a **Home dashboard**: the dashboard the customer's users see first after signing in. Tick **Hide home dashboard toolbar** to show it full screen with no toolbar.
4. Click **Add**.

## Give the customer devices, assets and dashboards

A device or asset has one **owner**: the tenant or one customer. To move it to a customer:

1. Open the device or asset.
2. Click **Manage owner and groups**.
3. Choose the customer as the owner, and click **Save**.

Its data, alarms and attributes move with it. The tenant administrator still sees and manages it; with **Include customer entities** switched on, the device and asset lists show customer-owned items too.

For a dashboard, use **Manage customer dashboards** in the customer's row, or open the dashboard and choose the customer there. A dashboard can be shared with several customers. Each customer's users see only the devices of their own customer in it, so one dashboard can serve every customer.

## Add the customer's users

1. In the customer's row, click **Manage customer users**.
2. Click **+** and fill in the user's email, name and role.
3. Send the activation email, or copy the activation link and send it yourself when the server has no mail settings.

See [Users](/docs/user-guide/ui/users/) for the details, and [Roles](/docs/administration/roles/) for what each user may do.

## Customer details

Click a customer to open its details. The tabs are **Details**, **Attributes**, **Latest telemetry**, **Alarm rules**, **Alarms**, **Events**, **Sub-Customers**, **Relations**, **Audit logs** and **Version control**.

## Delete a customer

Click the bin in the customer's row. What happens:

- Its users, and the devices, assets, entity views and dashboards it **owns**, are deleted with it. Move anything you want to keep to another owner first.
- Dashboards that were only **shared** with it are kept; they are just no longer shared with this customer.
- A customer that still has sub-customers cannot be deleted. Delete or move the sub-customers first.
- A customer that a calculated field reads cannot be deleted until the field points elsewhere.

It cannot be undone.

## Related

- [Users](/docs/user-guide/ui/users/)
- [Devices](/docs/user-guide/ui/devices/)
- [Dashboards](/docs/user-guide/dashboards/)
