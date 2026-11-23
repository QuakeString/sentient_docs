+++
title = "Widget actions"
description = "SENTIENT dashboard widget actions"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/widget-actions.md"
+++
Actions feature can be treated as navigation among [dashboard's states](/docs/user-guide/dashboards/#states) or between different [dashboards](/docs/user-guide/dashboards/).
Actions allow quickly and easily configuring the transition to created state, transferring to other dashboards, or even updating the dashboard you are in. 
Depending on the widget, the action sources differ. However, the type of action you are able to choose will be the same for all widgets.
Actions can be configured both when editing and creating the required widget.

In this guide, we will configure actions in the editing mode using the Entities table widget as an example. Please, [learn here](/docs/getting-started-guides/helloworld/#step-32-add-an-entities-table-widget) how to add an Entity table widget to your dashboard.

To fully understand how to use Actions, you have to add a State to your dashboard. [You can find information on how to do this here](/docs/user-guide/dashboards/#states).

## Add action

Let&#39;s add your first action. In this step, we will outline only the general steps without going into the details of each setting. Examples of using each  [type of action](#action-types) and [action source](#action-sources) will be covered later in the guide for better understanding.

Most widgets offer two configuration options: *basic* and *advanced*. Accordingly, the process of adding actions differs slightly between these modes. Let's explore both:

If you&#39;re using the *basic* widget configuration:

- Enter the editing mode of the widget to which you want to add an action, scroll down and find the "Actions" menu item;
- Click the "Add action" button (once you have created one or more actions, the "Add actions" button will change to the `+` icon).
  The "Actions" window will open. Right now, it's empty, but later it will display all created actions;
- Click the 'plus' icon in the top right corner of the screen to open a new "Add action" window. Here you must configure a new action by entering a name, specifying the action source, and selecting the action type. Further action configuration will depend on the selected action type. Then, click "Add" to proceed;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save";
- Click "Apply" to save the widget settings;
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-2-ce.webp" alt="Enter dashboard edit mode and click &quot;Edit widget&quot; icon to enter the editing mode of the widget;" loading="lazy"><figcaption>Enter dashboard edit mode and click "Edit widget" icon to enter the editing mode of the widget;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-3-ce.webp" alt="Scroll down and find the &quot;Actions&quot; menu item. Click the &quot;Add action&quot; button (once you have created one or more actions, the &quot;Add actions&quot; button will change to the &quot;plus&quot; icon);" loading="lazy"><figcaption>Scroll down and find the "Actions" menu item. Click the "Add action" button (once you have created one or more actions, the "Add actions" button will change to the "plus" icon);</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-4-ce.webp" alt="The &quot;Actions&quot; window will open. Right now, it&#39;s empty, but later it will display all created actions. Click the &quot;plus&quot; icon in the top right corner of the screen to open a new &quot;Add action&quot; window." loading="lazy"><figcaption>The "Actions" window will open. Right now, it&#39;s empty, but later it will display all created actions. Click the "plus" icon in the top right corner of the screen to open a new "Add action" window.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-5-ce.webp" alt="Click the &#39;plus&#39; icon in the top right corner of the screen to open a new &quot;Add action&quot; window. Here you must configure a new action by entering a name, specifying the action source, and selecting the action type. Further action configuration will depend on the selected action type. Then, click &quot;Add&quot; to proceed;" loading="lazy"><figcaption>Click the &#39;plus&#39; icon in the top right corner of the screen to open a new "Add action" window. Here you must configure a new action by entering a name, specifying the action source, and selecting the action type. Further action configuration will depend on the selected action type. Then, click "Add" to proceed;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-6-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action, so you can double-check the action source, icon, and action type. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action, so you can double-check the action source, icon, and action type. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-7-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-8-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


If you&#39;re using the *advanced* widget settings:

- Enter the widget editing mode, and navigate to the "Actions" tab. Currently, it is empty, but later all created actions will be displayed here;
- Click the "plus" icon in the top right corner of the screen to open a new "Add action" window. Here you must configure a new action by entering a name, specifying the action source, and selecting the action type. Further action configuration will depend on the selected action type. Then, click "Add" to proceed;
- Now, you can see the configured action, so you can double-check the action source, icon, and action type. Click "Save";
- Click "Apply" to save the widget settings;
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-2-ce.webp" alt="Enter dashboard edit mode and click &quot;Edit widget&quot; icon to enter the editing mode of the widget;" loading="lazy"><figcaption>Enter dashboard edit mode and click "Edit widget" icon to enter the editing mode of the widget;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-9-ce.webp" alt="Navigate to the &quot;Actions&quot; tab. Currently, it is empty, but later all created actions will be displayed here. Click &quot;plus&quot; icon to open an &quot;Add action&quot; window;" loading="lazy"><figcaption>Navigate to the "Actions" tab. Currently, it is empty, but later all created actions will be displayed here. Click "plus" icon to open an "Add action" window;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-10-ce.webp" alt="Here you must configure a new action by entering a name, specifying the action source, and selecting the action type. Further action configuration will depend on the selected action type. Then, click &quot;Add&quot; to proceed;" loading="lazy"><figcaption>Here you must configure a new action by entering a name, specifying the action source, and selecting the action type. Further action configuration will depend on the selected action type. Then, click "Add" to proceed;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-11-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/add-action-12-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


Now, you can use the action. This can involve clicking on a separate button, the widget title, an individual row of entity, etc.

## Action types

The types of action define the specific action that will be taken.
There are seven action types that are applicable to all widgets:
- **Navigate to new dashboard state** - transfers you to the specified state within the current dashboard;
- **Update current dashboard state** - updates the dashboard that you are currently on;
- **Navigate to other dashboard** - transfers you to a specified dashboard;
- **Custom action** - allows manual configuration of a function for an individual action on your widget;
- **Custom action (with HTML template)** - allows manual entry of a function within an existing HTML template;
- **Mobile action** - allows the use of various mobile device functions such as taking photos, scanning QR codes, getting device location, making phone calls and so on;
- **Open URL** - allows you to go to any resource represented by a URL.

There is also a special action type available exclusively for [Map widgets](/docs/user-guide/widgets/map-widgets/):
- **Place map item** — allows you to create and place a new entity directly on the map widget in just a few clicks.

Let&#39;s consider each of these types of actions separately.

### Navigate to new dashboard state

States are so-called levels that allow you to navigate between different devices, assets, and widget objects to see the information you need in more detail.
When choosing the _Navigate to new dashboard state_ action type, you will be transferred to the previously created state of your choice.

We assume that you have already added [a new state](/docs/user-guide/dashboards/#states) to the dashboard and familiarized yourself with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter edit widget mode and open "Add action" window;
- As an example for this manual, select "[Action cell button](#action-cell-button)" action source;
- Input a name for the action and select an icon that will represent a button. With this icon, action will be performed;
- Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu;
- After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously [created state](/docs/user-guide/dashboards/#states) you'd like to be transitioned to;
- When the desired state has been selected, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings. 
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-new-dashboard-state-1-ce.webp" alt="As an example for this manual, select &quot;Action cell button&quot; as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select a &quot;Navigate to new dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>As an example for this manual, select "Action cell button" as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-new-dashboard-state-2-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-new-dashboard-state-3-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-new-dashboard-state-4-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


After saving your changes, you'll see an action icon next to each entity. Click on any of them. You will be transferred to the state specified in the action.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-new-dashboard-state-5-ce.webp" alt="After saving your changes, you&#39;ll see an action icon next to each entity. Click on any of them;" loading="lazy"><figcaption>After saving your changes, you&#39;ll see an action icon next to each entity. Click on any of them;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-new-dashboard-state-6-ce.webp" alt="You will be transferred to the state specified in the action." loading="lazy"><figcaption>You will be transferred to the state specified in the action.</figcaption></figure></div>


#### Open new dashboard state in a separate dialog or in a popup window

There are times when it doesn't make sense to move to a separate dashboard state to view the details of a widget, and you just want to open it on the same dashboard page.
For these situations, there is an _Dashboard state display option_ feature that allows opening another [state](/docs/user-guide/dashboards/#states) on the same page in a separate dialog box or in a popup window.  

In the action settings, select the desired dashboard state display option and make additional window settings such as show/hide dashboard toolbar, popup window width and height, etc.

As an example, consider displaying the new dashboard state in a separate dialog window:

- Select an "Open in separate dialog" option in the "Dashboard state display option" field;
- By default, the checkbox "Hide dashboard toolbar in dialog" is ticked. If you need to see a toolbar in the dialog window, you should uncheck it. The toolbar displays entities, time window, dashboard export button, and expand to a fullscreen button;
- It is optional to adjust a dialog width and height in percents. Width is relative to viewport height, and height is relative to width correspondingly;
- When the action has been configured, save all changes.

To perform an action and open a dialog window with the new state, click an action button next to any entity.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-new-dashboard-state-7-ce.webp" alt="To open the state in a separate dialog, select the &quot;Open in separate dialog&quot; option in the &quot;Dashboard state display option&quot; field in the action settings;" loading="lazy"><figcaption>To open the state in a separate dialog, select the "Open in separate dialog" option in the "Dashboard state display option" field in the action settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-new-dashboard-state-8-ce.webp" alt="By default, the checkbox &quot;Hide dashboard toolbar in dialog&quot; is ticked. If you need to see a toolbar in the dialog window, you should uncheck it. The toolbar displays entities, time window, dashboard export button, and expand to a fullscreen button. It is optional to adjust a dialog width and height in percents. Width is relative to viewport height, and height is relative to width correspondingly. When the action has been configured, save all changes;" loading="lazy"><figcaption>By default, the checkbox "Hide dashboard toolbar in dialog" is ticked. If you need to see a toolbar in the dialog window, you should uncheck it. The toolbar displays entities, time window, dashboard export button, and expand to a fullscreen button. It is optional to adjust a dialog width and height in percents. Width is relative to viewport height, and height is relative to width correspondingly. When the action has been configured, save all changes;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-new-dashboard-state-9-ce.webp" alt="Click the action icon next to the name of any entity again;" loading="lazy"><figcaption>Click the action icon next to the name of any entity again;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-new-dashboard-state-10-ce.webp" alt="A separate dialog box will open with details about the selected device." loading="lazy"><figcaption>A separate dialog box will open with details about the selected device.</figcaption></figure></div>


### Update current dashboard state

This action type allows updating a dashboard that you are currently on.
While using a dashboard, you can view detailed information about a specific device/asset in real-time.
The most common use of this action type is through Chart widgets where you can see the details more accurately.

For this example, in addition to the "Entities table" widget, you need to add another widget to your dashboard - "Timeseries Line Chart". As a data source, specify the [asset type "Entity from dashboard state"](/docs/user-guide/ui/aliases/#entity-from-dashboard-state):


1. Enter edit mode of the dashboard and click the "Add new widget" button at the top of the screen;

1. Find the "Charts" widget bundle and click on it;

1. Select the "Time series chart" widget;

1. Navigate to the "Entity alias" tab in the "Datasource" section. Enter the desirable alias name in the "Entity alias" field and click the "Create a new one!" button;

1. Select the "Entity from dashboard state" from the "Filter type" field and click "Add";

1. Replace the label of the "temperature" key with <b>${entityName}</b>. Then, click "Add" to add new widget on the dashboard;

1. Drag the "Time series chart" widget to a free space and resize it.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-1-ce.webp" alt="Enter edit mode of the dashboard and click the &quot;Add new widget&quot; button at the top of the screen;" loading="lazy"><figcaption>Enter edit mode of the dashboard and click the "Add new widget" button at the top of the screen;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-2-ce.webp" alt="Find the &quot;Charts&quot; widget bundle and click on it;" loading="lazy"><figcaption>Find the "Charts" widget bundle and click on it;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-3-ce.webp" alt="Select the &quot;Time series chart&quot; widget;" loading="lazy"><figcaption>Select the "Time series chart" widget;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-4-ce.webp" alt="Navigate to the &quot;Entity alias&quot; tab in the &quot;Datasource&quot; section. Enter the desirable alias name in the &quot;Entity alias&quot; field and click the &quot;Create a new one!&quot; button;" loading="lazy"><figcaption>Navigate to the "Entity alias" tab in the "Datasource" section. Enter the desirable alias name in the "Entity alias" field and click the "Create a new one!" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-5-ce.webp" alt="Select the &quot;Entity from dashboard state&quot; from the &quot;Filter type&quot; field and click &quot;Add&quot;;" loading="lazy"><figcaption>Select the "Entity from dashboard state" from the "Filter type" field and click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-6-ce.webp" alt="Replace the label of the &quot;temperature&quot; key with ${entityName}. Then, click &quot;Add&quot; to add new widget on the dashboard;" loading="lazy"><figcaption>Replace the label of the "temperature" key with <b>${entityName}</b>. Then, click "Add" to add new widget on the dashboard;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-7-ce.webp" alt="Drag the &quot;Time series chart&quot; widget to a free space and resize it." loading="lazy"><figcaption>Drag the "Time series chart" widget to a free space and resize it.</figcaption></figure></div>


Now let's add an action with the type "Update current dashboard state" for the "Entities table" widget.
We assume that you are already familiar with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter edit widget mode and open "Add action" window;
- As an example for this manual, select "[Action cell button](#action-cell-button)" action source;
- Input a name for the action and select an icon that will represent a button. With this icon, action will be performed;
- Select an "Update current dashboard state" action type from the "Action" drop-down menu;
- Click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings.
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-8-ce.webp" alt="Select the &quot;Action cell button&quot; as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select an &quot;Update current dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. Then, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select the "Action cell button" as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select an "Update current dashboard state" action type from the "Action" drop-down menu. Then, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-9-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-10-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-11-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


After saving changes, you will see icons opposite the entity names in the "Entities table" widget. Clicking on any of these icons will update the entity details, and they will be shown on the "Timeseries Line Chart" widget on the current dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-12-ce.webp" alt="After saving changes, you will see icons opposite the entity names in the &quot;Entities table&quot; widget. Clicking on any of these icons will update the entity details, and they will be shown on the &quot;Time series chart&quot; widget on the current dashboard." loading="lazy"><figcaption>After saving changes, you will see icons opposite the entity names in the "Entities table" widget. Clicking on any of these icons will update the entity details, and they will be shown on the "Time series chart" widget on the current dashboard.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/update-current-dashboard-state-13-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Navigate to other dashboard

This type of action transfers you to a previously created dashboard of your choice.

We assume that you are already familiar with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter edit widget mode and open "Add action" window;
- As an example for this manual, select "[Widget header button](#widget-header-button)" action source;
- Input a name for the action and select an icon that will represent a button. With this icon, action will be performed;
- Select a "Navigate to other dashboard" action type from the "Action" drop-down menu;
- After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a dashboard you'd like to be transitioned to. Note that you can also navigate to an existing state of the selected dashboard;
- When the desired dashboard has been selected, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings;
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.

After saving the changes, you can see an icon in the upper right part of the widget. Click this icon. You will be transferred to the previously selected dashboard (or chosen state in that dashboard).


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-other-dashboard-1-ce.webp" alt="As an example for this manual, select &quot;Widget header button&quot; as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select a &quot;Navigate to other dashboard&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a dashboard you&#39;d like to be transitioned to. Note that you can also navigate to an existing state of the selected dashboard. When the desired dashboard has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>As an example for this manual, select "Widget header button" as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select a "Navigate to other dashboard" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a dashboard you&#39;d like to be transitioned to. Note that you can also navigate to an existing state of the selected dashboard. When the desired dashboard has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-other-dashboard-2-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-other-dashboard-3-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-other-dashboard-4-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page;" loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-other-dashboard-5-ce.webp" alt="After saving the changes, you can see an icon in the upper right part of the widget. Click this icon;" loading="lazy"><figcaption>After saving the changes, you can see an icon in the upper right part of the widget. Click this icon;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/navigate-to-other-dashboard-6-ce.webp" alt="You will be transferred to the previously selected dashboard (or chosen state in that dashboard)." loading="lazy"><figcaption>You will be transferred to the previously selected dashboard (or chosen state in that dashboard).</figcaption></figure></div>


### Custom action

A Custom action allows manually configuring a function that can be used to add an individual action to your widget (for example deleting listed devices/assets).
To configure a custom action with a function (with an example of a device deletion):

We assume that you are already familiar with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter edit widget mode and open "Add action" window;
- As an example for this manual, select "[Action cell button](#action-cell-button)" action source;
- Input a name for the action and select an icon that will represent an action button. With this icon, action will be performed;
- Select a "Custom action" action type from the "Action" drop-down menu;
- After choosing a Custom action type, a field for inputting a function will appear;
- Enter your custom function there. An example in this manual is an action that adds the ability to delete devices right from the table (you will find an example of this function below);

<details>
<summary>
<b>An example of the function for a device deletion (click to expand):</b>
</summary>

<figure class="highlight"><pre><code class="language-ruby" data-lang="ruby"><span class="n">let</span> <span class="vg">$injector</span> <span class="o">=</span> <span class="n">widgetContext</span><span class="o">.</span><span class="vg">$scope</span><span class="o">.</span><span class="vg">$injector</span><span class="p">;</span>
<span class="n">let</span> <span class="n">dialogs</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'dialogs'</span><span class="p">));</span>
<span class="n">let</span> <span class="n">deviceService</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'deviceService'</span><span class="p">));</span>

<span class="n">openDeleteDeviceDialog</span><span class="p">();</span>

<span class="n">function</span> <span class="n">openDeleteDeviceDialog</span><span class="p">()</span> <span class="p">{</span>
    <span class="n">let</span> <span class="n">title</span> <span class="o">=</span> <span class="s2">"Are you sure you want to delete the device "</span> <span class="o">+</span> <span class="n">entityName</span> <span class="o">+</span> <span class="s2">"?"</span><span class="p">;</span>
    <span class="n">let</span> <span class="n">content</span> <span class="o">=</span> <span class="s2">"Be careful, after the confirmation, the device and all related data will become unrecoverable!"</span><span class="p">;</span>
    <span class="n">dialogs</span><span class="p">.</span><span class="nf">confirm</span><span class="p">(</span><span class="n">title</span><span class="p">,</span> <span class="n">content</span><span class="p">,</span> <span class="s1">'Cancel'</span><span class="p">,</span> <span class="s1">'Delete'</span><span class="p">).</span><span class="nf">subscribe</span><span class="p">(</span>
        <span class="n">function</span><span class="p">(</span><span class="n">result</span><span class="p">)</span> <span class="p">{</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">result</span><span class="p">)</span> <span class="p">{</span>
                <span class="n">deleteDevice</span><span class="p">();</span>
            <span class="p">}</span>
        <span class="p">}</span>
    <span class="p">);</span>
<span class="p">}</span>

<span class="n">function</span> <span class="n">deleteDevice</span><span class="p">()</span> <span class="p">{</span>
    <span class="n">deviceService</span><span class="p">.</span><span class="nf">deleteDevice</span><span class="p">(</span><span class="n">entityId</span><span class="p">.</span><span class="nf">id</span><span class="p">).</span><span class="nf">subscribe</span><span class="p">(</span>
        <span class="n">function</span><span class="p">()</span> <span class="p">{</span>
            <span class="n">widgetContext</span><span class="p">.</span><span class="nf">updateAliases</span><span class="p">();</span>
        <span class="p">}</span>
    <span class="p">);</span>
<span class="p">}</span></code></pre></figure>

</details>

- After input function, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings;
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-1-ce.webp" alt="Select the &quot;Action cell button&quot; as the action source. Input a name for the action and select an icon that will represent an action button. With this icon, action will be performed. Select an &quot;Custom action&quot; action type from the &quot;Action&quot; drop-down menu. After choosing a &quot;Custom action&quot; type, a field for inputting a function will appear. Enter your custom function there. Then, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select the "Action cell button" as the action source. Input a name for the action and select an icon that will represent an action button. With this icon, action will be performed. Select an "Custom action" action type from the "Action" drop-down menu. After choosing a "Custom action" type, a field for inputting a function will appear. Enter your custom function there. Then, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-2-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-3-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-4-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page;" loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page;</figcaption></figure></div>


After saving the changes, you will see an action button next to the entity names in the "Entities Table" widget.
Clicking on one of them will perform the action of deleting the corresponding object.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-5-ce.webp" alt="After saving the changes, you will see an action button next to the entity names in the &quot;Entities table&quot; widget. Clicking on one of them will perform the action of deleting the corresponding object. Try removing one of the devices;" loading="lazy"><figcaption>After saving the changes, you will see an action button next to the entity names in the "Entities table" widget. Clicking on one of them will perform the action of deleting the corresponding object. Try removing one of the devices;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-6-ce.webp" alt="Confirm deleting the device in the dialog box;" loading="lazy"><figcaption>Confirm deleting the device in the dialog box;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-7-ce.webp" alt="Confirm the deletion of the device in the dialog box" loading="lazy"><figcaption>Confirm the deletion of the device in the dialog box</figcaption></figure></div>


### Custom action (with HTML template)

A Custom action with an HTML template allows manually entering a function in an existing HTML template (for example creating dialog windows with an opportunity to create or edit listed devices/assets).
After choosing a Custom action type (with HTML template), four tabs appear for setting up the action:

- "_Resources_" tab is used to specify external JavaScript/CSS resources used by the widget;
- "_CSS_" tab contains custom action specific CSS style definitions;
- "_HTML_" tab contains custom action HTML code;
- "_JavaScript_" tab contains JS code of your custom action.

In this example, we will add two action buttons. In the upper right corner of the widget there will be located action button for adding new entities. The second action will be responsible for the buttons next to the entity names for editing these entities.

Let's start with the action button for adding new entities. We assume that you have already completed the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter edit widget mode and open "Add action" window;
- As an example for this manual, select "[Widget header button](#widget-header-button)" action source;
- Input a name for the action and select an icon that will represent an action button. With this icon, action will be performed;
- Select a "Custom action (with HTML template)" action type from the "Action" drop-down menu;
- In the tabs that appear, select "_JavaScript_" tab. Enter a JavaScript function for your custom action. In this example, we use a function that adds the ability to create a new entity (you will find an example of this function below);

<details>

<summary>
<b>Example of a JavaScript function that adds the ability to add a device or an asset (click to expand):</b>
</summary>

<figure class="highlight"><pre><code class="language-ruby" data-lang="ruby"><span class="n">let</span> <span class="vg">$injector</span> <span class="o">=</span> <span class="n">widgetContext</span><span class="o">.</span><span class="vg">$scope</span><span class="o">.</span><span class="vg">$injector</span><span class="p">;</span>
<span class="n">let</span> <span class="n">customDialog</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'customDialog'</span><span class="p">));</span>
<span class="n">let</span> <span class="n">assetService</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'assetService'</span><span class="p">));</span>
<span class="n">let</span> <span class="n">deviceService</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'deviceService'</span><span class="p">));</span>
<span class="n">let</span> <span class="n">attributeService</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'attributeService'</span><span class="p">));</span>
<span class="n">let</span> <span class="n">entityRelationService</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'entityRelationService'</span><span class="p">));</span>

