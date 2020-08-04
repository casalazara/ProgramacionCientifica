
'''
                    Laboratorio 3: Numpy and Matplotlib
                          Programación Científica
                          Universidad de los Andes
Author: Nicolás Reyes
'''

##
# 1) Escriba una función que multiplique todos los números de un arreglo (lista).

def Mul(array):
    mul = 1     # Variable para actualizar la multiplicación
    for x in array:
        mul = mul * x   # Se multiplica cada elemento del array entre sí mediante el uso de un ciclo for, que recorre el vector de números.

    return print("La multiplicación de los elementos del arreglo:", array, "es: ", mul)

num = str.split(input('Ingrese el arreglo de números separados por una , . Ejemplo: 2,3,2,1,4'), ",") # Ingrese el arreglo (array) de la forma: x,x,x,x,x,x,...,x. La función 'split(",")' permite obtener cada elemento que está dentro de ,
num = list(map(int, num))      # La función 'map(function, iterable, ...)' permite aplicar una función (function) a cada elemento de la lista. En este caso, cada elemento de la lista se pasa a entero (int)

res = Mul(num)                 # Se llama la función "Mul" que permite multiplicar los números del arreglo ingresado (num)


## 2) Escriba una función que calcule el factorial de un número entero positivo


def factorial (n):
    if n >= 0:            # Aseguramos que sólo sirva para números enteros positivos
        if (n == 0):
            return 1      # El factorial de 0 es 1
        else:
            return n * factorial(n-1)      # Hallamos el n factorial!
    else:
        return print("ERROR: El número debe ser un entero positivo")

x = int(input("Ingrese el número (n) para conocer su factorial "))   # Ingrese el número n para conocer su factorial: (n!)
print ("El factorial de ",x," es: ", factorial(x))                   # Se muestra el resultado de n!


## 3) Escriba una función que indique si un número entero positivo es primo o no

def Primo(x):
    i = 2   # Los números primos empiezan desde 2

    while i < x:
        if x % i == 0:          # Se determina si el número x es divisible por números diferentes a 1 y el mismo.
            return print("El número",x,"NO es primo")
        i = i + 1
    if x == 1 or x ==0:         # Los números 0 y 1 No son primos
        return print("El número",x,"NO es primo")
    return print("El número",x,"Sí es primo")

x = int(input("Ingrese el número (n) para saber si es un número primo "))   # Ingrese el número n para conocer si es primo (Que solo se pueda dividir por 1 y el mismo)
Primo(x)


## 4) Escriba una función que indique si una cadena de caracteres es palíndrome o no.

def Palindrome(palabra):
    reverse = ''.join(reversed(palabra))   # reverse es la palabra ingresada pero al revés

    if (palabra == reverse):               # Se revisa si la palabra original y la que está al contrario son iguales
        return "es palindrome"             # Return es palindrome si cumple la condición anterior
    return "no es palindrome"

# Palabras palídromas de prueba
s1 = "sometemos"
s2 = "arenera"

print("La palabra:",s2,',',Palindrome(s2)) # Se imprime el resultado. Es palindrome o no.


## 5) Escriba una función que indique si un número entero positivo pertenece a la serie de Fibonacci.

def Fibonacci(numero):
    #primero hago la serie de fibonacci
    esParte = ",No hace parte de la serie de Fibonacci"
    l = [0,1]       # Los primeros números de la serie son: 0 y 1
    agregar = 0
    i = 0

    while (agregar < numero):       # Se implementa un bucle while que garantiza obtener la serie de Fibonacci hasta el número ingresado
        agregar = (l[i] + l[i+1])   # La serie de Fibonacci en la posición i se define al sumar los 2 números anteriores de forma sucesiva
        l.append(agregar)           # Se agrega cada elemento de la serie a un vector definido anteriormente
        i += 1

    if (l[len(l) -1] == numero):    # Este condicional determina si el número ingresado es igual al último de la serie de Fibonacci calculada anteriormente
        esParte = ",Si hace parte de la serie de Fibonacci"
    print(l)
    return esParte

num = int(input("Ingrese un número n para determinar si hace parte de la serie de Fibonacci"))    # Se ingresa el número que se desea identificar si pertenece o no a la serie de Fibonacci
print('El número',num,Fibonacci(num))

## 6) Escriba una función que calcule la media de cada una de las filas o columnas de una matriz.

