# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:59:22 2020

@author: ardau
"""
#%%
# First class example
class area(object):
    edge = 5 
    square = 0
    def square(self):
        self.square = self.edge * self.edge
        print(self.square)
         
first_object = area()
print(first_object.edge)
first_object.edge = 10
first_object.square()
#%%

class employee(object):
    age = 25
    salary = 1000
    def ratio(self):
        print(self.age / self.salary)
        
obj1 = employee()
obj1.ratio()
#%%
#Initializer or constructor

class animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getAge(self):
        return self.age
    
    def getName(self):
        print(self.name)
        
obj1 = animal('cat', 2)
obj1.getName()
    