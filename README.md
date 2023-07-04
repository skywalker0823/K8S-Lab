# K8S-Lab
Easy guide for creating a service on GCP using GKE.

## Initial test
1. Create a cluster.
2. Create a namespace -> ex. my-sample-app.
2. kubectl apply -f deployment.yaml
3. kubectl apply -f service.yaml
4. kubectl get service -n my-sample-app
5. localhost:30009


## Basic steps
1. Set default compute region and zone.
```shell
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a
```

2. Create a cluster.
```shell
gcloud container clusters create --machine-type=e2-medium --zone=us-west3-b lab-cluster
```

3. Get credentials for the cluster.
```shell
gcloud container clusters get-credentials lab-cluster
```

4. Create a deployment.
```shell
kubectl create deployment hello-server --image=gcr.io/google-samples/hello-app:1.0
```

5. Expose the deployment.
```shell
kubectl expose deployment hello-server --type=LoadBalancer --port 8080
```

6. Get the service.
```shell
kubectl get service hello-server
```

7. view the service.
```shell
http://<EXTERNAL-IP>:8080
```

8. Delete the cluster.
```shell
gcloud container clusters delete lab-cluster
```