def MediaMatriz(matriz, flag):
    # flag es una variable booleana. Si es verdadera calcula el promedio de las filas, si no el de las columnas
    print(matriz)

    if flag:
        promFilas = []
        for i in range(0, len(matriz)):
            prom = 0
            for j in range(0, len(matriz[0])):
                prom = prom + matriz[i][j]
            prom = prom / len(matriz)               # Promedio de los valores en las filas
            promFilas.append(prom)                  # El promedio de cada fila va ser la n-ésima fila de un vector
        return promFilas
    else:
        promCols = []
        for i in range(0, len(matriz[0])):
            prom = 0
            for j in range(0, len(matriz)):
                prom = prom + matriz[j][i]
            prom = prom / len(matriz[0])            # Promedio de los valores en las columnas
            promCols.append(prom)                   # El promedio de cada columna va ser la n-ésima columna de un vector
        return promCols

N = int(input('Número de filas: '))                 # Se le pide al usuario el número de filas de la matriz
M = int(input('Número de columnas: '))              # Se le pide al usuario el número de columnas de la matriz

mat = [[int(input('ingrese los valores de la matriz: ')) for filas in range(M)] for columnas in range(N)] # Se ingresan los valores de la matriz

res = MediaMatriz(mat, True)                     # Se calcula la media de las filas de la matriz (flag = True)
print("Promedio de cada fila:",res)

res = MediaMatriz(mat, False)                    # Se calcula la media de las columnas de la matriz (flag = False)
print("Promedio de cada columna:",res)


## 7) Escriba una función que calcule el máximo de cada una de las filas o columnas de una matriz.

def MaxMatriz(matriz7, filcol):
    print(matriz7)
    max = []

    if filcol == 1:
        for i in range(0, len(matriz7)):
            maximo = matriz7[i][0]              # Se recorren las filas de la matriz ingresada al dejar fija la posición de las filas y avanzando sobre las columnas.
            for j in range(0,len(matriz7[0])):
                if matriz7[i][j] > maximo:     # En cada fila se establece el primer elemento como el maximo y se va comparando con los elemntos siguientes, si alguno resulta ser mayor este se convierte en el nuevo maximo.
                    maximo = matriz7[i][j]
            max.append(maximo)
        return print("El máximo de cada fila es", max)   # Se determina el máximo de cada fila

    elif filcol == 0:
        for a in range(0, len(matriz7[0])):
            maximo = matriz7[0][a]             # Similar al anterior, ahora se deja fija la posicion de la columna
            for b in range(0, len(matriz7)):
                if matriz7[b][a] > maximo:
                    maximo = matriz7[b][a]
            max.append(maximo)
    return print("El máximo de cada columna es", max)     # Se determina el máximo de cada columna

N = int(input('Número de filas: '))                 # Se le pide al usuario el número de filas de la matriz
M = int(input('Número de columnas: '))              # Se le pide al usuario el número de columnas de la matriz

mat = [[int(input('Ingrese los valores de la matriz: ')) for filas in range(M)] for columnas in range(N)] # Se ingresan los valores de la matriz
f = int(input('Ingrese "1" si desea conocer el maximo de las filas o "0" si desea conocer el de las columnas'))

MaxMatriz(mat, f)


## 8) Escriba una función que calcule el mínimo de cada una de las filas o columnas de una matriz.

def MinMatriz(matriz8, filcol):
    print(matriz8)
    min = []
    if filcol == 1:
        for i in range(0, len(matriz8)):
            minimo = matriz8[i][0]                 # Se recorren las filas de la matriz ingresada al dejar fija la posición de las filas y avanzando sobre las columnas.
            for j in range(0,len(matriz8[0])):
                if matriz8[i][j] < minimo:         # En cada columna se establece el primer elemento como el mínimo y se va comparando con los elementos siguientes, si alguno resulta ser mayor este se convierte en el nuevo mínimo.
                    minimo = matriz8[i][j]
            min.append(minimo)
        return print("El mínimo de cada fila es", min)  # Se determina el mínimo de cada fila

    elif filcol == 0:
        for a in range(0, len(matriz8[0])):
            minimo = matriz8[0][a]                 # Similar al anterior, ahora se deja fija la posicion de la columna
            for b in range(0, len(matriz8)):
                if matriz8[b][a] < minimo:
                    minimo = matriz8[b][a]
            min.append(minimo)
    return print("El mínimo de cada columna es", min)  # Se determina el mínimo de cada columna

