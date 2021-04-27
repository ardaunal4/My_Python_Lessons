from scipy.stats import binom
import numpy as np 
import matplotlib.pyplot as plt 

# yazı tura
n = 2 # number of trials
p = 0.5 # probability of each trial
s = np.random.binomial(n, p, 10000) # 10000 = number of test
weights = np.ones_like(s) / float(len(s))
plt.hist(s, weights = weights)
plt.xlabel("number of success") # grafigin soluna dogru basari azaliyor
plt.ylabel("probability")
plt.show()
# 0.25 prob 0 success (2 yazı)
# 0.5 prob 1 success  (yazı-tura)
# 0.25 prob 2 success (2 tura)
# (yazı-yazı)(yazı-tura)(tura-yazı)(tura-tura)

# Bir zar 10 kez atiliyor. 4 kere 6 gelme olasiligi nedir?

n = 10 # number of trial
p = 1 / 6 # probability of success in each event
r = 4 # number of success

probability = binom.pmf(r, n, p)
print(probability)

