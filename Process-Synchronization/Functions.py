from time import sleep


def add(num, value):
    tmp = 0
    while True:
        print('Add')
        num.value += value
        tmp = num.value
        sleep(1)
        if tmp != num.value:
            print('Process Conflict! (ADD)')


def sub(num, value):
    tmp = 0
    while True:
        print('Sub')
        num.value -= value
        tmp = num.value
        sleep(1.5)
        if tmp != num.value:
            print('Process Conflict! (SUB)')


def mul(num, value):
    tmp = 0
    while True:
        print('Mul')
        num.value *= value
        tmp = num.value
        sleep(2)
        if tmp != num.value:
            print('Process Conflict! (MUL)')


def div(num, value):
    tmp = 0
    while True:
        num.value /= value
        tmp = num.value
        print(num.value)
        sleep(2.5)
        if tmp != num.value:
            print('Process Conflict! (DIV)')


def show(num):
    while True:
        sleep(0.5)
        print(num.value)
