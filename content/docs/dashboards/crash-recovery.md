+++
title = "Drafts and crash recovery"
description = "SENTIENT keeps your unsaved dashboard edits in the browser, so a crash or a closed tab does not lose them, and offers them back when you open the dashboard again."
weight = 72

[extra]
status = "checked"
checked = "4.3.0.57"
+++
> **From the release after 4.3.0.57.** In 4.3.0.57, unsaved dashboard edits exist only in the open tab. Save often, especially on large SCADA screens.

While you edit a dashboard, SENTIENT keeps a copy of your unsaved changes in the browser. If the browser crashes, the computer restarts or the tab is closed without saving, the changes are not lost: the next time you open the dashboard, SENTIENT offers them back.

## Get your changes back

Open the dashboard again in the same browser, signed in as the same user. A notice **Unsaved changes found** says when the changes were made and offers:

| Button | Does |
|---|---|
| **Restore** | Opens edit mode with your changes. Check them, then click **Save** |
| **Discard** | Deletes the changes for good |
| **Decide later** | Hides the notice. It comes back the next time you open the dashboard |

If someone saved the dashboard after your changes were made, the notice warns you: *This dashboard was saved again after these changes.* Restoring and then saving replaces that newer version. Choose **Discard** if you want to keep theirs.

Restoring is one undo step. **Ctrl+Z** right after **Restore** goes back to the saved dashboard.

## How it works

- The copy is written about one and a half seconds after each change, and every 10 seconds while you edit.
- It lives in the browser's own storage on this computer (IndexedDB), one copy per user and dashboard. It is not sent to the server, and another computer or browser does not see it.
- **Save** deletes it. So does leaving edit mode with **Close** and dropping the changes.
- A copy nobody comes back to is deleted after 30 days.
- If the dashboard is open in a second tab of the same browser, the second tab does not offer the first tab's changes while the first tab is still open.
- In a private window, or when the browser blocks site data, no copy can be kept. Editing still works, but a crash loses unsaved changes.

## Undo uses less memory

Undo (**Ctrl+Z**) and redo (**Ctrl+Y**) keep up to 50 steps. Each step stores only what changed, so 50 edits on a 200-widget dashboard take about 1.6 MB instead of about 21 MB. The history never takes more than 64 MB; past that, the oldest steps are dropped first.

## Related

- [Dashboards](/docs/user-guide/dashboards/)
- [What is new in SENTIENT dashboards](/docs/dashboards/)
