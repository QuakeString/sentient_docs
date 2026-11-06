+++
title = "IoT Gateway installation from sources."

[extra]
status = "imported"
checked = ""
source = "docs/iot-gateway/install/source-installation.md"
+++
## Installation from sources

To install SENTIENT IoT Gateway from sources, you should follow steps below:    
  
**1.** Install required libraries to the system with apt:
```bash
sudo apt install python3-dev python3-pip python3-venv libglib2.0-dev git
```


**2.** Download repository from GitHub:
```bash
git clone --recurse-submodules https://github.com/sentient/sentient-gateway.git --depth 1
```


**3.** Move into downloaded directory:
```bash
cd sentient-gateway
```


**4.** Create and activate virtual environment:
```bash
python3 -m venv venv && source venv/bin/activate
```


**5.** Install python requirements:
```bash
pip install -r requirements.txt
```


**6.** Install the library:
```bash
python setup.py install
```


**7.** Create "logs" folder:
```bash
mkdir logs
```


**8.** Configure the gateway to work with your instance of the SENTIENT platform: change the "host" and "accessToken" to your values in a *tb_gateway.json* configuration file.
You can find a description of this file in the [IoT Gateway Configuration](/docs/iot-gateway/configuration/#general-configuration-file) guide.

The tb_gateway.json file is located in the config folder:

```bash
sentient-gateway/sentient_gateway/config
```

**9.** Run gateway, to check installation result:
```bash
python3 ./sentient_gateway/tb_gateway.py
```


## Build local docker image

In order to build local docker image, follow the next steps:

**1.** Copy **Dockerfile** to **root** folder, using the following command:

```bash
cp docker/Dockerfile .
```


**2.** From project root folder execute the following command:

```bash
docker build -t local-gateway . 
```


## Hot Reloader

If you are using Gateway for development, you can enable Hot Reloader to restart Gateway every time when you edit any project file.

To run Gateway with Hot Reloader, use the following command:
```bash
python3 ./sentient_gateway/tb_gateway.py true
```
