
##
#    "Laboratorio 4: Funciones recursivas y manejo de archivos"
#                    "Universidad de los Andes"

# Author: Julio Nicolás Reyes (Profesor Asistente)

##
# 1) Realice un función recursiva que permita determinar si un número entero positivo pertenece a la serie de Fibonacci.

def Fibonacci(Num, n0 = 0, n1 = 1):             # Se define una función que tiene como parámetros: Num: Número a veriificar en la serie,
                                                # n0 = Número inicial, n1 = Número siguiente
    if n1 == Num or n0 == Num:                  # Criterio de parada, si el número ingresado es igual al calculado en la serie
        return print("El número",Num,"pertenece a la serie Fibonacci")
    elif n1 > Num:                              # Criterio de parada, si el número no pertenece a la serie de Fibonacci
        return print("El número", Num, "NO pertenece a la serie Fibonacci")
    else:
        Fibo = Fibonacci(Num, n1, n0 + n1)      # Proceso recursivo que actualiza: n0 = n1 y n1 = n0 + n1, de esta forma va
                                                # creando la serie de Fibonacci
        return Fibo

Fibonacci(21)
Fibonacci(18)

##
# Ciclo que imprime todos los números de la serie hasta el 1000

for i in range(0, 1001):
    nu2check = i
    isfib = Fibonacci(nu2check, 0, 1)
    if isfib:
        print(str(nu2check) + " is Fib")


####################################################

# 2) Realice un función recursiva que permita determinar si un número entero positivo pertenece a la serie de cuadrada.
# (Un número pertenece a la serie cuadrada si la parte fraccionaria de su correspondiente raíz cuadrada es cero.
# Por ejemplo: 1, 4, 9, 16, 25, 36, 49, etc., es decir, si su raíz cuadrada es un número entero).

def SerieCuadrada(n, i=1):              # Función que tiene como parámetros: n=número a verificar y i=1 (Variable auxiliar para hacer la operación i*i)
    if i*i == n:                        # Criterio de parada, si el número ingresado es igual a un valor de la serie cuadrada.
                                        # Los valores de la serie se obtienen al hacer la operación i*i
        return print("El número",n,"pertenece a la serie cuadrada")
    elif i*i < n:                       # Criterio de parada, si el número ingresado es mayor al resultado de hacer i*i, esto
                                        # indica que el número NO pertenece a la serie cuadrada
        return SerieCuadrada(n,i+1)     # Proceso recursivo que actualiza a i = i+1, de esta forma se construye la serie cuadrada
    else:
        return print("El número", n, "NO pertenece a la serie cuadrada")

SerieCuadrada(16)
SerieCuadrada(8)


###################################################

# NOTA: Definimos la función para obtener el factorial de un número (x) de forma recursiva. Esta va ser útil para el desarrollo
#de los demás dejercicios del laboratorio.

def Factorial(x):
    factorial = 1
    if x == 0:
        return factorial
    else:
        factorial = x * Factorial(x - 1)
        return factorial

##################################################


# 3) Escriba una función recursiva que devuelva el valor de la serie de Taylor de e^(x) para un número real dado x
# y un número máximo de términos en la serie N.

'''
Nota: La serie de Taylor para e^(x) está dada por: 
        
        e^(x) = sumatoria(x^(n) / n!)
'''

def exp(x, n):          # Se define una función recursiva con parámetros: x = número para hacer e^(x). n = Cantidad de datos de la sumatoria
    if n == 0:          # Criterio de parada, si n llega a 0 indica que se recorrió toda la sumatoria
        return 1
    else:
        Taylor = ((x ** n) / Factorial(n)) + exp(x, n-1)    # Operación recursiva que actualiza a n = n-1
        return Taylor

x = float(input("Ingrese el número x para calcular e^(x)"))
n = int(input("Ingrese el número N de la sumatoria (Presición de la serie)"))
print("El valor de e^(x) para x =",x,"es:",exp(x,n))

##################################################

# 4) Escriba una función recursiva que devuelva el valor de la serie de Taylor del seno (sen(x)) para un número real
# dado x y un número máximo de términos en la serie N.

'''
Nota: La serie de Taylor para sen^(x) está dada por: 

        sen^(x) = sumatoria( ((-1)^n/(2n+1)!) x^(2n+1))
'''


