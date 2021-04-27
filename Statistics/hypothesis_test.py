import pandas as pd 
import numpy as np 
from scipy import stats
'''
Null Hypothesis = relationship between radius_mean and area_mean is zero in tumor population
Alternate Hypothesis = relationship between radius_mean and area_mean is not zero in tumor population'''

data = pd.read_csv('data.csv')

statistic, p_value = stats.ttest_rel(data.radius_mean, data.area_mean) # Finding p-value
print('p-value = ', p_value) # Since p-value < 0.05 reject hypothesis