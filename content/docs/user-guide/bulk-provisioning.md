+++
title = "Bulk provisioning"
description = "Add many devices at once in SENTIENT 4.3.0.57: the state of CSV import, and the ways that work today."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
**Bulk provisioning** means adding many devices or assets at once, for example the 200 meters of a new building, instead of one by one.

> **Note for 4.3.0.57:** CSV import does not work yet. **Import device** under **Entities > Devices** does not read the rows of your file, and **Import assets** fails. Do not use them in 4.3.0.57: the device import can add test devices named `csv-device-1` to `csv-device-5`; delete them if you see them. A later version will add CSV import. Use one of the ways below meanwhile.

## Ways that work

| Way | Best for |
|---|---|
| **Through the gateway** | PLCs, Modbus and OPC UA equipment. The [SENTIENT Gateway](/docs/iot-gateway/) creates a device in SENTIENT for each device in its connector settings the first time it sends data. Nothing to add by hand |
| **Device provisioning** | Devices with their own MQTT, HTTP or CoAP client. Each device adds itself on first start with the profile's key and secret. See [Device profiles](/docs/user-guide/device-profiles/#device-provisioning) |
| **REST API script** | A list in a spreadsheet. A short script reads it and calls the API for each row, below |

## Add devices from a list with the REST API

Save the list as `devices.csv` with the columns `name,profile,label`, then run this script with Python 3 on any PC that reaches SENTIENT. It signs in as a tenant administrator, creates each device and prints its access token.

```python
import csv, getpass, requests

URL = "http://sentient.example.com:8080"
user = input("Tenant administrator email: ")
token = requests.post(f"{URL}/api/auth/login",
                      json={"username": user, "password": getpass.getpass()}).json()["token"]
h = {"X-Authorization": f"Bearer {token}"}

profiles = {p["name"]: p["id"] for p in requests.get(
    f"{URL}/api/deviceProfiles?pageSize=1000&page=0", headers=h).json()["data"]}

with open("devices.csv", newline="") as f:
    for row in csv.DictReader(f):
        d = requests.post(f"{URL}/api/device", headers=h, json={
            "name": row["name"], "label": row["label"],
            "deviceProfileId": profiles[row["profile"]]}).json()
        cred = requests.get(f"{URL}/api/device/{d['id']['id']}/credentials", headers=h).json()
        print(row["name"], cred["credentialsId"])
```

A device whose name already exists is refused; the script then stops with an error for that row.

## Related

- [Devices](/docs/user-guide/ui/devices/)
- [Device profiles](/docs/user-guide/device-profiles/)
