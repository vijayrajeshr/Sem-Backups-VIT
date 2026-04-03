from machine import Pin
from time import * 
L1 = Pin("LED", Pin.OUT)    # On-board LED
L2 = Pin(2, Pin.OUT)  # On-Kit LED (GPIO2) 
L3 = Pin(3, Pin.OUT)  # On-Kit LED (GPIO3) 
while True:
    x=3
    #L1.value(1)
    #L2.value(1)
    L3.value(1)     
    #sleep_ms(100) # Delay 0.1 second
    sleep_ms(x) # Delay x second 
    #L1.value(0)
    #L2.value(0)
    L3.value(0)
    #sleep_ms(100) # Delay 0.1 second
    sleep_ms(20-x) # Delay (20-x) second

