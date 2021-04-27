from scipy.stats import binom
import seaborn as sns
import matplotlib.pyplot as plt

""" 
Bernoulli dagilimi icin rastgele sayi ureten bir fonksiyon yazalim.
Burada 10 bir deneyde kac tane kart cektigimizin sayisi.
p ise olma olasiligi.
Size ise kac kere bu deneyi tekrarladigimizin sayisi
"""
olay = binom.rvs(n = 10, p = 1/2, size = 100) 

plt.figure(figsize = (10, 8))
ax = sns.distplot(olay, kde = False)   
ax.set(xlabel = 'Binomial', ylabel='Frekans')
plt.show()