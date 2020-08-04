
############################################
#          "Universidad de los Andes"
#           Programación Científica
#   Laboratorio 7: Solución de sistemas No lineales

# Autor: Julio Nicolás Reyes

############################################

import numpy as np
import time as ti
import struct as st
import matplotlib.pyplot as plt

##
'''Métodos de Intervalo Cerrado'''

# 1) Realice una función en Python que permita obtener la raíz de una ecuación no lineal de una variable usando el
# método de la bisección. La función debe recibir como parámetros la función objetivo f(x), el intervalo inicial, las
# tolerancias en X y Y, y debe retornar un arreglo con los valores estimados de la raíz para cada iteración.

# ------------------------------------------------------------------------------------------
# Se define la función a evaluar
def fun(x):
    return -(np.sqrt(3*x)**(2/5))   +   (x**3)*np.cos(3*x)   +   4*(x**2)  -  7

# ------------------------------------------------------------------------------------------
# Gráfica para determinar de forma visual en qué intervalo puede estar la raíz
x=np.arange(0,3,0.01)
plt.figure()
plt.grid(True)
plt.plot(x,fun(x))
plt.xlabel("x")
plt.ylabel("f(x)")

'''Datos para función fun(x)'''
# Intervalo Inicial
xi = 1.0
xf = 2.0

#Valores de Tolerancia para el error de 'x' y 'f(x).  (opción 1)'
Tolx = 10**-5
Tolf = 10**-5

xr_pre = 0              # Variable que almacena el valor de la raíz en la iteración anterior
iter=0                  # Variable para el número de iteraciones

Ea = 0                  # Variable que guarda el error relativo (opción 2)
# ------------------------------------------------------------------------------------------

def fun_Bise(funcion, xi, xf, Tolx, Tolf, iter=0, xr_pre = 0):
    funcion = fun(x)
    xr_arreglo = np.array([])  # Arreglo para ir guardando los valores de las raíces candidatas

    while 1:
        iter += 1
        if fun(xi)*fun(xf) < 0:     # Condición que evalúa si efectivamente existe una raíz en el intervalo [xi, xf]
            xr = (xi + xf) / 2.0    # Aproximación a la raíz (xr) por método de bisección
            xr_arreglo = np.append(xr_arreglo, xr)    # Los valores de 'xr' se van guardando en el arreglo: xr_arreglo

            '''Opción 1 para el cálculo del error (criterio de parada 1)'''
            #Ea = np.abs((xr - xr_pre) / xr) * 100      # Calculamos el error aproximado relativo (Ea)
            #if Ea <= Tol:
            #   break

            '''Opción 2 para el cálculo del error (criterio de parada 2)'''
            error = np.abs(xr - xr_pre)
            if error <= Tolx:
                break
            if np.abs(fun(xr)) <= Tolf:
                break

            #print('xi =', xi, ', xf =', xf, ', xr = ', xr, ', Error =', error)

            if fun(xi)*fun(xr) < 0:     # Consideración para actualizar la raíz
                xf = xr
            elif fun(xi)*fun(xr) > 0:   # Consideración para actualizar la raíz
                xi = xr

            xr_pre = xr                 # Se guarda el valor de la raíz para poder implementar el error

        else:
            print("El intervalo escogido entre ",xi,'y',xf,'NO encierran a ninguna raíz' )

    print("\nRaiz por el método de Bisección ->     xr =", xr)
    print("    # Iteraciones por Bisección ->      n =", iter)
    print('    Función evaluada en xr      ->  f(xr) = ', fun(xr))
    print('    Error para xr               ->  Error = ',  error)

    return xr_arreglo

Raices = fun_Bise(fun(x), xi, xf, Tolx, Tolf)    # Llamado a la función de Bisección. Entran como parámetros:
                                # - la función objetivo f(x), - el intervalo inicial [xi, xf], - las tolerancias en 'x' y 'f(x)'



