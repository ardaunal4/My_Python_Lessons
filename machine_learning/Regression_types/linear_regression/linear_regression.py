import  pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

"""
The coefficient of determination is the square of the correlation (r) between predicted y scores and actual y scores; thus, it ranges from 0 to 1. 
With linear regression, the coefficient of determination is also equal to the square of the correlation between x and y scores.

The mean squared error tells you how close a regression line is to a set of points. It does this by taking the distances from the points to the regression 
line (these distances are the “errors”) and squaring them. The squaring is necessary to remove any negative signs.
"""

df = pd.read_csv("C:\\Users\\ardau\\OneDrive\\Masaüstü\\machine_learning\\regression_types\\linear_regression_dataset.csv", sep = ";")

linear_reg = LinearRegression() # this is an object of Linear regression subclass

x = df.deneyim.values.reshape(-1, 1)
y = df.maas.values.reshape(-1, 1)

linear_reg.fit(x, y) # Fit linear regression line into data
# y = b1 * x + b0
b0 = linear_reg.intercept_ # is intercept point of y when x = 0
b1 = linear_reg.coef_ # is slope of the linear regression line

y_head = linear_reg.predict(x)

coeficient_of_determination =  r2_score(y, y_head)
cod_text = "COD = " + str(coeficient_of_determination)

mean_squared_err = mean_squared_error(y, y_head)
mse_text = "MSE = " + str(mean_squared_err)

fig = plt.figure(figsize = (12, 10))
plt.scatter(x, y, color = "blue", label = "Real Data")
plt.plot(x, y_head, color = "red", label = "Liner Regression")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.grid("on")
plt.title("Experience vs Salary")
plt.legend()
plt.show()
plt.close()