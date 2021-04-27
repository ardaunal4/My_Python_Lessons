import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def main():

    data = pd.read_csv("C:\\Users\\ardau\\OneDrive\\Masaüstü\\machine_learning\\regression_types\\logistic_regression_classification\\data.csv")

    data.drop(["id", "Unnamed: 32"], axis = 1, inplace = True) # Remove unnecessary features of data
    data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis] # Change object to the integer 

    y = data.diagnosis.values # binary classification outputs
    x_data = data.drop(["diagnosis"], axis = 1, inplace = False) # drop output to make database constructed by feature which is necessary for diagnosis
    print(x_data.info())
    x = ((x_data - np.min(x_data))/(np.max(x_data) - np.min(x_data))).values # normalization

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42) # Split data into train and test part

    logistic_reg = LogisticRegression()
    logistic_reg.fit(x_train, y_train) # (455, 30)

    print("Test accuracy = {}".format(logistic_reg.score(x_test, y_test)))

if __name__ == "__main__":
    main()