<span class="n">openAddEntityDialog</span><span class="p">();</span>

<span class="n">function</span> <span class="n">openAddEntityDialog</span><span class="p">()</span> <span class="p">{</span>
<span class="n">customDialog</span><span class="p">.</span><span class="nf">customDialog</span><span class="p">(</span><span class="n">htmlTemplate</span><span class="p">,</span> <span class="no">AddEntityDialogController</span><span class="p">).</span><span class="nf">subscribe</span><span class="p">();</span>
<span class="p">}</span>

<span class="n">function</span> <span class="no">AddEntityDialogController</span><span class="p">(</span><span class="n">instance</span><span class="p">)</span> <span class="p">{</span>
<span class="n">let</span> <span class="n">vm</span> <span class="o">=</span> <span class="n">instance</span><span class="p">;</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">allowedEntityTypes</span> <span class="o">=</span> <span class="p">[</span><span class="s1">'ASSET'</span><span class="p">,</span> <span class="s1">'DEVICE'</span><span class="p">];</span>
    <span class="n">vm</span><span class="p">.</span><span class="nf">entitySearchDirection</span> <span class="o">=</span> <span class="p">{</span>
        <span class="ss">from: </span><span class="s2">"FROM"</span><span class="p">,</span>
        <span class="ss">to: </span><span class="s2">"TO"</span>
    <span class="p">}</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">addEntityFormGroup</span> <span class="o">=</span> <span class="n">vm</span><span class="p">.</span><span class="nf">fb</span><span class="p">.</span><span class="nf">group</span><span class="p">({</span>
     <span class="ss">entityName: </span><span class="p">[</span><span class="s1">''</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]],</span>
     <span class="ss">entityType: </span><span class="p">[</span><span class="s1">'DEVICE'</span><span class="p">],</span>
     <span class="ss">entityLabel: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
     <span class="ss">type: </span><span class="p">[</span><span class="s1">''</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]],</span>
     <span class="ss">attributes: </span><span class="n">vm</span><span class="p">.</span><span class="nf">fb</span><span class="p">.</span><span class="nf">group</span><span class="p">({</span>
         <span class="ss">latitude: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
         <span class="ss">longitude: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
         <span class="ss">address: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
         <span class="ss">owner: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
         <span class="ss">number: </span><span class="p">[</span><span class="n">null</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">pattern</span><span class="p">(</span><span class="sr">/^-?[0-9]+$/</span><span class="p">)]],</span>
         <span class="ss">booleanValue: </span><span class="p">[</span><span class="n">null</span><span class="p">]</span>
     <span class="p">}),</span>
     <span class="ss">relations: </span><span class="n">vm</span><span class="p">.</span><span class="nf">fb</span><span class="p">.</span><span class="nf">array</span><span class="p">([])</span>
    <span class="p">});</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">cancel</span> <span class="o">=</span> <span class="n">function</span><span class="p">()</span> <span class="p">{</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">dialogRef</span><span class="p">.</span><span class="nf">close</span><span class="p">(</span><span class="n">null</span><span class="p">);</span>
    <span class="p">};</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">relations</span> <span class="o">=</span> <span class="n">function</span><span class="p">()</span> <span class="p">{</span>
        <span class="k">return</span> <span class="n">vm</span><span class="p">.</span><span class="nf">addEntityFormGroup</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'relations'</span><span class="p">);</span>
    <span class="p">};</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">addRelation</span> <span class="o">=</span> <span class="n">function</span><span class="p">()</span> <span class="p">{</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">relations</span><span class="p">().</span><span class="nf">push</span><span class="p">(</span><span class="n">vm</span><span class="p">.</span><span class="nf">fb</span><span class="p">.</span><span class="nf">group</span><span class="p">({</span>
         <span class="ss">relatedEntity: </span><span class="p">[</span><span class="n">null</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]],</span>
         <span class="ss">relationType: </span><span class="p">[</span><span class="n">null</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]],</span>
         <span class="ss">direction: </span><span class="p">[</span><span class="n">null</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]]</span>
        <span class="p">}));</span>
    <span class="p">};</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">removeRelation</span> <span class="o">=</span> <span class="n">function</span><span class="p">(</span><span class="n">index</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">relations</span><span class="p">().</span><span class="nf">removeAt</span><span class="p">(</span><span class="n">index</span><span class="p">);</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">relations</span><span class="p">().</span><span class="nf">markAsDirty</span><span class="p">();</span>
    <span class="p">};</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">save</span> <span class="o">=</span> <span class="n">function</span><span class="p">()</span> <span class="p">{</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">addEntityFormGroup</span><span class="p">.</span><span class="nf">markAsPristine</span><span class="p">();</span>
        <span class="n">saveEntityObservable</span><span class="p">().</span><span class="nf">subscribe</span><span class="p">(</span>
            <span class="n">function</span> <span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="p">{</span>
                <span class="n">widgetContext</span><span class="p">.</span><span class="nf">rxjs</span><span class="p">.</span><span class="nf">forkJoin</span><span class="p">([</span>
                    <span class="n">saveAttributes</span><span class="p">(</span><span class="n">entity</span><span class="p">.</span><span class="nf">id</span><span class="p">),</span>
                    <span class="n">saveRelations</span><span class="p">(</span><span class="n">entity</span><span class="p">.</span><span class="nf">id</span><span class="p">)</span>
                <span class="p">]).</span><span class="nf">subscribe</span><span class="p">(</span>
                    <span class="n">function</span> <span class="p">()</span> <span class="p">{</span>
                        <span class="n">widgetContext</span><span class="p">.</span><span class="nf">updateAliases</span><span class="p">();</span>
                        <span class="n">vm</span><span class="p">.</span><span class="nf">dialogRef</span><span class="p">.</span><span class="nf">close</span><span class="p">(</span><span class="n">null</span><span class="p">);</span>
                    <span class="p">}</span>
                <span class="p">);</span>
            <span class="p">}</span>
        <span class="p">);</span>
    <span class="p">};</span>

    <span class="n">function</span> <span class="n">saveEntityObservable</span><span class="p">()</span> <span class="p">{</span>
        <span class="n">const</span> <span class="n">formValues</span> <span class="o">=</span> <span class="n">vm</span><span class="p">.</span><span class="nf">addEntityFormGroup</span><span class="p">.</span><span class="nf">value</span><span class="p">;</span>
        <span class="n">let</span> <span class="n">entity</span> <span class="o">=</span> <span class="p">{</span>
            <span class="ss">name: </span><span class="n">formValues</span><span class="p">.</span><span class="nf">entityName</span><span class="p">,</span>
            <span class="ss">type: </span><span class="n">formValues</span><span class="p">.</span><span class="nf">type</span><span class="p">,</span>
            <span class="ss">label: </span><span class="n">formValues</span><span class="p">.</span><span class="nf">entityLabel</span>
        <span class="p">};</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">formValues</span><span class="p">.</span><span class="nf">entityType</span> <span class="o">==</span> <span class="s1">'ASSET'</span><span class="p">)</span> <span class="p">{</span>
            <span class="k">return</span> <span class="n">assetService</span><span class="p">.</span><span class="nf">saveAsset</span><span class="p">(</span><span class="n">entity</span><span class="p">);</span>
        <span class="p">}</span> <span class="k">else</span> <span class="k">if</span> <span class="p">(</span><span class="n">formValues</span><span class="p">.</span><span class="nf">entityType</span> <span class="o">==</span> <span class="s1">'DEVICE'</span><span class="p">)</span> <span class="p">{</span>
            <span class="k">return</span> <span class="n">deviceService</span><span class="p">.</span><span class="nf">saveDevice</span><span class="p">(</span><span class="n">entity</span><span class="p">);</span>
        <span class="p">}</span>
    <span class="p">}</span>

    <span class="n">function</span> <span class="n">saveAttributes</span><span class="p">(</span><span class="n">entityId</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">let</span> <span class="n">attributes</span> <span class="o">=</span> <span class="n">vm</span><span class="p">.</span><span class="nf">addEntityFormGroup</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'attributes'</span><span class="p">).</span><span class="nf">value</span><span class="p">;</span>
        <span class="n">let</span> <span class="n">attributesArray</span> <span class="o">=</span> <span class="p">[];</span>
        <span class="k">for</span> <span class="p">(</span><span class="n">let</span> <span class="n">key</span> <span class="k">in</span> <span class="n">attributes</span><span class="p">)</span> <span class="p">{</span>
            <span class="k">if</span><span class="p">(</span><span class="n">attributes</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">!==</span> <span class="n">null</span><span class="p">)</span> <span class="p">{</span>
                <span class="n">attributesArray</span><span class="p">.</span><span class="nf">push</span><span class="p">({</span><span class="ss">key: </span><span class="n">key</span><span class="p">,</span> <span class="ss">value: </span><span class="n">attributes</span><span class="p">[</span><span class="n">key</span><span class="p">]});</span>
            <span class="p">}</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">attributesArray</span><span class="p">.</span><span class="nf">length</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span>
            <span class="k">return</span> <span class="n">attributeService</span><span class="p">.</span><span class="nf">saveEntityAttributes</span><span class="p">(</span><span class="n">entityId</span><span class="p">,</span> <span class="s2">"SERVER_SCOPE"</span><span class="p">,</span> <span class="n">attributesArray</span><span class="p">);</span>
        <span class="p">}</span>
        <span class="k">return</span> <span class="n">widgetContext</span><span class="p">.</span><span class="nf">rxjs</span><span class="p">.</span><span class="nf">of</span><span class="p">([]);</span>
    <span class="p">}</span>

    <span class="n">function</span> <span class="n">saveRelations</span><span class="p">(</span><span class="n">entityId</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">let</span> <span class="n">relations</span> <span class="o">=</span> <span class="n">vm</span><span class="p">.</span><span class="nf">addEntityFormGroup</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'relations'</span><span class="p">).</span><span class="nf">value</span><span class="p">;</span>
        <span class="n">let</span> <span class="n">tasks</span> <span class="o">=</span> <span class="p">[];</span>
        <span class="k">for</span><span class="p">(</span><span class="n">let</span> <span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">relations</span><span class="p">.</span><span class="nf">length</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
            <span class="n">let</span> <span class="n">relation</span> <span class="o">=</span> <span class="p">{</span>
                <span class="ss">type: </span><span class="n">relations</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">relationType</span><span class="p">,</span>
                <span class="ss">typeGroup: </span><span class="s1">'COMMON'</span>
            <span class="p">};</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">relations</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">direction</span> <span class="o">==</span> <span class="s1">'FROM'</span><span class="p">)</span> <span class="p">{</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">to</span> <span class="o">=</span> <span class="n">relations</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">relatedEntity</span><span class="p">;</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">from</span> <span class="o">=</span> <span class="n">entityId</span><span class="p">;</span>
            <span class="p">}</span> <span class="k">else</span> <span class="p">{</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">to</span> <span class="o">=</span> <span class="n">entityId</span><span class="p">;</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">from</span> <span class="o">=</span> <span class="n">relations</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">relatedEntity</span><span class="p">;</span>
            <span class="p">}</span>
            <span class="n">tasks</span><span class="p">.</span><span class="nf">push</span><span class="p">(</span><span class="n">entityRelationService</span><span class="p">.</span><span class="nf">saveRelation</span><span class="p">(</span><span class="n">relation</span><span class="p">));</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">tasks</span><span class="p">.</span><span class="nf">length</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span>
            <span class="k">return</span> <span class="n">widgetContext</span><span class="p">.</span><span class="nf">rxjs</span><span class="p">.</span><span class="nf">forkJoin</span><span class="p">(</span><span class="n">tasks</span><span class="p">);</span>
        <span class="p">}</span>
        <span class="k">return</span> <span class="n">widgetContext</span><span class="p">.</span><span class="nf">rxjs</span><span class="p">.</span><span class="nf">of</span><span class="p">([]);</span>
    <span class="p">}</span>
<span class="p">}</span></code></pre></figure>
</details>

- In "_HTML_" tab, enter an HTML code for your custom action (you will find an example of this function below);

<details>

<summary>
<b>Example of a HTML code that adds the ability to add a device or an asset (click to expand):</b>
</summary>