N = int(input('Número de filas: '))                 # Se le pide al usuario el número de filas de la matriz
M = int(input('Número de columnas: '))              # Se le pide al usuario el número de columnas de la matriz

mat = [[int(input('Ingrese los valores de la matriz: ')) for filas in range(M)] for columnas in range(N)] # Se ingresan los valores de la matriz
f = int(input('Ingrese "1" si desea conocer el mínimo de las filas o "0" si desea conocer el de las columnas'))

MinMatriz(mat, f)


## 9) Escriba una función que devuelva la matriz resultante de la suma entre dos matrices de igual tamaño.

def SumMatrices(matrizA, matrizB):
    print("Matriz A:",matrizA)
    print("Matriz B:", matrizB)

    matrizC = [[matrizA[i][j] + matrizB[i][j] for j in range(len(matrizA[0]))] for i in range(len(matrizA))] # Se suma elemento a elemento la matriz A y B. La suma es una nueva matriz C.
    return print("La suma de las matrices A y B es:", matrizC)

filas = int(input('Número de filas: '))                 # Se le pide al usuario el número de filas de la matriz
colum = int(input('Número de columnas: '))              # Se le pide al usuario el número de columnas de la matriz

matrizA = [[int(input('Ingrese los valores de la primera matriz: ')) for columnasA in range(colum)] for filasA in range(filas)] # Se ingresan los valores de la matriz A
matrizB = [[int(input('Ingrese los valores de la segunda matriz: ')) for columnasB in range(colum)] for fiasB in range(filas)]  # Se ingresan los valores de la matriz B

SumMatrices(matrizA, matrizB)


## 10) Escriba una función que devuelva la matriz resultante de la multiplicación elemento por elemento entre dos matrices de igual tamaño.

def MulMatrices(matrizA, matrizB):
    print("Matriz A:",matrizA)
    print("Matriz B:", matrizB)

    matrizC = [[matrizA[i][j] * matrizB[i][j] for j in range(len(matrizA[0]))] for i in range(len(matrizA))] # Se multiplica elemento a elemento la matriz A y B. La multiplicación es una nueva matriz C.
    return print("La multiplicación de las matrices A y B es:", matrizC)

filas = int(input('Número de filas: '))                 # Se le pide al usuario el número de filas de la matriz
colum = int(input('Número de columnas: '))              # Se le pide al usuario el número de columnas de la matriz

matrizA = [[int(input('Ingrese los valores de la primera matriz: ')) for columnasA in range(colum)] for filasA in range(filas)] # Se ingresan los valores de la matriz A
matrizB = [[int(input('Ingrese los valores de la segunda matriz: ')) for columnasB in range(colum)] for fiasB in range(filas)]  # Se ingresan los valores de la matriz B

MulMatrices(matrizA, matrizB)




###########################################
## 11) Realice los puntos del 6 al 10 usando funciones de la librería numpy para Python y funciones de la librería nativa de Matlab.

# 11.1) Escriba una función que calcule la media de cada una de las filas o columnas de una matriz.
import numpy as np
from matplotlib import pyplot as plt

def MediaMatriz (matriz, flag):
    print("Matriz A:", matriz)

    # Inicialización de la matrices
    Mat = np.array(np.mat(matriz))

    if (flag):
        #1 hace el promedio sobre las filas
        promedio = Mat.mean(1)
    else:
        # 0 hace el promedio sobre las columnas
        promedio = Mat.mean(0)
    return promedio

N = int(input('Número de filas: '))                 # Se le pide al usuario el número de filas de la matriz
M = int(input('Número de columnas: '))              # Se le pide al usuario el número de columnas de la matriz

mat = [[int(input('ingrese los valores de la matriz: ')) for filas in range(M)] for columnas in range(N)] # Se ingresan los valores de la matriz

res = MediaMatriz(mat, True)                     # Se calcula la media de las filas de la matriz (flag = True)
print("Promedio de cada fila:",res)

res = MediaMatriz(mat, False)                    # Se calcula la media de las columnas de la matriz (flag = False)
print("Promedio de cada columna:",res)

