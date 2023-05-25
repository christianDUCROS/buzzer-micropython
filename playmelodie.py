#play star wars
from machine import Pin, PWM
import time
pwm0 = PWM(Pin(0))


#const hauteur notes
C3 = 261
C3d = 277
D3 = 294
D3d = 311
E3 = 329
F3 = 349
F3d = 370
G3 = 392
G3d = 415
A3 = 440
A3d = 466
B3 = 493
C4 = 523
C4d = 554
D4 = 587
D4d = 622
E4 = 659
F4 = 698
F4d = 740
G4 = 784
G4d = 830
A4 = 880
S = 'S'

def play_son(freq,duree, duty=32767): 
    pwm0.freq(freq)        
    pwm0.duty_u16(duty)
    time.sleep_ms(duree- 50) #valeur
    pwm0.duty_u16(0)
    time.sleep_ms(50) #valeur

def play_silence(duree): 
    pwm0.freq(440) #nombre différent de 0        
    pwm0.duty_u16(0)
    time.sleep_ms(duree) 
 
#star wars
SW_sequence_1 = [[A3, 500],[A3, 500], [A3, 500],[F3, 350],[C4, 150],[A3, 500],[F3, 350],[C4, 150],[A3, 650]]
SW_sequence_2 = [[S, 500]] #silence 
SW_sequence_3 = [[E4, 500],[E4, 500], [E4, 500],[F4, 350],[C4, 150],[G3d, 500],[F3, 350],[C4, 150],[A3, 650]]
SW_sequence_4 = [[S, 500]]
star_wars =  [SW_sequence_1,SW_sequence_2,SW_sequence_3,SW_sequence_4]

#Alarme
sequence_alarme_1 = [[A3, 500],[S, 500], [A3, 500],[S, 500],[A3, 500],[S, 500]]
alarme = [sequence_alarme_1]

def play_melodie(melodie) :  
    for i in range (len(melodie)) :
        for j in range (len(melodie[i])) :
            print(melodie[i][j][0],'\t',(melodie[i][j][1]))
            if melodie[i][j][0] == 'S' :
                play_silence(melodie[i][j][1])
            else :
                play_son(melodie[i][j][0],melodie[i][j][1])

if __name__ == "__main__":
    play_melodie(star_wars)
    play_melodie(alarme)


