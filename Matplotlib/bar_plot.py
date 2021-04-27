import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = 2*x + 5

plt.bar(x, y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
