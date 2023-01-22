from multiprocessing import Value, Array, Queue

class Semaphore:
     def __init__(self, count):
         self.val = Value('i', 1)
         self.arr = Array('i', [0] * count)
         self.queue = Queue(count)

     def semWait(self, i):
         self.val.value -= 1
         if self.val.value < 0:
             self.arr[i] = 0
             self.queue.put(i)

             while True:
                 if self.arr[i] == 1:
                     break

     def semSignal(self, i):
         self.val.value += 1
         if self.val.value <= 0:
             j = self.queue.get()
             self.arr[j] = 1
         self.arr[i] = 0
