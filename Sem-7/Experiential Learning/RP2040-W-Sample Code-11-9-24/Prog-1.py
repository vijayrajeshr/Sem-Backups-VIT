from machine import Pin
from time import sleep
L1 = Pin("LED", Pin.OUT)    # On-board LED
L2 = Pin(2, Pin.OUT)  # On-Kit LED (GPIO2) 
L3 = Pin(3, Pin.OUT)  # On-Kit LED (GPIO3) 
while True:
    L1.toggle()
    #L2.toggle()
    #L3.toggle()
    sleep(1)