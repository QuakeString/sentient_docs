+++
title = "SMS Provider Settings"
description = "SENTIENT IoT platform SMS provider settings"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/sms-provider-settings.md"
+++
SENTIENT System Administrator is able to configure SMS provider that will be used the SMS gateway to send text messages to your customers or users.
For example, you can set up sending an SMS alert to the user when the sensor detects an abnormal condition.


Tenant administrator is able to setup [**sms rule node**](/docs/user-guide/rule-engine-2-0/nodes/external/send-sms/) to distribute alarms produced by [**rule engine**](/docs/user-guide/rule-engine-2-0/re-getting-started/).  

To configure SMS provider settings in Sentient, follow these steps:


1. Login to SENTIENT UI. Navigate to the "Settings" page. Now, go to the "Notificatons" tab. In this window, choose one of the available providers: AWS SNS Twilio or SMPP;

1. If you have chosen AWS SNS, populate AWS Access Key ID and Secret access key. Click "Save" button;

1. If you have chosen Twilio, populate the Twilio account SID and Token. Specify phone number that will be used as a "sender". Click "Save" button;

1. If you have chosen SMPP, Populate System ID and Password. Specify SMPP version, SMPP host and port. Click "Save" button.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/sms/sms-provider-settings-step-2-ce.webp" alt="Login to SENTIENT UI. Navigate to the &quot;Settings&quot; page. Now, go to the &quot;Notificatons&quot; tab. In this window, choose one of the available providers: AWS SNS Twilio or SMPP;" loading="lazy"><figcaption>Login to SENTIENT UI. Navigate to the "Settings" page. Now, go to the "Notificatons" tab. In this window, choose one of the available providers: AWS SNS Twilio or SMPP;</figcaption></figure><figure><img src="/images/user-guide/ui/sms/sms-provider-settings-step-3-ce.webp" alt="If you have chosen AWS SNS, populate AWS Access Key ID and Secret access key. Click &quot;Save&quot; button;" loading="lazy"><figcaption>If you have chosen AWS SNS, populate AWS Access Key ID and Secret access key. Click "Save" button;</figcaption></figure><figure><img src="/images/user-guide/ui/sms/sms-provider-settings-step-4-ce.webp" alt="If you have chosen Twilio, populate the Twilio account SID and Token. Specify phone number that will be used as a &quot;sender&quot;. Click &quot;Save&quot; button;" loading="lazy"><figcaption>If you have chosen Twilio, populate the Twilio account SID and Token. Specify phone number that will be used as a "sender". Click "Save" button;</figcaption></figure><figure><img src="/images/user-guide/ui/sms/sms-provider-settings-step-5-ce.webp" alt="If you have chosen SMPP, Populate System ID and Password. Specify SMPP version, SMPP host and port. Click &quot;Save&quot; button." loading="lazy"><figcaption>If you have chosen SMPP, Populate System ID and Password. Specify SMPP version, SMPP host and port. Click "Save" button.</figcaption></figure></div>


<br>
Please use [AWS SNS](https://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-phone.html), [Twilio](https://www.twilio.com/docs/sms) or [SMPP](https://smpp.org/) documentation to learn more how to use the corresponding system.
