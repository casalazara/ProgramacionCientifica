##
import numpy as np
import matplotlib.pyplot as plt
# Funciones f1 y f2
def F1(x1,x2):
    return (x1**2.0)+x2-3.0
def F2(x1,x2):
    return ((x1-2.0)**2.0)+((x2+3.0)**2.0)-4.0
# Líneas de contorno para establecer las condiciones iniciales
# Vectores iniciales y espacio 2D para evaluar contornos
delta = 0.1
x1 = np.arange(-1.0, 5.0, delta)
x2 = np.arange(-6.0, 0.0, delta)
A, B = np.meshgrid(x1, x2)
# Líneas de contorno
plt.figure()
C1 = plt.contour(A, B, F1(A, B),[0.0],colors='b')
plt.clabel(C1, fontsize=10)
C2 = plt.contour(A, B, F2(A, B),[0.0], colors='r')
plt.clabel(C2, fontsize=10)
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid(1)

## Para la primer raíz
import numpy as np
import matplotlib.pyplot as plt
from Salazar_201816839 import F1,F2
# Jacobiano
def Jaco(x1,x2):
    A = np.zeros([2, 2])
    A[0, 0] = 2.0*x1
    A[0, 1] = 1.0
    A[1, 0] = (2.0*x1)-4.0
    A[1, 1] = (2.0*x2)+6.0
    return A

def calcular_raices(x1i0,x2i0,TolX,TolY,F1,F2,Jaco):
    # contador iteraciones
    iter = 0
    # Algoritmo para calcular las raices
    while 1:
        iter += 1
        # Planteamos sistema de ecuaciones con el jacobiano
        A = Jaco(x1i0, x2i0)
        b = np.zeros([2, 1])
        b[0] = -F1(x1i0, x2i0)
        b[1] = -F2(x1i0, x2i0)
        # Resolvemos el sistema para hallar los deltasx
        delta_x = np.linalg.solve(A, b)
        # La raiz candidata es x^i=x^i-1+DeltaX
        x1 = np.float(x1i0 + delta_x[0])
        x2 = np.float(x2i0 + delta_x[1])
        # Evaluamos las condiciones de parada
        if np.abs(x1-x1i0)<= TolX and np.abs(x2-x2i0)<= TolX:
            break
        if np.abs(F1(x1, x2))<= TolY and np.abs(F2(x1, x2))<= TolY:
            break
        # Actualizamos x1i0 y x2i0 para la siguiente iteración
        x1i0 = x1
        x2i0 = x2
    # Imprimimos los resultados
    print('Los valores de las raices, por el método multivariable son')
    print('x1 = ', x1)
    print('x2 = ', x2)
    print('el número de iteraciones fue', iter)

#Puntos iniciales para x1 y x2 cercanos a la raíz 1
x1i0 = 4.0
x2i0 = -1.0

TolX = 10**-5
TolY = 10**-5
print("Tolerancia 10^-5")
calcular_raices(x1i0,x2i0,TolX,TolY,F1,F2,Jaco)
print("Tolerancia 10^-10")
TolX = 10**-10
TolY = 10**-10
calcular_raices(x1i0,x2i0,TolX,TolY,F1,F2,Jaco)

## Para la segunda raíz
from Salazar_201816839 import F1,F2,Jaco, calcular_raices

#Puntos iniciales para x1 y x2 cercanos a la raíz 2
x1i0 = 3.0
x2i0 = -5.0

TolX = 10**-5
TolY = 10**-5
print("Tolerancia 10^-5")
calcular_raices(x1i0,x2i0,TolX,TolY,F1,F2,Jaco)
print("Tolerancia 10^-10")
TolX = 10**-10
TolY = 10**-10
calcular_raices(x1i0,x2i0,TolX,TolY,F1,F2,Jaco)
## Para que diverja
from Salazar_201816839 import F1,F2,Jaco, calcular_raices

#Puntos iniciales para x1 y x2 para que diverja
x1i0 = 1.75
x2i0 = -3.0

TolX = 10**-5
TolY = 10**-5
print("Tolerancia 10^-5")
calcular_raices(x1i0,x2i0,TolX,TolY,F1,F2,Jaco)
print("Tolerancia 10^-10")
TolX = 10**-10
TolY = 10**-10
calcular_raices(x1i0,x2i0,TolX,TolY,F1,F2,Jaco)