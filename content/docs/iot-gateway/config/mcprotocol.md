+++
title = "MELSEC MC Protocol connector"
description = "Read and write Mitsubishi MELSEC Q, L, QnA, iQ-L and iQ-R PLCs with SENTIENT Gateway over MC Protocol (SLMP), 3E or 4E frames, binary or ASCII."
weight = 239

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
The **MC Protocol** connector reads and writes Mitsubishi MELSEC PLCs over the MELSEC Communication protocol (also called SLMP), through the CPU's built-in Ethernet port or an Ethernet module. It needs no Mitsubishi software on the gateway machine.

Supported: **Q**, **L**, **QnA**, **iQ-L** and **iQ-R** series, **3E** and **4E** frames, **binary** and **ASCII** encoding.

## Prepare the PLC

In GX Works, open the Ethernet settings of the CPU or the Ethernet module and add an **open setting** (connection) for the gateway:

- Protocol **TCP**, open system **MC protocol** (or **SLMP**), and a port, often **5007**.
- Note whether the **communication data code** is binary or ASCII; the connector must use the same.
- On a Q or L CPU, allow writes during RUN if the gateway is to write.

Write the parameters to the PLC and reset it.

## Add a PLC

1. In SENTIENT, open the gateway, then **Connectors**, and add an **MC Protocol** connector.
2. Under **Mitsubishi MELSEC Devices**, click **+** and fill in:

   | Setting | Value |
   |---|---|
   | **Device Name**, **Device profile** | The device in SENTIENT |
   | **Host**, **Port** | The PLC's IP address and the port of the open setting |
   | **PLC series** | `Q` (default), `L`, `QnA`, `iQ-L` or `iQ-R`. It sets the device codes and address widths |
   | **MC frame** | `3E` (the usual) or `4E`, only if the module is set up for 4E |
   | **Encoding** | `binary` or `ascii`, as in the PLC's open setting |
   | **Network No.**, **PC (station) No.** | `0` and `255` for a PLC you reach directly |
   | **Module I/O No.**, **Module station No.** | `1023` and `0` to reach the CPU directly. Other values route to a module in a multidrop setup |
   | **Response timeout (ms)** | How long to wait for an answer |
   | **Poll Period (ms)**, **Connect Attempts**, **Wait After Failed (ms)** | How often to read, and how to retry |

3. Add keys, click **Apply**, and save the connector.

## Addresses

Use the device addresses as in GX Works:

| Kind | Examples |
|---|---|
| Word devices | `D100` (data register), `SD210`, `R100`, `TN5` and `CN3` (timer and counter current values), `W0FF`, `SW0`, `ZR1000` |
| One bit of a word | `D100.5` (bits 0 to 15) |
| Bit devices | `M200`, `L0`, `F0`, `SM400`, `X1A`, `Y0`, `B1F`, `TS5` and `TC5` (timer contact and coil), `CS3`, `CC3` |

`X`, `Y`, `B`, `W`, `SB`, `SW`, `DX`, `DY` and `ZR` are numbered in hexadecimal, as in GX Works; the others in decimal.

**Value Type**: `bool`, `int16` (the default), `uint16`, `int32`, `uint32`, `int64`, `uint64`, `float32`, `float64` or `string`. 32- and 64-bit types read the following registers too. Bit devices and `.bit` addresses are always `bool`.

**Modifier** scales a value, or maps a raw range to an engineering range. **Import Tags** reads keys from an `.xlsx`, `.csv` or `.ods` file, and the [key sheet](/docs/iot-gateway/key-sheets/) edits them all at once.

## Write to the PLC

Add keys under **RPC Methods** or **Attribute Updates** with an address and value type, or use [Add to RPC write](/docs/iot-gateway/rpc-write/). Writing one bit of a word (`D50.3`) reads the word, changes the bit and writes the word back, because MC Protocol has no single-bit write for word devices. Avoid it on a word that the PLC program changes at the same time.

## When something is wrong

| What you see | What to do |
|---|---|
| The PLC never answers | Check the port and that the open setting is **MC protocol**, not *unpassive* or a socket. Reset the PLC after changing parameters |
| Answers are garbled or every read fails | **Encoding** does not match the PLC's communication data code |
| One key fails, the rest work | The address does not exist on that series, for example an iQ-R device on a Q CPU. The log names it once a minute |
| Values differ from the Python gateway on an ASCII link | The Python gateway read hexadecimal devices (`X0A0`, `W0FF`) at the wrong point in ASCII mode. The new values are the correct ones |
| A long silence after the PLC restarts | After **Connect Attempts** failures the connector waits **Wait After Failed (ms)** (10 s by default) before trying again |

## Related

- [Key sheets](/docs/iot-gateway/key-sheets/)
- [Write values to devices](/docs/iot-gateway/rpc-write/)
