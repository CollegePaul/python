from machine import Pin,Timer
import random

class Blink_Led:
    def __init__(self, pin, frequency):
        self.led= Pin(pin, Pin.OUT)  
        self.timer = Timer()
        self.timer.init(freq=frequency, mode=Timer.PERIODIC, callback=self.blink)
        
    def blink(self,timer):
        self.led.toggle()
        
        
class Strobe_Led:
    def __init__(self, pin, frequency, chance):
        self.led= Pin(pin, Pin.OUT)
        self.chance = chance
        self.timer = Timer()
        self.timer.init(freq=frequency, mode=Timer.PERIODIC, callback=self.blink)
        
    def blink(self,timer):
        s = random.randint(0,9) 
        if s < self.chance:
            self.led.toggle()

#requires 2 LED's
class Flip_Led:
    def __init__(self, pin,pin2, frequency):
        self.led= Pin(pin, Pin.OUT)
        self.led2= Pin(pin2, Pin.OUT)
        self.led.value(0)
        self.led2.value(1)
        self.timer = Timer()
        self.timer.init(freq=frequency, mode=Timer.PERIODIC, callback=self.blink)
        
    def blink(self,timer):
        self.led.toggle()
        self.led2.toggle()
