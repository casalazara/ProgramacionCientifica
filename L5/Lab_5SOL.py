############################################
#          "Universidad de los Andes"
#           Programación Científica
#   Laboratorio 5: Gauss y Gauss-Jordan
############################################

import math as mt
import numpy as np
import time as ti
import matplotlib.pyplot as plt
import struct as st

##

#1. Para un sistema matricial de la forma Ax=b, donde A es una matriz de coeficientes constantes de NxN,
# x un vector de incógnitas de Nx1 y b un vector de contantes de Nx1, realice una función en Python que
# devuelva el vector de solución x usando el método de Gauss. Pruebe la función con una matriz A aleatoria (rand)
# de 3x3 y un vector b aleatorio de 3x1. Compare la solución encontrada con las funciones de la librería numpy del
# paquete linalg.

# Para matriz A y vector b aleatorios
#A = np.random.rand(3,3)
#b = np.random.rand(3,1)

# Matríz A y vector b para unos valores dados
A = np.array([[1,1,1],[3,2,1],[4,3,1]])
b = np.array([[60],[95],[125]])
Au=np.concatenate((A,b),1)
##

#Se define la función Gauss que implementa el método de solución de Gauss para reducir sistemas de ecuaciones diferenciales.

def Gauss(A,b,N):
    Au=np.concatenate((A,b),1)                  # Concatenación de la matriz A de coeficientes y el vector solución b.
    for i in range(0, np.size(Au, 0)):          # Ciclo que recorre cada fila
        for j in range(i+1, np.size(Au, 0)):    # Ciclo que recorre cada columna
            filaux=(1.0/Au[i,i])*Au[i,:]        # Cada pivote es dividido por él mismo
            filaux=(-1.0*Au[j,i])*filaux        # Se deja 0 debajo de los pivotes
            Au[j,:]=Au[j,:]+filaux              # Se reemplaza por el valor dado

    print(Au)                                   # Se imprime la matriz aumentada que arroja el método de Gauss

    x=np.zeros((N,1))                           # Se crea una matriz de ceros que será posteriormente actualizada
    for i in range(np.size(Au, 0) - 1, -1, -1): # Ciclo que permite obtener la solución de cada variable
        sumaux=0
        for j in range(i+1, np.size(A, 0)):     # Se recorren las columnas
            sumaux=sumaux+Au[i, j]*x[j]

        x[i]=(1.0/Au[i, i])*(Au[i, np.size(Au, 1) - 1]-sumaux)  # Se obtiene el vector 'x' que tiene la solución de las incógnitas
    print("Solución por Gauss: \n", x)
    return [x]

'''Solución por medio de la función Gauss'''
Gauss(A,b,3)

'''Solución por medio Numpy'''
x1=np.linalg.solve(A,b)                         # Paquete linalg de Numpy para solucionar el sistema de ecuaciones
print("Solución de Numpy: \n",x1)

############################################
# 2. Para un sistema matricial de la forma Ax=b, donde A es una matriz de coeficientes constantes de NxN,
# x un vector de incógnitas de Nx1 y b un vector contantes de Nx1, realice una función en Python que devuelva
# el vector de solución x usando el método de Gauss-Jordan. La función debe devolver igualmente la matriz inversa A-1.
# Pruebe la función con una matriz A aleatoria (rand) de 3x3 y un vector b aleatorio de 3x1. Compare la solución
# encontrada con las funciones de la librería numpy del paquete linalg.

def Gauss_Jordan(A,b):
    Au=np.concatenate((A,b),1)                  # Concatenación de la matriz A de coeficientes y el vector solución b.
    for i in range(0, np.size(Au, 0)):          # Ciclo que recorre cada fila
        Au[i, :] = (1.0/Au[i,i])*Au[i, :]       # Cada pivote es dividido por él mismo
        for j in range(0, np.size(Au, 0)):      # Ciclo que recorre cada columna
            if i == j:                          # Condición que evalúa los pivotes. Si es un pivote, salta a la siguiente fila
                continue
            filaux=(-1.0*Au[j,i])*Au[i,:]       # Se deja 0 debajo de los pivotes
            Au[j,:]=Au[j,:]+filaux              # Se reemplaza por el valor dado

    x2 = Au[:, np.size(Au, 1)-1]                # Se obtiene el vector x2 que contiene la solución de las incógnitas.
    print(Au)

    print("Solución por Gauss-Jordan: \n", x2)
    return [x2]

