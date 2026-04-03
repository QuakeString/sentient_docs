Edit SENTIENT configuration file 

```bash 
sudo nano /etc/sentient/conf/sentient.conf
``` 
{: .copy-code}

Add the following lines to the configuration file. 

```bash
# Update SENTIENT memory usage and restrict it to 2G in /etc/sentient/conf/sentient.conf
export JAVA_OPTS="$JAVA_OPTS -Xms2G -Xmx2G"
```
{: .copy-code}

We recommend adjusting these parameters depending on your server resources. It should be set to at least 2G (gigabytes), and increased accordingly if there is additional RAM space available. Usually, you need to set it to 1/2 of your total RAM if you do not run any other memory-intensive processes (e.g. Cassandra), or to 1/3 otherwise.