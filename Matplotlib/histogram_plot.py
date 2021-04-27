import pandas as pd 
import matplotlib.pyplot as plt 

df1 = pd.read_csv("iris.csv")
df1 = df1.drop("Id", axis = 1)

setosa = df1[df1.Species == "Iris-setosa"]
versicolor = df1[df1.Species == "Iris-versicolor"]
virginica = df1[df1.Species == "Iris-virginica"]

# print(df1.columns)
plt.hist(setosa.SepalLengthCm,bins=20) #bins means that number of details in the x-axis range
plt.xlabel("cm")
plt.ylabel("frequencies")
plt.title("Histogram")
plt.show()