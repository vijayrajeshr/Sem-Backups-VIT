from machine import Pin
from time import sleep
L1 = Pin("LED", Pin.OUT) # On-board LED
L2 = Pin(2, Pin.OUT)  # On-Kit LED (GPIO2) 
L3 = Pin(3, Pin.OUT)  # On-Kit LED (GPIO3) 
push_button1 = Pin(4, Pin.IN, Pin.PULL_UP) # GPIO 4 pin is input GP4SW1
push_button2 = Pin(5, Pin.IN, Pin.PULL_UP)# GPIO 5 pin is input GP5SW2
while True:
    L1.value(push_button1.value())
    if (not push_button1.value()):
        L1.value(1)
        sleep(0.15)
        L1.value(0)
        sleep(0.15)
    L2.value(push_button2.value())
    if (not push_button2.value()):
        L2.value(1)
        sleep(0.05)
        L3.value(0)
        sleep(0.05)