import pandas as pd 
import numpy as np 
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA # PCA : Principle Component Analysis
# PCA is using for dimension reduction
iris = load_iris()

data = iris.data
feature_names = iris.feature_names
classes = iris.target

df = pd.DataFrame(data = data, columns = feature_names)
df["class"] = classes

# Create PCA Model
pca = PCA(n_components = 2, whiten = True) # Whiten normalizes data
pca.fit(data) # Model is created

data_pca = pca.transform(data) # Apply model on the data

variance_ratio = pca.explained_variance_ratio_ # Variance of data (after apply PCA) with lower dimension
left_data = sum(pca.explained_variance_ratio_) # To see which percentage of data lost in the process.

df["p1"] = data_pca[:, 0]
df["p2"] = data_pca[:, 1]

#%% Visualization
import matplotlib.pyplot as plt

colors = ["green", "blue", "red"]

for each in range(3):
    
    plt.scatter(df.p1[df["class"] == each], df.p2[df["class"] == each], color = colors[each], label = iris.target_names[each])
    
plt.xlabel("p1")
plt.ylabel("p2")
plt.legend()
plt.show()