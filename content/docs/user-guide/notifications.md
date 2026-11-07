+++
title = "Notification center"
description = "Tell people about alarms, device activity and changes, in SENTIENT and by email, SMS, Telegram or WhatsApp; send messages yourself; set up escalation."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
The **notification center** decides who hears about what, and how. It sends messages in two ways:

- **Rules** send a notification by themselves when something happens, for example when an alarm is raised or a pump stops reporting.
- **Send notification** lets you write a message to a group of users right away or at a set time, for example a planned shutdown.

Open it from **Notification center** in the left menu. It has five tabs: **Inbox**, **Sent**, **Recipients**, **Templates** and **Rules**.

## Inbox

Every notification for you appears in the bell at the top right of SENTIENT as soon as it is sent, without reloading the page, and in the **Inbox** tab. Click one to open its link, for example the alarm's dashboard. **Mark all as read** clears the count. **Unread** and **All** switch the list.

## Delivery methods

| Method | Reaches the user | Set up in |
|---|---|---|
| **Web** | In the bell and the inbox | Always available |
| **Email** | At the user's email address | [Mail server](/docs/user-guide/ui/mail-settings/) |
| **SMS** | At the phone number in the user's profile | [SMS provider](/docs/user-guide/ui/sms-provider-settings/) |
| **Telegram**, **WhatsApp** | At the account the user linked | [Notification channels](/docs/user-guide/notification-channels/) |
| **Mobile app** | As a push message | [Notification channels](/docs/user-guide/notification-channels/#mobile-app-push) |
| **Slack**, **Microsoft Teams** | Not available in 4.3.0.57 | [Slack](/docs/user-guide/ui/slack-settings/) |

A method that is not set up cannot be chosen. Each user can switch methods off for each kind of notification under their initials › **Account** › **Notification settings**.

## Recipients

A **recipient group** names who gets a notification. Click **+** in the **Recipients** tab, give it a name, and choose one of:

| Type | Who |
|---|---|
| **All users** | Everyone in the tenant |
| **Tenant administrators** | The tenant's administrators |
| **Customer users** | The users of one customer |
| **User list** | Users you pick by name |
| **Users of the entity owner** | The users of the customer that owns the device or asset the notification is about. Use it to tell each customer only about its own equipment |
| **Affected user** | The user an alarm was assigned to, or whose comment was answered |

Make groups by role, for example `Shift supervisors` and `Maintenance`, so rules stay simple when people change.

## Templates

A **template** is the text of a notification, with a version for each delivery method: a subject and message for email, a short text for SMS, a message and an optional button for the web. Placeholders are filled in when the notification is sent:

| Placeholder | Becomes |
|---|---|
| `${alarmType}`, `${alarmSeverity}`, `${alarmStatus}` | The alarm's type, severity and status |
| `${alarmOriginatorName}`, `${alarmOriginatorEntityType}` | The device or asset that raised it |
| `${deviceName}`, `${deviceType}`, `${deviceLabel}` | For device activity |
| `${entityName}`, `${entityType}`, `${actionType}`, `${userEmail}` | For entity actions: what changed, how, and by whom |
| `${comment}`, `${userFirstName}`, `${userLastName}` | For alarm comments |
| `${recipientFirstName}`, `${recipientLastName}`, `${recipientEmail}` | The person receiving it |

Add `:upperCase`, `:lowerCase` or `:capitalize` to change the case, for example `${alarmSeverity:capitalize}`. A web template's button can open a dashboard or a link.

## Rules

A **rule** sends a template to recipients when its trigger fires. Click **+** in the **Rules** tab, choose the **Trigger**, the **Template** and the recipients, and set the trigger's filter:

![The Rules tab of the notification center, with the default rules every tenant gets](/images/st/notification-rules.webp)

| Trigger | Fires when | Filter |
|---|---|---|
| **Alarm** | An alarm is created, changes severity, is acknowledged or cleared (**Notify on**) | Alarm types and severities. Empty means all |
| **Device activity** | A device becomes active or inactive | Devices or device profiles |
| **Entity action** | A device, asset or other entity is added, updated or deleted | Entity type and actions |
| **Alarm comment** | Someone comments on an alarm | Alarm types, severities; **Notify only user comments** |
| **Alarm assignment** | An alarm is assigned or unassigned | Alarm types, severities |

> **Note for 4.3.0.57:** the system administrator's triggers (**Entities limit**, **API usage limit**, **Exceeded rate limits**, **New platform version**, **Rule engine lifecycle event**, **Edge connection**, **Edge communication failure**, **Task processing failure**, **Resources shortage**) can be saved but do not send anything yet. Licence limit warnings are sent.

### Escalation for alarms

For the **Alarm** trigger, the recipients form an **escalation chain**: the **First recipient** group is told at once, and you can add further groups, each with a delay. When a group's delay has passed, that group is told too. Under **Stop the escalation on the alarm status become**, choose for example **Acknowledged** and **Cleared**: once someone acknowledges the alarm, or it clears, the later groups are not told. Without it, every group is told, whatever happened to the alarm.

A typical chain for a plant:

1. Shift operator, at once, by web and Telegram.
2. Shift supervisor, after 10 minutes, by SMS.
3. Plant manager, after 30 minutes, by SMS and email.

## Send notification

1. In the **Inbox** or **Sent** tab, click **Send notification**.
2. Choose a template, or switch it off and write the message here.
3. Choose the **Recipients** groups and the **Delivery method**s.
4. To send it later, switch on **Schedule for later** and set the date and time.
5. Click **Send**. The **Sent** tab shows each sent or scheduled notification and how many recipients it reached; a scheduled one can still be deleted there.

## Related

- [Working with alarms](/docs/user-guide/alarms/)
- [Alarm rules](/docs/user-guide/alarm-rules/)
- [Notification channels](/docs/user-guide/notification-channels/)
