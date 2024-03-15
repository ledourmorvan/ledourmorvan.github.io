#%%  question a) : importation

import numpy as np
import matplotlib.pyplot as plt


#%%  question b) : définition de la grille

Nx=151      #définition de la taille et du pas de la grille
Ny=151      
a=1e-6       
V=np.zeros((Nx,Ny))  # initialisation du potentiel                 


#%%  question c) : conditions limites sur le bord de la grille

CL=np.empty((Nx,Ny), dtype=bool) 
CL[:,:]=False        # initialisation du tableau CL   

def CL1():
    for j in range(Ny):
        V[Nx-1,j]=00    
        V[0,j]=0 
    for i in range(Nx):    
        V[i,0]=0     
        V[i,Ny-1]=0  
    
    
#%%  question d) : conditions limites à l'intérieur de la grille

def CL2():
    b=1
    
    #situation S2 (à laisser en commentaires)
    #for i in range(int(Nx/2),Nx-1,1) :
    #        CL[i,int(Ny/2)]=True
    #        V[i,int(Ny/2)]=10

    #situation S3 (à laisser en commentaires)
    V[int(Nx/4):int(3*Nx/4),int(8*Ny/20)]=10
    CL[int(Nx/4):int(3*Nx/4),int(8*Ny/20)]=True
    V[int(Nx/4):int(3*Nx/4),int(12*Ny/20)]=-10
    CL[int(Nx/4):int(3*Nx/4),int(12*Ny/20)]=True

#%%  question e) 

def ecart(V1,V2) :
    somme=0
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
             somme=somme+   (V1[i,j]-V2[i,j])**2
    return (somme/(Nx*Ny))**0.5

#%%  question f) 
def IterationJacobi() :
    Vn=np.copy(V)
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
            if not(CL[i,j]) :
               V[i,j]=(Vn[i+1,j]+Vn[i-1,j]+Vn[i,j+1]+Vn[i,j-1])/4
    return ecart(V,Vn)

#%%  question g) 
    
def Jacobi(eps):
    compteur=0
    e=1
    while e>eps : 
        e=IterationJacobi2() 
        compteur=compteur+1
    return compteur
        
    

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
    print(Jacobi(eps))

    Ex,Ey=calcul_champE(V)

    import matplotlib
    matplotlib.rcParams['figure.figsize']=[9,9]

    Valeurs=np.linspace(np.min(V),np.max(V),21)
    plt.clf()
    plt.imshow(V)
    plt.contour(V,Valeurs,cmap='hot')
    plt.streamplot(np.linspace(0,Nx-1,Nx), np.linspace(0,Ny-1,Ny), Ex, Ey, color="red", linewidth=1, density=1)  
    plt.show()

    
#%%  question i) : version 2 de l'algorithme

def ecart2(V1,V2) :
    return (np.sum((V1-V2)**2)/(Nx*Ny))**(1/2)

def IterationJacobi2() :
    Vn=np.copy(V)
    V[1:Nx-1,1:Ny-1]=(Vn[1:Nx-1,0:Ny-2]+Vn[1:Nx-1,2:Ny]+Vn[2:Nx,1:Ny-1]+Vn[0:Nx-2,1:Ny-1])/4
    CL2()
    return ecart2(V,Vn)