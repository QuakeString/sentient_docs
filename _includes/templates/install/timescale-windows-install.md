Please refer to the official [TimescaleDB installation page](https://docs.timescale.com/self-hosted/latest/install/installation-windows/) on Windows and follow the instructions in accordance with your installed PostgreSQL version.

After package installation, you need to create TimescaleDB extension in your SENTIENT database:
1. Run PSQL console: Start Menu → PostgreSQL → SQL Shell (psql);
2. Login to your "sentient" database;
3. Run the command:
```bash 
CREATE EXTENSION IF NOT EXISTS timescaledb;
```
{: .copy-code}