## 2) Realice una función en Python que permita obtener la raíz de una ecuación no lineal de una variable usando el
# método de falsa posición. La función debe recibir como parámetros la función objetivo f(x), el intervalo inicial, las
# tolerancias en X y Y, y debe retornar un arreglo con los valores estimados de la raíz para cada iteración.
import numpy as np
# ------------------------------------------------------------------------------------------
# Se define la función a evaluar
def fun(x):
    return -(np.sqrt(3*x)**(2/5))   +   (x**3)*np.cos(3*x)   +   4*(x**2)  -  7

# ------------------------------------------------------------------------------------------
# Gráfica para determinar de forma visual en qué intervalo puede estar la raíz
x=np.arange(0,3,0.01)
plt.figure()
plt.grid(True)
plt.plot(x,fun(x))
plt.xlabel("x")
plt.ylabel("f(x)")

'''Datos para función fun(x)'''
# Intervalo Inicial
xi = 1.0
xf = 2.0

#Valores de Tolerancia para el error de 'x' y 'f(x).  (opción 1)'
Tolx = 10**-5
Tolf = 10**-5

xr_pre = 0              # Variable que almacena el valor de la raíz en la iteración anterior
iter=0                  # Variable para el número de iteraciones

Ea = 0                  # Variable que guarda el error relativo (opción 2)
# ------------------------------------------------------------------------------------------

def fun_FalsaPos(funcion, xi, xf, Tolx, Tolf, iter=0, xr_pre = 0):
    funcion = fun(x)
    xr_arreglo = np.array([])  # Arreglo para ir guardando los valores de las raíces candidatas

    while 1:
        iter += 1
        if fun(xi)*fun(xf) < 0:     # Condición que evalúa si efectivamente existe una raíz en el intervalo [xi, xf]
            xr = xf - ((fun(xf))*(xi - xf) / (fun(xi) - fun(xf)))    # Aproximación a la raíz (xr) por método de falsa posición

            xr_arreglo = np.append(xr_arreglo, xr)    # Los valores de 'xr' se van guardando en el arreglo: xr_arreglo

            '''Opción 1 para el cálculo del error (criterio de parada 1)'''
            #Ea = np.abs((xr - xr_pre) / xr) * 100      # Calculamos el error aproximado relativo (Ea)
            #if Ea <= Tol:
            #   break

            '''Opción 2 para el cálculo del error (criterio de parada 2)'''
            error = np.abs(xr - xr_pre)
            if error <= Tolx:
                break
            if np.abs(fun(xr)) <= Tolf:
                break

            #print('xi =', xi, ', xf =', xf, ', xr = ', xr, ', Error =', error)

            if fun(xi)*fun(xr) < 0:     # Consideración para actualizar la raíz
                xf = xr
            elif fun(xi)*fun(xr) > 0:   # Consideración para actualizar la raíz
                xi = xr

            xr_pre = xr                 # Se guarda el valor de la raíz para poder implementar el error

        else:
            print("El intervalo escogido entre ",xi,'y',xf,'NO encierran a ninguna raíz' )

    print("\nRaiz por el método de Falsa Posición ->     xr =", xr)
    print("    # Iteraciones por Falsa Posición ->      n =", iter)
    print('    Función evaluada en xr           ->  f(xr) = ', fun(xr))
    print('    Error para xr                    ->  Error = ', error)

    return xr_arreglo

Raices = fun_FalsaPos(fun(x), xi, xf, Tolx, Tolf)    # Llamado a la función de Bisección. Entran como parámetros:
                                # - la función objetivo f(x), - el intervalo inicial [xi, xf], - las tolerancias en 'x' y 'f(x)'


##################################################################################
'''Métodos de Intervalo Abierto'''

