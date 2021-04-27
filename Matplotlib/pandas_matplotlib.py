#Matplotlib intro and pandas review
# subplot, line plot, scatter plot, bar plot, histogram ...

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')

print(df.columns)
 
species = df.Species.unique() # it shows only different(or unique) species in the data
print(species)

info = df.info()
print(info)

description = df.describe() # give us some statistical values 
print(description)

""" ------------line plot ------------------"""

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())

df1 = df.drop(["Id"], axis = 1)
df1.plot(grid = True, linestyle = ":", alpha = 0.5) #alpha is contrast of graph lines
plt.show()

plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa ")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "yellow", label = "versicolor ")
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "yellow", label = "virginica ")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()
