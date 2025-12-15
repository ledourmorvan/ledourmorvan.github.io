#%% 1-Importation

import numpy as np
import matplotlib.pyplot as plt
 
#%% 2-Parametres

t0=0                        # Instant initial         
Liste_t=[t0]                # Liste des températures successives 
T0=298                      # Température initiale         
Liste_T=[T0]                # Liste des températures successives 
C0=0.2                  # Concentration initiale
Liste_C=[C0]                # Liste des concentrations successives
DrH0=-76000                 # Enthalpie de réaction
k1,Ea=0.0004, 72000         # Cte de vitesse et energie d'activation (à 298 K)
rho, ce=1.0, 4200.0         # masse volumique et capacite thermique massique de la solution
 
Duree=7/k1                  #  durée d'évolution (en s)   
N=5000                      # nd de pas
      
#%% 3-Calcul de la constante de vitesse 

def k(T):
    R=8.314
    ki=k1*np.exp(-Ea/R*(1/T-1/T0))
    return ki

#%% 4-Calcul de la vitesse de réaction

def v(C,T):
    vi=C*k(T)
    return vi

#%% 5-Calcul des accroissements  des variables

def etape(t,C,T):
    dt=Duree/N
    dC=-v(C,T)*dt
    dT=DrH0*dC/(rho*ce)
    return dt,dC,dT

#%% 6-Construction des listes 
    
def listes(t, T, C):
    for i in range(N):
        Dt,DC,DT=etape(t,C,T)
        C=C+DC
        T=T+DT
        t=t+Dt
        Liste_C.append(C)
        Liste_T.append(T)
        Liste_t.append(t)
    return Liste_t, Liste_T, Liste_C

#%% 7-Calcul de C(t) et T(t)  

L_temps, L_temperature, L_concentration = listes(t0,T0,C0) 
    
#%% 8-Affichage des résultats

fig=plt.figure()

ax1=fig.add_subplot(211)  # les subplot sont nommés 'axe' en Python
plt.plot(L_temps,L_temperature)
ax1.set_title('T(t)')
ax1.set_xlabel(r'$t$ (s)')
ax1.set_ylabel(r'$T$ (K)')
ax1.grid()

ax2=fig.add_subplot(212) 
plt.plot(L_temps,L_concentration)
ax2.set_title("C(t)")
ax2.set_xlabel(r'$t$ (s)')
ax2.set_ylabel(r'$C$ (mol/L)')
ax2.grid()
    
plt.show()