## 3) Realice una función en Python que permita obtener la raíz de una ecuación no lineal de una variable usando el método
# del punto fijo. La función debe recibir como parámetros la función objetivo f(x), la función g(x), el punto inicial,
# las tolerancias en X y Y, y debe retornar un arreglo con los valores estimados de la raíz para cada iteración.
import numpy as np
# ------------------------------------------------------------------------------------------
# Se define la función a evaluar
def fun(x):
    return -(np.sqrt(3*x)**(2.0/5.0))   +   (x**3)*np.cos(3*x)   +   4*(x**2)  -  7.0
def g(x):
    return np.sqrt((1.0/4.0) * (np.sqrt(3*x)**(2.0/5.0)  -   (x**3)*np.cos(3*x)   +   7.0) )
#def g(x):
#    return x + (np.sqrt(3 * x) ** (2 / 5)) - (x ** 3) * np.cos(3 * x) - 4 * (x ** 2) + 7

# ------------------------------------------------------------------------------------------
# Gráfica para determinar de forma visual en qué intervalo puede estar la raíz
x = np.arange(0,2,0.01)
plt.figure()
plt.plot(x, g(x), 'r')
plt.plot(x, x, 'c')
plt.grid(True)
plt.xlabel("x")
plt.ylabel("g(x)")

'''Datos para función fun(x)'''
# Intervalo Inicial
xi = 2.0

#Valores de Tolerancia para el error de 'x' y 'f(x).  (opción 1)'
Tolx = 10**-5
Tolf = 10**-5

xr_pre = xi             # Variable que almacena el valor de la raíz en la iteración anterior
iter=0                  # Variable para el número de iteraciones

Ea = 0                  # Variable que guarda el error relativo (opción 2)
# ------------------------------------------------------------------------------------------

def fun_PuntoFijo(funcion, fung, xi, Tolx, Tolf, iter=0, xr_pre = 0):
    funcion = fun(x)
    xr_arreglo = np.array([])  # Arreglo para ir guardando los valores de las raíces candidatas

    while 1:
        iter += 1

        xr = g(xi)          # Aproximación a la raíz (xr) por método de Punto Fijo

        xr_arreglo = np.append(xr_arreglo, xr)    # Los valores de 'xr' se van guardando en el arreglo: xr_arreglo

        '''Opción 1 para el cálculo del error (criterio de parada 1)'''
        #Ea = np.abs((xr - xr_pre) / xr) * 100      # Calculamos el error aproximado relativo (Ea)
        #if Ea <= Tol:
        #   break

        '''Opción 2 para el cálculo del error (criterio de parada 2)'''
        error = np.abs(xr - xr_pre)
        if error <= Tolx:
            break
        if np.abs(fun(xr)) <= Tolf:
            break

        xi = xr                     # Actualización de 'xi' con el valor de 'xr'
        xr_pre = xr                 # Se guarda el valor de la raíz para poder implementar el error

        print('i=', iter, 'xr = ', xr, ', Error =', error)

    print("\nRaiz por el método de Punto Fijo ->     xr =", xr)
    print("    # Iteraciones por Punto Fijo ->      n =", iter)
    print('    Función evaluada en xr       ->  f(xr) = ', fun(xr))
    print('    Error para xr                ->  Error = ', error)

    return xr_arreglo

Raices = fun_PuntoFijo(fun(x), g(x), xi, Tolx, Tolf)    # Llamado a la función de Bisección. Entran como parámetros:
                                # - la función objetivo f(x), - el intervalo inicial [xi, xf], - las tolerancias en 'x' y 'f(x)'



## 4) Realice una función en Python que permita obtener la raíz de una ecuación no lineal de una variable usando el método
# de Newton. La función debe recibir como parámetros la función objetivo f(x), el punto inicial, las tolerancias en 'x' y 'f(x)',
# y debe retornar un arreglo con los valores estimados de la raíz para cada iteración.

import numpy as np
# ------------------------------------------------------------------------------------------
# Se define la función a evaluar
def fun(x):
   return -(np.sqrt(3.0*x)**(2.0/5.0))   +   (x**3.0)*np.cos(3.0*x)   +   4.0*(x**2.0)  -  7.0
