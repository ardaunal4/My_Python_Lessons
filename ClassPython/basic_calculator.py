# -*- coding: utf-8 -*-
"""
Created on Sun May 10 05:40:58 2020

@author: ardau
"""

""" Calculator Project """

class calculator(object):
    
    def __init__(self, variable1, variable2 ):
        self.variable1 = variable1
        self.variable2 = variable2
    
    def addition(self):
        return self.variable1 + self.variable2
    
    def multiplication(self):
        return self.variable1 * self.variable2
    
    def division(self):
        return self.variable1 / self.variable2
    
    def subtruction(self):
        return self.variable1 - self.variable2
    

selection = input(" Selections: Addition(1), Multiplication(2), Division(3), Subtriction(4) : ")

v1 = float(input('variable1 = '))
v2 = float(input('variable2 = '))
          

obj1 = calculator(v1, v2)

if selection == "1":
    add_result = obj1.addition()
    print('Addition Result = {}'.format(add_result))
elif selection == "2":
    mult_result = obj1.multiplication()
    print('Multiplication Result = {}'.format(mult_result))
elif selection == "3":
    div_result = obj1.division()
    print('Division Result = {}'.format(div_result))
elif selection == "4":
    sub_result = obj1.subtruction()
    print('Division Result = {}'.format(sub_result))
else:
    print('Wrong choice!')