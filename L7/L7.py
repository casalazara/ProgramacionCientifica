import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt

# Lo voy a usar para hallar intervalos
def inspeccionNumerica(f, inic, fin, pasos,titulo):
    print("INSPECCIÓN NUMÉRICA")
    x = np.arange(inic, fin, pasos,dtype=np.float64)
    plt.figure()
    plt.plot(x, f(x))
    plt.grid(1)
    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("y")
    indiceraiz = np.argmin(np.abs(f(x)))
    print("Una posible raiz para la función es: ", x[indiceraiz], "\n")

## 1
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt

def biseccion(f, x0, x1, Tol, Toly):
    # Condiciones de parada
    Tolx = Tol
    Tolf = Toly

    # Variables para almacenar la raiz en cada iteracion y contar el numero de iteraciones
    x2prev = x1
    iter = 0

    # Arreglo para guardar las raices candidatas
    raices = np.array([])
    # Iteracion
    while 1:
        # Aumentamos en 1 las iteraciones
        iter += 1
        # Evaluar la raiz candidata
        x2 = (x0 + x1) / 2.0
        # Guardar la raiz candidata en el arreglo
        raices = np.append(raices, x2)
        # Evaluar las condiciones de parada
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f(x2)) <= Tolf:
            break
        # Actualizmos el intervalo segun el metodo de biseccion
        if f(x2) * f(x0) < 0:
            x1 = x2
        else:
            x0 = x2
        # Actualizar x0, x1 y la raiz candidata
        x2prev = x2
    # Imprimir resultado y retornar arreglo de raíces
    print('Método de Biseccion - La raiz calculada es:', x2)
    print('Método Biseccion - El número de iteraciones realizadas fue:', iter, "\n")
    return raices


## 2
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt

def falsaPos(f, x0, x1, Tol, Toly):
    # Tolerancias
    Tolx = Tol
    Tolf = Toly
    # Variable para almacenar la raíz en la iteración anterior
    x2prev = x1
    # Contador de iteraciones
    iter = 0
    # Arreglo para guardar las raices candidatas
    raices = np.array([])
    # Iteración
    while 1:
        # Aumentamos en 1 las iteraciones
        iter += 1
        # Hallamos la raiz candidata
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
        # Guardar la raiz candidata en el arreglo
        raices = np.append(raices, x2)
        # Evaluamos el criterio de tolerancia en x
        if np.abs(x2 - x2prev) <= Tolx:
            break
        # Evaluamos el criterio de tolerancia en y
        if np.abs(f(x2)) <= Tolf:
            break
        # Cambiamos el intervalo de acuerdo a x2
        if (f(x2) * f(x0) < 0):
            x1 = x2
        else:
            x0 = x2
        # Actualizamos el valor de la raíz
        x2prev = x2
    # Imprimir resultado y retornar raíces
    print("Falsa Posición - La raíz es:", x2)
    print("Falsa Posición - Número de iteraciones:", iter, "\n")
    return raices


## 3
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt

def puntoFijo(f, g, x1, Tol, Toly):
    # Tolerancias
    Tolx = Tol
    Tolf = Toly
    # Variable para almacenar la raíz en la iteración anterior
    x2prev = x1
    # Contador de iteraciones
    iter = 0
    # Arreglo para guardar las raices candidatas
    raices = np.array([])
    # Iteración
    while 1:
        # Aumentamos en 1 las iteraciones
        iter += 1
        # Hallamos la raiz candidata
        x2 = g(x1)
        # Guardar la raiz candidata en el arreglo
        raices = np.append(raices, x2)
        # Evaluamos el criterio de tolerancia en x
        if (np.abs(x2 - x2prev) <= Tolx):
            break
        # Evaluamos el criterio de tolerancia en y
        if (np.abs(f(x2)) <= Tolf):
            break
        # Actualizmaos x1 y la raíz anterior
        x1 = x2
        x2prev = x2
    # Imprimir resultado y retornar raíces
    print("La raiz es", x2)
    print("# De iteraciones", iter, "\n")
    return raices


## 4
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt

def newton(f, x1, df, Tol, Toly):
    # Tolerancias
    Tolx = Tol
    Tolf = Toly
    # Variable para guardar la raíz anterior
    x2prev = x1
    # Contador de iteraciones
    iter = 0
    # Arreglo para almacenar las raíces candidatas
    raices = np.array([])
    # Iteración
    while 1:
        # Aumentamos en 1 las iteraciones
        iter += 1
        # Hallamos la raíz candidata
        x2 = x1 - (f(x1) / df(x1))
        # Almacenamos la raíz candidata
        raices = np.append(raices, x2)
        # Evaluamos el criterio de tolerancia en x
        if (np.abs(x2 - x2prev) <= Tolx):
            break
        # Evaluamos el criterio de tolerancia en y
        if (np.abs(f(x2)) <= Tolf):
            break
        # Actualizmaos x1 y la raíz anterior
        x1 = x2
        x2prev = x2
    # Imprimir resultado y retornar raíces
    print("Con Newton la raiz es:", x2)
    print("Con Newton el # De iteraciones es", iter, "\n")
    return raices


