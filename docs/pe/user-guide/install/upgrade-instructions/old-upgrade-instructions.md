---
layout: docwithnav-pe
assignees:
- ashvayka
title: Upgrade instructions
description: SENTIENT Professional Edition IoT platform upgrade instructions
hidetoc: "true"

---

<ul id="markdown-toc">
  <li>
    <a href="#upgrading-to-241pe" id="markdown-toc-upgrading-to-241pe">Upgrading to 2.4.1PE</a>
    <ul>
        <li>
            <a href="#ubuntucentos" id="markdown-toc-ubuntucentos-1">Ubuntu/CentOS</a>
        </li>
        <li>
            <a href="#windows" id="markdown-toc-windows-1">Windows</a>
        </li>
    </ul>
  </li>
  <li>
      <a href="#upgrading-to-2421pe" id="markdown-toc-upgrading-to-2421pe">Upgrading to 2.4.2.1PE</a>
      <ul>
          <li>
              <a href="#ubuntucentos-1" id="markdown-toc-ubuntucentos-2">Ubuntu/CentOS</a>
          </li>
          <li>
              <a href="#windows-1" id="markdown-toc-windows-2">Windows</a>
          </li>
      </ul>
  </li>
  <li>
      <a href="#upgrading-to-243pe" id="markdown-toc-upgrading-to-243pe">Upgrading to 2.4.3PE</a>
      <ul>
          <li>
              <a href="#ubuntucentos-2" id="markdown-toc-ubuntucentos-3">Ubuntu/CentOS</a>
          </li>
          <li>
              <a href="#windows-2" id="markdown-toc-windows-3">Windows</a>
          </li>
      </ul>
  </li>
  <li>
        <a href="#upgrading-to-25pe" id="markdown-toc-upgrading-to-25pe">Upgrading to 2.5PE</a>
        <ul>
            <li>
                <a href="#ubuntucentos-3" id="markdown-toc-ubuntucentos-4">Ubuntu/CentOS</a>
            </li>
            <li>
                <a href="#windows-3" id="markdown-toc-windows-4">Windows</a>
            </li>
        </ul>
    </li>
  <li>
        <a href="#upgrading-to-251pe" id="markdown-toc-upgrading-to-251">Upgrading to 2.5.1PE</a>
        <ul>
             <li>
                 <a href="#ubuntucentos-251" id="markdown-toc-ubuntucentos-20">Ubuntu/CentOS</a>
             </li>
             <li>
                 <a href="#windows-251" id="markdown-toc-windows-20">Windows</a>
             </li>
        </ul>
  </li>
  <li>
        <a href="#upgrading-to-252pe" id="markdown-toc-upgrading-to-252">Upgrading to 2.5.2PE</a>
        <ul>
             <li>
                 <a href="#ubuntucentos-252" id="markdown-toc-ubuntucentos-252">Ubuntu/CentOS</a>
             </li>
             <li>
                 <a href="#windows-252" id="markdown-toc-windows-252">Windows</a>
             </li>
        </ul>
  </li>
  <li>
        <a href="#upgrading-to-253pe" id="markdown-toc-upgrading-to-253">Upgrading to 2.5.3PE</a>
        <ul>
             <li>
                 <a href="#ubuntucentos-253" id="markdown-toc-ubuntucentos-253">Ubuntu/CentOS</a>
             </li>
             <li>
                 <a href="#windows-253" id="markdown-toc-windows-253">Windows</a>
             </li>
        </ul>
    </li>
  <li>
        <a href="#upgrading-to-254pe" id="markdown-toc-upgrading-to-254">Upgrading to 2.5.4PE</a>
        <ul>
             <li>
                 <a href="#ubuntucentos-254" id="markdown-toc-ubuntucentos-254">Ubuntu/CentOS</a>
             </li>
             <li>
                 <a href="#windows-254" id="markdown-toc-windows-254">Windows</a>
             </li>
        </ul>
  </li>
  <li>
        <a href="#upgrading-to-255pe" id="markdown-toc-upgrading-to-255">Upgrading to 2.5.5PE</a>
        <ul>
             <li>
                 <a href="#ubuntucentos-255" id="markdown-toc-ubuntucentos-255">Ubuntu/CentOS</a>
             </li>
             <li>
                 <a href="#windows-255" id="markdown-toc-windows-255">Windows</a>
             </li>
        </ul>
  </li>
  <li>
        <a href="#upgrading-to-256pe" id="markdown-toc-upgrading-to-256">Upgrading to 2.5.6PE</a>
        <ul>
             <li>
                 <a href="#ubuntucentos-256" id="markdown-toc-ubuntucentos-256">Ubuntu/CentOS</a>
             </li>
             <li>
                 <a href="#windows-256" id="markdown-toc-windows-256">Windows</a>
             </li>
        </ul>
  </li>
</ul>



## Prepare for upgrading SENTIENT (CentOS, Ubuntu)

