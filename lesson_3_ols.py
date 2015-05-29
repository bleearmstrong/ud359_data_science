# -*- coding: utf-8 -*-

import numpy
import pandas
import scipy
import statsmodels.api as sm


def predictions(weather_turnstile):
 
    data = weather_turnstile[['Hour', 'maxpressurei', 'maxdewpti', 'mindewpti',	'minpressurei',	'meandewpti', 'meanpressurei', 'fog', 'rain', 'meanwindspdi', 'mintempi', 'meantempi', 'maxtempi', 'precipi', 'thunder']]
    values = weather_turnstile[['ENTRIESn_hourly']]
    data = sm.add_constant(data)
    
    est = sm.OLS(values, data)
    est = est.fit()
    prediction = est.predict(data)
    return prediction
