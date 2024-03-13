#%%  question a) : importation

import numpy as np
import matplotlib.pyplot as plt


#%%  question b) : définition de la grille

Nx=  #définition de la taille et du pas de la grille
Ny=    
a=   
V=np.zeros((Nx,Ny))  # initialisation du potentiel                 


#%%  question c) : conditions limites sur le bord de la grille

CL=np.empty((Nx,Ny), dtype=bool) # définition du tableau CL
                    # initilisation du tableau CL   

def CL1():          #  compléter
    
    
#%%  question d) : conditions limites à l'intérieur de la grille

def CL2():
    b=1
    
    #situation S2 (à laisser en commentaires)
    #for i in range(int(Nx/2),Nx-1,1) 
    #        CL[i,int(Ny/2)]=True
    #        V[i,int(Ny/2)]=10

    #situation S3 (à laisser en commentaires)
    #V[int(Nx/4):int(3*Nx/4),int(8*Ny/20)]=10
    #CL[int(Nx/4):int(3*Nx/4),int(8*Ny/20)]=True
    #V[int(Nx/4):int(3*Nx/4),int(12*Ny/20)]=-10
    #CL[int(Nx/4):int(3*Nx/4),int(12*Ny/20)]=True


#%%  question e) 

def ecart(V1,V2)            #A rédiger

    
#%%  question f) 
    
def IterationJacobi() :     #A rédiger

    
#%%  question g) 
    
def Jacobi(eps):            #A rédiger
    

#%%  Reprise des fonctions du TD précédent sur le calcul du champs et l'affichage

def champE(V,i,j):
    Ex=(V[i,j]-V[i,j+1])/a
    Ey=(V[i,j]-V[i+1,j])/a
    return Ex,Ey


def calcul_champE(V):
    Ex=np.zeros((Nx,Ny))
    Ey=np.zeros((Nx,Ny))
    for i in range(Nx-1):
        for j in range(Ny-1):
            Ex[i,j],Ey[i,j]=champE(V,i,j)
    return Ex,Ey


#%%  Exécution

def execution(eps):
    CL1()
    CL2()
    print(Jacobi(eps))              #Calcul du potentiel

    Ex,Ey=calcul_champE(V)          #Calcul du champ électrique

    import matplotlib
    matplotlib.rcParams['figure.figsize']=[9,9]

    Valeurs=np.linspace(np.min(V),np.max(V),21)
    plt.clf()
    plt.imshow(V)
    plt.contour(V,Valeurs,cmap='hot')
    plt.streamplot(np.linspace(0,Nx-1,Nx), np.linspace(0,Ny-1,Ny), Ex, Ey, color="red", linewidth=1, density=1)  
    plt.show()

    