**Stop SENTIENT**
Check if SENTIENT and database services are running 
Initially SENTIENT, check status to ensure it is stopped and then databases.  
```bash
sudo systemctl stop sentient
```
{: .copy-code}

```bash
sudo systemctl status sentient
```
{: .copy-code}

## Backup Database
Make a backup of the database before upgrading.  
#### PostgreSQL
Check PostgreSQL status. It is unnecessary to stop PostgreSQL for the backup.
```bash
sudo systemctl status postgresql
```
{: .copy-code}
***Make sure you have enough space to place a backup of the database***  
Check database size
```bash
sudo -u postgres psql -c "SELECT pg_size_pretty( pg_database_size('sentient') );"
```
{: .copy-code}

Check free space
```bash
df -h /
```
{: .copy-code}

If there is enough free space - make a backup.
```bash
sudo -Hiu postgres pg_dump sentient > sentient.sql.bak
```
{: .copy-code}
Check backup file being created.

#### Cassandra
Check Cassandra status. It is necessary to stop Cassandra for the backup.

```bash
sudo systemctl status cassandra
```
{: .copy-code}

Flush all memtables from the node to SSTables on disk.

```bash
nodetool drain
```
{: .copy-code}

Stop Cassandra.

```bash
sudo systemctl stop cassandra
```
{: .copy-code}

And you have to check the status again to ensure they are surely stopped.

```bash
sudo systemctl status cassandra
```
{: .copy-code}

***Make sure you have enough space to place a backup of the database***  
Check database size.
```bash
du -h /var/lib/cassandra/ | tail -1
```
{: .copy-code}

Check free space.
```bash
df -h /
```
{: .copy-code}

Make a backup of Cassandra database.
```bash
mkdir backup
sudo tar -cvf backup/cassandra.tar /var/lib/cassandra
```  
{: .copy-code}

***Check archive being created***

### Start Database
**Cassandra**  
```bash
sudo systemctl start cassandra
```
{: .copy-code}

**PostgreSQL**
Do nothing, postgresql is already running.  


## Upgrading to 2.4.1PE

These steps are applicable for 2.4.0PE SENTIENT Professional Edition version.

### Ubuntu/CentOS

#### SENTIENT Professional Edition package download

{% capture tabspec %}sentient-download-2-4-1
sentient-download-2-4-1-ubuntu,Ubuntu,shell,resources/2.4.1pe/sentient-ubuntu-download.sh,/docs/user-guide/install/resources/2.4.1pe/sentient-ubuntu-download.sh
sentient-download-2-4-1-centos,CentOS,shell,resources/2.4.1pe/sentient-centos-download.sh,/docs/user-guide/install/resources/2.4.1pe/sentient-centos-download.sh{% endcapture %}  
{% include tabs.html %}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-8-install-sentient-webreport-component).


{% capture tabspec %}sentient-installation-2-4-1
sentient-installation-2-4-1-ubuntu,Ubuntu,shell,resources/2.4.1pe/sentient-ubuntu-installation.sh,/docs/user-guide/install/resources/2.4.1pe/sentient-ubuntu-installation.sh
sentient-installation-2-4-1-centos,CentOS,shell,resources/2.4.1pe/sentient-centos-installation.sh,/docs/user-guide/install/resources/2.4.1pe/sentient-centos-installation.sh{% endcapture %}  
{% include tabs.html %}

**NOTE:** Package installer will ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.  
Please make sure that you set **database.entities.type** and **database.ts.type** parameters values (in the file **/etc/sentient/conf/sentient.yml**) to "cassandra" instead of "sql" in order to upgrade your cassandra database:
 
```
    database:
      entities:
        type: "${DATABASE_ENTITIES_TYPE:cassandra}" # cassandra OR sql
      ts:
        type: "${DATABASE_TS_TYPE:cassandra}" # cassandra OR sql (for hybrid mode, only this value should be cassandra)
```

Execute upgrade script
```bash
sudo /usr/share/sentient/bin/install/upgrade.sh --fromVersion=2.4.0 
```
{: .copy-code}

#### Start the service

```bash
sudo service sentient start
```
{: .copy-code}

