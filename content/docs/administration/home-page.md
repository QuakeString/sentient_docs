+++
title = "Home page settings"
description = "Choose what users see on the Home page and which dashboard opens after sign-in: the built-in home page, a home dashboard, or a default dashboard."
weight = 179

[extra]
status = "checked"
checked = "4.3.0.57"
+++
**Home** is the first item in the left menu and the page users see after signing in. Out of the box it is SENTIENT's built-in home page; you can replace it with one of your own dashboards.

## The built-in home page

Each kind of user gets a built-in home page:

- **Tenant administrators**: device, alarm and dashboard counts, message charts, this month's [API usage](/docs/administration/api-usage/), quick links, recent dashboards, getting started steps, the [Solution hub](/docs/solution-hub/), documentation links and the [mobile app QR code](/docs/user-guide/ui/mobile-qr-code/).
- **Customer users**: their devices, alarms and dashboards.
- **System administrator**: CPU, memory and disk of the server, the version, counts of tenants, devices and users, message charts and the mobile app QR code.

Each user can hide the mobile app QR code card on their own home page.

## A home dashboard

A **home dashboard** replaces the built-in home page with a dashboard of your own, for example a plant overview. With **Hide home dashboard toolbar** the dashboard fills the page without its toolbar (time window, states, full screen).

You can set a home dashboard in three places:

| Where | Applies to |
|---|---|
| **Settings > Home** (tenant administrator) | The tenant |
| A customer's details, **Home dashboard** | The customer's users |
| A user's details, **Home dashboard** | That user |

The Home page uses the first one that applies: the user's own, then (for customer users) the customer's, then the tenant's. A dashboard the user is not allowed to open is skipped, so share the tenant's home dashboard with a customer if its users should see it. If none applies, the user sees the built-in home page.

> **In 4.3.0.57** only the **user's** home dashboard is used: the tenant and customer settings are saved but not read, so set the home dashboard on each user there. The order above applies from the release after 4.3.0.57.

## A default dashboard

A user's details also have **Default dashboard** and **Always fullscreen**, for tenant administrators and customer users. The default dashboard opens right after the user signs in, instead of Home, and the user can still use the menu. With **Always fullscreen** the user only ever sees that dashboard, without the left menu and header: use it for a control-room screen or kiosk account.

## Related

- [Users](/docs/user-guide/ui/users/)
- [Customers](/docs/user-guide/ui/customers/)
- [Dashboards](/docs/user-guide/dashboards/)
