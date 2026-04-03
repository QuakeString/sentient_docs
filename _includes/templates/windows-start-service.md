Now let's start the SENTIENT service!
Open the command prompt as an Administrator and execute the following command:

```shell
net start sentient
```
{: .copy-code}

Expected output:

```text
The SENTIENT Server Application service is starting.
The SENTIENT Server Application service was started successfully.
```

In order to restart the SENTIENT service you can execute following commands:

```shell
net stop sentient
net start sentient
```
{: .copy-code}

Once started, you will be able to open Web UI using the following link:

```bash
http://localhost:8080/
```
{: .copy-code}

The following default credentials are available if you have specified *--loadDemo* during execution of the installation script:

- **System Administrator**: sysadmin@sentient.org / sysadmin
- **Tenant Administrator**: tenant@sentient.org / tenant
- **Customer User**: customer@sentient.org / customer

You can always change passwords for each account in account profile page.