### Windows

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-setup-2.4.1pe.exe](https://dist.docs.sentient.invenia.in/sentient-windows-setup-2.4.1pe.exe).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.
 
```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT Professional Edition configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Run installation package **sentient-windows-setup-2.4.1pe.exe**.
* Compare your old SENTIENT configuration files (from the backup you made in the first step) with new ones.
* Please make sure that you set **database.entities.type** and **database.ts.type** parameters values (in the file **\<SENTIENT install dir\>\conf\sentient.yml**) to "cassandra" instead of "sql" in order to upgrade your cassandra database:
  
  ```
  database:
    entities:
      type: "${DATABASE_ENTITIES_TYPE:cassandra}" # cassandra OR sql
    ts:
      type: "${DATABASE_TS_TYPE:cassandra}" # cassandra OR sql (for hybrid mode, only this value should be cassandra)
  ```       

* Run **upgrade.bat** script to upgrade SENTIENT to the new version.

**NOTE** Scripts listed above should be executed using Administrator Role.

```text
C:\sentient>upgrade.bat --fromVersion=2.4.0
```
{: .copy-code}

#### Start the service

```text
net start sentient
```
{: .copy-code}

## Upgrading to 2.4.2.1PE

These steps are applicable for 2.4.1PE and 2.4.2PE SENTIENT Professional Edition versions.

### Ubuntu/CentOS

#### SENTIENT Professional Edition package download

{% capture tabspec %}sentient-download-2-4-2
sentient-download-2-4-2-ubuntu,Ubuntu,shell,resources/2.4.2.1pe/sentient-ubuntu-download.sh,/docs/user-guide/install/resources/2.4.2.1pe/sentient-ubuntu-download.sh
sentient-download-2-4-2-centos,CentOS,shell,resources/2.4.2.1pe/sentient-centos-download.sh,/docs/user-guide/install/resources/2.4.2.1pe/sentient-centos-download.sh{% endcapture %}  
{% include tabs.html %}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-8-install-sentient-webreport-component).


{% capture tabspec %}sentient-installation-2-4-2
sentient-installation-2-4-2-ubuntu,Ubuntu,shell,resources/2.4.2.1pe/sentient-ubuntu-installation.sh,/docs/user-guide/install/resources/2.4.2.1pe/sentient-ubuntu-installation.sh
sentient-installation-2-4-2-centos,CentOS,shell,resources/2.4.2.1pe/sentient-centos-installation.sh,/docs/user-guide/install/resources/2.4.2.1pe/sentient-centos-installation.sh{% endcapture %}  
{% include tabs.html %}

**NOTE:** Package installer will ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.  
Please make sure that you set **database.entities.type** and **database.ts.type** parameters values (in the file **/etc/sentient/conf/sentient.yml**) to "cassandra" instead of "sql" in order to upgrade your cassandra database:
 
```
    database:
      entities:
        type: "${DATABASE_ENTITIES_TYPE:cassandra}" # cassandra OR sql
      ts:
        type: "${DATABASE_TS_TYPE:cassandra}" # cassandra OR sql (for hybrid mode, only this value should be cassandra)
```

Execute upgrade script:
```bash
sudo /usr/share/sentient/bin/install/upgrade.sh --fromVersion=2.4.1
```
{: .copy-code}

#### Start the service

```bash
sudo service sentient start
```
{: .copy-code}

### Windows

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-setup-2.4.2.1pe.exe](https://dist.docs.sentient.invenia.in/sentient-windows-setup-2.4.2.1pe.exe).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.
 
```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT Professional Edition configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Run installation package **sentient-windows-setup-2.4.2.1pe.exe**.
* Compare your old SENTIENT configuration files (from the backup you made in the first step) with new ones.
* Please make sure that you set **database.entities.type** and **database.ts.type** parameters values (in the file **\<SENTIENT install dir\>\conf\sentient.yml**) to "cassandra" instead of "sql" in order to upgrade your cassandra database:
  
```
      database:
        entities:
          type: "${DATABASE_ENTITIES_TYPE:cassandra}" # cassandra OR sql
        ts:
          type: "${DATABASE_TS_TYPE:cassandra}" # cassandra OR sql (for hybrid mode, only this value should be cassandra)
```

* Run **upgrade.bat** script to upgrade SENTIENT to the new version.

**NOTE** Scripts listed above should be executed using Administrator Role.

```text
C:\sentient>upgrade.bat --fromVersion=2.4.1
```
{: .copy-code}

#### Start the service

```text
net start sentient
```

## Upgrading to 2.4.3PE

These steps are applicable for 2.4.2PE and 2.4.2.1PE SENTIENT Professional Edition versions.

### Ubuntu/CentOS

#### SENTIENT Professional Edition package download

{% capture tabspec %}sentient-download-2-4-3
sentient-download-2-4-3-ubuntu,Ubuntu,shell,resources/2.4.3pe/sentient-ubuntu-download.sh,/docs/user-guide/install/resources/2.4.3pe/sentient-ubuntu-download.sh
sentient-download-2-4-3-centos,CentOS,shell,resources/2.4.3pe/sentient-centos-download.sh,/docs/user-guide/install/resources/2.4.3pe/sentient-centos-download.sh{% endcapture %}  
{% include tabs.html %}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-8-install-sentient-webreport-component).


{% capture tabspec %}sentient-installation-2-4-3
sentient-installation-2-4-3-ubuntu,Ubuntu,shell,resources/2.4.3pe/sentient-ubuntu-installation.sh,/docs/user-guide/install/resources/2.4.3pe/sentient-ubuntu-installation.sh
sentient-installation-2-4-3-centos,CentOS,shell,resources/2.4.3pe/sentient-centos-installation.sh,/docs/user-guide/install/resources/2.4.3pe/sentient-centos-installation.sh{% endcapture %}  
{% include tabs.html %}