## 11.2) Escriba una función que calcule el máximo de cada una de las filas o columnas de una matriz.

import numpy as np
from matplotlib import pyplot as plt

def MaxMatriz (matriz, flag):
    print("Matriz A:", matriz)

    # Inicialización de la matrices
    Mat = np.array(np.mat(matriz))

    if (flag):
        maximo = Mat.max(1)             # max(1): Halla el máximo de cada fila
        return print("El máximo de cada fila es", maximo)
    else:
        maximo = Mat.max(0)             # max(0): Halla el máximo de cada columna
    return print("El máximo de cada columna es", maximo)

N = int(input('Número de filas: '))                 # Se le pide al usuario el número de filas de la matriz
M = int(input('Número de columnas: '))              # Se le pide al usuario el número de columnas de la matriz

mat = [[int(input('Ingrese los valores de la matriz: ')) for filas in range(M)] for columnas in range(N)] # Se ingresan los valores de la matriz
f = int(input('Ingrese "1" si desea conocer el maximo de las filas o "0" si desea conocer el de las columnas'))

MaxMatriz(mat, f)


## 11.3) Escriba una función que calcule el mínimo de cada una de las filas o columnas de una matriz.

import numpy as np
from matplotlib import pyplot as plt

def MinMatriz (matriz, flag):
    print("Matriz A:", matriz)

    # Inicialización de la matrices
    Mat = np.array(np.mat(matriz))

    if (flag):
        minimo = Mat.min(1)             # max(1): Halla el mínimo de cada fila
        return print("El mínimo de cada fila es", minimo)
    else:
        minimo = Mat.min(0)             # max(0): Halla el mínimo de cada columna
    return print("El mínimo de cada columna es", minimo)

N = int(input('Número de filas: '))                 # Se le pide al usuario el número de filas de la matriz
M = int(input('Número de columnas: '))              # Se le pide al usuario el número de columnas de la matriz

mat = [[int(input('Ingrese los valores de la matriz: ')) for filas in range(M)] for columnas in range(N)] # Se ingresan los valores de la matriz
f = int(input('Ingrese "1" si desea conocer el mínimo de las filas o "0" si desea conocer el de las columnas'))

MinMatriz(mat, f)


## 11.4) Escriba una función que devuelva la matriz resultante de la suma entre dos matrices de igual tamaño.

def SumMatrices(matrizA, matrizB):

    print("Matriz A:", matrizA)
    print("Matriz B:", matrizB)

    # Inicialización de la matrices
    Mat1 = np.array(np.mat(matrizA))
    Mat2 = np.array(np.mat(matrizB))

    if (Mat1.shape == Mat2.shape):
        Suma = np.add(Mat1, Mat2)

        # Retorna la matriz resultante
        return print("La suma de las matrices A y B es: \n", Suma)
    else:
        Suma = "Las matrices no tienen la misma dimension"
    return Suma


filas = int(input('Número de filas: '))                 # Se le pide al usuario el número de filas de la matriz
colum = int(input('Número de columnas: '))              # Se le pide al usuario el número de columnas de la matriz

matrizA = [[int(input('Ingrese los valores de la primera matriz: ')) for columnasA in range(colum)] for filasA in range(filas)] # Se ingresan los valores de la matriz A
matrizB = [[int(input('Ingrese los valores de la segunda matriz: ')) for columnasB in range(colum)] for fiasB in range(filas)]  # Se ingresan los valores de la matriz B

SumMatrices(matrizA, matrizB)


## 11.5) Escriba una función que devuelva la matriz resultante de la multiplicación elemento por elemento
#entre dos matrices de igual tamaño.

def MulMatrices(n,m):

    print("Matriz A:",matrizA)
    print("Matriz B:", matrizB)

    # Inicialización de las matrices
    N = np.array(np.mat(n))
    M = np.array(np.mat(m))

    # Dimensiones de las matrices
    n = np.shape(N)[0]
    m = np.shape(N)[1]

    # Verifica si se pueden multiplicar
    if n == np.shape(M)[0] and m == np.shape(M)[1]:

        #Utiliza la funcionalidad de multiplicar elemento por elemento de numpy
        R = N*M

        #Retorna la matriz resultante
        return print("La multiplicación de las matrices A y B es: \n", R)
    else:
        print("Las matrices no son de igual tamanio")

