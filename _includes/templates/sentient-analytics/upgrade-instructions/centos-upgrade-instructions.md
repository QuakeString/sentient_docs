{%- assign platform = "SENTIENT ANALYTICS" -%}
{%- assign current_version = include.version -%}
{%- assign family = include.family -%}
{%- assign patch_status = include.patch_status -%}
{%- assign base_version = include.base_version -%}

{%- assign curr_parts = current_version | split: "." -%}

{%- assign curr_major = curr_parts[0] -%}
{%- assign curr_minor = curr_parts[1] -%}

{%- assign curr_major_n = curr_major | plus: 0 -%}
{%- assign curr_minor_n = curr_minor | plus: 0 -%}

{% if patch_status == "true" %}
### Upgrading {{ platform }} to latest {{ base_version }} ({{ current_version }})
{% else %}
### Upgrading {{ platform }} to {{ current_version }}
{% endif %}

{%- assign platform_hash = "#upgrading-sentient-analytics-analytics-to-" -%}

{% capture difference %}
**NOTE:**
<br>
[**Prepare**](#prepare-for-upgrading-sentient-analytics-analytics) for upgrading SENTIENT ANALYTICS.
{% endcapture %}
{% include templates/info-banner.md content=difference %}

{% capture tb_haproxy_note %}
**NOTE:**
<br>
If you are using SENTIENT ANALYTICS behind **HAProxy**, make sure that the paths **`/sentient-analytics/`** and **`/apiSENTIENT ANALYTICS/`** are routed to the SENTIENT ANALYTICS backend instead of **`/sentient-analytics`** and **`/apiSENTIENT ANALYTICS`**.
**NOTE:**
<br>
Additionally, we highly recommend adding SENTIENT ANALYTICS to the **SENTIENT HAProxy configuration** so that SENTIENT ANALYTICS is accessible from the **same domain as SENTIENT**.
{% endcapture %}
{% include templates/warn-banner.md content=tb_haproxy_note %}

#### SENTIENT ANALYTICS package download

```bash
wget https://dist.sentient.invenia.in/sentient-analytics-{{ current_version }}.rpm
```
{: .copy-code}

#### SENTIENT ANALYTICS service upgrade

* Install latest SENTIENT ANALYTICS service

```bash
sudo rpm -Uvh sentient-analytics-{{ current_version }}.rpm
```
{: .copy-code}

**NOTE:** Package installer will ask you to merge your SENTIENT ANALYTICS configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.

Execute regular upgrade script:

```bash
sudo /usr/share/sentient-analytics/bin/install/upgrade.sh
```
{: .copy-code}

#### Start the service

```bash
sudo service sentient-analytics start
```
{: .copy-code}

#### Sync SENTIENT ANALYTICS with SENTIENT

After upgrade, it's necessary to sync SENTIENT ANALYTICS with SENTIENT. You can find out how to do it [here](/docs/sentient-analytics/install/rhel#step-6-sync-sentient-with-sentient-analytics).
