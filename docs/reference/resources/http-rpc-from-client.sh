# Post client-side rpc request. Replace $SENTIENT_HOST_NAME and $ACCESS_TOKEN with corresponding values.
curl -X POST -d @rpc-client-request.json http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc --header "Content-Type:application/json"
# For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (North America), $ACCESS_TOKEN is ABC123:
curl -X POST -d @rpc-client-request.json https://sentient.cloud/api/v1/ABC123/rpc --header "Content-Type:application/json"
# For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (Europe), $ACCESS_TOKEN is ABC123:
curl -X POST -d @rpc-client-request.json https://eu.sentient.cloud/api/v1/ABC123/rpc --header "Content-Type:application/json"