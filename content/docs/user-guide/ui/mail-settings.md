+++
title = "Mail server configuration"
description = "SENTIENT IoT platform mail settings"
aliases = ["/docs/samples/alarms/mail/"]

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ui/mail-settings.md"
+++
This document provides step-by-step instructions for configuring the mail server in SENTIENT.
Using email allows you to send [notifications](/docs/user-guide/notifications/), password recovery messages, scheduled reports, and other important system messages.


SENTIENT system administrator defines global mail server settings, which apply to all customers.


<div class="st-callout info">


**Note:** The tenant administrator can [configure the email rule node](/docs/user-guide/rule-engine-2-0/tutorials/send-email/) to send emails using the [rule engine](/docs/user-guide/rule-engine-2-0/re-getting-started/).


</div>


## Mail server configuration

Following steps are required to configure Mail server settings:

**Step 1.** Log in to your SENTIENT instance WEB UI as system administrator;

**Step 2.** Go to the "Mail server" tab on the "Settings" page. You will be taken directly to the mail server settings;


**Step 3.** Mail server configuration:
  - Fill in the "Mail From" field;
  - Select an SMTP provider;
  - Proceed to the connection settings: 
    - Choose the SMTP protocol;
    - Specify host and port of the SMTP server;
    - Set the timeout;
    - Optionally, enable TLS and Proxy;
  - Authentication: Enter credentials for SMTP authentication. Use either the "Basic" or "OAuth 2.0" authentication method. 

**Step 4.** You can send a test email to verify the settings;

**Step 5.** Finally, click "Save" to complete the mail server configuration.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/mail/mail-server-configuration-1-ce.webp" alt="Go to the &quot;Mail server&quot; tab of the &quot;Settings&quot; page. You will be taken directly to the mail server settings. Fill in the &quot;Mail From&quot; field, select an SMTP provider, and proceed to the connection settings: choose the SMTP protocol, specify host and port of the SMTP server, and set the timeout;" loading="lazy"><figcaption>Go to the "Mail server" tab of the "Settings" page. You will be taken directly to the mail server settings. Fill in the "Mail From" field, select an SMTP provider, and proceed to the connection settings: choose the SMTP protocol, specify host and port of the SMTP server, and set the timeout;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/mail-server-configuration-2-ce.webp" alt="Optionally, enable TLS and Proxy;" loading="lazy"><figcaption>Optionally, enable TLS and Proxy;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/mail-server-configuration-3-ce.webp" alt="Enter credentials for SMTP authentication. Use either the &quot;Basic&quot; or &quot;OAuth 2.0&quot; authentication method. Now, you can send a test email to verify the settings. Finally, click &quot;Save&quot; to complete the mail server configuration." loading="lazy"><figcaption>Enter credentials for SMTP authentication. Use either the "Basic" or "OAuth 2.0" authentication method. Now, you can send a test email to verify the settings. Finally, click "Save" to complete the mail server configuration.</figcaption></figure></div>


## Examples of mail server settings

