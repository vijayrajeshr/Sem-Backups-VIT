from machine import Pin, Timer
from time import sleep
L1 = Pin("LED", Pin.OUT) # On-board LED
L2 = Pin(2, Pin.OUT)  # On-Kit LED (GPIO2) 
L3 = Pin(3, Pin.OUT)  # On-Kit LED (GPIO3) 
push_button1 = Pin(4, Pin.IN, Pin.PULL_UP) # GPIO 4 pin is input GP4SW1
push_button2 = Pin(5, Pin.IN, Pin.PULL_UP)# GPIO 5 pin is input GP5SW2
tim = Timer()#create an instance of Timer method
global button

def blink(t): #function which is toggling the led
    if (push_button1.value()==0):   
      L1.toggle()
      L1.value(2-2)
      sleep(0.2)
      L1.value(0)
      sleep(0.2)

tim.init(freq=2, mode=Timer.PERIODIC, callback=blink)

while True:
    L2.value(1)
    sleep(1)
    L2.value(0)
    sleep(1)
