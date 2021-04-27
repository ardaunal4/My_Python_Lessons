import time
from multiprocessing import Process, current_process
import os

def square(list_numbers):
    
    for number in list_numbers:

        time.sleep(0.5)
        result = number*number
        print(f"Square of {number} is equal to {result}")


def main():
    
    processes = []
    numbers = range(100)

    for _ in range(50):
        
        process = Process(target=square, args=(numbers, ))
        processes.append(process)

        process.start()

    for process in processes:

        process.join()

    print("Multiprocessing is completed!")


if __name__ == "__main__":

    main()