import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

df1 = pd.read_csv("iris.csv")
# print(df1.columns)
# df1 = df1.drop("Id", axis = 1)

# df1.plot(grid = True, alpha = 0.9, subplots = True)
# plt.show()

setosa = df1[df1.Species == "Iris-setosa"]
versicolor = df1[df1.Species == "Iris-versicolor"]
virginica = df1[df1.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")
plt.ylabel("setosa - petallenght")

plt.subplot(2,1,2)
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "blue", label = "versicolor")
plt.ylabel("versicolor - petallenght")
plt.show()