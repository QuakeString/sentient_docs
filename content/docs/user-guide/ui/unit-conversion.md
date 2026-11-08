+++
title = "Unit conversion"
description = "Unit conversion"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/unit-conversion.md"
+++


Starting from SENTIENT 4.1, widgets support automatic data conversion and unit switching based on the selected unit system. 
This is especially useful in global IoT solutions and significantly improves data interaction for users across different geographic regions where various measurement standards are used — such as the metric system (°C, km, kg) and the imperial system (°F, miles, lbs).

<br><b><font size="4">Key benefits:</font></b>

- Automatic conversion of numerical values into the appropriate units directly within the widget — no additional data processing required.
- Flexible widget configuration that eliminates the need to duplicate widgets or create separate dashboards for users with different regional unit standards.
- Support for a wide range of measurement units, allowing users to view values in the units that are most familiar and convenient to them.

<b><font size="4">Where the unit conversion feature can be applied?</font></b>

All widgets designed to display telemetry data include a unit conversion option.   
Unit conversion is supported for telemetry data, Y-axis scales, and threshold settings.

> **Note:** If a widget contains multiple telemetry keys, the unit conversion feature must be configured individually for each key.

## Enable unit conversion

Unit conversion is configured in the **unit settings** available in the **telemetry keys**, **Y-axis**, and **thresholds** configurations within the widget settings.

- Specify the **source unit** — the unit of the incoming telemetry value received from the server to ensure correct conversion to the target unit.
- Enable unit conversion by toggling the "**Enable unit conversion**" switch.
- The system will automatically suggest commonly used target units for each unit system (e.g., °C for Metric, °F for Imperial, and °C for Hybrid). However, you can override these by selecting different units from the dropdown list.

> **Note**: All available units are grouped by category (e.g., temperature, length, mass). You can only select target units from the same category as the source unit.

> **Note**: If you do not specify a unit for a particular unit system, that system will fall back to using the unit defined in the **Source unit** field.

- Click "**Apply**" to save the changes.

Once unit conversion is enabled, an icon will appear in the Unit field indicating that the feature is active.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-configuring-1-ce.webp" alt="Unit conversion is configured in the unit settings available in the telemetry keys, Y-axis, and thresholds configurations within the widget settings." loading="lazy"><figcaption>Unit conversion is configured in the <b>unit settings</b> available in the <b>telemetry keys</b>, <b>Y-axis</b>, and <b>thresholds</b> configurations within the widget settings.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-configuring-2-ce.webp" alt="Specify the source unit — the unit of the incoming telemetry value received from the server to ensure correct conversion to the target unit." loading="lazy"><figcaption>Specify the <b>source unit</b> — the unit of the incoming telemetry value received from the server to ensure correct conversion to the target unit.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-configuring-3-ce.webp" alt="Enable unit conversion by toggling the &quot;Enable unit conversion&quot; switch. The system will automatically suggest commonly used target units for each unit system (e.g., °C for Metric, °F for Imperial, and °C for Hybrid). However, you can override these by selecting different units from the dropdown list. After, click &quot;Apply&quot; to save the changes." loading="lazy"><figcaption>Enable unit conversion by toggling the "Enable unit conversion" switch. The system will automatically suggest commonly used target units for each unit system (e.g., °C for Metric, °F for Imperial, and °C for Hybrid). However, you can override these by selecting different units from the dropdown list. After, click "<b>Apply</b>" to save the changes.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-configuring-4-ce.webp" alt="Once unit conversion is enabled, an icon will appear in the Unit field indicating that the feature is active." loading="lazy"><figcaption>Once unit conversion is enabled, an icon will appear in the Unit field indicating that the feature is active.</figcaption></figure></div>


### Range color settings

**Range color settings** use the **original telemetry value** received from the server in its source **units** — before any unit conversion is applied.

For example, if your device sends a temperature value of **22 °C** and unit conversion is enabled, the widget may display it as **71 °F**. 
However, the **range logic still uses the original 22 °C** to determine the color.

