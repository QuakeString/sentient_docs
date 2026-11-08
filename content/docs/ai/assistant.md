+++
title = "AI assistant"
description = "Ask the AI assistant about your data, or have it build dashboards, calculated fields, alarm rules, reports and solutions, with your approval for every change."
weight = 157

[extra]
status = "checked"
checked = "4.3.0.57"
+++
The **AI assistant** is a chat panel that sees the page you are on. Ask it a question about your plant, or describe what to build. It reads what exists, checks its own work, and asks before it changes anything.

It needs an [AI model](/docs/ai/models/). If none is available, the panel says **No AI model available**.

## Open it

Click the ✨ button at the top right, or the **Open the AI assistant** tab at the right edge of the screen. The panel can **Float over the page** or be **Pinned to the side**.

The assistant **sees this page**: the dashboard, device, report or solution draft you have open. **Don't use this page** removes it from the conversation. The suggestions in an empty conversation change with the page, for example *Add a trend chart for the main energy meter to this dashboard* on a dashboard, or *Why did this device raise its latest alarm?* on a device.

## Ask and build

Type what you need and press Enter. Some examples:

- *Create a dashboard for my devices.*
- *Add a calculated field for energy per hour.*
- *Why is energy higher today than yesterday?*
- *Create a daily energy report for this asset.*
- *Build an energy-monitoring solution for three feeders.*
- *Explain this page.*

While it works, the panel shows what it is doing (**Reading**, **Checking**, **Adding**, **Saving** …). **Stop** halts it.

### Point at things

**Point at something on the page** lets you click a widget, or a part of one (a series, a column, an axis, the legend), to mention it in your message. Drag to pick several.

### Attach files

**Attach files** (or drop them on the panel) adds a P&ID, a photo of a panel, a specification or a spreadsheet: images, PDFs, DXF drawings, Word, PowerPoint, OpenDocument and text files, up to 8 MB each. For example, attach a P&ID and ask for a SCADA screen of it.

**Voice input** lets you speak instead of typing.

## Approving changes

Under **Before changing anything**, choose:

- **Ask**: the assistant asks before each change. **Approve**, **Approve all** or **Deny**.
- **Auto**: it makes changes without asking. Deletes still ask, unless you tick **Allow deletes for this conversation**.

**Show changes** lists what it changed. The assistant **runs as you, with your permissions**: it cannot see or do more than you can, and every change is in the audit log. If you are editing a dashboard the assistant changed, SENTIENT asks you to save or discard your edits first.

## Model and effort

- **Model** picks one of the **System models** your tenant may use, or **Your models**. Your own model is billed to your provider account; SENTIENT counts its use but does not limit it.
- **Effort** trades speed for thoroughness: **Minimal**, **Low**, **Medium** or **High** (thinks longer, uses more tokens).

**Context and usage** shows how full the conversation is (**Context window**), and the tokens used by you and by the tenant this month against the **System model limits** set in the tenant profile.

## Conversations

**Conversations** lists your earlier conversations to continue one. **New conversation** starts fresh; **Delete this conversation** removes one.

## Customer users

Customer users can use the assistant too, if their tenant allows it. They can ask about their dashboards, devices and alarms, and make the changes their role allows.

## Related

- [AI models](/docs/ai/models/)
- [AI features](/docs/ai/)
