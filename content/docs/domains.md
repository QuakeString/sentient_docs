+++
title = "Managing domain"
description = "Domain managing through SENTIENT"

[extra]
status = "imported"
checked = ""
source = "docs/domains.md"
+++
[SENTIENT](/docs/user-guide/install/installation-options/)  allows you to use a custom domain to provide secure user access.
To achieve this, you need to configure an HAProxy Load Balancer and provide an SSL certificate. [This documentation](/docs/user-guide/install/pe/add-haproxy-ubuntu/) will help you do this.
Once set up, you will be able to access the SENTIENT platform through your custom domain using a secure (HTTPS) connection.


## Domain registration


<div class="st-callout info">


**Note**: You must be owner of the domain you are registering.


</div>


In order to use your own host name instead of **IP address** you must register it first. To do this, follow these steps:

First, on your DNS provider&#39;s website, you must add a canonical record for your domain to map it with eu.sentient.cloud. See [How to Create a CNAME Record For Your Domain](#how-to-create-a-cname-record) for details.

Once done, you can start the procedure of adding a domain. 

## Add domain


<div class="st-callout info">


</div>


- Log in to [SENTIENT](/docs/user-guide/install/installation-options/) account as system administrator;


1. Go to the "OAuth 2.0" page of the "Security" section. On the "Domains" tab click the "plus" icon;

1. Enter valid domain name in the "Domain name" field and click "Add" button;

1. You can see your domain name on the "Domains" tab.


<div class="st-gallery"><figure><img src="/images/user-guide/domain/adding-new-domain-1-ce.webp" alt="Go to the &quot;OAuth 2.0&quot; page of the &quot;Security&quot; section. On the &quot;Domains&quot; tab click the &quot;plus&quot; icon;" loading="lazy"><figcaption>Go to the "OAuth 2.0" page of the "Security" section. On the "Domains" tab click the "plus" icon;</figcaption></figure><figure><img src="/images/user-guide/domain/adding-new-domain-2-ce.webp" alt="Enter valid domain name in the &quot;Domain name&quot; field and click &quot;Add&quot; button;" loading="lazy"><figcaption>Enter valid domain name in the "Domain name" field and click "Add" button;</figcaption></figure><figure><img src="/images/user-guide/domain/adding-new-domain-3-ce.webp" alt="You can see your domain name on the &quot;Domains&quot; tab." loading="lazy"><figcaption>You can see your domain name on the "Domains" tab.</figcaption></figure></div>


## Log in with your chosen domain name

Now you can use your domain name to access SENTIENT web interface and services. Try to login by entering the chosen domain name in the browser address line.


<div class="st-gallery"><figure><img src="/images/user-guide/domain/domain-login-1-ce.webp" alt="Now you can use your domain name to access SENTIENT web interface and services. Try to login by entering the chosen domain name in the browser address line." loading="lazy"><figcaption>Now you can use your domain name to access SENTIENT web interface and services. Try to login by entering the chosen domain name in the browser address line.</figcaption></figure></div>


## Domain details

To view details about a registered domain, simply click on it to open the domain details dialog.
 This dialog provides information about registered domain CNAME record and issued "SSL certificate" details including current validity period (*Not before* and *Not after*).


The SSL certificate is valid for 90 days, but no need to worry — SENTIENT will automatically renew it at least 30 days before it expires.
No action is required on your part unless you change or delete the domain&#39;s CNAME record.


<div class="st-gallery"><figure><img src="/images/user-guide/domain/domain-details-1-ce.webp" alt="To view details about a registered domain, simply click on it to open the domain details dialog. Switch to editing mode by clicking the large orange button;" loading="lazy"><figcaption>To view details about a registered domain, simply click on it to open the domain details dialog. Switch to editing mode by clicking the large orange button;</figcaption></figure><figure><img src="/images/user-guide/domain/domain-details-2-ce.webp" alt="Make the required modifications. Confirm and save your changes by clicking the &quot;Apply changes&quot; button." loading="lazy"><figcaption>Make the required modifications. Confirm and save your changes by clicking the "Apply changes" button.</figcaption></figure></div>


## Delete domain

To delete the registered domain click "trash" icon in the domain's row you want to delete. In the confirmation dialog, click "Yes" if you are sure you want to delete the domain.


