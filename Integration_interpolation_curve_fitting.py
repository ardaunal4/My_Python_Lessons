import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab
from scipy.integrate import * # "quad" function

# Integration:

def f(x):# first define function
    return 3.0*x*x + 1.0

I, error = quad(f, 0, 1) # Integration from 0 to 1
print(I)
print(error)