'''Solución por medio de la función Gauss-Jordan'''
Gauss_Jordan(A,b)

'''Solución por medio Numpy'''
x1=np.linalg.solve(A,b)                         # Paquete linalg de Numpy para solucionar el sistema de ecuaciones
print("Solución de Numpy: \n",x1)
##
def Inversa(A):
    identidad = np.identity(3)
    Au = np.concatenate((A, identidad), 1)      # Concatenación de la matriz A de coeficientes y el vector solución b.
    for i in range(0, np.size(Au, 0)):          # Ciclo que recorre cada fila
        Au[i, :] = (1.0/Au[i,i])*Au[i, :]       # Cada pivote es dividido por él mismo
        for j in range(0, np.size(Au, 0)):      # Ciclo que recorre cada columna
            if i == j:                          # Condición que evalúa los pivotes. Si es un pivote, salta a la siguiente fila
                continue
            filaux=(-1.0*Au[j,i])*Au[i,:]       # Se deja 0 debajo de los pivotes
            Au[j,:]=Au[j,:]+filaux              # Se reemplaza por el valor dado

    x2 = Au[:, np.size(Au, 1)-1]                # Se obtiene el vector x2 que contiene la solución de las incógnitas.

    print("Matriz Aumentada: \n", Au)

    inv = np.array(Au[:, 3:])
    print("Matriz Inversa: \n", inv)

Inversa(A)
###############################################
# 3). Para el sistema matricial de la forma Ax=b, explique cada uno de los casos en los cuales el sistema
# tiene una única solución, infinitas soluciones o no tiene solución. Refiérase a la matriz aumentada
# para explicar cada caso.

# Única solución
# Sistema consistente o compatible es aquel en el que cada variable en la matriz tiene sólo un posible valor. Es decir, existe un número
# igual de variables y filas diferentes a cero.
#   "Matriz reducida"
#   [a a -a, e]
#   [0 -a e, h]
#   [0 0 a, -a]
#
# Infinita solución
# Sistema consistente el cual tiene mayor número de variables que de filas diferentes a cero en la
# matriz reducida.
# Ejemplo:
#   "Matriz aumentada"              "Matriz reducida"
#   [-c -e g, j]                      [a 0-g, -e]
#   [-a 0 g, e]                       [0 b -c, a]
#   [a a j, -d]                       [0 0 0, 0]
#
#En la última fila de la matriz reducida es un sistema de 0's. Esto significa que, para cualquier valor de Z
# habrá una única solución de X y Y.

# No Solución
# Un sistema de ecuaciones no tiene solución en los casos donde se produzca 0=1, es decir, si el sistema
# de ecuaciones es inconsistente.
# Ejemplo:
#   "Matriz aumentada"              "Matriz reducida"
#   [a a a, b]                      [a 0 d, a]
#   [0 a -c, a]                     [0 a -c, a]
#   [b a e, 0]                      [0 0 0, -c]
#
# En la última fila de la matriz reducida se tiene 0x+0y+0z=-c lo cual no es posible, pues 0 no puede ser igual a -c.
# Por lo tanto, el sistema no tiene solución.
#
#
#REFERENCIAS
#https://chbe241.github.io/Module-0-Introduction/MATH-152/Unique%20Solution,%20No%20Solution,%20or%20Infinite%20
# Solutions.html
# https://www.math.tamu.edu/~jlewis/Threetypesofsolsets.htm
# https://www.math.utah.edu/~gustafso/s2008/threePossibilitiesRankSymbol-k.pdf

###############################################
# 4) El círculo que pasa por los puntos (-2, 0), (-7, 1) y (5, -1) está dado por la ecuación x2+y2+ax+by+c=0.
# Utilice las funciones desarrolladas en los puntos 1 y 2 para hallar los coeficientes a, b y c. Compare la solución
# encontrada con las funciones de la librería numpy del paquete linalg. Realice una gráfica del círculo encontrado
# para 50 valores (x, y) equidistantes alrededor del círculo.


# Se ingresa la matríz de coeficientes A y el vector solución b
A = np.array([[-2.0,0,1.0],[-7.0,1.0,1.0],[5.0,-1.0,1.0]])
b = np.array([[-4],[-50],[-26]])


