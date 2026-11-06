+++
title = "LwM2M over DTLS"
description = "Launching SENTIENT with secure LwM2M protocol to connect your IoT devices and projects."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ssl/lwm2m-over-dtls.md"
+++
SENTIENT provides the ability to run LwM2M server over DTLS. 
Platform supports Pre-Shared Key, Raw Public Key and X.509 Certificate credentials over DTLS.
DTLS provisioning requires valid [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) certificates. 
ECDSA keys are smaller than RSA keys and thus more preferable for constrained devices. 
See comparison [article](https://sectigostore.com/blog/ecdsa-vs-rsa-everything-you-need-to-know/) for more details.
We recommend to use valid SSL certificates generated using trusted CA authorities and avoid spending time on resolving issues with [self-signed certificates](#self-signed-certificates-generation).
See instructions below on how to configure SSL for certificates stored in PEM file format or Java Keystore.


## DTLS configuration using PEM certificates file


<table style="width:auto">
   <thead>
     <tr>
	 <td style="text-align: center"><strong><em>Available since TB Version 3.3.2</em></strong></td>
     </tr>
   </thead>
</table> 


Configure the following environment variables via [configuration](/docs/user-guide/install/config/) file, docker-compose or kubernetes scripts.
We will use **sentient.conf** for example:

```bash
...
export LWM2M_SERVER_CREDENTIALS_ENABLED=true
export LWM2M_SERVER_CREDENTIALS_TYPE=PEM
export LWM2M_SERVER_PEM_CERT=server.pem
export LWM2M_SERVER_PEM_KEY=server_key.pem
export LWM2M_SERVER_PEM_KEY_PASSWORD=secret
# To enable Bootstrap and Bootstrap over DTLS
export LWM2M_ENABLED_BS=true
export LWM2M_BS_CREDENTIALS_ENABLED=true
export LWM2M_BS_CREDENTIALS_TYPE=PEM
export LWM2M_BS_PEM_CERT=server.pem
export LWM2M_BS_PEM_KEY=server_key.pem
export LWM2M_BS_PEM_KEY_PASSWORD=secret
...
```

where:

* LWM2M_SERVER_CREDENTIALS_ENABLED - Enable/disable X509 Certificate/RPK credentials support;
* LWM2M_SERVER_CREDENTIALS_TYPE -  Server credentials type. PEM - pem certificate file; KEYSTORE - java keystore;
* LWM2M_SERVER_PEM_CERT - Path to the server certificate file. Holds server certificate or certificate chain, may also include server private key;
* LWM2M_SERVER_PEM_KEY - Path to the server certificate private key file. Optional by default. Required if the private key is not present in server certificate file;
* LWM2M_SERVER_PEM_KEY_PASSWORD - Optional server certificate private key password.

After completing the setup, start or restart the SENTIENT server.


<div class="st-callout warn">


**Make sure the certificate files are reachable by SENTIENT process:**

* Linux: use */etc/sentient/conf* folder. Make sure the files have same permissions as *sentient.conf*; Use relative file path, e.g. *server.pem*;
* Docker Compose: mount or use existing volume to */config* folder of the container; Use full file path, e.g. */config/server.pem*;
* K8S: mount separate volume to */https-config* or similar folder. Use full file path, e.g. */https-config/server.pem*;
* Windows: use *C:\Program Files (x86)\sentient\conf\\* folder. Make sure the files have same permissions as *sentient.conf*; Use relative file path, e.g. *server.pem*;


</div>


## Additional configuration properties

You may configure following additional environment variables via [configuration](/docs/user-guide/install/config/) file, docker-compose or kubernetes scripts.

* LWM2M_SECURITY_BIND_ADDRESS - the bind address for the secure LwM2M server. Default value *0.0.0.0* indicates all interfaces;
* LWM2M_SECURITY_BIND_PORT - the bind port for the secure LwM2M server. Default value is *5686*;
* TB_LWM2M_SERVER_SECURITY_SKIP_VALIDITY_CHECK_FOR_CLIENT_CERT - Skip certificate validity check for client certificates. Default value is *false*.
* LWM2M_BS_SECURITY_BIND_ADDRESS - the bind address for the secure LwM2M Bootstrap server. Default value *0.0.0.0* indicates all interfaces;
* LWM2M_BS_SECURITY_BIND_PORT - he bind port for the secure LwM2M Bootstrap server. Default value is *5688*;

## Self-signed certificates generation

Use the instructions below to generate your own certificate files. Useful for tests, but time-consuming and not recommended for production.

> **Note:** These steps require Linux-based OS with openssl installed.

You need to either create a self-signed certificate for the server or follow the advanced steps to create a CA-signed server certificate. 
Both methods achieve the same goal: securing your server with a valid certificate.

#### Self-signed certificate PEM file

This is a simpler method where the server generates its own certificate and signs it. 
Useful for basic testing or small setups where you don't need a Certificate Authority (CA).
To generate a server self-signed PEM certificate and private key, use the following command:

```bash
openssl ecparam -out server_key.pem -name secp256r1 -genkey
openssl req -new -key server_key.pem -x509 -nodes -days 365 -out server.pem 
```


You can also add `-nodes` (short for no DES) if you don't want to protect your private key with a passphrase. Otherwise, it will prompt you for "at least a 4 character" password.

The **days** parameter (365) you can replace with any number to affect the expiration date. It will then prompt you for things like "Country Name", but you can just hit Enter and accept the defaults.

Add `-subj '/CN=localhost'` to suppress questions about the contents of the certificate (replace localhost with your desired domain).

Self-signed certificates are not validated with any third party unless you import them to the browsers previously. If you need more security, you should use a certificate signed by a certificate authority (CA).

#### Certificate PEM File signed by a certificate authority (CA)

This method creates a Certificate Authority (CA) to sign your server certificate. For more secure setups,
particularly if you plan to manage multiple certificates or require a dedicated Certificate Authority (CA) for signing.

**Generate a CA private key:**

```bash
openssl ecparam -out ca_key.pem -name secp256r1 -genkey
```


**Generate a self-signed CA certificate:**

```bash
openssl req -new -x509 -key ca_key.pem -days 365 -out ca.pem
```


This creates a self-signed CA certificate "**ca.pem**" valid for 365 days. When prompted, fill out the certificate details (e.g., Common Name: My Root CA).

**Generate a private key for the server:**

```bash
openssl ecparam -out server_key.pem -name secp256r1 -genkey
```


This generates an **EC private key: server_key.pem**.

**Create a Certificate Signing Request (CSR):**

```bash
openssl req -new -key server_key.pem -out server.csr
```


The CSR "**server.csr**" contains the server's details to be signed by the CA.

**Finally, Sign the server certificate using the CA:**

```bash
openssl x509 -req -in server.csr -CA ca.pem -CAkey ca_key.pem -CAcreateserial -out server.pem -days 365
```


This command produces "**server.pem**", a server certificate signed by the CA.

`-req` - indicates that the input is a Certificate Signing Request (CSR).
`-CA` and `-CAkey` - specify the CA certificate "**ca.pem**" and its private key "**ca_key.pem**" used to sign the server certificate.

The `-CAcreateserial` flag automatically generates a serial number file "**ca.srl**" to keep track of certificate serial numbers for this CA. 
This is useful if you plan to sign multiple certificates. If you don’t want to generate "**ca.srl**", replace `-CAcreateserial` with `-set_serial <serial_number>` to specify the serial number manually.


## Client Examples

See following resources:

- [Access Token based authentication](/docs/user-guide/ssl/coap-access-token/) for example of **one-way SSL** connection;
- [X.509 Certificate based authentication](/docs/user-guide/ssl/coap-x509-certificates/) for example of **two-way SSL** connection.
