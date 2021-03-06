import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data = pd.read_csv("data.csv")
data.drop(["id", "Unnamed: 32"], axis = 1, inplace = True)

M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]

# scatter plot
plt.scatter(M.radius_mean, M.texture_mean, color = "red", label = "malignant", alpha = 0.3)
plt.scatter(B.radius_mean, B.texture_mean, color = "green", label = "benign", alpha = 0.3)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()

# Choose vector classification data and normalize features
data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"], axis = 1)
x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data))

# Seperate data into test and train
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

# Train data
svm = SVC(random_state = 1)
svm.fit(x_train, y_train)

# Test data
print("print accuracy of svm algo: ", svm.score(x_test, y_test))