from multiprocessing import Process, Value, Array, Queue, Lock
from Functions import *
from time import sleep

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(2))
    lock = Lock()

    q = Queue()
    p1 = Process(target=add, args=(lock, num, 10))
    p2 = Process(target=sub, args=(lock, num, 5))
    p3 = Process(target=mul, args=(lock, num, 2))
    p4 = Process(target=div, args=(lock, num, 4))

    show = Process(target=show, args=(lock, num,))
    sleep(1)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
