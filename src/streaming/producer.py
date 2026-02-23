# we are going to first load the log to queue and then by using the consumer function we will take out the log 
import threading
from queue import Queue 
my_queue=Queue()

def publish (message):
    my_queue.put(message)
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
   
thread2 =threading.Thread(target=waiter)
thread1.start()
thread1.join()
thread2.start()
thread2.join()



