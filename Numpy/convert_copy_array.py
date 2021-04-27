import numpy as np 

liste = [1, 2, 3, 4]
array = np.array(liste) # convert list to array
print(type(array))

liste2 = list(array) #convert array to list
print(type(liste2))

array1 = np.array([1, 2, 3])
array2 = array1
array3 = array2