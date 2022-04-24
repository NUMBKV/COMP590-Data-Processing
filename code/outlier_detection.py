#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
from sklearn import preprocessing, ensemble
from prophet import Prophet


# def get_median_filtered(signal, window_size=3):
#     result = []
#     for idx in range(len(signal)-window_size):
#         result.append(np.median(signal[idx:idx+window_size]))
#     return result


def get_rolling_median_filtered(signal, window_size=3, threshold=8):
    """
    Input: 
        signals: List of numbers 
        window_size: Integer, window size that calculate median from
        threshold: Integer, the difference between calculate median and given 
                    value that will be considered as an outlier
    
    Output: List of numbers that represent the index of outlier
    """
    result = pd.Series(signal).rolling(window_size).median().fillna(method='bfill') 
    difference = np.abs(result - signal)
    outlier = difference > threshold
    outlier_index = outlier[outlier].index.values
    return outlier_index


def cart_outlier(signal, fraction = 0.05):
    """
    Input: 
        signals: List of numbers
        fraction: Float, the portion of data that we will be considered as outliers
    
    Output: List of numbers that represent the index of outlier
    """
    scaler = preprocessing.StandardScaler()
    signal_scaled = scaler.fit_transform(np.array(signal).reshape(-1, 1))
    data = pd.DataFrame(signal_scaled)
    model = ensemble.IsolationForest(contamination=fraction)
    model.fit(data)
    outlier = model.predict(data)
    outlier_index = np.where(outlier == -1)[0]
    return list(outlier_index)


def prophet_prediction(signal, date):
    """
    Input:
        signals: List of numbers
        date: List of strings, ex: ['1/22/20', '1/23/20', ...]
    
    Output: List of numbers that represent the index of outlier
    """
    model = Prophet(daily_seasonality = False, yearly_seasonality = False, 
                    weekly_seasonality = False,
                    seasonality_mode = 'additive')
    df = pd.DataFrame(list(zip(date, list_)), columns=['ds','y'])
    model.fit(df)
    forecast = model.predict(df)
    forecast['fact'] = df['y'].reset_index(drop = True)
    forecast['anomaly'] = 0
    forecast.loc[forecast['fact'] > forecast['yhat_upper'], 'anomaly'] = 1
    forecast.loc[forecast['fact'] < forecast['yhat_lower'], 'anomaly'] = -1
    outlier_index = forecast[forecast['anomaly'] != 0].index
    return list(outlier_index)



if __name__ == "__main__" : 
    file = "/Users/seanlin/Desktop/Rice/2022Spring/COMP590/COMP590-Data-Processing-main/daily_cases/new_daily_states_county/confirmed_cases_texas.csv"
    data = pd.read_csv(file)
    list_ = list(data.loc[0]['1/22/20':])
    date = list(data.loc[:, '1/22/20':].columns)
    

    rolling_median_outlier_idx = get_rolling_median_filtered(list_, 3, 30)
    print(rolling_median_outlier_idx)

    cart_outlier_idx = cart_outlier(list_)
    print(cart_outlier_idx)
   
    prophet_outlier_idx = prophet_prediction(list_, date)
    print(prophet_outlier_idx)






