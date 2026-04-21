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
<br>
Additionally, we highly recommend adding SENTIENT ANALYTICS to the **SENTIENT HAProxy configuration** so that SENTIENT ANALYTICS is accessible from the **same domain as SENTIENT**.
{% endcapture %}
{% include templates/warn-banner.md content=tb_haproxy_note %}

#### {{ platform }} service upgrade

{% include docs/sentient-analytics/install/docker-upgrade-steps.md version=current_version %}

#### Sync SENTIENT ANALYTICS with SENTIENT

After upgrade, it's necessary to sync SENTIENT ANALYTICS with SENTIENT. You can find out how to do it [here](/docs/sentient-analytics/install/docker#step-6-sync-sentient-with-sentient-analytics).