def SerieSeno(x, n):    # Se define una función recursiva con parámetros: x = número para hacer sen^(x). n = Cantidad de datos de la sumatoria
    if n == 0:          # Criterio de parada, si n llega a 0 indica que se recorrió toda la sumatoria.
        return x        # El primer término en la serie del seno es X
    else:
        Seno = ( ((-1)** n) / Factorial(2*n + 1)) * (x ** (2*n+1)) + SerieSeno(x, n-1)  # Proceso recursivo, se actualiza a n = n-1
        return Seno

x = float(input("Ingrese el número x para calcular sen^(x)"))
n = int(input("Ingrese el número N de la sumatoria (Presición de la serie)"))
print("El valor de sen^(x) para x =", x, "es:", SerieSeno(x, n))

##################################################

# 5) Escriba una función recursiva que devuelva el valor de la serie de Taylor del coseno (cos(x)) para un número real
# dado x y un número máximo de términos en la serie N.

'''
Nota: La serie de Taylor para cos^(x) está dada por: 

        cos^(x) = sumatoria( ((-1)^n/(2n+1)!) x^(2n+1))
'''


def SerieCos(x, n):     # Se define una función recursiva con parámetros: x = número para hacer cos(x). n = Cantidad de datos de la sumatoria
    if n == 0:          # Criterio de parada, si n llega a 0 indica que se recorrió toda la sumatoria.
        return 1        # El primer término en la serie del coseno es 1
    else:
        Cos = ( ((-1)** n) / Factorial(2*n)) * (x ** (2*n)) + SerieCos(x, n-1)  # Proceso recursivo, se actualiza n = n-1
        return Cos

x = float(input("Ingrese el número x para calcular cos^(x)"))
n = int(input("Ingrese el número N de la sumatoria (Presición de la serie)"))
print("El valor de cos^(x) para x =", x, "es:", SerieCos(x, n))

##################################################

# 6) A partir de la función realizada en el punto 3, realice una curva que presente el valor estimado de e^(x)
# para valores de N desde 10 hasta 1000 con pasos de 10; realice otra curva que presente el error absoluto de la serie
# para los mismos valores estimados de N (10:10:1000); realice otra curva que presente el error relativo de la serie
# para los mismos valores estimados de N (10:10:1000). Tome como valor “verdadero” (más preciso) el que devuelve la
# función nativa e^(x) del lenguaje de programación.

import math as mt
import numpy as np
from matplotlib import pyplot as plt


x = 4           # Definimos el valor de x (x=4) para realizar la operación e^(x) = e^(4)
exp_nativa = np.exp(4)      # Resultado de la función nativa para exp(4)


# a) Resultado de e^(x) para la función recursiva que se creó en el punto (3): exp(x, N)
exp_estimado =[]    # Se define este arreglo con el fin de guardar los valores obtenidos de la exponencial creada recursivamente
for N in range(0, 400, 10):
    exp_estimado.append(exp(x, N))


# b) Calculamos el error absoluto de la función exponencial rescursiva vs la función nativa de python.
error_abs =[]
for i in range(len(exp_estimado)):
    error_abs.append(abs(exp_nativa - exp_estimado[i]))

# c) Calculamos el error relativo de la función exponencial rescursiva vs la función nativa de python.
error_rel =[]
for i in range(len(exp_estimado)):
    error_rel.append((error_abs[i] / exp_nativa)*100)

# Graficamos
x = np.arange(1,len(exp_estimado)+1,1)
plt.figure()

plt.subplot(311)
plt.plot(x, exp_estimado,color='r')
plt.xlabel('N')
plt.title('Resultado de la función recursiva')
#plt.ylim(54.5,55)
plt.grid(True)

plt.subplot(312)
plt.plot(x, error_abs,color='g')
plt.xlabel('N')
plt.title('Resultado del error absoluto')
#plt.ylim(0,0.5)
plt.grid(True)

plt.subplot(313)
plt.plot(x, error_rel)
plt.xlabel('N')
plt.title('Resultado del error relativo')
#plt.ylim(54.5,55)
plt.grid(True)

plt.tight_layout()
plt.show()

##################################################

# 7) Repita el punto 6 para la función realizada en el punto 4 (sen(x)).

import math as mt
import numpy as np
from matplotlib import pyplot as plt


