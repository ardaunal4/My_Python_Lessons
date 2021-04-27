#With memorization mehod we can write our Fibonacci sequence more easy way
from functools import lru_cache #Least recently used cache

@lru_cache(maxsize = 1000)
def Fibonacci(n):
    #check that input is positive integer
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise TypeError("n must be a positive integer")

    #Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1 
    elif n > 2:
        return Fibonacci(n-1) + Fibonacci(n-2)

for n in range(1,500):
    print(n,":",Fibonacci(n))

