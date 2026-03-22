import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error

def train_arima(series, order=(5,1,0)):
    """
    Train ARIMA model.
    """
    model = ARIMA(series, order=order)
    model_fit = model.fit()
    return model_fit


def get_residuals(model_fit):
    """
    Extract residuals from trained model.
    """
    return model_fit.resid

def evaluate_arima_model(df_train, df_test, y, arima_order):
  
    """
    Evaluate the forecasting performance of an ARIMA model
    """
  
    train, test = df_train[y].values, df_test[y].values
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=arima_order)
        model.initialize_approximate_diffuse()
        model_fit = model.fit()
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test[t])

    # calculate out of sample error
    mse = mean_squared_error(test, predictions)

    return mse

def evaluate_models(train,valid, y_name, p_values, d_values, q_values):
    """
    Evaluate combinations of p, d and q values for an ARIMA model
    """

    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p,d,q)
                try:
                    mse = evaluate_arima_model(train,valid, y_name, order)
                    if mse < best_score:
                        best_score, best_cfg = mse, order
                        print('ARIMA%s MSE=%.9f' % (order,mse))
                except:
                    continue
    print('Best ARIMA%s MSE=%.9f' % (best_cfg, best_score))


def create_sequences(dataset, time_steps):
    '''
    Random Forest, XGBoost cannot directly model time dependencies.
    Therefore, lagged observations are used as predictors.
    '''
    X, y = [], []
    for i in range(len(dataset) - time_steps):
        X.append(dataset[i:(i + time_steps), 0])
        y.append(dataset[i + time_steps, 0])
    return np.array(X), np.array(y)

