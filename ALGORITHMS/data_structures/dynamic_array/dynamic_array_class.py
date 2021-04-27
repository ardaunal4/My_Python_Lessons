import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0 # number of elements
        self.capacity = 1 # capacity of array
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Returns number of elements in the array.
        """
        return self.n

    def __getitem__(self, k):
        """
        Returns chosen element in the array.
        """
        if not 0 <= k < self.n:
            return IndexError('It is out of bounds!')

        return self.A[k]
    
    def append(self, element):
        """
        Add element into array.
        """
        if self.n == self.capacity:
            self.__resize(2*self.capacity)

        self.A[self.n] = element
        self.n += 1

    def __resize(self, new_capacity):
        """
        Resize capacity of array.
        """
        B = self.make_array(new_capacity) # create new array
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity
    
    def make_array(self, new_capacity):
        """
        Returns new array.
        """
        return (new_capacity*ctypes.py_object)()