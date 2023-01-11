from time import sleep

def add(num, value):
    tmp = 0
    while True:
        print('add')
        num.value += value
        tmp = num.value
        sleep(1)
        if tmp != num.value:
            print("Process conflict")