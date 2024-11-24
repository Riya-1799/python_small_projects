import time
import threading
from threading import Thread

def sleepMe(i):
    print("thread %i will sleep." %i)
    time.sleep(8)
    print("thread %i is awake" %i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print("current thread: %i." % threading.active_count())