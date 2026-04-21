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

{% capture tb_haproxy_note %}
**NOTE:**
<br>
If you are using SENTIENT ANALYTICS behind **HAProxy**, make sure that the paths **`/sentient-analytics/`** and **`/apiSENTIENT ANALYTICS/`** are routed to the SENTIENT ANALYTICS backend instead of **`/sentient-analytics`** and **`/apiSENTIENT ANALYTICS`**.
Additionally, we highly recommend adding SENTIENT ANALYTICS to the **SENTIENT HAProxy configuration** so that SENTIENT ANALYTICS is accessible from the **same domain as SENTIENT**.
{% endcapture %}
{% include templates/warn-banner.md content=tb_haproxy_note %}

#### SENTIENT ANALYTICS package download

Download SENTIENT ANALYTICS installation package for Windows: [sentient-analytics-windows-{{ current_version }}.zip](https://dist.sentient.invenia.in/sentient-analytics-windows-{{ current_version }}.zip).

#### SENTIENT ANALYTICS service upgrade

* Stop SENTIENT ANALYTICS service if it is running.

```text
net stop sentient-analytics
```
{: .copy-code}

* Make a backup of previous SENTIENT ANALYTICS configuration located in \<SENTIENT ANALYTICS install dir\>\conf (for ex. C:\sentient-analytics\conf).
* Remove SENTIENT install dir.
* Unzip installation archive to SENTIENT install dir.
* Compare your old SENTIENT ANALYTICS configuration files (from the backup you made in the first step) with new ones.

{% assign base_version_parts = base_version | split: "." %}
{% assign patch_part = base_version_parts[2] %}
{% if patch_status == "true" %}
{% capture update_note %}
**NOTE:**
If you are upgrading from version {{ family | append: "." | append: patch_part | append: ".x" }}, **DO NOT** run the upgrade script; proceed directly to starting the service.
{% endcapture %}
{% include templates/info-banner.md content=update_note %}
{% endif %}

* Finally, run **upgrade.bat** script to upgrade SENTIENT ANALYTICS to the new version.

**NOTE** Scripts listed above should be executed using Administrator Role. 

```text
C:\sentient-analytics>upgrade.bat
```
{: .copy-code}

#### Start the service

```text
net start sentient-analytics
```
{: .copy-code}

#### Sync SENTIENT ANALYTICS with SENTIENT

After upgrade, it's necessary to sync SENTIENT ANALYTICS with SENTIENT. You can find out how to do it [here](/docs/sentient-analytics/install/windows#step-6-sync-sentient-with-sentient-analytics).