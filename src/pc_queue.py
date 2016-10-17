# pc_queue.py
#
# An example of using queues to set up producer/consumer problems

import threading
import time
import Queue

# A queue of items being produced

items = Queue.Queue()

# A producer thread
def producer():
    print "I'm the producer"
    for i in range(30):
        items.put(i)
        time.sleep(1)
        
# A consumer thread
def consumer():
    print "I'm a consumer", threading.currentThread().name
    while True:
        x = items.get() 
        print threading.currentThread().name,"got", x
        time.sleep(5)
    

# Launch a bunch of consumers
cons = [threading.Thread(target=consumer)
        for i in range(10)]
for c in cons:
    c.setDaemon(True)
    c.start()

# Run the producer
producer()



        
