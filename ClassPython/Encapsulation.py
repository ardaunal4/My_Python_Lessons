# -*- coding: utf-8 -*-
"""
Created on Sun May 10 06:22:37 2020

@author: ardau
"""
""" Encapsulation : Restrict to access variables methods.
    We can access private variables with using functions.
    We can access private functions with using functions."""

class BankAccount(object):
    def __init__(self, name, balance, city):
        self.name = name # global variable
        self.__money = float(balance) # private variable
        self.city = city
    
    def getMoney(self):
        return self.__money
    
    def setMoney(self, price):
        self.__money = price
        
    def __AddMoney(self, amount): # Private function
        self.__money += amount
    
    def add_money(self, amount):
        self.__AddMoney(amount)
    

person1 = BankAccount("neymar", 2000, 'sivas')
person1.name = "abdulmuttalip"
try:
    person1.add_money(1512)
except:
    print("olmadi")
    
print(person1.getMoney())
# print(person1.__money())
# person2 = BankAccount('messi', 1000, 'paris')


#print(person1.__money) does not work
# print(person2.getMoney())


