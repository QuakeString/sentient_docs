Edit “sentient-analytics/sentient-analytics-secret.yml” and replace YOUR_DB_IP_ADDRESS and YOUR_DB_PASSWORD and apply Kubernetes Job:
```text
kubectl apply -f ./sentient-analytics/sentient-analytics-secret.yml
kubectl apply -f ./sentient-analytics/sentient-analytics-create-db.yml
```
{: .copy-code}

You can see logs if you run the next command:
```text
kubectl logs job/sentient-analytics-create-db -n sentient
```
