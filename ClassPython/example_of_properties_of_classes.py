# -*- coding: utf-8 -*-
"""
Created on Wed May 27 02:35:30 2020

@author: ardau
"""
from abc import ABC, abstractmethod
from cmath import pi

class shape(ABC):
    """
    Parent class / abstract class example
    """    
    # abstract methods
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
    # overriding and polymorphism
    def toString(self):
        pass
    
class square(shape):
    
    def __init__(self, edge):
        self.__edge = edge # encapsulation or with other mean private attribute
        
    def area(self):
        area = self.__edge ** 2
        print('Square area = ', area)
    
    def perimeter(self):
        perimeter = self.__edge * 4
        print('Perimeter of square = ', perimeter)
        
    def toString(self):
        print('Square edge = ', self.__edge)

class circle(shape):
    
    def __init__(self, radius):
        self.__radius = radius
    
    def area(self):
        area = pi * self.__radius ** 2
        print('circle area = ', area)
        
    def perimeter(self):
        perimeter = 2 * pi * self.__radius
        print("perimeter of circle = ", perimeter)
        
    def toString(self):
        print('Circle radius = ', self.__radius)
        
c = circle(5)
c.toString()
c.area()
c.perimeter()

s = square(5)
s.toString()
s.area()
s.perimeter()



        