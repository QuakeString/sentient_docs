#!/bin/sh

# Set SENTIENT host to "mqtt.sentient.cloud" for SENTIENT Cloud (North America)
# Set SENTIENT host to "mqtt.eu.sentient.cloud" for SENTIENT Cloud (Europe)
# Set SENTIENT host to "localhost" for local platform installation
SENTIENT_HOST="mqtt.sentient.cloud"
# Replace YOUR_ACCESS_TOKEN with one from Device details panel.
ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
# Publish serial number and firmware version attributes
mosquitto_pub -d -h "$SENTIENT_HOST" -t "v1/devices/me/attributes" -u "$ACCESS_TOKEN" -f "attributes-data.json"
# Publish timeseries data as an object without timestamp (server-side timestamp will be used)
mosquitto_pub -d -h "$SENTIENT_HOST" -t "v1/devices/me/telemetry" -u "$ACCESS_TOKEN" -f "telemetry-data.json"