**NOTE:** Package installer will ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.  
Please make sure that you set **database.entities.type** and **database.ts.type** parameters values (in the file **/etc/sentient/conf/sentient.yml**) to "cassandra" instead of "sql" in order to upgrade your cassandra database:
 
```
    database:
      entities:
        type: "${DATABASE_ENTITIES_TYPE:cassandra}" # cassandra OR sql
      ts:
        type: "${DATABASE_TS_TYPE:cassandra}" # cassandra OR sql (for hybrid mode, only this value should be cassandra)
```

Execute upgrade script:
```bash
sudo /usr/share/sentient/bin/install/upgrade.sh --fromVersion=2.4.2
```
{: .copy-code}

#### Start the service

```bash
sudo service sentient start
```
{: .copy-code}

### Windows

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-setup-2.4.3pe.exe](https://dist.docs.sentient.invenia.in/sentient-windows-setup-2.4.3pe.exe).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.
 
```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT Professional Edition configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Run installation package **sentient-windows-setup-2.4.3pe.exe**.
* Compare your old SENTIENT configuration files (from the backup you made in the first step) with new ones.
* Please make sure that you set **database.entities.type** and **database.ts.type** parameters values (in the file **\<SENTIENT install dir\>\conf\sentient.yml**) to "cassandra" instead of "sql" in order to upgrade your cassandra database:

```
      database:
        entities:
          type: "${DATABASE_ENTITIES_TYPE:cassandra}" # cassandra OR sql
        ts:
          type: "${DATABASE_TS_TYPE:cassandra}" # cassandra OR sql (for hybrid mode, only this value should be cassandra)
```       

* Run **upgrade.bat** script to upgrade SENTIENT to the new version.

**NOTE** Scripts listed above should be executed using Administrator Role.

```text
C:\sentient>upgrade.bat --fromVersion=2.4.2
```
{: .copy-code}

#### Start the service

```text
net start sentient
```
{: .copy-code}

## Upgrading to 2.5PE

These steps are applicable for 2.4.3PE SENTIENT Professional Edition version.

### Ubuntu/CentOS

#### SENTIENT Professional Edition package download

{% capture tabspec %}sentient-download-2-5
sentient-download-2-5-ubuntu,Ubuntu,shell,resources/2.5pe/sentient-ubuntu-download.sh,/docs/user-guide/install/resources/2.5pe/sentient-ubuntu-download.sh
sentient-download-2-5-centos,CentOS,shell,resources/2.5pe/sentient-centos-download.sh,/docs/user-guide/install/resources/2.5pe/sentient-centos-download.sh{% endcapture %}  
{% include tabs.html %}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-8-install-sentient-webreport-component).


{% capture tabspec %}sentient-installation-2-5
sentient-installation-2-5-ubuntu,Ubuntu,shell,resources/2.5pe/sentient-ubuntu-installation.sh,/docs/user-guide/install/resources/2.5pe/sentient-ubuntu-installation.sh
sentient-installation-2-5-centos,CentOS,shell,resources/2.5pe/sentient-centos-installation.sh,/docs/user-guide/install/resources/2.5pe/sentient-centos-installation.sh{% endcapture %}  
{% include tabs.html %}

**NOTE:** Upgrading SENTIENT Professional Edition from 2.4.3 to 2.5 version in case of using PostgreSQL database require to upgrade the PostgreSQL service to 11.x version.

Please refer to the guides below that will describe how to upgrade your PostgreSQL service on:

 - [Ubuntu](https://gist.github.com/ShvaykaD/1f0e6c1321a0a2b4b9f3b9ea9ab3e8d3)
 - [CentOS](https://gist.github.com/ShvaykaD/313745d31a9af6db3d6a01ec9f16aac8)
 
**NOTE:** Package installer will ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.  
Please make sure that you set **database.entities.type** and **database.ts.type** parameters values (in the file **/etc/sentient/conf/sentient.yml**) to "cassandra" instead of "sql" in order to upgrade your cassandra database:
 
```
    database:
      ts_max_intervals: "${DATABASE_TS_MAX_INTERVALS:700}" # Max number of DB queries generated by single API call to fetch telemetry records
      entities:
        type: "${DATABASE_ENTITIES_TYPE:sql}" # cassandra OR sql
      ts:
        type: "${DATABASE_TS_TYPE:sql}" # cassandra, sql, or timescale (for hybrid mode, DATABASE_TS_TYPE value should be cassandra, or timescale)

    # note: timescale works only with postgreSQL database for DATABASE_ENTITIES_TYPE.
```

**NOTE:** If you are using **PostgreSql(Sql)** for time-series data storage before executing the upgrade script, go to the PostgreSQL terminal(psql) and follow the instructions below: 

```bash
    # Connect to sentient database:
    \c sentient

    # Execute the next commands:

    # Update ts_kv table constraints:
    ALTER TABLE ts_kv DROP CONSTRAINT IF EXISTS ts_kv_unq_key;
    ALTER TABLE ts_kv DROP CONSTRAINT IF EXISTS ts_kv_pkey;
    ALTER TABLE ts_kv ADD CONSTRAINT ts_kv_pkey PRIMARY KEY (entity_type, entity_id, key, ts);

    # Update ts_kv_latest table constraints:
    ALTER TABLE ts_kv_latest DROP CONSTRAINT IF EXISTS ts_kv_latest_unq_key;
    ALTER TABLE ts_kv_latest DROP CONSTRAINT IF EXISTS ts_kv_latest_pkey;
    ALTER TABLE ts_kv_latest ADD CONSTRAINT ts_kv_latest_pkey PRIMARY KEY (entity_type, entity_id, key);

    # exit psql terminal 
    \q
```

Finally, execute upgrade script:
```bash
sudo /usr/share/sentient/bin/install/upgrade.sh --fromVersion=2.4.3
```
{: .copy-code}

#### Start the service

```bash
sudo service sentient start
```
{: .copy-code}

### Windows

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-setup-2.5pe.exe](https://dist.docs.sentient.invenia.in/sentient-windows-setup-2.5pe.exe).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.
 
```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT Professional Edition configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Run installation package **sentient-windows-setup-2.5pe.exe**.
* Compare your old SENTIENT configuration files (from the backup you made in the first step) with new ones.
* Please note that upgrading SENTIENT Professional Edition from 2.4.3 to 2.5 version in case of using PostgreSQL database require to upgrade the PostgreSQL service to 11.x version.
* Please make sure that you set **database.entities.type** and **database.ts.type** parameters values (in the file **\<SENTIENT install dir\>\conf\sentient.yml**) to "cassandra" instead of "sql" in order to upgrade your cassandra database:

```
    database:
      ts_max_intervals: "${DATABASE_TS_MAX_INTERVALS:700}" # Max number of DB queries generated by single API call to fetch telemetry records
      entities:
        type: "${DATABASE_ENTITIES_TYPE:sql}" # cassandra OR sql
      ts:
        type: "${DATABASE_TS_TYPE:sql}" # cassandra, sql, or timescale (for hybrid mode, DATABASE_TS_TYPE value should be cassandra, or timescale)

    # note: timescale works only with postgreSQL database for DATABASE_ENTITIES_TYPE.
```

**NOTE:** If you are using **PostgreSql(Sql)** for time-series data storage before executing the upgrade script, you need to access the psql terminal. Once you will be logged to the psql terminal, please follow the instructions below:

```bash
    # Connect to sentient database:
    \c sentient

    # Execute the next commands:

    # Update ts_kv table constraints:
    ALTER TABLE ts_kv DROP CONSTRAINT IF EXISTS ts_kv_unq_key;
    ALTER TABLE ts_kv DROP CONSTRAINT IF EXISTS ts_kv_pkey;
    ALTER TABLE ts_kv ADD CONSTRAINT ts_kv_pkey PRIMARY KEY (entity_type, entity_id, key, ts);

    # Update ts_kv_latest table constraints:
    ALTER TABLE ts_kv_latest DROP CONSTRAINT IF EXISTS ts_kv_latest_unq_key;
    ALTER TABLE ts_kv_latest DROP CONSTRAINT IF EXISTS ts_kv_latest_pkey;
    ALTER TABLE ts_kv_latest ADD CONSTRAINT ts_kv_latest_pkey PRIMARY KEY (entity_type, entity_id, key);

    # exit psql terminal 
    \q
```
{: .copy-code}

* Finally, run **upgrade.bat** script to upgrade SENTIENT to the new version.

**NOTE** Scripts listed above should be executed using Administrator Role.

```text
C:\sentient>upgrade.bat --fromVersion=2.4.3
```
{: .copy-code}

#### Start the service

```text
net start sentient
```
{: .copy-code}

## Upgrading to 2.5.1PE

These steps are applicable for 2.4.3PE SENTIENT Professional Edition version.

### Ubuntu/CentOS {#ubuntucentos-251}

#### SENTIENT Professional Edition package download

{% capture tabspec %}sentient-download-2-5
sentient-download-2-5-1-ubuntu,Ubuntu,shell,resources/2.5.1pe/sentient-ubuntu-download.sh,/docs/user-guide/install/resources/2.5.1pe/sentient-ubuntu-download.sh
sentient-download-2-5-1-centos,CentOS,shell,resources/2.5.1pe/sentient-centos-download.sh,/docs/user-guide/install/resources/2.5.1pe/sentient-centos-download.sh{% endcapture %}  
{% include tabs.html %}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-8-install-sentient-webreport-component).


