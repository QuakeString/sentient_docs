+++
title = "X.509 Certificate Based Authentication"
description = "SENTIENT  X.509 Certificate based authentication for IoT devices and projects."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/certificates.md"
+++
X.509 Certificates are used to setup [mutual](https://en.wikipedia.org/wiki/Mutual_authentication) (two-way) authentication for MQTT over TLS.
It is similar to [access token](/docs/user-guide/access-token/) authentication, but uses X.509 Certificate instead of token.

Instructions below will describe how to connect MQTT client using X.509 Certificate to SENTIENT Cloud. 

In particular, there are two strategies that can be used for establishing connection between client and SENTIENT:

- **X.509 Certificate chain** - *recommended*. <br>
Configure SENTIENT to trust all client certificates from a specific trust anchor (*intermediate certificate*). 
The device name is automatically discovered from the certificate Common Name using configurable regular expression.
This feature eliminates the need for manual certificate updates on each device when certificate rotation occurs. 
Furthermore, it allows auto-provisioning new devices over MQTT, if *Create new devices* is enabled in the configuration.
- **X.509 Certificate.** <br> Configure SENTIENT to accept connections from the specific devices using pre-configured client certificates.


<div class="st-tabs">

<div class="st-tab" data-label="X.509 Certificate chain (recommended)">

## X.509 Certificate chain:

### Step 1. Prepare your server and certificate chain


Follow the [MQTT over SSL](/docs/user-guide/mqtt-over-ssl/) guide to provision server certificate if you are hosting your own SENTIENT instance.


Once provisioned, you should prepare a CA root certificate in pem format. This certificate will be used by mqtt client to validate the server certificate.
Save the CA root certificate to your working directory as "**ca-root.pem**".
An example of CA root certificate for *localhost* is located [here](/docs/paas/user-guide/resources/mqtt-over-ssl/ca-root.pem).

### Step 2. Generate Client certificate chain

We should generate a certificate chain with **reasonable** Common Names (CNs). We will use the intermediate certificate to sign certificates for our devices.
For example, the certificate chain CNs might be the following: 

 * Root certificate CN: company-name.com;
 * Intermediate certificate: device-group-name.company-name.com;
 * Device certificate: device-name.device-group-name.company-name.com;

Use the following commands to generate the self-signed private keys, certificate signing requests, and x509 certificates
for each chain level. The commands are based on the **OpenSSL** tool, which is most likely already installed on your workstation:

**Step 2.1** Generate root certificate 

Generate the Root certificate and private key, use the following command. Don't forget to put the correct CN when prompted:

```bash
openssl req -x509 -newkey rsa:4096 -keyout rootKey.pem -out rootCert.pem -sha256 -days 365 -nodes
```


<details>
<summary>
Sample output, referencing *company.com* as CN
</summary>
<figure class="highlight"><pre><code class="language-text" data-lang="text">Generating a RSA private key
writing new private key to 'rootKey.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:company.com
Email Address []:</code></pre></figure>
</details>
<br>

**Step 2.2** Generate intermediate certificate 

To generate the intermediate key and certificate request, use the following command. Don't forget to put the correct CN when prompted:

```bash
openssl req -new -newkey rsa:4096 -keyout intermediateKey.pem -out intermediate.csr -sha256 -nodes
```


<details>
<summary>
Sample output, referencing *group.company.com* as CN
</summary>
<figure class="highlight"><pre><code class="language-text" data-lang="text">Generating a RSA private key
writing new private key to 'intermediateKey.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:group.company.com
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:</code></pre></figure>
</details>
<br>

To generate the intermediate certificate, use the following command. Don't forget to put the correct CN when prompted:

```bash
openssl x509 -req -in intermediate.csr -out intermediateCert.pem -CA rootCert.pem -CAkey rootKey.pem -days 365 -sha256 -CAcreateserial -extfile <(echo "basicConstraints=CA:TRUE")
```


<details>
<summary>
Sample output
</summary>
<figure class="highlight"><pre><code class="language-text" data-lang="text">Signature ok
subject=C = AU, ST = Some-State, O = Internet Widgits Pty Ltd, CN = group.company.com
Getting CA Private Key</code></pre></figure>
</details>
<br>


**Step 2.3** Generate device certificate 

To generate the device certificate, use the following command. Don't forget to put the correct CN when prompted:

```bash
openssl req -new -newkey rsa:4096 -keyout deviceKey.pem -out device.csr -sha256 -nodes
```


<details>
<summary>
Sample output, referencing <i>device123.group.company.com</i> as CN
</summary>
<figure class="highlight"><pre><code class="language-text" data-lang="text">Generating a RSA private key
writing new private key to 'deviceKey.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:device.group.company.com
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:</code></pre></figure>
</details>
<br>

To generate the intermediate certificate, use the following command. Don't forget to put the correct CN when prompted:

```bash
openssl x509 -req -in device.csr -out deviceCert.pem -CA intermediateCert.pem -CAkey intermediateKey.pem -days 365 -sha256 -CAcreateserial
```


<details>
<summary>
Sample output
</summary>
<figure class="highlight"><pre><code class="language-text" data-lang="text">Signature ok
subject=C = AU, ST = Some-State, O = Internet Widgits Pty Ltd, CN = device.group.company.com
Getting CA Private Key</code></pre></figure>
</details>
<br>


Finally, you need to concatenate certificates into a chain starting from the device certificate till the root.

```bash
cat deviceCert.pem intermediateCert.pem rootCert.pem > chain.pem
```


The output of the commands will be private keys and certificates for each level of chain. In the next steps
we will use device key file *deviceKey.pem* and a chain of certificates *chain.pem*.

### Step 3. Provision Client Intermediate Public Key as Device Profile X509 provision strategy

Go to **SENTIENT Web UI -> Profiles -> Device profiles -> Your Device profile -> Device provisioning**.
Select **X.509 Certificates Chain** provision strategy, insert the contents of *intermediateCert.pem* file
and regular expression pattern to fetch common name from *deviceCert.pem*, choose allow to create new devices or not and click save.
Alternatively, the same can be done through the [REST API](/docs/reference/rest-api/).

### Step 4. Test the connection

Execute the following command to upload temperature readings to SENTIENT Cloud using secure channel:


```bash
mosquitto_pub --cafile ca-root.pem -d -q 1 -h "YOUR_TB_HOST" -p "8883" \
-t "v1/devices/me/telemetry" --key deviceKey.pem --cert chain.pem -m {"temperature":25}
```


Similar command for the [self-signed](/docs/user-guide/mqtt-over-ssl/#self-signed-certificates-generation) server certificate:

```bash
mosquitto_pub --insecure --cafile server.pem -d -q 1 -h "YOUR_TB_HOST" -p "8883" \
-t "v1/devices/me/telemetry" --key deviceKey.pem --cert chain.pem -m {"temperature":25}
```


 

Don't forget to replace **YOUR_TB_HOST** with the host of your SENTIENT instance.


</div>

<div class="st-tab" data-label="X.509 Certificate">

## X.509 Certificate:

### Step 1. Prepare your server and certificate chain


Follow the [MQTT over SSL](/docs/user-guide/mqtt-over-ssl/) guide to provision server certificate if you are hosting your own SENTIENT instance.


Once provisioned, you should prepare a CA root certificate in pem format. This certificate will be used by mqtt client to validate the server certificate.
Save the CA root certificate to your working directory as "**ca-root.pem**".
An example of CA root certificate for *localhost* is located [here](/docs/paas/user-guide/resources/mqtt-over-ssl/ca-root.pem).

### Step 2. Generate Client certificate

Use the following command to generate the self-signed private key and x509 certificate.
The command is based on the **openssl** tool which is most likely already installed on your workstation:

To generate the RSA based key and certificate, use:

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365 -nodes
```


To generate the EC based key and certificate, use:

```bash
openssl ecparam -out key.pem -name prime256v1 -genkey
openssl req -new -key key.pem -x509 -nodes -days 365 -out cert.pem 
```


The output of the command will be a private key file *key.pem* and a public certificate *cert.pem*.
We will use them in next steps.

### Step 3. Provision Client Public Key as Device Credentials

Go to **SENTIENT Web UI -> Entities -> Devices -> Your Device -> Manage credentials**.
Select **X.509 Certificate** device credentials, insert the contents of *cert.pem* file and click save.
Alternatively, the same can be done through the [REST API](/docs/reference/rest-api/).

### Step 4. Test the connection

Execute the following command to upload temperature readings to SENTIENT Cloud using secure channel:


```bash
mosquitto_pub --cafile ca-root.pem -d -q 1 -h "YOUR_TB_HOST" -p "8883" \
-t "v1/devices/me/telemetry" --key key.pem --cert cert.pem -m {"temperature":25}
```


Don't forget to replace **YOUR_TB_HOST** with the host of your SENTIENT instance.


</div>

</div>
