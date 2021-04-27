import numpy as np 
import matplotlib.pyplot as plt
import random

x = np.random.random_integers(10,size=100000)

mean_sample = []

for i in range(10000):
    sample_number = random.randrange(5, 10) # It generates a random number in an given interval (5, 10)
    samples = random.sample(list(x), sample_number) # It takes sample_number times value from the x
    mean_of_samples = np.mean(samples) # Takes means of samples
    mean_sample.append(mean_of_samples)

plt.hist(mean_sample, bins = 50, color = 'blue')
plt.show()