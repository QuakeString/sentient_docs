# Send subscribe attributes request with 20 seconds timeout. Replace $SENTIENT_HOST_NAME and $ACCESS_TOKEN with corresponding values.
curl -v -X GET http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes/updates?timeout=20000
# For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (North America), $ACCESS_TOKEN is ABC123:
curl -v -X GET https://sentient.cloud/api/v1/ABC123/attributes/updates?timeout=20000
# For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (Europe), $ACCESS_TOKEN is ABC123:
curl -v -X GET https://eu.sentient.cloud/api/v1/ABC123/attributes/updates?timeout=20000