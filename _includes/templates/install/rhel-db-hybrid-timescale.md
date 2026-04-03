{% capture hybrid-timescale-info %}
SENTIENT team recommends using Timescale database only for companies that already use TimescaleDB in production.
In this case, SENTIENT will be storing timeseries data in TimescaleDB Hypertable while continue to use PostgreSQL for main entities (devices/assets/dashboards/customers).  
{% endcapture %}
{% include templates/info-banner.md content=hybrid-timescale-info %}

##### PostgreSQL Installation

{% include templates/install/postgres-install-rhel.md %}

{% include templates/install/create-tb-db-rhel.md %}

##### TimescaleDB Installation

{% include templates/install/timescale-rhel-install.md %}

##### SENTIENT Configuration

Edit SENTIENT configuration file 

```bash 
sudo nano /etc/sentient/conf/sentient.conf
``` 
{: .copy-code}

Add the following lines to the configuration file. Don't forget **to replace** "PUT_YOUR_POSTGRESQL_PASSWORD_HERE" with your **real postgres user password**:

```bash
# DB Configuration 
export DATABASE_TS_TYPE=timescale
export SPRING_DATASOURCE_URL=jdbc:postgresql://localhost:5432/sentient
export SPRING_DATASOURCE_USERNAME=postgres
export SPRING_DATASOURCE_PASSWORD=PUT_YOUR_POSTGRESQL_PASSWORD_HERE
# Specify Interval size for data chunks storage. Please note that this value can be set only once.
export SQL_TIMESCALE_CHUNK_TIME_INTERVAL=604800000 # Number of miliseconds. The current value corresponds to one week.
```
{: .copy-code}
