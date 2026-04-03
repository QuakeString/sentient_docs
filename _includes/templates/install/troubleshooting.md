SENTIENT logs are stored in the following directory:
 
```bash
/var/log/sentient
```
{: .copy-code}

You can issue the following command in order to check if there are any errors on the backend side:
 
```bash
cat /var/log/sentient/sentient.log | grep ERROR
```
{: .copy-code}