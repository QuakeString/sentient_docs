+++
title = "EtherCAT connector"
description = "Make SENTIENT Gateway the EtherCAT master: scan the bus, read and write process data (PDO) and the object dictionary (SDO) of EtherCAT slaves."
weight = 234

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
The **EtherCAT** connector makes the gateway the **EtherCAT master** (MainDevice) of a segment: it brings up the bus, exchanges process data with the slaves every cycle, and reads and writes their object dictionaries. Use it where no PLC owns the bus, for example a test bench or a skid with I/O terminals and drives.

> EtherCAT support is complete but has not yet been run against real hardware. Treat the first site as commissioning, and compare values with the slaves' own displays.

## What the gateway machine needs

- **Linux**, and a **network port used only for EtherCAT**. The master sends raw Ethernet frames on it; nothing else may use that port.
- The gateway in **Docker** (the image has the EtherCAT connector; the Linux packages and the bare program do not), with `network_mode: host` and `cap_add: [NET_RAW]` in the compose file.
- An EtherCAT segment can have only one master. If a PLC already runs the bus, read the values from the PLC instead (for example with the [ADS](/docs/iot-gateway/config/ads/) or [S7](/docs/iot-gateway/config/s7/) connector).

## Set up the master

1. In SENTIENT, open the gateway, then **Connectors**, and add an **EtherCAT** connector.
2. Under **EtherCAT Master Settings**:

   | Setting | Value |
   |---|---|
   | **Network interface** | The dedicated port, for example `eth1` |
   | **Cycle time (µs)** | How often process data is exchanged. Shorter is faster and costs more CPU |
   | **Use Distributed Clocks** | Only if your slaves need tight synchronisation, for example motion drives |

3. Under **EtherCAT Slaves**, click **Scan bus**. The gateway lists each slave with its **Slave position**, **Slave Name**, **Vendor ID**, **Product Code** and **I/O (bytes)** in and out. Add the ones you need, or click **+** and enter the **Slave position** (counted from 0 at the master).

## Keys

Each key has a **Tag**, an **Address** and a **Value Type** (always required: `bool`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `int64`, `uint64`, `float32`, `float64` or `string`).

| Address | Reads |
|---|---|
| `pdo:<byte>` | Process data at that byte of the slave's input image, for example `pdo:0`. Updated every cycle |
| `pdo:<byte>.<bit>` | One bit, for example `pdo:2.1`. Must be `bool`, and a `bool` PDO must name a bit |
| `sdo:<index>:<subindex>` | An object-dictionary entry, decimal or hex, for example `sdo:0x603F:0` (a drive's error code) |

**Import Tags** reads keys from an `.xlsx`, `.csv` or `.ods` file, and the [key sheet](/docs/iot-gateway/key-sheets/) edits them all at once.

## Write to slaves

Add keys under **RPC Methods** or **Attribute Updates**, or use [Add to RPC write](/docs/iot-gateway/rpc-write/). A `pdo:` write goes into the slave's output image on the next cycle; an `sdo:` write is a mailbox transfer.

## When something is wrong

| What you see | What to do |
|---|---|
| The bus does not come up | Check **Network interface**, that the container runs with `network_mode: host` and `NET_RAW`, and that nothing else uses the port |
| All slaves go offline together | A slave left the segment (power, cable). The gateway notices it from the frame counter after three cycles, takes the segment offline, and brings it up again by itself |
| A drive's values freeze | Look in the log for a lost exchange: the gateway restarts the bus on its own and logs why |

## Related

- [Install on Linux and Docker](/docs/iot-gateway/install-linux/)
- [Key sheets](/docs/iot-gateway/key-sheets/)
