from scipy.stats import binom
import numpy as np 
import matplotlib.pyplot as plt 

# örnegin her saatte ortalama 3 kamyon gorsellestirmesi
lamda = 3
s1 = np.random.poisson(lamda, 100000)
weights1 = np.ones_like(s1) / float(len(s1))
plt.hist(s1, weights = weights1, bins = 100)
plt.xlabel("number of occurances") # grafigin soluna dogru basari azaliyor
plt.ylabel("probability")
plt.show()
# sekilde goruldugu gibi en yuksek olasilik saatte 10 kamyon ama saatte 20 kamyon bile olabilir

