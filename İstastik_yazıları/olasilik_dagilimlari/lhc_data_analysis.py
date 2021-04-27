import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates  

data = pd.read_csv("corrected_data.csv")
adc24bit = data["24bit[bin]"].values

plt.figure(figsize = (10, 8))
ax = sns.distplot(adc24bit, kde = True, bins = 20)
ax.set(xlabel = 'Bin', ylabel = 'Frekans')
plt.show()