<figure class="highlight"><pre><code class="language-ruby" data-lang="ruby"><span class="o">&lt;</span><span class="n">form</span> <span class="c1">#addEntityForm="ngForm" [formGroup]="addEntityFormGroup"</span>
      <span class="p">(</span><span class="n">ngSubmit</span><span class="p">)</span><span class="o">=</span><span class="s2">"save()"</span> <span class="k">class</span><span class="o">=</span><span class="s2">"add-entity-form"</span><span class="o">&gt;</span>
    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">toolbar</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">color</span><span class="o">=</span><span class="s2">"primary"</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">h2</span><span class="o">&gt;</span><span class="no">Add</span> <span class="n">entity</span><span class="o">&lt;</span><span class="sr">/h2&gt;
        &lt;span fxFlex&gt;&lt;/s</span><span class="n">pan</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">button</span> <span class="n">mat</span><span class="o">-</span><span class="n">icon</span><span class="o">-</span><span class="n">button</span> <span class="p">(</span><span class="n">click</span><span class="p">)</span><span class="o">=</span><span class="s2">"cancel()"</span> <span class="n">type</span><span class="o">=</span><span class="s2">"button"</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">icon</span> <span class="k">class</span><span class="o">=</span><span class="s2">"material-icons"</span><span class="o">&gt;</span><span class="n">close</span><span class="o">&lt;</span><span class="sr">/mat-icon&gt;
        &lt;/</span><span class="n">button</span><span class="o">&gt;</span>
    <span class="o">&lt;</span><span class="sr">/mat-toolbar&gt;
    &lt;mat-progress-bar color="warn" mode="indeterminate" *ngIf="isLoading$ | async"&gt;
    &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">progress</span><span class="o">-</span><span class="n">bar</span><span class="o">&gt;</span>
    <span class="o">&lt;</span><span class="n">div</span> <span class="n">style</span><span class="o">=</span><span class="s2">"height: 4px;"</span> <span class="o">*</span><span class="n">ngIf</span><span class="o">=</span><span class="s2">"!(isLoading$ | async)"</span><span class="o">&gt;&lt;</span><span class="sr">/div&gt;
    &lt;div mat-dialog-content fxLayout="column"&gt;
        &lt;div fxLayout="row" fxLayoutGap="8px" fxLayout.xs="column"  fxLayoutGap.xs="0"&gt;
            &lt;mat-form-field fxFlex class="mat-block"&gt;
                &lt;mat-label&gt;Entity Name&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">input</span> <span class="n">matInput</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"entityName"</span> <span class="n">required</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">error</span> <span class="o">*</span><span class="n">ngIf</span><span class="o">=</span><span class="s2">"addEntityFormGroup.get('entityName').hasError('required')"</span><span class="o">&gt;</span>
                    <span class="no">Entity</span> <span class="nb">name</span> <span class="n">is</span> <span class="n">required</span><span class="p">.</span>
                <span class="nf">&lt;</span><span class="o">/</span><span class="n">mat</span><span class="o">-</span><span class="n">error</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
            &lt;mat-form-field fxFlex class="mat-block"&gt;
                &lt;mat-label&gt;Entity Label&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">input</span> <span class="n">matInput</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"entityLabel"</span> <span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
        &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">div</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">fxLayoutGap</span><span class="o">=</span><span class="s2">"8px"</span> <span class="n">fxLayout</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"column"</span>  <span class="n">fxLayoutGap</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"0"</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">tb</span><span class="o">-</span><span class="n">entity</span><span class="o">-</span><span class="n">type</span><span class="o">-</span><span class="nb">select</span>
                    <span class="k">class</span><span class="o">=</span><span class="s2">"mat-block"</span>
                    <span class="n">formControlName</span><span class="o">=</span><span class="s2">"entityType"</span>
                    <span class="p">[</span><span class="n">showLabel</span><span class="p">]</span><span class="o">=</span><span class="s2">"true"</span>
                    <span class="p">[</span><span class="n">allowedEntityTypes</span><span class="p">]</span><span class="o">=</span><span class="s2">"allowedEntityTypes"</span>
            <span class="o">&gt;&lt;</span><span class="sr">/tb-entity-type-select&gt;
            &lt;tb-entity-subtype-autocomplete
                    fxFlex *ngIf="addEntityFormGroup.get('entityType').value == 'ASSET'"
                    class="mat-block"
                    formControlName="type"
                    [required]="true"
                    [entityType]="'ASSET'"
            &gt;&lt;/</span><span class="n">tb</span><span class="o">-</span><span class="n">entity</span><span class="o">-</span><span class="n">subtype</span><span class="o">-</span><span class="n">autocomplete</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">tb</span><span class="o">-</span><span class="n">entity</span><span class="o">-</span><span class="n">subtype</span><span class="o">-</span><span class="n">autocomplete</span>
                    <span class="n">fxFlex</span> <span class="o">*</span><span class="n">ngIf</span><span class="o">=</span><span class="s2">"addEntityFormGroup.get('entityType').value != 'ASSET'"</span>
                    <span class="k">class</span><span class="o">=</span><span class="s2">"mat-block"</span>
                    <span class="n">formControlName</span><span class="o">=</span><span class="s2">"type"</span>
                    <span class="p">[</span><span class="n">required</span><span class="p">]</span><span class="o">=</span><span class="s2">"true"</span>
                    <span class="p">[</span><span class="n">entityType</span><span class="p">]</span><span class="o">=</span><span class="s2">"'DEVICE'"</span>
            <span class="o">&gt;&lt;</span><span class="sr">/tb-entity-subtype-autocomplete&gt;
        &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">div</span> <span class="n">formGroupName</span><span class="o">=</span><span class="s2">"attributes"</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"column"</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">div</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">fxLayoutGap</span><span class="o">=</span><span class="s2">"8px"</span> <span class="n">fxLayout</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"column"</span>  <span class="n">fxLayoutGap</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"0"</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span> <span class="n">fxFlex</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-block"</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span><span class="no">Latitude</span><span class="o">&lt;</span><span class="sr">/mat-label&gt;
                    &lt;input type="number" step="any" matInput formControlName="latitude"&gt;
                &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span> <span class="n">fxFlex</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-block"</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span><span class="no">Longitude</span><span class="o">&lt;</span><span class="sr">/mat-label&gt;
                    &lt;input type="number" step="any" matInput formControlName="longitude"&gt;
                &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="sr">/div&gt;
            &lt;div fxLayout="row" fxLayoutGap="8px" fxLayout.xs="column"  fxLayoutGap.xs="0"&gt;
                &lt;mat-form-field fxFlex class="mat-block"&gt;
                    &lt;mat-label&gt;Address&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">input</span> <span class="n">matInput</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"address"</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
                &lt;mat-form-field fxFlex class="mat-block"&gt;
                    &lt;mat-label&gt;Owner&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">input</span> <span class="n">matInput</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"owner"</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
            &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">div</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">fxLayoutGap</span><span class="o">=</span><span class="s2">"8px"</span> <span class="n">fxLayout</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"column"</span>  <span class="n">fxLayoutGap</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"0"</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span> <span class="n">fxFlex</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-block"</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span><span class="no">Integer</span> <span class="no">Value</span><span class="o">&lt;</span><span class="sr">/mat-label&gt;
                    &lt;input type="number" step="1" matInput formControlName="number"&gt;
                    &lt;mat-error *ngIf="addEntityFormGroup.get('attributes.number').hasError('pattern')"&gt;
                        Invalid integer value.
                    &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">error</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
                &lt;div class="boolean-value-input" fxLayout="column" fxLayoutAlign="center start" fxFlex&gt;
                    &lt;label class="checkbox-label"&gt;Boolean Value&lt;/</span><span class="n">label</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">checkbox</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"booleanValue"</span> <span class="n">style</span><span class="o">=</span><span class="s2">"margin-bottom: 40px;"</span><span class="o">&gt;</span>
                        
                    <span class="o">&lt;</span><span class="sr">/mat-checkbox&gt;
                &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="sr">/div&gt;
        &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">div</span> <span class="k">class</span><span class="o">=</span><span class="s2">"relations-list"</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">div</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-body-1"</span> <span class="n">style</span><span class="o">=</span><span class="s2">"padding-bottom: 10px; color: rgba(0,0,0,0.57);"</span><span class="o">&gt;</span><span class="no">Relations</span><span class="o">&lt;</span><span class="sr">/div&gt;
            &lt;div class="body" [fxShow]="relations().length"&gt;
                &lt;div class="row" fxLayout="row" fxLayoutAlign="start center" formArrayName="relations" *ngFor="let relation of relations().controls; let i = index;"&gt;
                    &lt;div [formGroupName]="i" class="mat-elevation-z2" fxFlex fxLayout="row" style="padding: 5px 0 5px 5px;"&gt;
                        &lt;div fxFlex fxLayout="column"&gt;
                            &lt;div fxLayout="row" fxLayoutGap="8px" fxLayout.xs="column"  fxLayoutGap.xs="0"&gt;
                                &lt;mat-form-field class="mat-block" style="min-width: 100px;"&gt;
                                    &lt;mat-label&gt;Direction&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="nb">select</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"direction"</span> <span class="nb">name</span><span class="o">=</span><span class="s2">"direction"</span><span class="o">&gt;</span>
                                        <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">option</span> <span class="o">*</span><span class="n">ngFor</span><span class="o">=</span><span class="s2">"let direction of entitySearchDirection | keyvalue"</span> <span class="p">[</span><span class="n">value</span><span class="p">]</span><span class="o">=</span><span class="s2">"direction.value"</span><span class="o">&gt;</span>
                                            
                                        <span class="o">&lt;</span><span class="sr">/mat-option&gt;
                                    &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="nb">select</span><span class="o">&gt;</span>
                                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">error</span> <span class="o">*</span><span class="n">ngIf</span><span class="o">=</span><span class="s2">"relation.get('direction').hasError('required')"</span><span class="o">&gt;</span>
                                        <span class="no">Relation</span> <span class="n">direction</span> <span class="n">is</span> <span class="n">required</span><span class="p">.</span>
                                    <span class="nf">&lt;</span><span class="o">/</span><span class="n">mat</span><span class="o">-</span><span class="n">error</span><span class="o">&gt;</span>
                                <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
                                &lt;tb-relation-type-autocomplete
                                        fxFlex class="mat-block"
                                        formControlName="relationType"
                                        [required]="true"&gt;
                                &lt;/</span><span class="n">tb</span><span class="o">-</span><span class="n">relation</span><span class="o">-</span><span class="n">type</span><span class="o">-</span><span class="n">autocomplete</span><span class="o">&gt;</span>
                            <span class="o">&lt;</span><span class="sr">/div&gt;
                            &lt;div fxLayout="row" fxLayout.xs="column"&gt;
                                &lt;tb-entity-select
                                        fxFlex class="mat-block"
                                        [required]="true"
                                        formControlName="relatedEntity"&gt;
                                &lt;/</span><span class="n">tb</span><span class="o">-</span><span class="n">entity</span><span class="o">-</span><span class="nb">select</span><span class="o">&gt;</span>
                            <span class="o">&lt;</span><span class="sr">/div&gt;
                        &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
                        <span class="o">&lt;</span><span class="n">div</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"column"</span> <span class="n">fxLayoutAlign</span><span class="o">=</span><span class="s2">"center center"</span><span class="o">&gt;</span>
                            <span class="o">&lt;</span><span class="n">button</span> <span class="n">mat</span><span class="o">-</span><span class="n">icon</span><span class="o">-</span><span class="n">button</span> <span class="n">color</span><span class="o">=</span><span class="s2">"primary"</span>
                                    <span class="n">aria</span><span class="o">-</span><span class="n">label</span><span class="o">=</span><span class="s2">"Remove"</span>
                                    <span class="n">type</span><span class="o">=</span><span class="s2">"button"</span>
                                    <span class="p">(</span><span class="n">click</span><span class="p">)</span><span class="o">=</span><span class="s2">"removeRelation(i)"</span>
                                    <span class="n">matTooltip</span><span class="o">=</span><span class="s2">"Remove relation"</span>
                                    <span class="n">matTooltipPosition</span><span class="o">=</span><span class="s2">"above"</span><span class="o">&gt;</span>
                                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">icon</span><span class="o">&gt;</span><span class="n">close</span><span class="o">&lt;</span><span class="sr">/mat-icon&gt;
                            &lt;/</span><span class="n">button</span><span class="o">&gt;</span>
                        <span class="o">&lt;</span><span class="sr">/div&gt;
                    &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="sr">/div&gt;
            &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">div</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">button</span> <span class="n">mat</span><span class="o">-</span><span class="n">raised</span><span class="o">-</span><span class="n">button</span> <span class="n">color</span><span class="o">=</span><span class="s2">"primary"</span>
                        <span class="n">type</span><span class="o">=</span><span class="s2">"button"</span>
                        <span class="p">(</span><span class="n">click</span><span class="p">)</span><span class="o">=</span><span class="s2">"addRelation()"</span>
                        <span class="n">matTooltip</span><span class="o">=</span><span class="s2">"Add Relation"</span>
                        <span class="n">matTooltipPosition</span><span class="o">=</span><span class="s2">"above"</span><span class="o">&gt;</span>
                    <span class="no">Add</span>
                <span class="o">&lt;</span><span class="sr">/button&gt;
            &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="sr">/div&gt;
    &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
    <span class="o">&lt;</span><span class="n">div</span> <span class="n">mat</span><span class="o">-</span><span class="n">dialog</span><span class="o">-</span><span class="n">actions</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">fxLayoutAlign</span><span class="o">=</span><span class="s2">"end center"</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">button</span> <span class="n">mat</span><span class="o">-</span><span class="n">button</span> <span class="n">color</span><span class="o">=</span><span class="s2">"primary"</span>
                <span class="n">type</span><span class="o">=</span><span class="s2">"button"</span>
                <span class="p">[</span><span class="n">disabled</span><span class="p">]</span><span class="o">=</span><span class="s2">"(isLoading$ | async)"</span>
                <span class="p">(</span><span class="n">click</span><span class="p">)</span><span class="o">=</span><span class="s2">"cancel()"</span> <span class="n">cdkFocusInitial</span><span class="o">&gt;</span>
            <span class="no">Cancel</span>
        <span class="o">&lt;</span><span class="sr">/button&gt;
        &lt;button mat-button mat-raised-button color="primary"
                type="submit"
                [disabled]="(isLoading$ | async) || addEntityForm.invalid || !addEntityForm.dirty"&gt;
            Create
        &lt;/</span><span class="n">button</span><span class="o">&gt;</span>
    <span class="o">&lt;</span><span class="sr">/div&gt;
&lt;/</span><span class="n">form</span><span class="o">&gt;</span></code></pre></figure>
</details>

- After input functions, click the "Add" button at the bottom of the "Add action" window.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-1-ce.webp" alt="As an example for this manual, select &quot;Widget header button&quot; as the action source. Input a name for the action and select an icon that will represent an action button. With this icon, action will be performed. Select a &quot;Custom action (with HTML template)&quot; action type from the &quot;Action&quot; drop-down menu. In the tabs that appear, select &quot;JavaScript&quot; tab;" loading="lazy"><figcaption>As an example for this manual, select "Widget header button" as the action source. Input a name for the action and select an icon that will represent an action button. With this icon, action will be performed. Select a "Custom action (with HTML template)" action type from the "Action" drop-down menu. In the tabs that appear, select "JavaScript" tab;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-2-ce.webp" alt="Enter a JavaScript function for your custom action;" loading="lazy"><figcaption>Enter a JavaScript function for your custom action;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-3-ce.webp" alt="In &quot;HTML&quot; tab, enter an HTML code for your custom action. After input functions, click the &quot;Add&quot; button;" loading="lazy"><figcaption>In "HTML" tab, enter an HTML code for your custom action. After input functions, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-4-ce.webp" alt="The first action button for adding a new entity has been added." loading="lazy"><figcaption>The first action button for adding a new entity has been added.</figcaption></figure></div>


Now let's add an action button to edit the entities.

- Click the "plus" icon in the top right corner of the screen again to open a new "Add action" window;
- As an example for this manual, select "[Action cell button](#action-cell-button)" action source;
- Input a name for the action and select an icon that will represent an action button. With this icon, action will be performed;
- Select a "Custom action (with HTML template)" action type from the "Action" drop-down menu;
- In the tabs that appear, select "JavaScript" tab. Enter a JavaScript function for your custom action. In this example, we use a function that adds the ability to edit an entity (you will find an example of this function below);

<details>
<summary>
<b>Example of a JavaScript function that adds a possibility to edit a device or an asset (click to expand):</b>
</summary>

<figure class="highlight"><pre><code class="language-ruby" data-lang="ruby"><span class="n">let</span> <span class="vg">$injector</span> <span class="o">=</span> <span class="n">widgetContext</span><span class="o">.</span><span class="vg">$scope</span><span class="o">.</span><span class="vg">$injector</span><span class="p">;</span>
<span class="n">let</span> <span class="n">customDialog</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'customDialog'</span><span class="p">));</span>
<span class="n">let</span> <span class="n">entityService</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'entityService'</span><span class="p">));</span>
<span class="n">let</span> <span class="n">assetService</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'assetService'</span><span class="p">));</span>
<span class="n">let</span> <span class="n">deviceService</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'deviceService'</span><span class="p">));</span>
<span class="n">let</span> <span class="n">attributeService</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'attributeService'</span><span class="p">));</span>
<span class="n">let</span> <span class="n">entityRelationService</span> <span class="o">=</span> <span class="vg">$injector</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">widgetContext</span><span class="p">.</span><span class="nf">servicesMap</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'entityRelationService'</span><span class="p">));</span>

<span class="n">openEditEntityDialog</span><span class="p">();</span>

<span class="n">function</span> <span class="n">openEditEntityDialog</span><span class="p">()</span> <span class="p">{</span>
<span class="n">customDialog</span><span class="p">.</span><span class="nf">customDialog</span><span class="p">(</span><span class="n">htmlTemplate</span><span class="p">,</span> <span class="no">EditEntityDialogController</span><span class="p">).</span><span class="nf">subscribe</span><span class="p">();</span>
<span class="p">}</span>

