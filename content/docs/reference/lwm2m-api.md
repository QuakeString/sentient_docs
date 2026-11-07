+++
title = "LwM2M"
description = "LwM2M devices cannot connect to SENTIENT 4.3.0.57. What to use instead."
aliases = ["/docs/user-guide/ssl/lwm2m-over-dtls/"]

[extra]
status = "checked"
checked = "4.3.0.57"
+++
<div class="st-callout warn">

**SENTIENT 4.3.0.57 does not accept LwM2M devices.** The device profile still offers the LwM2M transport type, and you can save such a profile, but no LwM2M server is running, so a device using it never connects. This also applies to LwM2M over DTLS.

</div>

Until LwM2M is available, connect the device in one of these ways:

| Device can | Use |
|---|---|
| Speak CoAP | [CoAP](/docs/reference/coap-api/), on UDP port 5683 |
| Speak MQTT or HTTP | [MQTT](/docs/reference/mqtt-api/) or [HTTP](/docs/reference/http-api/) |
| Only speak its own protocol, or a fieldbus | The [SENTIENT Gateway](/docs/iot-gateway/), which reads the device and sends its values over MQTT |

See [Device protocols](/docs/reference/protocols/) to compare them.
