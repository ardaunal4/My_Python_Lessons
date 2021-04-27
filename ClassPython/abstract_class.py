from abc import ABC, abstractmethod # abc -> abstract base class

class Animal(ABC): #super class
    
    @abstractmethod # this makes the class abstract
    def walk(self):
        pass
    
    def run(self):
        pass
    # this abstract class is a kind of template for other sub classes

class Bird(Animal): # sub class or child class
    def __init__(self):
        print('bird')

    def walk(self):
        print('walk')
    

obj1 = Animal()
# b1 = Bird()