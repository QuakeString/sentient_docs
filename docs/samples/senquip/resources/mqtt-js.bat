@echo off

REM Set SENTIENT host to "mqtt.sentient.cloud" for SENTIENT Cloud (North America)
REM Set SENTIENT host to "mqtt.eu.sentient.cloud" for SENTIENT Cloud (Europe)
REM Set SENTIENT host to "localhost" for local platform installation
set SENTIENT_HOST=mqtt.sentient.cloud

REM Replace YOUR_ACCESS_TOKEN with one from Device details panel.
set ACCESS_TOKEN=YOUR_ACCESS_TOKEN

REM Read serial number and firmware version attributes
set /p ATTRIBUTES=<attributes-data.json

REM Read timeseries data as an object without timestamp (server-side timestamp will be used)
set /p TELEMETRY=<telemetry-data.json

REM publish attributes and telemetry data via mqtt client
node publish.js