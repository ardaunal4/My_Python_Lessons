import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def initialize_weights_bias(dimension):

    w = np.full((dimension, 1), 0.01) # number of features
    b = 0.0
    return w, b

def sigmoid(z):

    y_head = 1/(1 + np.exp(-z))
    return y_head

def forward_and_backward_propogation(w, b, x_train, y_train):

    z = np.dot(w.T, x_train) + b
    y_head = sigmoid(z)
    loss = -y_train*np.log(y_head) - (1 - y_train)*np.log(1-y_head) # This is loss formula of propogation
    cost = np.sum(loss)/x_train.shape[1] # x_train.shape is used for normalization of cost

    derivative_weight = (np.dot(x_train, (y_head-y_train).T))/x_train.shape[1]
    derivative_bias = np.sum(y_head - y_train)/x_train.shape[1]
    gradients = {"derivative_weight":derivative_weight, "derivative_bias":derivative_bias}

    return cost, gradients

def update(w, b, x_train, y_train, learning_rate ,number_of_iteration):

    cost_list = []
    cost_list2 = []
    index = []

    for counter in range(number_of_iteration):

        cost, gradients = forward_and_backward_propogation(w, b, x_train, y_train)
        cost_list.append(cost)

        w = w - learning_rate * gradients["derivative_weight"]
        b = b - learning_rate * gradients["derivative_bias"]

        if counter%10 == 0:
            print("{%d}. cost is {%d}", counter, cost)
            index.append(counter)
            cost_list2.append(cost)

    parameters = {"weight":w, "bias":b}

    plt.figure(figsize=(12, 10))
    plt.plot(index, cost_list2)
    plt.xlabel("INDEX")
    plt.ylabel("COST")
    plt.title("COST at Every 10 Iteration")
    plt.show()
    
    return parameters, gradients, cost_list

def prediction(w, b, x_test):

    z = sigmoid(np.dot(w.T, x_test) + b)
    Y_prediction = np.zeros((1, x_test.shape[1]))

    for count in range(z.shape[1]):

        if z[0, count] <= 0.5:
            Y_prediction[0, count] = 0
        else:
            Y_prediction[0, count] = 1
    
    return Y_prediction

def logistic_regression(x_train, y_train, x_test, y_test, learning_rate, number_of_iteration):

    dimension = x_train.shape[0] # number of features
    w, b = initialize_weights_bias(dimension)

    paramaters, gradients, cost_list = update(w, b, x_train, y_train, learning_rate, number_of_iteration)

    y_prediction = prediction(paramaters["weight"], paramaters["bias"], x_train)

    print("Test accuracy = {}%".format(100 - np.mean(np.abs(y_prediction - y_test)) * 100))

def main():

    data = pd.read_csv("C:\\Users\\ardau\\OneDrive\\Masaüstü\\machine_learning\\regression_types\\logistic_regression_classification\\data.csv")

    data.drop(["id", "Unnamed: 32"], axis = 1, inplace = True) # Remove unnecessary features of data
    data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis] # Change object to the integer 
    

    y = data.diagnosis.values # binary classification outputs
    x_data = data.drop(["diagnosis"], axis = 1, inplace = False) # drop output to make database constructed by feature which is necessary for diagnosis
    print(x_data.info())
    x = ((x_data - np.min(x_data))/(np.max(x_data) - np.min(x_data))).values # normalization

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42) # Split data into train and test part

    # Transpose of vectors
    x_train = x_train.T
    x_test = x_test.T
    y_train = y_train.T
    y_test = y_test.T
    
    logistic_regression(x_train, y_train, x_test, y_test, learning_rate = 1, number_of_iteration = 3000)

if __name__ == "__main__":

    main()