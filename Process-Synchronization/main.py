from multiprocessing import Process, Value, Array, Queue
from Functions import *
from time import sleep

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(2))

    q = Queue()
    p1 = Process(target=add, args=(num, 10))
    p2 = Process(target=sub, args=(num, 5))
    p3 = Process(target=mul, args=(num, 2))
    p4 = Process(target=div, args=(num, 4))

    show = Process(target=show, args=(num,))
    sleep(1)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