<div class="st-gallery"><figure><img src="/images/user-guide/domain/delete-domain-1-ce.webp" alt="To delete the domain click &quot;Delete&quot; button on the &quot;Domain&quot; tab;" loading="lazy"><figcaption>To delete the domain click "Delete" button on the "Domain" tab;</figcaption></figure><figure><img src="/images/user-guide/domain/delete-domain-2-ce.webp" alt="In the confirmation dialog, click &quot;Yes&quot; if you are sure you want to delete the domain." loading="lazy"><figcaption>In the confirmation dialog, click "Yes" if you are sure you want to delete the domain.</figcaption></figure></div>


Once confirmed, the domain information and associated SSL certificate will be deleted, and you will not be able to access SENTIENT web interface and services using that domain.
You can always re-register the same or a different domain using [Domain registration](#domain-registration) procedure.

## How to Create a CNAME Record For Your Domain {#how-to-create-a-cname-record}

The procedure of adding CNAME record to DNS database depending on your DNS service Provider. Below is the list of instructions for some popular DNS providers:

* [Amazon Route 53](https://aws.amazon.com/premiumsupport/knowledge-center/route-53-create-alias-records/)
* [GoDaddy](https://www.godaddy.com/help/add-a-cname-record-19236)
* [Cloudflare](https://community.cloudflare.com/t/how-do-i-add-a-cname-record/59)
* [ClouDNS](https://www.cloudns.net/wiki/article/13/)
* [Google Cloud DNS](https://cloud.google.com/dns/docs/records)
* [Name.com](https://www.name.com/support/articles/115004895548-adding-a-cname-record)
* [easyDNS](https://kb.easydns.com/knowledge/how-to-make-a-dns-entry/)
* [DNSimple](https://support.dnsimple.com/articles/manage-cname-record/#adding-a-cname-record)
* [DNSMadeEasy](https://support.dnsmadeeasy.com/hc/en-us/articles/34327195668507-CNAME-Record)
* [No-IP.com](https://www.noip.com/support/knowledgebase/how-to-configure-your-no-ip-hostname/)
* [Infoblox NIOS](https://docs.infoblox.com/display/BloxOneDDI/Creating+a+CNAME+Record)
* [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain)

If none of the DNS providers listed above is the one you are using, try to find this information on the provider&#39;s website or by reaching out to their support team.

## Troubleshooting

Firs of all you need to check if you have added CNAME to your domain correctly:

Use [Google Admin Toolbox](https://toolbox.googleapps.com/apps/dig/) or "dig" command if your OS system is Linux:
```bash
dig $YOUR_DOMAIN_NAME any
```


Replace $YOUR_DOMAIN_NAME with your domain value.

For example, $YOUR_DOMAIN_NAME is `mycompany.sentient.space`:
```bash
dig mycompany.sentient.space any
```

The "dig" command in Linux is used to gather DNS information. It stands for Domain Information Groper, and it collects data about Domain Name Servers. The "dig" command is helpful for diagnosing DNS problems, but is also used to display DNS information.

The output of "dig" command could vary duy to your domain setup.
For example:
```bash
$ dig mycompany.sentient.space any

; <<>> DiG 9.16.1-Ubuntu <<>> mycompany.sentient.space any
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 27275
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;mydomain.sentient.online.	IN	ANY

;; ANSWER SECTION:
mycompany.sentient.space. 3600 IN	HINFO	"RFC8482" ""

;; Query time: 36 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: чт чер 29 15:36:44 EEST 2023
;; MSG SIZE  rcvd: 77
```

This output shows that there are NO CNAME added to the mycompany.sentient.space domain ("ANSWER SECTION" block).

Correct output should look like that:
```bash
...
;; ANSWER SECTION:
mycompany.sentient.space. 3600 IN	CNAME	eu.sentient.cloud
...
```

If all the things are correct, but some issue still persists - please [contact us](https://sentient.invenia.in/docs/contact-us/) for further support.

## Next step


<div class="st-callout info"><p class="st-callout-title">SENTIENT Professional Edition feature</p>


Only [**Professional Edition**](/products/sentient-pe/) supports **White labeling** feature.<br>
Use [**SENTIENT Cloud**](/installations/choose-region/) or [**install**](/docs/user-guide/install/pe/installation-options/) your own platform instance.


</div>


Learn how to customize SENTIENT login page and user interface, configure your company or product logo, and adjust the color scheme, navigate to the [White labeling](/docs/user-guide/white-labeling/) section.
