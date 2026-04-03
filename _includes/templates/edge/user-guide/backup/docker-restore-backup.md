Stop the **SENTIENT GATEWAY** container (if it's still running):

```bash
docker compose stop
```
{: .copy-code}

To restore data from a backup volume to the main volume, run the following command:

```bash
docker run --rm -v tb-edge-postgres-data-backup:/source -v tb-edge-postgres-data:/target busybox sh -c "cp -a /source/. /target"
 ```
{: .copy-code}

Start the **SENTIENT GATEWAY** container:

```bash
docker compose up -d 
```
{: .copy-code}
