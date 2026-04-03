# Publish response to RPC request. Replace $SENTIENT_HOST_NAME and $ACCESS_TOKEN with corresponding values.
coap-client -f rpc-response.json -m post coap://$SENTIENT_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc/1
# For example, $SENTIENT_HOST_NAME reference to SENTIENT Cloud (North America), $ACCESS_TOKEN is ABC123:
coap-client -f rpc-response.json -m post coap://coap.sentient.cloud/api/v1/ABC123/rpc/1
# For example, $SENTIENT_HOST_NAME reference to SENTIENT Cloud (Europe), $ACCESS_TOKEN is ABC123:
coap-client -f rpc-response.json -m post coap://coap.eu.sentient.cloud/api/v1/ABC123/rpc/1