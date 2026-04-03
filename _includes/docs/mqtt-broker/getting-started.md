{% include templates/mqtt-broker/pe-st-rmqtt-explore-banner.md %}

* TOC
{:toc}

## Introduction

The goal of this tutorial is to showcase the fundamental usage of <a target="_blank" href="/products/mqtt-broker/">ST-RMQTT</a>. 
Through this tutorial, you will gain knowledge and proficiency in the following areas:

* Establishing connections between MQTT clients and the broker.
* Publishing MQTT messages.
* Subscribing to topics to receive published messages.
* Configuring authentication and authorization mechanisms for MQTT clients.

For more comprehensive information regarding the architecture of ST-RMQTT, navigate to the following [document](/docs/{{docsPrefix}}mqtt-broker/architecture/).
This resource provides detailed insights into the underlying structure and design principles of the broker.

## Try Live Demo

The fastest way to get started with ST-RMQTT is to use our free public MQTT broker at [demo.st-rmqtt.io](https://demo.st-rmqtt.io){:target="_blank"}.
This sandbox environment allows you to explore ST-RMQTT features without any installation.

**MQTT connection details:**

| Parameter | Value           |
|-----------|-----------------|
| Host      | demo.st-rmqtt.io    |
| TCP Port  | 1883            |
| TLS Port  | 8883            |
| Username  | demo            |
| Password  | *(leave empty)* |

You can start publishing and subscribing to topics immediately using these credentials.
To access the ST-RMQTT UI and explore sessions, subscriptions, and other features, [sign up](https://demo.st-rmqtt.io/signup){:target="_blank"} for a free account.

{% capture demo_note %}
The demo instance provides read-only access to the UI. You can observe all sessions, subscriptions, and broker statistics, but cannot modify configurations.
If you prefer to run ST-RMQTT locally with full administrative access, proceed to the [Install ST-RMQTT locally](#install-st-rmqtt-{{st-rmqttSuffixLc}}-locally) section.
{% endcapture %}
{% include templates/info-banner.md content=demo_note %}

## Install ST-RMQTT {{st-rmqttSuffix}} locally

For full control over your ST-RMQTT {{st-rmqttSuffix}} instance, you can install it locally.
For detailed instructions on different platforms, see the [Installation options](/docs/{{docsPrefix}}mqtt-broker/install/installation-options) documentation.

Follow the instructions below for a quick local installation.

{% capture contenttogglespec %}
Linux & Mac OS%,%linuxmacos%,%templates/mqtt-broker/install/linux-macos/linux-macos.md%br%
Windows%,%windows%,%templates/mqtt-broker/install/windows/windows.md{% endcapture %}

{% include content-toggle.html content-toggle-id="st-rmqttGettingStartedInstallation" toggle-spec=contenttogglespec %}

{% if docsPrefix == "pe/" %}

Before proceeding, make sure you’ve selected your subscription plan or chosen to purchase a perpetual license.
If you haven’t done this yet, please visit the [Pricing page](/pricing/?section=st-rmqtt-options){: target="_blank"} to compare available options
and obtain your license key.

{% capture replace_st-rmqtt_license_secret %}
Update your `docker-compose.yml` file with the license secret you obtained earlier.
Open the file, find the **ST-RMQTT_LICENSE_SECRET** environment variable,
and replace **YOUR_LICENSE_KEY_HERE** with your actual license secret.
After updating the file, restart ST-RMQTT by running the following command.
{% endcapture %}
{% include templates/warn-banner.md content=replace_st-rmqtt_license_secret %}
 
```shell
./st-rmqtt-install-and-run.sh
```
{: .copy-code}

{% endif %}

Once the installation process is complete for local deployment, you can access ST-RMQTT UI by visiting the following URL: **http://localhost:8083**. 
Wait patiently until the services are up and running. To log in, utilize the following default credentials.

**Username:**
```text
sysadmin@sentient.org
```
{: .copy-code}

**Password:**
```text
sysadmin
```
{: .copy-code}

## Configure client authentication & authorization

{% capture auth_note %}
If you are using the [demo instance](https://demo.st-rmqtt.io){:target="_blank"}, skip this section. Demo credentials are pre-configured and ready to use.
{% endcapture %}
{% include templates/info-banner.md content=auth_note %}

To secure the connection to the broker, [enable Basic authentication](/docs/{{docsPrefix}}mqtt-broker/security/authentication/basic/).

Once Basic authentication is enabled, create MQTT Client Credentials of type `Basic` to authenticate connecting clients:

* Navigate to _Authentication_ - _Credentials_ tab, click "+" in the top right corner of the table.
* Input credentials name. For example, "Getting Started Credentials".
* Input "username" and "password" with chosen values. For example, use `username` and `password` values respectively.
* Authorization rules are set to allow publishing/subscribing to any topic by default.
* Click "Add" to save credentials.

{% include images-gallery.html imageCollection="broker-mqtt-creds-creation" %}

For additional authentication methods, refer to the [security guide](/docs/{{docsPrefix}}mqtt-broker/security/overview/).

## Publishing and Subscribing to Topics

Now, let's publish messages and subscribe to topics to observe the flow of messages.
This tutorial uses [Mosquitto](https://mosquitto.org/) clients. See the documentation for [mosquitto_pub](https://mosquitto.org/man/mosquitto_pub-1.html) and [mosquitto_sub](https://mosquitto.org/man/mosquitto_sub-1.html) for more details.

{% capture pubsubtogglespec %}
Demo Instance<small>demo.st-rmqtt.io</small>%,%demo%,%templates/mqtt-broker/getting-started/pub-sub-demo.md%br%
Local Deployment<small>localhost</small>%,%local%,%templates/mqtt-broker/getting-started/pub-sub-local.md{% endcapture %}

{% include content-toggle.html content-toggle-id="pubSubCommand" toggle-spec=pubsubtogglespec %}

##### Result

You should see the published message received by the subscribed client:

![image](/images/mqtt-broker/getting-started/broker-pub-sub.png)

## Next Steps

{% assign currentGuide = "GettingStartedGuide" %}{% include templates/mqtt-broker-guides-banner.md %}
