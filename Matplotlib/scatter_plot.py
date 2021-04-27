import matplotlib.pyplot as plt 
import pandas as pd 


df1 = pd.read_csv("/home/arda/Desktop/Code_Examples/Matplotlib/iris.csv")
# print(df1.columns)
df1 = df1.drop("Id", axis = 1)
# print(df1.columns)
unique_species = df1.Species.unique()
# print(unique_species)
setosa = df1[df1.Species == "Iris-setosa"]
versicolor = df1[df1.Species == "Iris-versicolor"]
virginica = df1[df1.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color = "red", label = "setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color = "blue", label = "versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalLengthCm, color = "green", label = "virginica")
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.legend()
plt.show()
