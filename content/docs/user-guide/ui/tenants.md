+++
title = "Tenants"
description = "SENTIENT Tenants management"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/tenants.md"
+++
## Introduction

SENTIENT supports [Multitenancy](https://en.wikipedia.org/wiki/Multitenancy) out-of-the-box.

You can treat Tenant as a separate business-entity: individual or organization who owns or produces devices and assets.

Tenant may have multiple tenant administrator users, enormous number of [customers](/docs/user-guide/ui/customers), and an unlimited number of [users](/docs/user-guide/ui/users), assets, and devices.

## Сreate new tenant

The **System administrator** is able to create tenant entities.

To add a new tenant, please follow the instructions below:


1. Login to your SENTIENT instance WEB UI as a system administrator;

1. Navigate to the Tenants page. Then click on the "plus" icon in the upper right corner of the screen;

1. You must fill in the required fields: title and tenant profile;

1. Optionally, include the country, city, address, phone number, and email address. Then click "Add";

1. New tenant is created.


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/create-tenant-1-ce.webp" alt="Login to your SENTIENT instance WEB UI as a system administrator;" loading="lazy"><figcaption>Login to your SENTIENT instance WEB UI as a system administrator;</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/create-tenant-2-ce.webp" alt="Navigate to the Tenants page. Then click on the &quot;plus&quot; icon in the upper right corner of the screen;" loading="lazy"><figcaption>Navigate to the Tenants page. Then click on the "plus" icon in the upper right corner of the screen;</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/create-tenant-3-ce.webp" alt="You must fill in the required fields: title and tenant profile;" loading="lazy"><figcaption>You must fill in the required fields: title and tenant profile;</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/create-tenant-4-ce.webp" alt="Optionally, include the country, city, address, phone number, and email address. Then click &quot;Add&quot;;" loading="lazy"><figcaption>Optionally, include the country, city, address, phone number, and email address. Then click "Add";</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/create-tenant-5-ce.webp" alt="New tenant is created." loading="lazy"><figcaption>New tenant is created.</figcaption></figure></div>


Learn more about tenant profiles [here](/docs/user-guide/tenant-profiles).

<br>
On the Tenant details page, you as the System administrator can view the attributes, the latest telemetry, assign the home dashboard, and copy the tenant ID.


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/tenant-details-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Create tenant administrator

The **System administrator** is also able to create multiple **users with Tenant administrator role** in each tenant.

To add the User follow the instructions below:


1. Click the "Manage tenant admins" icon on the row of the tenant. The second option: choose the tenant and click on it. Then click on "Manage tenant admins" button;

1. Click on the "plus" icon in the top right corner. In "Add User" window specify user email, enter information about the new user and select "Show activation link" or "Send activation email" from the drop-down menu;

1. If you selected the option "Show activation link", copy the link address and send it to the user. Click "OK";

1. New user with tenant administrator role is created.


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/create-user-in-tenant-1-ce.webp" alt="Click the &quot;Manage tenant admins&quot; icon on the row of the tenant. The second option: choose the tenant and click on it. Then click on &quot;Manage tenant admins&quot; button;" loading="lazy"><figcaption>Click the "Manage tenant admins" icon on the row of the tenant. The second option: choose the tenant and click on it. Then click on "Manage tenant admins" button;</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/create-user-in-tenant-2-ce.webp" alt="Click on the &quot;plus&quot; icon in the top right corner. In &quot;Add User&quot; window specify user email, enter information about the new user and select &quot;Show activation link&quot; or &quot;Send activation email&quot; from the drop-down menu;" loading="lazy"><figcaption>Click on the "plus" icon in the top right corner. In "Add User" window specify user email, enter information about the new user and select "Show activation link" or "Send activation email" from the drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/create-user-in-tenant-3-ce.webp" alt="If you selected the option &quot;Show activation link&quot;, copy the link address and send it to the user. Click &quot;OK&quot;;" loading="lazy"><figcaption>If you selected the option "Show activation link", copy the link address and send it to the user. Click "OK";</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/create-user-in-tenant-4-ce.webp" alt="New user with tenant administrator role is created." loading="lazy"><figcaption>New user with tenant administrator role is created.</figcaption></figure></div>


In a tenant details window, the System administrator can use the following action tabs:

1) **Disable the User account**.

2) **Display activation link** shows the activation link for the Tenant administrator user.

3) **Resend activation** resends the account activation email to the user’s email box.

4) **Login as Tenant administrator** opens the Sentient platform from the Tenant administrator UI.

5) The System Administrator can also **Delete user** from both the user details page and tenant admins list.


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/user-details-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Edit tenant or user

In the Tenant details you can edit all fields.

Let's see how to do this:


