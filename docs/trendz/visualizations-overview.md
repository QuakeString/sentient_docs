---
layout: docwithnav-sentient-analytics
assignees:
- vparomskiy
title: Visualisations Overview
description: Built in Visualisation Types in SENTIENT ANALYTICS 
---

SENTIENT ANALYTICS provides major visualization types required for analyzing IoT datasets. 

* [**Tables**](/docs/sentient-analytics/visualizations-tables)
* [**Line Chart**](/docs/sentient-analytics/visualizations-line)
* [**Bar Chart & Histogram**](/docs/sentient-analytics/visualizations-bar)
* [**Pie Chart**](/docs/sentient-analytics/visualizations-pie)
* [**Scatter Plot**](/docs/sentient-analytics/visualizations-scatter)
* [**Heat Map**](/docs/sentient-analytics/visualizations-heatmap)
* [**Calendar**](/docs/sentient-analytics/visualizations-calendar)
* [**Card**](/docs/sentient-analytics/visualizations-card)

## First visualisation

<div class="image-block">
    <div class="image-wrapper">
       <video poster="/images/sentient-analytics/simple-line.png" autoplay="" loop="" preload="auto" muted="" style="width: 750px">
            <source src="https://tb-videos.s3-us-west-1.amazonaws.com/trndz-first-view.webm" type="video/webm">                 
        </video> 
    </div>
</div>

* Open Trend UI home page and press **Create View** button
* Select **Line** chart
* Select **Date** field from left navigation panel and drop it to the **X axis** section
* Select any telemetry field from left navigation panel and drop it to the **Y axis** section

At this moment you will see average measurement from all entities in the SENTIENT

* Add **Entity Name** to the **Series** section - separate series displayed for each entity

## Video Tutorial

We are glad to present the series of webinars about SENTIENT SENTIENT ANALYTICS functionality. 
Learn more about SENTIENT ANALYTICS features and how it helps to transform the IoT data into value for informed decision-making.

&nbsp;
<div id="video">  
    <div id="video_wrapper">
        <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/8a4cPI-XOkI" frameborder="0" allowfullscreen></iframe>
    </div>
</div>

## Next Steps

{% assign currentGuide = "AvailableVisualizations" %}{% include templates/trndz-guides-banner.md %}