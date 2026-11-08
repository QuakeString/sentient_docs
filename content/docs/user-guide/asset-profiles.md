+++
title = "Asset profiles"
description = "Group the settings that many assets share: rule chain, queue, mobile dashboard, alarm rules and calculated fields."
aliases = ["/docs/user-guide/ui/asset-profiles", "/docs/user-guide/ui/asset-profiles/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
An **asset profile** does for [assets](/docs/user-guide/ui/assets/) what a [device profile](/docs/user-guide/device-profiles/) does for devices: it holds the settings that a kind of asset has in common. Make one per kind, for example `Plant`, `Production line` or `Boiler house`. Every asset has exactly one profile; new assets get `default` unless you choose another.

The tenant administrator manages them under **Profiles > Asset profiles** in the left menu.

## Add a profile

Click **+**, then **Create new asset profile**, fill in the settings below and click **Add**. **Import asset profile** loads a profile exported from another SENTIENT as a JSON file.

| Setting | What it does |
|---|---|
| **Name** | Unique within the tenant |
| **Default rule chain** | The [rule chain](/docs/user-guide/rule-engine-2-0/overview/) for messages that come from these assets, for example values written by a calculated field. Empty means the **Root Rule Chain** |
| **Mobile dashboard** | The dashboard the mobile app opens for one of these assets |
| **Queue** | The queue those messages go through. Keep `Main` unless you set up [queues](/docs/user-guide/rule-engine-2-5/queues/) |
| **Default edge rule chain** | The rule chain used on an [Edge](/docs/edge/) |
| **Image** | Shown for the profile in lists and widgets |
| **Description** | Free text |

## Tabs

Click a profile to open it. Besides **Details**, it has **Calculated fields** and **Alarm rules** that apply to every asset of the profile, for example a plant's total power from its meters, or an alarm when a line's output drops. **Audit logs** and **Version control** show its history.

## Default and delete

**Make asset profile default** in a profile's row makes it the one new assets get. To delete a profile, click the bin in its row. SENTIENT refuses with "The asset profile referenced by the assets cannot be deleted!" while assets still use it; move them to another profile first.

## Related

- [Assets](/docs/user-guide/ui/assets/)
- [Device profiles](/docs/user-guide/device-profiles/)
- [Calculated fields](/docs/user-guide/calculated-fields/)
