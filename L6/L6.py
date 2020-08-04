## Punto 1
import numpy as np

#NOTA: Este código es de la solución del lab5, créditos a Julio. Solo añadí el pivoteo.
def gaussJordanPivoteParcial(A,B):
    Au=np.concatenate((A,B),1)
    for i in range(np.size(Au, 0)): #Me muevo por las filas
        iMax = np.argmax(np.abs(Au[i:, i])) #Pivoteo parcialmente dejando el mayor primero
        if (iMax != 0):
            Au[[i, iMax], :] = Au[[iMax, i], :]
        Au[i, :] = (1.0/Au[i,i])*Au[i, :]       # Cada pivote es dividido por él mismo
        for j in range(np.size(Au, 0)):      # Ciclo que recorre cada columna
            if i == j:                          # Condición que evalúa los pivotes. Si es un pivote, salta a la siguiente fila
                continue
            filaux=(-1.0*Au[j,i])*Au[i,:]       # Se deja 0 debajo de los pivotes
            Au[j,:]=Au[j,:]+filaux              # Se reemplaza por el valor dado
    x2 = Au[:, np.size(Au, 1)-1]   # Obtengo el vector solución de nuevo
    return x2

#a=np.array([[1,1,1],[3,2,1],[4,3,1]],dtype=float)
#b=np.array([[60],[95],[125]], dtype=float)
a = np.random.rand(3,3)
b = np.random.rand(3,1)
print("Solución Gauss Jordan con pivote parcial: ")
print(gaussJordanPivoteParcial(a,b))
print("Solución numPy:")
print(np.linalg.solve(a,b))
##2
#Está en el PDF adjunto
## 3
import numpy as np
import matplotlib.pyplot as plt
import struct as st
import pandas as pd
#NOTA: Este código es de la solución del lab5, créditos a Julio. Solo añadí el pivoteo.
def gaussJordanPivoteParcial(A,B):
    Au=np.concatenate((A,B),1)
    for i in range(np.size(Au, 0)): #Me muevo por las filas
        iMax = np.argmax(np.abs(Au[i:, i])) #Pivoteo parcialmente dejando el mayor primero
        if (iMax != 0):
            Au[[i, iMax], :] = Au[[iMax, i], :]
        Au[i, :] = (1.0/Au[i,i])*Au[i, :]       # Cada pivote es dividido por él mismo
        for j in range(np.size(Au, 0)):      # Ciclo que recorre cada columna
            if i == j:                          # Condición que evalúa los pivotes. Si es un pivote, salta a la siguiente fila
                continue
            filaux=(-1.0*Au[j,i])*Au[i,:]       # Se deja 0 debajo de los pivotes
            Au[j,:]=Au[j,:]+filaux              # Se reemplaza por el valor dado
    x2 = Au[:, np.size(Au, 1)-1]   # Obtengo el vector solución de nuevo
    return x2

def estimarCoeficientes(x, y):

    # Calculo los valores de la matriz
    mediaX = np.mean(x)
    mediaY = np.mean(y)
    mediaX2=np.mean(x**2)
    xy=np.mean(x*y)
    #Armo la matriz
    A=[[1,mediaX],[mediaX,mediaX2]]
    B=[[mediaY],[xy]]
    #Calculo c0 y c1
    coeficientes=gaussJordanPivoteParcial(A,B)
    #Aplico la fórmula
    Y=coeficientes[0]+coeficientes[1]*x
    #Grafico
    plt.plot(x,y,'.r')
    plt.plot(x,Y,'b')
    plt.title("Regresión Lineal")
    plt.xlabel("Variable independiente(X)")
    plt.ylabel("Variable dependiente(Y)")
    plt.show()
    return coeficientes
#Leo los dos archivos binarios y desempaco
file = open("Lab-Reg-X.bin", "rb")
var1 = file.read()
x = st.unpack("d"*int(len(var1)/8), var1)
file.close()
file = open("Lab-Reg-Y.bin", "rb")
var1 = file.read()
y = st.unpack("d"*int(len(var1)/8), var1)
#Armo las listas
x = np.array(x)
y = np.array(y)

#Calculo los coeficientes de la función creada y de numpy y listo.
coeficientes=estimarCoeficientes(x,y)
a0=coeficientes[0]
a1=coeficientes[1]
print("Coeficientes obtenidos con la función creada:","a0=",a0,"a1=",a1)
coeficientes=np.polyfit(x,y,1)
a0=coeficientes[1]
a1=coeficientes[0]
print("Coeficientes obtenidos con numPy:","a0=",a0,"a1=",a1)