1. Click on a tenant`s name to open their details. Click the "pencil" icon to enter edit mode;

1. Edit the fields. For example, you can set up a home dashboard for all users of this tenant. After that, save all changes;

1. You have updated tenant information.


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/edit-tenant-1-ce.webp" alt="Click on a tenant`s name to open their details. Click the &quot;pencil&quot; icon to enter edit mode;" loading="lazy"><figcaption>Click on a tenant`s name to open their details. Click the "pencil" icon to enter edit mode;</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/edit-tenant-2-ce.webp" alt="Edit the fields. For example, you can set up a home dashboard for all users of this tenant. After that, save all changes;" loading="lazy"><figcaption>Edit the fields. For example, you can set up a home dashboard for all users of this tenant. After that, save all changes;</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/edit-tenant-3-ce.webp" alt="You have updated tenant information." loading="lazy"><figcaption>You have updated tenant information.</figcaption></figure></div>


Also, you can edit the **user**.

The steps are similar to how we edit the tenant:


1. Click on a user`s name to open their details. Click the "pencil" icon to enter edit mode;

1. Edit the fields. For example, you can set up a home dashboard for all users of this user. After editing, save all changes;

1. You have updated user information.


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/edit-user-1-ce.webp" alt="Click on a user`s name to open their details. Click the &quot;pencil&quot; icon to enter edit mode;" loading="lazy"><figcaption>Click on a user`s name to open their details. Click the "pencil" icon to enter edit mode;</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/edit-user-2-ce.webp" alt="Edit the fields. For example, you can set up a home dashboard for all users of this user. After editing, save all changes;" loading="lazy"><figcaption>Edit the fields. For example, you can set up a home dashboard for all users of this user. After editing, save all changes;</figcaption></figure><figure><img src="/images/user-guide/tenant-profile/CE/edit-user-3-ce.webp" alt="You have updated user information." loading="lazy"><figcaption>You have updated user information.</figcaption></figure></div>


## Delete tenant or user

You can delete the **Tenant** at once with all its users. To do this, click on the "trash" icon and then also confirm the deletion by clicking on "Yes".


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/delete-tenant-2-ce.webp" alt="Find the tenant you want to delete. Click on the &quot;delete&quot; icon and confirm the deletion by clicking on &quot;Yes&quot;." loading="lazy"><figcaption>Find the tenant you want to delete. Click on the "delete" icon and confirm the deletion by clicking on "Yes".</figcaption></figure></div>


In addition, there is an option to delete the user using the action tab in Tenant details window.


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/delete-tenant-3-ce.webp" alt="In addition, there is an option to delete the Tenant using the action tab in Tenant details window." loading="lazy"><figcaption>In addition, there is an option to delete the Tenant using the action tab in Tenant details window.</figcaption></figure></div>


Also, you can delete any **user** from the Tenant. To do this, go to the Tenant, find the user you need and click on the "trash" icon. After clicking, a warning window will appear. If you are sure you want to delete the user, click on "Yes".


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/delete-user-2-ce.webp" alt="Go to the tenant. Find the user you want to delete. Click on the &quot;delete&quot; icon and confirm the deletion by clicking on &quot;Yes&quot;." loading="lazy"><figcaption>Go to the tenant. Find the user you want to delete. Click on the "delete" icon and confirm the deletion by clicking on "Yes".</figcaption></figure></div>


In addition, there is an option to delete the Tenant using the action tab in Tenant details window.


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/delete-user-3-ce.webp" alt="In addition, there is an option to delete the user using the action tab in Tenant details window." loading="lazy"><figcaption>In addition, there is an option to delete the user using the action tab in Tenant details window.</figcaption></figure></div>


## Login as tenant administrator

If you need to log in as a tenant, just open the tenant group and click the icon opposite to the user account to log in as this tenant.


<div class="st-gallery"><figure><img src="/images/user-guide/tenant-profile/CE/login-as-a-tenant-administrator-1-ce.webp" alt="Open the tenant group. Click the &quot;login&quot; icon opposite to the user account to log in as a tenant administrator." loading="lazy"><figcaption>Open the tenant group. Click the "login" icon opposite to the user account to log in as a tenant administrator.</figcaption></figure></div>


The Tenant Administrator is able to do following actions:

- Provision and Manage [Devices](/docs/user-guide/ui/devices).
- Provision and Manage [Assets](/docs/user-guide/ui/assets).
- Create and Manage [Customers](/docs/user-guide/ui/customers).
- Create and Manage [Dashboards](/docs/user-guide/ui/dashboards).
- Configure [Rule Engine](/docs/user-guide/rule-engine-2-0/re-getting-started/).
- Add or modify default widgets using [Widget Library](/docs/user-guide/ui/widget-library).

All actions listed above are available using [REST API](/docs/reference/rest-api/).

## Next steps
