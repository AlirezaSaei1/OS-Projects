from multiprocessing import Value, Array, Queue

class Semaphore:
     def __init__(self, count):
         self.val = Value('i', 1)
         self.arr = Array('i', [0] * count)
         self.queue = Queue(count)

     def semWait(self, i):
         self.val.value -= 1
         if self.val.value < 0:
             self.queue.put(i)
             self.arr[i] = 0
             while self.arr[i] != 1:
                 pass

     def semSignal(self, i):
         self.val.value += 1
         if self.val.value <= 0:
             temp = self.queue.get()
             self.arr[temp] = 1
         self.arr[i] = 0
