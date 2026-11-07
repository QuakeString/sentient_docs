+++
title = "EtherNet/IP connector"
description = "Read and write Allen-Bradley ControlLogix, CompactLogix, Micro800, SLC 500 and MicroLogix controllers with SENTIENT Gateway over EtherNet/IP."
weight = 235

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
The **EtherNet/IP** connector reads and writes Rockwell Automation (Allen-Bradley) controllers over EtherNet/IP (TCP port **44818**). Logix controllers are read by tag name, SLC 500 and MicroLogix by data-file address. No Rockwell software is needed on the gateway machine.

| PLC Type | Addressed by |
|---|---|
| **ControlLogix**, **CompactLogix** | Tag name (CIP) |
| **Micro800** (Micro820, 850, 870) | Tag name, one tag per request |
| **SLC500**, **MicroLogix** | Data-file address (PCCC) |

> Micro800 support has not yet been tried on real hardware. On a first Micro800 site, compare a few tags with the controller's own display before you rely on them.

## Add a controller

1. In SENTIENT, open the gateway, then **Connectors**, and add an **EtherNet/IP** connector.
2. Under **EtherNet/IP Devices**, click **+**. Or click the search button (**Discover EtherNet/IP devices on network**): the gateway lists the controllers that answer, with their **IP Address** and **Product Name**. Click **Add** next to one.
3. Fill in:

   | Setting | Value |
   |---|---|
   | **Device Name**, **Device profile** | The device in SENTIENT |
   | **Host** | The controller's IP address. For a ControlLogix, the address of the Ethernet module in the chassis |
   | **Slot** | The slot of the processor in the chassis (ControlLogix). `0` for a CompactLogix |
   | **PLC Type** | One of the types above |
   | **Upload tag list from PLC on connect** | Reads the controller's tag list when it connects. Needed only to read user-defined types (UDTs) member by member, and for **Browse Tags** |
   | **Poll Period (ms)**, **Connect Attempts**, **Wait After Failed (ms)** | How often to read, and how to retry |

4. Add keys, click **Apply**, and save the connector.

**PLC Information** shows the controller's identity and, for a chassis, the **Backplane Module Info**.

## Keys

Each key has a **Tag** (the key's name in SENTIENT) and a **PLC Tag**.

**Logix and Micro800**: the controller's tag name, for example `MotorSpeed`, a program tag `Program:MainProgram.Temperature`, an array element `Tags[3]`, or a member `Tags[3].Member`. **Browse Tags** lists the controller's tags with their type, **Access** and **Dimensions**; tick tags and add them as time series or attributes. **Auto-discover Tags** does the same in one step.

A structure (UDT) arrives in SENTIENT as JSON text with its members in order. Reading a UDT needs **Upload tag list from PLC on connect**; without it, the log says so for that key and the other keys keep reading.

**SLC 500 and MicroLogix**: a data-file address:

| File | Examples |
|---|---|
| Integer, float, long | `N7:0`, `F8:1`, `L9:0` |
| Bit | `B3:0/1`, or `B3/17` (bit 17 of the file) |
| Timer, counter | `T4:0.ACC`, `T4:0.PRE`, `T4:0.DN`, `C5:0.PRE`, `C5:0.CU` |
| Status, string, ASCII | `S:1/15`, `ST10:0`, `A11:0` |
| Inputs, outputs | `I:0.0/3`, `O:0.0/1` |

An address that is not valid is explained in the dialog, for example *SLC addresses use a colon* when you typed `N7.0`.

**Modifier** scales a value, or maps a raw range to an engineering range. You can also **import** keys from an `.xlsx`, `.xls` or `.csv` file by choosing the **PLC Tag Column** and **Tag Name Column**, or edit them all in the [key sheet](/docs/iot-gateway/key-sheets/).

## Write to the controller

Add keys under **RPC Methods** or **Attribute Updates** with a **PLC Tag** and a data type (`BOOL`, `SINT`, `INT`, `DINT`, `LINT`, `USINT`, `UINT`, `UDINT`, `ULINT`, `REAL`, `LREAL` or `STRING`), or use [Add to RPC write](/docs/iot-gateway/rpc-write/).

- Writing `T4:0.PRE` sets the timer's preset, and a string write replaces the whole string.
- A write the controller refuses, for example to a misspelt tag, is reported for that key. The connection stays up.

## Controller clock

**Sync Time** (**Sync PLC clock to system time**) sets a Logix controller's clock from the gateway. Time synchronization can also repeat it on an interval. It works on ControlLogix and CompactLogix only.

## When something is wrong

| What you see | What to do |
|---|---|
| The device does not start; the log lists valid PLC types | The **PLC Type** is misspelt in the configuration. Choose it again in the dialog |
| A UDT key reports *set initTags on the device to decode it by member* | Turn on **Upload tag list from PLC on connect** |
| No answer from a ControlLogix | Check **Slot**: it is the processor's slot, not the Ethernet module's |
| Discovery finds nothing | Discovery uses a broadcast, which routers do not pass. Type the **Host** instead |

## Related

- [Key sheets](/docs/iot-gateway/key-sheets/)
- [Write values to devices](/docs/iot-gateway/rpc-write/)
