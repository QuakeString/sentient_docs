+++
title = "IoT Gateway Remote Configuration"
description = "IoT Gateway Remote Configuration"

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/guides/how-to-enable-remote-configuration.md"
+++
Remote Configuration is a powerful feature of SENTIENT IoT Gateway that allows you to manage and configure your 
gateway directly from the SENTIENT web interface. This feature is especially useful for managing multiple 
gateways or when physical access to the gateway is limited.

For purpose of this guide, we will use following things:
1. Locally installed instance of SENTIENT platform (How to install you can [read here](/docs/user-guide/install/installation-options/)).
2. SENTIENT IoT Gateway (How to install you can [read here](/docs/iot-gateway/installation/)).


<div class="st-callout warn">


<div>
  <p>
    <b style="color:red">WARNING:</b>
    <span style="color:black">If you've previously configured the gateway, create a backup, as the new remote configuration will overwrite existing settings files.  
    <br>For those who used a gateway version earlier than 3.4, the gateway will automatically generate a new configuration file in JSON format.</span>
  </p>
</div>


</div>


## Gateway List

In order to remotely manage gateways, you need to go to the "**Entities**" > "**Gateways**" tab on the side menu of 
the SENTIENT.

Gateway list page displays all your gateways and all the necessary details about them, namely:
- Date and time of creation.
- Name of the gateway.
- Status (Active/Inactive).
- Number of enabled connectors.
- Gateway version.

And also navigation elements:
- **Launch command** - when clicked, a modal window opens with a command to launch the gateway.
- **Gateway configuration** - when clicked, a modal window with general gateway settings opens.
- **Connectors** - when clicked, a page for managing and configuring connectors opens.
- **Delete gateway** - when clicked, a gateway deletion confirmation modal window opens.

On this page, you can create a new gateway, as well as sort them according to the parameters described above.

![](/images/gateway/dashboard/gateway-dashboard-list.webp)

### Gateway Info Page

If you select a gateway and click on it, you will be transferred to the page of the selected gateway.

![](/images/gateway/dashboard/gateway-dashboard.webp)

The dashboard consists of 4 main widgets:
- **General gateway information**, which consists of the following cards:
   - Status (Active/Inactive).
   - Name of the gateway.
   - Type of the gateway.
   - Devices (Active/Inactive).
   - Connectors (Enabled/Disabled) with link to Connectors page.
   - Errors count with link to Logs page.

![](/images/gateway/dashboard/gateway-dashboard-cards.webp)

- **Devices** is a table that contains basic information about connected devices through the gateway:
   - Device Name.
   - Device Type.
   - Status (Active/Inactive).
   - Connector Name.
   - Connector Type.
   - Device info button that opens a modal window with detailed information about the device.
   - As well as elements of filtering and searching for the necessary devices.

![](/images/gateway/dashboard/gateway-dashboard-devices.webp)

- **Alarms** is a standard alarm widget where you will receive all alarms related to selected gateway.

![](/images/gateway/dashboard/gateway-dashboard-alarms.webp)

