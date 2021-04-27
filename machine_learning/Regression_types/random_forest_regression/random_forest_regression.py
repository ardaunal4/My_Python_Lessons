# https://www.newgenapps.com/blog/random-forest-analysis-in-ml-and-when-to-use-it/
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

df = pd.read_csv("C:\\Users\\ardau\\OneDrive\\Masaüstü\\machine_learning\\regression_types\\random_forest_regression\\random_forest_regression_dataset.csv", sep=";")

x = df.iloc[:, 0].values.reshape(-1, 1)
y = df.iloc[:, 1].values.reshape(-1, 1)

rand_forest_reg = RandomForestRegressor(n_estimators=100, random_state=42) # n_estimators represents number of trees, random_state is a measure of randomness of trees
model = rand_forest_reg.fit(x, y)

# x_head = np.arange(min(x), max(x), 0.01).reshape(-1, 1) # if we increase number of predictions then we will have more accurate regression!
y_head = model.predict(x)

plt.scatter(x, y, color = "red", label = "Real Data")
plt.plot(x, y_head, color = "green", label = "Random Forest Regression")
plt.title("Random Forest Regression")
plt.legend()
plt.grid("on")
plt.show()

print("R^2 Score of regression = ", r2_score(y, y_head))