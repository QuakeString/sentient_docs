+++
title = "Domains"
description = "Tell SENTIENT which host names users reach it on, so the right OAuth 2.0 sign-in buttons appear."
aliases = ["/docs/domains/"]
weight = 169

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **domain** is a host name users type to reach SENTIENT, for example `sentient.example.com`. In SENTIENT 4.3.0.57, domains decide which [OAuth 2.0](/docs/user-guide/oauth-2-support/) sign-in buttons the sign-in page shows: a provider's button appears only on the domains it is linked to.

The system administrator manages them under **Security > OAuth 2.0 > Domains**.

## Add a domain

1. Click **+**.
2. Type the host name only: `sentient.example.com`, without `https://`, path or port.
3. Choose the **OAuth 2.0 clients** whose buttons should appear there.
4. Click **Add**.

A user who opens SENTIENT on an address that is not a domain, for example `http://192.168.10.20:8080`, sees no OAuth buttons and signs in with a password.

## Several addresses

Add one domain per address users use, for example the plant's internal name and the public name. Each can show different providers: a company sign-in on the public address, and only passwords inside the plant.

The provider's redirect URI must match each address: `https://sentient.example.com/login/oauth2/code/`. Register every address with the provider.

## Related

- [OAuth 2.0 sign-in](/docs/user-guide/oauth-2-support/)
