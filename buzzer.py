from machine import Pin, PWM
import time

def play_son(freq,duty,duree) :   
    pwm0.freq(freq)        
    pwm0.duty_u16(duty)
    time.sleep_ms(duree - 50) #valeur
    pwm0.duty_u16(0)
    time.sleep_ms(50) #valeur

print('son 1')
play_son(440,32767,1000)
time.sleep(1)
print('son 2')
play_son(440,5000,1000)
time.sleep(1)
