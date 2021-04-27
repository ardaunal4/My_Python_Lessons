import numpy as np 

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# flatten -> transformation of a matrix into a vector 
array1 = array.flatten()
print(array1)
#or
array2 = array.ravel()
print(array2)
