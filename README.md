# mlflow-serving
Example of locally serving a MLflow Model


## Deployment Steps

```
python3 train.py #train model
mlflow models serve --model-uri runs:/<run-id>/model --no-conda #remove conda env variable if you are in conda env
curl -d '{"data":[[0.09178,0.0,4.05,0.0,0.51,6.416,84.1,2.6463,5.0,296.0,16.6,395.5,9.04]]}' -H 'Content-Type: application/json'  localhost:5000/invocations #while previous shell is open
```
