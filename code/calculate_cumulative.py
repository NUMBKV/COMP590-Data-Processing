#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:43:51 2022

@author: seanlin
"""

import pandas as pd
import numpy as np
import glob




for file in glob.glob('../remove_outlier_cases/*/*.csv'):
    print(file)
    ori_data = pd.read_csv(file)
    method = file.split('/')[-2]
    state = file.split('/')[-1].split('.csv')[0].split('_')[-1]
    date = '1/22/20'
    remain_part = ori_data.iloc[:, :ori_data.columns.get_loc(date)]
    detect_part = ori_data.loc[:, date:]

    for row in range(len(detect_part)):
        series = detect_part.iloc[row, :]
        series = np.cumsum(series)
        detect_part.iloc[row, :] = series
    result = pd.concat([remain_part, detect_part], axis=1, join="inner")
    file_name = '../cumulative_remove_outlier_cases/' + method + '/cumulative_remove_outlier_' + state + '.csv'
    result.to_csv(file_name, index = False)

    
    
    