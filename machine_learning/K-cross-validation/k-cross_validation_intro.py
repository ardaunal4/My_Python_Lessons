import pandas as pd 
import numpy as np 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

iris = load_iris()

x = iris.data
y = iris.target

x = (x - np.min(x)) / (np.max(x) - np.min(x))

x_train, x_test, y_train, y_test = train_test_split(x, y)

knn = KNeighborsClassifier(n_neighbors = 3)

accuracies = cross_val_score(estimator = knn, X = x_train, y = y_train, cv = 10) # 10 different seperation for cross validation
print("Average accuracy = ", np.mean(accuracies))
print("STD of accuracy = ", np.std(accuracies))

knn.fit(x_train, y_train)
y_predict = knn.predict(x_test)
print("Score of model = ", knn.score(x_test, y_test))
