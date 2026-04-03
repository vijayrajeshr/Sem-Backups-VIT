from machine import Pin
import time
import _thread

led1 = Pin(2, machine.Pin.OUT)
led2 = Pin(3, machine.Pin.OUT)

sLock = _thread.allocate_lock()
def CoreTask():
    while True:
        sLock.acquire()
        for x in range(5):
           print("cores",x)
           print(x)
           time.sleep(0.1)
        sLock.release()
_thread.start_new_thread(CoreTask, ())

while True:
    sLock.acquire() # Acquire the semaphore lock
    for x in range(5,9):
           print("corem",x)
           print(x)
           time.sleep(0.1)
    sLock.release() # Release the semaphore lock

