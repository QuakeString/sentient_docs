You can detach from session terminal using `Ctrl-p` `Ctrl-q` key sequence - the container will keep running in the background.

In case of any issues, you can examine service logs for errors.
For example, to see SENTIENT ANALYTICS container logs, execute the following command:

```
docker compose logs -f sentient-analytics
```
{: .copy-code}

To stop the container:

```
docker compose stop sentient-analytics
```
{: .copy-code}

To start the container:

```
docker compose start sentient-analytics
```
{: .copy-code}
