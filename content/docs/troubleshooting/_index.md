+++
title = "Troubleshooting and error codes"
description = "Find the fix for common errors in SENTIENT, the gateway, Platform Manager and devices."
sort_by = "weight"

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Every error has its own page in the [error catalogue](/docs/troubleshooting/errors/), with an ID such as `ST-LIC-002`. Search this site for the ID or for words from the message.

Or start from what you see:

| You see | Go to |
|---|---|
| An error ID such as `ST-DEV-001` | [Error catalogue](/docs/troubleshooting/errors/) |
| An error message with a number, or an API response with `errorCode` | [API error codes](/docs/troubleshooting/error-codes/) |
| A licence dialog, *No active license*, *License has expired*, code 50, 51 or 52 | [Licence errors](/docs/troubleshooting/licence-errors/) |
| Platform Manager or Docker installation stops, or the server does not start | [Installation errors](/docs/troubleshooting/install-errors/) |
| A device shows **Inactive** or sends no values | [Devices do not connect](/docs/troubleshooting/device-connection/) |
| A gateway is offline, a PLC is not read, or a write fails | [Gateway errors](/docs/troubleshooting/gateway-errors/) |
| None of these, or you need help from support | [Collect logs for support](/docs/troubleshooting/logs/) |

When you contact support, send the error ID or the exact message (a screenshot is fine), the SENTIENT version you run, and the log from the minutes around the error.