## 5
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt

def secante(f, x0, x1, Tol, Toly):
    # Tolerancias
    Tolx = Tol
    Tolf = Toly
    # Arreglo para guardar las raíces candidatas
    raices = np.array([])
    # Variables para guardar la raíz anterior y contar las iteraciones
    x2prev = x1
    iter = 0
    # Iteración
    while 1:
        # Aumento en 1 las iteraciones
        iter += 1
        # Evaluar la raiz candidata
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
        # Guardar la raiz candidata en el arreglo
        raices = np.append(raices, x2)
        # Evaluar las condiciones de parada con los criterios de tolerancia en x y y
        if np.abs(x2 - x2prev) <= Tolx:
            break
        if np.abs(f(x2)) <= Tolf:
            break
        # Actualizar x0, x1 y la raiz candidata
        x0 = x1
        x1 = x2
        x2prev = x2
    print('Método de Secante - La raiz calculada es:', x2)
    print('Método Secante - El número de iteraciones realizadas fue:', iter, "\n")
    return raices


## 6
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt

def tasa_convergencia(f, raices, metodo):
    # Para estimar ahora la tasa de convergencia requerimos hallar el valor verdadero de la raiz
    xroot_true = opt.fsolve(f, raices[-1])

    # Con el valor de la raiz en cada iteracion hallamos el error
    eps_array = np.abs(raices - xroot_true)
    # Hallamos la tasa de convergencia de cada iteracion con el logaritmo (diapositive 13)
    r_array = (np.log10(eps_array[1:np.size(eps_array) - 1] /
                        eps_array[2:np.size(eps_array)]) /
               np.log10(eps_array[0:np.size(eps_array) - 2] /
                        eps_array[1:np.size(eps_array) - 1]))
    # Plot
    iter_array = np.arange(1.0, np.size(r_array) + 1)
    plt.figure()
    plt.plot(iter_array, r_array)
    plt.plot(iter_array, r_array, 'or')
    plt.xlabel('Iteración')
    plt.ylabel('Tasa de convergencia est.')
    plt.title(metodo)
    plt.grid(1)
    print(metodo, "La tasa de convergencia para las últimas iteraciones está entre", r_array[-2], "y", r_array[-1],
          "\n")
    return r_array

## 7.1
from Salazar_201816839 import inspeccionNumerica,falsaPos,biseccion,newton,secante
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt

# PARA LA PRIMER FUNCIÓN
def f1(x):
    return np.e ** (-5.0 * (x ** 2.0)) - (x ** (3.0 / 4.0)) + np.sin(4.0 * x) - 1.0


def df1(x):
    return (-10 * x) * (np.e ** (-5.0 * (x ** 2.0))) - (3.0 / 4.0 * (x ** (-1.0 / 4.0))) + (4.0 * np.cos(4.0 * x))

print("------------f1(X)------------")
#Hallo el intervalo por inspección numérica
inspeccionNumerica(f1,0.0,10.0,0.001,"f1(x)")
tolerancia = 10 ** -5
a1 = biseccion(f1, 0.2, 0.6, tolerancia, tolerancia)
a2 = falsaPos(f1, 0.2, 0.6, tolerancia, tolerancia)
a3 = newton(f1, 0.6, df1, tolerancia, tolerancia)
a4 = secante(f1, 0.55, 0.6, tolerancia, tolerancia)
print("Bisección", f1(a1[-1]))
print("Falsa Posición", f1(a2[-1]))
print("Newton", f1(a3[-1]))
print("Secante", f1(a4[-1]))

## 7.2
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt
from Salazar_201816839 import *

# PARA LA SEGUNDA FUNCIÓN
def f2(x):
    return (np.sin(4*x)*np.sqrt(x**2))+(x**5)+(6*x)-4

def df2(x):
    return (4*np.cos(4*x)*np.sqrt(x**2)+np.sin(4*x))+(5*(x**4))+6

print("------------f2(X)------------")
#Hallo el intervalo por inspección numérica
inspeccionNumerica(f2,0.0,10.0,0.001,"f2(x)")
tolerancia = 10 ** -5
a1 = biseccion(f2, 0.0, 1.0, tolerancia, tolerancia)
a2 = falsaPos(f2, 0.0, 1.0, tolerancia, tolerancia)
a3 = newton(f2, 1.0, df2, tolerancia, tolerancia)
a4 = secante(f2, 0.95, 0.5, tolerancia, tolerancia)
print("Bisección", f2(a1[-1]))
print("Falsa Posición", f2(a2[-1]))
print("Newton", f2(a3[-1]))
print("Secante", f2(a4[-1]))
## 7.3
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt
from Salazar_201816839 import *

# PARA LA TERCER FUNCIÓN
def f3(x):
    h = np.pi / 2.0
    c = np.pi / 2.0
    return -(3.65 * np.log(x / 5.33)) + np.sqrt(2.0) * (np.e ** ((-c ** 2.0) - 4.25)) + 10.54 * np.cos(x - 2.2) - (6.67 * h)


