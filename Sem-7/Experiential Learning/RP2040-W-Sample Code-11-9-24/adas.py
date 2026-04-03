from machine import Pin, PWM
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

# Buzzer setup (GPIO 6)
buzzer = PWM(Pin(6))
buzzer.freq(2000)  # tone frequency

def get_distance():
    """Measure distance using the ultrasonic sensor"""
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()

    # Wait for echo start
    timeout_start = utime.ticks_us()
    while echo.value() == 0:
        if utime.ticks_diff(utime.ticks_us(), timeout_start) > 30000:
            return None
        signaloff = utime.ticks_us()

    # Wait for echo end
    timeout_start = utime.ticks_us()
    while echo.value() == 1:
        if utime.ticks_diff(utime.ticks_us(), timeout_start) > 30000:
            return None
        signalon = utime.ticks_us()

    # Calculate distance in cm
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

def beep(duration_ms, duty):
    """Soft beep with adjustable loudness"""
    buzzer.duty_u16(duty)  # lower duty = softer sound (0–65535)
    utime.sleep_ms(duration_ms)
    buzzer.duty_u16(0)

while True:
    distance = get_distance()

    lcd.clear()
    lcd.move_to(0, 0)

    if distance is None:
        lcd.putstr("No echo detected")
        buzzer.duty_u16(0)
        utime.sleep(0.5)
        continue

    lcd.putstr("Dist: " + str(round(distance, 1)) + " cm")
    lcd.move_to(0, 1)
    lcd.putstr("Parking Assist")

    # Smart buzzer response
    if distance > 50:
        buzzer.duty_u16(0)  # silent
        utime.sleep(1)
    elif 30 < distance <= 50:
        beep(70, 500)   # low volume, slow beep
        utime.sleep(0.8)
    elif 15 < distance <= 30:
        beep(70, 1500)  # medium volume, faster beep
        utime.sleep(0.4)
    elif 8 < distance <= 15:
        beep(80, 3000)  # louder, rapid beep
        utime.sleep(0.2)
    else:  # Very close (<8 cm)
        # Continuous loud warning
        buzzer.duty_u16(6000)
        lcd.clear()
        lcd.putstr("!!! STOP !!!")
        lcd.move_to(0, 1)
        lcd.putstr("Too Close!")
        utime.sleep(0.5)
        buzzer.duty_u16(0)
        utime.sleep(0.1)