def dfun(x):
   return -((3.0**(1.0/5.0))/5.0)*(x**(-4.0/5.0))    -   3.0*(x**3.0)*np.sin(3.0*x)   +   3.0*(x**2.0)**np.cos(3.0*x)   +    8*x

# ------------------------------------------------------------------------------------------

'''Datos para función fun(x)'''
# Gráfica para determinar de forma visual en qué intervalo puede estar la raíz
x = np.arange(0,2,0.01)
plt.figure()
plt.plot(x, fun(x), 'r')
plt.plot(x, x, 'c')
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")

# Intervalo Inicial
xi = 2.0

#Valores de Tolerancia para el error de 'x' y 'f(x).  (opción 1)'
Tolx = 10**-5
Tolf = 10**-5

Ea = 0                  # Variable que guarda el error relativo (opción 2)
# ------------------------------------------------------------------------------------------

def fun_Newton(funcion, xi, Tolx, Tolf, iter=0, xr_pre = xi):
    funcion = fun(x)
    xr_arreglo = np.array([])  # Arreglo para ir guardando los valores de las raíces candidatas

    while 1:
        iter += 1

        xr = xi - (fun(xi)/dfun(xi))    # Aproximación a la raíz (xr) por método de Punto Fijo

        xr_arreglo = np.append(xr_arreglo, xr)      # Los valores de 'xr' se van guardando en el arreglo: xr_arreglo

        '''Opción 1 para el cálculo del error (criterio de parada 1)'''
        #Ea = np.abs((xr - xr_pre) / xr) * 100      # Calculamos el error aproximado relativo (Ea)
        #if Ea <= Tol:
        #   break

        '''Opción 2 para el cálculo del error (criterio de parada 2)'''
        error = np.abs(xr - xr_pre)
        if error <= Tolx:
            break
        if np.abs(fun(xr)) <= Tolf:
            break

        print('i=', iter, 'xr = ', xr, ', Error =', error)

        xi = xr
        xr_pre = xr  # Se guarda el valor de la raíz para poder implementar el error

    print("\nRaiz por el método de Newton ->     xr =", xr)
    print("    # Iteraciones por Newton ->      n =", iter)
    print('    Función evaluada en xr   ->  f(xr) = ', fun(xr))
    print('    Error para xr            ->  Error = ', error)

    return xr_arreglo

Raices = fun_Newton(fun(xi), xi, Tolx, Tolf)    # Llamado a la función de Bisección. Entran como parámetros:
                                # - la función objetivo f(x), - el intervalo inicial [xi, xf], - las tolerancias en 'x' y 'f(x)'



## 5) Realice una función en Python que permita obtener la raíz de una ecuación no lineal de una variable usando el método
# de la Secante. La función debe recibir como parámetros la función objetivo f(x), los puntos iniciales, las tolerancias en 'x' y 'f(x)',
# y debe retornar un arreglo con los valores estimados de la raíz para cada iteración.

# ------------------------------------------------------------------------------------------
# Se define la función a evaluar
def fun(x):
    return -(np.sqrt(3.0*x)**(2.0/5.0))   +   (x**3.0)*np.cos(3.0*x)   +   4.0*(x**2.0)  -  7.0

# ------------------------------------------------------------------------------------------

# Gráfica para determinar de forma visual en qué intervalo puede estar la raíz
x = np.arange(0,2,0.01)
plt.figure()
plt.plot(x, fun(x), 'r')
plt.plot(x, x, 'c')
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")

'''Datos para función fun(x)'''
# Intervalo Inicial
x0 = 2.0
xi = 1.9

#Valores de Tolerancia para el error de 'x' y 'f(x).  (opción 1)'
Tolx = 10**-5
Tolf = 10**-5

Ea = 0                  # Variable que guarda el error relativo (opción 2)
# ------------------------------------------------------------------------------------------

