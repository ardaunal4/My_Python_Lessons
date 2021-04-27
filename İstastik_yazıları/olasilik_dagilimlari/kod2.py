from scipy.stats import bernoulli
import seaborn as sns
import matplotlib.pyplot as plt

# Bernoulli dagilimi icin rastgele sayi ureten bir fonksiyon
olay = bernoulli.rvs(size = 1000, p = 0.6) 

plt.figure(figsize = (10, 8))
ax = sns.distplot(olay, kde = False)   
ax.set(xlabel = 'Bernouli', ylabel = 'Frekans')
plt.show()
