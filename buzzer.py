from machine import Pin, PWM
import time
buzzer = PWM(Pin(0)) # branchement  

def play_son(freq,duree,duty=32767) :   
    buzzer.freq(freq)        
    buzzer.duty_u16(duty)
    time.sleep_ms(duree - 50) #valeur
    buzzer.duty_u16(0)
    time.sleep_ms(50) #valeur

if __name__ == "__main__":    
    print('son 1')
    play_son(440,1000) #duty par defaut
    time.sleep(1)
    print('son 2')
    play_son(440,1000,5000) 
    time.sleep(1)
