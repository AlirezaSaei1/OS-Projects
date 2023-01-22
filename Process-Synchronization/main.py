from multiprocessing import Process, Value, Array, Queue
from Functions import *
from time import sleep
from Sem import Semaphore
if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(2))
    sem = Semaphore(4)

    q = Queue()
    p1 = Process(target=add, args=(sem, num, 10))
    p2 = Process(target=sub, args=(sem, num, 5))
    p3 = Process(target=mul, args=(sem, num, 2))
    p4 = Process(target=div, args=(sem, num, 4))

    show = Process(target=show, args=(sem, num,))
    sleep(1)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
