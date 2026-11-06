+++
title = "SCADA dashboards"
description = "SCADA IoT dashboards using SENTIENT"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/scada.md"
+++
<table style="width:auto">
   <thead>
     <tr>
	 <td style="text-align: center"><strong><em>Available since TB Version 3.8.0</em></strong></td>
     </tr>
   </thead>
</table> 


[SCADA](https://en.wikipedia.org/wiki/SCADA) (Supervisory Control and Data Acquisition) refers to an architecture used to monitor and control various machines and manufacturing processes. 
In this system, SENTIENT serves as the supervisory computer element, gathering data from various PLCs (Programmable Logic Controllers) and RTUs (Remote Terminal Units), 
often with the assistance of the [IoT Gateway](/docs/iot-gateway/what-is-iot-gateway/) software or physical gateway devices. 
Additionally, SENTIENT offers robust [alarm](/docs/user-guide/alarms/) and [notification](/docs/user-guide/notifications/) systems, which are essential components of any IoT system.

Starting from release 3.8.0, SENTIENT introduces support for SCADA-like HMI dashboards, which we will cover in this documentation.


<div id="video">  
    <div id="video_wrapper">
        <iframe referrerpolicy="strict-origin-when-cross-origin" src="https://www.youtube.com/embed/kBMcsg7YEcQ" frameborder="0" allowfullscreen></iframe>
    </div>
</div>

## SCADA dashboard layout

A SCADA dashboard in SENTIENT provides all the functionalities of a typical platform [Dashboard](/docs/user-guide/dashboards/) with a specialized SCADA [layout](/docs/user-guide/dashboards/#layouts), 
designed to facilitate the creation of SCADA HMIs (Human-Machine Interfaces).

The SCADA dashboard typically consists of special scalable widgets known as SCADA symbols. 
Each symbol can represent the state of a physical object such as a valve, pump, motor, tank, or pipe. 
Users can also interact with these widgets to send commands to the physical objects, such as turning a pump on and off, or opening and closing a valve. 
Additionally, you can combine SCADA widgets with over 500 existing SENTIENT [widgets](/docs/user-guide/widgets/) on the same dashboard.

Here are some key features of the SCADA layout:

- **Margin**  
  In the SCADA layout, there is no margin between widgets. This intentional design ensures that pipes and other SCADA symbols always connect properly.

- **Widget appearance**  
  By default, regular widgets are placed with a transparent background and without a shadow, allowing them to blend seamlessly into the SCADA dashboard.

## Building a SCADA dashboard

To begin building a SCADA dashboard, create a new dashboard:


1. Go to the "Dashboards" page, and click on the "plus" icon located in the upper-right corner of the screen to add a new dashboard. Select "Create new dashboard" from the dropdown menu that appears. In the dialog box that opens, type in the title for the dashboard and confirm by clicking "Add";

1. Once created, the new dashboard will open automatically, allowing you to configure it immediately. Click on the "Layouts" sign in the top-left corner of the dashboard interface;

1. Then, simply change the layout from "Default" to "SCADA", then save your changes.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/add-scada-dashboard-1-ce.webp" alt="Go to the &quot;Dashboards&quot; page, and click on the &quot;plus&quot; icon located in the upper-right corner of the screen to add a new dashboard. Select &quot;Create new dashboard&quot; from the dropdown menu that appears. In the dialog box that opens, type in the title for the dashboard and confirm by clicking &quot;Add&quot;;" loading="lazy"><figcaption>Go to the "Dashboards" page, and click on the "plus" icon located in the upper-right corner of the screen to add a new dashboard. Select "Create new dashboard" from the dropdown menu that appears. In the dialog box that opens, type in the title for the dashboard and confirm by clicking "Add";</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/add-scada-dashboard-2-ce.webp" alt="Once created, the new dashboard will open automatically, allowing you to configure it immediately. Click on the &quot;Layouts&quot; sign in the top-left corner of the dashboard interface;" loading="lazy"><figcaption>Once created, the new dashboard will open automatically, allowing you to configure it immediately. Click on the "Layouts" sign in the top-left corner of the dashboard interface;</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/add-scada-dashboard-3-ce.webp" alt="Then, simply change the layout from &quot;Default&quot; to &quot;SCADA&quot;, then save your changes." loading="lazy"><figcaption>Then, simply change the layout from "Default" to "SCADA", then save your changes.</figcaption></figure></div>


### Layout settings

Layout settings determine the background configurations of the dashboard and how widgets will be arranged on it. 
Click the "gear" icon in the "Manage layouts" window. This opens a small window with layout settings.


1. Click the "gear" icon in the "Manage layouts" window;

1. This opens a small window with layout setting.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/layout-settings-1-ce.webp" alt="Click the &quot;gear&quot; icon in the &quot;Manage layouts&quot; window;" loading="lazy"><figcaption>Click the "gear" icon in the "Manage layouts" window;</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/layout-settings-2-ce.webp" alt="This opens a small window with layout setting." loading="lazy"><figcaption>This opens a small window with layout setting.</figcaption></figure></div>


Here are some key settings for the SCADA layout:

**Columns count**. The number of columns in the layout settings must be divisible by 24 (e.g., 24, 48, 72, up to 1008).
This value defines how your screen is divided into a widget placeholder matrix and determines the dashboard's granularity.
You can configure different layout settings for each layout breakpoint: xl, lg, md, sm, xs.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-columns-count-1-ce.webp" alt="The number of columns in the layout settings must be divisible by 24 (e.g., 24, 48, 72, up to 1008);" loading="lazy"><figcaption>The number of columns in the layout settings must be divisible by 24 (e.g., 24, 48, 72, up to 1008);</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-columns-count-2-ce.webp" alt="The count of columns is set to 24;" loading="lazy"><figcaption>The count of columns is set to 24;</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-columns-count-3-ce.webp" alt="The count of columns is set to 48." loading="lazy"><figcaption>The count of columns is set to 48.</figcaption></figure></div>


**Minimum layout width**. By default, the minimum number of columns is 24. You can increase or decrease this number. The minimum number of columns is 10. We recommend the value of this setting to be equal or more then *columns count* value.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-minimum-layout-width-1-ce.webp" alt="By default, the minimum number of columns is 24. You can increase or decrease this number. The minimum number of columns is 10. We recommend the value of this setting to be equal or more then columns count value;" loading="lazy"><figcaption>By default, the minimum number of columns is 24. You can increase or decrease this number. The minimum number of columns is 10. We recommend the value of this setting to be equal or more then columns count value;</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-minimum-layout-width-2-ce.webp" alt="The count of minimum columns is set to 24." loading="lazy"><figcaption>The count of minimum columns is set to 24.</figcaption></figure></div>


<br>
**Background color**. The "Background color" setting allows you to customize the color of the dashboard's background.
To change the background color, click the color in the small square on the right in the background color section.
In the popup window, select the desired color and transparency. Then click "Select". Afterwards, apply the layout settings.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-background-color-1-ce.webp" alt="To change the background color, click the color in the small square on the right in the background color section. In the popup window, select the desired color and transparency. Then click &quot;Select&quot;;" loading="lazy"><figcaption>To change the background color, click the color in the small square on the right in the background color section. In the popup window, select the desired color and transparency. Then click "Select";</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-background-color-2-ce.webp" alt="After saving the changes, you will see that the background color has changed." loading="lazy"><figcaption>After saving the changes, you will see that the background color has changed.</figcaption></figure></div>


<br>
**Background image** and **Background size mode**. This option allows you to set an image as the background of the dashboard. You can choose an image from the [Image gallery](/docs/user-guide/image-gallery/) or set a direct link.

To select an image from the gallery, click "Browse from gallery". Choose an already uploaded image or add a new one.
**Background size mode**. To adjust the positioning of the image more precisely, click the dropdown menu in the "Background size mode" section and select how exactly the image will fill the background space. 
For example, let's choose "Cover" and click "Save" to see how the background has changed.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-background-image-1-ce.webp" alt="To select an image from the gallery, click &quot;Browse from gallery&quot;;" loading="lazy"><figcaption>To select an image from the gallery, click "Browse from gallery";</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-background-image-2-ce.webp" alt="Choose an already uploaded image or add a new one;" loading="lazy"><figcaption>Choose an already uploaded image or add a new one;</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-background-image-3-ce.webp" alt="To more precisely adjust the position of the image, click the dropdown menu of the &quot;Background size mode&quot; section and select how exactly the image will fill the background space;" loading="lazy"><figcaption>To more precisely adjust the position of the image, click the dropdown menu of the "Background size mode" section and select how exactly the image will fill the background space;</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-background-image-4-ce.webp" alt="see how the background has changed." loading="lazy"><figcaption>see how the background has changed.</figcaption></figure></div>


### Multi-state dashboards

Experienced platform users know that a dashboard can contain multiple [states](/docs/user-guide/dashboards/#states).
A single dashboard can combine regular dashboard states with SCADA states. 
For instance, the main state might display a high-level overview of the SCADA system, while clicking on a particular element can open a regular dashboard state or a popup widget.

Below is a [sample dashboard](/docs/user-guide/resources/multi-state-scada-dashboard.json) that does not display real data, but you can [import](/docs/user-guide/dashboards/#import-dashboard) it into your environment to explore how navigation between states is implemented.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/multi-state-dashboards-1-ce.webp" alt="Clicking on a specific SCADA element will execute a customized action. Give it a try." loading="lazy"><figcaption>Clicking on a specific SCADA element will execute a customized action. Give it a try.</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/multi-state-dashboards-2-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/multi-state-dashboards-3-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/multi-state-dashboards-4-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## SCADA symbol

SENTIENT SCADA symbols are based on [SVG](https://en.wikipedia.org/wiki/SVG) (Scalable Vector Graphics) files. 
The use of vector graphics ensures that SCADA symbols scale seamlessly to any screen size. 
SENTIENT's engineers have extended the SVG format to make these symbols interactive.
Specifically, we define how the SVG object changes based on the properties configured by the user or the data received from the device.
We also define clickable areas of the SVG object, allowing users to configure actions that can be triggered once the symbol is added to the dashboard. 


<div class="st-callout info">


In SENTIENT version 3.9, in addition to traditional SCADA symbols, high-performance SCADA symbols have been introduced.


</div>


High-performance SCADA symbols in SENTIENT are optimized graphical elements used to display information about the status of processes and equipment in SCADA systems created on the SENTIENT platform. They are designed to enhance the efficiency of information perception and speed up decision-making by the operator.

Key features of High-performance SCADA symbols in SENTIENT:

- Simplified Design: Minimalist symbols that exclude unnecessary decorative elements. Priority is given to informativeness and readability.
- Color Coding: Main states (normal) are typically represented by neutral colors (e.g., gray). Critical states (emergencies, errors) are highlighted with bright colors such as red or yellow.
- Dynamic Changes: Symbols can change color depending on their state (e.g., valve closed/open, or pump on/off).
- Standardization: A standardized set of symbols is used for different types of devices or processes to reduce user training time.
- Compatibility: Symbols are easily adaptable to different screen sizes and device types (desktops, tablets, smartphones).


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/high-performance-scada-symbols-1-ce.webp" alt="High-performance SCADA dashboard." loading="lazy"><figcaption>High-performance SCADA dashboard.</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/high-performance-scada-symbols-2-ce.webp" alt="Traditional SCADA dashboard." loading="lazy"><figcaption>Traditional SCADA dashboard.</figcaption></figure></div>


<br>
We currently provide 100+ SCADA symbols available out of the box, with plans to increase this number to 500+ in upcoming releases. 
If you need a symbol that is not available, you are encouraged to create your own using the following [guide](/docs/user-guide/scada/scada-symbols-dev-guide/).

## SCADA symbol widget

The SCADA symbol widget is designed to place any SCADA symbol onto the dashboard. It acts as a bridge between the generic SCADA symbol and the dashboard.

The SCADA symbol widget contains five configuration blocks, which we will explain below using the 'Horizontal wheel valve' symbol as a reference:

Let's first add this widget to the dashboard:


1. While in dashboard editing mode, сlick the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the Select widgets bundle dialog box;

1. Find the "SCADA fluid system" widgets bundle and click on it;

1. Choose the "Horizontal wheel valve" widget.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/add-scada-symbol-widget-1-ce.webp" alt="While in dashboard editing mode, сlick the &quot;+ Add widget&quot; icon at the top of the screen, or (if this is your first widget on this dashboard) click a large &quot;Add new widget&quot; sign in the middle of the screen to open the Select widgets bundle dialog box;" loading="lazy"><figcaption>While in dashboard editing mode, сlick the "+ Add widget" icon at the top of the screen, or (if this is your first widget on this dashboard) click a large "Add new widget" sign in the middle of the screen to open the Select widgets bundle dialog box;</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/add-scada-symbol-widget-2-ce.webp" alt="Find the &quot;SCADA fluid system&quot; widgets bundle and click on it;" loading="lazy"><figcaption>Find the "SCADA fluid system" widgets bundle and click on it;</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/add-scada-symbol-widget-3-ce.webp" alt="Choose the &quot;Horizontal wheel valve&quot; widget." loading="lazy"><figcaption>Choose the "Horizontal wheel valve" widget.</figcaption></figure></div>


### Target entity

This points the widget to a single entity: device, asset, etc. 
It defines the entity that will be used to control the behavior of the symbol. 
You may omit the target entity parameter if interactive behavior is not required.
Experienced users may use [entity aliases](/docs/user-guide/ui/aliases/) that resolve to a single entity. 
This is particularly useful for advanced use cases, such as configuring the target entity to an asset instead of a device.

In our example, we will select the smart device that controls our valve. Typically, this device is connected via an IoT Gateway using a Modbus connector, but we will omit these details for simplicity in this guide.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-selected-target-device-1-ce.webp" alt="Specify a single entity: device, asset, etc. Omit the target entity parameter if interactive behavior is not required." loading="lazy"><figcaption>Specify a single entity: device, asset, etc. Omit the target entity parameter if interactive behavior is not required.</figcaption></figure></div>


### SCADA symbol

This points to a specific SCADA [symbol](#scada-symbol) from the library. 
In our case, we have selected the 'Horizontal wheel valve' from the library. 
Ensure you have selected 'Include system symbols' if this symbol is not visible in the library.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-symbol-device-1-ce.webp" alt="This points to a specific SCADA symbol from the library." loading="lazy"><figcaption>This points to a specific SCADA symbol from the library.</figcaption></figure></div>


### Behavior

The list of behavior parameters is specific to the chosen SCADA symbol and is entirely controlled by the symbol's author. 


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-behavior-settings-1-ce.webp" alt="The list of behavior parameters is specific to the chosen SCADA symbol and is entirely controlled by the symbol&#39;s author" loading="lazy"><figcaption>The list of behavior parameters is specific to the chosen SCADA symbol and is entirely controlled by the symbol&#39;s author</figcaption></figure></div>


<br>
There are three types of behavior parameters: "Value", "Action", and "Widget action".

- "**Value**" parameters usually control the visual representation of the symbol and may change over time based on the received value;
- "**Action**" parameters define the actions performed against the target entity when a specific event occurs;
- "**Widget action**" parameters define the actions triggered when the user clicks on the component of the SCADA symbol.

Action types to retrieve **value**:

- "**Do nothing**" action will just take the constant defined by the user.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-action-do-nothing-1-ce.webp" alt="&quot;Do nothing&quot; action will just take the constant defined by the user." loading="lazy"><figcaption>"Do nothing" action will just take the constant defined by the user.</figcaption></figure></div>


- "**Execute RPC**" action will send a command to the target device to get the value. The value is resolved once during the creation of the widget.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-action-execute-rpc-1-ce.webp" alt="&quot;Execute RPC&quot; action will send a command to the target device to get the value. The value is resolved once during the creation of the widget." loading="lazy"><figcaption>"Execute RPC" action will send a command to the target device to get the value. The value is resolved once during the creation of the widget.</figcaption></figure></div>

 

- "**Get attribute**" action will subscribe to the value of the target entity's attribute. The widget will receive updates when the attribute value changes.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-action-get-attribute-1-ce.webp" alt="&quot;Get attribute&quot; action will subscribe to the value of the target entity&#39;s attribute. The widget will receive updates when the attribute value changes." loading="lazy"><figcaption>"Get attribute" action will subscribe to the value of the target entity&#39;s attribute. The widget will receive updates when the attribute value changes.</figcaption></figure></div>


- "**Get time series**" action will subscribe to the value of the target entity's time series field. The widget will receive updates when new time series data arrives.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-action-get-time-series-1-ce.webp" alt="&quot;Get time series&quot; action will subscribe to the value of the target entity&#39;s time series field. The widget will receive updates when new time series data arrives." loading="lazy"><figcaption>"Get time series" action will subscribe to the value of the target entity&#39;s time series field. The widget will receive updates when new time series data arrives.</figcaption></figure></div>


- "**Get alarm status**" action subscribes to the alarm status field. The widget will receive updates according to the type of alarm.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-action-get-alarm-status-1-ce.webp" alt="The &quot;Get alarm status&quot; action subscribes to the alarm status field. The widget will receive updates according to the type of alarm." loading="lazy"><figcaption>The "Get alarm status" action subscribes to the alarm status field. The widget will receive updates according to the type of alarm.</figcaption></figure></div>


- "**Get dashboard state**" action will use the name of the current dashboard state. This is useful in specific cases that are not related to the state of the target device.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-action-get-dashboard-state-1-ce.webp" alt="&quot;Get dashboard state&quot; action will use the name of the current dashboard state. This is useful in specific cases that are not related to the state of the target device." loading="lazy"><figcaption>"Get dashboard state" action will use the name of the current dashboard state. This is useful in specific cases that are not related to the state of the target device.</figcaption></figure></div>


<br>
The platform supports three types of **actions** regarding the target entity:

- "**Execute RPC**" will send a command to the target device. You can define the method and parameters of the command.
  

<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-action-execute-rpc-to-target-device-1-ce.webp" alt="&quot;Execute RPC&quot; action will send a command to the target device. You can define the method and parameters of the command." loading="lazy"><figcaption>"Execute RPC" action will send a command to the target device. You can define the method and parameters of the command.</figcaption></figure></div>


    
- "**Set attribute**" will send a command to the target device. You can define the scope, key, and value of the attribute to set.
  

<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-action-set-attribute-1-ce.webp" alt="&quot;Set attribute&quot; action will send a command to the target device. You can define the scope, key, and value of the attribute to set." loading="lazy"><figcaption>"Set attribute" action will send a command to the target device. You can define the scope, key, and value of the attribute to set.</figcaption></figure></div>


 
- "**Add time series**" will add a new time series value to the target device. You can define the key and value of the new time series data.
  

<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-action-add-time-series-1-ce.webp" alt="&quot;Add time series&quot; action will add a new time series value to the target device. You can define the key and value of the new time series data." loading="lazy"><figcaption>"Add time series" action will add a new time series value to the target device. You can define the key and value of the new time series data.</figcaption></figure></div>


<br>

**Widget action** parameter "On click" defines the actions triggered when the user clicks on the component. 
In our example, the valve symbol does not have any widget action parameters, but you may explore other symbols like 'Left motor pump' for such actions. 
Possible action types are documented [here](/docs/user-guide/ui/widget-actions/#action-types).


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-action-left-motor-pump-1-ce.webp" alt="The &quot;On click&quot; action parameter defines the action that is triggered when a user clicks on the component." loading="lazy"><figcaption>The "On click" action parameter defines the action that is triggered when a user clicks on the component.</figcaption></figure></div>


<br>
As an example, we will consider the parameters of the "Horizontal Wheel Valve" symbol:

- The first parameter "Opened" controls the visual representation of the SCADA symbol "Horizontal Wheel Valve" and can dynamically change, usually based on the value of an attribute or time series data received from the device.
In the case of our valve, this parameter determines whether the valve is "Open" or "Closed";

- The second and third parameters determine which action should be executed in relation to the target object when the user interacts with the valve.
In the case of the horizontal wheel valve, there are two actions: "Open" and "Close". The "Open" action sets the value "true" for the "open" attribute, and the "Close" action sets the value "false" for the "open" attribute.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/example-of-parameters-scada-symbol-1-ce.webp" alt="The first parameter &quot;Opened&quot; controls the visual representation of the SCADA symbol &quot;Horizontal Wheel Valve&quot; and can dynamically change, usually based on the value of an attribute or time series data received from the device. In the case of our valve, this parameter determines whether the valve is &quot;Open&quot; or &quot;Closed&quot;;" loading="lazy"><figcaption>The first parameter "Opened" controls the visual representation of the SCADA symbol "Horizontal Wheel Valve" and can dynamically change, usually based on the value of an attribute or time series data received from the device. In the case of our valve, this parameter determines whether the valve is "Open" or "Closed";</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/example-of-parameters-scada-symbol-2-ce.webp" alt="The &quot;Open&quot; action sets the value &quot;true&quot; for the &quot;open&quot; attribute;" loading="lazy"><figcaption>The "Open" action sets the value "true" for the "open" attribute;</figcaption></figure><figure><img src="/images/user-guide/scada/scada-dashboards/ce/example-of-parameters-scada-symbol-3-ce.webp" alt="The &quot;Close&quot; action sets the value &quot;false&quot; for the &quot;open&quot; attribute." loading="lazy"><figcaption>The "Close" action sets the value "false" for the "open" attribute.</figcaption></figure></div>


### Appearance

There are common appearance parameters, such as symbol title and icon, available for any SCADA symbol. 
Other parameters are specific to the chosen SCADA symbol and are controlled by the symbol's author. 
In the case of our valve, you can define the color of the valve symbol in both the opened and closed states. 
You can also configure the animation of the wheel by setting the angle of rotation. 
There are several types of appearance parameters, which are intuitive for the end user. 
For more details, see the symbol development [guide](/docs/user-guide/scada/scada-symbols-dev-guide/).


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-appearance-1-ce.webp" alt="For any SCADA symbol, general appearance parameters such as the symbol title and icon are available. Other parameters are specific to the selected SCADA symbol and are controlled by the symbol&#39;s author." loading="lazy"><figcaption>For any SCADA symbol, general appearance parameters such as the symbol title and icon are available. Other parameters are specific to the selected SCADA symbol and are controlled by the symbol&#39;s author.</figcaption></figure></div>


### Card Appearance

The card appearance settings are generic for any SCADA symbol and include background (transparent by default), list of enabled card buttons, card border radius, and padding parameters.


<div class="st-gallery"><figure><img src="/images/user-guide/scada/scada-dashboards/ce/scada-card-appearance-1-ce.webp" alt="The card appearance settings are generic for any SCADA symbol and include background (transparent by default), list of enabled card buttons, card border radius, and padding parameters." loading="lazy"><figcaption>The card appearance settings are generic for any SCADA symbol and include background (transparent by default), list of enabled card buttons, card border radius, and padding parameters.</figcaption></figure></div>