{% capture tabspec %}sentient-installation-2-5-1
sentient-installation-2-5-1-ubuntu,Ubuntu,shell,resources/2.5.1pe/sentient-ubuntu-installation.sh,/docs/user-guide/install/resources/2.5.1pe/sentient-ubuntu-installation.sh
sentient-installation-2-5-1-centos,CentOS,shell,resources/2.5.1pe/sentient-centos-installation.sh,/docs/user-guide/install/resources/2.5.1pe/sentient-centos-installation.sh{% endcapture %}  
{% include tabs.html %}

**NOTE:** Upgrading SENTIENT Professional Edition from 2.4.3 to 2.5.1 version in case of using PostgreSQL database require to upgrade the PostgreSQL service to 11.x version.

Please refer to the guides below that will describe how to upgrade your PostgreSQL service on:

- [Ubuntu](https://gist.github.com/ShvaykaD/1f0e6c1321a0a2b4b9f3b9ea9ab3e8d3)
- [CentOS](https://gist.github.com/ShvaykaD/313745d31a9af6db3d6a01ec9f16aac8)

**NOTE:** Package installer will ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.

Finally, execute upgrade script:
```bash
sudo /usr/share/sentient/bin/install/upgrade.sh --fromVersion=2.4.3
```
{: .copy-code}

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```bash
sudo service sentient start
```
{: .copy-code}

### Windows {#windows-251}

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-setup-2.5.1pe.exe](https://dist.docs.sentient.invenia.in/sentient-windows-setup-2.5.1pe.exe).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT Professional Edition configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Run installation package **sentient-windows-setup-2.5.1pe.exe**.
* Compare your old SENTIENT configuration files (from the backup you made in the first step) with new ones.
* Please note that upgrading SENTIENT Professional Edition from 2.4.3 to 2.5.1 version in case of using PostgreSQL database require to upgrade the PostgreSQL service to 11.x version.

* Finally, run **upgrade.bat** script to upgrade SENTIENT to the new version.

**NOTE** Scripts listed above should be executed using Administrator Role.

```text
C:\sentient>upgrade.bat --fromVersion=2.4.3
```
{: .copy-code}

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```text
net start sentient
```
{: .copy-code}

## Upgrading to 2.5.2PE

### Ubuntu/CentOS {#ubuntucentos-252}

**NOTE**: These upgrade steps are applicable for SENTIENT version 2.5.1PE. In order to upgrade to 2.5.2PE you need to [**upgrade to 2.5.1PE first**](/docs/user-guide/install/pe/upgrade-instructions/#ubuntucentos-251).

#### SENTIENT Professional Edition package download

{% capture tabspec %}sentient-download-2-5-2
sentient-download-2-5-2-ubuntu,Ubuntu,shell,resources/2.5.2pe/sentient-ubuntu-download.sh,/docs/user-guide/install/resources/2.5.2pe/sentient-ubuntu-download.sh
sentient-download-2-5-2-centos,CentOS,shell,resources/2.5.2pe/sentient-centos-download.sh,/docs/user-guide/install/resources/2.5.2pe/sentient-centos-download.sh{% endcapture %}  
{% include tabs.html %}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-8-install-sentient-webreport-component).


{% capture tabspec %}sentient-installation-2-5-2
sentient-installation-2-5-2-ubuntu,Ubuntu,shell,resources/2.5.2pe/sentient-ubuntu-installation.sh,/docs/user-guide/install/resources/2.5.2pe/sentient-ubuntu-installation.sh
sentient-installation-2-5-2-centos,CentOS,shell,resources/2.5.2pe/sentient-centos-installation.sh,/docs/user-guide/install/resources/2.5.2pe/sentient-centos-installation.sh{% endcapture %}  
{% include tabs.html %}

**NOTE:** Upgrading SENTIENT to 2.5.2 version in case of using PostgreSQL database require to upgrade the PostgreSQL service to 11.x version.

Please refer to the guides below that will describe how to upgrade your PostgreSQL service on:

- [Ubuntu](https://gist.github.com/ShvaykaD/1f0e6c1321a0a2b4b9f3b9ea9ab3e8d3)
- [CentOS](https://gist.github.com/ShvaykaD/313745d31a9af6db3d6a01ec9f16aac8)

**NOTE:** Package installer will ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```bash
sudo service sentient start
```
{: .copy-code}

### Windows {#windows-252}

**NOTE**: These upgrade steps are applicable for SENTIENT version 2.5.1PE. In order to upgrade to 2.5.2PE you need to [**upgrade to 2.5.1PE first**](/docs/user-guide/install/pe/upgrade-instructions/#windows-251).

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-setup-2.5.2pe.exe](https://dist.docs.sentient.invenia.in/sentient-windows-setup-2.5.2pe.exe).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT Professional Edition configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Run installation package **sentient-windows-setup-2.5.2pe.exe**.
* Compare your old SENTIENT configuration files (from the backup you made in the first step) with new ones.
* Please note that upgrading SENTIENT Professional Edition from 2.4.3 to 2.5.1 version in case of using PostgreSQL database require to upgrade the PostgreSQL service to 11.x version.

* Finally, run **upgrade.bat** script to upgrade SENTIENT to the new version.

**NOTE** Scripts listed above should be executed using Administrator Role.

```text
C:\sentient>upgrade.bat --fromVersion=2.4.3
```
{: .copy-code}

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```text
net start sentient
```
{: .copy-code}

## Upgrading to 2.5.3PE

### Ubuntu/CentOS {#ubuntucentos-253}

**NOTE**: These upgrade steps are applicable for SENTIENT version 2.5.2PE. In order to upgrade to 2.5.3PE you need to [**upgrade to 2.5.2PE first**](/docs/user-guide/install/pe/upgrade-instructions/#ubuntucentos-252).

#### SENTIENT Professional Edition package download

{% capture tabspec %}sentient-download-2-5-3
sentient-download-2-5-3-ubuntu,Ubuntu,shell,resources/2.5.3pe/sentient-ubuntu-download.sh,/docs/user-guide/install/resources/2.5.3pe/sentient-ubuntu-download.sh
sentient-download-2-5-3-centos,CentOS,shell,resources/2.5.3pe/sentient-centos-download.sh,/docs/user-guide/install/resources/2.5.3pe/sentient-centos-download.sh{% endcapture %}  
{% include tabs.html %}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-8-install-sentient-webreport-component).


{% capture tabspec %}sentient-installation-2-5-3
sentient-installation-2-5-3-ubuntu,Ubuntu,shell,resources/2.5.3pe/sentient-ubuntu-installation.sh,/docs/user-guide/install/resources/2.5.3pe/sentient-ubuntu-installation.sh
sentient-installation-2-5-3-centos,CentOS,shell,resources/2.5.3pe/sentient-centos-installation.sh,/docs/user-guide/install/resources/2.5.3pe/sentient-centos-installation.sh{% endcapture %}  
{% include tabs.html %}

**NOTE:** Package installer will ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```bash
sudo service sentient start
```
{: .copy-code}

### Windows {#windows-253}

**NOTE**: These upgrade steps are applicable for SENTIENT version 2.5.2PE. In order to upgrade to 2.5.3PE you need to [**upgrade to 2.5.2PE first**](/docs/user-guide/install/pe/upgrade-instructions/#windows-252).

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-setup-2.5.3pe.exe](https://dist.docs.sentient.invenia.in/sentient-windows-setup-2.5.3pe.exe).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT Professional Edition configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Run installation package **sentient-windows-setup-2.5.3pe.exe**.
* Compare your old SENTIENT configuration files (from the backup you made in the first step) with new ones.

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```text
net start sentient
```
{: .copy-code}

## Upgrading to 2.5.4PE

### Ubuntu/CentOS {#ubuntucentos-254}

**NOTE**: These upgrade steps are applicable for SENTIENT version 2.5.3PE. In order to upgrade to 2.5.4PE you need to [**upgrade to 2.5.3PE first**](/docs/user-guide/install/pe/upgrade-instructions/#ubuntucentos-253).

#### SENTIENT Professional Edition package download

{% capture tabspec %}sentient-download-2-5-4
sentient-download-2-5-4-ubuntu,Ubuntu,shell,resources/2.5.4pe/sentient-ubuntu-download.sh,/docs/user-guide/install/resources/2.5.4pe/sentient-ubuntu-download.sh
sentient-download-2-5-4-centos,CentOS,shell,resources/2.5.4pe/sentient-centos-download.sh,/docs/user-guide/install/resources/2.5.4pe/sentient-centos-download.sh{% endcapture %}  
{% include tabs.html %}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-9-install-sentient-webreport-component).


{% capture tabspec %}sentient-installation-2-5-4
sentient-installation-2-5-4-ubuntu,Ubuntu,shell,resources/2.5.4pe/sentient-ubuntu-installation.sh,/docs/user-guide/install/resources/2.5.4pe/sentient-ubuntu-installation.sh
sentient-installation-2-5-4-centos,CentOS,shell,resources/2.5.4pe/sentient-centos-installation.sh,/docs/user-guide/install/resources/2.5.4pe/sentient-centos-installation.sh{% endcapture %}  
{% include tabs.html %}

**NOTE:** Package installer will ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```bash
sudo service sentient start
```
{: .copy-code}

### Windows {#windows-254}

**NOTE**: These upgrade steps are applicable for SENTIENT version 2.5.3PE. In order to upgrade to 2.5.4PE you need to [**upgrade to 2.5.3PE first**](/docs/user-guide/install/pe/upgrade-instructions/#windows-253).

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-setup-2.5.4pe.exe](https://dist.docs.sentient.invenia.in/sentient-windows-setup-2.5.4pe.exe).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT Professional Edition configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Run installation package **sentient-windows-setup-2.5.4pe.exe**.
* Compare your old SENTIENT configuration files (from the backup you made in the first step) with new ones.

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```text
net start sentient
```
{: .copy-code}

## Upgrading to 2.5.5PE

### Ubuntu/CentOS {#ubuntucentos-255}

**NOTE**: These upgrade steps are applicable for SENTIENT version 2.5.4PE. In order to upgrade to 2.5.5PE you need to [**upgrade to 2.5.4PE first**](/docs/user-guide/install/pe/upgrade-instructions/#ubuntucentos-254).

#### SENTIENT Professional Edition package download

{% capture tabspec %}sentient-download-2-5-5
sentient-download-2-5-5-ubuntu,Ubuntu,shell,resources/2.5.5pe/sentient-ubuntu-download.sh,/docs/user-guide/install/resources/2.5.5pe/sentient-ubuntu-download.sh
sentient-download-2-5-5-centos,CentOS,shell,resources/2.5.5pe/sentient-centos-download.sh,/docs/user-guide/install/resources/2.5.5pe/sentient-centos-download.sh{% endcapture %}  
{% include tabs.html %}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-9-install-sentient-webreport-component).


{% capture tabspec %}sentient-installation-2-5-5
sentient-installation-2-5-5-ubuntu,Ubuntu,shell,resources/2.5.5pe/sentient-ubuntu-installation.sh,/docs/user-guide/install/resources/2.5.5pe/sentient-ubuntu-installation.sh
sentient-installation-2-5-5-centos,CentOS,shell,resources/2.5.5pe/sentient-centos-installation.sh,/docs/user-guide/install/resources/2.5.5pe/sentient-centos-installation.sh{% endcapture %}  
{% include tabs.html %}

**NOTE:** Package installer will ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```bash
sudo service sentient start
```
{: .copy-code}

### Windows {#windows-255}

**NOTE**: These upgrade steps are applicable for SENTIENT version 2.5.4PE. In order to upgrade to 2.5.5PE you need to [**upgrade to 2.5.4PE first**](/docs/user-guide/install/pe/upgrade-instructions/#windows-254).

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-setup-2.5.5pe.exe](https://dist.docs.sentient.invenia.in/sentient-windows-setup-2.5.5pe.exe).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT Professional Edition configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Run installation package **sentient-windows-setup-2.5.5pe.exe**.
* Compare your old SENTIENT configuration files (from the backup you made in the first step) with new ones.

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```text
net start sentient
```
{: .copy-code}

## Upgrading to 2.5.6PE

### Ubuntu/CentOS {#ubuntucentos-256}

**NOTE**: These upgrade steps are applicable for SENTIENT version 2.5.5PE. In order to upgrade to 2.5.6PE you need to [**upgrade to 2.5.5PE first**](/docs/user-guide/install/pe/upgrade-instructions/#ubuntucentos-255).

#### SENTIENT Professional Edition package download

{% capture tabspec %}sentient-download-2-5-6
sentient-download-2-5-6-ubuntu,Ubuntu,shell,resources/2.5.6pe/sentient-ubuntu-download.sh,/docs/user-guide/install/resources/2.5.6pe/sentient-ubuntu-download.sh
sentient-download-2-5-6-centos,CentOS,shell,resources/2.5.6pe/sentient-centos-download.sh,/docs/user-guide/install/resources/2.5.6pe/sentient-centos-download.sh{% endcapture %}  
{% include tabs.html %}

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```bash
sudo service sentient stop
```
{: .copy-code}

* Install Sentient Web Report component as described [here](/docs/user-guide/install/pe/ubuntu/#step-9-install-sentient-webreport-component).


{% capture tabspec %}sentient-installation-2-5-6
sentient-installation-2-5-6-ubuntu,Ubuntu,shell,resources/2.5.6pe/sentient-ubuntu-installation.sh,/docs/user-guide/install/resources/2.5.6pe/sentient-ubuntu-installation.sh
sentient-installation-2-5-6-centos,CentOS,shell,resources/2.5.6pe/sentient-centos-installation.sh,/docs/user-guide/install/resources/2.5.6pe/sentient-centos-installation.sh{% endcapture %}  
{% include tabs.html %}

**NOTE:** Package installer will ask you to merge your sentient configuration. It is preferred to use **merge option** to make sure that all your previous parameters will not be overwritten.

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```bash
sudo service sentient start
```
{: .copy-code}

### Windows {#windows-256}

**NOTE**: These upgrade steps are applicable for SENTIENT version 2.5.5PE. In order to upgrade to 2.5.6PE you need to [**upgrade to 2.5.5PE first**](/docs/user-guide/install/pe/upgrade-instructions/#windows-255).

#### SENTIENT Professional Edition package download

Download SENTIENT Professional Edition installation package for Windows: [sentient-windows-setup-2.5.6pe.exe](https://dist.docs.sentient.invenia.in/sentient-windows-setup-2.5.6pe.exe).

#### SENTIENT Professional Edition service upgrade

* Stop SENTIENT service if it is running.

```text
net stop sentient
```
{: .copy-code}

* Make a backup of previous SENTIENT Professional Edition configuration located in \<SENTIENT install dir\>\conf (for ex. C:\sentient\conf).
* Run installation package **sentient-windows-setup-2.5.6pe.exe**.
* Compare your old SENTIENT configuration files (from the backup you made in the first step) with new ones.

#### Start the service

{% include templates/redis-post-upgrade-notice.md %}

```text
net start sentient
```
{: .copy-code}

## Next steps

{% assign currentGuide = "InstallationGuides" %}{% include templates/guides-banner.md %}
