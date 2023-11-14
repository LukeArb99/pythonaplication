from funciones import Problema_de_Cauchy
import matplotlib.pyplot as plt
from numpy import linspace

def Simulacion(F,U0,scheme):
    d_t = 0.01
    N=1000
    t=linspace(0,N*d_t,N+1)


    U = Problema_de_Cauchy(F,t,U0,scheme)

    plt.title(scheme)
    plt.axis('equal')
    plt.plot(U[0,:], U[1,:])
    plt.show()
