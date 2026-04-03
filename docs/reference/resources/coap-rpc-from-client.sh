# Post client-side rpc request. Replace $SENTIENT_HOST_NAME and $ACCESS_TOKEN with corresponding values.
cat rpc-client-request.json | coap post coap://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc
# For example, $SENTIENT_HOST_NAME reference to SENTIENT Cloud (North America), $ACCESS_TOKEN is ABC123:
cat rpc-client-request.json | coap post coap://coap.sentient.cloud/api/v1/ABC123/rpc
# For example, $SENTIENT_HOST_NAME reference to SENTIENT Cloud (Europe), $ACCESS_TOKEN is ABC123:
cat rpc-client-request.json | coap post coap://coap.eu.sentient.cloud/api/v1/ABC123/rpc