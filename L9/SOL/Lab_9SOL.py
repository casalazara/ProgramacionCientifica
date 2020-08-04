############################################
#                      "Universidad de los Andes"
#                       Programación Científica
#   Laboratorio 9: Interpolación Polinomial y por Polinomios de Lagrange
############################################

import numpy as np
import struct as st
import numpy as np
import matplotlib.pyplot as plt

#
# 1) Realice un programa en Python que, a partir de un conjunto de puntos observados (x, y), implemente la interpolación
# polinomial usando el método matricial (matriz de Vandermonde). Adicionalmente, el programa debe estimar, para una serie de
# valores xnew, los correspondientes valores interpolados ynew.

xi = np.array([13, 16, 17, 23, 28, 33])
yi = np.array([30, 92, 21, 159, 94, 236])

''' Parte A) Función que obtiene los coeficientes'''
def Coeficientes(xi, yi):

    N = np.size(xi)

    A = np.zeros([N, N]) # Matriz cuadrada A de Ax = b
    b = np.zeros([N, 1]) # Vector b

    for i in range(N):          # Se itera sobre cada columna de la matriz
        for j in range(N):

            # Se llena cada posición de la matriz con el Xi[i]**(N-j-1)
            A[i, j] = xi[i] ** (N - j - 1)

        b[i] = yi[i]    # Se llena cada posición del vector b con el Yi[i]

    # Solucionamos el sistema Ac=b
    Ci = np.linalg.solve(A, b)

    # Comparando con Polyfit
    CiPolyfit = np.polyfit(xi, yi, np.size(xi) - 1)

    return Ci, CiPolyfit
Ci, CiPolyfit = Coeficientes(xi, yi)


''' Parte B) Obtención de los valores incógnitos (yk)'''
xk = np.array([15, 19, 21, 25, 27, 32])

def yk(Ci, xk, CiPolyfit):
    N = np.size(Ci)

    fx = np.zeros(np.size(xk))# Arreglo para almacenar los valores obtenidos

    for i in range(np.size(xk)):
        for j in range(N):
            fx[i] += (Ci[j]) * (xk[i]**(N - j - 1))

    # Comparando con Polyval, que valúa los puntos xk en el polinomio determinado por polyfit
    YkPolyfit = np.polyval(CiPolyfit, xk)

    #print('xk \t {:>18s} \t {:>25s}\t'.format('yk', 'yk Polyval'))

    #for i in range(np.size(xk)):
    #    print('{0:.2f} \t {1:24.10f} \t {2:20.10f}'.format(xk[i], fx[i], YkPolyfit[i]))  #En format, la 'e' sirve para indicar notación científica

    return fx, YkPolyfit

Ynew, YkPolyfit = yk(Ci, xk, CiPolyfit)







##
# 2) Realice un programa en Python que, a partir de un conjunto de puntos observados (x, y), implemente la interpolación
# polinomial usando el método de Lagrange. El programa debe estimar, para una serie de valores xnew, los correspondientes valores
# interpolados ynew.

#Puntos conocidos
xi = np.array([13, 16, 17, 23, 28, 33])
yi = np.array([30, 92, 21, 159, 94, 236])

#Valores de xk donde queremos saber el yk
xk = np.array([15, 19, 21, 25, 27, 32])


def CoeLagrange(xi, yi, xk):

    yk = np.zeros(np.size(xk))

    for k in range(np.size(xk)):        #Iteración sobre cada valor de xk
        for i in range(np.size(yi)):    #Iteración sobre cada punto conocido yi

            multiaux = 1                #Multiplicatoria asociada a las operaciones con yi

            for j in range(np.size(yi)):
                if i==j:
                    continue
                multiaux *= ((xk[k] - xi[j]) / (xi[i] - xi[j]))
            # Se incrementa la suma acumulada
            yk[k] += yi[i] * multiaux

    # Con numpy
    CiPolyfitLagrange = np.polyfit(xi, yi, np.size(xi) - 1)
    ykPolyfit = np.polyval(CiPolyfitLagrange, xk)

    # Imprimimos los valores de yk
    #print('xk \t{:^30s} \t {:^20s}\t'.format('yk', 'ykPolyval'))

    #for i in range(np.size(xk)):
    #    print('C_{:.2f} \t {:18.10f} \t {:20.10f}'.format(xk[i], yk[i], ykPolyfit[i]))

    return yk, CiPolyfitLagrange

