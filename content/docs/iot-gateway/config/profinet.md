+++
title = "PROFINET connector"
description = "Run SENTIENT Gateway as a PROFINET IO controller: find and name stations, import their GSDML, read inputs and, when allowed, drive outputs."
weight = 246

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
With the **PROFINET** connector, the gateway itself is the **PROFINET IO controller** (RT class 1) for its devices. It finds and names stations by DCP, connects them with the modules from their GSDML file, exchanges their cyclic IO, and sends their values, alarms and diagnoses to SENTIENT. No PLC or vendor tool is needed.

> **Status.** The controller has been tested against software IO devices and matches TIA Portal's frames for the same device. It has not yet run against field hardware. Try it on a test bench first, never on a running production line.

## What the gateway needs

PROFINET is raw Ethernet, so the gateway must run on **Linux** with raw network access:

- In Docker: `network_mode: host` and `cap_add: [NET_RAW]`. The connection's RPCs also use UDP port **34964**.
- A network port **dedicated to the PROFINET segment** is best, with an address in the devices' subnet. The gateway names and addresses devices on it.
- For steady cycle timing, add `cap_add: [SYS_NICE]` and set **Real-time priority**. Without them, the timing is best effort.

See [Install on Linux and Docker](/docs/iot-gateway/install-linux/#which-connectors-need-what).

## Set up the controller

In SENTIENT, open the gateway, then **Connectors**, and add a **PROFINET** connector. In its **General** tab, under **IO controller**:

| Setting | Value |
|---|---|
| **Interface** | The network interface facing the devices, for example `eth1` |
| **Controller name of station** | The gateway's own PROFINET name |
| **Real-time priority** | Optional, see above |
| **Commissioning** | **Allow the platform to name stations, set their addresses and reset them**. Off by default |

## Add a device

1. Under **PROFINET devices**, add a device. Click **Find on network** to scan the interface and pick the station: its name, address and identity fill the form.
2. Check **On the network**: **Name of station** (lower-case letters, digits, `-` and `.`), **IP address**, **Subnet mask**, **Default gateway**. Tick **Assign this address to the device** to have the gateway set the address when it connects.
3. Check **Identity and cycle**: **Vendor ID**, **Device ID**, **Cycle**, **Data hold factor** (how many missed cycles end the connection) and **Publish every** (how often values go to SENTIENT). **Read I&M0 when the device comes online** reads the device's name plate.
4. Under **Modules**, click **Import GSDML** and choose the device's GSDML file. Pick the **Device access point** and the module in each **Slot** and **Subslot**, keep **Add keys for the modules' inputs and outputs** ticked, and click **Apply**. The import replaces the device's modules.
5. Save the connector.

## Keys

Each key reads a value from a submodule's IO data. **Place** names the **Slot**, **Subslot** and **Offset** in octets, **Type** the data type, **Bit** a single bit, and **Length** the size of a string or bytes value. **Frame** is **Input (from the device)** or **Output (read back)**.

**Quality** publishes the PROFINET status of the value **As an attribute** or **As telemetry**, or not at all. **Leave the value out while it is not GOOD** drops values the device marks as bad.

The gateway also sends, for each device, its alarms (telemetry `alarm`), its active diagnoses (attributes `diagnoses` and `diagnosisCount`, named from the GSDML) and its ports with their LLDP neighbours (`ports`).

## Outputs

Under **Outputs and records**, **Drive outputs** is **off** by default. While it is off, the outputs are sent as BAD, so the device keeps its substitute values (normally off), and writes to outputs are refused.

> **Turn on Drive outputs only for a device you are allowed to control.** The gateway then drives its outputs every cycle, from attribute updates and RPCs, and whatever they are wired to will move. If the link to SENTIENT is lost, the outputs go BAD again.

RPC methods use **Write an output** or **Read a value**. **Allow record writes by RPC** lets the gateway's own `writeRecord` method change device records. `readRecord`, `writeRecord`, `readIm0` and `status` are reserved for the gateway, so your methods cannot use these names.

## Commissioning stations

**Scan the network** lists every station that answers on the connector's interface, with its MAC, name, type and address. Pick one to:

- **Flash LED**, to find it in the cabinet.
- **Assign name** or **Assign address**.
- **Reset to factory settings**: the station forgets its name and address.

Names, addresses and resets are sent only while **Commissioning** is allowed in the **General** tab. A station that is already connected to a controller refuses them.

## When something is wrong

| What you see | What to do |
|---|---|
| **The gateway did not answer** when scanning | The gateway is not connected, or is older than 4.9.0 |
| **No station answered** | Wrong **Interface**, or the gateway lacks raw network access (`NET_RAW`, host network) |
| The device does not connect | The **Name of station** does not match the device's, or the modules do not match its hardware. Import the GSDML again |
| Writes to outputs are refused | **Drive outputs** is off |
| Values come and go | The cycle is too short for the machine. Raise **Cycle** or **Data hold factor**, or set **Real-time priority** |

## Related

- [Write values to devices](/docs/iot-gateway/rpc-write/)
- [EtherCAT connector](/docs/iot-gateway/config/ethercat/)
