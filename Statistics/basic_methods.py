import numpy as np 
from scipy import stats 


maas = [100,13,44,23,56,13,68]
# Mean
mean_maas = np.mean(maas)
print(mean_maas)

# Median
median_maas = np.median(maas)
print(median_maas)

# Mode
mode = stats.mode(maas)
print(mode)

# Range
range_of_maas = np.max(maas) - np.min(maas)
print(range_of_maas)

# Variance
variance = np.var(maas)
print(variance)

# Standard Deviation
std = np.std(maas)
print(std)