from matplotlib.pyplot import *
import numpy as np

r=0.75   #Rapport cycliique 
def C(n):
    return 2*r*np.exp(-1j*np.pi*n*r)*np.sin(np.pi*n*r)/(np.pi*n*r)
spectre = [r]
P = 10  # harmoniques
for n in range(1,P+1):
    spectre.append(np.abs(C(n)))
figure(figsize=(12,6))
stem(np.arange(P+1),spectre,'r')
title(f"Representation harmonique signal rectangle de rapport cyclyque = {r}",color= "red",fontsize=15,fontweight="bold")
xlabel('n',fontsize=16)
ylabel('Cn',fontsize=16)
grid()
axis([0.5,10,0,0.7])
show()
