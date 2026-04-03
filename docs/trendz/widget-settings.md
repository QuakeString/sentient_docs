---
layout: docwithnav-sentient-analytics
assignees:
- vparomskiy
title: Widget settings
description: Widget settings description

sentient-analytics-widget-automated-refresh:
  0:
    image: /images/sentient-analytics/sentient-analytics-widget-auto-refresh-data.png
    title: 'SENTIENT ANALYTICS widget data refresh settings'

sentient-analytics-widget-filter-change-event:
  0:
    image: /images/sentient-analytics/sentient-analytics-widget-filter-change-event.png
    title: 'SENTIENT ANALYTICS widget filter change event'

---
* TOC
{:toc}

## SENTIENT ANALYTICS widget auto refresh

You can update SENTIENT ANALYTICS widgets on the SENTIENT dashboard with the frequency you prefer by configuring auto refresh.
Here's how to do it:

* Add a widget to the SENTIENT dashboard.
* Open the widget's edit mode and go to the Advanced tab.
* Check the "Update data in real time" checkbox.
* Choose the desired interval for updating data in real time (in minutes).
* Save your changes.

{% include images-gallery.html imageCollection="sentient-analytics-widget-automated-refresh" %}

## Sharing filters between widget

To improve your experience and usability, we've introduced a new feature in our product – the ability to share filter change events between SENTIENT ANALYTICS views on your dashboard. Here's how it works:

1. **Setting Up the Main View:**
   
     When you add a new SENTIENT ANALYTICS view to your dashboard using either the latest or static widget, you'll notice three new fields in the Appearance tab while in edit mode. These fields are:
   * **Broadcast filter change event:** This checkbox allows you to share the filter value with other views.
   * **Listen filter change event:** Enabling this checkbox for a view indicates that it should update its filters when the filter value changes in the main view.
   * **Filter change event name:** All connected views must use the same filter change event name to synchronize their filter updates.

2. **Establishing Connections:**
   * Start by enabling the 'Broadcast filter change event' checkbox in the Appearance tab of the main view. This action shares the filter value with other views.
   * Next, enable the 'Listen filter change event' checkbox for each view that should update its filters based on changes in the main view. These views will now respond to filter changes broadcasted by the main view.
   * Ensure that all connected views use the same filter change event name to maintain synchronization.

{% include images-gallery.html imageCollection="sentient-analytics-widget-filter-change-event" %}

## Next Steps

{% assign currentGuide = "EmbedVisualizations" %}{% include templates/trndz-guides-banner.md %}
