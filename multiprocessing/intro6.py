# Youtube Link: https://www.youtube.com/watch?v=TQx3IfCVvQ0&list=PL5tcWHG-UPH3SX16DI6EP1FlEibgxkg_6&index=6
# Queue : class to communicate between different processes.
from multiprocessing import Process, Queue

def square(numbers, queue):

    for i in numbers:
        queue.put(i*i)

def cube(numbers, queue):

    for i in numbers:
        queue.put(i*i*i)

def main():

    numbers = range(5)
    queue = Queue()

    square_process = Process(target=square, args=(numbers, queue))
    cube_process = Process(target=cube, args=(numbers, queue))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue.empty():
        print("Queue = {}".format(queue.get()))

if __name__ == "__main__":
    main()