Starting from SENTIENT 3.5.2 we have added mail settings templates for such providers: [Sendgrid](#sendgrid-configuration-example), [Gmail](#gmail-configuration-with-basic-authentication-example) and [Office 365](#office-365-configuration-with-oauth2-authentication-example). 
So users don't have to fill in connection settings like SMTP server host, port and TLS configuration.
If you want to use a different SMTP server, use the SMTP provider type "Custom".

### Sendgrid configuration example

A SendGrid configuration is fairly simple and straightforward. First, you need to create [SendGrid](https://sendgrid.com/) account. 
You can try it for free and the free plan is most likely enough for platform evaluation.

**ㅤ1. Setup SendGrid configuration**


1. Once you create your account, you will be forwarded to the welcome page. Click "Start" button;

1. Go to the "Email API" section -> "Integration Guide" page and choose a setup method - "SMTP Relay";

1. Create an API key: enter the API key name and generate it.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/mail/sendgrid-welcome.webp" alt="Once you create your account, you will be forwarded to the welcome page. Click &quot;Start&quot; button;" loading="lazy"><figcaption>Once you create your account, you will be forwarded to the welcome page. Click "Start" button;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/sendgrid-smtp-relay.webp" alt="Go to the &quot;Email API&quot; section -> &quot;Integration Guide&quot; page and choose a setup method - &quot;SMTP Relay&quot;;" loading="lazy"><figcaption>Go to the "Email API" section -> "Integration Guide" page and choose a setup method - "SMTP Relay";</figcaption></figure><figure><img src="/images/user-guide/ui/mail/sendgrid-token.webp" alt="Create an API key: enter the API key name and generate it." loading="lazy"><figcaption>Create an API key: enter the API key name and generate it.</figcaption></figure></div>


**ㅤ2. Setup SENTIENT mail server settings**

Now navigate to the "Settings" page -> "Mail Server" tab your SENTIENT instance and fill in the form:

- Fill in the "Mail From" field;
- Select SMTP provider - **SendGrid**;
- Enter username: **apikey**;
- Enter password: previously generated **password**.

Click "Save" button.


![image](/images/user-guide/ui/mail/sendgrid-settings-ce.webp)


<br>
**ㅤ3. Send test email**

Optional, you can receive test mail on your email.
In case of error in configuration, you should receive a popup with the error log.

You can also complete verification on the SendGrid website.

![image](/images/user-guide/ui/mail/sendgrid-it-works.webp)

### Gmail configuration with basic authentication example

In order to use Gmail, you will need to enable two-step verification (this step is not mandatory, but it is highly recommended.) and generate an [**app password**](https://support.google.com/accounts/answer/185833?hl=en).

**ㅤ1. Setup Google Account configuration**


1. Go to your Google Account and navigate to the "Security" page. Then select "2-Step Verification" tab;

1. At the bottom of the page, select "App passwords";

1. Click on the "Select app" and select "Other" app in the drop-down menu;

1. Enter app name and click "Generate" button;

1. Copy and save app password.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/mail/gmail-generate-an-app-password-1.webp" alt="Go to your Google Account and navigate to the &quot;Security&quot; page. Then select &quot;2-Step Verification&quot; tab;" loading="lazy"><figcaption>Go to your Google Account and navigate to the "Security" page. Then select "2-Step Verification" tab;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/gmail-generate-an-app-password-2.webp" alt="At the bottom of the page, select &quot;App passwords&quot;;" loading="lazy"><figcaption>At the bottom of the page, select "App passwords";</figcaption></figure><figure><img src="/images/user-guide/ui/mail/gmail-generate-an-app-password-3.webp" alt="Click on the &quot;Select app&quot; and select &quot;Other&quot; app in the drop-down menu;" loading="lazy"><figcaption>Click on the "Select app" and select "Other" app in the drop-down menu;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/gmail-generate-an-app-password-4.webp" alt="Enter app name and click &quot;Generate&quot; button;" loading="lazy"><figcaption>Enter app name and click "Generate" button;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/gmail-generate-an-app-password-5.webp" alt="Copy and save app password." loading="lazy"><figcaption>Copy and save app password.</figcaption></figure></div>


**ㅤ2. Setup SENTIENT mail server settings**

Once this is ready, you should be able to set up mail server using the information below.
Navigate to the "Settings" page -> "Mail Server" tab your SENTIENT instance and fill in the form:

- Fill in the "Mail From" field;
- Select SMTP provider - **Google**;
- Enter your email as **username**;
- Leave **basic** authentication type;
- Enter previously copied **app password**.

Click "Save" button.


![image](/images/user-guide/ui/mail/gmail-settings-basic-ce.webp)


<br>
**ㅤ3. Send test email**

Optional, you can receive test mail on your email.
In case of error in configuration, you should receive a popup with the error log.

### Gmail configuration with OAuth2 authentication example

Starting from SENTIENT 3.5.2 it is possible to use OAuth2 authorization for Gmail SMTP server. 
Using OAuth 2.0 protocol, user can do authentication by Gmail Web OAuth instead of inputting user and password directly in application. 
This way is more secure, but a little bit complex.

To use Gmail OAuth2 you need to create a project in Google Developers Console but first let's set up SENTIENT mail server settings.

**ㅤ1. Setup SENTIENT mail server settings**

- In your SENTIENT instance, go to the "Settings" page -> "Mail Server" tab;
- Fill in the "mail From" field;
- Select SMTP provider - "**Google**";
- In the "Authentication" block, fill in username with email address you are going to use for sending mail from;
- Toggle the authentication type to **OAuth2**;
- Copy and save the "**Redirect URI template**". It will be needed while set up Google project credentials.


![image](/images/user-guide/ui/mail/google-oauth-settings-1-ce.webp)


<br>
**ㅤ2. Now let's create a project in [Google Developers Console](https://console.developers.google.com/projectcreate)**


1. Input “Project name” and “Location”. Then click “Create”. New project is created.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/mail/gmail-with-oauth2-1-pe.webp" alt="Input “Project name” and “Location”. Then click “Create”. New project is created." loading="lazy"><figcaption>Input “Project name” and “Location”. Then click “Create”. New project is created.</figcaption></figure></div>


**ㅤ3. Then you need to create credentials**


1. Select created project and navigate to the "APIs & Services" page;

1. Click on the "Credentials" tab, then click on the "Create Credentials" button and select "OAuth client ID";

1. In a "Create OAuth client ID" window select application type - "Web application" and input the name of your OAuth2 client. Then, in the "Authorized redirect URIs" section, click the "+ Add URI" button and paste the previously copied "Redirect URI template". Click "Create";

1. Save created client ID and client secret for future steps.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/mail/gmail-with-oauth2-2-pe.webp" alt="Select created project and navigate to the &quot;APIs & Services&quot; page;" loading="lazy"><figcaption>Select created project and navigate to the "APIs & Services" page;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/gmail-with-oauth2-3-pe.webp" alt="Click on the &quot;Credentials&quot; tab, then click on the &quot;Create Credentials&quot; button and select &quot;OAuth client ID&quot;;" loading="lazy"><figcaption>Click on the "Credentials" tab, then click on the "Create Credentials" button and select "OAuth client ID";</figcaption></figure><figure><img src="/images/user-guide/ui/mail/gmail-with-oauth2-4-pe.webp" alt="In a &quot;Create OAuth client ID&quot; window select application type - &quot;Web application&quot; and input the name of your OAuth2 client. Then, in the &quot;Authorized redirect URIs&quot; section, click the &quot;+ Add URI&quot; button and paste the previously copied &quot;Redirect URI template&quot;. Click &quot;Create&quot;;" loading="lazy"><figcaption>In a "Create OAuth client ID" window select application type - "Web application" and input the name of your OAuth2 client. Then, in the "Authorized redirect URIs" section, click the "+ Add URI" button and paste the previously copied "Redirect URI template". Click "Create";</figcaption></figure><figure><img src="/images/user-guide/ui/mail/gmail-with-oauth2-5-pe.webp" alt="Save created client ID and client secret for future steps." loading="lazy"><figcaption>Save created client ID and client secret for future steps.</figcaption></figure></div>


<br>
**ㅤ4. Complete SENTIENT settings setup**

Back to the Sentient portal and paste **Client ID** and **Client secret** from the previous steps into the appropriate fields. Click "Save".


![image](/images/user-guide/ui/mail/google-oauth-settings-2-ce.webp)


<br>
**ㅤ5. Generate access token**

Finally, we can get access token. For this click on the **Generate access token** and your browser will redirect you to provider login page. 
Please follow the steps in your browser and after acceptance we will automatically save Refresh Token and Access Token and redirect you back to SENTIENT portal. 
If access token was successfully generated you will see status "generated".


![image](/images/user-guide/ui/mail/google-oauth-settings-3-ce.webp)


<br>
**ㅤ6. Send test email**

To check if everything works click "Send test email" button. Keep in mind that each time you change provider info system will drop refresh and access token and you will need to generate it again.

### Office 365 configuration with OAuth2 authentication example

Starting from SENTIENT 3.6 it is possible to use OAuth2 authorization for Office 365 SMTP server. 


<div class="st-callout info">


**Please note:**
<br>
Take a note that OAuth 2.0 is supported for Microsoft 365 accounts, but NOT for personal Outlook accounts (e.g. @outlook.com or @hotmail.com accounts). 


</div>


First, go to the "Azure directory" to save user principal name of user you want to use for mail sending (if not exists, please create or invite from external services):

 - Sign in to the [Azure portal](https://portal.azure.com/) and select Microsoft Entra ID;
 - Select microsoft user and copy user principal name.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/mail/azure-create-application-1.webp" alt="Sign in to the Azure portal and select Microsoft Entra ID;" loading="lazy"><figcaption>Sign in to the Azure portal and select Microsoft Entra ID;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/microsoft-azure-copy-user-principal-name-1-pe.webp" alt="Select microsoft user and copy user principal name." loading="lazy"><figcaption>Select microsoft user and copy user principal name.</figcaption></figure></div>


To use Office 365 OAuth2 you need to register an application in the Azure portal but first let’s set up SENTIENT mail server settings.

**ㅤ1. Setup SENTIENT mail server settings**:

 - In your SENTIENT instance, go to the "Settings" page -> "Mail Server" tab;
 - Enter previously copied Microsoft user principal name (e.g. app_user@onmicrosoft.com);
 - Select SMTP provider - "**Office 365**";
 - In the "Authentication" block, fill in username with microsoft user principal name (the same as you used for mail from);
 - Toggle the authentication type to **OAuth2**;
 - Copy and save the "**Redirect URI template**". It will be needed while set up the Azure portal credentials.


![image](/images/user-guide/ui/mail/microsoft-azure-oauth-settings-1-ce.webp)


<br>
**ㅤ2. Now let's register an application in the Azure portal**:


1. Under the "Manage" section select the "App registrations" page, and click the "New registration" button;

1. Enter a name for your application and paste the previously copied "Redirect URI template". Click the "Register" button;

1. After application is created you can find "Client ID" and "Directory (tenant) ID" on "Overview" page. Save them for future steps.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/mail/azure-create-application-2.webp" alt="Under the &quot;Manage&quot; section select the &quot;App registrations&quot; page, and click the &quot;New registration&quot; button;" loading="lazy"><figcaption>Under the "Manage" section select the "App registrations" page, and click the "New registration" button;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/azure-create-application-3.webp" alt="Enter a name for your application and paste the previously copied &quot;Redirect URI template&quot;. Click the &quot;Register&quot; button;" loading="lazy"><figcaption>Enter a name for your application and paste the previously copied "Redirect URI template". Click the "Register" button;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/microsoft-azure-with-oauth2-4-pe.webp" alt="After application is created you can find &quot;Client ID&quot; and &quot;Directory (tenant) ID&quot; on &quot;Overview&quot; page. Save them for future steps." loading="lazy"><figcaption>After application is created you can find "Client ID" and "Directory (tenant) ID" on "Overview" page. Save them for future steps.</figcaption></figure></div>


<br>
**ㅤ3. Then you need to create a "Client secret"**:


1. Select "Certificates & secrets" > "Client secrets" > click "New client secret" button;

1. Add a description for your client secret. Select an expiration for the secret or specify a custom lifetime. Click "Add";

1. Save client secret value for future step.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/mail/microsoft-azure-with-oauth2-5-pe.webp" alt="Select &quot;Certificates & secrets&quot; > &quot;Client secrets&quot; > click &quot;New client secret&quot; button;" loading="lazy"><figcaption>Select "Certificates & secrets" > "Client secrets" > click "New client secret" button;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/microsoft-azure-with-oauth2-6-pe.webp" alt="Add a description for your client secret. Select an expiration for the secret or specify a custom lifetime. Click &quot;Add&quot;;" loading="lazy"><figcaption>Add a description for your client secret. Select an expiration for the secret or specify a custom lifetime. Click "Add";</figcaption></figure><figure><img src="/images/user-guide/ui/mail/microsoft-azure-with-oauth2-7-pe.webp" alt="Save client secret value for future step." loading="lazy"><figcaption>Save client secret value for future step.</figcaption></figure></div>


<br>
**ㅤ4. To finish the authentication set up you need add API permissions for SMTP**:


1. In the Azure portal go to “API permissions” page and click “Add a permission” button;

1. Select an API - "Microsoft Graph";

1. Select type of permissions - "Delegated permissions";

1. Search and check the box “SMTP.Send” permission. Then click “Add permissions” button;

1. Permissions is updated.


<div class="st-gallery"><figure><img src="/images/user-guide/ui/mail/microsoft-azure-with-oauth2-api-permissions-1-pe.webp" alt="In the Azure portal go to “API permissions” page and click “Add a permission” button;" loading="lazy"><figcaption>In the Azure portal go to “API permissions” page and click “Add a permission” button;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/microsoft-azure-with-oauth2-api-permissions-2-pe.webp" alt="Select an API - &quot;Microsoft Graph&quot;;" loading="lazy"><figcaption>Select an API - "Microsoft Graph";</figcaption></figure><figure><img src="/images/user-guide/ui/mail/microsoft-azure-with-oauth2-api-permissions-3-pe.webp" alt="Select type of permissions - &quot;Delegated permissions&quot;;" loading="lazy"><figcaption>Select type of permissions - "Delegated permissions";</figcaption></figure><figure><img src="/images/user-guide/ui/mail/microsoft-azure-with-oauth2-api-permissions-4-pe.webp" alt="Search and check the box “SMTP.Send” permission. Then click “Add permissions” button;" loading="lazy"><figcaption>Search and check the box “SMTP.Send” permission. Then click “Add permissions” button;</figcaption></figure><figure><img src="/images/user-guide/ui/mail/microsoft-azure-with-oauth2-api-permissions-5-pe.webp" alt="Permissions is updated." loading="lazy"><figcaption>Permissions is updated.</figcaption></figure></div>


<br>
**ㅤ5. Complete SENTIENT settings setup**:

Back to the SENTIENT portal and paste **Client ID**, **Client secret** and **Directory (tenant) ID** from the previous steps into the appropriate fields. Click "Save".


![image](/images/user-guide/ui/mail/microsoft-azure-oauth-settings-2-ce.webp)


<br>
**ㅤ6. Generate access token**:

Finally, we can get access token. For this click on the "Generate access token" button and your browser will redirect you to provider login page. Please follow the steps
in your browser and after acceptance we will automatically save Refresh Token and Access Token and redirect you back to SENTIENT portal. 
If access token was successfully generated you will see status "generated".


![image](/images/user-guide/ui/mail/microsoft-azure-oauth-settings-3-ce.webp)


<br>
**ㅤ7. Send test email**:

To check if everything works click "Send test email" button. Keep in mind that each time you change provider info system will drop refresh and access token and you will need to generate it again.

<br>
**Office 365 troubleshooting**

If you see authentication errors while sending email (e.x. 5.7.3):

1. Make sure SMTP settings are enabled for user. For this go to [here](https://portal.office.com/adminportal/home#/users). Then select user →  Mail → Manage email apps → Authenticate SMTP (if enabled - disable and enable again);
2. In Azure portal make sure Security defaults are disabled.

## Next steps
