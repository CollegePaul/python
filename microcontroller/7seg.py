from machine import Pin
from utime import sleep
sleep(0.1) # Wait for USB to become ready

print("Pico counter is running")

btn = Pin(10, Pin.IN, Pin.PULL_UP)
current_digit = 0
pressed = False

a = Pin(1, Pin.OUT)
b = Pin(2, Pin.OUT)
c = Pin(3, Pin.OUT)
d = Pin(4, Pin.OUT)
e = Pin(5, Pin.OUT)
f = Pin(6, Pin.OUT)
g = Pin(7, Pin.OUT)
leds = (a,b,c,d,e,f,g)

def all_off():
  for led in leds:
    led.value(0) #off

all_off()

numbers = [
  [a,b,c,d,e,f],      #0
  [b,c],
  [a,b,d,e,g],
  [a,b,c,d,g],
  [b,c,f,g],
  [a,c,d,f,g],
  [a,c,d,e,f,g],
  [a,b,c],
  [a,b,c,d,e,f,g],
  [a,b,c,f,g]         #9
]


while True:
  if btn.value() == 0 and pressed == False: #pressed
    current_digit += 1
    if current_digit > 9:
      current_digit = 0
  
    all_off()
   
    for led in numbers[current_digit]:
      led.value(1)
    pressed = True
  
  if btn.value() == 0:
    pressed = False
    
  
  sleep(0.1)


