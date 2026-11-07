+++
title = "Roles and permissions"
description = "Control what each user can see and do with roles: built-in roles, your own roles with permissions and restrictions, and roles on groups of entities."
weight = 164

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **role** is a list of what a user may do: which kinds of entities (devices, dashboards, alarms …) and which operations on them (read, write, send RPC …). Users get roles through their **user group**, so you set permissions once for a team instead of user by user.

Open **Security > Roles** in the left menu.

## Built-in roles

Every tenant starts with these roles, which cannot be deleted:

| Role | May do |
|---|---|
| **Tenant Administrator** | Everything in the tenant |
| **Tenant User** | Read and change entities, attributes and telemetry, read credentials and send RPC commands, but not create or delete |
| **Customer Administrator** | Everything within the customer |
| **Customer User** | Read entities, attributes, telemetry and credentials, and send RPC commands |

The built-in user groups **Tenant Administrators**, **Customer Administrators** and **Customer Users** hold these roles, so a new user in one of them gets the matching rights.

## Create a role

Click **+** › **Add role** and set:

- **Name**, for example `Shift operator`.
- **Role type**:
  - **Generic**: applies to all entities the user's owner holds.
  - **Group**: applies only to the entities of one entity group, chosen when the role is given (see below).
- **Permissions**: click **Add**, pick a **Resource** (or **All**) and its **Operations**: **All**, **Create**, **Read**, **Write**, **Delete**, **Read Attributes**, **Write Attributes**, **Read Telemetry**, **Write Telemetry**, **Read Credentials**, **Write Credentials**, **RPC Call**, **Add to Group**, **Remove from Group**, **Change owner**, **Claim devices**, **Share Group**, **Assign to Customer**, **Unassign from Customer**, **Execute** and **Impersonate**.
- **Restrictions (Deny Rules)**: operations the role must never allow, even where a permission grants them. For example, permissions **All** › **All** with the restriction **Device** › **Delete** gives full rights except deleting devices.

Resources include the usual entities, and SENTIENT's own: **Calculated Fields**, **Notifications**, **Notification Rules**, **Scheduler Events**, **Report Templates**, **Recipes** and **Recipe Data**.

## Give a role to users

Roles go to **user groups**, not to single users:

1. Open **Entities > Entity groups**, and the user group (or create one, for example `Operators, Line 2`).
2. In its **Roles** tab, click **Add group permission**, pick the **Role**, and for a **Group** role the **Entity Group** it applies to.

For example, a **Group** role `Line operator` (read telemetry, send RPC) given on the device group `Line 2 machines` lets the operators run line 2 and nothing else.

A user's rights are the sum of all roles of all their groups, minus any restriction.

## Check what a role allows

The role's details show its permissions and restrictions. **Parent-assigned role (read-only)** marks a role given by the owner above, which you can see but not change.

## Related

- [Entity groups](/docs/administration/entity-groups/)
- [Users](/docs/user-guide/ui/users/)
