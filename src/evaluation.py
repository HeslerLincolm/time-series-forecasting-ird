import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def forecast_metrics(y_true, y_pred): 
    mse = mean_squared_error(y_true, y_pred) 
    rmse = np.sqrt(mse) 
    mae = mean_absolute_error(y_true, y_pred) 
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100 
    return mse, rmse, mae, mape