from machine import Pin
import time
import _thread
led1=Pin(2,Pin.OUT)
led2=Pin(3,Pin.OUT)
def second_core_function():
    while(1):
           led2.toggle()
           time.sleep(1)
_thread.start_new_thread(second_core_function, ())
while True:
    led1.toggle()    
    time.sleep(0.01)