So if you&#39;ve defined a green range from **18 to 24 °C**, then any temperature readings within that range will be shown in green — regardless of whether it&#39;s displayed as 22 °C or 71 °F.

This ensures that **range coloring remains consistent**, even when switching between unit systems.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/unit-conversion/range-color-settings-1-ce.webp" alt="Range color settings use the original telemetry value received from the server in its source units — before any unit conversion is applied." loading="lazy"><figcaption>Range color settings use the original telemetry value received from the server in its source units — before any unit conversion is applied.</figcaption></figure></div>


## Changing the unit system

To change the unit system used in your SENTIENT account:
- Click the **three-dot icon** in the top-right corner of the screen and select "**Account**".
- In the **Profile** settings, choose the desired unit system from the dropdown list:
  - **Auto** - Automatically determines the appropriate unit system based on the user&#39;s browser locale or regional settings.
  - **Metric** - The most widely used system globally, based on units like meter (m), kilogram (kg), second (s), etc.
  - **Imperial** - Commonly used in the USA, based on units such as inches (in), feet (ft), miles (m), pounds (lb), gallons (gal), etc.
  - **Hybrid** - A mixed measurement system, typically used in the United Kingdom. Often blends metric and imperial units depending on the context. For example: miles (mi) for distance, Celsius (°C) for temperature, kilograms (kg) or stones (st) for body weight.
- Apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/unit-conversion/changing-unit-system-1-ce.webp" alt="Click the three-dot icon in the top-right corner of the screen and select &quot;Account&quot;." loading="lazy"><figcaption>Click the three-dot icon in the top-right corner of the screen and select "<b>Account</b>".</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/unit-conversion/changing-unit-system-2-ce.webp" alt="In the Profile settings, choose the desired unit system from the dropdown list. Then, apply changes." loading="lazy"><figcaption>In the <b>Profile</b> settings, choose the desired unit system from the dropdown list. Then, apply changes.</figcaption></figure></div>


## Example

Let&#39;s walk through configuring the unit conversion feature using the **Temperature & Humidity dashboard** as an example.   
This dashboard contains widgets that display the **temperature** in degrees Celsius (**°C**) and **humidity** in percentage (**%**).


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-1-ce.webp" alt="For this guide, we will create a new device called Tracker1, which receives longitude, latitude, speed, circle radius, status, and polygon coordinates as telemetry using an emulator written in JavaScript." loading="lazy"><figcaption>For this guide, we will create a new device called Tracker1, which receives longitude, latitude, speed, circle radius, status, and polygon coordinates as telemetry using an emulator written in JavaScript.</figcaption></figure></div>


We will apply the **unit conversion feature** to the **temperature telemetry value**, the **Y-axis of the temperature chart**, **and the temperature threshold**.
The **humidity** value will remain unchanged, as the unit of measurement for humidity is **percentage (%)**, regardless of the selected **unit system**.

<b><font size="3">Step 1: Edit the Chart widget</font></b>

Switch to edit mode for the "**Temperature and Humidity history**" chart widget.

First, configure the unit conversion for the "**temperature**" telemetry key:
- Click on the "**Units**" row in the "**temperature**" key field. You&#39;ll see that the **source unit** is already set to **Celsius** (°C), which is exactly what we need.
- To enable conversion, simply toggle on the "**Enable unit conversion**" option and specify the target unit for each unit system (e.g., °F for Imperial, °C for Metric and Hybrid). 
- Click "**Apply**".


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-2-ce.webp" alt="Switch to edit mode for the “Temperature and Humidity history” chart widget. First, configure the unit conversion for the &quot;temperature&quot; telemetry key: Click on the &quot;Units&quot; row in the &quot;temperature&quot; key field." loading="lazy"><figcaption>Switch to edit mode for the “Temperature and Humidity history” chart widget. First, configure the unit conversion for the "temperature" telemetry key: Click on the "Units" row in the "temperature" key field.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-3-ce.webp" alt="The source unit is already set to Celsius (°C), which is exactly what we need. To enable conversion, simply toggle on the “Enable unit conversion” option and specify the target unit for each unit system (e.g., °F for Imperial, °C for Metric and Hybrid). Then, click &quot;Apply&quot;." loading="lazy"><figcaption>The source unit is already set to Celsius (°C), which is exactly what we need. To enable conversion, simply toggle on the “Enable unit conversion” option and specify the target unit for each unit system (e.g., °F for Imperial, °C for Metric and Hybrid). Then, click "Apply".</figcaption></figure></div>


