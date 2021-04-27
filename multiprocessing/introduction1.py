from multiprocessing import Pool
import time


def f(x):
    #time.sleep(1)
    return x*x

def main():
    t1 = time.perf_counter()

    with Pool(3) as p:
        print(p.map(f, [1, 2, 3]))

    t2 = time.perf_counter()
    print("Result time : {}".format(t2-t1))

if __name__ == '__main__':
    main()