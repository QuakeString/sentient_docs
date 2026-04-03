# Publish response to RPC request. Replace $SENTIENT_HOST_NAME and $ACCESS_TOKEN with corresponding values.
curl -v -X POST -d @rpc-response.json http://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc/1 --header "Content-Type:application/json"
# For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (North America), $ACCESS_TOKEN is ABC123:
curl -v -X POST -d @rpc-response.json https://sentient.cloud/api/v1/ABC123/rpc/1 --header "Content-Type:application/json"
# For example, $SENTIENT_HOST_NAME reference SENTIENT Cloud (Europe), $ACCESS_TOKEN is ABC123:
curl -v -X POST -d @rpc-response.json https://eu.sentient.cloud/api/v1/ABC123/rpc/1 --header "Content-Type:application/json"