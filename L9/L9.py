## Punto 1
import numpy as np
import matplotlib.pyplot as plt
import struct as st
import pandas as pd
#Para interpolar
import scipy.interpolate as interpol

def Coeficientes(xi, yi):
    N = np.size(xi)
    A = np.zeros([N, N],dtype="float64") # Matriz cuadrada A de Ax = b
    b = np.zeros([N, 1],dtype="float64") # Vector b

    for i in range(N):          # Se itera sobre cada columna de la matriz
        for j in range(N):

            # Se llena cada posición de la matriz con el Xi[i]**(N-j-1)
            A[i, j] = xi[i] ** (N - j - 1)

        b[i] = yi[i]    # Se llena cada posición del vector b con el Yi[i]

    # Solucionamos el sistema Ac=b
    ci = np.linalg.solve(A, b)
    return ci

def vandermonde(Ci, xk):
    N = np.size(Ci)
    fx = np.zeros(np.size(xk),dtype="float64")# Arreglo para almacenar los valores obtenidos
    for i in range(np.size(xk)):
        for j in range(N):
            fx[i] += (Ci[j]) * (xk[i]**(N - j - 1))
    return fx

## Punto 2
from Salazar_201816839 import *

def lagrange(Xi,Yi,Xk):
    #Creo el arreglo para guardar las parejas de los Xk
    Yk=np.zeros(np.size(Xk),dtype="float64")
    #Empezamos a buscar parejas para los Xk
    for k in range(np.size(Xk)):
        #Para esto recorremos los Yi conocidos
        for i in range(np.size(Yi)):
            #Hallamos la multiplicatoria interior asociada a cada Yi
            multaux=1
            for j in range(np.size(Yi)):
                if i==j:
                    continue
                multaux *= ((Xk[k]-Xi[j])/(Xi[i]-Xi[j]))
            #Incrementamos la suma acumulada
            Yk[k]+=Yi[i]*multaux
    #Retorno las Y halladas
    return Yk
## Punto 3
from Salazar_201816839 import *

#Lectura de los archivos binarios
equis=open("x_obs.bin","rb")
yes=open("y_obs.bin","rb")
var=equis.read()
var2=yes.read()

#Desempaquetamiento
X = np.array(st.unpack("d"*int(len(var)/8), var),dtype="float64")
Y = np.array(st.unpack("d"*int(len(var2)/8), var2),dtype="float64")

#Valores Xk
xnew=np.array([78.12,0.98,67.59,8.69,55.69,48.12,13.24,97.56,25.69,1.26],dtype="float64")

'''Polinomial'''
Ci = Coeficientes(X, Y)
Yk = vandermonde(Ci, xnew)

'''Lagrange'''
Yk2=lagrange(X,Y,xnew)

'''NumPy'''
#Hago el ajuste
CiPoly=np.polyfit(X,Y,np.size(X)-1)

#Evaluo
YkPoly=np.polyval(CiPoly,xnew)

#Guardo en excel
df = pd.DataFrame({'xnew': xnew,
                   'ynew (Polinomial)': Yk,
                   'ynew (Lagrange)':Yk2,
                   'ynew (Numpy)':YkPoly
                   })
writer = pd.ExcelWriter('Punto3.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Punto 3', index=False,startrow=1, startcol=1)
writer.save()

#Imprimo
print('Xnew \t{:>30s} \t {:>25s}\t {:>22s}\t'.format('ynew (Polinomial)', 'ynew (Lagrange)','ynew (Numpy)'))

for i in range(np.size(xnew)):
    print('{:f} \t {:25.10e} \t {:25.10e} \t {:25.10f}'.format(xnew[i],Yk[i],Yk2[i],YkPoly[i]))

## Punto 4
from Salazar_201816839 import *

#Arreglos para guardar en excel
xnews=np.array([],dtype="float64")
polinomials=np.array([],dtype="float64")
lagranges=np.array([],dtype="float64")
YkPolys=np.array([],dtype="float64")

