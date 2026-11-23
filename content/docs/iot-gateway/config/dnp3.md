+++
title = "DNP3 connector"
description = "Poll DNP3 (IEEE 1815) outstations with SENTIENT Gateway over TCP, TLS (IEC 62351-3), UDP or serial RS-232/RS-485: classes, unsolicited events, controls, time sync and secure authentication."
weight = 233

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
The **DNP3** connector makes the gateway a DNP3 master (IEEE 1815). It polls outstations such as RTUs, protection relays and meters, receives their unsolicited events, and sends controls. It runs over **TCP**, **TLS** (IEC 62351-3), **UDP** or a **serial** RS-232 / RS-485 line, and supports Secure Authentication v5.

The set-up has two parts: **channels** (the connections) on the **General** tab, and **outstations** (the devices) on the **Devices** tab.

## 1. Add a channel

A channel is one connection. Over TCP or TLS it usually carries one outstation; one serial RS-485 line can carry several.

1. In SENTIENT, open the gateway, then **Connectors**, and add a **DNP3** connector.
2. On **General**, under **Channels**, click **Add channel**, give it a **Channel name**, and choose its **Type**:

| Type | Settings |
|---|---|
| **TCP client** | Host and port (DNP3's is **20000**). **Alternate addresses** for a second network or a redundant path: a failed attempt tries the next one. **Local address** to choose the gateway's network |
| **TLS client (IEC 62351-3)** | Host and port (**19999** by default), **CA certificate**, the gateway's own **Gateway certificate** and **Gateway private key** for mutual authentication, **Server name**, **Minimum TLS version**. Certificate paths are files on the gateway |
| **UDP (one frame per datagram)** | The outstation's port, and the gateway's **Local address** and **Local port** where answers and unsolicited reports arrive (20000 by default) |
| **Serial port (RS-232 / RS-485)** | **Serial port** (`COM3`, `/dev/ttyUSB0`), **Baud rate**, **Data bits**, **Parity**, **Stop bits**, **Flow control**, and **Open delay (ms)** for line drivers that lose the first frame |

**Connect timeout (ms)**, **First retry delay (ms)** and **Longest retry delay (ms)** control reconnection: the delay doubles after each failure, up to the longest.

## 2. Add an outstation

On **Devices**, under **DNP3 Outstations**, click **+**:

| Setting | Value |
|---|---|
| **Device Name**, **Device profile** | The device in SENTIENT |
| **Channel** | The channel it is reached over |
| **Master address** | The gateway's link address, as configured in the outstation (often `1`) |
| **Outstation address** | The outstation's link address, 0 to 65519. Each outstation on a channel needs its own |
| **Startup** | On every connection: **Disable unsolicited reporting first**, run an **Integrity poll**, then **Enable unsolicited for** the chosen classes |
| **Polls** | **Integrity poll every (ms)** reads everything; **Class 1/2/3 poll every (ms)** reads that class's events. `0` turns a poll off. **Poll events the outstation reports waiting** reads them at once |
| **Time synchronisation** | **None**, **LAN** or **Non-LAN** (serial links). Turn it on only if no SCADA master already sets the clock |
| **Use the outstation's event times** | Events keep the time the outstation recorded. Turn off if nobody sets its clock |
| **Response timeout (ms)**, **Timeouts before offline**, request retries, **Link keep-alive (ms)** | Timing |
| **Allow cold and warm restart RPCs** | Off by default: a restart interrupts the outstation's control |

On a shared **RS-485** line, outstations are polled in turn. Turn their unsolicited reporting off (no classes selected), or their reports collide on the line.

## Points

A point is a **Point type** and an **Index** in the outstation's point list. Its static and event values update the same key in SENTIENT; an event keeps the outstation's time.

Point types: **Binary input**, **Double-bit binary**, **Binary output status**, **Counter**, **Frozen counter**, **Analog input**, **Analog output status**, **Octet string** and **Security statistic**.

- **State names (00, 01, 10, 11)** give a double-bit point readable values, such as `intermediate`, `open`, `closed`, `bad`.
- **Quality flags** publishes the point's flags (ONLINE, RESTART, COMM_LOST, forced, over range) as `<key>Quality`, as an attribute or as telemetry.
- **Drop values that are not ONLINE** keeps doubtful values out.

**Import XML** reads the outstation vendor's **IEEE 1815 Device Profile** and adds its points, named after the profile, with double-bit state names. Points you already have are left as they are.

## Controls

A command acts on one output point and is called from SENTIENT as an RPC (or from an attribute update):

- **Binary output (CROB)**: choose **Operation** (**Pulse on**, **Pulse off**, **Latch on**, **Latch off**), **Trip / close**, **Count**, **On time (ms)** and **Off time (ms)**. For an attribute, choose the command sent **When true** and **When false**.
- **Analog output**: the set point, with its **Encoding**: g41 variation 1 (int32), 2 (int16), 3 (float32) or 4 (float64).
- **Mode**: **Select before operate** (safest: the outstation checks the command first), **Direct operate**, or **Direct operate, no acknowledgement**.

The outstation's status for the point is the RPC's answer.

These RPC names are built in and answered by the gateway: `read`, `integrityPoll`, `eventPoll`, `timeSync`, `enableUnsolicited`, `disableUnsolicited`, `coldRestart`, `warmRestart`.

## Secure authentication

To use IEEE 1815-2012 Secure Authentication v5, turn on **Authenticate with the outstation (SAv5)** and add users. **User 1** is required. For each user, **Update key file** is the path of a file on the gateway holding the update key (32 or 64 hex digits, or 16 or 32 raw bytes, for AES-128 or AES-256); the key itself is never stored in SENTIENT. **Session key change (ms)** must be shorter than the outstation's own session key lifetime (15 minutes by default).

## When something is wrong

| What you see | What to do |
|---|---|
| The device goes offline after a few seconds | Check **Master address** and **Outstation address**: they must match the outstation's settings exactly |
| No events, only integrity values | Events come through class polls or unsolicited reports. Set a class poll, or enable unsolicited for the classes |
| Garbled frames on RS-485 | Several outstations report unsolicited at once. Turn unsolicited off and poll them |
| Clock jumps on the outstation | Two masters set its clock. Set **Time synchronisation** to **None** |
| TLS connection refused | Check the **CA certificate** and **Server name**, and give the gateway's certificate and key if the outstation asks for them |

## Related

- [Write values to devices](/docs/iot-gateway/rpc-write/)
- [Serial connector](/docs/iot-gateway/config/serial/)