<span class="n">function</span> <span class="no">EditEntityDialogController</span><span class="p">(</span><span class="n">instance</span><span class="p">)</span> <span class="p">{</span>
<span class="n">let</span> <span class="n">vm</span> <span class="o">=</span> <span class="n">instance</span><span class="p">;</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">entityName</span> <span class="o">=</span> <span class="n">entityName</span><span class="p">;</span>
    <span class="n">vm</span><span class="p">.</span><span class="nf">entityType</span> <span class="o">=</span> <span class="n">entityId</span><span class="p">.</span><span class="nf">entityType</span><span class="p">;</span>
    <span class="n">vm</span><span class="p">.</span><span class="nf">entitySearchDirection</span> <span class="o">=</span> <span class="p">{</span>
        <span class="ss">from: </span><span class="s2">"FROM"</span><span class="p">,</span>
        <span class="ss">to: </span><span class="s2">"TO"</span>
    <span class="p">};</span>
    <span class="n">vm</span><span class="p">.</span><span class="nf">attributes</span> <span class="o">=</span> <span class="p">{};</span>
    <span class="n">vm</span><span class="p">.</span><span class="nf">oldRelationsData</span> <span class="o">=</span> <span class="p">[];</span>
    <span class="n">vm</span><span class="p">.</span><span class="nf">relationsToDelete</span> <span class="o">=</span> <span class="p">[];</span>
    <span class="n">vm</span><span class="p">.</span><span class="nf">entity</span> <span class="o">=</span> <span class="p">{};</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">editEntityFormGroup</span> <span class="o">=</span> <span class="n">vm</span><span class="p">.</span><span class="nf">fb</span><span class="p">.</span><span class="nf">group</span><span class="p">({</span>
        <span class="ss">entityName: </span><span class="p">[</span><span class="s1">''</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]],</span>
        <span class="ss">entityType: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
        <span class="ss">entityLabel: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
        <span class="ss">type: </span><span class="p">[</span><span class="s1">''</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]],</span>
        <span class="ss">attributes: </span><span class="n">vm</span><span class="p">.</span><span class="nf">fb</span><span class="p">.</span><span class="nf">group</span><span class="p">({</span>
            <span class="ss">latitude: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
            <span class="ss">longitude: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
            <span class="ss">address: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
            <span class="ss">owner: </span><span class="p">[</span><span class="n">null</span><span class="p">],</span>
            <span class="ss">number: </span><span class="p">[</span><span class="n">null</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">pattern</span><span class="p">(</span><span class="sr">/^-?[0-9]+$/</span><span class="p">)]],</span>
            <span class="ss">booleanValue: </span><span class="p">[</span><span class="kp">false</span><span class="p">]</span>
        <span class="p">}),</span>
        <span class="ss">oldRelations: </span><span class="n">vm</span><span class="p">.</span><span class="nf">fb</span><span class="p">.</span><span class="nf">array</span><span class="p">([]),</span>
        <span class="ss">relations: </span><span class="n">vm</span><span class="p">.</span><span class="nf">fb</span><span class="p">.</span><span class="nf">array</span><span class="p">([])</span>
    <span class="p">});</span>

    <span class="n">getEntityInfo</span><span class="p">();</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">cancel</span> <span class="o">=</span> <span class="n">function</span><span class="p">()</span> <span class="p">{</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">dialogRef</span><span class="p">.</span><span class="nf">close</span><span class="p">(</span><span class="n">null</span><span class="p">);</span>
    <span class="p">};</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">relations</span> <span class="o">=</span> <span class="n">function</span><span class="p">()</span> <span class="p">{</span>
        <span class="k">return</span> <span class="n">vm</span><span class="p">.</span><span class="nf">editEntityFormGroup</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'relations'</span><span class="p">);</span>
    <span class="p">};</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">oldRelations</span> <span class="o">=</span> <span class="n">function</span><span class="p">()</span> <span class="p">{</span>
        <span class="k">return</span> <span class="n">vm</span><span class="p">.</span><span class="nf">editEntityFormGroup</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'oldRelations'</span><span class="p">);</span>
    <span class="p">};</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">addRelation</span> <span class="o">=</span> <span class="n">function</span><span class="p">()</span> <span class="p">{</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">relations</span><span class="p">().</span><span class="nf">push</span><span class="p">(</span><span class="n">vm</span><span class="p">.</span><span class="nf">fb</span><span class="p">.</span><span class="nf">group</span><span class="p">({</span>
            <span class="ss">relatedEntity: </span><span class="p">[</span><span class="n">null</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]],</span>
            <span class="ss">relationType: </span><span class="p">[</span><span class="n">null</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]],</span>
            <span class="ss">direction: </span><span class="p">[</span><span class="n">null</span><span class="p">,</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]]</span>
        <span class="p">}));</span>
    <span class="p">};</span>

    <span class="n">function</span> <span class="n">addOldRelation</span><span class="p">()</span> <span class="p">{</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">oldRelations</span><span class="p">().</span><span class="nf">push</span><span class="p">(</span><span class="n">vm</span><span class="p">.</span><span class="nf">fb</span><span class="p">.</span><span class="nf">group</span><span class="p">({</span>
            <span class="ss">relatedEntity: </span><span class="p">[{</span><span class="ss">value: </span><span class="n">null</span><span class="p">,</span> <span class="ss">disabled: </span><span class="kp">true</span><span class="p">},</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]],</span>
            <span class="ss">relationType: </span><span class="p">[{</span><span class="ss">value: </span><span class="n">null</span><span class="p">,</span> <span class="ss">disabled: </span><span class="kp">true</span><span class="p">},</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]],</span>
            <span class="ss">direction: </span><span class="p">[{</span><span class="ss">value: </span><span class="n">null</span><span class="p">,</span> <span class="ss">disabled: </span><span class="kp">true</span><span class="p">},</span> <span class="p">[</span><span class="n">vm</span><span class="p">.</span><span class="nf">validators</span><span class="p">.</span><span class="nf">required</span><span class="p">]]</span>
        <span class="p">}));</span>
    <span class="p">}</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">removeRelation</span> <span class="o">=</span> <span class="n">function</span><span class="p">(</span><span class="n">index</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">relations</span><span class="p">().</span><span class="nf">removeAt</span><span class="p">(</span><span class="n">index</span><span class="p">);</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">relations</span><span class="p">().</span><span class="nf">markAsDirty</span><span class="p">();</span>
    <span class="p">};</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">removeOldRelation</span> <span class="o">=</span> <span class="n">function</span><span class="p">(</span><span class="n">index</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">oldRelations</span><span class="p">().</span><span class="nf">removeAt</span><span class="p">(</span><span class="n">index</span><span class="p">);</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">relationsToDelete</span><span class="p">.</span><span class="nf">push</span><span class="p">(</span><span class="n">vm</span><span class="p">.</span><span class="nf">oldRelationsData</span><span class="p">[</span><span class="n">index</span><span class="p">]);</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">oldRelations</span><span class="p">().</span><span class="nf">markAsDirty</span><span class="p">();</span>
    <span class="p">};</span>

    <span class="n">vm</span><span class="p">.</span><span class="nf">save</span> <span class="o">=</span> <span class="n">function</span><span class="p">()</span> <span class="p">{</span>
        <span class="n">vm</span><span class="p">.</span><span class="nf">editEntityFormGroup</span><span class="p">.</span><span class="nf">markAsPristine</span><span class="p">();</span>
        <span class="n">widgetContext</span><span class="p">.</span><span class="nf">rxjs</span><span class="p">.</span><span class="nf">forkJoin</span><span class="p">([</span>
            <span class="n">saveAttributes</span><span class="p">(</span><span class="n">entityId</span><span class="p">),</span>
            <span class="n">saveRelations</span><span class="p">(</span><span class="n">entityId</span><span class="p">),</span>
            <span class="n">saveEntity</span><span class="p">()</span>
        <span class="p">]).</span><span class="nf">subscribe</span><span class="p">(</span>
            <span class="n">function</span> <span class="p">()</span> <span class="p">{</span>
                <span class="n">widgetContext</span><span class="p">.</span><span class="nf">updateAliases</span><span class="p">();</span>
                <span class="n">vm</span><span class="p">.</span><span class="nf">dialogRef</span><span class="p">.</span><span class="nf">close</span><span class="p">(</span><span class="n">null</span><span class="p">);</span>
            <span class="p">}</span>
        <span class="p">);</span>
    <span class="p">};</span>

    <span class="n">function</span> <span class="n">getEntityAttributes</span><span class="p">(</span><span class="n">attributes</span><span class="p">)</span> <span class="p">{</span>
        <span class="k">for</span> <span class="p">(</span><span class="n">var</span> <span class="n">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">attributes</span><span class="p">.</span><span class="nf">length</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
            <span class="n">vm</span><span class="p">.</span><span class="nf">attributes</span><span class="p">[</span><span class="n">attributes</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">attributes</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">value</span><span class="p">;</span>
        <span class="p">}</span>
    <span class="p">}</span>

    <span class="n">function</span> <span class="n">getEntityRelations</span><span class="p">(</span><span class="n">relations</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">let</span> <span class="n">relationsFrom</span> <span class="o">=</span> <span class="n">relations</span><span class="p">[</span><span class="mi">0</span><span class="p">];</span>
        <span class="n">let</span> <span class="n">relationsTo</span> <span class="o">=</span> <span class="n">relations</span><span class="p">[</span><span class="mi">1</span><span class="p">];</span>
        <span class="k">for</span> <span class="p">(</span><span class="n">let</span> <span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">relationsFrom</span><span class="p">.</span><span class="nf">length</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
            <span class="n">let</span> <span class="n">relation</span> <span class="o">=</span> <span class="p">{</span>
                <span class="ss">direction: </span><span class="s1">'FROM'</span><span class="p">,</span>
                <span class="ss">relationType: </span><span class="n">relationsFrom</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">type</span><span class="p">,</span>
                <span class="ss">relatedEntity: </span><span class="n">relationsFrom</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">to</span>
            <span class="p">};</span>
            <span class="n">vm</span><span class="p">.</span><span class="nf">oldRelationsData</span><span class="p">.</span><span class="nf">push</span><span class="p">(</span><span class="n">relation</span><span class="p">);</span>
            <span class="n">addOldRelation</span><span class="p">();</span>
        <span class="p">}</span>
        <span class="k">for</span> <span class="p">(</span><span class="n">let</span> <span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">relationsTo</span><span class="p">.</span><span class="nf">length</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
            <span class="n">let</span> <span class="n">relation</span> <span class="o">=</span> <span class="p">{</span>
                <span class="ss">direction: </span><span class="s1">'TO'</span><span class="p">,</span>
                <span class="ss">relationType: </span><span class="n">relationsTo</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">type</span><span class="p">,</span>
                <span class="ss">relatedEntity: </span><span class="n">relationsTo</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">from</span>
            <span class="p">};</span>
            <span class="n">vm</span><span class="p">.</span><span class="nf">oldRelationsData</span><span class="p">.</span><span class="nf">push</span><span class="p">(</span><span class="n">relation</span><span class="p">);</span>
            <span class="n">addOldRelation</span><span class="p">();</span>
        <span class="p">}</span>
    <span class="p">}</span>

    <span class="n">function</span> <span class="n">getEntityInfo</span><span class="p">()</span> <span class="p">{</span>
        <span class="n">widgetContext</span><span class="p">.</span><span class="nf">rxjs</span><span class="p">.</span><span class="nf">forkJoin</span><span class="p">([</span>
            <span class="n">entityRelationService</span><span class="p">.</span><span class="nf">findInfoByFrom</span><span class="p">(</span><span class="n">entityId</span><span class="p">),</span>
            <span class="n">entityRelationService</span><span class="p">.</span><span class="nf">findInfoByTo</span><span class="p">(</span><span class="n">entityId</span><span class="p">),</span>
            <span class="n">attributeService</span><span class="p">.</span><span class="nf">getEntityAttributes</span><span class="p">(</span><span class="n">entityId</span><span class="p">,</span> <span class="s1">'SERVER_SCOPE'</span><span class="p">),</span>
            <span class="n">entityService</span><span class="p">.</span><span class="nf">getEntity</span><span class="p">(</span><span class="n">entityId</span><span class="p">.</span><span class="nf">entityType</span><span class="p">,</span> <span class="n">entityId</span><span class="p">.</span><span class="nf">id</span><span class="p">)</span>
        <span class="p">]).</span><span class="nf">subscribe</span><span class="p">(</span>
            <span class="n">function</span> <span class="p">(</span><span class="n">data</span><span class="p">)</span> <span class="p">{</span>
                <span class="n">getEntityRelations</span><span class="p">(</span><span class="n">data</span><span class="p">.</span><span class="nf">slice</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">));</span>
                <span class="n">getEntityAttributes</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="mi">2</span><span class="p">]);</span>
                <span class="n">vm</span><span class="p">.</span><span class="nf">entity</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="mi">3</span><span class="p">];</span>
                <span class="n">vm</span><span class="p">.</span><span class="nf">editEntityFormGroup</span><span class="p">.</span><span class="nf">patchValue</span><span class="p">({</span>
                    <span class="ss">entityName: </span><span class="n">vm</span><span class="p">.</span><span class="nf">entity</span><span class="p">.</span><span class="nf">name</span><span class="p">,</span>
                    <span class="ss">entityType: </span><span class="n">vm</span><span class="p">.</span><span class="nf">entityType</span><span class="p">,</span>
                    <span class="ss">entityLabel: </span><span class="n">vm</span><span class="p">.</span><span class="nf">entity</span><span class="p">.</span><span class="nf">label</span><span class="p">,</span>
                    <span class="ss">type: </span><span class="n">vm</span><span class="p">.</span><span class="nf">entity</span><span class="p">.</span><span class="nf">type</span><span class="p">,</span>
                    <span class="ss">attributes: </span><span class="n">vm</span><span class="p">.</span><span class="nf">attributes</span><span class="p">,</span>
                    <span class="ss">oldRelations: </span><span class="n">vm</span><span class="p">.</span><span class="nf">oldRelationsData</span>
                <span class="p">},</span> <span class="p">{</span><span class="ss">emitEvent: </span><span class="kp">false</span><span class="p">});</span>
            <span class="p">}</span>
        <span class="p">);</span>
    <span class="p">}</span>

    <span class="n">function</span> <span class="n">saveEntity</span><span class="p">()</span> <span class="p">{</span>
        <span class="n">const</span> <span class="n">formValues</span> <span class="o">=</span> <span class="n">vm</span><span class="p">.</span><span class="nf">editEntityFormGroup</span><span class="p">.</span><span class="nf">value</span><span class="p">;</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">vm</span><span class="p">.</span><span class="nf">entity</span><span class="p">.</span><span class="nf">label</span> <span class="o">!==</span> <span class="n">formValues</span><span class="p">.</span><span class="nf">entityLabel</span><span class="p">){</span>
            <span class="n">vm</span><span class="p">.</span><span class="nf">entity</span><span class="p">.</span><span class="nf">label</span> <span class="o">=</span> <span class="n">formValues</span><span class="p">.</span><span class="nf">entityLabel</span><span class="p">;</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">formValues</span><span class="p">.</span><span class="nf">entityType</span> <span class="o">==</span> <span class="s1">'ASSET'</span><span class="p">)</span> <span class="p">{</span>
                <span class="k">return</span> <span class="n">assetService</span><span class="p">.</span><span class="nf">saveAsset</span><span class="p">(</span><span class="n">vm</span><span class="p">.</span><span class="nf">entity</span><span class="p">);</span>
            <span class="p">}</span> <span class="k">else</span> <span class="k">if</span> <span class="p">(</span><span class="n">formValues</span><span class="p">.</span><span class="nf">entityType</span> <span class="o">==</span> <span class="s1">'DEVICE'</span><span class="p">)</span> <span class="p">{</span>
                <span class="k">return</span> <span class="n">deviceService</span><span class="p">.</span><span class="nf">saveDevice</span><span class="p">(</span><span class="n">vm</span><span class="p">.</span><span class="nf">entity</span><span class="p">);</span>
            <span class="p">}</span>
        <span class="p">}</span>
        <span class="k">return</span> <span class="n">widgetContext</span><span class="p">.</span><span class="nf">rxjs</span><span class="p">.</span><span class="nf">of</span><span class="p">([]);</span>
    <span class="p">}</span>

    <span class="n">function</span> <span class="n">saveAttributes</span><span class="p">(</span><span class="n">entityId</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">let</span> <span class="n">attributes</span> <span class="o">=</span> <span class="n">vm</span><span class="p">.</span><span class="nf">editEntityFormGroup</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'attributes'</span><span class="p">).</span><span class="nf">value</span><span class="p">;</span>
        <span class="n">let</span> <span class="n">attributesArray</span> <span class="o">=</span> <span class="p">[];</span>
        <span class="k">for</span> <span class="p">(</span><span class="n">let</span> <span class="n">key</span> <span class="k">in</span> <span class="n">attributes</span><span class="p">)</span> <span class="p">{</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">attributes</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">!==</span> <span class="n">vm</span><span class="p">.</span><span class="nf">attributes</span><span class="p">[</span><span class="n">key</span><span class="p">])</span> <span class="p">{</span>
                <span class="n">attributesArray</span><span class="p">.</span><span class="nf">push</span><span class="p">({</span><span class="ss">key: </span><span class="n">key</span><span class="p">,</span> <span class="ss">value: </span><span class="n">attributes</span><span class="p">[</span><span class="n">key</span><span class="p">]});</span>
            <span class="p">}</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">attributesArray</span><span class="p">.</span><span class="nf">length</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span>
            <span class="k">return</span> <span class="n">attributeService</span><span class="p">.</span><span class="nf">saveEntityAttributes</span><span class="p">(</span><span class="n">entityId</span><span class="p">,</span> <span class="s2">"SERVER_SCOPE"</span><span class="p">,</span> <span class="n">attributesArray</span><span class="p">);</span>
        <span class="p">}</span>
        <span class="k">return</span> <span class="n">widgetContext</span><span class="p">.</span><span class="nf">rxjs</span><span class="p">.</span><span class="nf">of</span><span class="p">([]);</span>
    <span class="p">}</span>

    <span class="n">function</span> <span class="n">saveRelations</span><span class="p">(</span><span class="n">entityId</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">let</span> <span class="n">relations</span> <span class="o">=</span> <span class="n">vm</span><span class="p">.</span><span class="nf">editEntityFormGroup</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="s1">'relations'</span><span class="p">).</span><span class="nf">value</span><span class="p">;</span>
        <span class="n">let</span> <span class="n">tasks</span> <span class="o">=</span> <span class="p">[];</span>
        <span class="k">for</span><span class="p">(</span><span class="n">let</span> <span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">relations</span><span class="p">.</span><span class="nf">length</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
            <span class="n">let</span> <span class="n">relation</span> <span class="o">=</span> <span class="p">{</span>
                <span class="ss">type: </span><span class="n">relations</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">relationType</span><span class="p">,</span>
                <span class="ss">typeGroup: </span><span class="s1">'COMMON'</span>
            <span class="p">};</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">relations</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">direction</span> <span class="o">==</span> <span class="s1">'FROM'</span><span class="p">)</span> <span class="p">{</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">to</span> <span class="o">=</span> <span class="n">relations</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">relatedEntity</span><span class="p">;</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">from</span> <span class="o">=</span> <span class="n">entityId</span><span class="p">;</span>
            <span class="p">}</span> <span class="k">else</span> <span class="p">{</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">to</span> <span class="o">=</span> <span class="n">entityId</span><span class="p">;</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">from</span> <span class="o">=</span> <span class="n">relations</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">relatedEntity</span><span class="p">;</span>
            <span class="p">}</span>
            <span class="n">tasks</span><span class="p">.</span><span class="nf">push</span><span class="p">(</span><span class="n">entityRelationService</span><span class="p">.</span><span class="nf">saveRelation</span><span class="p">(</span><span class="n">relation</span><span class="p">));</span>
        <span class="p">}</span>
        <span class="k">for</span> <span class="p">(</span><span class="n">let</span> <span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">vm</span><span class="p">.</span><span class="nf">relationsToDelete</span><span class="p">.</span><span class="nf">length</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span> <span class="p">{</span>
            <span class="n">let</span> <span class="n">relation</span> <span class="o">=</span> <span class="p">{</span>
                <span class="ss">type: </span><span class="n">vm</span><span class="p">.</span><span class="nf">relationsToDelete</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">relationType</span>
            <span class="p">};</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">vm</span><span class="p">.</span><span class="nf">relationsToDelete</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">direction</span> <span class="o">==</span> <span class="s1">'FROM'</span><span class="p">)</span> <span class="p">{</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">to</span> <span class="o">=</span> <span class="n">vm</span><span class="p">.</span><span class="nf">relationsToDelete</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">relatedEntity</span><span class="p">;</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">from</span> <span class="o">=</span> <span class="n">entityId</span><span class="p">;</span>
            <span class="p">}</span> <span class="k">else</span> <span class="p">{</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">to</span> <span class="o">=</span> <span class="n">entityId</span><span class="p">;</span>
                <span class="n">relation</span><span class="p">.</span><span class="nf">from</span> <span class="o">=</span> <span class="n">vm</span><span class="p">.</span><span class="nf">relationsToDelete</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="nf">relatedEntity</span><span class="p">;</span>
            <span class="p">}</span>
            <span class="n">tasks</span><span class="p">.</span><span class="nf">push</span><span class="p">(</span><span class="n">entityRelationService</span><span class="p">.</span><span class="nf">deleteRelation</span><span class="p">(</span><span class="n">relation</span><span class="p">.</span><span class="nf">from</span><span class="p">,</span> <span class="n">relation</span><span class="p">.</span><span class="nf">type</span><span class="p">,</span> <span class="n">relation</span><span class="p">.</span><span class="nf">to</span><span class="p">));</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">tasks</span><span class="p">.</span><span class="nf">length</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span>
            <span class="k">return</span> <span class="n">widgetContext</span><span class="p">.</span><span class="nf">rxjs</span><span class="p">.</span><span class="nf">forkJoin</span><span class="p">(</span><span class="n">tasks</span><span class="p">);</span>
        <span class="p">}</span>
        <span class="k">return</span> <span class="n">widgetContext</span><span class="p">.</span><span class="nf">rxjs</span><span class="p">.</span><span class="nf">of</span><span class="p">([]);</span>
    <span class="p">}</span>
