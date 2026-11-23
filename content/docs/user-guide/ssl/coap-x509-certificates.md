+++
title = "X.509 Certificate Based Authentication for CoAP over DTLS"
description = "SENTIENT  X.509 Certificate based authentication for CoAP over DTLS."

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/ssl/coap-x509-certificates.md"
+++
X.509 Certificates are used to setup [mutual](https://en.wikipedia.org/wiki/Mutual_authentication) (two-way) authentication for CoAP over DTLS.
It is similar to [access token](/docs/user-guide/access-token/) authentication, but uses X.509 Certificate instead of token.

Instructions below will describe how to connect CoAP client using X.509 Certificate to SENTIENT Cloud.

## Step 1. Generate Client certificate

Use the following command to generate the self-signed EC based private key and x509 certificate.
The command is based on the **openssl** tool which is most likely already installed on your workstation:

```bash
openssl ecparam -out key.pem -name secp256r1 -genkey
openssl req -new -key key.pem -x509 -nodes -days 365 -out cert.pem 
```


The output of the command will be a private key file *key.pem* and a public certificate *cert.pem*.
We will use them in next steps.

## Step 2. Provision Client Public Key as Device Credentials

Go to **SENTIENT Web UI -> Devices -> Your Device -> Device Credentials**.

Select **X.509 Certificate** device credentials, insert the contents of *cert.pem* file and click save.
Alternatively, the same can be done through the [REST API](/docs/reference/rest-api/).

## Step 3. Connect DTLS CoAP Client using X.509 certificate

Install the CoAP client with DTLS support on Linux by following the next steps:
 
- step 1: clone libcoap git repo: 

```bash
git clone https://github.com/obgm/libcoap --recursive --depth 1
```


- step 2: navigate into libcoap directory:

```bash
cd libcoap
```


- step 3: execute next commands and then run ./autogen.sh script:

```bash
sudo apt-get update
```


```bash
sudo apt-get install autoconf libtool libssl-dev
```


```bash
./autogen.sh
```


- step 4: run ./configure script with next options:

```bash
./configure --with-openssl --disable-doxygen --disable-manpages --disable-shared
```


- step 5: execute next command:

```bash
make
```


- step 6: execute next command:

```bash
sudo make install
```


Finally, run the example script below to validate DTLS with X.509 Certificate auth and subscribe for shared attributes updates:
The coap-client example below demonstrates how to connect to [SENTIENT Cloud](https://localhost/signup) or to any other SENTIENT CoAP server that has valid and trusted certificate.

```bash
coap-client-openssl -v 9 -c cert.pem  -j key.pem -m POST \
-t "application/json" -e '{"temperature":43}' coaps://localhost/api/v1/telemetry
```


Don't forget to replace **localhost** with the host of your SENTIENT instance.
