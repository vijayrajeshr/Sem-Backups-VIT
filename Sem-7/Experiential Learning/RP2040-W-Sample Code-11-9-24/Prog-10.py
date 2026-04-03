from machine import Pin
import time
import _thread
sLock = _thread.allocate_lock()
def second_core_function():
    while(1):
        sLock.acquire()
        for x in range(5):
           print("core S",x)
           print(x)
           time.sleep(2)
        sLock.release()
_thread.start_new_thread(second_core_function, ())
while True:
   sLock.acquire()
   for x in range(5):
       print("Core M",x)
       print(x)
       
       time.sleep(2)
   sLock.release()