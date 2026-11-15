+++
title = "Beckhoff ADS connector"
description = "Read and write Beckhoff TwinCAT 2 and 3 PLCs with SENTIENT Gateway over ADS, by symbol name or index group and offset, polled or pushed on change."
weight = 230

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
The **ADS** connector reads and writes Beckhoff TwinCAT PLCs over ADS (AMS/TCP, port **48898**). It speaks ADS itself, so the gateway needs no TwinCAT installation, and it can read by symbol name (`MAIN.fTemp`) without you giving a data type.

## Prepare the PLC: add a route

TwinCAT answers only machines it has a **route** to. On the PLC, in TwinCAT, add a static route for the gateway:

- **AMS Net Id**: the gateway's, usually its IP address followed by `.1.1`, for example `192.168.10.50.1.1`.
- **Address**: the gateway's IP address. **Transport**: TCP/IP.

If you choose another AMS Net Id for the gateway, enter the same value as **Client AMS NetId** below.

## Add a PLC

1. In SENTIENT, open the gateway, then **Connectors**, and add an **ADS** connector.
2. Under **Beckhoff ADS Devices**, click **+** and fill in:

   | Setting | Value |
   |---|---|
   | **Device Name**, **Device profile** | The device in SENTIENT |
   | **Host** | The PLC's IP address |
   | **AMS NetId** | The PLC's AMS Net Id, for example `5.19.44.2.1.1`. TwinCAT shows it in the system tray menu, under **Router > Change AMS NetId** |
   | **AMS Port** | `851` for the first TwinCAT 3 PLC runtime, `852` for the second. TwinCAT 2: `801` |
   | **Client AMS NetId** | The gateway's own AMS Net Id. Leave empty to use the gateway's IP address with `.1.1` |
   | **Push on change (ADS notifications)** | The PLC sends a value only when it changes, instead of being polled. Less load and lower delay |
   | **Poll Period (ms)**, **Connect Attempts**, **Wait After Failed (ms)** | How often to read, and how to retry |

3. Add keys, click **Apply**, and save the connector.

## Keys

Each key has a **Tag** (the key's name in SENTIENT) and an **Address**:

- A **symbol name**, as in the TwinCAT project: `MAIN.fTemp`, `GVL.bReady`, `.globalVar`, `MAIN.aValues[3]`, `MAIN.stMotor.nSpeed`. You can leave **Value Type** empty: the gateway asks the PLC for the type. Strings, arrays and structures are read whole.
- An **index group and offset**, for example `0x4020:0` or `16416:0`. Here **Value Type** is required: `bool`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, `int64`, `uint64`, `float32`, `float64` or `string`.

**Browse symbols online** lists the PLC's symbols with their type and **Comment**; tick them and add them as time series or attributes. **Import Tags** reads keys from an `.xlsx`, `.csv` or `.ods` file, and the [key sheet](/docs/iot-gateway/key-sheets/) edits them all at once. **Modifier** scales a value, or maps a raw range to an engineering range.

## Write to the PLC

Add keys under **RPC Methods** or **Attribute Updates** with an address, or use [Add to RPC write](/docs/iot-gateway/rpc-write/).

## When something is wrong

| What you see | What to do |
|---|---|
| The PLC refuses the connection, or nothing answers | The route is missing or names another AMS Net Id. Check the route on the PLC and **Client AMS NetId** |
| ADS error 1808 on one key | The symbol does not exist. Check its spelling; the other keys keep reading |
| Keys stop briefly after a program download | Normal: the gateway takes new handles for the changed symbols and goes on |
| Wrong values from an index-group key | Its **Value Type** does not match the PLC variable |

## Related

- [Key sheets](/docs/iot-gateway/key-sheets/)
- [Write values to devices](/docs/iot-gateway/rpc-write/)
