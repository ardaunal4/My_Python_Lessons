#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:04:39 2020

@author: arda
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv('data.csv')

statistic, p_value = stats.ttest_rel(data.radius_mean, data.area_mean) # Find p value
print('p-value: ', p_value)