##4
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#NOTA: Este código es de la solución del lab5, créditos a Julio. Solo añadí el pivoteo.
def gaussJordanPivoteParcial(A,B):
    Au=np.concatenate((A,B),1)
    for i in range(np.size(Au, 0)): #Me muevo por las filas
        iMax = np.argmax(np.abs(Au[i:, i])) #Pivoteo parcialmente dejando el mayor primero
        if (iMax != 0):
            Au[[i, iMax], :] = Au[[iMax, i], :]
        Au[i, :] = (1.0/Au[i,i])*Au[i, :]       # Cada pivote es dividido por él mismo
        for j in range(np.size(Au, 0)):      # Ciclo que recorre cada columna
            if i == j:                          # Condición que evalúa los pivotes. Si es un pivote, salta a la siguiente fila
                continue
            filaux=(-1.0*Au[j,i])*Au[i,:]       # Se deja 0 debajo de los pivotes
            Au[j,:]=Au[j,:]+filaux              # Se reemplaza por el valor dado
    x2 = Au[:, np.size(Au, 1)-1]   # Obtengo el vector solución de nuevo
    return x2

def estimarCoeficientes(x, y):

    # Calculo los valores de la matriz
    mediaX = np.mean(x)
    mediaY = np.mean(y)
    mediaX2=np.mean(x**2)
    xy=np.mean(x*y)
    #Armo la matriz
    A=[[1,mediaX],[mediaX,mediaX2]]
    B=[[mediaY],[xy]]
    #Calculo c0 y c1
    coeficientes=gaussJordanPivoteParcial(A,B)

    return coeficientes

#Leo el excel discriminando filas vacías
file = pd.read_excel("tabla.xlsx")
hombres = np.array(file.iloc[:, :2].dropna())
mujeres = np.array(file.iloc[:, ::2].dropna())
aniosH=hombres[:, 0]
aniosM=mujeres[:, 0]
anios=np.array([i for i in range(1900,2251)], dtype=float)
tH=hombres[:, 1]
tM=mujeres[:, 1]
coeficientesH=estimarCoeficientes(aniosH,tH)
coeficientesM=estimarCoeficientes(aniosM,tM)

#Aplico la fórmula para los Hombres
#Extrapolo primero
YHL=coeficientesH[0]+coeficientesH[1]*anios
plt.plot(anios,YHL,'r--',label="Hombres")
#Aplico la formula sobre los años en los datos
Y=coeficientesH[0]+coeficientesH[1]*aniosH

#Comparo resultados
npCoeficientes=np.polyfit(aniosH,tH,1)
x0=npCoeficientes[1]
x1=npCoeficientes[0]
print("Coeficientes numPy para Hombres:",x0,x1)
print("Coeficientes función creada para Hombres:",coeficientesH[0],coeficientesH[1])
#Grafico
plt.plot(aniosH,tH,'.r')
plt.plot(aniosH,Y,'r')

#Aplico la fórmula para las Mujeres
#Extrapolo primero
YML=coeficientesM[0]+coeficientesM[1]*anios
plt.plot(anios,YML,'b--',label="Mujeres")
#Aplico la formula sobre los años en los datos
Y=coeficientesM[0]+coeficientesM[1]*aniosM
#Comparo resultados
npCoeficientes=np.polyfit(aniosM,tM,1)
x0=npCoeficientes[1]
x1=npCoeficientes[0]
print("Coeficientes numPy para Mujeres:",x0,x1)
print("Coeficientes función creada para Mujeres:",coeficientesM[0],coeficientesM[1])
#Grafico
plt.plot(aniosM,tM,'.b')
plt.plot(aniosM,Y,'b')

#Etiqueto y muestro
plt.title("Regresión Lineal")
plt.xlabel("Años")
plt.ylabel("Tiempo para ganar")
plt.legend(frameon=False, fontsize=10, numpoints=1, loc='upper right')

#Encuentro el punto de intersección y lo grafico.
ix=(coeficientesM[0]-coeficientesH[0])/(coeficientesH[1]-coeficientesM[1]) #x=b2-b1/m1-m2
iy=coeficientesH[1]*ix+coeficientesH[0] #y=m1*x+b1
plt.scatter(ix,iy, color='black' )
plt.text(ix,iy, '({}, {})'.format(ix, iy))

plt.show()
