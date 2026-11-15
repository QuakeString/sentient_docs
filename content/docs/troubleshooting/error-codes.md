+++
title = "API error codes"
description = "The error codes the SENTIENT REST API returns, what causes them and how to fix them."
weight = 185

[extra]
status = "checked"
checked = "4.3.0.57"
+++
When a request fails, the REST API answers with a JSON body like this:

```json
{
  "status": 402,
  "message": "No active license. Please activate a license to continue.",
  "errorCode": 50,
  "timestamp": 1793977099768
}
```

The web UI shows the `message` in a red notice. Integrations, scripts and the mobile app receive the whole body. Use `errorCode` to decide what to do, and the `message` to see the details.

| Code | HTTP | Meaning | What to do |
|---|---|---|---|
| **10** | 401 | **Authentication failed.** Wrong user name or password, or the session token has expired or is invalid. | Sign in again. For scripts, request a new token with `POST /api/auth/login`, or use an [API key](/docs/user-guide/security/api-keys/). If sign-in keeps failing, check the account is activated and not disabled. |
| **20** | 403 | **Permission denied.** You are signed in, but your user may not do this. For example, a customer user tried to change a device, or a tenant administrator opened a system setting. | Ask an administrator for the right role, or sign in as a user who has it. See [Roles and permissions](/docs/administration/roles/). |
| **31** | 400 | **Bad request.** A value is missing or invalid, a name is already used, or a limit in the tenant profile was reached. | Read the `message`: it names the field or the limit. Fix the value, or raise the limit in the [tenant profile](/docs/user-guide/tenant-profiles/). |
| **32** | 404 | **Not found.** The device, dashboard or other item does not exist, or it belongs to another tenant or customer. | Check the ID. It often happens after an item was deleted, or when an export from another system is imported with its old IDs. |
| **50** | 402 | **No licence, or the licence has expired.** | See [Licence errors](/docs/troubleshooting/licence-errors/#no-active-license-code-50). |
| **51** | 400 | **Licence limit exceeded.** Creating this would go over the licence. | Delete what you no longer need, or get a larger licence. See [Licence errors](/docs/troubleshooting/licence-errors/#license-limit-exceeded-code-51). |
| **52** | 403 | **System blocked.** The licence grace period has ended. | See [Licence errors](/docs/troubleshooting/licence-errors/#system-blocked-code-52). |

## Errors without a code

| HTTP | Meaning | What to do |
|---|---|---|
| **429** | **Too many requests.** A rate limit was hit. The answer has `retryAfter` and a `Retry-After` header that say how many seconds to wait. | Wait and try again. Send fewer requests, for example by reading many values in one call. See [Rate limits](/docs/user-guide/api-limits/). |
| **500** | **Internal error.** Something failed inside SENTIENT, usually the database. For security, the details are not sent to the caller. | Try again. If it keeps happening, the server log has the details. See [Collect logs for support](/docs/troubleshooting/logs/). |
| **501** | **Not implemented.** The call exists in the API description but SENTIENT does not support it. | Use another call, or ask support. |

## Device connections

Devices that send data over MQTT, HTTP or CoAP get different errors, such as an MQTT CONNACK code or an HTTP 401 for a wrong access token. See [Devices do not connect](/docs/troubleshooting/device-connection/) and [MQTT v5 error codes](/docs/reference/mqtt-v5-errors-code/).
