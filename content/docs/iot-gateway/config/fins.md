+++
title = "Omron FINS connector"
description = "Read and write Omron CJ, CS, CP and NJ/NX PLCs with SENTIENT Gateway over FINS/UDP."
weight = 244

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
The **FINS** connector reads and writes Omron PLCs over FINS on UDP (port **9600**), the protocol CX-Programmer uses on Ethernet. It works with CJ, CS and CP series CPUs and with NJ/NX controllers that have FINS enabled. No Omron software is needed on the gateway machine.

## Add a PLC

1. In SENTIENT, open the gateway, then **Connectors**, and add a **FINS** connector.
2. Under **Omron FINS Devices**, click **+** and fill in:

   | Setting | Value |
   |---|---|
   | **Device Name**, **Device profile** | The device in SENTIENT |
   | **Host**, **Port** | The PLC's IP address and port, `9600` by default |
   | **FINS network (DNA)** | `0` for the local network |
   | **Destination node (DA1)** | The PLC's FINS node. Leave empty to use the last number of its IP address, the usual Omron setting |
   | **Destination unit (DA2)** | `0` for the CPU unit |
   | **Source node (SA1)** | The gateway's node. Leave empty to use the last number of the gateway's IP address |
   | **Response timeout (ms)** | How long to wait for an answer |
   | **Low word first (CX-Programmer convention)** | On (default): 32- and 64-bit values keep the low word at the lower address, as CJ, CS and CP CPUs do. Turn off only for a device that stores the high word first |
   | **Poll Period (ms)**, **Connect Attempts**, **Wait After Failed (ms)** | How often to read, and how to retry |

3. Add keys, click **Apply**, and save the connector.

The source node must be free on the FINS network: two gateways or a gateway and a PC with the same last IP number confuse the PLC's replies.

## Addresses

Use the addresses as in CX-Programmer:

| Area | Examples |
|---|---|
| Data memory | `D100` or `DM100` |
| CIO | `CIO20`, or just `20` |
| Work, holding, auxiliary | `W10`, `H5`, `A448` |
| Extended memory | `E0_100` (bank 0, word 100) |
| Timer and counter present values | `T15`, `C4` |
| One bit of a word | `D100.5`, `CIO20.07` (bits 0 to 15) |

**Value Type**: `uint16` (a word, the default), `int16`, `uint32`, `int32`, `uint64`, `int64`, `float32`, `float64`, `string` or `bool`. A bit address is always `bool`.

**Modifier** scales a value, or maps a raw range to an engineering range. **Import Tags** reads keys from an `.xlsx`, `.csv` or `.ods` file, and the [key sheet](/docs/iot-gateway/key-sheets/) edits them all at once.

## Write to the PLC

Add keys under **RPC Methods** or **Attribute Updates** with an address and value type, or use [Add to RPC write](/docs/iot-gateway/rpc-write/). A write the PLC refuses is reported for that key only; the connection stays up.

## When something is wrong

| What you see | What to do |
|---|---|
| No answer at all | FINS uses UDP. Check that nothing between the gateway and the PLC blocks UDP 9600, and that the PLC's FINS/UDP is enabled |
| No answer, but the PLC can be pinged | Check **Destination node**. With the automatic setting, the PLC's node must equal the last number of its IP address |
| REAL values look like tiny or huge nonsense numbers | **Low word first** does not match how the device stores them |
| One key fails, the others work | The PLC refused that address (for example a bank that does not exist). The log names it, and the other keys keep reading |

## Related

- [Key sheets](/docs/iot-gateway/key-sheets/)
- [Write values to devices](/docs/iot-gateway/rpc-write/)
