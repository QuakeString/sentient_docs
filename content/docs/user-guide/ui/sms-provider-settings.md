+++
title = "SMS provider"
description = "Connect SENTIENT to an SMS service so it can text alarm notifications and two-factor codes."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT sends text messages for [notifications](/docs/user-guide/notifications/), such as alarms, and for [two-factor authentication](/docs/user-guide/two-factor-authentication/) codes. It does not send SMS itself: it hands each message to an SMS service you have an account with.

The system administrator sets the service under **Settings > Notifications**, in the **SMS provider settings** card. One provider serves the whole platform.

**On an offline plant network**, the SENTIENT server must still reach the provider over the internet. Without that, use a provider with a server on your network that offers an HTTP interface, through **Custom HTTP**.

## Providers

| Provider | Enter |
|---|---|
| **Amazon SNS** | **AWS Access Key ID**, **AWS Secret Access Key** and **AWS Region**, for example `ap-south-1`. The key needs permission to publish SMS (`sns:Publish`) |
| **Twilio** | **Phone Number From** (your Twilio number in E.164 format, a phone number SID `PN…` or a messaging service SID `MG…`), **Twilio Account SID** and **Twilio Account Token** |
| **Custom HTTP** | The request your SMS service expects, see below. Use it for local and regional services such as Fast2SMS, MSG91, TextLocal or Gupshup |
| **SMPP** | Listed, but **not supported in 4.3.0.57**: saving works, sending fails with "SMPP SMS provider is not implemented in SENTIENT". Use Custom HTTP if your operator also offers an HTTP interface |

Secrets are stored encrypted and shown masked after you save.

## Custom HTTP

Describe the request your service's documentation shows. In the URL, headers and body you can use these placeholders, which SENTIENT fills in for each message:

| Placeholder | Becomes |
|---|---|
| `${to}` | The recipient's phone number, in E.164 format, for example `+919123456789` |
| `${message}` | The text of the message |
| `${apiKey}` | The value of **API key / token** |
| `${name}` | Any value from **Extra params (JSON)**, for example `${senderId}` |

| Setting | What to enter |
|---|---|
| **HTTP method** | `GET` or `POST` |
| **Request URL** | The service address. Placeholders are URL-encoded |
| **API key / token** | The secret the service gave you |
| **Content-Type (POST)** | `application/json` or `application/x-www-form-urlencoded` |
| **Body template (POST)** | The request body. Placeholders are escaped to suit the content type |
| **Headers (JSON)** | Optional headers, for example `{"Authorization":"Bearer ${apiKey}"}` |
| **Extra params (JSON)** | Optional values that are not secret, for example `{"senderId":"PLANTA"}` |
| **Success marker (optional)** | Text that a successful response always contains, for example `"return":true`. Many services answer HTTP 200 even when the message was refused; with a marker, SENTIENT treats such answers as failures |

An example for a service that takes JSON:

```text
HTTP method:   POST
Request URL:   https://sms.example.com/api/send
Content-Type:  application/json
Body template: {"to":"${to}","text":"${message}","sender":"${senderId}"}
Headers:       {"Authorization":"Bearer ${apiKey}"}
Extra params:  {"senderId":"PLANTA"}
```

The request times out after 15 seconds.

## Test and save

Click **Send test SMS**, type a phone number in E.164 format and a message, and send. When the text arrives, click **Save**.

## Phone numbers

SENTIENT sends to the phone number in each user's profile. It must be in **E.164 format**: a `+`, the country code and the number, without spaces, for example `+919123456789`. Numbers in other formats are skipped with "Phone number must be in E.164 format".

A message longer than 1,600 characters is cut. The [API usage](/docs/administration/api-usage/) page counts every 70 characters as one SMS.

## Common errors

| Error | Cause | Fix |
|---|---|---|
| invalid SMS provider credentials | The service answered 401 or 403 | Check the key, token or account SID |
| SMS rate-limited | The service answered 429 | Wait, or ask the provider for a higher limit |
| SMS provider error *code*: *text* | The service refused the message; the text is its reason | Often an unregistered sender ID, a template not approved by the operator (DLT in India), or no credit |
| response missing success marker | The answer did not contain the **Success marker** | The service refused the message; the error shows its answer |
| SMS transport error | SENTIENT could not reach the service | Check that the server can reach the internet or the provider's host |

## Related

- [Notification channels](/docs/user-guide/notification-channels/)
- [Notification center](/docs/user-guide/notifications/)
- [Two-factor authentication](/docs/user-guide/two-factor-authentication/)