x = 28           # Definimos el valor de x (x=28) para realizar la operación sin(x) = sin(28)
sen_nativa = np.sin(28)      # Resultado de la función nativa para sin(28)

# a) Resultado de sin(x) para la función recursiva que se creó en el punto (4): SerieSeno(x, n)
sen_estimado =[]    # Se define este arreglo con el fin de guardar los valores obtenidos de la seno creada recursivamente
for n in range(0, 100, 10):
    sen_estimado.append(SerieSeno(x, n))


# b) Calculamos el error absoluto de la función seno rescursiva vs la función seno nativa de python.
error_abs =[]
for i in range(len(sen_estimado)):
    error_abs.append(abs(sen_nativa - sen_estimado[i]))

# c) Calculamos el error relativo de la función seno rescursiva vs la función nativa de python.
error_rel =[]
for i in range(len(sen_estimado)):
    error_rel.append((error_abs[i] / sen_nativa)*100)

# Graficamos
x = np.arange(1,len(sen_estimado)+1,1)
plt.figure()

plt.subplot(311)
plt.plot(x, sen_estimado,color='r')
plt.xlabel('N')
plt.title('Resultado de la función recursiva')
#plt.ylim(54.5,55)
plt.grid(True)

plt.subplot(312)
plt.plot(x, error_abs,color='g')
plt.xlabel('N')
plt.title('Resultado del error absoluto')
#plt.ylim(0,0.5)
plt.grid(True)

plt.subplot(313)
plt.plot(x, error_rel)
plt.xlabel('N')
plt.title('Resultado del error relativo')
#plt.ylim(54.5,55)
plt.grid(True)

plt.tight_layout()
plt.show()

##################################################

# 8) Repita el punto 6 para la función realizada en el punto 5 (cos(x)).

import math as mt
import numpy as np
from matplotlib import pyplot as plt


x = 28           # Definimos el valor de x (x=28) para realizar la operación cos(x) = sin(28)
cos_nativa = np.cos(28)      # Resultado de la función nativa para cos(28)

# a) Resultado de sin(x) para la función recursiva que se creó en el punto (4): SerieCos(x, n)
cos_estimado =[]    # Se define este arreglo con el fin de guardar los valores obtenidos de la seno creada recursivamente
for n in range(0, 100, 10):
    cos_estimado.append(SerieCos(x, n))


# b) Calculamos el error absoluto de la función seno rescursiva vs la función seno nativa de python.
error_abs =[]
for i in range(len(cos_estimado)):
    error_abs.append(abs(cos_nativa - cos_estimado[i]))

# c) Calculamos el error relativo de la función seno rescursiva vs la función nativa de python.
error_rel =[]
for i in range(len(cos_estimado)):
    error_rel.append((error_abs[i] / cos_nativa)*100)

# Graficamos
x = np.arange(1,len(cos_estimado)+1,1)
plt.figure()

plt.subplot(311)
plt.plot(x, cos_estimado,color='r')
plt.xlabel('N')
plt.title('Resultado de la función recursiva')
#plt.ylim(54.5,55)
plt.grid(True)

plt.subplot(312)
plt.plot(x, error_abs,color='g')
plt.xlabel('N')
plt.title('Resultado del error absoluto')
#plt.ylim(0,0.5)
plt.grid(True)

plt.subplot(313)
plt.plot(x, error_rel)
plt.xlabel('N')
plt.title('Resultado del error relativo')
#plt.ylim(54.5,55)
plt.grid(True)

plt.tight_layout()
plt.show()

##################################################

# 9. Realice un programa que genere 1000 número aleatorios enteros entre -10 y 10 y los guarde un archivo binario
# con formato de 16 bits (int16). El archivo se debe llamar FileBinInt16.bin.

import numpy as np
import struct as st

# Se generan los 1000 números aleatorios entre -10 a 10
v1 = np.random.randint(-10, 10, 1000)

FileName = "FileBinInt16.bin"

# Empaquetamiento de los datos
v1_Pack = st.pack('h'*len(v1), *v1)

# Apertura del archivo en modo lectura (w) y de tipo binario (b)
file = open(FileName, "wb")
file.write(v1_Pack)
file.close()

##################################################

# 10. Realice un programa que lea los datos guardados en el archivo creado en el punto 9 y grafique el histograma
# correspondiente usando 30 casillas (30 bins).

