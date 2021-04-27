from sklearn.datasets import load_iris
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

iris = load_iris()

x = iris.data
y = iris.target

x = x[:100, :]
y = y[:100] 

x = (x - np.min(x)) / (np.max(x) - np.min(x))

x_train, x_test, y_train,y_test = train_test_split(x, y, test_size = 0.3)

grid = {"C":np.logspace(-3, 3, 7), "penalty":["l1", "l2"]}  # l1 = lasso ve l2 = ridge

log_reg = LogisticRegression()
log_reg_cv = GridSearchCV(log_reg, grid, cv = 10)
log_reg_cv.fit(x_train, y_train)

print("Tuned hyperparameters(best parameters): ", log_reg_cv.best_params_)
print("Accuracy: ", log_reg_cv.best_score_)

log_reg2 = LogisticRegression(C = 1, penalty = "l2")
log_reg2.fit(x_train, y_train)
print("score: ", log_reg2.score(x_test, y_test))
