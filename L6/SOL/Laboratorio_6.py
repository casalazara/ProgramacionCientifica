############################################
#          "Universidad de los Andes"
#           Programación Científica
#   Laboratorio 6: Regresión Lineal
############################################

import math as mt
import numpy as np
import time as ti
import matplotlib.pyplot as plt
import struct as st
import pandas as pd


## 1)
# Para un sistema matricial de la forma Ax=b, donde A es una matriz de coeficientes constantes de
# NxN, x un vector de incógnitas de Nx1 y b un vector contantes de Nx1, realice una función en Python
#  que devuelva el vector de solución x usando el método de Gauss-Jordan con pivote parcial (por filas).
# La función debe devolver igualmente la matriz inversa A^(-1). Pruebe la función con una matriz A aleatoria (rand)
# de 3x3 y un vector b aleatorio de 3x1. Compare la solución encontrada con las funciones de la librería numpy del
# paquete linalg.

# Para matriz A y vector b aleatorios
A = np.random.rand(3,3)
b = np.random.rand(3,1)

# Matríz A y vector b para unos valores dados
#A = np.array([[1,1,1],[3,2,1],[4,3,1]], dtype=float)
#b = np.array([[60],[95],[125]], dtype=float)


def GaussJordanParcial(A,b):
    Au=np.concatenate((A,b),1)                  # Concatenación de la matriz A de coeficientes y el vector solución b. Matriz Aumentada

    for i in range(0, np.size(A, 1)):           # Ciclo que recorre cada columna
        pos = np.argmax(np.abs(Au[i:, i]))      # Se determina la posición en donde está el número mayor en cada columna
        if pos == 0:                            # Condición que evalúa si hay o no necesidad de ordenar las filas
            Au = Au
        else:
            Au[[i, pos], :] = Au[[pos, i], :]   # Método de ordenamiento, asegura que el pivote sea el mayor de los valores en cada columna

        Au[i, :] = (1.0 / Au[i,i]) * Au[i, :]   # Cada pivote es dividido por él mismo. Se normaliza asegurando que sea 1
        for j in range(0, np.size(Au, 0)):      # Ciclo que recorre cada fila
            if i == j:                          # Condición que evalúa si el término es pivote o no
                continue
            filaux=(-1.0*Au[j,i])*Au[i,:]       # Variable auxiliar que guarda el negativo de una fila
            Au[j,:]=Au[j,:]+filaux              # Los términos que no son pivote en cada columna se hace iguales a 0

    x2 = Au[:, np.size(Au, 1)-1]                # Variable X2 que guarda el resultado final
    print(Au)                                   # Se imprime la matríz aumentada equivalente, solución por Gauss-Jordan

    print("Solución de Gauss-Jordan con pivote parcial: \n", x2)
    return [x2]                                 # Se retorna el resultado

'''Solución por medio de la función Gauss-Jordan'''
GaussJordanParcial(A,b)

'''Solución por medio Numpy'''
x1=np.linalg.solve(A,b)                         # Paquete linalg de Numpy para solucionar el sistema de ecuaciones
print("Solución de Numpy: \n",x1)



## 2) Demostracion de los coeficientes a1 y a0

'''Nota: La demostración la encuentran en SICUA'''

## 3) Realice una función en Python que a partir de un conjunto de datos (x, y), devuelva los coeficientes de la regresión lineal
# que más se ajusta al conjunto de puntos usando el método de los mínimos cuadrados. Utilice la forma matricial de la regresión
# lineal para hallar los coeficientes, y use el método de Gauss-Jordan implementado en el punto 1 para hallar la solución. Para
# validar el método se proveen los archivos Lab-Reg-X.bin y Lab-Reg-Y.bin los cuales contienen una serie de puntos (x, y), almacenados
# en formato binario de tipo ‘double’. Halle los coeficientes de la regresión lineal de esta serie de puntos usando la función desarrollada
# y compare la solución con las funciones polyfit de numpy. Realice una gráfica que contenga los puntos (x, y) y la recta encontrada.# Puede usar la función polyval de numpy.