import numpy as np
import struct as st

FileName = "FileBinInt16.bin"
ReadFile = open(FileName,'rb')  # Se abre el archivo en modo lectura (r) binario (b)

Read = ReadFile.read()  # Se lee el archivo
ReadFile.close()
Read = np.array(st.unpack('h'*int(len(Read)/2), Read))      # Desempaquetamiento de los datos

# Se grafica el histograma de los datos desempaquetados
plt.hist(Read, bins=30)
plt.title('Histograma')
plt.show()

##################################################

# 11. Realice un programa que genere 1000 número aleatorios reales entre -1 y 1 y los guarde un archivo binario
# con formato de 64 bits (double). El archivo se debe llamar FileBinDouble.bin.

import numpy as np
import struct as st

v2 = np.random.randint(-10, 10, 1000)

FileName = "FileBinDouble.bin"

# Empaquetamiento de los datos
v2_Pack = st.pack('d'*len(v2), *v2)

# Apertura del archivo en modo lectura (w) y de tipo binario (b)
file = open(FileName, "wb")
file.write(v2_Pack)
file.close()

##################################################

# 12. Realice un programa que lea los datos guardados en el archivo creado en el punto 11 y grafique el histograma
# correspondiente usando 30 casillas (30 bins).

import numpy as np
import struct as st

FileName = "FileBinDouble.bin"
ReadFile_double = open(FileName,'rb')   # Se abre el archivo en modo lectura (r) binario (b)

Read_double = ReadFile_double.read()    # Se lee el archivo
ReadFile_double.close()
Read_double = np.array(st.unpack('d'*int(len(Read_double)/8), Read_double)) # Desempaquetamiento de los datos

# Se grafica el histograma de los datos desempaquetados
plt.hist(Read_double, bins=30)
plt.title('Histograma')
plt.show()

##################################################
# En el archivo binario File-214.bin se encuentran una serie de números enteros sin signo (unsigned), cada uno
# almacenado en 32 bits. El promedio de todos los datos es: 64023.8381.

##################################################

# 13. Realice un programa que lea adecuadamente todos los datos de este archivo y comprueba el valor promedio
# de todos los datos.

File = open("File-214.bin", "rb")   # Se abre al archivo en modo lectura
ReadFile214 = File.read()           # Se lee
File.close()
ReadFile214 = np.array(st.unpack("I"*int(len(ReadFile214)/4), ReadFile214)) # Se desempaqueta y se obtienen los datos

Promedio = np.mean(ReadFile214)     # Se halla el promedio
print('El promedio de los datos es:',Promedio)

##################################################

# 14. A partir de los datos leídos de en el punto 13, realice un programa que permita determinar el número de datos
# que pertenecen a la serie de Fibonacci y escriba el número total de datos que pertenecen a esta serie (utilice la
# función realizada en el punto 1).

# Serie Fibonacci
def Fibonacci2(Num, n0=0, n1=1):
    if n1 == Num or n0 == Num:
        return 1
    elif n1 > Num:
        return 0
    else:
        Fibo = Fibonacci2(Num, n1, n0 + n1)
        return Fibo

cont = 0

# Se crea un ciclo para leer cada valor del archivo ReadFile214.bin y se verifica en la función de Fibonacci
for Num in ReadFile214:
    if (Fibonacci2(Num) == 1):
        cont += 1
print('El número total de datos del archivo File-214.bin que pertenecen a la serie Fibonacci es: ', cont)

##################################################

# 15. A partir de los datos leídos de en el punto 13, realice un programa que permita determinar el número de datos
# que pertenecen a la serie cuadrada y escriba el número total de datos que pertenecen a esta serie (utilice la función
# realizada en el punto 2).


# Serie Cuadrada
def SerieCuadrada2(n, i=1):
    if i*i == n:
        return 1
    elif i*i < n:
        return SerieCuadrada2(n,i+1)
    else:
        return 0

cont2 = 0

# Se crea un ciclo para leer cada valor del archivo ReadFile214.bin y se verifica en la función Cuadrada
for Num in ReadFile214:
    if (SerieCuadrada2(Num) == 1):
        cont2 += 1
print('El número total de datos del archivo File-214.bin que pertenecen a la serie Cuadrada es: ', cont2)




