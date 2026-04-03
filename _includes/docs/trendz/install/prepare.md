### Prepare for upgrading SENTIENT ANALYTICS

**Stop SENTIENT ANALYTICS**
Check if SENTIENT ANALYTICS and database services are stopped.
```bash
sudo systemctl stop sentient-analytics
```
{: .copy-code}

```bash
sudo systemctl status sentient-analytics
```
{: .copy-code}

#### Backup Database
Make a backup of the database before upgrading.

Check PostgreSQL status. It is unnecessary to stop PostgreSQL for the backup.
```bash
sudo systemctl status postgresql
```
{: .copy-code}

***Make sure you have enough space to place a backup of the database***

Check database size
```bash
sudo -u postgres psql -c "SELECT pg_size_pretty( pg_database_size('sentient-analytics') );"
```
{: .copy-code}
Check free space

```bash
df -h /
```
{: .copy-code}

If there is enough free space - make a backup.
```bash
sudo -Hiu postgres pg_dump sentient-analytics > sentient-analytics.sql.bak
```
{: .copy-code}

Check backup file being created.