# Solucionamos el sistema Ax = b, usando el método de reducción de Gauss
#X = Gauss(A,b,3)  # A la variable 'X' asignamos el resultado para a,b y c que arroja el método de Gauss
X = Gauss_Jordan(A,b)

'''
Observación 1:

La ecuación del círculo está dada por: (x-po)^2 + (y-p1)^2 = r^2 (círculo de radio r, centrado en el punto po,p1)

    - La ecuación anterior es equivalente a: x^2 + y^2 + ax + by + c = 0

    - Los puntos po y p1 son: 
            po = -(a/2),   p1 = -(b/2)
            
    - El radio r es:
            r = sqrt(po^2 + p1^2 - c)
'''

# Hallamos los puntos po, p1 y el radio del círculo 'r'
po = -(X[0][0]/2)
p1 = -(X[0][1]/2)
r = np.sqrt(po**2 + p1**2 - (X[0][2]))

'''
Observación 2:

La gráfica del círculo se define mediante coordenadas polares.

Recordar:
    -> x = po + r*cos(theta)
    -> y = p1 + r*sen(theta)
'''
theta = np.linspace(0, 2 * np.pi, 100)  # Ángulo theta, de 0 a 2*pi

# Se grafica el círculo
plt.plot(po + r * np.cos(theta), p1 + r * np.sin(theta), color='c', lw='2')
plt.title(f'Círculo: $x^2 + y^2 + a \ x + b \ y + c = 0$', fontsize=10)
plt.axis('equal')


# Se grafican los 50 puntos equidistantes sobre el círculo
theta50 = np.linspace(0, 2 * np.pi, 50)  # Ángulo theta, de 0 a 2*pi
plt.plot(po + r * np.cos(theta50), p1 + r * np.sin(theta50), 'o', color='y', lw='2')
plt.title(f'Círculo: $x^2 + y^2 + a \ x + b \ y + c = 0$', fontsize=10)
plt.axis('equal')



##############################################

#5. Un polinomio de orden 4 está dado por la ecuación P(x) = c4 x^4 + c3 x^3 + c2 x^2 + c1 x + c0 , donde
# c4, c3, c2, c1 y c0 corresponden a coeficientes constantes. Encuentre la ecuación P(x) del polinomio de orden
# 4 que pasa por los puntos (-2.68, 0), (-3.25, 1.15), (-4.45, -1.56), (-6.25, -2.84) y (-8.15, 0.23).
# Utilice las funciones desarrolladas en los puntos 1 y 2 para hallar los coeficientes requeridos. Compare
# la solución encontrada con las funciones de la librería numpy del paquete linalg. Realice una gráfica del
# polinomio encontrado para x=−8.15:0.1:−2.68 .

# Se ingresa la matríz de coeficientes A y el vector solución b
A = np.array([[(-2.68)**4, (-2.68)**3, (-2.68)**2, (-2.68), 1],
              [(-3.25)**4, (-3.25)**3, (-3.25)**2, (-3.25), 1],
              [(-4.45)**4, (-4.45)**3, (-4.45)**2, (-4.45), 1],
              [(-6.25)**4, (-6.25)**3, (-6.25)**2, (-6.25), 1],
              [(-8.15)**4, (-8.15)**3, (-8.15)**2, (-8.15), 1]])

b = np.array([[0],[1.15],[-1.56],[-2.84],[0.23]])

# Solución por el método de Gauss
X = Gauss(A,b,5)

# Solución por el método de Gauss - Jordan
#X = Gauss_Jordan(A,b)

#Se define el polinomio y los valores de la variable independiente 'x'
x = np.linspace(-10,10,1000)
Px = X[0][0] * (x)**4 + X[0][1] * (x)**3 + X[0][2] * (x)**2 + X[0][3] * (x) + X[0][4]

# Gráfica del polinomio
plt.plot(x,Px, color='y')
plt.xlim(-8.15, -2.68)
plt.ylim(-4, 2)
plt.grid(True)
plt.show()


##########
A = np.array([[float(input("Ingrese el elemento ({},{}) de la matriz A:".format(columnas + 1, filas + 1))) for filas in range(0, N)] for columnas in range(0, N)])
print(A)
b = np.array([[float(input("Ingrese el elemento ({},{}) de la matriz b:".format(filas + 1, columnas + 1))) for filas in range(1)]for columnas in range(0, N)])
print(b)