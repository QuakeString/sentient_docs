# Post client-side rpc request. Replace $SENTIENT_EDGE_HOST_NAME and $ACCESS_TOKEN with corresponding values.
cat rpc-client-request.json | coap post coap://$SENTIENT_EDGE_HOST_NAME/api/v1/$ACCESS_TOKEN/rpc
# For example, $SENTIENT_EDGE_HOST_NAME reference localhost, $ACCESS_TOKEN is ABC123:
cat rpc-client-request.json | coap post coap://localhost/api/v1/ABC123/rpc