def fun_Secante(funcion, x0, xi, Tolx, Tolf, iter=0, xr_pre = 0, xr = xi):
    funcion = fun(x)
    xr_arreglo = np.array([])  # Arreglo para ir guardando los valores de las raíces candidatas

    while 1:
        iter += 1

        xr = xi - ((fun(xi) * (x0 - xi)) / (fun(x0) - fun(xi)))    # Aproximación a la raíz (xr) por método de Punto Fijo

        xr_arreglo = np.append(xr_arreglo, xr)      # Los valores de 'xr' se van guardando en el arreglo: xr_arreglo

        '''Opción 1 para el cálculo del error (criterio de parada 1)'''
        #Ea = np.abs((xr - xr_pre) / xr) * 100      # Calculamos el error aproximado relativo (Ea)
        #if Ea <= Tol:
        #   break

        '''Opción 2 para el cálculo del error (criterio de parada 2)'''
        error = np.abs(xr - xr_pre)
        if error <= Tolx:
            break
        if np.abs(fun(xr)) <= Tolf:
            break

        #print('i=', iter, 'xr = ', xr, ', Error =', error)

        x0 = xi
        xi = xr
        xr_pre = xr  # Se guarda el valor de la raíz para poder implementar el error

    print("\nRaiz por el método de la Secante ->     xr =", xr)
    print("    # Iteraciones por Secante    ->      n =", iter)
    print('    Función evaluada en xr       ->  f(xr) = ', fun(xr))
    print('    Error para xr                ->  Error = ', error)

    return xr_arreglo

Raices = fun_Secante(fun(xi), x0, xi, Tolx, Tolf)    # Llamado a la función de Bisección. Entran como parámetros:
                                # - la función objetivo f(x), - el intervalo inicial [xi, xf], - las tolerancias en 'x' y 'f(x)'




## 6) Realice una función en Python que permita calcular la tasa de convergencia de un método dado. La función debe recibir
# como parámetros un arreglo con los valores estimados de la raíz para cada iteración y retornar los valores estimados de la
# tasa de convergencia para las iteraciones de la 2 hasta la última menos 1.

import scipy.optimize as opt

def TasaConvergencia(raices, funcion, xr):      # Se define la función para la tasa de convergencia

    Xroot = opt.fsolve(fun, xr)                 # Raíz 'ideal'

    error = np.abs(raices - Xroot)              # Error calculado para cada raíz obtenida

    '''Tasa de Convergencia (r)'''
    r = (np.log10(error[1:np.size(error) - 1] / error[2:np.size(error)]) /
         np.log10(error[0:np.size(error) - 2] / error[1:np.size(error) - 1]))

    '''Gráfica de la tasa de convergencia (r)'''
    x = np.arange(1.0, np.size(r) + 1)
    plt.plot(x, r)
    plt.plot(x, r, 'co')
    plt.grid()

    return r

r = TasaConvergencia(Raices, fun(xi), xf)

print('Las respectivas tasas de convergencia en cada iteración son:', r)







##________________________________________________________________________________________-
'''Ejercicio 7.   Completar las siguientes tablas'''

import numpy as np
import time as ti
import struct as st
import matplotlib.pyplot as plt


'''FUNCIÓN 1'''
def fun(x):
   return np.exp(-5.0*(x**2)) - x**(3.0/4.0) + np.sin(4*x)-1
def dfun(x):
  return (-10*x)*np.exp(-5.0*(x**2)) - (3.0/4.0)*x**(-1.0/4.0) + 4.0*np.cos(4*x)

# Graficamos
x=np.arange(0,3,0.01)
plt.figure()
plt.grid(True)
plt.plot(x,fun(x))
plt.xlabel("x")
plt.ylabel("f(x)")

# Se aplican las funciones definidas previamente para conocer la solución  por los diferentes métodos
SolBise = fun_Bise(fun(x), 0.2, 0.6, 10**-5, 10**-5)
SolFalsaPos = fun_FalsaPos(fun(x), 0.2, 0.6, 10**-5, 10**-5)
SolNewton = fun_Newton(fun(x), 0.6, 10**-5, 10**-5)
SolSecante = fun_Secante(fun(x), 0.55, 0.6, 10**-5, 10**-5)

