### **TIME SERIES MODELING OF THE DAILY INFLATION ADJUSTMENT INDEX AND ITS IMPLICATIONS FOR INFLATION MEASUREMENT IN PERU**

Author: Hesler Bustos Chavez   
Project Context: Applied Time Series and Economic Modeling with Python

### Overview

Inflation represents a continuous decrease in the purchasing power of a currency, negatively affecting economic stability. In Peru, its primary indicator is the Consumer Price Index (CPI), calculated monthly by the National Institute of Statistics and Informatics (INEI). Based on this metric, the Central Reserve Bank of Peru (BCRP) establishes the Daily Readjustment Index (IRD), a mathematical factor designed to update financial liabilities in the national currency (soles) for terms of no less than 90 days, aiming to maintain the constant value of these amounts relative to inflation.

This project demonstrates the utility of historical Daily Readjustment Index (IRD) data in reconstructing monthly variations of the Consumer Price Index (CPI). Furthermore, it illustrates how this information enables the analysis of inflationary dynamics and the projection of short-term purchasing power loss. The study combines mathematical formulation, economic interpretation, and computational analysis in Python.

### Problem statement 

Inflation reduces the purchasing power of money and affects economic stability. Inflation is commonly measured by the Consumer Price Index (CPI), which is published monthly. However, the Daily Adjustment Index (DAI) provides daily information that can reflect short-term inflationary dynamics. The problem this project addresses is whether historical DAI data can be used to approximate monthly inflationary behavior and analyze short-term changes in purchasing power.


### Objectives
* Recover monthly CPI inflation rates using continuous daily IRD data.

* Develop and compare alternative time series forecasting models to project the index and assess short-term purchasing power depreciation.

### Data Description
The data used in this project corresponds to the Daily Readjustment Index (IRD) published by the Central Reserve Bank of Peru (BCRP).

* Frequency: Daily
* Source: [BCRP Statistical Database](https://estadisticas.bcrp.gob.pe/estadisticas/series/)
* Period: January 2024 - February 2026

### Methodology
The Daily Readjustment Index (IRD) was analyzed as a time series to model and forecast its behavior. Several forecasting models were implemented, including ARIMA, SARIMA, Random Forest, XGBoost, and Long Short-Term Memory (LSTM). Model performance was evaluated using the metrics MSE, RMSE, MAE, and MAPE, selecting the model with the lowest prediction error.

### Results
Several forecasting models (ARIMA, SARIMA, Random Forest, XGBoost, and LSTM) were evaluated using MSE, RMSE, MAE, and MAPE. SARIMA achieved the best performance, indicating that the IRD series exhibits seasonal patterns effectively captured by this model. On the test set, SARIMA forecasts closely follow the observed values, with most data points falling within the 95% confidence interval demonstrating reliable and consistent predictions.

### Limitations & Future Work

- The recovered inflation depends entirely on the accuracy of the IRD forecast; forecasting errors may propagate directly into the inflation estimates.
- The method assumes that the exponential interpolation structure of the IRD perfectly reflects the CPI dynamics within the month, which may not fully capture short-term price shocks or irregular movements.

Future work:
Future research could explore more advanced models, such as hybrid statistical–machine learning approaches, to further improve forecasting accuracy and robustness.