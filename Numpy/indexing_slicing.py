import numpy as np 

array1 = np.array([1, 2, 3, 4, 5, 6, 7])

print(array1[0])
print(array1[0:4])

reverse_array = array1[::-1] #reversed array
print(reverse_array)

array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array2[1, 1])
print(array2[:, 1])
print(array2[1, :])
print(array2[1, 1:4])
print(array2[-1, :])