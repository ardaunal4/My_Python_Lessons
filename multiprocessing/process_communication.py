from multiprocessing import Process, Queue

def cube(numbers):
    
    for num in numbers:
        queue.put(num*num*num)

def square(numbers):
    
    for num in numbers:
        queue.put(num*num)


if __name__ == "__main__":
    
    numbers = range(6)
    queue = Queue()

    square_process = Process(target=square, args=(numbers, queue))
    cube_process = Process(target=cube, args=(numbers, queue))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue.empty():
        print(queue.get())