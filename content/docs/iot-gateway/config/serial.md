+++
title = "Serial connector"
description = "Read text or binary frames from a device on a serial port (RS-232, RS-485, USB) with SENTIENT Gateway, and send it commands."
weight = 249

[extra]
status = "checked"
checked = "gateway 4.14.0"
+++
The **Serial** connector reads devices that send their own frames on a serial port, such as scales, barcode readers, analysers and simple sensors that print a line every second. It cuts each frame into values by byte position or by delimiter, and can send commands back. For Modbus RTU devices, use the [Modbus connector](/docs/iot-gateway/config/modbus/) instead; for DNP3 over serial, the [DNP3 connector](/docs/iot-gateway/config/dnp3/).

## Add it

SENTIENT's connector list has no **Serial** entry. Add it on the gateway's [local web page](/docs/iot-gateway/admin-ui/): **Services > Connectors**, add a connector of type **Serial**, and paste or edit its JSON configuration. The gateway reports the new connector to SENTIENT, which keeps it from then on.

A configuration made for the Python gateway's custom serial example (`custom_serial.json`) works unchanged.

## Configuration

```json
{
  "name": "Scale on COM3",
  "devices": [
    {
      "name": "Scale 1",
      "type": "scale",
      "port": "COM3",
      "baudrate": 9600,
      "bytesize": 8,
      "parity": "N",
      "stopbits": 1,
      "delimiter": "\r\n",
      "timeseries": [
        { "key": "weight", "type": "float", "untilDelimiter": " kg" }
      ],
      "attributes": [
        { "key": "serialNumber", "type": "string", "fromByte": 4, "toByte": -1 }
      ],
      "attributeUpdates": [
        { "attributeOnPlatform": "tare", "stringToDevice": "T${tare}\r\n" }
      ],
      "serverSideRpc": [
        { "method": "zero", "type": "string", "withResponse": true,
          "responseType": "string", "responseUntilDelimiter": "\r", "responseTimeoutSec": 5 }
      ]
    }
  ]
}
```

### The port

| Key | Default | Meaning |
|---|---|---|
| `port` | `/dev/ttyUSB0` | The serial port: `COM3` on Windows, `/dev/ttyUSB0` or `/dev/ttyS0` on Linux |
| `baudrate` | 9600 | Speed |
| `bytesize`, `parity`, `stopbits` | 8, `N`, 1 | Data bits; parity `N`, `E` or `O`; stop bits 1, 1.5 or 2 |
| `rtscts`, `dsrdtr`, `xonxoff` | off | Hardware or software flow control |
| `delimiter` | `\n` | The bytes that end a frame |
| `timeout` | 1 | Seconds of silence after which a frame without a delimiter is taken as it is |

### Values

Each entry in `timeseries` (or `telemetry`) and `attributes` cuts one value out of a frame:

| Key | Meaning |
|---|---|
| `key` | The key's name in SENTIENT |
| `type` | `string`, `int`, `float` (or `double`), `bool` or `json`. Without a type, the bytes arrive as hexadecimal text |
| `fromByte`, `toByte` | Byte positions, counted from 0. `toByte: -1` means to the end of the frame |
| `fromDelimiter`, `untilDelimiter` | Text that starts or ends the value, used instead of byte positions. The value starts *at* `fromDelimiter`, so the delimiter itself is part of it; it ends just before `untilDelimiter`. A delimiter that is not in the frame leaves the frame whole |

A reading of `0`, `false` or empty text is sent like any other value.

### Commands to the device

- **`attributeUpdates`**: when the shared attribute named in `attributeOnPlatform` changes in SENTIENT, the gateway sends `stringToDevice` with `${attribute}`, `${deviceName}` and `${deviceType}` filled in.
- **`serverSideRpc`**: an RPC with that `method` sends its parameter, encoded by `type` (`int`, `float` or text). With `withResponse: true`, the gateway waits up to `responseTimeoutSec` for the answer, ends it at `responseUntilDelimiter` (or cuts it with `responseFromByte` and `responseToByte`), and returns it as `responseType`.

## Access to the port

- **Linux**: the packages add the gateway's service user to the `dialout` group (`uucp` on Arch). If you run the program another way, add its user to that group.
- **Docker**: map the device into the container, for example `devices: ["/dev/ttyUSB0:/dev/ttyUSB0"]`.
- **Windows**: close any other program that holds the COM port. A port can be open in only one program at a time.

## Related

- [Local web page](/docs/iot-gateway/admin-ui/)
- [Modbus connector](/docs/iot-gateway/config/modbus/)
