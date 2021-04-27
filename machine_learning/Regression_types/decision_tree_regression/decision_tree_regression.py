"""
Decision tree regression uses CART algorithm which is Classification and Regression Trees.
It is useful to use this algorithm when you want to sepcify certain data levels.
"""
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv("decision_tree_regression_dataset.csv", sep = ";")

x = df.iloc[:, 0].values.reshape(-1, 1)
y = df.iloc[:, 1].values.reshape(-1, 1)

dec_tree = DecisionTreeRegressor()

model = dec_tree.fit(x, y)
x_head = np.arange(min(x), max(x), 0.01).reshape(-1, 1)
y_head = model.predict(x_head) 

plt.scatter(x, y, color = "red", label = "Real Data")
plt.plot(x_head, y_head, color = "green", label = "Decision Tree")
plt.legend()
plt.title("Decision Tree Algorithm")
plt.grid("on")
plt.show()