Ynew_Lagrange, Ynew_PolyLagrange = CoeLagrange(xi, yi, xk)






##
# 3) En los archivos x_obs.bin y y_obs.bin se encuentran una serie de puntos observados (x, y) almacenados en formato binario
# de tipo double. A partir de los procedimientos implentados en los puntos 1 y 2, complete la siguiente tabla con los valores
# de ynew correspondientes a cada uno de los valores presentados en la columna xnew. Complete adicionalmente la última columna
# con los correspondientes valores ynew estimados por la función nativa de interpolación polinomial de numpy.

FileNameX = "x_obs.bin"
FileNameY = "y_obs.bin"

FileX = open(FileNameX,'rb')   # Se abre el archivo para X en modo lectura (r) binario (b)
FileY = open(FileNameY,'rb')   # Se abre el archivo para Y en modo lectura (r) binario (b)

'''Para los datos de X'''
ReadFileX = FileX.read()    # Se lee el archivo
FileX.close()
FileX = np.array(st.unpack('d'*int(len(ReadFileX)/8), ReadFileX)) # Desempaquetamiento de los datos

'''Para los datos de Y'''
ReadFileY = FileY.read()    # Se lee el archivo
FileY.close()
FileY = np.array(st.unpack('d'*int(len(ReadFileY)/8), ReadFileY)) # Desempaquetamiento de los datos

# Se grafica el histograma de los datos desempaquetados
plt.plot(FileX, FileY, '-c')
plt.xlabel('Datos en X')
plt.ylabel('Datos en Y')
plt.grid(1)
plt.show()

Xnew = [78.12, 0.98, 67.59, 8.69, 55.69, 48.12, 13.24, 97.56, 25.69, 1.26]

'''Para interpolación polinomial'''
Coef, CiPolyfit = Coeficientes(FileX, FileY)
Ynew, YkPolyfit = yk(Coef, Xnew, CiPolyfit)

'''Para la interpolación con Polinomios de Lagrange'''
Ynew_Lagrange, Ynew_PolyLagrange = CoeLagrange(FileX, FileY, Xnew)


# Imprimimos la tabla con los valores de Ynew para: Polinomial, Lagrange y Numpy(Polinomial)
print('\n \n X_new \t {:>20s} \t {:>20s} \t {:>20s}'.format('Ynew (Polinomial)', 'Ynew (Lagrange)', 'Ynew (Numpy)'))

for i in range(np.size(Xnew)):
    print('{0:.2f} \t {1:20.10e} \t {2:20.10e} \t {3:20.10f}'.format(Xnew[i], Ynew[i], Ynew_Lagrange[i], YkPolyfit[i]))  # En format, la 'e' sirve para indicar notación científica






##
# 4) Repita el procedimiento realizado en el punto 3 pero esta vez para procedimientos sucesivos de interpolación para cada
# serie de 4 puntos consecutivos de xnew. Complete la siguiente tabla:

FileNameX = "x_obs.bin"
FileNameY = "y_obs.bin"

FileX = open(FileNameX,'rb')   # Se abre el archivo para X en modo lectura (r) binario (b)
FileY = open(FileNameY,'rb')   # Se abre el archivo para Y en modo lectura (r) binario (b)

'''Para los datos de X'''
ReadFileX = FileX.read()    # Se lee el archivo
FileX.close()
FileX = np.array(st.unpack('d'*int(len(ReadFileX)/8), ReadFileX)) # Desempaquetamiento de los datos

'''Para los datos de Y'''
ReadFileY = FileY.read()    # Se lee el archivo
FileY.close()
FileY = np.array(st.unpack('d'*int(len(ReadFileY)/8), ReadFileY)) # Desempaquetamiento de los datos


Xnew = [78.12, 0.98, 67.59, 8.69, 55.69, 48.12, 13.24, 97.56, 25.69, 1.26]  #Valores Xnew que se quieren identifica


'''Hallamos los coeficientes que permite construir un polinomio de orden 3 cada 4 puntos '''