<span class="p">}</span></code></pre></figure>
</details>

- In "<b>HTML</b>" tab, enter an HTML code for your custom action (you will find an example of this function below);

<details>

<summary>
<b>Example of HTML code that adds a possibility to edit a device or an asset (click to expand):</b>
</summary>

<figure class="highlight"><pre><code class="language-ruby" data-lang="ruby"><span class="o">&lt;</span><span class="n">form</span> <span class="c1">#editEntityForm="ngForm" [formGroup]="editEntityFormGroup"</span>
      <span class="p">(</span><span class="n">ngSubmit</span><span class="p">)</span><span class="o">=</span><span class="s2">"save()"</span>  <span class="k">class</span><span class="o">=</span><span class="s2">"edit-entity-form"</span><span class="o">&gt;</span>
    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">toolbar</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">color</span><span class="o">=</span><span class="s2">"primary"</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">h2</span><span class="o">&gt;</span><span class="no">Edit</span>  <span class="o">&lt;</span><span class="sr">/h2&gt;
        &lt;span fxFlex&gt;&lt;/s</span><span class="n">pan</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">button</span> <span class="n">mat</span><span class="o">-</span><span class="n">icon</span><span class="o">-</span><span class="n">button</span> <span class="p">(</span><span class="n">click</span><span class="p">)</span><span class="o">=</span><span class="s2">"cancel()"</span> <span class="n">type</span><span class="o">=</span><span class="s2">"button"</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">icon</span> <span class="k">class</span><span class="o">=</span><span class="s2">"material-icons"</span><span class="o">&gt;</span><span class="n">close</span><span class="o">&lt;</span><span class="sr">/mat-icon&gt;
        &lt;/</span><span class="n">button</span><span class="o">&gt;</span>
    <span class="o">&lt;</span><span class="sr">/mat-toolbar&gt;
    &lt;mat-progress-bar color="warn" mode="indeterminate" *ngIf="isLoading$ | async"&gt;
    &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">progress</span><span class="o">-</span><span class="n">bar</span><span class="o">&gt;</span>
    <span class="o">&lt;</span><span class="n">div</span> <span class="n">style</span><span class="o">=</span><span class="s2">"height: 4px;"</span> <span class="o">*</span><span class="n">ngIf</span><span class="o">=</span><span class="s2">"!(isLoading$ | async)"</span><span class="o">&gt;&lt;</span><span class="sr">/div&gt;
    &lt;div mat-dialog-content fxLayout="column"&gt;
        &lt;div fxLayout="row" fxLayoutGap="8px" fxLayout.xs="column"  fxLayoutGap.xs="0"&gt;
            &lt;mat-form-field fxFlex class="mat-block"&gt;
                &lt;mat-label&gt;Entity Name&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">input</span> <span class="n">matInput</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"entityName"</span> <span class="n">required</span> <span class="n">readonly</span><span class="o">=</span><span class="s2">""</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
            &lt;mat-form-field fxFlex class="mat-block"&gt;
                &lt;mat-label&gt;Entity Label&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">input</span> <span class="n">matInput</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"entityLabel"</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
        &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">div</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">fxLayoutGap</span><span class="o">=</span><span class="s2">"8px"</span> <span class="n">fxLayout</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"column"</span>  <span class="n">fxLayoutGap</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"0"</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span> <span class="n">fxFlex</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-block"</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span><span class="no">Entity</span> <span class="no">Type</span><span class="o">&lt;</span><span class="sr">/mat-label&gt;
                &lt;input matInput formControlName="entityType" readonly&gt;
            &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span> <span class="n">fxFlex</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-block"</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span><span class="no">Type</span><span class="o">&lt;</span><span class="sr">/mat-label&gt;
                &lt;input matInput formControlName="type" readonly&gt;
            &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="sr">/div&gt;
        &lt;div formGroupName="attributes" fxLayout="column"&gt;
            &lt;div fxLayout="row" fxLayoutGap="8px" fxLayout.xs="column"  fxLayoutGap.xs="0"&gt;
                &lt;mat-form-field fxFlex class="mat-block"&gt;
                    &lt;mat-label&gt;Latitude&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">input</span> <span class="n">type</span><span class="o">=</span><span class="s2">"number"</span> <span class="n">step</span><span class="o">=</span><span class="s2">"any"</span> <span class="n">matInput</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"latitude"</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
                &lt;mat-form-field fxFlex class="mat-block"&gt;
                    &lt;mat-label&gt;Longitude&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">input</span> <span class="n">type</span><span class="o">=</span><span class="s2">"number"</span> <span class="n">step</span><span class="o">=</span><span class="s2">"any"</span> <span class="n">matInput</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"longitude"</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
            &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">div</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">fxLayoutGap</span><span class="o">=</span><span class="s2">"8px"</span> <span class="n">fxLayout</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"column"</span>  <span class="n">fxLayoutGap</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"0"</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span> <span class="n">fxFlex</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-block"</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span><span class="no">Address</span><span class="o">&lt;</span><span class="sr">/mat-label&gt;
                    &lt;input matInput formControlName="address"&gt;
                &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span> <span class="n">fxFlex</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-block"</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span><span class="no">Owner</span><span class="o">&lt;</span><span class="sr">/mat-label&gt;
                    &lt;input matInput formControlName="owner"&gt;
                &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="sr">/div&gt;
            &lt;div fxLayout="row" fxLayoutGap="8px" fxLayout.xs="column"  fxLayoutGap.xs="0"&gt;
                &lt;mat-form-field fxFlex class="mat-block"&gt;
                    &lt;mat-label&gt;Integer Value&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">input</span> <span class="n">type</span><span class="o">=</span><span class="s2">"number"</span> <span class="n">step</span><span class="o">=</span><span class="s2">"1"</span> <span class="n">matInput</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"number"</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">error</span> <span class="o">*</span><span class="n">ngIf</span><span class="o">=</span><span class="s2">"editEntityFormGroup.get('attributes.number').hasError('pattern')"</span><span class="o">&gt;</span>
                        <span class="no">Invalid</span> <span class="n">integer</span> <span class="n">value</span><span class="p">.</span>
                    <span class="nf">&lt;</span><span class="o">/</span><span class="n">mat</span><span class="o">-</span><span class="n">error</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
                &lt;div class="boolean-value-input" fxLayout="column" fxLayoutAlign="center start" fxFlex&gt;
                    &lt;label class="checkbox-label"&gt;Boolean Value&lt;/</span><span class="n">label</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">checkbox</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"booleanValue"</span> <span class="n">style</span><span class="o">=</span><span class="s2">"margin-bottom: 40px;"</span><span class="o">&gt;</span>
                        
                    <span class="o">&lt;</span><span class="sr">/mat-checkbox&gt;
                &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="sr">/div&gt;
        &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">div</span> <span class="k">class</span><span class="o">=</span><span class="s2">"relations-list old-relations"</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">div</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-body-1"</span> <span class="n">style</span><span class="o">=</span><span class="s2">"padding-bottom: 10px; color: rgba(0,0,0,0.57);"</span><span class="o">&gt;</span><span class="no">Relations</span><span class="o">&lt;</span><span class="sr">/div&gt;
            &lt;div class="body" [fxShow]="oldRelations().length"&gt;
                &lt;div class="row" fxLayout="row" fxLayoutAlign="start center" formArrayName="oldRelations" 
                     *ngFor="let relation of oldRelations().controls; let i = index;"&gt;
                    &lt;div [formGroupName]="i" class="mat-elevation-z2" fxFlex fxLayout="row" style="padding: 5px 0 5px 5px;"&gt;
                        &lt;div fxFlex fxLayout="column"&gt;
                            &lt;div fxLayout="row" fxLayoutGap="8px" fxLayout.xs="column"  fxLayoutGap.xs="0"&gt;
                                &lt;mat-form-field class="mat-block" style="min-width: 100px;"&gt;
                                    &lt;mat-label&gt;Direction&lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span>
                                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="nb">select</span> <span class="n">formControlName</span><span class="o">=</span><span class="s2">"direction"</span> <span class="nb">name</span><span class="o">=</span><span class="s2">"direction"</span><span class="o">&gt;</span>
                                        <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">option</span> <span class="o">*</span><span class="n">ngFor</span><span class="o">=</span><span class="s2">"let direction of entitySearchDirection | keyvalue"</span> <span class="p">[</span><span class="n">value</span><span class="p">]</span><span class="o">=</span><span class="s2">"direction.value"</span><span class="o">&gt;</span>
                                            
                                        <span class="o">&lt;</span><span class="sr">/mat-option&gt;
                                    &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="nb">select</span><span class="o">&gt;</span>
                                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">error</span> <span class="o">*</span><span class="n">ngIf</span><span class="o">=</span><span class="s2">"relation.get('direction').hasError('required')"</span><span class="o">&gt;</span>
                                        <span class="no">Relation</span> <span class="n">direction</span> <span class="n">is</span> <span class="n">required</span><span class="p">.</span>
                                    <span class="nf">&lt;</span><span class="o">/</span><span class="n">mat</span><span class="o">-</span><span class="n">error</span><span class="o">&gt;</span>
                                <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
                                &lt;tb-relation-type-autocomplete
                                        fxFlex class="mat-block"
                                        formControlName="relationType"
                                        required="true"&gt;
                                &lt;/</span><span class="n">tb</span><span class="o">-</span><span class="n">relation</span><span class="o">-</span><span class="n">type</span><span class="o">-</span><span class="n">autocomplete</span><span class="o">&gt;</span>
                            <span class="o">&lt;</span><span class="sr">/div&gt;
                            &lt;div fxLayout="row" fxLayout.xs="column"&gt;
                                &lt;tb-entity-select
                                        fxFlex class="mat-block"
                                        required="true"
                                        formControlName="relatedEntity"&gt;
                                &lt;/</span><span class="n">tb</span><span class="o">-</span><span class="n">entity</span><span class="o">-</span><span class="nb">select</span><span class="o">&gt;</span>
                            <span class="o">&lt;</span><span class="sr">/div&gt;
                        &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
                        <span class="o">&lt;</span><span class="n">div</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"column"</span> <span class="n">fxLayoutAlign</span><span class="o">=</span><span class="s2">"center center"</span><span class="o">&gt;</span>
                            <span class="o">&lt;</span><span class="n">button</span> <span class="n">mat</span><span class="o">-</span><span class="n">icon</span><span class="o">-</span><span class="n">button</span> <span class="n">color</span><span class="o">=</span><span class="s2">"primary"</span>
                                    <span class="n">aria</span><span class="o">-</span><span class="n">label</span><span class="o">=</span><span class="s2">"Remove"</span>
                                    <span class="n">type</span><span class="o">=</span><span class="s2">"button"</span>
                                    <span class="p">(</span><span class="n">click</span><span class="p">)</span><span class="o">=</span><span class="s2">"removeOldRelation(i)"</span>
                                    <span class="n">matTooltip</span><span class="o">=</span><span class="s2">"Remove relation"</span>
                                    <span class="n">matTooltipPosition</span><span class="o">=</span><span class="s2">"above"</span><span class="o">&gt;</span>
                                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">icon</span><span class="o">&gt;</span><span class="n">close</span><span class="o">&lt;</span><span class="sr">/mat-icon&gt;
                            &lt;/</span><span class="n">button</span><span class="o">&gt;</span>
                        <span class="o">&lt;</span><span class="sr">/div&gt;
                    &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="sr">/div&gt;
            &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="sr">/div&gt;
        &lt;div class="relations-list"&gt;
            &lt;div class="mat-body-1" style="padding-bottom: 10px; color: rgba(0,0,0,0.57);"&gt;New Relations&lt;/</span><span class="n">div</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">div</span> <span class="k">class</span><span class="o">=</span><span class="s2">"body"</span> <span class="p">[</span><span class="n">fxShow</span><span class="p">]</span><span class="o">=</span><span class="s2">"relations().length"</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">div</span> <span class="k">class</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">fxLayoutAlign</span><span class="o">=</span><span class="s2">"start center"</span> <span class="n">formArrayName</span><span class="o">=</span><span class="s2">"relations"</span> <span class="o">*</span><span class="n">ngFor</span><span class="o">=</span><span class="s2">"let relation of relations().controls; let i = index;"</span><span class="o">&gt;</span>
                    <span class="o">&lt;</span><span class="n">div</span> <span class="p">[</span><span class="n">formGroupName</span><span class="p">]</span><span class="o">=</span><span class="s2">"i"</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-elevation-z2"</span> <span class="n">fxFlex</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">style</span><span class="o">=</span><span class="s2">"padding: 5px 0 5px 5px;"</span><span class="o">&gt;</span>
                        <span class="o">&lt;</span><span class="n">div</span> <span class="n">fxFlex</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"column"</span><span class="o">&gt;</span>
                            <span class="o">&lt;</span><span class="n">div</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">fxLayoutGap</span><span class="o">=</span><span class="s2">"8px"</span> <span class="n">fxLayout</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"column"</span>  <span class="n">fxLayoutGap</span><span class="p">.</span><span class="nf">xs</span><span class="o">=</span><span class="s2">"0"</span><span class="o">&gt;</span>
                                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">form</span><span class="o">-</span><span class="n">field</span> <span class="k">class</span><span class="o">=</span><span class="s2">"mat-block"</span> <span class="n">style</span><span class="o">=</span><span class="s2">"min-width: 100px;"</span><span class="o">&gt;</span>
                                    <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">label</span><span class="o">&gt;</span><span class="no">Direction</span><span class="o">&lt;</span><span class="sr">/mat-label&gt;
                                    &lt;mat-select formControlName="direction" name="direction"&gt;
                                        &lt;mat-option *ngFor="let direction of entitySearchDirection | keyvalue" [value]="direction.value"&gt;
                                            
                                        &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">option</span><span class="o">&gt;</span>
                                    <span class="o">&lt;</span><span class="sr">/mat-select&gt;
                                    &lt;mat-error *ngIf="relation.get('direction').hasError('required')"&gt;
                                        Relation direction is required.
                                    &lt;/m</span><span class="n">at</span><span class="o">-</span><span class="n">error</span><span class="o">&gt;</span>
                                <span class="o">&lt;</span><span class="sr">/mat-form-field&gt;
                                &lt;tb-relation-type-autocomplete
                                        fxFlex class="mat-block"
                                        formControlName="relationType"
                                        [required]="true"&gt;
                                &lt;/</span><span class="n">tb</span><span class="o">-</span><span class="n">relation</span><span class="o">-</span><span class="n">type</span><span class="o">-</span><span class="n">autocomplete</span><span class="o">&gt;</span>
                            <span class="o">&lt;</span><span class="sr">/div&gt;
                            &lt;div fxLayout="row" fxLayout.xs="column"&gt;
                                &lt;tb-entity-select
                                        fxFlex class="mat-block"
                                        [required]="true"
                                        formControlName="relatedEntity"&gt;
                                &lt;/</span><span class="n">tb</span><span class="o">-</span><span class="n">entity</span><span class="o">-</span><span class="nb">select</span><span class="o">&gt;</span>
                            <span class="o">&lt;</span><span class="sr">/div&gt;
                        &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
                        <span class="o">&lt;</span><span class="n">div</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"column"</span> <span class="n">fxLayoutAlign</span><span class="o">=</span><span class="s2">"center center"</span><span class="o">&gt;</span>
                            <span class="o">&lt;</span><span class="n">button</span> <span class="n">mat</span><span class="o">-</span><span class="n">icon</span><span class="o">-</span><span class="n">button</span> <span class="n">color</span><span class="o">=</span><span class="s2">"primary"</span>
                                    <span class="n">aria</span><span class="o">-</span><span class="n">label</span><span class="o">=</span><span class="s2">"Remove"</span>
                                    <span class="n">type</span><span class="o">=</span><span class="s2">"button"</span>
                                    <span class="p">(</span><span class="n">click</span><span class="p">)</span><span class="o">=</span><span class="s2">"removeRelation(i)"</span>
                                    <span class="n">matTooltip</span><span class="o">=</span><span class="s2">"Remove relation"</span>
                                    <span class="n">matTooltipPosition</span><span class="o">=</span><span class="s2">"above"</span><span class="o">&gt;</span>
                                <span class="o">&lt;</span><span class="n">mat</span><span class="o">-</span><span class="n">icon</span><span class="o">&gt;</span><span class="n">close</span><span class="o">&lt;</span><span class="sr">/mat-icon&gt;
                            &lt;/</span><span class="n">button</span><span class="o">&gt;</span>
                        <span class="o">&lt;</span><span class="sr">/div&gt;
                    &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="sr">/div&gt;
            &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
            <span class="o">&lt;</span><span class="n">div</span><span class="o">&gt;</span>
                <span class="o">&lt;</span><span class="n">button</span> <span class="n">mat</span><span class="o">-</span><span class="n">raised</span><span class="o">-</span><span class="n">button</span> <span class="n">color</span><span class="o">=</span><span class="s2">"primary"</span>
                        <span class="n">type</span><span class="o">=</span><span class="s2">"button"</span>
                        <span class="p">(</span><span class="n">click</span><span class="p">)</span><span class="o">=</span><span class="s2">"addRelation()"</span>
                        <span class="n">matTooltip</span><span class="o">=</span><span class="s2">"Add Relation"</span>
                        <span class="n">matTooltipPosition</span><span class="o">=</span><span class="s2">"above"</span><span class="o">&gt;</span>
                    <span class="no">Add</span>
                <span class="o">&lt;</span><span class="sr">/button&gt;
            &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="sr">/div&gt;
    &lt;/</span><span class="n">div</span><span class="o">&gt;</span>
    <span class="o">&lt;</span><span class="n">div</span> <span class="n">mat</span><span class="o">-</span><span class="n">dialog</span><span class="o">-</span><span class="n">actions</span> <span class="n">fxLayout</span><span class="o">=</span><span class="s2">"row"</span> <span class="n">fxLayoutAlign</span><span class="o">=</span><span class="s2">"end center"</span><span class="o">&gt;</span>
        <span class="o">&lt;</span><span class="n">button</span> <span class="n">mat</span><span class="o">-</span><span class="n">button</span> <span class="n">color</span><span class="o">=</span><span class="s2">"primary"</span>
                <span class="n">type</span><span class="o">=</span><span class="s2">"button"</span>
                <span class="p">[</span><span class="n">disabled</span><span class="p">]</span><span class="o">=</span><span class="s2">"(isLoading$ | async)"</span>
                <span class="p">(</span><span class="n">click</span><span class="p">)</span><span class="o">=</span><span class="s2">"cancel()"</span> <span class="n">cdkFocusInitial</span><span class="o">&gt;</span>
            <span class="no">Cancel</span>
        <span class="o">&lt;</span><span class="sr">/button&gt;
        &lt;button mat-button mat-raised-button color="primary"
                type="submit"
                [disabled]="(isLoading$ | async) || editEntityForm.invalid || !editEntityForm.dirty"&gt;
            Save
        &lt;/</span><span class="n">button</span><span class="o">&gt;</span>
    <span class="o">&lt;</span><span class="sr">/div&gt;
