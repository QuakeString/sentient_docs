#### Docker installation

Install Docker for [CentOS/RHEL](https://docs.docker.com/engine/install/centos/)

{% include templates/install/docker-install-note.md %}

{% include templates/install/queue-kafka-in-docker.md %}

##### SENTIENT Configuration

Edit SENTIENT configuration file

```text
sudo nano /etc/sentient/conf/sentient.conf
```
{: .copy-code}

Add the following line to the configuration file. **Don't forget** to replace "localhost:9092" with your real Kafka bootstrap servers:

```bash
export TB_QUEUE_TYPE=kafka
export TB_KAFKA_SERVERS=localhost:9092
```
{: .copy-code}