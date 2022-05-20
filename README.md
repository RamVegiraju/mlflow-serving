# mlflow-serving
Example of locally serving a MLflow Model as REST API


## Deployment Steps

```
python3 train.py

mlflow models serve --model-uri runs:/<run-id>/model --no-conda

curl -d '{"data":[[0.09178,0.0,4.05,0.0,0.51,6.416,84.1,2.6463,5.0,296.0,16.6,395.5,9.04]]}' -H 'Content-Type: application/json'  
localhost:5000/invocations
```

## [Blog](https://ram-vegiraju.medium.com/mlflow-model-serving-bcd936d59052)