filas = int(input('Número de filas: '))                 # Se le pide al usuario el número de filas de la matriz
colum = int(input('Número de columnas: '))              # Se le pide al usuario el número de columnas de la matriz

matrizA = [[int(input('Ingrese los valores de la primera matriz: ')) for columnasA in range(colum)] for filasA in range(filas)] # Se ingresan los valores de la matriz A
matrizB = [[int(input('Ingrese los valores de la segunda matriz: ')) for columnasB in range(colum)] for fiasB in range(filas)]  # Se ingresan los valores de la matriz B

MulMatrices(matrizA, matrizB)

###########################################



## 12) Usando funciones de las librerías numpy y matplotlib para Python y nativas de Matlab, grafique funciones seno entre 0 y 10 segundos, que oscilen a frecuencias de 1 a 10 Hz con pasos de 1 Hz. Grafique la función sinusoidal vs. tiempo.

import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0,10,1000)              # Se define el tiempo de (0s) a (10s)

for freq in range(1,11):                # Bucle que varia la frecuencia. Esta oscila de 1 a 10 Hz con pasos de 1 Hz.
    y = np.sin(2 * np.pi * (freq*t))    # Se calcula la función seno para cada frecuencia
    plt.subplot(5,2,freq)               # Se crea un subplot de 5 filas y 2 columnas
    plt.plot(t,y)                       # Graficamos cada funcion seno resultante
    plt.title(['Frecuencia = ', freq, 'Hz'])    # Nombre de cada subplot para cada frecuencia
    plt.tight_layout()                  # Función que dá propiedades a cada subplot para que se ajusten adecuadamente en la figura.
plt.show()                              # Se muestra la figura


## 13) Usando funciones de las librerías numpy y matplotlib para Python y nativas de Matlab, obtenga 10000 valores aleatorios con distribución uniforme y grafique el correspondiente histograma para un número de divisiones de 10, 20, 30 y 50 particiones.

import numpy as np
from matplotlib import pyplot as plt

for x in range(1, 5):                   # Bucle que recorre las 4 divisiones
    bins = [10, 20, 30, 50]             # Las diferentes divisiones

    plt.subplot(2, 2, x)                # Se define un subplot de 2 filas y 2 columnas
    y = np.random.uniform(0,1,10000)    # Con la función "random.uniform" se obtiene un número ramdom de números con distribución uniforme de probabilidad. En este caso, se generan 10000 números aleatorios.
    plt.hist(y, bins=bins[x-1],color='green')       # Se grafica el histograma de y con en correspondiente numéro de divisiones (bin) del histograma.
    plt.title(['Bin = ', bins[x-1]])    # Nombre de cada subplot para cada bin
    plt.tight_layout()
plt.show()



## 14) Usando funciones de las librerías numpy y matplotlib para Python y nativas de Matlab, obtenga 10000 valores aleatorios con distribución normal y grafique el correspondiente histograma para un número de divisiones de 10, 20, 30 y 50 particiones.

import numpy as np
from matplotlib import pyplot as plt

for x in range(1, 5):                   # Bucle que recorre las 4 divisiones
    bins = [10, 20, 30, 50]             # Las diferentes divisiones

    plt.subplot(2, 2, x)                # Se define un subplot de 2 filas y 2 columnas
    y = np.random.normal(0,1,10000)     # Con la función "random.normal" se obtiene un número ramdom de números con distribución normal de probabilidad. En este caso, se generan 10000 números aleatorios.
    plt.hist(y, bins=bins[x-1],color='c')       # Se grafica el histograma de y con en correspondiente numéro de divisiones (bin) del histograma.
    plt.title(['Bin = ', bins[x-1]])    # Nombre de cada subplot para cada bin
    plt.tight_layout()
plt.show()










#########################

#           "Ejemplos de otros tipos de gráficas"

#########################

import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on sine and cosine curves
x = np.linspace(0, 3 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(2, 1, 1)

# Make the first plot
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show()

##
from matplotlib import pyplot as plt
x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]
plt.bar(x, y, align = 'center')
plt.bar(x2, y2, color = 'g', align = 'center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

##
import numpy as np
import matplotlib.pyplot as plt
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, density=1)       # matplotlib version (plot)
plt.show()

##
import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def lorenz(x, y, z, s=10, r=28, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.01
num_steps = 10000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)


# Plot
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()