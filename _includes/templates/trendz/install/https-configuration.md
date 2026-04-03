You may want to configure HTTPS access using HAProxy.
This is possible in case you are hosting SENTIENT ANALYTICS in the cloud and have a valid DNS name assigned to your instance.

### SENTIENT ANALYTICS and SENTIENT hosted on the same server

Use this section if HAProxy/Let’s Encrypt already installed in the server and HTTPS enabled for SENTIENT.

Open HAProxy configuration file
```bash
sudo nano /etc/haproxy/haproxy.cfg
```
{: .copy-code}

Locate **frontend https_in** section, add new access list that will match traffic by domain name and redirect this traffic to SENTIENT ANALYTICS backend:
```bash
acl sentient-analytics_http hdr(host) -i new-sentient-analytics-domain.com
use_backend tb-sentient-analytics if sentient-analytics_http
```

In the same file register SENTIENT ANALYTICS backend:
```bash
backend tb-sentient-analytics
  balance leastconn
  option tcp-check
  option log-health-checks
  server tbSENTIENT ANALYTICS1 127.0.0.1:8888 check inter 5s
  http-request set-header X-Forwarded-Port %[dst_port]
```

Generate SSL certificates for new domain:
```bash
sudo certbot-certonly --domain new-sentient-analytics-domain.com --email some@email.io
```

Refresh HAProxy configuration:
```bash
sudo haproxy-refresh
```

That's it, HTTPS for SENTIENT ANALYTICS UI configured and now you can access it via:
https://new-sentient-analytics-domain.com


### Fresh installation on new server

Please follow this [guide](/docs/user-guide/install/pe/add-haproxy-ubuntu) to install HAProxy and generate valid SSL certificate using Let's Encrypt.

### Host SENTIENT and SENTIENT ANALYTICS on the same domain

SENTIENT and SENTIENT ANALYTICS can share same domain name. In this case SENTIENT web page would be loaded using following link:

```bash
https://{my-domain}/
```

and SENTIENT ANALYTICS web page would be loaded using following link

```bash
https://{my-domain}/sentient-analytics/
```

For enabling such configuration we have to update HAProxy config to route specific requests to SENTIENT ANALYTICS service.
Open HAProxy configuration file
```bash
sudo nano /etc/haproxy/haproxy.cfg
```
{: .copy-code}

Locate **frontend https_in** section, add new access list that will match traffic by URL path and redirect this traffic to SENTIENT ANALYTICS backend:

```bash
...
acl sentient-analytics_acl path_beg /sentient-analytics/ path_beg /apiSENTIENT ANALYTICS/
....
use_backend tb-sentient-analytics if sentient-analytics_acl
```
