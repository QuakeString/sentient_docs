Topic filters define **MQTT-based subscriptions** and act as triggers for ST-RMQTT HTTP Integration. When the broker receives a message matching configured **topic filters**, the integration processes it and forwards the data to the specified external system.

If the integration is configured with the topic filter:
```plaintext
st-rmqtt/devices/+/status
```

Then, any message matching this pattern will trigger the integration, including:
```plaintext
st-rmqtt/devices/device-01/status
st-rmqtt/devices/gateway-01/status
```