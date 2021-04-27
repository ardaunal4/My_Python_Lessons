import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
# y = b0 + b1*x + b2*x^2 + b3*x^3 + ... + bn*x^n

df = pd.read_csv("polynomial_regression.csv", sep=";")

x = df.araba_fiyat.values.reshape(-1, 1)
y = df.araba_max_hiz.values.reshape(-1, 1)

poly_reg = PolynomialFeatures(degree=4) # degree means until x^4
x_trans = poly_reg.fit_transform(x) # it transforms x for Linear regression model according to polynomial regression

linear_reg = LinearRegression()
model = linear_reg.fit(x_trans, y)
y_head = linear_reg.predict(x_trans)

plt.figure(figsize = (10, 8))
plt.scatter(x, y, color  = "blue", label = "Real Data")
plt.plot(x, y_head, color = "green" , label = "Polynomial Regression")
plt.legend()
plt.title("Polynomial Regression")
plt.xlabel("Car Prices")
plt.ylabel("Car Max Speed")
plt.legend()
plt.grid("on")
plt.show()
plt.close()