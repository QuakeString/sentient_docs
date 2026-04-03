If something goes wrong, you can stream the SENTIENT container logs in real time:

```bash
docker compose logs -f sentient-pe
```
{: .copy-code}

Bring down every container defined in your Compose file:

```bash
docker compose down
```
{: .copy-code}

Launch all services in detached mode:

```bash
docker compose up -d
```
{: .copy-code}
