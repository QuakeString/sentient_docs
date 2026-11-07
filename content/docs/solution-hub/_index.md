+++
title = "Solution hub"
description = "Install a complete monitoring solution in one step, change it before or after you install it, and share your own solutions, dashboards, rules and pipelines as packages."
sort_by = "weight"


[extra]
status = "checked"
checked = "4.3.0.57"
+++
A **solution** is everything one application needs, packed together: device and asset profiles, devices and assets, dashboards, calculated fields, alarm rules, rule chains, analytics pipelines, notification rules, users and roles. The **solution hub** installs a solution in one step and removes it again just as cleanly.

Open **Solution hub** in the left menu. It has three tabs: **Templates**, **Drafts** and **Installed**.

![The solution hub's Templates tab: solution cards with their dashboard, category, contents and Install button](/images/st/solution-hub.webp)

## Templates

**Templates** lists what you can install. The tabs along the top switch between whole **Solutions** and single items: **Dashboards**, **Widgets**, **Calculated fields**, **Alarm rules**, **Rule chains**, **Device profiles** and **Analytics pipelines**. The chips filter solutions by category; the magnifier searches.

SENTIENT ships with these solutions, marked **Official**:

| Category | Solutions |
|---|---|
| Manufacturing | Asset health monitoring, CNC machine monitoring, EOT crane management |
| Energy & utilities | Battery energy storage, Diesel generator monitoring, Distribution transformer health, Feeder energy monitoring, Gas meter AMR, Water meter AMR, Commercial rooftop solar, Solar PV plant, Smart street lighting |
| Buildings & facilities | AHU and HVAC monitoring |
| Oil, gas & process | Tank farm |
| Water & environment | Pump station |
| Agriculture | Greenhouse climate |
| Logistics & fleet | Fleet tracking |
| Healthcare, retail & city | Vaccine and medical fridge |

Each card shows how many devices, assets, dashboards and calculated fields the solution creates. Click a card for **About this solution**: **What's inside**, the devices it works with, its alarm rules and notifications, and a **Preview** of its dashboards with simulated values.

## Install a solution

1. Click **Install** on the card.
2. Name the installed solution, and fill in the lists it asks for, for example your devices or zones. The lists start with example rows: replace them with your own, import them with **Import CSV** (**CSV template** gives you the columns), or keep them to try the solution with sample data. **Start with an empty list** clears them.
3. Check **Limits and settings**, such as alarm thresholds. **Reset to defaults** puts back the template's values.
4. If the solution creates users, **Send activation e-mails to the new users** sends each one a link to set a password.
5. Click **Install**. If anything fails, everything already created is removed again, so a failed install leaves nothing behind.

To change anything else before installing, click **Customize**: the values open as a draft (see below).

Many solutions include an **Emulator**. **Start emulator**, on the solution's row under **Installed**, sends realistic simulated data to the solution's devices for two hours, so the dashboards show something before real devices are connected.

## Installed

**Installed** lists the solutions in your tenant, with the template and version they came from.

- **Open dashboard** opens the solution's main dashboard.
- **View as user** signs you in as one of the solution's users to see it the way they do. Log out to come back.
- **Edit** opens the solution as a draft, **Rename** renames it, **Copy as a new solution** starts a copy next to it, and **Save as template** turns it into a template.
- **Update to the newer template** appears when SENTIENT brings a newer version of the template. Changes you made to installed items are listed first, and **Apply anyway** overwrites them.
- **Uninstall** removes everything the solution created. **Keep its devices and assets (with their telemetry)** keeps your plant data. Items that another installed solution still uses are kept.

## Drafts: build or change a solution

A **draft** is a solution being put together, either new or as changes to an installed one. In **Drafts**, click **New solution** and choose how to start:

| Start | Gives you |
|---|---|
| **From scratch** | An empty solution. Describe it to the AI assistant, or add items yourself |
| **From a template** | The template's defaults as a starting point |
| **Change installed** | An installed solution's items as they are now. Installing applies your changes in place, and devices keep their data |
| **Copy installed** | A new solution next to an installed one, with its own names |

The draft lists its items by section: devices, dashboards, rule chains and so on. Click an item to edit it as JSON, **Add from this tenant** copies an existing entity into the draft, and **Ask the assistant** lets the [AI assistant](/docs/ai/assistant/) change the draft. Its changes are marked, so you can review each one. **Check** validates the draft, and **Install** or **Apply** creates it.

**Save as template** turns the draft into a template in your tenant's **Templates**, ready to install again.

## Share solutions and single items

- On many SENTIENT pages, such as a dashboard, an alarm rule or a rule chain, **Save to Solution hub** keeps a copy in the hub, and **Add from Solution hub** adds one from the hub to that page.
- **Export as file** saves a solution as a `.sentient-solution` package for another SENTIENT. **Import package** reads one.

A package shows where it came from: **Official** (ships with SENTIENT), **Verified** (signed by a trusted key), **Unsigned**, or **Yours**. For an unsigned package, tick **I trust where this package came from** before installing. **What it needs** lists the widgets and images the package brings, with those that differ here. **Replace widgets and images that differ here** overwrites yours.

## Related

- [Data pipelines](/docs/solution-hub/pipelines/)
- [Alarm rules](/docs/user-guide/alarm-rules/)
- [Dashboards](/docs/user-guide/dashboards/)