Repeat the same steps to convert temperature values for the **Y-axis** and the **threshold** — enable unit conversion and specify the target units for each measurement system.
After that, apply all changes.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-4-ce.webp" alt="Repeat the same steps to convert temperature values for the Y-axis — enable unit conversion and specify the target units for each measurement system. Click &quot;Apply&quot;." loading="lazy"><figcaption>Repeat the same steps to convert temperature values for the Y-axis — enable unit conversion and specify the target units for each measurement system. Click "Apply".</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-5-ce.webp" alt="For the threshold, also enable unit conversion and specify the target units for each unit system. Then, apply all changes." loading="lazy"><figcaption>For the threshold, also enable unit conversion and specify the target units for each unit system. Then, apply all changes.</figcaption></figure></div>


<b><font size="3">Step 2: Edit the Temperature Card widget</font></b>

Switch to edit mode for the "**Temperature**" card widget.

In the "**Unit settings**" dialog, enable unit conversion and provide the appropriate units for each unit system, just like before. 
Apply your changes and save the dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-6-ce.webp" alt="Switch to edit mode for the &quot;Temperature&quot; card widget." loading="lazy"><figcaption>Switch to edit mode for the "Temperature" card widget.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-7-ce.webp" alt="In the &quot;Unit settings&quot; dialog, enable unit conversion and provide the appropriate units for each unit system, just like before. Apply your changes and save the dashboard." loading="lazy"><figcaption>In the "Unit settings" dialog, enable unit conversion and provide the appropriate units for each unit system, just like before. Apply your changes and save the dashboard.</figcaption></figure></div>


Since our current unit system is set to **Metric**, temperature values are shown in Celsius (**°C**).


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-8-ce.webp" alt="Since our current unit system is set to Metric, temperature values are shown in Celsius (°C)." loading="lazy"><figcaption>Since our current unit system is set to <b>Metric</b>, temperature values are shown in Celsius (<b>°C</b>).</figcaption></figure></div>


<b><font size="3">Step 3: Changing the unit system</font></b>

To see the unit conversion in action, change your unit system to **Imperial**. 
To do this, go to your **Account** settings, find the "**Unit system**" dropdown, and select **Imperial**.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-9-ce.webp" alt="Click the three-dot icon in the top-right corner of the screen and select &quot;Account&quot;." loading="lazy"><figcaption>Click the three-dot icon in the top-right corner of the screen and select "<b>Account</b>".</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-10-ce.webp" alt="In the Profile settings, choose the Imperial unit system from the dropdown list. Then, apply changes." loading="lazy"><figcaption>In the <b>Profile</b> settings, choose the <b>Imperial</b> unit system from the dropdown list. Then, apply changes.</figcaption></figure></div>


Return to the dashboard — you will now see that the temperature value, Y-axis labels, and threshold have been converted from Celsius to Fahrenheit according to the selected unit system.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/unit-conversion/unit-conversion-example-11-ce.webp" alt="Return to the dashboard — you will now see that the temperature value, Y-axis labels, and threshold have been converted from Celsius to Fahrenheit according to the selected unit system." loading="lazy"><figcaption>Return to the dashboard — you will now see that the temperature value, Y-axis labels, and threshold have been converted from Celsius to Fahrenheit according to the selected unit system.</figcaption></figure></div>