for i in range(0, np.size(FileX)-1,3):        # Salte cada 8 espacios
    #Modifica xi y yi para obtener sólo 4 puntos con saltos de 4
    v = FileX[i:i+4]
    u = FileY[i:i+4]

    '''Con interpolación Polinomial'''
    Ci, CiP = Coeficientes(v, u)            # Se llama a la función coeficientes para obtener los Ci

    #for j in range(np.size(Ci)):
    #    print('Polinomio: {:d} \t C_{:d} \t {:32.10f} \t {:25.10f}'.format(i, j, Ci[j][0], CiP[j]))

    # Gráfica de los datos
    plt.plot(FileX, FileY, 'oc')
    plt.plot(v, u, '--', color = 'y', label='{:s} \t {:d}'.format('polinomio ->', i))
    #plt.legend()
    plt.xlabel('xk')
    plt.ylabel('yk')
    plt.grid(1)
    plt.show()

    # Gráfica del polinomio resultante para unos valores de x
    xp = np.arange(v[0], v[-1], 0.01)
    yp, ypPol = yk(Ci, xp, CiP)
    plt.plot(xp, yp)

    YnewP = np.array([])

    '''Calculamos los Ynew'''
    for k in range (np.size(Xnew)):
        if FileX[i] < Xnew[k] < FileX[i+3]:
            Ynew, YnewPol = yk(Ci, np.array([Xnew[k]]), CiP)
            YnewP = np.append(Ynew, YnewP)
            Ynew_L, Ynew_LP = CoeLagrange(v, u, np.array([Xnew[k]]))
            print('Con interpolación Polinomial, el valor de Ynew para Xnew=', Xnew[k], 'es:', Ynew)
            print('Con Polinomios de Lagrange, el valor de Ynew para Xnew=', Xnew[k], 'es:', Ynew_L, '\n')







## 5) A parir del mismo conjunto de datos observados presentados en los archivos del punto 3, utilice ahora el método de
# interpolación por splines cúbicos de la librería scipy para completar la tabla presentada a continuación,

import scipy.interpolate as interpol    #Importamos librería Scipy para la interpolación

# Los puntos conocidos (x,y)
FileNameX = "x_obs.bin"
FileNameY = "y_obs.bin"

FileX = open(FileNameX,'rb')   # Se abre el archivo para X en modo lectura (r) binario (b)
FileY = open(FileNameY,'rb')   # Se abre el archivo para Y en modo lectura (r) binario (b)

'''Para los datos de X'''
ReadFileX = FileX.read()    # Se lee el archivo
FileX.close()
x = np.array(st.unpack('d'*int(len(ReadFileX)/8), ReadFileX)) # Desempaquetamiento de los datos

'''Para los datos de Y'''
ReadFileY = FileY.read()    # Se lee el archivo
FileY.close()
y = np.array(st.unpack('d'*int(len(ReadFileY)/8), ReadFileY)) # Desempaquetamiento de los datos


'''Parte a) Hallar el polinomio de interpolación por Splines para los datos previamente conocidos'''
# Se llama la función CubicSpline del paquete interpolate de Scipy
# Método 1: natural
f1 = interpol.CubicSpline(x, y, bc_type='natural')

# Método 2: not-a-knot
f2 = interpol.CubicSpline(x, y, bc_type='not-a-knot')

# Método 3: clamped
f3 = interpol.CubicSpline(x, y, bc_type='clamped')

# Se define un rango en X para gráficar los polinomios resultantes

xp = np.arange(x[0], x[-1] - 0.001, 0.001)

plt.figure()
plt.plot(x, y , 'sc')
plt.plot(xp, f1(xp), '--r')
plt.plot(xp, f2(xp), '--m')
plt.plot(xp, f3(xp), '--g')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(['puntos conocidos', 'natural', 'Not-a-knot', 'clamped'])
plt.grid(True)


'''Parte b) Hallar los Ynew previamente desconocidos para diferentes Xnew'''
Xnew = [78.12, 0.98, 67.59, 8.69, 55.69, 48.12, 13.24, 97.56, 25.69, 1.26]  #Valores Xnew que se quieren identifica

Ynew1 = f1(Xnew)    # 'Spline con método natural'
Ynew2 = f2(Xnew)    # 'Spline con método Not-a-knot'
Ynew3 = f3(Xnew)    # 'Spline con método clamped'

# Imprimimos los nuevos Ynew obtenidos por los 3 métodos de interpolación por Splines Cúbicos
print("Xnew \t {:^15s} \t {:^15s} \t {:^15s}".format("Ynew (natural)","Ynew (Not-a-knot)","Ynew (clamped)"))
for i in range(np.size(Xnew)):
    print("{:.2f} \t {:15.10f} \t {:15.10f} \t {:15.10f}".format(Xnew[i], Ynew1[i], Ynew2[i], Ynew3[i]))

