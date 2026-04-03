import machine
import time
import rp2
# Single pin (base pin) starts at output and logic low
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1) [31]
    nop()        [31]
    nop()        [31]
    nop()        [31]
    nop()        [31]
    set(pins, 0) [31]
    nop()        [31]
    nop()        [31]
    nop()        [31]
    nop()        [31]
    wrap()
# Init state machine with "blink" program
# (state machine 0, running at 2kHz, base pin is GP2 (LED))
sm = rp2.StateMachine(0, blink, freq=2000, set_base=machine.Pin(2))
sm.active(1) # Start State Machine 1
#time.sleep(3)
#sm.active(0) # Start State Machine 1

