from time import sleep


def add(sem, num, value):
    tmp = 0
    while True:
        sem.semWait(0)
        print(f'Add {num.value} with {value} = {num.value + value}')
        num.value += value
        tmp = num.value
        sleep(1)
        if tmp != num.value:
            print('Process Conflict! (ADD)')
        sem.semSignal(0)


def sub(sem, num, value):
    tmp = 0
    while True:
        sem.semWait(1)
        print(f'Subtract {num.value} by {value} = {num.value - value}')
        num.value -= value
        tmp = num.value
        sleep(1.5)
        if tmp != num.value:
            print('Process Conflict! (SUB)')
        sem.semSignal(1)

def mul(sem, num, value):
    tmp = 0
    while True:
        sem.semWait(2)
        print(f'Multiply {num.value} by {value} = {num.value * value}')
        num.value *= value
        tmp = num.value
        sleep(2)
        if tmp != num.value:
            print('Process Conflict! (MUL)')
        sem.semSignal(2)

def div(sem, num, value):
    tmp = 0
    while True:
        sem.semWait(3)
        print(f'Divide {num.value} by {value} = {num.value / value}')
        num.value /= value
        tmp = num.value
        print(num.value)
        sleep(2.5)
        if tmp != num.value:
            print('Process Conflict! (DIV)')
        sem.semSignal(3)

def show(sem, num):
    while True:
        sleep(0.5)
        print(num.value)
