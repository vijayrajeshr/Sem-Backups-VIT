from machine import Pin
from gpio_lcd import GpioLcd
import utime

# LCD setup
lcd = GpioLcd(rs_pin=Pin(8),
              enable_pin=Pin(9),
              d4_pin=Pin(10),
              d5_pin=Pin(11),
              d6_pin=Pin(12),
              d7_pin=Pin(13))

# Ultrasonic sensor pins
trigger = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)

# Main loop
while True:
    # Send trigger pulse
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()

    # Wait for echo
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()

    # Calculate distance
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2

    # Display on LCD
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Distance: " + str(round(distance, 1)) + " cm")
    lcd.move_to(0, 1)
    lcd.putstr("Sensor Active")

    # Small delay before next measurement
    utime.sleep(1)
