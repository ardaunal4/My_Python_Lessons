import os
from multiprocessing import Process, current_process
from time import perf_counter

def square(number):

    result = number*number
    process_id = os.getpid() # assign process by os
    print(f"ID of process is {process_id}") 
    process_name = current_process().name
    print(f"Process name is {process_name}")
    print(f"Square of {number} is equal to {result}")

def main():

    t1 = perf_counter()
    processes = []
    numbers = [1, 2, 3, 4]

    for number in numbers:
        process = Process(target = square, args = (number, ))
        processes.append(Process)
        process.start()
    
    t2 = perf_counter()
    print(f"Process's time is {t2-t1}")

if __name__ == "__main__":

    main()