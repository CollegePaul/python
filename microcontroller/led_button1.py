from machine import Pin
from utime import sleep

led = Pin(5, Pin.OUT)
btn = Pin(6, Pin.IN, Pin.PULL_UP)

while True:

    if (btn.value() == 0): #pressed
        led.value(1)
    else:
        led.value(0)
        
    sleep(0.5)
    
    