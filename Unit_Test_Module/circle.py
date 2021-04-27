#we can test our code with using unit test module
from math import pi

def circle_area(r):
    """my circle function"""
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number! ")
    if r < 0:
        raise ValueError("The radius can not be negative ! ")
    return pi*(r**2)