&lt;/</span><span class="n">form</span><span class="o">&gt;</span></code></pre></figure>
</details>

- After input functions, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured actions, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings;
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-5-ce.webp" alt="Click the &quot;plus&quot; icon in the top right corner of the screen again to open a new &quot;Add action&quot; window;" loading="lazy"><figcaption>Click the "plus" icon in the top right corner of the screen again to open a new "Add action" window;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-6-ce.webp" alt="Select the &quot;Action cell button&quot; as the action source. Input a name for the action and select an icon that will represent an action button. With this icon, action will be performed. Select an &quot;Custom action (with HTML template)&quot; action type from the &quot;Action&quot; drop-down menu. In the tabs that appear, select &quot;JavaScript&quot; tab;" loading="lazy"><figcaption>Select the "Action cell button" as the action source. Input a name for the action and select an icon that will represent an action button. With this icon, action will be performed. Select an "Custom action (with HTML template)" action type from the "Action" drop-down menu. In the tabs that appear, select "JavaScript" tab;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-7-ce.webp" alt="Enter a JavaScript function for your custom action;" loading="lazy"><figcaption>Enter a JavaScript function for your custom action;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-8-ce.webp" alt="In &quot;HTML&quot; tab, enter an HTML code for your custom action. After input functions, click the &quot;Add&quot; button;" loading="lazy"><figcaption>In "HTML" tab, enter an HTML code for your custom action. After input functions, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-9-ce.webp" alt="Now in the “Actions” window, you can see the configured actions, so you can double-check the action source, icon, and action type. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the “Actions” window, you can see the configured actions, so you can double-check the action source, icon, and action type. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-10-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-11-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page;" loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page;</figcaption></figure></div>


Perform the actions of adding a new device by clicking the "Add device" action button at the top of the widget.
In the "Add entity" window that opens, select the type of new entity - "Device" and enter its name. Enter the required data and click "Create".


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-12-ce.webp" alt="Perform the actions of adding a new device by clicking the &quot;Add device&quot; action button at the top of the widget;" loading="lazy"><figcaption>Perform the actions of adding a new device by clicking the "Add device" action button at the top of the widget;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-13-ce.webp" alt="In the &quot;Add entity&quot; window that opens, select the type of new entity - &quot;Device&quot; and enter its name. Enter the required data and click &quot;Create&quot;;" loading="lazy"><figcaption>In the "Add entity" window that opens, select the type of new entity - "Device" and enter its name. Enter the required data and click "Create";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-14-ce.webp" alt="The new device has been added." loading="lazy"><figcaption>The new device has been added.</figcaption></figure></div>


Click on the action button next to the name of the device you want to edit. After clicking the action button, the device editing window will open. Make the necessary changes and click "Save".


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-15-ce.webp" alt="Click on the &quot;pencil&quot; icon next to the name of the device you want to edit;" loading="lazy"><figcaption>Click on the "pencil" icon next to the name of the device you want to edit;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-16-ce.webp" alt="After clicking the action button, the device editing window will open. Make the necessary changes and click &quot;Save&quot;;" loading="lazy"><figcaption>After clicking the action button, the device editing window will open. Make the necessary changes and click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/custom-action-with-html-template-17-ce.webp" alt="Changes have been made." loading="lazy"><figcaption>Changes have been made.</figcaption></figure></div>


### Mobile action

Mobile action is explained in mobile application configuration. See [Mobile actions](/docs/mobile/mobile-actions/) for details.

### Open URL

This type of action will transfer you to the resource represented by the URL. This resource can be an HTML page, a document, an image, internal SENTIENT page (for example, Alarms), etc.

We assume that you are already familiar with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter edit widget mode and open "Add action" window;
- As an example for this manual, select "[Widget header button](#widget-header-button)" action source;
- Input a name for the action and select an icon that will represent a button. With this icon, action will be performed;
- Select an "Open URL" action type from the "Action" drop-down menu;
- After selecting an action type, "URL" menu appears. Insert the URL link to the page you want to navigate to when the action button is clicked;
- Optionally, enable the option to open the URL page in a new browser tab;
- Click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings;
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/open-url-1-ce.webp" alt="As an example for this manual, select the &quot;Widget header button&quot; as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select an &quot;Open URL&quot; action type from the &quot;Action&quot; drop-down menu. After selecting an action type, &quot;URL&quot; menu appears. Insert the URL link to the page you want to navigate to when the action button is clicked. Optionally, enable the option to open the URL page in a new browser tab. Finally, click the &quot;Add&quot; button;" loading="lazy"><figcaption>As an example for this manual, select the "Widget header button" as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select an "Open URL" action type from the "Action" drop-down menu. After selecting an action type, "URL" menu appears. Insert the URL link to the page you want to navigate to when the action button is clicked. Optionally, enable the option to open the URL page in a new browser tab. Finally, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/open-url-2-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/open-url-3-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/open-url-4-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page;" loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page;</figcaption></figure></div>


After saving the changes, you can see an icon in the upper right part of the widget. Click this icon. You will be transferred to the URL specified in the action. In our case, it's the "Working with SENTIENT widgets" documentation page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/open-url-5-ce.webp" alt="After saving the changes, you can see an icon in the upper right part of the widget. Click this icon;" loading="lazy"><figcaption>After saving the changes, you can see an icon in the upper right part of the widget. Click this icon;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/types/open-url-6-ce.webp" alt="You will be transferred to the URL specified in the action. In our case, it&#39;s the &quot;Working with SENTIENT widgets&quot; documentation page." loading="lazy"><figcaption>You will be transferred to the URL specified in the action. In our case, it&#39;s the "Working with SENTIENT widgets" documentation page.</figcaption></figure></div>


#### Place map item

The **Place map item** action type allows users to create new entities and immediately place them on the map widget.

<br>
As an example, let&#39;s add a button that allows users to place charging stations on the map:

To start, and to ensure that newly created entities are instantly displayed on the map, you need to configure the data source.

- In the "**Overlays**" section, under the "**Marker**" tab, create a new entity alias as the data source. Name it "**EV stations**".
- Since we&#39;ll be creating entities of the type "**EV station**", set the filter type to "**Asset type**" and specify the type as "**EV station**".
- Apply changes.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/data-source-for-action-1-ce.webp" alt="In the &quot;Overlays&quot; section, under the &quot;Marker&quot; tab, create a new entity alias as the data source. Name it &quot;EV stations&quot;." loading="lazy"><figcaption>In the "Overlays" section, under the "Marker" tab, create a new entity alias as the data source. Name it "EV stations".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/data-source-for-action-2-ce.webp" alt="Since we&#39;ll be creating entities of the type &quot;EV station&quot;, set the filter type to &quot;Asset type&quot; and specify the type as &quot;EV station&quot;. Apply changes." loading="lazy"><figcaption>Since we&#39;ll be creating entities of the type "EV station", set the filter type to "Asset type" and specify the type as "EV station". Apply changes.</figcaption></figure></div>


Now let&#39;s move on to configuring the action:

- Scroll down to the "**Actions**" section and click the "**Add action**" button.
- A new window will open, displaying all your created actions. Click the "plus" icon button in the top-right corner to add one.
- Select the action source as "**Widget header button**", enter a name for the button, and choose its type.
- Optionally, change the icon that will appear next to the button or hide it entirely. You can also set a custom color for the button.
- From the dropdown menu, select the type of action to be performed. In our case, it&#39;s "**Place map item**".
- Next, choose the **type of map item** to be placed — we&#39;ll be placing a "**Marker**".
- The **custom action function** field already contains a default function that opens a dialog for creating a device or an asset — exactly what we need.
- In the "**Action**" section, choose "**Place map item**" from the dropdown menu. Select the type of map item to be placed — in our case, it&#39;s "**Marker**". The Custom action function field contains a default function that opens a dialog to create a device or an asset — exactly what we need.
- Then click "**Add**".
- Apply all changes and save the dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/action-1-ce.webp" alt="Scroll down to the &quot;Actions&quot; section and click the &quot;Add action&quot; button." loading="lazy"><figcaption>Scroll down to the "Actions" section and click the "Add action" button.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-2-ce.webp" alt="A new window will open, displaying all your created actions. Click the &quot;plus&quot; icon button in the top-right corner to add one." loading="lazy"><figcaption>A new window will open, displaying all your created actions. Click the "plus" icon button in the top-right corner to add one.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-3-ce.webp" alt="Select the action source as &quot;Widget header button&quot;, enter a name for the button, and choose its type." loading="lazy"><figcaption>Select the action source as "Widget header button", enter a name for the button, and choose its type.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-4-ce.webp" alt="Optionally, change the icon that will appear next to the button or hide it entirely. You can also set a custom color for the button." loading="lazy"><figcaption>Optionally, change the icon that will appear next to the button or hide it entirely. You can also set a custom color for the button.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-5-ce.webp" alt="From the dropdown menu, select the type of action to be performed. In our case, it&#39;s &quot;Place map item&quot;. Next, choose the type of map item to be placed — we&#39;ll be placing a &quot;Marker&quot;. The custom action function field already contains a default function that opens a dialog for creating a device or an asset — exactly what we need. Then, click &quot;Add&quot;." loading="lazy"><figcaption>From the dropdown menu, select the type of action to be performed. In our case, it&#39;s "Place map item". Next, choose the type of map item to be placed — we&#39;ll be placing a "Marker". The custom action function field already contains a default function that opens a dialog for creating a device or an asset — exactly what we need. Then, click "Add".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-6-ce.webp" alt="Apply all changes and save the dashboard." loading="lazy"><figcaption>Apply all changes and save the dashboard.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-7-ce.webp" alt="A new action button labeled &quot;Add EV station&quot; has now appeared at the top of the map." loading="lazy"><figcaption>A new action button labeled "Add EV station" has now appeared at the top of the map.</figcaption></figure></div>


A new action button labeled "**Add EV station**" has now appeared at the top of the map. Let&#39;s use it.


1. Click the newly created "Add EV station" button. Then, find the location on the map where you want to place the EV station and click on it.

1. In the "Add entity" dialog that appears, make sure to enter a name for the new entity and select its type — Asset. The other fields are optional. Then click "Create".

1. The new "EV station" marker is now added to the map.


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/action-place-marker-1-ce.webp" alt="Click the newly created &quot;Add EV station&quot; button. Then, find the location on the map where you want to place the EV station and click on it." loading="lazy"><figcaption>Click the newly created "Add EV station" button. Then, find the location on the map where you want to place the EV station and click on it.</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-place-marker-2-ce.webp" alt="In the &quot;Add entity&quot; dialog that appears, make sure to enter a name for the new entity and select its type — Asset. The other fields are optional. Then click &quot;Create&quot;." loading="lazy"><figcaption>In the "Add entity" dialog that appears, make sure to enter a name for the new entity and select its type — Asset. The other fields are optional. Then click "Create".</figcaption></figure><figure><img src="/images/user-guide/widgets/maps/action-place-marker-3-ce.webp" alt="The new &quot;EV station&quot; marker is now added to the map." loading="lazy"><figcaption>The new "EV station" marker is now added to the map.</figcaption></figure></div>


Go to the "**Assets**" page — there you&#39;ll find your newly created asset, "**EV station 1**".


<div class="st-gallery"><figure><img src="/images/user-guide/widgets/maps/action-created-asset-1-ce.webp" alt="Go to the &quot;Assets&quot; page — there you&#39;ll find your newly created asset, &quot;EV station 1&quot;." loading="lazy"><figcaption>Go to the "Assets" page — there you&#39;ll find your newly created asset, "EV station 1".</figcaption></figure></div>


## Action sources

