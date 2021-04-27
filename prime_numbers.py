import time # Measure time in processing 

def is_prime_v1(n):
    """ Return 'True' in n is prime number otherwise 'False' """
    if n == 1:
        return False 
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
        
# ==========Time Function=============
t = time.time()
for n in range(1, 20):
    print(n, is_prime_v1(n))

t1 = time.time()
print("Time required = ", t1 - t)