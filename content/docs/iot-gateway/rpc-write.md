+++
title = "Write values to devices"
description = "Turn the keys the gateway reads into RPC write methods or attribute updates, so dashboards and rules can write set points to the equipment."
weight = 226

[extra]
status = "checked"
checked = "4.3.0.57"
+++
A gateway connector reads values from the equipment through its **time series** and **attribute** keys. To write a value back, for example a set point or a start command, the device needs a write key. There are two kinds:

| Kind | How a write happens |
|---|---|
| **RPC write** method | A dashboard button, switch or input, or a rule chain, calls the method with the value to write |
| **Attribute update** | Changing a shared attribute of the device in SENTIENT writes the new value to the equipment |

You can write these keys by hand, but most of the time the address you want to write is one you already read. **Add to RPC write** copies read keys into write keys with the same address and data type.

## Add write keys from read keys

1. In SENTIENT, open the gateway, then **Connectors**, and open the device in the connector's configuration.
2. Open its **Time series** or **Attributes** keys.
3. Tick the keys you want to write. In the [key sheet](/docs/iot-gateway/key-sheets/), select their rows by the row number instead.
4. Click **Add to RPC write** or **Add to attribute updates**.
5. In the dialog, check the names:
   - **Method name** or **Attribute name** is what a dashboard widget or a rule calls. Choose **Same as key** or **set_ + key** for all of them, and change any single name in the list.
   - **Data type** and **Writes with** show how each value will be written. They come from the read key.
6. Click **Add N methods** (or **Add N attribute updates**), then **Apply** and save the connector.

The new keys are copies. Changing the read key later does not change the write key.

## Keys that are skipped

The dialog lists every key you ticked and says why one cannot be added:

| Message | Why |
|---|---|
| Input registers can't be written, Discrete inputs can't be written | Modbus function codes 4 and 2 are read only on the device |
| A bit inside a register can't be written on its own | Modbus writes whole registers. Write the register, or use a coil |
| Status and measured values can't be written, Inputs can't be written | The protocol does not allow writes to that address |
| Reads several points; add it by hand | The key reads more than one address |
| Already written by *name* | A write key for that address exists. It is not added twice |
| Same address as a key above | Two ticked keys read the same address; only the first is added |
| Name already used for *address* | The name was taken, so the new key is named `name_2`, shown in orange. Change it if you want |

The summary line says how many of the keys will be added.

## Connectors

**Add to RPC write** works for Modbus (single device mode), OPC UA, Siemens S7, Beckhoff ADS, MELSEC MC Protocol, Omron FINS, EtherNet/IP, EtherCAT, IEC 61850, PROFINET, DNP3 and SNMP. For BACnet and KNX, add write keys by hand.

The gateway's [local web page](/docs/iot-gateway/admin-ui/) has the same buttons on a device's keys for Modbus, OPC UA, S7, ADS, MC Protocol, FINS, EtherCAT and EtherNet/IP (gateway 4.14.0 and later).

## Write from a dashboard

Add a control widget, for example a switch, a knob or a value input, to a dashboard. Point it at the connector device, not at the gateway, and set its RPC method to the **Method name** you chose. The widget sends the value, and the gateway writes it with the address and data type of the key.

To test a method without a dashboard, use the gateway's **RPC debug terminal** in SENTIENT.

## Related

- [Key sheets](/docs/iot-gateway/key-sheets/)
- [Widget actions](/docs/user-guide/ui/widget-actions/)
