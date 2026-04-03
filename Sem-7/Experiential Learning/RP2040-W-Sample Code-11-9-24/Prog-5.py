from machine import Pin, Timer
from time import sleep
L1 = Pin("LED", Pin.OUT) # On-board LED
L2 = Pin(2, Pin.OUT)  # On-Kit LED (GPIO2) 
L3 = Pin(3, Pin.OUT)  # On-Kit LED (GPIO3) 
push_button1 = Pin(4, Pin.IN, Pin.PULL_UP) # GPIO 4 pin is input GP4SW1
push_button2 = Pin(5, Pin.IN, Pin.PULL_UP)# GPIO 5 pin is input GP5SW2

tim = Timer()#create an instance of Timer method
tim1 = Timer()  #create an another instance of Timer 

def blink(t): L2.toggle()  #function which is toggling the On-board LED
def blink1(t): L3.toggle()  #function which is toggling the On-Kit LED (GPIO2)

tim.init(freq=1, mode=Timer.PERIODIC, callback=blink)
tim1.init(period=100, mode=Timer.PERIODIC, callback=blink1)

# while True:
#     L3.value(1)
#     sleep(1)
#     L3.value(0)
#     sleep(1)
