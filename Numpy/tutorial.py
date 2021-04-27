import numpy as np 

array = np.array([1,2,3,4])
print(array)
print(array.shape)

array1 = array.reshape(2,2)
print("shape of a = ",array1.shape)
print("dimension = ", array1.ndim)
print("data type = ",array1.dtype.name)
print("size: ", array1.size)

array2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Create zeros
array3 = np.zeros((3,3))
print(array3)
array3[0,0] = 5
print(array3)

#create ones
array4 = np.ones((3,4))
print(array4)

#create empty
array5 = np.empty((4,4))
print(array5)

# Create a sequence
array6 = np.arange(10,50,5) # it starts from 10 and goes 45 with increasing 5
print(array6)

# division the range with signed number
array7 = np.linspace(10,50,20) # it divide 20 equal space of the range of 10 to 50
print(array7)