##

'''FUNCIÓN 2'''
def fun(x):
    return np.sin(4*x) * x + x**5 +6*x - 4
def dfun(x):
    return 4*np.cos(4*x) * x + np.sin(4*x) + 5*(x**4) + 6

x=np.arange(0,5,0.01)
plt.figure()
plt.grid(True)
plt.plot(x,fun(x))
plt.xlabel("x")
plt.ylabel("f(x)")

# Se aplican las funciones definidas previamente para conocer la solución  por los diferentes métodos
SolBise = fun_Bise(fun(x), 0.0, 1.0, 10**-5, 10**-5)
SolFalsaPos = fun_FalsaPos(fun(x), 0.0, 1.0, 10**-5, 10**-5)
SolNewton = fun_Newton(fun(x), 1.0, 10**-5, 10**-5)
SolSecante = fun_Secante(fun(x), 0.95, 1.0, 10**-5, 10**-5)


##
'''FUNCIÓN 3'''

def fun(x):
    return (6.67*np.pi/2) + 3.65*np.log(x/5.33) - (np.sqrt(2))*np.exp(-(np.pi/2)**2 - 4.25) - 10.54*np.cos(x-2.2)
def dfun(x):
     return 3.65/x + 10.54*np.sin(x-2.2)

x=np.arange(0,5,0.01)
plt.figure()
plt.grid(True)
plt.plot(x,fun(x))
plt.xlabel("x")
plt.ylabel("f(x)")

# Se aplican las funciones definidas previamente para conocer la solución  por los diferentes métodos
SolBise = fun_Bise(fun(x), 0.01, 0.1, 10**-5, 10**-5)
SolFalsaPos = fun_FalsaPos(fun(x), 0.01, 0.1, 10**-5, 10**-5)
SolNewton = fun_Newton(fun(x), 0.01, 10**-5, 10**-5)
SolSecante = fun_Secante(fun(x), 0.01, 0.015, 10**-5, 10**-5)



###########
'''
    Ejericio 8.    Aplicación del método del punto fijo
'''

import math as mt
import numpy as np
import time as ti
import struct as st
import matplotlib.pyplot as plt

# Se define la función
def fun(x):
    R = 4
    return -1.440*x**(-2)+0.710*x**(-1)+0.688+0.0636*x-((R-1)/(R+1))

# Se definen los diferentes g(x) obtenidos de la función fun(x)
def g(x):
    return ((1/1.440)*(0.710*x**(-1)+0.0636*x+0.088))**(-0.5)

#def g(x):
    return (1/0.0636)*(1.440*x**(-2)-0.710*x**(-1)-0.088)

#def g(x):
    return 1.440*x**(-2)-0.710*x**(-1)-0.0636*x-0.088+x


# Se grafica la función para determinar visualmente cúal puede ser la solución
x=np.arange(0,2,0.01)
plt.figure()
plt.grid(True)
plt.plot(x,fun(x))
plt.xlabel("x")
plt.ylabel("f(x)")

Sol_PuntoFijo = fun_PuntoFijo(fun(x), g(x), 2, 10**-5, 10**-5)



###########
'''
    Ejericio 9
'''

# Se definen: la función 'fun(x)' y su correspondiente derivada 'dfun(x)'
def fun(x):
    R = 4
    return -1.440*x**(-2)+0.710*x**(-1)+0.688+0.0636*x-((R-1)/(R+1))

def dfun(x):
    return 2.88*x**(-3) - 0.710*(x**-2.0) + 0.0636



'''Punto b'''
SolNewton = fun_Newton(fun(x), 2, 10**-5, 10**-5)

'''Punto c'''
TasaConvergencia(SolNewton, fun(x), SolNewton[np.size(SolNewton)-1])







