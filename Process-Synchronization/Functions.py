from time import sleep


def add(lock, num, value):
    tmp = 0
    while True:
        lock.acquire()

        print(f'Add {num.value} with {value} = {num.value + value}')
        num.value += value
        tmp = num.value
        sleep(1)
        if tmp != num.value:
            print('Process Conflict! (ADD)')

        lock.release()


def sub(lock, num, value):
    tmp = 0
    while True:
        lock.acquire()

        print(f'Subtract {num.value} by {value} = {num.value - value}')
        num.value -= value
        tmp = num.value
        sleep(1.5)
        if tmp != num.value:
            print('Process Conflict! (SUB)')

        lock.release()


def mul(lock, num, value):
    tmp = 0
    while True:
        lock.acquire()

        print(f'Multiply {num.value} by {value} = {num.value * value}')
        num.value *= value
        tmp = num.value
        sleep(2)
        if tmp != num.value:
            print('Process Conflict! (MUL)')

        lock.release()


def div(lock, num, value):
    tmp = 0
    while True:
        lock.acquire()

        print(f'Divide {num.value} by {value} = {num.value / value}')
        num.value /= value
        tmp = num.value
        print(num.value)
        sleep(2.5)
        if tmp != num.value:
            print('Process Conflict! (DIV)')

        lock.release()


def show(lock, num):
    while True:
        lock.acquire()

        sleep(0.5)
        print(num.value)

        lock.release()
