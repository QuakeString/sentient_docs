Set the terminal in the directory which contains the `docker-compose.yml` file and execute the following commands to up this docker compose directly:

```
docker compose --profile sentient-analytics up -d && docker compose logs -f sentient-analytics
```
{: .copy-code}

After executing this command you can open `http://{your-host-ip}:8888` in your browser (for ex. `http://localhost:8888`).
You should see SENTIENT ANALYTICS login page.
