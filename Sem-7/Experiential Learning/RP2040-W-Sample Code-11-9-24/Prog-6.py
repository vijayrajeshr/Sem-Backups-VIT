from machine import Pin, PWM
from time import sleep

L2 = PWM(Pin(2))
L3 = PWM(Pin(3))
L2.freq(100)
L3.freq(100)

while True:    
    for duty in range(0,65535):
        L2.duty_u16(duty)
        L3.duty_u16(65535-duty)
        sleep(0.0001)
    sleep(1)   
    for duty in range(65535,0,-1):
        L2.duty_u16(duty)
        L3.duty_u16(65535-duty)
        sleep(0.0001)
    sleep(1)