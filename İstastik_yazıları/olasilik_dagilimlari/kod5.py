from scipy.stats import poisson
import seaborn as sns
import matplotlib.pyplot as plt

veri = poisson.rvs(mu = 5, size = 730)

plt.figure(figsize = (10, 8))
ax = sns.distplot(veri, kde = True, bins = 15)
#ax.set(xlabel = 'Poisson', ylabel = 'Frekans')
plt.show()