- **Navigation Panel** is a navigation panel on which all other pages for configuring, managing and monitoring the gateway are located, namely:
   - Launch command - a modal window with an auto-generated command for launching the gateway.
  
   ![](/images/gateway/dashboard/gateway-dashboard-launch-command.webp)

   - [General configuration](#general-configuration) - page with general gateway settings.
  
   [![](/images/gateway/dashboard/gateway-dashboard-gen-conf-button.webp)](#general-configuration)

   - [Connectors configuration](#connector-configuration) - page with management and configuration of connectors.
  
   [![](/images/gateway/dashboard/gateway-dashboard-connectors-conf-button.webp)](#connector-configuration)

   - [Logs](#logs) - a page with various types of logs (it should be noted that the button is active only when **Remote Logging** is enabled on the gateway).
  
   [![](/images/gateway/dashboard/gateway-dashboard-logs-button.webp)](#logs)

   - [Statistics](#statistics) - a page with general and custom statistics of the gateway.

   [![](/images/gateway/dashboard/gateway-dashboard-statistics-button.webp)](#statistics)

   - [Remote Shell](#remote-shell) - page with Remote Shell (it should be noted that the button is active only when **Remote Shell** is enabled on the gateway).

   [![](/images/gateway/dashboard/gateway-dashboard-remote-shell-button.webp)](#remote-shell)

   - [RPC](#rpc) - Gateway RPC sending page.

   [![](/images/gateway/dashboard/gateway-dashboard-rpc-button.webp)](#rpc)

### General Configuration

If you click on the **General Configuration** button on the gateway page in the Navigation Panel, you will be 
transferred to the dashboard general settings of the gateway.

You can switch configuration modes between **Basic** and **Advanced**. Basic mode provides a user-friendly interface 
for configuring the gateway, while Advanced mode allows you to edit the configuration file in JSON format directly.

#### Basic Configuration Mode

The page consists of the following tabs:


<div class="st-callout info">


For each field there are hints that appear when hovering over the **"i"** icon.


</div>


<div class="st-tabs">

<div class="st-tab" data-label="General">

General - this tab contains the main settings, namely:
- Remote Configuration - enables remote configuration and management of the gateway.
- Remote Shell - enables remote control of the operating system with the gateway from the Remote Shell widget.
- Platform host - hostname or IP address of platform server.
- Platform port - port of MQTT service on platform server.
- Security type (you can read more about them [here](/docs/iot-gateway/configuration/#subsection-security)) - currently 3 types of security are supported for remote configuration:
  - Access Token.
  - TLS + Access Token.
  - Username and Password.
  - TLS + Private Key (**unsupported yet**).
- Report strategy (you can read more [here](/docs/iot-gateway/features-overview/report-strategy/)) - strategy for sending gateway status to SENTIENT:
  - On report period - sends gateway status after the report period.
  - On value change - sends gateway status when the value changes.
  - On value change or report period - sends gateway status when the value changes or report period.
  - On received - sends gateway status after receiving data from the device (default strategy).

![](/images/gateway/dashboard/gateway-dashboard-general-conf.webp)


</div>

<div class="st-tab" data-label="Logs">

Logs - a tab for setting local and remote logs, which consists of 3 main sections:
- General log settings - the usual settings for the Python [logging](https://docs.python.org/3.8/library/logging.config.html) module are used here:
  - Date format - date format of log message.
  - Log format - log message format.
- Remote logging - to configure remote logs:
  - Remote logs - enables remote logging and logs reading from the gateway.
  - Log level.
- Local logging - for configuring local loggers (Service, Connector, Converter, TB Connection, Storage, Extension):
  - Log level - logging level for each local logger: INFO, DEBUG, WARNING, ERROR, CRITICAL, TRACE, NONE.
  - File path - path to the log folder.
  - Log saving period.
  - Backup count - if **Backup count** is > 0, when a rollover is done, no more than **Backup count** files are kept - the oldest ones are deleted.

![](/images/gateway/dashboard/gateway-dashboard-logs-conf.webp)


</div>

<div class="st-tab" data-label="Storage">

Storage - provides configuration for saving incoming data before it is sent to the platform:
- [Memory storage](/docs/iot-gateway/configuration/?storageConfig=memory#storage-configuration) - saved data to the RAM memory.
- [File storage](/docs/iot-gateway/configuration/?storageConfig=file#storage-configuration) - saving received data to the hard drive.
- [SQLITE](/docs/iot-gateway/configuration/?storageConfig=sqlite#storage-configuration) - saved data to the .db file.

![](/images/gateway/dashboard/gateway-dashboard-storage-conf.webp)


</div>

<div class="st-tab" data-label="GRPC">

GRPC - provides GRPC configuration:
- Server port - network port on which the GRPC server will listen for incoming connections.
- Keep alive permit without calls - allow server to keep the GRPC connection alive even when there are no active RPC calls.
- Keep alive - duration (in milliseconds) between two successive keepalive ping messages when there is no active RPC call.
- Max pings without data - maximum number of keepalive ping messages that the server can send without receiving any data before it considers the connection dead.
- Keep alive timeout - maximum time (in milliseconds) the server should wait for a keepalive ping response before considering the connection dead.
- Min time between pings - minimum amount of time (in milliseconds) the server should wait between sending keepalive ping messages.
- Min ping interval without data - minimum amount of time (in milliseconds) the server should wait between sending keepalive ping messages when there is no data being sent or received.

![](/images/gateway/dashboard/gateway-dashboard-grpc-conf.webp)


</div>

<div class="st-tab" data-label="Statistics">

Statistics - in this tab you can configure general statistics, as well as custom statistics:
- General statistics - enable/disable gateway statistics (machine, storage, connectors).
- Custom statistics - enable/disable collecting statistics using custom commands.
- Statistic send period (in seconds) - period of time for sending statistics.
- Custom send period (in seconds) - period of time for sending custom statistics.
- Commands - commands for collecting additional statistics (to add a new command, press the **"Add command"** button):
  - Timeseries name - gateway telemetry key name.
  - Timeout (in seconds) - timeout for command execution.
  - Command - the result of the command will be used as the value of the client attribute (for example **"/bin/sh -c ipconfig getifaddr en0"**).
  - Advanced settings:
    - Install command - command for installing required packages (for example **"apt-get install -y curl"**).

![](/images/gateway/dashboard/gateway-dashboard-statistics-conf.webp)


</div>

<div class="st-tab" data-label="Other">

Other - in this tab, you can configure additional gateway parameters:
- Checking device activity - enables monitoring the activity of each connected device:
  - Inactivity timeout (in seconds) - device inactivity time after which the gateway will disconnect the device.
  - Inactivity check period (in seconds) - periodicity of device activity check.
- Advanced - additional gateway settings:
  - Min pack send delay (in milliseconds) - delay between sending packets (Decreasing this setting results in increased CPU usage).
  - QoS - quality of Service in MQTT messaging (0 - at most once, 1 - at least once).
  - Check connectors' configuration (in seconds) - the period of time when the configuration of the connectors will be checked for a change.
  - Max payload size in bytes-defines the largest message the gateway can process at once, ensuring stable performance and preventing oversized data from causing errors.
  - Min packet size to send-defines the smallest message size the gateway will transmit, preventing the sending of packets that are too small or incomplete.

![](/images/gateway/dashboard/gateway-dashboard-other-conf.webp)


</div>

</div>


#### Advanced Configuration Mode

Advanced mode allows you to edit the configuration file in JSON format directly and useful for configuring complex 
settings that are not available in Basic mode.

![](/images/gateway/dashboard/gateway-dashboard-general-configuration-advanced-mode.webp)

### Connectors Configuration

If you click on the **Connectors configuration** button on the gateway page in the **Navigation Panel**, you will be 
transferred to the **Connectors configuration page**.

![](/images/gateway/dashboard/gateway-dashboard-connectors.webp)

The page consists of two main sections:
- Connectors list - basic information and control elements of all created connectors are displayed here:
   - Enabled - enable or disable the connector.
   - Name of connector.
   - Type of connector.
   - Configuration status - displays whether the remote configuration is synchronized with the local configuration.
   - Status of the connector - if it is "green" - there are no errors, and the connector is working correctly. If it is "red" - the connector is not working correctly.
   - Actions:
     - RPC - dashboard for sending RPC through gateway to connector.
     - Logs - dashboard with connector logs.
     - Delete connector.
- Connector configuration - fields for configuring the connector.

Also, you can create a new connector by clicking on the **+** button in the top right corner of the page.

### Logs


<div class="st-callout info">


It should be noted that the **Logs page** is active only when **Remote Logging** is enabled on the gateway.


</div>


If you click on the **Logs** button on the gateway page in the **Navigation Panel**, you will be transferred
to the Logs page.

![](/images/gateway/dashboard/gateway-dashboard-logs.webp)

The dashboard displays the main gateway log information in real time (General, Service, Connection, Storage, Extension):
- Created time.
- Level.
- Message.

### Statistics

If you click on the **Statistics** button on the gateway page in the **Navigation Panel**, you will be transferred
to the Statistics page. 

In the right sidebar you can switch between **Storage**, **Machine** and **Custom** statistics.
Also, you can check gateway status in the real time in the bottom right corner of the page.

#### Storage Statistics

Storage statistics display information about the storage used by the gateway. The page consists of the following widgets:
- Storage message count - displays the total number of messages stored in the gateway storage.
- Message from platform - displays the total number of messages received from the platform.
- Pushed datapoints char - displays the total number of telemetry and attributes data points pushed to the platform.
- Messages char - displays the total number of messages processed by the gateway:
    - Messages pulled from storage - total number of messages pulled from storage.
    - Messages pushed to platform - total number of messages pushed to the platform.
    - Messages sent to platform - total number of messages sent to the platform.

![](/images/gateway/dashboard/gateway-dashboard-storage-statistics.webp)

#### Machine Statistics

Machine statistics display information about the gateway machine performance. The page consists of the following widgets:
- CPU usage - displays the current CPU usage percentage of the gateway machine.
- RAM usage - displays the current RAM usage percentage of the gateway machine.
- Disk usage - displays the current Disk usage percentage of the gateway machine.

![](/images/gateway/dashboard/gateway-dashboard-machine-statistics.webp)

#### Custom Statistics

Custom statistics display user-defined statistics of the gateway. You can add custom statistics in the 
**Statistics** tab on **General configuration** page or by clicking on **Create new** button in 
the "**Time series name**" field. Depends on the added custom statistics, the page will consist of different widgets:
char widgets for numerical statistics and table widgets for string statistics.

![](/images/gateway/dashboard/gateway-dashboard-custom-statistics.webp)

### Remote Shell


<div class="st-callout info">


It should be noted that the **Remote Shell dashboard** is active only when **Remote Shell** is enabled on the gateway.


</div>


If you click on the **Remote Shell** button on the gateway page in the **Navigation Panel**, you will be transferred
to the Remote Shell page.

![](/images/gateway/dashboard/gateway-dashboard-shell.webp)

The dashboard allows control of the operating system with the gateway from the Remote Shell widget.

### RPC

If you click on the **RPC** button on the gateway page in the **Navigation Panel**, you will be transferred
to the Gateway RPC sending page. 

![](/images/gateway/dashboard/gateway-dashboard-rpc.webp)

The page consists of 3 widgets:
- Service RPC - for sending RPC and viewing the result of command execution:
   - Command - [service gateway RPC](/docs/iot-gateway/guides/how-to-use-gateway-rpc-methods/) (Ping, Stats, Devices, Update, Version, Restart, Reboot).
   - Timeout - command execution time.
   - Response - the result of executing the sent command.
- RPS Logs - displays gateway logs when processing the sent RPC.
- RPC debug terminal - widget for debugging gateway RPCs.

## Next steps

Explore guides related to main SENTIENT features:

 - [Data Visualization](/docs/user-guide/dashboards/) - how to visualize collected data.
 - [Device attributes](/docs/user-guide/attributes/) - how to use device attributes.
 - [Telemetry data collection](/docs/user-guide/telemetry/) - how to collect telemetry data.
 - [Using RPC capabilities](/docs/user-guide/rpc/) - how to send commands to/from devices.
 - [Rule Engine](/docs/user-guide/rule-engine-2-0/overview/) - how to use rule engine to analyze data from devices.
