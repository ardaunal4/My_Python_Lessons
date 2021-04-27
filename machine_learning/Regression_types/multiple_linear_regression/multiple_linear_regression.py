import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression

# y = b0 + b1 * x + b2 * x + ......

df = pd.read_csv("C:\\Users\\ardau\\OneDrive\\Masaüstü\\machine_learning\\regression_types\\multiple_linear_regression\\multiple_linear_regression_dataset.csv", sep = ";")

x = df.iloc[:, [0, 2]].values
y = df.maas.values.reshape(-1, 1)
print(x.shape)

multiple_linear_reg = LinearRegression()

model = multiple_linear_reg.fit(x, y)
b0 = model.intercept_
coeff = model.coef_
b1, b2 = coeff[0][0], coeff[0][1]
print(b1, b2)