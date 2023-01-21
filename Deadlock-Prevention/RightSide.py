from multiprocessing import Process, Queue, Value, Array
from time import sleep
from Car import Car


def producer(sem, queue, id, ):
    print('Producer: Running', flush=True)
    while True:
        value = Car(id.value)
        id.value += 1
        sleep(0.5)
        queue.put(value)


def consumer(sem, queue, street):
    print('Consumer: Running', flush=True)
    while True:
        with sem:
            item = queue.get()
            street.value = item.id
            print('car id: ', item.id, 'sleep: ', item.time)
            temp = street.value
            sleep(item.time)
            if temp != street.value:
                print('Process conflict!')
