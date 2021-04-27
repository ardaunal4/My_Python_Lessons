import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.linear_model import LinearRegression

data = pd.read_csv('/home/arda/Desktop/Code_Examples/Statistics/linear_regression_dataset.csv', sep = ';')

x = data['deneyim']
y = data['maas']
plt.scatter(x, y, color = 'blue') # normal data


# linear regression model     y = b0 + b1 * x
linear_reg = LinearRegression()

x1 = data.deneyim.values.reshape(-1, 1)
y1 = data.maas.values.reshape(-1, 1)

linear_reg.fit(x1, y1)

b0 = linear_reg.predict(0)
print("b0: ", b0)

b0_ = linear_reg.intercept_
print("b0_: ", b0_)   # y eksenini kestigi nokta intercept

b1 = linear_reg.coef_
print("b1: ", b1)   # egim slope

# maas = 1663 + 1138*deneyim 

maas_yeni = 1663 + 1138*11
print(maas_yeni)
print(linear_reg.predict(11))

y_head = linear_reg.predict(x1)  # maas
plt.plot(x1, y_head, color = "red") # fitting line
plt.show()