import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

veri = pd.read_csv('C:\\Users\\ardau\\Downloads\\corrected_data.csv')

range1 = list(veri["RANGE2[V]"])

plt.figure(figsize = (10, 8))
ax = sns.distplot(range1, kde = True, bins = 20)
ax.set(xlabel = 'Bin', ylabel = 'Frekans')
plt.show()