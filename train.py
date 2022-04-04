import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics

import mlflow
import mlflow.sklearn

if __name__ == "__main__":
    #Load data
    boston = datasets.load_boston()
    df = pd.DataFrame(boston.data, columns = boston.feature_names)
    df['MEDV'] = boston.target
    
    #Split Model
    X = df.drop(['MEDV'], axis = 1) 
    y = df['MEDV']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 42)
    
    #Model Creation
    lm = LinearRegression()
    lm.fit(X_train,y_train)
    
    #Model prediction
    Y_Pred = lm.predict(X_test)
    RMSE = np.sqrt(metrics.mean_squared_error(y_test, Y_Pred))
    
    print(f"RMSE: {RMSE}")
    mlflow.log_metric("score", RMSE)
    mlflow.sklearn.log_model(lm, "model")
    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)