Action sources are specific actions that need to be performed to achieve a goal (like clicking a widget header button, double-clicking a row, or a map's marker). They vary across different widgets. 
Action sources will be explained separately for each widget type, separately using an example of the most commonly used type of action "[Navigate to new dashboard state](/docs/user-guide/ui/widget-actions/#navigate-to-new-dashboard-state)". 

Next, we will demonstrate how to utilize each action source using the "Entities table" widget as an example.
If you're unfamiliar with adding an Entity table widget to your dashboard, you can [learn how to do so here](/docs/getting-started-guides/helloworld/#step-32-add-an-entities-table-widget).

### Action cell button

The "Action cell button" action adds an action button to each individual entity in the widget, such as deleting devices/assets or editing them.
This action button is often used in the "Entity table" widget. In the example of this widget, let's consider the use of "Action cell button".
Clicking on the action icon of a selected entity will transfer us to another state with detailed information about that entity.

We assume that you have already added [a new state](/docs/user-guide/dashboards/#states) to the dashboard and familiarized yourself with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter edit widget mode and open "Add action" window;
- Select "Action cell button" as the action source;
- Input a name for the action and select an icon that will represent a button. With this icon, action will be performed;
- Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu;
- After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously [created state](/docs/user-guide/dashboards/#states) you'd like to be transitioned to;
- When the desired state has been selected, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings.
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/action-cell-button-1-ce.webp" alt="Select &quot;Widget header button&quot; as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select a &quot;Navigate to new dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select "Widget header button" as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/action-cell-button-2-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/action-cell-button-3-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/action-cell-button-4-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


As you can see, there is an action cell button next to each entity name. By clicking this button, the corresponding action will be executed, namely transitioning to the chosen state.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/action-cell-button-5-ce.webp" alt="After saving the changes, you can see the action button next to the device name to open the device details. Click this button;" loading="lazy"><figcaption>After saving the changes, you can see the action button next to the device name to open the device details. Click this button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/action-cell-button-6-ce.webp" alt="You will be transferred to the state specified in the action." loading="lazy"><figcaption>You will be transferred to the state specified in the action.</figcaption></figure></div>


### On cell click 

<i>* only in Entities table, Alarms table, Device admin table, and Asset admin table widgets.</i>

The "On cell click" action adds a function for each cell in the specified table column. 

Let's explore how this action works using the "Entities table" widget as an example. It displays a list of devices and their latest temperature and humidity readings.
We will configure this widget so that clicking on a cell in a specific column will open a popup with detailed telemetry information for the selected device.

For this, we will need to add an action for each column of the table.

We assume that you have already added two new [states](/docs/user-guide/dashboards/#states) to the dashboard and familiarized yourself with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

Let's add the first action for the "temperature" column:

- Select the "On cell click " as the action source;
- From the "Column index" drop-down menu, select the "temperature" column to which this action will be applied;
- Enter a name for the action, and optionally, choose an icon;
- For the action type, select "Navigate to new dashboard state" from the drop-down menu;
- Specify the "Target dashboard state" which will display detailed temperature data for the selected device;
- Select the "Open in popover" option in the "Dashboard state display options" field;
- Specify the placement of the popover;
- Optionally, specify the width and height of the popover;
- Click "Add" to add the action.

We have configured an action for the "temperature" column.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-1-ce.webp" alt="Select the &quot;On cell click&quot; as the action source. From the &quot;Column index&quot; drop-down menu, select the &quot;temperature&quot; column to which this action will be applied;" loading="lazy"><figcaption>Select the "On cell click" as the action source. From the "Column index" drop-down menu, select the "temperature" column to which this action will be applied;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-2-1-ce.webp" alt="Enter a name for the action, and optionally, choose an icon. For the action type, select &quot;Navigate to new dashboard state&quot; from the drop-down menu. Specify the &quot;Target dashboard state&quot; which will display detailed temperature data for the selected device;" loading="lazy"><figcaption>Enter a name for the action, and optionally, choose an icon. For the action type, select "Navigate to new dashboard state" from the drop-down menu. Specify the "Target dashboard state" which will display detailed temperature data for the selected device;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-2-2-ce.webp" alt="Select the &quot;Open in popover&quot; option in the &quot;Dashboard state display options&quot; field, and specify the placement of the popover. Optionally, specify the width and height of the popover. Click &quot;Add&quot; to add the action;" loading="lazy"><figcaption>Select the "Open in popover" option in the "Dashboard state display options" field, and specify the placement of the popover. Optionally, specify the width and height of the popover. Click "Add" to add the action;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-3-ce.webp" alt="We have configured an action for the &quot;temperature&quot; column." loading="lazy"><figcaption>We have configured an action for the "temperature" column.</figcaption></figure></div>


Now, we need to add another action for the "humidity" column:

- Click the "plus" icon in the top right corner of the "Actions" window to start adding a new action;
- Repeat the steps as above but select the "humidity" column this time from the "Column index" drop-down menu;
- Specify the "Target dashboard state" which will display detailed humidity data for the selected device;
- Select the "Open in popover" option in the "Dashboard state display options" field;
- Specify the placement of the popover;
- Optionally, specify the width and height of the popover;
- Click "Add" to add the action;
- After configuring the actions, click "Save" and then "Apply" to save the widget settings;
- Save your entire dashboard configuration by clicking "Save" located in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-4-ce.webp" alt="Click the &quot;plus&quot; icon in the top right corner of the &quot;Actions&quot; window to start adding a new action;" loading="lazy"><figcaption>Click the "plus" icon in the top right corner of the "Actions" window to start adding a new action;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-5-ce.webp" alt="Select the &quot;On cell click&quot; as the action source. From the &quot;Column index&quot; drop-down menu, select the &quot;humidity&quot; column to which this action will be applied;" loading="lazy"><figcaption>Select the "On cell click" as the action source. From the "Column index" drop-down menu, select the "humidity" column to which this action will be applied;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-6-1-ce.webp" alt="Enter a name for the action, and optionally, choose an icon. For the action type, select &quot;Navigate to new dashboard state&quot; from the drop-down menu. Specify the &quot;Target dashboard state&quot; which will display detailed humidity data for the selected device;" loading="lazy"><figcaption>Enter a name for the action, and optionally, choose an icon. For the action type, select "Navigate to new dashboard state" from the drop-down menu. Specify the "Target dashboard state" which will display detailed humidity data for the selected device;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-6-2-ce.webp" alt="Select the &quot;Open in popover&quot; option in the &quot;Dashboard state display options&quot; field, and specify the placement of the popover. Optionally, specify the width and height of the popover. Click &quot;Add&quot; to add the action;" loading="lazy"><figcaption>Select the "Open in popover" option in the "Dashboard state display options" field, and specify the placement of the popover. Optionally, specify the width and height of the popover. Click "Add" to add the action;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-7-ce.webp" alt="After configuring the actions, click &quot;Save&quot;;" loading="lazy"><figcaption>After configuring the actions, click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-8-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-9-ce.webp" alt="Save your entire dashboard configuration by clicking &quot;Save&quot; located in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save your entire dashboard configuration by clicking "Save" located in the upper right corner of the dashboard page.</figcaption></figure></div>


Now, when you click on a cell in the "temperature" column for any device, an action will be performed: a popup window will appear with detailed information about the temperature of the selected device.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-10-ce.webp" alt="Click on a cell in the &quot;temperature&quot; column for any device to perform an action;" loading="lazy"><figcaption>Click on a cell in the "temperature" column for any device to perform an action;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-11-ce.webp" alt="A popup window will appear with detailed information about the temperature of the selected device." loading="lazy"><figcaption>A popup window will appear with detailed information about the temperature of the selected device.</figcaption></figure></div>


Similarly, clicking on a cell in the "humidity" column will appear with detailed information about the humidity of the selected device.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-12-ce.webp" alt="Click on a cell in the &quot;humidity&quot; column for any device to perform an action;" loading="lazy"><figcaption>Click on a cell in the "humidity" column for any device to perform an action;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-cell-click-13-ce.webp" alt="A popup window will appear with detailed information about the humidity of the selected device." loading="lazy"><figcaption>A popup window will appear with detailed information about the humidity of the selected device.</figcaption></figure></div>


### Widget header button

The "Widget header button" action adds an action button in the header of the widget. Clicking this button executes an action. This button is responsible for the whole widget, not for separate entities. 
The widget header button is the most commonly used action source, and it can be found in all widgets. To configure the _Widget header button_ action source, you should follow these steps:

We assume that you have already added [a new state](/docs/user-guide/dashboards/#states) to the dashboard and familiarized yourself with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter edit widget mode and open "Add action" window;
- Select "Widget header button" as the action source;
- Input a name for the action and select an icon that will represent a button. With this icon, action will be performed;
- Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu;
- After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously [created state](/docs/user-guide/dashboards/#states) you'd like to be transitioned to;
- When the desired state has been selected, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings.
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/widget-header-button-1-ce.webp" alt="Select &quot;Widget header button&quot; as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select a &quot;Navigate to new dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select "Widget header button" as the action source. Input a name for the action and select an icon that will represent a button. With this icon, action will be performed. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/widget-header-button-2-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/widget-header-button-3-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/widget-header-button-4-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


As you see now, an action button has appeared in the header of the widget. After you click it, action will be performed, namely, the transition to the chosen state.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/widget-header-button-5-ce.webp" alt="After saving the changes, you can see the action button in the header of the widget. Click this button;" loading="lazy"><figcaption>After saving the changes, you can see the action button in the header of the widget. Click this button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/widget-header-button-6-ce.webp" alt="You will be transferred to the state specified in the action." loading="lazy"><figcaption>You will be transferred to the state specified in the action.</figcaption></figure></div>


### On row click

The "On row click" action triggers an action when a row in the widget is clicked. This action button is often used in the "Entity table" widget. Let's illustrate the use of the "On row click" action with the aforementioned widget as an example. Clicking on a row of the selected entity in the widget will navigate us to another state with detailed information about that entity.

We assume that you have already added [a new state](/docs/user-guide/dashboards/#states) to the dashboard and familiarized yourself with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter edit widget mode and open "Add action" window;
- Select "On row click" as the action source;
- Input a name for the action. Optionally, select an icon;
- Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu;
- After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously [created state](/docs/user-guide/dashboards/#states) you'd like to be transitioned to;
- When the desired state has been selected, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings.
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-click-1-ce.webp" alt="Select &quot;On row click&quot; as the action source. Input a name for the action. Optionally, select an icon. Select a &quot;Navigate to new dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select "On row click" as the action source. Input a name for the action. Optionally, select an icon. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-click-2-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-click-3-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-click-4-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


Click on any entity row to perform an action, namely, to navigate to the selected state where detailed information about the chosen device is displayed.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-click-5-ce.webp" alt="Click on the row of any entity to navigate to the state;" loading="lazy"><figcaption>Click on the row of any entity to navigate to the state;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-click-6-ce.webp" alt="You will be transferred to the state specified in the action." loading="lazy"><figcaption>You will be transferred to the state specified in the action.</figcaption></figure></div>


### On row double click

The "On row double click" action triggers an action when a row in the widget is double-clicked. Let's explore its use with the "Entities table" widget, where this action is often used.
Double-clicking on a row of the selected entity in the widget will navigate us to another state with detailed information about that entity.

We assume that you have already added [a new state](/docs/user-guide/dashboards/#states) to the dashboard and familiarized yourself with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter edit widget mode and open "Add action" window;
- Select "On row double click" as the action source;
- Input a name for the action. Optionally, select an icon;
- Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu;
- After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously [created state](/docs/user-guide/dashboards/#states) you'd like to be transitioned to;
- When the desired state has been selected, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings.
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-double-click-1-ce.webp" alt="Select &quot;On row double click&quot; as the action source. Input a name for the action. Optionally, select an icon. Select a &quot;Navigate to new dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select "On row double click" as the action source. Input a name for the action. Optionally, select an icon. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-double-click-2-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-double-click-3-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-double-click-4-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


Double-click on an entity row to perform an action, namely, navigate to the selected state. In our example, clicking a node will navigate you to a state displaying the details of the selected node.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-double-click-5-ce.webp" alt="Double click on the row of any entity to navigate to the state;" loading="lazy"><figcaption>Double click on the row of any entity to navigate to the state;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-row-double-click-6-ce.webp" alt="You will be transferred to the state specified in the action." loading="lazy"><figcaption>You will be transferred to the state specified in the action.</figcaption></figure></div>


### On node selected

<i>* only in Entities Hierarchy widget.</i>

In this example, we'll add an "Entity hierarchy" widget to our dashboard. Entities Hierarchy widget displays the hierarchy of entities based on their relations.
For more information about entities and relations, you can [read here](/docs/user-guide/entities-and-relations/#step-1-provision-entities-and-relations). Clicking on any entity (node) in the Entities hierarchy will perform the configured action.

We assume that you have already added [a new state](/docs/user-guide/dashboards/#states) to the dashboard. Let's start setting up the action:


1. Enter dashboard edit mode. Click the "Add widget" button at the top of the screen or click the large "Add new widget" icon in the center of the screen (if this is your first widget on this dashboard);

1. Find the "Entity widgets" widget bundle and click on it;

1. Select the "Entity hierarchy" widget;

1. Specify the data source for the widget and navigate to the "Actions" tab. Click the "plus" icon in the top right corner of the screen to open a new "Add action" window;

1. Select "On node selected" as the action source. Input a name for the action. Optionally, select an icon. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;

1. Now in the "Actions" window, you can see the configured action. Click "Apply" to save the widget settings;

1. Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-node-selected-1-ce.webp" alt="Enter dashboard edit mode. Click the &quot;Add widget&quot; button at the top of the screen or click the large &quot;Add new widget&quot; icon in the center of the screen (if this is your first widget on this dashboard);" loading="lazy"><figcaption>Enter dashboard edit mode. Click the "Add widget" button at the top of the screen or click the large "Add new widget" icon in the center of the screen (if this is your first widget on this dashboard);</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-node-selected-2-ce.webp" alt="Find the &quot;Entity widgets&quot; widget bundle and click on it;" loading="lazy"><figcaption>Find the "Entity widgets" widget bundle and click on it;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-node-selected-3-ce.webp" alt="Select the &quot;Entity hierarchy&quot; widget;" loading="lazy"><figcaption>Select the "Entity hierarchy" widget;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-node-selected-4-ce.webp" alt="Specify the data source for the widget and navigate to the &quot;Actions&quot; tab. Click the &quot;plus&quot; icon in the top right corner of the screen to open a new &quot;Add action&quot; window;" loading="lazy"><figcaption>Specify the data source for the widget and navigate to the "Actions" tab. Click the "plus" icon in the top right corner of the screen to open a new "Add action" window;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-node-selected-5-ce.webp" alt="Select &quot;On node selected&quot; as the action source. Input a name for the action. Optionally, select an icon. Select a &quot;Navigate to new dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select "On node selected" as the action source. Input a name for the action. Optionally, select an icon. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-node-selected-6-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-node-selected-7-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


To perform an action you should click any of the nodes in the Entities hierarchy. In our example, clicking a node will navigate to a state that displays the details of the selected node.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-node-selected-8-ce.webp" alt="To perform an action you should click any of the nodes in the Entities hierarchy;" loading="lazy"><figcaption>To perform an action you should click any of the nodes in the Entities hierarchy;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-node-selected-9-ce.webp" alt="You will be transferred to the state specified in the action." loading="lazy"><figcaption>You will be transferred to the state specified in the action.</figcaption></figure></div>


### On HTML element click

<table style="width:auto"><thead><tr><td style="text-align: center"><strong><em>Only for HTML widgets</em></strong></td></tr></thead></table> 

**On HTML element click** allows you to trigger an action (navigate to a state, open a link, execute a custom action, etc.) when a user clicks on an element in the HTML layout of the widget.   

<br><b><font size="3">How it works</font></b>

When configuring **On HTML element click**, the `id` attribute is the link between the **HTML code** of the widget and the **action** defined in the widget&#39;s **Actions** tab.

You can assign the `id` to any HTML element (e.g., `<div>`, `<span>`, `<p>`, `<h1>`, `<button>`). Typically, the `id` is applied to a container element (like `<p>` or `<div>`), so the entire block becomes clickable.   

```html
<p id="details" class="blue-box">
    Current temperature: <span>22.5 °C</span>
</p>
```

<b><font size="3">Tips</font></b>
- Works **only with HTML widgets**; for tables, charts, and others use their specific action sources ([On row click](#on-row-click), [On cell click](#on-cell-click), [On node selected](#on-node-selected), etc.).
- `ID` must match **Name** exactly (case-sensitive).
- For more advanced scenarios (dialogs, forms), use [Custom action with HTML template](#custom-action-with-html-template) / *widgetContext.dialogs* / *widgetContext.customDialog* in widgets that support it.

<b><font size="3">Configuration step by step</font></b>
1. Enter **widget edit mode** → go to the **Actions** tab → click **+** (**Add action**). 
2. In Action source, select **On HTML element click**.
3. Set a **Name** (this will also serve as the **ID** for the HTML element).
4. In **Action**, choose the action type (e.g., [Navigate to new dashboard state](#navigate-to-new-dashboard-state)) and specify the target state.
5. Save the action (**Add**).
6. Go to the **Appearance** tab → **HTML** section, and add an element with an `id` that **exactly matches** the action&#39;s Name. 
7. Apply changes (**Apply**) and **save the dashboard**.

After saving, SENTIENT "listens" for clicks on the element with an id that matches the Name of the created action for that widget. If found, the chosen action type (navigate, update state, custom action, etc.) is executed.

<br><b><font size="3">Example: Markdown/HTML Card widget — Click the blue area</font></b>

**Preparation:**
1. Add a [Markdown/HTML Card](/docs/user-guide/widgets/cards/markdown-html-card/) widget to your dashboard using the HTML and CSS provided below.  
2. [Create a new dashboard state](/docs/user-guide/dashboards/#states) with device **temperature details**.

**Alternative:** You can [download a pre-configured dashboard](/docs/user-guide/widgets/resources/smart_device_details.json) with the Markdown/HTML Card widget and the details state already set up, then [import](/docs/user-guide/dashboards/#import-dashboard) it into your SENTIENT instance.


<div class="st-callout info">


**Important:** After importing, update the **target entity** and **data key** in the widget&#39;s datasource.


</div>


<b><font size="3">Add the Markdown/HTML Card</font></b>

**Markdown/HTML pattern:**

```html
const entity = data[0];
const color = entity.temperature > 25 ? "red" : entity.temperature > 20 ? 'green' : 'blue'
const entityName = `### Temperature value card\n - Current entity: <span >${entity.entityName}</span>\n `
const temp = `- Current temperature: <span style="color:${color};">${entity.temperature.toFixed(1)} °C</span>\n `
return entityName + temp;
```


**Markdown/HTML CSS:**

```css
.office-card {
  box-sizing: border-box;
  padding: 16px;
  margin: 6px 0;
  text-align: center;
  font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, "Noto Sans";
}

.office-card h3 {
  margin: 0 0 12px;
  font-size: 24px;
}

.blue-box {
  background: #1870741A;
  border: 2px solid #187074;
  border-radius: 10px;
  padding: 10px;
  margin: 8px 0;
  font-weight: 700;
}

.green-box {
  background: #4CAF501A;
  border: 2px solid #4CAF50;
  border-radius: 10px;
  padding: 10px;
  margin: 6px 0;
  font-weight: 700;
}

.temp-value,
.hum-value {
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}
```


<b><font size="3">Add the action</font></b>

1. Enter **widget edit mode** → go to the **Actions** tab → click **+** (**Add action**).
2. Choose **Action source**: **On HTML element click**. 
3. Enter **details** as the **action name**. 
4. In **Action**, select **Navigate to new dashboard state**. 
5. In **Target dashboard state**, select the state you [created earlier](/docs/user-guide/dashboards/#states). 
6. Click **Add** to save the action.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-html-element-click-1-ce.webp" alt="Enter widget edit mode → go to the Actions tab → click + (Add action). Add the action: Choose Action source: On HTML element click; Enter details as the action name; In Action, select Navigate to new dashboard state; In Target dashboard state, select the state you created earlier; Click Add to save the action." loading="lazy"><figcaption>Enter <b>widget edit mode</b> → go to the <b>Actions</b> tab → click <b>+</b> (<b>Add action</b>).<br> <b>Add the action</b>: Choose <b>Action source</b>: <b>On HTML element click</b>; Enter <b>details</b> as the action name; In <b>Action</b>, select <b>Navigate to new dashboard state</b>; In <b>Target dashboard state</b>, select the state you created earlier; Click <b>Add</b> to save the action.</figcaption></figure></div>


<b><font size="3">Add id to the HTML</font></b>

1. Go to the **Appearance** tab → **HTML** section. 
2. Add an element with the `id=details` to the `<p class="blue-box">` line.   
   Replace it with:

    ```
    <p id="details" class="blue-box">
    ```
    

    This makes the entire blue-box block clickable and tied to the **details** action.

3. Apply changes (**Apply**) and **save the dashboard**.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-html-element-click-2-ce.webp" alt="Add id to the HTML: Go to the Appearance tab → HTML section; Add an element with the id details to the HTML. Apply changes (Apply) and save the dashboard." loading="lazy"><figcaption><b>Add id to the HTML</b>: Go to the <b>Appearance</b> tab → <b>HTML</b> section; Add an element with the id <b>details</b> to the HTML. Apply changes (<b>Apply</b>) and <b>save the dashboard</b>.</figcaption></figure></div>


<b><font size="3">Result</font></b>

Clicking the **blue block with the current temperature** will execute the configured action and navigate to your target state.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-html-element-click-3-ce.webp" alt="Clicking the blue block with the current temperature will execute the configured action (navigate to your target state)." loading="lazy"><figcaption>Clicking the blue block with the current temperature will execute the configured action (navigate to your target state).</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/sources/on-html-element-click-4-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


### Map widget action sources

Map widget has unique action sources that need to be considered separately. 

Let&#39;s start by adding a map widget, namely OpenStreetMap widget. We have a separate guide on [how to create and configure a map widget](/docs/user-guide/widgets/map-widgets/). Please, familiarize yourself with it first.


![image](/images/user-guide/ui/widgets/actions/guide/map-widget-action-sources-1-ce.webp)


Now it&#39;s time to add an action.
All further explanations concerning actions assume that you have already added [a new state](/docs/user-guide/dashboards/#states) to the dashboard and familiarized yourself with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

#### On circle click

Circle is a plane figure, boundary points of which are always the same distance away from a fixed central point. We use circle which is based on coordinates that are specified within the device we use.
Learn how to add a circle on the Map widget, by reading [here](/docs/user-guide/widgets/map-widgets/#circle-settings).


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-circle-click-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- Enter edit widget mode and open "Add action" window;
- Select "On circle click" as the action source;
- Input a name for the action. Optionally, select an icon;
- Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu;
- After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously [created state](/docs/user-guide/dashboards/#states) you'd like to be transitioned to;
- When the desired state has been selected, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings.
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-circle-click-2-ce.webp" alt="Select &quot;On circle click&quot; as the action source. Input a name for the action. Optionally, select an icon. Select a &quot;Navigate to new dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select "On circle click" as the action source. Input a name for the action. Optionally, select an icon. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-circle-click-3-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-circle-click-4-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


After clicking on the circle on the map, action will be performed, namely, the transition to the specified state.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-circle-click-5-ce.webp" alt="Clicking on the circle on the map will take you to the specified state." loading="lazy"><figcaption>Clicking on the circle on the map will take you to the specified state.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-circle-click-6-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


#### On marker click

The action will be executed by clicking on the red entity marker on the map.

- Enter edit widget mode and open "Add action" window;
- Select "On marker click" as the action source;
- Input a name for the action. Optionally, select an icon;
- Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu;
- After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously [created state](/docs/user-guide/dashboards/#states) you'd like to be transitioned to;
- When the desired state has been selected, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings.
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-marker-click-1-ce.webp" alt="Select &quot;On marker click&quot; as the action source. Input a name for the action. Optionally, select an icon. Select a &quot;Navigate to new dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select "On marker click" as the action source. Input a name for the action. Optionally, select an icon. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-marker-click-2-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-marker-click-3-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


Clicking on the marker on the map will take you to the specified state.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-marker-click-4-ce.webp" alt="Clicking on the marker on the map will take you to the specified state;" loading="lazy"><figcaption>Clicking on the marker on the map will take you to the specified state;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-marker-click-5-ce.webp" alt="You will be transferred to the state specified in the action." loading="lazy"><figcaption>You will be transferred to the state specified in the action.</figcaption></figure></div>


#### On polygon click

Polygon is a plane figure that’s described by a finite number of dots. We use polygon which is based on coordinates specified within the device we use, but you can use any other entity.
You may mark your assets and any other entities with a polygon option.
Learn how to add a polygon on the Map widget, by reading [here](/docs/user-guide/widgets/map-widgets/#polygon-settings).


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-polygon-click-1-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


- Enter edit widget mode and open "Add action" window;
- Select "On polygon click" as the action source;
- Input a name for the action. Optionally, select an icon;
- Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu;
- After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously [created state](/docs/user-guide/dashboards/#states) you'd like to be transitioned to;
- When the desired state has been selected, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings.
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-polygon-click-2-ce.webp" alt="Select &quot;On polygon click&quot; as the action source. Input a name for the action. Optionally, select an icon. Select a &quot;Navigate to new dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select "On polygon click" as the action source. Input a name for the action. Optionally, select an icon. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-polygon-click-3-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-polygon-click-4-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure></div>


To execute an action click anywhere inside the polygon.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-polygon-click-5-ce.webp" alt="To execute an action click anywhere inside the polygon." loading="lazy"><figcaption>To execute an action click anywhere inside the polygon.</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/on-polygon-click-6-ce.webp" alt="You will be transferred to the state specified in the action." loading="lazy"><figcaption>You will be transferred to the state specified in the action.</figcaption></figure></div>


#### Tooltip tag action

You can configure the map widget settings so that when you click on a marker, a tooltip appears. The tooltip can contain a link that will execute the configured action.
Please note, in this manual explains only the basic usage of the tooltip tag action source. It is possible to configure several links for various devices/assets that return different values.
Use [the tooltip function](/docs/user-guide/widgets/map-widgets/#tooltip-function) in the advanced mode of the map widget to accomplish this.

- Enter edit widget mode and open "Add action" window;
- Select "Tooltip tag action" as the action source;
- Input a name for the action. Optionally, select an icon;
- Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu;
- After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously [created state](/docs/user-guide/dashboards/#states) you'd like to be transitioned to;
- When the desired state has been selected, click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type.
- Now navigate to the "Appearance" tab of the widget;
- Scroll down to the Tooltip configuration and toggle the "Show tooltip" checkbox;
- In the Tooltip line find link-act name and input an ID of the action which is its name in a format:

```
<link-act name='TooltipTag'>Navigate to the ${entityName}</link-act>
```


where _TooltipTag_ is an action name and _Navigate to the Building A_ is the text that will be shown as a link on a tooltip.

- Click "Apply" to save the widget settings;
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/tooltip-tag-action-1-ce.webp" alt="Select &quot;Tooltip tag action&quot; as the action source. Input a name for the action. Optionally, select an icon. Select a &quot;Navigate to new dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. After choosing an action type, the &quot;Target dashboard state&quot; drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Select "Tooltip tag action" as the action source. Input a name for the action. Optionally, select an icon. Select a "Navigate to new dashboard state" action type from the "Action" drop-down menu. After choosing an action type, the "Target dashboard state" drop-down menu appears. Select a previously created state you&#39;d like to be transitioned to. When the desired state has been selected, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/tooltip-tag-action-2-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Now navigate to the &quot;Appearance&quot; tab;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Now navigate to the "Appearance" tab;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/tooltip-tag-action-3-ce.webp" alt="Scroll down to the Tooltip configuration and toggle the &quot;Show tooltip&quot; checkbox. In the Tooltip line find link-act name and input an ID of the action which is its name. After, click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Scroll down to the Tooltip configuration and toggle the "Show tooltip" checkbox. In the Tooltip line find link-act name and input an ID of the action which is its name. After, click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/tooltip-tag-action-4-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


Click on the marker on the map to display the tooltip. To perform the action, click on the link text at the bottom of the tooltip.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/tooltip-tag-action-5-ce.webp" alt="Click on the marker on the map to display the tooltip. To perform the action, click on the link text at the bottom of the tooltip;" loading="lazy"><figcaption>Click on the marker on the map to display the tooltip. To perform the action, click on the link text at the bottom of the tooltip;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/tooltip-tag-action-6-ce.webp" alt="You will be transferred to the state specified in the action." loading="lazy"><figcaption>You will be transferred to the state specified in the action.</figcaption></figure></div>


## Special actions settings

### Open right dashboard layout (mobile view)


<div class="st-callout info">


These settings will be useful to you if you are using the [SENTIENT Mobile Application](/docs/mobile/). If you're not using it yet, [give it a try](/docs/mobile/getting-started/)! Stay informed about all events in your IoT solution, even when you're on the go.


</div>


Often, users need to see updated information about an entity from one widget on another widget next to it. For example, we have a list of assets in the "Entity table" widget, and we want to see their details in the "Time series chart" widget next to it. 
On the desktop, this is easy to set up by placing the two widgets side by side and selecting the action type "[Update current dashboard state](#update-current-dashboard-state)". 
However, on the responsive screen of the [SENTIENT Mobile Application](/docs/mobile/) the widgets are automatically stacked one below the other. This means that you'll need to scroll down to view the relevant information on the second widget.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-1-ce.webp" alt="From the desktop, when you click on the row of any entity on the dashboard, the information panel updates, and the details of the selected entity are displayed in the &quot;Time series chart&quot; widget next to the &quot;Entities table&quot; widget;" loading="lazy"><figcaption>From the desktop, when you click on the row of any entity on the dashboard, the information panel updates, and the details of the selected entity are displayed in the "Time series chart" widget next to the "Entities table" widget;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-2-ce.webp" alt="In mobile mode, the action will also be executed when you click on a row of the entity. However, you&#39;ll need to scroll down to see the details of the selected entity in the &quot;Time series chart&quot; widget." loading="lazy"><figcaption>In mobile mode, the action will also be executed when you click on a row of the entity. However, you&#39;ll need to scroll down to see the details of the selected entity in the "Time series chart" widget.</figcaption></figure></div>


[Layouts](/docs/user-guide/dashboards/#layouts) feature solves this issue. To configure layouts, you should:


1. Enter the Dashboard&#39;s edit mode On the left top of the window click "Manage layouts" icon;

1. In the opened "Manage layouts" window, turn on the "Divider" option;

1. Now we have two layouts. Optionally, you can adjust the size of the windows in a certain percentage ratio relative to each other. Click "Save";


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-4-ce.webp" alt="Enter the Dashboard&#39;s edit mode On the left top of the window click &quot;Manage layouts&quot; icon;" loading="lazy"><figcaption>Enter the Dashboard&#39;s edit mode On the left top of the window click "Manage layouts" icon;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-5-ce.webp" alt="In the opened &quot;Manage layouts&quot; window, turn on the &quot;Divider&quot; option;" loading="lazy"><figcaption>In the opened "Manage layouts" window, turn on the "Divider" option;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-6-ce.webp" alt="Now we have two layouts. Optionally, you can adjust the size of the windows in a certain percentage ratio relative to each other. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now we have two layouts. Optionally, you can adjust the size of the windows in a certain percentage ratio relative to each other. Click "Save";</figcaption></figure></div>


Now we need to add the "Time series chart" widget to the right layout:


1. Click the "Add new widget" button in the center of the right layout;

1. Find the "Charts" widget bundle and click on it;

1. Select the "Time series chart" widget;

1. Navigate to the "Entity alias" tab in the "Datasource" section. Enter the desirable alias name in the "Entity alias" field and click the "Create a new one!" button;

1. Select the "Entity from dashboard state" from the "Filter type" field and click "Add";

1. Replace the label of the "temperature" key with <b>${entityName}</b>. Then, click "Add" to add new widget on the dashboard;

1. Resize the "Time series chart" widget until you are happy with its size.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-7-ce.webp" alt="Click the &quot;Add new widget&quot; button in the center of the right layout;" loading="lazy"><figcaption>Click the "Add new widget" button in the center of the right layout;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-8-ce.webp" alt="Find the &quot;Charts&quot; widget bundle and click on it;" loading="lazy"><figcaption>Find the "Charts" widget bundle and click on it;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-9-ce.webp" alt="Select the &quot;Time series chart&quot; widget;" loading="lazy"><figcaption>Select the "Time series chart" widget;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-10-ce.webp" alt="Navigate to the &quot;Entity alias&quot; tab in the &quot;Datasource&quot; section. Enter the desirable alias name in the &quot;Entity alias&quot; field and click the &quot;Create a new one!&quot; button;" loading="lazy"><figcaption>Navigate to the "Entity alias" tab in the "Datasource" section. Enter the desirable alias name in the "Entity alias" field and click the "Create a new one!" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-11-ce.webp" alt="Select the &quot;Entity from dashboard state&quot; from the &quot;Filter type&quot; field and click &quot;Add&quot;;" loading="lazy"><figcaption>Select the "Entity from dashboard state" from the "Filter type" field and click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-12-ce.webp" alt="Replace the label of the &quot;temperature&quot; key with ${entityName}. Then, click &quot;Add&quot; to add new widget on the dashboard;" loading="lazy"><figcaption>Replace the label of the "temperature" key with <b>${entityName}</b>. Then, click "Add" to add new widget on the dashboard;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-13-ce.webp" alt="Resize the &quot;Time series chart&quot; widget until you are happy with its size." loading="lazy"><figcaption>Resize the "Time series chart" widget until you are happy with its size.</figcaption></figure></div>


Now let's add an action button with the "Update current dashboard state" type for each entity of the "Entities table" widget.
We assume that you are already familiar with the "[Add action](#add-action)" step. Therefore, we will proceed directly to the action configuration step.

- Enter the editing mode of the "Time series chart" widget and open the "Add action" window;
- As an example for this manual, select "[On row click](#on-row-click)" action source;
- Input a name for the action and select an icon that will represent a button. With this icon, action will be performed;
- Select an "Update current dashboard state" action type from the "Action" drop-down menu;
- Turn on the "Open right dashboard layout (mobile view)" option;
- Click the "Add" button at the bottom of the "Add action" window;
- Now in the "Actions" window, you can see the configured action, allowing you to double-check the action source, icon, and action type. Click "Save", and then click "Apply" to save the widget settings.
- Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-14-ce.webp" alt="Enter the editing mode of the &quot;Time series chart&quot; widget and start adding new action. Select the &quot;On row click&quot; as the action source. Input a name for the action and select an icon that will represent a button. Select an &quot;Update current dashboard state&quot; action type from the &quot;Action&quot; drop-down menu. Turn on the &quot;Open right dashboard layout (mobile view)&quot; option. Then, click the &quot;Add&quot; button;" loading="lazy"><figcaption>Enter the editing mode of the "Time series chart" widget and start adding new action. Select the "On row click" as the action source. Input a name for the action and select an icon that will represent a button. Select an "Update current dashboard state" action type from the "Action" drop-down menu. Turn on the "Open right dashboard layout (mobile view)" option. Then, click the "Add" button;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-15-ce.webp" alt="Now in the &quot;Actions&quot; window, you can see the configured action. Click &quot;Save&quot;;" loading="lazy"><figcaption>Now in the "Actions" window, you can see the configured action. Click "Save";</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-16-ce.webp" alt="Click &quot;Apply&quot; to save the widget settings;" loading="lazy"><figcaption>Click "Apply" to save the widget settings;</figcaption></figure><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-17-ce.webp" alt="Save the dashboard by clicking &quot;Save&quot; in the upper right corner of the dashboard page." loading="lazy"><figcaption>Save the dashboard by clicking "Save" in the upper right corner of the dashboard page.</figcaption></figure></div>


Click the row of any entity in the "Entity Table" widget to perform an action, namely, update the details about the selected entity. This entity's data will be displayed in the "Time series chart" widget on the current dashboard.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-18-ce.webp" alt="Click the row of any entity in the &quot;Entity Table&quot; widget to perform an action, namely, update the details about the selected entity. This entity&#39;s data will be displayed in the &quot;Time series chart&quot; widget on the current dashboard." loading="lazy"><figcaption>Click the row of any entity in the "Entity Table" widget to perform an action, namely, update the details about the selected entity. This entity&#39;s data will be displayed in the "Time series chart" widget on the current dashboard.</figcaption></figure></div>


Now open this dashboard in your [SENTIENT Mobile Application](/docs/mobile/). In the "Entity table" widget click a row of any entity. You will be moved directly to the "Time series chart" widget where you can see the details of the selected entity of the main widget.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/mob-layout-19-ce.webp" alt="Open this dashboard in your SENTIENT Mobile Application. In the &quot;Entity table&quot; widget click a row of any entity. You will be moved directly to the &quot;Time series chart&quot; widget where you can see the details of the selected entity of the main widget." loading="lazy"><figcaption>Open this dashboard in your SENTIENT Mobile Application. In the "Entity table" widget click a row of any entity. You will be moved directly to the "Time series chart" widget where you can see the details of the selected entity of the main widget.</figcaption></figure></div>


### Set entity from widget

_Set entity from widget_ checkbox is responsible for adding specific entity from the widget to the state. This allows you to use the entity in the target dashboard state by creating the "[Entity from dashboard state](/docs/user-guide/ui/aliases/#entity-from-dashboard-state)" or other aliases. For example, if you have a list of devices in the table widget and would like to display specific device details when you click on the table row.

Sometimes you need to store more then one entity in the state. For example, you would like to navigate to customer list, then to devices of the customer and finally to specific device details. In such case, you may have three states: "Main", "Customer Devices" and "Device Details".
You may use two different state entity parameters to reference current customer (e.g. "currentCustomer") and current device (e.g. "currentDevice") on the "Device Details" state.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/widgets/actions/guide/entityfromwidget-ce.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>
