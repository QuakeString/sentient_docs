+++
title = "Layouts"
description = "SENTIENT Dashboard Layouts"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/layouts.md"
+++
Dashboard layouts organize how widgets appear on the dashboard grid. 
Each dashboard state can have its own layout type, settings, and breakpoints, 
which helps create tailored visual presentations for different IoT use cases and screen resolutions.

To modify layouts for a specific [state](/docs/user-guide/dashboards/#states), follow these steps:

1. Enter [dashboard edit mode](/docs/user-guide/dashboards/#edit-mode) by clicking the "Edit mode" button in the upper right corner of the window;
2. Click the "Layouts" button located in the upper left corner of the dashboard window. This will open the layout management window.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/manage-layouts-1-ce.webp" alt="Enter dashboard edit mode by clicking the &quot;Edit mode&quot; button in the upper right corner of the window;" loading="lazy"><figcaption>Enter dashboard edit mode by clicking the "Edit mode" button in the upper right corner of the window;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/manage-layouts-2-ce.webp" alt="Click the &quot;Layouts&quot; button located in the upper left corner of the dashboard window. This will open the layout management window." loading="lazy"><figcaption>Click the "Layouts" button located in the upper left corner of the dashboard window. This will open the layout management window.</figcaption></figure></div>


In the "Manage layouts" window, you can select the layout type suitable for your needs:

- **Default** - a flexible, general-purpose layout;
- **SCADA** - best suited for displaying SCADA HMIs (Human-Machine Interfaces);
- **Divider** - useful for separating sections visually.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/select-layout-type-1-ce.webp" alt="In the &quot;Manage layouts&quot; window, you can select the layout type suitable for your needs: Default, SCADA, or Divider." loading="lazy"><figcaption>In the "Manage layouts" window, you can select the layout type suitable for your needs: Default, SCADA, or Divider.</figcaption></figure></div>


<br>
Breakpoints allow you to create responsive layouts that adapt to different screen sizes.
You can add and configure breakpoints to ensure your dashboard looks perfect on any device.
Further details on setting up each layout type and configuring breakpoints will be discussed below.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/breakpoints-1-ce.webp" alt="Breakpoints allow you to create responsive layouts that adapt to different screen sizes. You can add and configure breakpoints to ensure your dashboard looks perfect on any device." loading="lazy"><figcaption>Breakpoints allow you to create responsive layouts that adapt to different screen sizes. You can add and configure breakpoints to ensure your dashboard looks perfect on any device.</figcaption></figure></div>


## Layout types

The platform supports three layout types: Default, SCADA, and Divider. Each dashboard [state](/docs/user-guide/dashboards/#states) has exactly one layout type configured.

### Default layout

The **Default** layout is a general-purpose layout that fits most dashboards. 
This layout type supports screen breakpoints for responsive design.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-default-1-ce.webp" alt="The Default layout is a general-purpose layout that fits most dashboards. This layout type supports screen breakpoints for responsive design." loading="lazy"><figcaption>The Default layout is a general-purpose layout that fits most dashboards. This layout type supports screen breakpoints for responsive design.</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-default-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### SCADA

The **SCADA** layout is designed for creating SCADA HMIs (Human-Machine Interfaces). 
SCADA HMIs typically consist of scalable widgets called SCADA symbols. 
However, you can also combine [SCADA symbols](/docs/user-guide/scada) with over 500 existing SENTIENT [widgets](/docs/user-guide/widgets/) on the same layout.
This layout type also supports screen breakpoints for responsive design.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-scada-1-ce.webp" alt="The SCADA layout is designed for creating SCADA HMIs (Human-Machine Interfaces) an typically consists of scalable widgets called SCADA symbols. " loading="lazy"><figcaption>The SCADA layout is designed for creating SCADA HMIs (Human-Machine Interfaces) an typically consists of scalable widgets called SCADA symbols. </figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-scada-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Divider

The legacy **Divider** layout lets you split one "Default" layout into two sub-layouts: left and right. 
You can configure the width of these sub-layouts using either a fixed pixel value or a percentage of the screen width. 
Most layout parameters available for the "Default" layout are also supported by the sub-layouts. 
However, sub-layouts do not support breakpoints at this time.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-divider-1-ce.webp" alt="Choose the behavior type &quot;Divider&quot; to split the dashboard into two separate sections: left and right. You can configure the width of these sub-layouts using either a fixed pixel value or a percentage of the screen width." loading="lazy"><figcaption>Choose the behavior type "Divider" to split the dashboard into two separate sections: left and right. You can configure the width of these sub-layouts using either a fixed pixel value or a percentage of the screen width.</figcaption></figure></div>


Just to see how it can look like, let's set up both layouts in completely different ways. Add a background image to the left layout and apply a new background color to the right layout.
And we resize the window in a certain percentage ratio to each other (it is just an example and definitely not a recommendation). After setting the parameters, click the "Save" button in the Layouts window to see the changes.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-divider-2-ce.webp" alt="Set up both layouts in completely different ways. Set a different background for each window. And resize the window sizes in a certain percentage ratio to each other. Then save changes." loading="lazy"><figcaption>Set up both layouts in completely different ways. Set a different background for each window. And resize the window sizes in a certain percentage ratio to each other. Then save changes.</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-divider-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Breakpoints

Breakpoints were introduced in SENTIENT 3.8.0. 
They allow you to define different layout settings and widgets based on the screen width of the end-user.

Each dashboard [state](/docs/user-guide/dashboards/#states) has a `Default` breakpoint. 
This layout is used if no other breakpoints match the current screen resolution.

You can define the following breakpoints:

* Desktop (xl) - min 1920px, max 5000px;
* Desktop (lg) - min 1280px, max 1919px;
* Laptop (md) - min 960px, max 1279px;
* Tablet (sm) - min 600px, max 959px;
* Mobile (xs) - max 599px.

### Adding a Breakpoint

To add a breakpoint, open the "Manage layouts" window and click the "+" button in the breakpoints table. 
When adding a new breakpoint, you can select the corresponding screen resolution and copy both widgets and layout settings from another breakpoint.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/adding-breakpoint-1-ce.webp" alt="To add a breakpoint, open the &quot;Manage layouts&quot; window and click the &quot;+&quot; button in the breakpoints table;" loading="lazy"><figcaption>To add a breakpoint, open the "Manage layouts" window and click the "+" button in the breakpoints table;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/adding-breakpoint-2-ce.webp" alt="Select the breakpoint from the drop-down list;" loading="lazy"><figcaption>Select the breakpoint from the drop-down list;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/adding-breakpoint-3-ce.webp" alt="When adding a new breakpoint, you can select the corresponding screen resolution and copy both widgets and layout settings from another breakpoint. Click &quot;Add&quot;." loading="lazy"><figcaption>When adding a new breakpoint, you can select the corresponding screen resolution and copy both widgets and layout settings from another breakpoint. Click "Add".</figcaption></figure></div>


You can click the "gears" icon to open the layout settings for that breakpoint. Layout settings determine the background configurations of the dashboard and how widgets will be arranged on it.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/adding-breakpoint-4-ce.webp" alt="You can click the “gears” icon to open the layout settings for that breakpoint;" loading="lazy"><figcaption>You can click the “gears” icon to open the layout settings for that breakpoint;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/adding-breakpoint-5-ce.webp" alt="Layout settings determine the background configurations of the dashboard and how widgets will be arranged on it." loading="lazy"><figcaption>Layout settings determine the background configurations of the dashboard and how widgets will be arranged on it.</figcaption></figure></div>


You can also click the "waste-bin" icon to delete a breakpoint. Confirm deleting the breakpoint in the dialog box.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/adding-breakpoint-6-ce.webp" alt="Click the &quot;waste-bin&quot; icon to delete a breakpoint;" loading="lazy"><figcaption>Click the "waste-bin" icon to delete a breakpoint;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/adding-breakpoint-7-ce.webp" alt="Confirm deleting the breakpoint in the dialog box." loading="lazy"><figcaption>Confirm deleting the breakpoint in the dialog box.</figcaption></figure></div>


### Switching between Breakpoints

When a user opens the dashboard, the appropriate breakpoint layout is automatically selected based on the screen resolution.

When editing the dashboard, users can switch between layouts using the combobox located in the top-left corner of the screen.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/switching-between-breakpoints-1-ce.webp" alt="When editing the dashboard, users can switch between layouts using the combobox located in the top-left corner of the screen;" loading="lazy"><figcaption>When editing the dashboard, users can switch between layouts using the combobox located in the top-left corner of the screen;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/switching-between-breakpoints-2-ce.webp" alt="Breakpoint for laptop;" loading="lazy"><figcaption>Breakpoint for laptop;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/switching-between-breakpoints-3-ce.webp" alt="Breakpoint for mobile." loading="lazy"><figcaption>Breakpoint for mobile.</figcaption></figure></div>


### Breakpoints demo dashboard

We have prepared a [demo dashboard](/docs/user-guide/resources/example_of_breakpoints_on_my_dashboard.json) with some configured breakpoints. You can [import](/docs/user-guide/dashboards/#import-dashboard) it into your environment to explore how to switch between different breakpoints in edit mode.
You can also change the screen resolution in your browser's developer tools to see how layouts change when crossing certain screen resolution breakpoints.

See how the same dashboard looks on different screen types:


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/breakpoints-demo-dashboard-1-ce.webp" alt="Default breakpoint." loading="lazy"><figcaption>Default breakpoint.</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/breakpoints-demo-dashboard-2-ce.webp" alt="Laptop breakpoint." loading="lazy"><figcaption>Laptop breakpoint.</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/breakpoints-demo-dashboard-3-ce.webp" alt="Mobile breakpoint." loading="lazy"><figcaption>Mobile breakpoint.</figcaption></figure></div>


### Widget references vs widget copies

**Widget references**

When working with multiple breakpoints, it's important to understand the difference between a widget reference and a widget copy.

By default, when a new breakpoint layout is created, all widgets from the source layout are copied by reference. 
For example, if two breakpoints—Default and Desktop (xl)—reference the same chart widget, any changes made to the widget configuration will be synchronized between both layouts. 
However, changes to the widget's position and size are independent for each layout.

- To copy a widget by reference, right-click on the widget and select "Copy reference" (Ctrl+R);
- To paste the widget as a reference in another breakpoint layout, right-click on the empty space and select "Paste reference" (Ctrl+I).


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/copy-widget-by-reference-1-ce.webp" alt="To copy a widget by reference, right-click on the widget and select &quot;Copy reference&quot; (Ctrl+R);" loading="lazy"><figcaption>To copy a widget by reference, right-click on the widget and select "Copy reference" (Ctrl+R);</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/copy-widget-by-reference-2-ce.webp" alt="To paste the widget as a reference in another breakpoint layout, right-click on the empty space and select &quot;Paste reference&quot; (Ctrl+I);" loading="lazy"><figcaption>To paste the widget as a reference in another breakpoint layout, right-click on the empty space and select "Paste reference" (Ctrl+I);</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/copy-widget-by-reference-3-ce.webp" alt="The widget is pasted as a reference." loading="lazy"><figcaption>The widget is pasted as a reference.</figcaption></figure></div>


In edit mode, you can identify a referenced widget by the presence of a "Reference" button in the widget's edit panel.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/identify-referenced-widget-1-ce.webp" alt="In edit mode, you can identify a referenced widget by the presence of a &quot;Reference&quot; button in the widget&#39;s edit panel." loading="lazy"><figcaption>In edit mode, you can identify a referenced widget by the presence of a "Reference" button in the widget&#39;s edit panel.</figcaption></figure></div>


To replace the reference with the widget copy, click the "Reference" button on the widget editing panel, or right-click on the widget and select "Replace reference with widget copy".


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/replace-reference-with-widget-copy-1-ce.webp" alt="To replace the reference with the widget copy, click the &quot;Reference&quot; button on the widget editing panel, or right-click on the widget and select &quot;Replace reference with widget copy&quot;." loading="lazy"><figcaption>To replace the reference with the widget copy, click the "Reference" button on the widget editing panel, or right-click on the widget and select "Replace reference with widget copy".</figcaption></figure></div>


<br>
**Widget copies**

A widget copy is a complete and independent copy of the widget configuration. Changes made to the copied widget will not affect the original widget.

- To copy a widget, right-click on the widget and select "Copy" (Ctrl+C);
- To paste the widget in another breakpoint layout, right-click on the empty space and select "Paste" (Ctrl+V).


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/copy-widget-1-ce.webp" alt="To copy a widget, right-click on the widget and select &quot;Copy&quot; (Ctrl+C);" loading="lazy"><figcaption>To copy a widget, right-click on the widget and select "Copy" (Ctrl+C);</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/copy-widget-2-ce.webp" alt="To paste the widget in another breakpoint layout, right-click on the empty space and select &quot;Paste&quot; (Ctrl+V);" loading="lazy"><figcaption>To paste the widget in another breakpoint layout, right-click on the empty space and select "Paste" (Ctrl+V);</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/copy-widget-3-ce.webp" alt="The widget is pasted. Changes made to the copied widget will not affect the original widget." loading="lazy"><figcaption>The widget is pasted. Changes made to the copied widget will not affect the original widget.</figcaption></figure></div>


## Layout settings

Click the "gear" icon opposite the breakpoint to open the layout settings.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-1-ce.webp" alt="Click the &quot;gear&quot; icon opposite the breakpoint to open the layout settings." loading="lazy"><figcaption>Click the "gear" icon opposite the breakpoint to open the layout settings.</figcaption></figure></div>


### Columns count

While editing the dashboard, specifically the size and space of your widgets, you can notice a whitish grid on a gray background.
These are columns that determine how many widgets can fit horizontally on a Dashboard.
By default, the number of columns is 24. You can increase or decrease their number. The minimum number of columns is 10. The maximum number is 1000 columns.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-columns-count-1-ce.webp" alt="While editing the Dashboard, specifically the size and space of your widgets, you can notice a whitish grid on a gray background. These are columns that determine how many widgets can fit horizontally on the dashboard;" loading="lazy"><figcaption>While editing the Dashboard, specifically the size and space of your widgets, you can notice a whitish grid on a gray background. These are columns that determine how many widgets can fit horizontally on the dashboard;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-columns-count-2-ce.webp" alt="By default, the number of columns is 24. You can increase or decrease their number. The minimum number of columns is 10. The maximum number is 1000 columns." loading="lazy"><figcaption>By default, the number of columns is 24. You can increase or decrease their number. The minimum number of columns is 10. The maximum number is 1000 columns.</figcaption></figure></div>


### Minimum layout width

By default, the minimum number of columns is 24. You can increase or decrease this number. The minimum number of columns is 10. We recommend that the value of this parameter be equal to or more than the column count.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-minimum-layout-width-1-ce.webp" alt="By default, the minimum number of columns is 24. You can increase or decrease this number. The minimum number of columns is 10. We recommend that the value of this parameter be equal to or more than the column count." loading="lazy"><figcaption>By default, the minimum number of columns is 24. You can increase or decrease this number. The minimum number of columns is 10. We recommend that the value of this parameter be equal to or more than the column count.</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-minimum-layout-width-2-ce.webp" alt="With these settings, the minimum layout width is set to 10 columns." loading="lazy"><figcaption>With these settings, the minimum layout width is set to 10 columns.</figcaption></figure></div>


### Margin between widgets

This margin type determines how much space is between widgets.
By default, the margin is set to 10. You can remove it by setting the "**Margin between widgets**" field to 0 or increasing the margin, meaning the distance between widgets. The maximum allowable margin is 50.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-margin-between-widgets-1-ce.webp" alt="This field type determines the distance between widgets;" loading="lazy"><figcaption>This field type determines the distance between widgets;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-margin-between-widgets-2-ce.webp" alt="By default, the margin is set to 10;" loading="lazy"><figcaption>By default, the margin is set to 10;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-margin-between-widgets-3-ce.webp" alt="You can decrease or increase the distance between widgets." loading="lazy"><figcaption>You can decrease or increase the distance between widgets.</figcaption></figure></div>


### Apply margin to the sides of the layout

This parameter determines whether the "Margin between widgets" value should be applied to the sides of the layout.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-apply-margin-to-sides-of-layout-1-ce.webp" alt="This parameter determines whether the &quot;Margin between widgets&quot; value should be applied to the sides of the layout;" loading="lazy"><figcaption>This parameter determines whether the "Margin between widgets" value should be applied to the sides of the layout;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-apply-margin-to-sides-of-layout-2-ce.webp" alt="There is a space between the widgets and the side of the layout;" loading="lazy"><figcaption>There is a space between the widgets and the side of the layout;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-apply-margin-to-sides-of-layout-3-ce.webp" alt="There is no space between the widgets and the side of the layout." loading="lazy"><figcaption>There is no space between the widgets and the side of the layout.</figcaption></figure></div>


### Auto fill layout height

By default, the "**Auto fill layout height**" checkbox is unchecked so that you can freely adjust the size of the widgets.
If you tick this option, all the widgets on the dashboard will fill in vertically in the space of the screen.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-auto-fill-layout-height-1-ce.webp" alt="By default, the &quot;Auto fill layout height&quot; checkbox is unchecked;" loading="lazy"><figcaption>By default, the "Auto fill layout height" checkbox is unchecked;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-auto-fill-layout-height-2-ce.webp" alt="The &quot;Auto fill layout height&quot; checkbox is unchecked so that you can freely adjust the size of the widgets;" loading="lazy"><figcaption>The "Auto fill layout height" checkbox is unchecked so that you can freely adjust the size of the widgets;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-auto-fill-layout-height-3-ce.webp" alt="If you tick this option, all widgets on the dashboard will fill the screen space vertically." loading="lazy"><figcaption>If you tick this option, all widgets on the dashboard will fill the screen space vertically.</figcaption></figure></div>


### Background color

The "Background color setting allows you to customize the color of the dashboard's background.
To change the background color, click the color in the small square on the right in the background color section.
In the popup window, select the desired color and transparency. Then click "Select". Afterward, apply the layout settings. After saving, you can see the customized background.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-background-color-1-ce.webp" alt="The &quot;Background color&quot; option allows you to customize the color that you&#39;d like to be on the dashboard&#39;s background;" loading="lazy"><figcaption>The "Background color" option allows you to customize the color that you&#39;d like to be on the dashboard&#39;s background;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-background-color-2-ce.webp" alt="To change the background color, click the color in the small square on the right in the background color section. In the popup window, select the desired color and transparency. Then click &quot;Select&quot;. Afterward, apply the layout settings;" loading="lazy"><figcaption>To change the background color, click the color in the small square on the right in the background color section. In the popup window, select the desired color and transparency. Then click "Select". Afterward, apply the layout settings;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-background-color-3-ce.webp" alt="After saving, you can see the customized background." loading="lazy"><figcaption>After saving, you can see the customized background.</figcaption></figure></div>


### Background image

This option allows you to set an image as the background of the dashboard. You can choose an image from the [Image gallery](/docs/user-guide/image-gallery/) or set a direct link.

To select an image from the gallery, click "Browse from gallery". Choose an already uploaded image or add a new one.
To more precisely adjust the position of the image, click the dropdown menu of the "**Background size mode**" section and select how exactly the image will fill the background space.
For example, let's choose "Cover" and click "Save" to see how the background has changed.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-background-image-1-ce.webp" alt="This option allows you to set an image as the background of the dashboard. You can choose an image from the Image gallery or set a direct link. To select an image from the gallery, click &quot;Browse from gallery&quot;;" loading="lazy"><figcaption>This option allows you to set an image as the background of the dashboard. You can choose an image from the Image gallery or set a direct link. To select an image from the gallery, click "Browse from gallery";</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-background-image-2-ce.webp" alt="Choose an already uploaded image or add a new one;" loading="lazy"><figcaption>Choose an already uploaded image or add a new one;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-background-image-3-ce.webp" alt="To more precisely adjust the position of the image, click the dropdown menu of the &quot;Background size mode&quot; section and select how exactly the image will fill the background space. For example, let&#39;s choose &quot;Cover&quot; and click &quot;Save&quot; to see how the background has changed." loading="lazy"><figcaption>To more precisely adjust the position of the image, click the dropdown menu of the "Background size mode" section and select how exactly the image will fill the background space. For example, let&#39;s choose "Cover" and click "Save" to see how the background has changed.</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-settings-background-image-4-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Mobile layout settings

By default, the "**Auto fill layout height**" checkbox is unchecked so that you can freely adjust the size of the widgets for your mobile device.
If you tick this option, all the widgets on the Dashboard will fill in vertically in the space of the screen.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-mobile-settings-auto-fill-layout-height-1-ce.webp" alt="By default, the &quot;Auto fill layout height&quot; checkbox is unchecked so that you can freely adjust the size of the widgets for your mobile device;" loading="lazy"><figcaption>By default, the "Auto fill layout height" checkbox is unchecked so that you can freely adjust the size of the widgets for your mobile device;</figcaption></figure><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-mobile-settings-auto-fill-layout-height-2-ce.webp" alt="If you tick &quot;Auto fill layout height&quot; option, all the widgets on the Dashboard will fill in vertically in the space of the screen." loading="lazy"><figcaption>If you tick "Auto fill layout height" option, all the widgets on the Dashboard will fill in vertically in the space of the screen.</figcaption></figure></div>


#### Mobile row height

Mobile row height determines how tall you'd like your widgets to be on your mobile device.
By default, the height is set to 70px, but you can make it smaller or larger. The minimum Mobile row height is 5px, and the maximum allowable value is 200px.


<div class="st-gallery"><figure><img src="/images/user-guide/dashboards/layouts/ce/layout-mobile-settings-auto-fill-layout-height-3-ce.webp" alt="Mobile row height determines how tall you’d like your widgets to be on your mobile device." loading="lazy"><figcaption>Mobile row height determines how tall you’d like your widgets to be on your mobile device.</figcaption></figure></div>
