from time import sleep
import _thread
spLock = _thread.allocate_lock() 

def core0_thread():
    while True:
        spLock.acquire() 
        print('C')
        sleep(0.5)
        print('O')
        sleep(0.5)
        print('R')
        sleep(0.5)
        print('E')
        sleep(0.5)
        print('0')
        sleep(0.5)
        spLock.release()
def core1_thread():
    while True:
        spLock.acquire() 
        print('c')
        sleep(0.5)
        print('o')
        sleep(0.5)
        print('r')
        sleep(0.5)
        print('e')
        sleep(0.5)
        print('1')
        sleep(0.5)
        spLock.release()
second_thread = _thread.start_new_thread(core1_thread, ())

core0_thread()