def df3(x):
    return -((3.65) / x) - 10.54 * np.sin(x - 2.2)


print("------------f3(X)------------")
#Hallo el intervalo por inspección numérica
inspeccionNumerica(f3,0.0,10.0,0.001,"f3(x)")
tolerancia = 10 ** -5
a1 = biseccion(f3, 0.01, 0.1, tolerancia, tolerancia)
a2 = falsaPos(f3, 0.01, 0.1, tolerancia, tolerancia)
a3 = newton(f3, 0.01, df3, tolerancia, tolerancia)
a4 = secante(f3, 0.01, 0.015, tolerancia, tolerancia)
print("Bisección", f3(a1[-1]))
print("Falsa Posición", f3(a2[-1]))
print("Newton", f3(a3[-1]))
print("Secante", f3(a4[-1]))

## 8
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt
from Salazar_201816839 import *


def f8(x):
    return (-1.440 * (x ** -2.0)) + (0.710 * (x ** -1.0)) + 0.088 + (0.0636 * x)


def g81(x):
    return ((1.0 / 1.440) * ((0.710 * (x ** -1.0)) + 0.088 + (0.0636 * x))) ** (-1.0 / 2.0)


def g82(x):
    return (1.0 / 0.0636) * ((1.440 * (x ** -2.0)) - (0.710 * (x ** -1.0)) - 0.088)


def g83(x):
    return (1.440 * (x ** -2.0)) - (0.710 * (x ** -1.0)) - 0.088 - (0.0636 * x) + x

## 8B
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt
from Salazar_201816839 import *

inspeccionNumerica(f8, 0.01, 3.0, 0.0001,"Punto 8")

## 8C.1
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt
from Salazar_201816839 import *

tolerancia = 10 ** -5
raices = puntoFijo(f8, g81, 2.0, tolerancia, tolerancia)
print(g81(2.0))  # 0
iteraciones=[1,5,10,13]
for iteracion in iteraciones:
    if(iteracion<=len(raices)):
        if iteracion==1:
            print(raices[iteracion-1],g81(raices[iteracion-1]),np.abs(2.0-raices[iteracion-1]))
        else:
            print(raices[iteracion-1],g81(raices[iteracion-1]),np.abs(raices[iteracion-2]-raices[iteracion-1]))
    else:
        break


## 8C.2
#import numpy as np
#import matplotlib.pyplot  as plt
#import scipy.optimize as opt
#from Salazar_201816839 import *
#tolerancia = 10 ** -5
# raices = puntoFijo(f8, g82, 2.0, tolerancia, tolerancia)  Lo comenté porque no converge.
print(g82(2.0))  # 0
#iteraciones=[1,5,10,13]
#for iteracion in iteraciones:
    #if(iteracion<=len(raices)):
        #if iteracion==1:
            #print(raices[iteracion-1],f8(raices[iteracion-1]),np.abs(2.0-raices[iteracion-1]))
        #else:
            #print(raices[iteracion-1],f8(raices[iteracion-1]),np.abs(raices[iteracion-2]-raices[iteracion-1]))
    #else:
        #break


## 8C.3
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt
from Salazar_201816839 import *

tolerancia = 10 ** -5
raices = puntoFijo(f8, g83, 2.0, tolerancia, tolerancia)
print(g83(2.0))  # 0
iteraciones=[1,5,10,13]
for iteracion in iteraciones:
    if(iteracion<len(raices)):
        if iteracion==1:
            print(raices[iteracion-1],g83(raices[iteracion-1]),np.abs(raices[iteracion-1]-2.0))
        else:
            print(raices[iteracion-1],g83(raices[iteracion-1]),np.abs(raices[iteracion]-raices[iteracion-1]))
    else:
        break


## 9B
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt
from Salazar_201816839 import *

def df8(x):
    return (2.880*(x**-3.0))-(0.71*(x**-2))+0.0636
tolerancia = 10 ** -5
raices =newton(f8,2.0,df8,tolerancia,tolerancia)
print(f8(2.0))  # 0
iteraciones=[1,3,6,10]
for iteracion in iteraciones:
    if(iteracion<len(raices)):
        print(iteracion,iteracion-1,iteracion-2)
        if iteracion==1:
            print(raices[iteracion-1],f8(raices[iteracion-1]),np.abs(raices[iteracion-1]-2.0))
        else:
            print(raices[iteracion-1],f8(raices[iteracion-1]),np.abs(raices[iteracion]-raices[iteracion-1]))
    else:
        break
## 9C
import numpy as np
import matplotlib.pyplot  as plt
import scipy.optimize as opt
from Salazar_201816839 import *
tolerancia = 10 ** -5
raices =newton(f8,2.0,df8,tolerancia,tolerancia)
tasas=tasa_convergencia(f8,raices,'Newton')
print("Las tasas de convergencia para cada iteración son:",tasas)