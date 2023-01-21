from time import sleep


def add(sem, num, value):
    tmp = 0
    while True:
        with sem:
            print(f'Add {num.value} with {value} = {num.value + value}')
            num.value += value
            tmp = num.value
            sleep(1)
            if tmp != num.value:
                print('Process Conflict! (ADD)')


def sub(sem, num, value):
    tmp = 0
    while True:
        with sem:
            print(f'Subtract {num.value} by {value} = {num.value - value}')
            num.value -= value
            tmp = num.value
            sleep(1.5)
            if tmp != num.value:
                print('Process Conflict! (SUB)')


def mul(sem, num, value):
    tmp = 0
    while True:
        with sem:
            print(f'Multiply {num.value} by {value} = {num.value * value}')
            num.value *= value
            tmp = num.value
            sleep(2)
            if tmp != num.value:
                print('Process Conflict! (MUL)')


def div(sem, num, value):
    tmp = 0
    while True:
        with sem:
            print(f'Divide {num.value} by {value} = {num.value / value}')
            num.value /= value
            tmp = num.value
            print(num.value)
            sleep(2.5)
            if tmp != num.value:
                print('Process Conflict! (DIV)')


def show(sem, num):
    while True:
        with sem:
            sleep(0.5)
            print(num.value)
