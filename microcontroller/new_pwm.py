
from machine import Pin, PWM
from time import sleep



breath = PWM(Pin(14))



#pwm
duty_max = 65000  #65025 is the max  how long its on
breath.freq(500)  #soft pulsing


while True:
        
    #  getting brigher 0 to duty_max  in steps of 5
    for duty in range(0,duty_max,5):
        breath.duty_u16(duty)
        sleep(0.0006)
    
    #  getting dimmer duty_max to 0  in steps of 5
    for duty in range(duty_max,0, -5):
        breath.duty_u16(duty)
        sleep(0.0006)  # time - usually  0.0001
        
   
        
