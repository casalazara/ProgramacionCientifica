## Punto 1
numero = int(input("Ingrese un numero"))


def esFibonacci(numero, prev=0, sig=1):
    if (numero == prev or numero == sig):
        return True
    elif (prev + sig > numero):
        return False
    else:
        return esFibonacci(numero, prev + sig, prev + sig + sig)


print(esFibonacci(numero))
## Punto 2
numero = int(input("Ingrese un numero"))


def perteneceSerieCuadrada(numero, n=1):
    if (n ** 2 == numero):
        return True
    elif (n ** 2 > numero):
        return False
    else:
        return perteneceSerieCuadrada(numero, n + 1)


print(perteneceSerieCuadrada(numero))
## Punto 3
s = int(input("Ingrese el exponente"))
n = int(input("Ingrese el número de términos"))


# Lo necesito para las recursiones
def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)


def taylorExp(s, n):
    if (n == 0):
        return 1
    else:
        return (s ** n) / factorial(n) + taylorExp(s, n - 1)


print(taylorExp(s, n))
## Punto 4
s = int(input("Ingrese el ángulo"))
n = int(input("Ingrese el número de términos"))


# Lo necesito para las recursiones
def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)


def taylorSeno(s, n):
    if (n == 0):
        return ((((-1) ** 0)*(s ** ((2 * 0) + 1))) / factorial((2 * 0) + 1))
    else:
        return ((((-1) ** n)*(s ** ((2 * n) + 1))) / factorial((2 * n) + 1)) + taylorSeno(s, n - 1)


print(taylorSeno(s, n))
## Punto 5
s = int(input("Ingrese el ángulo"))
n = int(input("Ingrese el número de términos"))


# Lo necesito para las recursiones
def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)


def taylorCoseno(s, n):
    if (n == 0):
        return ((((-1) ** 0)*(s ** (2 * 0))) / factorial(2 * 0))
    else:
        return ((((-1) ** n)*(s ** (2 * n))) / factorial(2 * n)) + taylorCoseno(s, n - 1)


print(taylorCoseno(s, n))
## Punto 6

import matplotlib.pyplot as mp
import math

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)


def taylorExp(s, n):
    if (n == 0):
        return 1
    else:
        return ((s ** n) / factorial(n)) + taylorExp(s, n - 1)


def evalTaylorExp():
    y = []
    x = []
    absoluto = []
    relativo = []
    for i in range(10, 1010, 10):
        x.append(i)
        z = taylorExp(10, i)
        vReal = math.exp(10)
        y.append(z)

        a = abs(vReal - z)
        absoluto.append(a)

        r = (a / vReal) * 100
        relativo.append(r)

    mp.subplot(2, 2, 1)
    mp.title("Apróximado")
    mp.plot(x, y)

    mp.subplot(2, 2, 2)
    mp.title("Error absoluto")
    mp.plot(x, absoluto)

    mp.subplot(2, 2, 3)
    mp.title("Error relativo")
    mp.plot(x, relativo)
    mp.show()
evalTaylorExp()

## Punto 7

import matplotlib.pyplot as mp
import math

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)


def taylorSeno(s, n):
    if (n == 0):
        return s
    else:
        return (((-1) ** n)*(s ** ((2 * n) + 1))) / factorial((2 * n) + 1) + taylorSeno(s, n - 1)


def evalTaylorSeno():
    y = []
    x = []
    absoluto = []
    relativo = []
    for i in range(10, 1010, 10):
        x.append(i)
        z = taylorSeno(6, i)
        vReal = math.sin(6)
        y.append(z)

        a = abs(vReal - z)
        absoluto.append(a)

        r = (a / vReal) * 100
        relativo.append(r)
    mp.subplot(2, 2, 1)
    mp.title("Apróximado")
    mp.plot(x, y)

    mp.subplot(2, 2, 2)
    mp.title("Error absoluto")
    mp.plot(x, absoluto)

    mp.subplot(2, 2, 3)
    mp.title("Error relativo")
    mp.plot(x, relativo)

    mp.show()
evalTaylorSeno()
## Punto 8
import matplotlib.pyplot as mp
import math
def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)

def taylorCoseno(s, n):
    if (n == 0):
        return ((((-1) ** 0)*(s ** (2 * 0))) / factorial(2 * 0))
    else:
        return ((((-1)** n)*(s** (2 * n))) / factorial(2 * n)) + taylorCoseno(s, n - 1)

def evalTaylorCoseno():
    y = []
    x = []
    absoluto = []
    relativo = []
    for i in range(10, 1010, 10):
        x.append(i)
        z = taylorCoseno(3, i)
        vReal = math.cos(3)
        y.append(z)

        a = abs(vReal - z)
        absoluto.append(a)

        r = (a / vReal) * 100
        relativo.append(r)

    mp.subplot(2, 2, 1)
    mp.title("Apróximado")
    mp.plot(x, y)

    mp.subplot(2, 2, 2)
    mp.title("Error absoluto")
    mp.plot(x, absoluto)

    mp.subplot(2, 2, 3)
    mp.title("Error relativo")
    mp.plot(x, relativo)
    mp.show()
evalTaylorCoseno()
##9
import numpy as np
arreglo=np.linspace(-10,10,1000,dtype='int16')
writer=open("FileBinInt16.bin","ab")
writer.write(arreglo)
writer.close()
##10
import numpy as np
leido = np.fromfile('FileBinInt16.bin', dtype='int16')
mp.title("Gráfica")
mp.hist(leido, bins=30, density=1)
##11
import numpy as np
arreglo=np.linspace(-1,1,1000,dtype='float64')
writer=open("FileBinDouble.bin","ab")
writer.write(arreglo)
writer.close()
##12
import numpy as np
leido = np.fromfile('FileBinDouble.bin', dtype='float64')
mp.title("Gráfica")
mp.hist(leido, bins=30, density=1)
##13
import numpy as np
leido = np.fromfile('File-214.bin', dtype='uint32')
print(round(np.mean(leido),4)== 64023.8381) #Lo redondeé porque si no no dan iguales
## 14
import numpy as np

def esFibonacci(numero, prev=0, sig=1):
    if (numero == prev or numero == sig):
        return True
    elif (prev + sig > numero):
        return False
    else:
        return esFibonacci(numero, prev + sig, prev + sig + sig)


leido = np.fromfile('File-214.bin', dtype='uint32')
contador=0
for numero in leido:
    if(esFibonacci(numero)):
        contador+=1
print("Hay "+str(contador)+" números que pertenecen a la serie de Fibonacci en el archivo")
## 15
import numpy as np
def perteneceSerieCuadrada(numero, n=1):
    if (n ** 2 == numero):
        return True
    elif (n ** 2 > numero):
        return False
    else:
        return perteneceSerieCuadrada(numero, n + 1)

leido = np.fromfile('File-214.bin', dtype='uint32')
contador=0
for numero in leido:
    if(perteneceSerieCuadrada(numero)):
        contador+=1
print("Hay "+str(contador)+" números que pertenecen a la serie cuadrada en el archivo")