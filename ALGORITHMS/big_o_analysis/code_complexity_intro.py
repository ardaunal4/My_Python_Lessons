# CODE COMPLEXITY : is a measure of optimization of time of running algorithm.
# As an example, 2 seperate function with same duty
import time

def square_sum_loop(n):

    sum = 0
    for count in range(1, n+1):
        sum += count**2
    
    return sum

def square_sum_formula(n):

    return (n*(n+1)*(2*n+1)/2)


def main():

    t1 = time.perf_counter()
    square_sum_loop(15)
    t2 = time.perf_counter()
    print("Performance of loop function :", t2-t1)

    t1 = time.perf_counter()
    square_sum_formula(15)
    t2 = time.perf_counter()
    print("Performance of formula function :", t2-t1)

if __name__ == "__main__":
    main()