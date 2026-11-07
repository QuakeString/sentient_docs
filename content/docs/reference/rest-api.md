+++
title = "REST API"
description = "Supported REST API Reference for server-side integration of your IoT projects"

[extra]
status = "imported"
checked = ""
source = "docs/reference/rest-api.md"
+++
SENTIENT provides a powerful REST API that allows you to manage all platform entities, perform integrations, automate device provisioning, and build custom applications. 
To simplify API exploration and testing, SENTIENT includes built-in interactive documentation powered by [Swagger UI](https://swagger.io/).

## Swagger UI

Swagger UI is an interactive tool that lets you:
- browse all available REST API endpoints
- inspect request and response schemas
- test API calls directly in the browser
- authenticate and run API requests as a specific user

This makes it ideal for development, debugging, and API exploration.

## Where to find Swagger UI?


Every SENTIENT instance hosts its own Swagger UI page at:

```
http://$SENTIENT_HOST:PORT/swagger-ui.html
```


&#42; Replace **$SENTIENT_HOST:PORT** with the address of your SENTIENT deployment.


 

## Authentication in Swagger UI

<b><font size="3">Automatic authentication</font></b>

If you are already logged in through the main SENTIENT UI, Swagger UI automatically uses your authenticated session.

<b><font size="3">Manual authentication</font></b>

You can authenticate or authorize as a different user using the **Authorize** button in the top-right corner of Swagger UI.

Steps:
- Open **Swagger UI**
- Click **Authorize**
- Enter your **username** and **password**, `or` paste your **API key** In the **API key form (apiKey)** section.
- Click **Authorize**

**Note:** Only one authentication method should be used at a time.   
If both are authorized, **JWT takes priority**.


<div class="st-gallery"><figure><img src="/images/user-guide/security/api-keys/authentication-in-swagger-ui-1.webp" alt="You can manually authenticate or authorize as another user by clicking the Authorize button on the right side of the Swagger page." loading="lazy"><figcaption>You can manually authenticate or authorize as another user by clicking the <b>Authorize</b> button on the right side of the Swagger page.</figcaption></figure><figure><img src="/images/user-guide/security/api-keys/authentication-in-swagger-ui-2.webp" alt="Enter your username and password, or paste your API key In the API key form (apiKey) section.Then, click Authorize." loading="lazy"><figcaption>Enter your username and password, or paste your API key In the API key form (apiKey) section.<br>Then, click <b>Authorize</b>.</figcaption></figure></div>


### API key authentication


<table style="width:auto">
   <thead>
     <tr>
	 <td style="text-align: center"><strong><em>Available since TB Version 4.3</em></strong></td>
     </tr>
   </thead>
</table> 


API keys provide a simpler, automation-friendly alternative to JWT authentication.
- **No login required:** You don&#39;t need to exchange passwords or manage token refresh loops
- **Long-lived:** They stay active indefinitely or until the expiration date you choose
- **Revocable:** You can easily disable a specific key


<div class="st-callout info">


**Note:** Use the **API keys** tab in the SENTIENT UI to create and manage them.
For more details, see the [full documentation](/docs/user-guide/security/api-keys/).


</div>


Using API keys

To authenticate via the API key, include it in the X-Authorization header with the "**ApiKey**" prefix:

```
X-Authorization: ApiKey $YOUR_API_KEY_VALUE
```


&#42; Replace **$YOUR_API_KEY_VALUE** with the API key.

**Important:** API keys should only be used over HTTPS.

Example (curl)

```
curl -X GET --header 'Accept: application/json' \
            --header 'X-Authorization: ApiKey $YOUR_API_KEY_VALUE' \
            'http://$SENTIENT_URL/api/auth/user'
```

<hr>

### JWT authentication (deprecated)

SENTIENT uses [JWT](https://jwt.io/) tokens to authenticate API requests.

When you log in, your username and password are exchanged for two tokens:
- **Access Token (JWT)** - A short-lived token used for API requests.
- **Refresh Token** - When the Access Token expires, the Refresh Token allows obtaining a new Access Token without re-authentication.

**Default expiration times**
- **Access Token** is valid for **2.5 hours**.
- **Refresh Token** is valid for **1 week**.


Expiration times are [configurable](/docs/user-guide/install/config/) in system settings:
- <span class="code-light">JWT_TOKEN_EXPIRATION_TIME</span>
- <span class="code-light">JWT_REFRESH_TOKEN_EXPIRATION_TIME</span>
  

<hr>

<b><font size="4">How to obtain a JWT token?</font></b>


To obtain a JWT token for the user "tenant@sentient.org" with password "tenant" on "$SENTIENT_URL" (actual SENTIENT server address), execute the following command:

```
curl -X POST --header 'Content-Type: application/json' \
             --header 'Accept: application/json' \
             -d '{"username":"tenant@sentient.org", "password":"tenant"}' \
             'http://$SENTIENT_URL/api/auth/login'
```


Response:

```json
{"token":"$YOUR_JWT_TOKEN", "refreshToken":"$YOUR_JWT_REFRESH_TOKEN"}
```


Once authenticated, use the obtained JWT token in the X-Authorization header for all API requests:

```
X-Authorization: Bearer $YOUR_JWT_TOKEN
```


## Additional tools

For easier integration with the SENTIENT API, you can use SENTIENT team client libraries:

- [Java REST API Client](/docs/reference/rest-client/) – client library written in Java to simplify consumption of the REST API.
- [Python REST API Client](/docs/reference/python-rest-client/) – client library written in Python to simplify the consumption of the REST API.

These clients allow you to create devices, assets, users, and other entities, as well as manage their relationships within SENTIENT.
