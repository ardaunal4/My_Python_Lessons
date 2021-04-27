# -*- coding: utf-8 -*-
"""
Created on Sun May 10 08:49:14 2020

@author: ardau
"""

""" Inheritance example. Principle of parent and child. 
    Main idea is that when we create parent class which has general methods, these methods can be used by child classes.
    So, it means that parent class has general methods and child classes has specific methods which are interested with child class! """

class Animal(object): # Parent class
    def __init__(self):
        print("Animal has created.")
        
    def walk(self):
        print("Animal has started to walk.")
        
    def toString(self):
        print("Animal")

class Monkey(Animal): # Child class
    def __init__(self):
        super().__init__() # use init method of parent(animal) class
        print("Monkey has created.")
    
    def climb(self):
        print("Monkey can climb.")
    
class Bird(Animal): # Child class
    def __init__(self):
        super().__init__()
        print("Bird has created.")
    
    def fly(self):
        print("Bird can fly.")
    
animal1 = Animal()
print('-----------------')

monkey1 = Monkey()
print('-----------------')
monkey1.walk()
monkey1.toString()
monkey1.climb()
bird1 = Bird()
print('-----------------')
bird1.walk()
monkey1.walk()
bird1.fly()
monkey1.climb()
#%%
bird1.climb()
#%%
""" Inheritance project """
class website:
    # Parent
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def loginInfo(self):
        print(self.name + ' ' + self.surname)
        
class website1(website):
    def __init__(self, name, surname, ids):
        website.__init__(self, name, surname)
        self.ids = ids
        
    def login(self):
        print(self.name + ' ' + self.surname + ' ' + self.ids)
        
user1 = website('name', 'surname')
user1.loginInfo()

user2 = website1('name', 'surname', '123')
user2.login() # from childe class
user2.loginInfo() # from parent class
print(user2.name)