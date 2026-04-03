# Publish client-side attributes update. Replace $SENTIENT_HOST_NAME and $ACCESS_TOKEN with corresponding values.
curl -v -X POST --data "{"attribute1": "value1", "attribute2":true, "attribute3": 43.0}" http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes --header "Content-Type:application/json"
# For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (North America), $ACCESS_TOKEN is ABC123:
curl -v -X POST --data "{"attribute1": "value1", "attribute2":true, "attribute3": 43.0}" https://sentient.cloud/api/v1/ABC123/attributes --header "Content-Type:application/json"
# For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (Europe), $ACCESS_TOKEN is ABC123:
curl -v -X POST --data "{"attribute1": "value1", "attribute2":true, "attribute3": 43.0}" https://eu.sentient.cloud/api/v1/ABC123/attributes --header "Content-Type:application/json"

# Publish client-side attributes update from file. Replace $SENTIENT_HOST_NAME and $ACCESS_TOKEN with corresponding values.
curl -v -X POST -d @new-attributes-values.json http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/attributes --header "Content-Type:application/json"
# For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (North America), $ACCESS_TOKEN is ABC123:
curl -v -X POST -d @new-attributes-values.json https://sentient.cloud/api/v1/ABC123/attributes --header "Content-Type:application/json"
# For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (Europe), $ACCESS_TOKEN is ABC123:
curl -v -X POST -d @new-attributes-values.json https://eu.sentient.cloud/api/v1/ABC123/attributes --header "Content-Type:application/json"