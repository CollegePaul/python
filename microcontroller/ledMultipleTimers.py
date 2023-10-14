from machine import Pin, Timer
import random

ledFlash = Pin(15, Pin.OUT) #20 on board
ledSlow = Pin(14, Pin.OUT) #19 on board
ledFlicker = Pin(13, Pin.OUT) #17 on board
ledon = Pin(12, Pin.OUT) #26 on board

timer = Timer()
timerSlow = Timer()
timerFlicker= Timer()
ledon.value(1)
ledSlow.value(1)
ledFlicker.value(1)

def blink(timer):
    ledFlash.toggle()

def blinkSlow(timerSlow):
    ledSlow.toggle()
    
def Flicker(timerSlow):
    n = random.randint(1,6)
    if n <2:
        ledFlicker.toggle()
    
    
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
timerSlow.init(freq=0.5, mode=Timer.PERIODIC, callback=blinkSlow)
timerFlicker.init(freq=100, mode=Timer.PERIODIC, callback=Flicker)
