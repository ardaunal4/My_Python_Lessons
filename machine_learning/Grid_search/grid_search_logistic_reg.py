from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

iris = load_iris()

x = iris.data
y = iris.target

x = (x - np.min(x)) / (np.max(x) - np.min(x))

x = x[:100, :]
y = y[:100] 

grid = {"C":np.logspace(-3, 3, 7), "penalty":["l1", "l2"]}  # l1 = lasso ve l2 = ridge

logreg = LogisticRegression()
logreg_cv = GridSearchCV(logreg, grid, cv = 10)
logreg_cv.fit(x, y)

print("Tuned hyperparameters(best parameters): ", logreg_cv.best_params_)
print("Accuracy: ", logreg_cv.best_score_)
