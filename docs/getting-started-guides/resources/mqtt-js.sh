#!/bin/sh

# Set SENTIENT host to "mqtt.sentient.cloud" for SENTIENT Cloud (North America)
# Set SENTIENT host to "mqtt.eu.sentient.cloud" for SENTIENT Cloud (Europe)
# Set SENTIENT host to "localhost" for local platform installation
export SENTIENT_HOST=mqtt.sentient.cloud

# Replace YOUR_ACCESS_TOKEN with one from Device details panel.
export ACCESS_TOKEN=YOUR_ACCESS_TOKEN

# Read serial number and firmware version attributes
ATTRIBUTES=$( cat attributes-data.json )
export ATTRIBUTES

# Read timeseries data as an object without timestamp (server-side timestamp will be used)
TELEMETRY=$( cat telemetry-data.json )
export TELEMETRY

# publish attributes and telemetry data via mqtt client
node publish.js
