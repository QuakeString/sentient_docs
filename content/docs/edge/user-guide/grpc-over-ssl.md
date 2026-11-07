+++
title = "Edge over TLS/SSL"
description = "Edge over TLS/SSL"

[extra]
status = "imported"
checked = ""
source = "docs/edge/user-guide/grpc-over-ssl.md"
+++
This guide outlines steps to secure connections between SENTIENT and Edge instances using gRPC connections over TLS/SSL.

You can configure SSL termination in two ways: by utilizing the built-in SSL capabilities of the platform for gRPC traffic or by employing an external load balancer as the termination point.

The instructions are divided into two main parts: configuring the server side (platform) and the client side (edge).

## Server SSL Configuration

Choose between the built-in mechanism or using a load balancer for SSL termination for gRPC traffic. Use the content toggle below to select and view the instructions for each option.


<div class="tb-content-toggle" id="platformOption">
    <div class="panel panel-default">
        <div class="panel-heading">
            
            
            
            
            <a class="content-toggle-button" data-target="#build_in">
                <div class="content-toggle-button-text">
                    Build-in mechanism
                </div>
            </a>
            
            
            
            
            <a class="content-toggle-button" data-target="#load_balancer">
                <div class="content-toggle-button-text">
                    Load Balancer
                </div>
            </a>
            
        </div>
        
        
        
        
        
        <div id="build_in" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


Follow the instructions below to generate your own certificate files. This approach is useful for testing but is time-consuming and not recommended for production environments.

#### Generate a Private Key


Generate a new private key using the command below. This will create a 2048-bit RSA private key and store it in a file named `privateKey.pem`:

```bash
openssl genpkey -algorithm RSA -out privateKey.pem -pkeyopt rsa_keygen_bits:2048
```


#### Generate a Certificate Signing Request (CSR)


Next, use your private key to generate a CSR. 
You will need to provide details such as your organization's name, common name (domain name), and an email address, which will be included in the certificate's subject field. 
Save the CSR as `certRequest.csr`:

```bash
openssl req -new -key privateKey.pem -out certRequest.csr
```


<div class="st-callout warn">


If your SENTIENT server is running locally, ensure you set 'localhost' as the common name (domain name) when generating your certificate. 
If the server is hosted, use its domain name. 

SSL connections will fail if the certificate's domain name does not match the server's hostname.


</div>


#### Generate a Self-Signed Certificate


Finally, create a self-signed certificate from your CSR. The following command generates a certificate named `certFile.crt`, valid for 365 days. You can modify the `-days` parameter to adjust the certificate's validity period:

```bash
openssl x509 -req -in certRequest.csr -signkey privateKey.pem -out certFile.crt -days 365
```


#### Enable SSL Communication on the Server


For both Ubuntu and CentOS/RHEL installations, enable SSL communication server-side with the following command:

```bash
sudo sh -c 'cat <<EOL >> /etc/sentient/conf/sentient.conf
export EDGES_RPC_SSL_ENABLED=true
export EDGES_RPC_SSL_CERT=certFile.crt
export EDGES_RPC_SSL_PRIVATE_KEY=privateKey.pem
EOL'
```


Restart the server to apply the changes:

```bash
sudo systemctl restart sentient
```


                </td></tr></table>
            </div>
        </div>
        
        
        
        
        
        <div id="load_balancer" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


The guide recommends using HAProxy as the SSL termination point for your platform.

For those utilizing Ubuntu Server, please follow [these specific steps](/docs/user-guide/install/pe/add-haproxy-ubuntu/#step-6-configure-edge-tls-communication-optional).

If you're on a CentOS/RHEL Server, adhere to [these instructions](/docs/user-guide/install/pe/add-haproxy-rhel/#step-6-configure-edge-tls-communication-optional).


                </td></tr></table>
            </div>
        </div>
        
    </div>
</div>


## Configuring Edge to Use SSL Connection

### Ubuntu or CentOS/RHEL

To enable SSL communication on the Edge for Ubuntu or CentOS/RHEL installations, execute the following command:

```bash
sudo sh -c 'cat <<EOL >> /etc/tb-edge/conf/tb-edge.conf
export CLOUD_RPC_SSL_ENABLED=true
EOL'
```


If you are using self-signed certificates, it is necessary to add the server-side public certificate to the Edge's configuration to verify the server's certificate:

```bash
sudo sh -c 'cat <<EOL >> /etc/tb-edge/conf/tb-edge.conf
export CLOUD_RPC_SSL_CERT=certFile.crt
EOL'
```


To apply these changes, restart the Edge:

```bash
sudo systemctl restart tb-edge
```


### Docker

In Docker setups, make sure the **CLOUD_RPC_SSL_ENABLED** variable in the `docker-compose.yml` file is set to 'true'. 
If using self-signed certificates, also set **CLOUD_RPC_SSL_CERT** accordingly.

After making these changes, restart the SENTIENT Edge docker container with the command:

```bash
docker compose restart mytbedge
```


### Next Steps
