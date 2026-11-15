+++
title = "Entity groups"
description = "Group devices, assets, users, dashboards and other entities to give permissions per group, share a group with a customer's users, and set how the group's table looks."
weight = 165

[extra]
status = "checked"
checked = "4.3.0.57"
+++
An **entity group** is a named set of entities of one kind: devices, assets, entity views, customers, users, dashboards or edges. Groups let you give permissions per group, for example *operators of line 2 may control the line 2 machines*, and share a set of entities with a customer's users.

Open **Entities > Entity groups** in the left menu. Every owner has an **All** group per kind, which holds every entity of that kind.

## Create a group

1. Click **+**, choose the **Entity type**, and give the group a **Name** and **Description**.
2. Optionally, under **Share entity group**, share it right away with **All users** or one **User group**, with **Read**, **Write** or **Other** permissions.
3. Click **Add**.

**Manage entities** (or the group's **Entities** list) adds and removes members: **Add Entities**, **Remove from Group**, **Move to Group**, and **Change owner**. An entity can be in several groups.

## The group's tabs

| Tab | What it holds |
|---|---|
| **Roles** (user groups) | The roles the group's users have. See [Roles and permissions](/docs/administration/roles/) |
| **Permissions** (other groups) | Which user groups may use this group, and with which role |
| **Columns** | The columns of the group's entity table: entity fields, attributes or telemetry, with their order, default sort and whether they are hidden on mobile |
| **Settings** | What the table allows: search, add, delete, selection, group transfer actions, when to open entity details, pagination and page size |
| **Actions** | Buttons on the table's rows: open a URL, go to another dashboard, or a custom action |
| **Attributes**, **Latest telemetry**, **Audit logs**, **Version control** | As for other entities |

## Share a group with a customer

To let a customer's users see a set of devices without assigning each device:

1. Create a device group, for example `Customer A pumps`, and add the devices.
2. Open its **Permissions** tab and click **Add group permission**.
3. Choose the customer's user group, for example **Customer Users** of that customer, and the role, for example **Customer User** for read-only access.

## Public groups

**Make entity group public** makes the group and all its data readable without signing in, for example for a public status dashboard. **Make entity group private** undoes it. Use it only for data that may really be public.

## Related

- [Roles and permissions](/docs/administration/roles/)
- [Customers](/docs/user-guide/ui/customers/)
