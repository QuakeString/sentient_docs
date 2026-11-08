+++
title = "HTTP Access Token based authentication"
description = "SENTIENT Access Token based authentication for HTTP transport."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ssl/http-access-token.md"
+++
Access token–based authentication is the default authentication method for devices in SENTIENT. 
When a device is created, SENTIENT automatically generates a unique access token. This token can be [updated](/docs/user-guide/ui/devices/#manage-device-credentials) later in the device details.

To authenticate a device over HTTP, the client must include the access token as part of the HTTP request URL.

For details about supported endpoints, request formats, and payloads, refer to the [HTTP API](/docs/reference/http-api/) documentation.
