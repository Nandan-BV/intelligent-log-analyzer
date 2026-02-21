
import threading
from queue import Queue
my_queue=Queue()

def publish (message):
    my_queue.put(message)

def consume():
    if my_queue.empty():
        print("the queue is empty")
    else:
     message=my_queue.get()
     return message 
def chef():
   publish("burger")
   publish("pizza")
   publish("pasta")
def waiter():
   print(consume())
   print(consume())
   print(consume())


thread1 =threading.Thread(target=chef)
thread2 =threading.Thread(target=waiter)
thread1.start()
thread1.join()
thread2.start()
thread2.join()
