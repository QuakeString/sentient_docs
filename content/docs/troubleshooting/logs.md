+++
title = "Collect logs for support"
description = "Where SENTIENT, Platform Manager and gateway logs are, and what to send to support."
weight = 190

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Logs show what really happened. Collect them **soon after the problem**, before the interesting lines rotate out.

## What to send

1. What you did, what you expected and what happened instead, with the exact error text or a screenshot.
2. The SENTIENT version: it's shown at the bottom of the sign-in page.
3. The time of the problem, with the time zone.
4. The SENTIENT log covering that time. Add the gateway log if devices or PLCs are involved.

<div class="st-callout warn">

Logs can contain device names, IP addresses and user email addresses. They don't contain passwords. Check a log before you send it outside your company.

</div>

## SENTIENT server

**Platform Manager (Windows and Linux):** open **Logs**. It shows the most recent lines of the SENTIENT log. Turn on **Follow** to watch new lines arrive, and click **Export…** to save the log to a file.

**Docker:**

```bash
docker compose -f <compose file> logs --since 2h sentient > sentient.log
```

**Native Linux (systemd):** the log files are in `/var/log/sentient`. You can also run:

```bash
journalctl -u sentient --since "2 hours ago" > sentient.log
```

### More detail for a short time

Raise the log level with the `RUST_LOG` setting, for example `RUST_LOG=debug`. Reproduce the problem, then set it back to the default (`info,sentient_api=info`), because debug logging writes a lot and slows the server down. See [Environment settings](/docs/operations/settings/).

## SENTIENT Gateway

| Installed as | Log |
|---|---|
| Linux package | `journalctl -u sentient-gateway --since "2 hours ago"` |
| Docker | `docker logs --since 2h <gateway container>` |
| Windows | The gateway's admin UI shows its log. |

Gateways can also send their log to SENTIENT. See [Remote logging](/docs/iot-gateway/guides/how-to-enable-remote-logging/).

## Web browser

For problems in the web UI, such as a blank page, a widget that doesn't load or a button that does nothing:

1. Press **F12** to open the developer tools and choose the **Console** tab.
2. Reproduce the problem.
3. Right-click in the console, choose **Save as…**, and send the file together with a screenshot of the page.