'''Hallamos los coeficientes que permite construir un polinomio de orden 3 cada 4 puntos '''
print('Xnew \t{:>30s} \t {:>25s}\t {:>22s}\t'.format('ynew (Polinomial)', 'ynew (Lagrange)','ynew (Numpy)')) #Encabezado
for i in range(0, np.size(X)-1,3):        # Salte cada 4 espacios
    #Modifica xi y yi para obtener sólo 4 puntos con saltos de 4
    v = X[i:i+4]
    u = Y[i:i+4]
    Ci = Coeficientes(v, u)            # Se llama a la función coeficientes para obtener los Ci
    CiPolyfit = np.polyfit(v, u, np.size(v) - 1)   # Comparar la solución de la función con numpy
    candidatos=np.array([],dtype="float64") #Arreglo para los números en el rango de x seleccionado

    for numero in xnew:
        if v[0]<=numero<=v[-1]: #Guardo los números en ese rango de x seleccionado
            candidatos=np.append(candidatos,numero)

    # Evaluo
    YkPoly = np.polyval(CiPolyfit, candidatos)

    #Polinomial
    yp3 = vandermonde(Ci, candidatos)

    #Lagrange
    Yk2 = lagrange(v, u, candidatos)

    #Imprimo la tabla y guardo en los arreglos para el excel
    for i in range(np.size(candidatos)):
        print('{:f} \t {:25.10f} \t {:25.10f} \t {:25.10f}'.format(candidatos[i],yp3[i],Yk2[i],YkPoly[i]))
        xnews=np.append(xnews,candidatos[i])
        polinomials=np.append(polinomials,yp3[i])
        lagranges=np.append(lagranges,Yk2[i])
        YkPolys=np.append(YkPolys,YkPoly[i])

#Guardo en excel
df = pd.DataFrame({'xnew': xnews,
                   'ynew (Polinomial)': polinomials,
                   'ynew (Lagrange)':lagranges,
                   'ynew (Numpy)':YkPolys
                   })
writer = pd.ExcelWriter('Punto4.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Punto 4', index=False,startrow=1, startcol=1)
writer.save()

## Punto 5
from Salazar_201816839 import *

#Puntos X,Y conocidos
Xi = X
Yi = Y

# Splines de tipo natural
f1Nat=interpol.CubicSpline(Xi,Yi,bc_type="natural")

# Splines de tipo not-a-knot
f1NaK=interpol.CubicSpline(Xi,Yi,bc_type="not-a-knot")

# Splines de tipo Clamped con k=0
f1Clam=interpol.CubicSpline(Xi,Yi,bc_type="clamped")

#Rango de X para graficar polinomios resultantes
Xp=np.arange(Xi[0],Xi[-1]-0.001,0.001)

#Gráfica
plt.figure()
plt.plot(Xi,Yi,'sr')
plt.plot(Xp,f1Nat(Xp),'--b')
plt.plot(Xp,f1NaK(Xp),'--m')
plt.plot(Xp,f1Clam(Xp),'--g')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Puntos conocidos","Natural","Not-a-Knot","Clamped"])
plt.grid(True)

#Puntos Xk a los que se les quiere encontrar Yk
Xk= xnew

#Valores de Yk estimados

#Natural
YkNat=f1Nat(Xk)

#Not-a-knot
YkNaK=f1NaK(Xk)

#Clamped
YkClam=f1Clam(Xk)

#Imprimo
print('Xk \t {:>20s} \t {:>20s} \t {:>15s}'.format("Yk Natural","Yk Not-a-K-not","Yk Clamped"))
for i in range(np.size(Xk)):
    print('{:f} \t {:15.10f} \t {:15.10f} \t {:15.10f}'.format(Xk[i],YkNat[i],YkNaK[i],YkClam[i]))

#Guardo en excel
df = pd.DataFrame({'xnew': xnew,
                   'ynew (Splines natural)': YkNat,
                   'ynew (Splines Not-a-Knot)':YkNaK,
                   'ynew (Splines Clamped)':YkClam
                   })
writer = pd.ExcelWriter('Punto5.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Punto 5', index=False,startrow=1, startcol=1)
writer.save()
