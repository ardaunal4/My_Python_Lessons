import numpy as np 
import random

array1 = np.array([[1, 2, 3], [7, 8, 9]])
array2 = np.array([[4, 5, 6], [10, 11, 12]])

print(array1 + array2)
print(array1 * array2)
print(array2 - array1)
print(array1 ** 2)
print(np.sin(array1)) # sinus of elements of array1
print(array1 < 2)

# element wise production
print(array1 * array2)

#matrix product
print(array1.dot(array2.T)) # array2.T -> transpose of array2

print(np.exp(array1)) # exponential of the elements of the matrix

print(np.random.random((5, 5))) # 5x5 random(between 0 and 1) elements matrix

#some useful funtions
print(array1.sum())
print(array1.max())
print(array1.min())

print(array1.sum(axis = 0))  # it reduce row numbers by summing elements in a column
print(array1.sum(axis=2)) # reverse of the upper function

print(np.sqrt(array1))
print(np.square(array1)) # array1 ** 2