def RegresionLineal(Data_X, Data_Y):

    '''Matriz que agrupa los coeficientes c0 y c1. Aproximaciñón para obtener la regresión lineal por mínimos cuadrados'''
    X_mean = np.mean(Data_X)
    Y_mean = np.mean(Data_Y)
    X_cuad = np.mean(Data_X**2)
    XY = np.mean(Data_X * Data_Y)

    A = np.array([[1, X_mean],[X_mean, X_cuad]])
    b = np.array([[Y_mean],[XY]])

    '''Se aplica Gauss Jordan con pivote parcial para obtener C0 y C1'''
    Coef = GaussJordanParcial(A,b)

    '''Gráfica de los datos extraídos, puntos (x,y)'''
    plt.style.use('ggplot')
    plt.rcParams['axes.prop_cycle']
    plt.plot(Data_X, Data_Y, 'o')

    '''Gráfica de la regresión lineal  (y = mx + b)'''
    y = C1*Data_X + C0
    #plt.plot(Data_X, y, 'r')
    #plt.title('Regresión lineal')

    return Coef


'''Lectura y Extracción de datos'''

Reg_X = open('Lab-Reg-X.bin', 'rb') # Se abre el archivo 'Lab-Reg-X.bin' en modo lectura (r) binario (b)
Reg_Y = open('Lab-Reg-Y.bin', 'rb') # Se abre el archivo 'Lab-Reg-X.bin' en modo lectura (r) binario (b)

Read_X = Reg_X.read()  # Se lee el archivo Reg_X
Read_Y = Reg_Y.read()  # Se lee el archivo Reg_Y

Reg_X.close()
Reg_Y.close()

Data_X = np.array(st.unpack('d'*int(len(Read_X)/8), Read_X))    # Desempaquetamiento de los datos de Reg_X
Data_Y = np.array(st.unpack('d'*int(len(Read_Y)/8), Read_Y))    # Desempaquetamiento de los datos de Reg_Y

'''Llamamos a la función Regresión Lineal'''
Coef = RegresionLineal(Data_X,Data_Y)

C0 = Coef[0][0] # Corte con el eje Y
C1 = Coef[0][1] # Pendiente de la función lineal

'''Solución con polyfit'''
CoefPoly = np.polyfit(Data_X, Data_Y, 1)        #Función polyfit que ajusta un polinomio de grado 1 a los puntos ingresados
print('Los coeficientes mediante polyfit son: \n', CoefPoly)

'''Ecuación de la función lineal obtenida'''
print('La ecuación de la recta obtenida es: \n y =',C1, 'x +',C0)




## 4) Del libro King and Mody, 2010 (referencia 2 del programa), realizar el problema 2.15. Presentar los resultados y figuras
# respectivas en Python. Utilice la función desarrollada en el punto 3 y compare los resultados con las funciones nativas de numpy
# (polyfit y polyval).

'''Extracción de los datos. Se uso la librería 'pandas' para obtener los datos desde un archivo Excell'''
Hombre = np.array(pd.read_excel('Data.xlsx', sheet_name = 'Hombres' ))
Mujer = np.array(pd.read_excel('Data.xlsx', sheet_name = 'Mujeres' ))

'''Tiempos'''
Tiempo_Hombre = Hombre[:,1]
Tiempo_Mujer = Mujer[:,1]

'''Años'''
Anio_Hombre = Hombre[:,0]
Anio_Mujer = Mujer[:,0]


'''Obtenemos los coeficientes obtenidos por la Regresión Lineal'''
Coef_Hombre = RegresionLineal(Anio_Hombre, Tiempo_Hombre)
Coef_Mujer = RegresionLineal(Anio_Mujer, Tiempo_Mujer)


'''Datos para la extrapolación'''
Tiempo = np.arange(1900, 2180)
Extrapolacion_H = Coef_Hombre[0][1] * Tiempo  + Coef_Hombre[0][0]
Extrapolacion_M = Coef_Mujer[0][1] * Tiempo  + Coef_Mujer[0][0]

'''Grafica de la extrapolación'''
Extra_Hombre = plt.plot(Tiempo, Extrapolacion_H, 'c')
Extra_Mujeres = plt.plot(Tiempo, Extrapolacion_M, 'm')

plt.legend(labels = ['Hombres', 'Mujeres'], loc='upper right')
plt.plot(2156, Coef_Mujer[0][1] * 2156  + Coef_Mujer[0][0], '*', linewidth=5)

plt.text(2156, 7.5, 'Intersección: [2156]', fontsize = 9, fontstyle = 'italic', horizontalalignment = 'center', verticalalignment = 'bottom')
plt.title("Regresión Lineal")
plt.xlabel("Años")
plt.ylabel("Tiempos para ganar (s)")


