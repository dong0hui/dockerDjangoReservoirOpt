# Django Template for Reservoir Optimization

## Build the docker image
```
docker build -t django/reservoiroptimization:0.0.1 .
```

## Test the docker image
```
docker run -p 8083:8000 django/reservoiroptimization:0.0.1
```
Use Postman (or Swagger) test http://127.0.0.1:8083/api/v1/storage/downloand/ with POST method
```
{
    "username": <username>,
    "blobaccount": <blob account>,
    "blobcontainer": <blob container>
}
```
To test the codes, go into Docker container
```
winpty docker run -it django/reservoiroptimization:0.0.1 bash
#python3 /reservoiroptimization/test/CosmosMongo_test.py
```

## Push docker image to Azure container Registry
```
az login
az acr login --name container1324
docker tag django/reservoiroptimization:0.0.1 container1324.azurecr.io/django/reservoiroptimization:0.0.1
docker push container1324.azurecr.io/django/reservoiroptimization:0.0.1
```

## Deploy docker image to Kubernetes
```
kubectl create namespace django
kubectl apply -f reservoiroptimization.yaml
kubectl get service -n django --watch
```
After external IP of Load Balancer is available, you can send post request to http://<external IP>:8000/api/v1/storage/download/
