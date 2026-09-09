"""
Week 8 Final Project: Florida Housing Analysis and Prediction
Author: Sean Coggeshall

Analyzes Zillow Home Value Index (ZHVI) data for all Florida counties from
2018-2023, generates trend visualizations, and builds per-county linear
regression models using 12-month lag features to predict home values. Outputs
trend plots, actual-vs-predicted charts, and evaluation metrics (MSE, R-squared).
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

OUTPUT_DIR = 'output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# load & filter
df = pd.read_csv('data/fl.csv')
df = df[df['RegionType'].str.lower() == 'county']

# reshape wide→long
id_cols = ['RegionID','SizeRank','RegionName','RegionType',
           'StateName','State','Metro','StateCodeFIPS','MunicipalCodeFIPS']
long = pd.melt(df, id_vars=id_cols, var_name='Date', value_name='ZHVI')
long['Date'] = pd.to_datetime(long['Date'], errors='coerce')
long.dropna(subset=['Date','ZHVI'], inplace=True)
long = long[(long['Date'] >= '2018-01-01') & (long['Date'] <= '2023-12-31')]
long.sort_values(['RegionName','Date'], inplace=True)

counties = long['RegionName'].unique()
results = {}

for county in counties:
    cdf = long[long['RegionName']==county].copy()
    if cdf['ZHVI'].size < 24:
        # too little data to train/predict
        continue

    # summary
    print(f"{county} ZHVI Summary:\n{cdf['ZHVI'].describe()}\n")

    # trend plot
    fn = county.replace(' ','_')
    plt.figure(figsize=(8,4))
    sns.lineplot(x='Date', y='ZHVI', data=cdf)
    plt.title(f'{county} ZHVI (2018–2023)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/{fn}_trend.png')
    plt.close()

    # build lag features
    for lag in range(1,13):
        cdf[f'lag{lag}'] = cdf['ZHVI'].shift(lag)
    cdf.dropna(inplace=True)

    X = cdf[[f'lag{i}' for i in range(1,13)]]
    y = cdf['ZHVI']
    if len(y) < 13:
        continue

    X_train, X_test = X.iloc[:-12], X.iloc[-12:]
    y_train, y_test = y.iloc[:-12], y.iloc[-12:]

    model = LinearRegression().fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2  = r2_score(y_test, y_pred)
    results[county] = (mse, r2)

    # actual vs predicted
    dates = cdf['Date'].iloc[-12:]
    plt.figure(figsize=(8,4))
    plt.plot(dates, y_test,  'o-', label='Actual')
    plt.plot(dates, y_pred, 'x--', label='Predicted')
    plt.title(f'{county} Actual vs Predicted (last 12 mo)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/{fn}_pred.png')
    plt.close()

# final report
print("Model Evaluation:")
for county,(mse,r2) in results.items():
    print(f" {county}: MAE=${np.sqrt(mse):,.2f}, R²={r2:.3f}")

print(f"\nDone! Check all output in ./{OUTPUT_DIR}/")
