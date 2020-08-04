'Hice los primeros puntos de forma recursiva creyendo que en este laboratorio entraba ese tema'
## 1 Punto
lista=[int(x) for x in input("Ingrese los numeros de la lista separados por espacio").split(" ")]
tamanio=len(lista)-1
def multiplicar(lista,tamanio):
    if(tamanio==0):
        return lista[0]
    else:
        return (lista[tamanio]*multiplicar(lista,tamanio-1))
print(multiplicar(lista,tamanio))
## 2 Punto
numero=int(input("Ingrese el número"))
def factorial(numero):
    if(numero==1):
        return 1
    else:
        return numero*factorial(numero-1)
print(factorial(numero))
## 3 Punto
numero=int(input("Ingrese el número"))
def esPrimo(n, i = 2):
    if (n <= 2):
        return True
    elif (n % i == 0):
        return False
    elif (i * i > n):
        return True
    else:
        return esPrimo(n, i + 1)
print(esPrimo(numero))
## 4 Punto
palabra=input("Ingrese la palabra")
def palindromo(palabra,i=0):
	if(i>=int(len(palabra)/2)):
		return True
	elif(palabra[i]!=palabra[len(palabra)-1-i]):
		return False
	else:
		return palindromo(palabra,i+1)
print(palindromo(palabra))
## 5 Punto
numero=int(input("Ingrese un numero"))
def esFibonacci(numero,prev=0,sig=1):
    if(numero==prev or numero==sig):
        return True
    elif(prev+sig>numero):
        return False
    else:
        return esFibonacci(numero,prev+sig,prev+sig+sig)
print(esFibonacci(numero))
## 6 Punto
matriz1 = [[1, 2, 3], [57, 64, 321], [21, 4, 2]]
def mediaMatriz(matriz1):
    rta=""
    rtaF = []
    for fila in matriz1:
        rtaF.append(sum(fila) / len(fila))
    rta+="Media por filas: "+ str(rtaF)+"\n"
    rtaC = []
    for j in range(len(matriz1[0])):
        suma = 0
        for i in range(len(matriz1)):
            suma += matriz1[i][j]
        rtaC.append(suma / len(matriz1))
    rta+="Media por columnas: "+str(rtaC)
    return rta
print(mediaMatriz(matriz1))
## 7 Punto
matriz1 = [[1, 2, 3], [57, 64, 321], [21, 4, 2]]
def mayorMatriz(matriz1):
    rta=""
    rtaF = []
    for fila in matriz1:
        rtaF.append(max(fila))
    rta+="Mayor por filas: "+str(rtaF)+"\n"
    rtaC = []
    for j in range(len(matriz1[0])):
        maximo = 0
        for i in range(len(matriz1)):
            if (matriz1[i][j] > maximo):
                maximo = matriz1[i][j]
        rtaC.append(maximo)
    rta+="Mayor por columnas: "+str(rtaC)
    return rta
print(mayorMatriz(matriz1))
## 8 Punto
matriz1 = [[1, 2, 3], [57, 64, 321], [21, 4, 2]]
def menorMatriz(matriz1):
    rta=""
    rtaF = []
    for fila in matriz1:
        rtaF.append(min(fila))
    rta+="Menor por filas: "+ str(rtaF)+"\n"
    rtaC = []
    for j in range(len(matriz1[0])):
        menor = matriz1[0][j]
        for i in range(len(matriz1)):
            if (matriz1[i][j] < menor):
                menor = matriz1[i][j]
        rtaC.append(menor)
    rta+="Menor por columnas: "+ str(rtaC)
    return rta
print(menorMatriz(matriz1))
## 9 Punto
matriz1=[[1,2,3],[57,64,321],[21,4,2]]
matriz2=[[1,4,51],[12,45,41],[1241,4,23]]
def sumarMatrices(matriz1,matriz2):
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            matriz1[i][j] += matriz2[i][j]
    return(matriz1)
print(sumarMatrices(matriz1,matriz2))
## 10 Punto
matriz1=[[1,2,3],[57,64,321],[21,4,2]]
matriz2=[[1,4,51],[12,45,41],[1241,4,23]]
def multiplicarMatrices(matriz1,matriz2):
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            matriz1[i][j] *= matriz2[i][j]
    return(matriz1)
print(multiplicarMatrices(matriz1,matriz2))
## 11.1 Punto
import numpy as np
matriz1=[[1,2,3],[57,64,321],[21,4,2]]
rtaF=np.mean(matriz1, axis=1)
rtaC=np.mean(matriz1, axis=0)
print("Media por filas: ", rtaF)
print("Media por columnas: ", rtaC)

## 11.2 Punto
import numpy as np
matriz1=[[1,2,3],[57,64,321],[21,4,2]]
rtaF=np.max(matriz1, axis=1)
rtaC=np.max(matriz1, axis=0)
print("Mayor por filas: ", rtaF)
print("Mayor por columnas: ", rtaC)

## 11.3 Punto
import numpy as np
matriz1=[[1,2,3],[57,64,321],[21,4,2]]
rtaF=np.min(matriz1, axis=1)
rtaC=np.min(matriz1, axis=0)
print("Menor por filas: ", rtaF)
print("Menor por columnas: ", rtaC)

## 11.4 Punto
import numpy as np
matriz1=np.array([[1,2,3],[57,64,321],[21,4,2]])
matriz2=np.array([[1,4,51],[12,45,41],[1241,4,23]])
print(matriz1+matriz2)

## 11.5 Punto
import numpy as np
matriz1=np.array([[1,2,3],[57,64,321],[21,4,2]])
matriz2=np.array([[1,4,51],[12,45,41],[1241,4,23]])
print(matriz1*matriz2)
## 12 Punto
import matplotlib.pyplot as mp
import numpy as np
t=np.linspace(0,10,1000)
f=np.sin(2*np.pi*t**2)
mp.plot(t,f,color='red')
mp.show()
## 13 Punto
import numpy as np
import matplotlib.pyplot as mp
v = np.random.uniform(0,1,10000)
mp.subplot(2,2,1)
mp.title("10 Particiones")
mp.hist(v, bins=10, density=1)

mp.subplot(2,2,2)
mp.title("20 Particiones")
mp.hist(v, bins=20, density=1)

mp.subplot(2,2,3)
mp.title("30 Particiones")
mp.hist(v, bins=30, density=1)

mp.subplot(2,2,4)
mp.title("50 Particiones")
mp.hist(v, bins=50, density=1)
mp.show()
## 14 Punto
import numpy as np
import matplotlib.pyplot as mp
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)
mp.subplot(2,2,1)
mp.title("10 Particiones")
mp.hist(v, bins=10, density=1)

mp.subplot(2,2,2)
mp.title("20 Particiones")
mp.hist(v, bins=20, density=1)

mp.subplot(2,2,3)
mp.title("30 Particiones")
mp.hist(v, bins=30, density=1)

mp.subplot(2,2,4)
mp.title("50 Particiones")
mp.hist(v, bins=50, density=1)
mp.show()