
'''
                                        "Ejercicios Python"
Programación Científica
Universidad de los Andes
'''

##
# 1. Escriba un programa que pregunte el radio de un círculo y calcule su área.

from math import pi #Se importa la constante 'pi' de la libreria matemática: math

r = float(input("Ingrese el radio del circulo: ")) #Con float permitimos números con parte decimal (punto flotante)
print ("El área del círculo con radio ",r , " es: " , pi * r**2)


##
# 2. Escriba un programa que pregunte el nombre y apellido y los imprima en orden contrario.

fname = input("Ingrese el nombre : ")
lname = input("Ingrese el apellido : ")
print ("Hola " + lname + " " + fname)     #Concatenamos los strings en el orden que queremos

##
# 3. Escriba un programa que pregunte un número n y calcule el valor de r = n+(n*n)+(n*n*n).

a = int(input("Ingrese un número entero : "))
n1 = int(a)
n2 = int(n1*n1)
n3 = int(n1*n1*n1)
r = n1+n2+n3
print ("r = " + str(r))   #Opción 1: Usamos str() para convertir un número a String y concatenamos
print ("r =",r)           #Opción 2


##
# 4)Escriba un programa que calcule el número de días entre dos fechas en formato AAAA-MM-DD. (14)

'''
        Opción 1
'''
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print('El número de días entre las 2 fechas es:', delta.days)


'''
        Opción 2

daysUpToMonth = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
daysUpToMonthLeapYear = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

#Ingresamos la fecha 1
yearPreceding = 2010
monthPreceding = 8
dayPreceding = 2

#Ingresamos la fecha 2
yearSubsequent = 2020
monthSubsequent = 2
daySubsequent = 13
IsDate1AfterDate2 = 0

IsLeapPrecedingYear = (yearPreceding % 4 == 0) and ((yearPreceding % 100 != 0) or (yearPreceding % 400 == 0))
IsLeapSubsequentYear = (yearSubsequent % 4 == 0) and ((yearSubsequent % 100 != 0) or (yearSubsequent % 400 == 0))


if (yearPreceding == yearSubsequent):
    if IsLeapPrecedingYear:
        resultDays = daysUpToMonthLeapYear[monthSubsequent - 1] - daysUpToMonthLeapYear[monthPreceding - 1] + (daySubsequent - dayPreceding)
    else:
        resultDays = daysUpToMonth[monthSubsequent - 1] - daysUpToMonth[monthPreceding - 1] + (daySubsequent - dayPreceding)
else:
    if IsLeapPrecedingYear:
        resultDays = 366 - (daysUpToMonthLeapYear[monthPreceding - 1] + dayPreceding)
    else:
        resultDays = 365 - (daysUpToMonth[monthPreceding - 1] + dayPreceding)

    yearPreceding += 1
    while yearPreceding < yearSubsequent:
        IsLeapPrecedingYear = (yearPreceding % 4 == 0) and ((yearPreceding % 100 != 0) or (yearPreceding % 400 == 0))
        if IsLeapPrecedingYear:
            resultDays += 366
        else:
            resultDays += 365
        yearPreceding += 1

    if IsLeapSubsequentYear:
        resultDays += daysUpToMonthLeapYear[monthSubsequent - 1] + daySubsequent
    else:
        resultDays += daysUpToMonth[monthSubsequent - 1] + daySubsequent

    if IsDate1AfterDate2:
        resultDays *= -1

print('El número de días entre las 2 fechas es:', resultDays)

'''


##
# 5)Escriba un programa que pregunte el radio de una esfera y calcule el volúmen. (15)

from math import pi

r = float(input("Radio de la esfera: "))  # Se ingresa el radio de la esfera (Puede ser un valor decimal)
V = (4/3)*pi* r**3                        # Se aplica la fórmula matemática para hallar el volúmen
print('El volúmen de la esfera es: ',V)


##

# 6) Escriba un programa que calcule la diferencia entre un número n y 12. Si la diferencia es mayor que
#    12 devuelva el valor absoluto de esta al cuadrado.

'''
#Solucion 1
def difference(n):
    if n <= 12:
        return 12 - n
    else:
        return (n - 12) ** 2

print(difference(14))
'''

#Solucion 2
n = int(input("Ingrese el número n: "))
dif = n-12
if dif <= 12:
    print (dif)
else:
    dif = (n - 12) ** 2
    print(dif)


##
# 7) Escriba un programa que verifique si un número es menor que 100 o está entre 100 y 1000 o entre
#1000 y 2000 o es mayor que 2000.

n = int(input("Ingrese el número n: "))

if n < 100:
    print("El número es menor que 100")
elif n <= 1000 and  n >=100:
    print("El número está en el intervalo [1000,100]")
elif n <= 2000 and n >= 1000:
    print("El número está en el intervalo [2000,1000]")
else:
    print("El número es mayor que 2000")

##
# 8. Escriba un programa que verifique si un número es impar.

num = int(input("Ingrese un número: "))
mod = num % 2                  #Con el operador (%) hallamos el módulo o residuo de la división

if mod > 0:
    print("Es un número impar.")
else:
    print("No es un número impar.")

##
# 9. Escriba un programa que cuente el número de veces que se repite el número n en un arreglo.

'''
Solución 1: Definiendo una función
def list(nums):
 count = 0
 n = int(input("Ingrese el número n: "))
 for num in nums:
   if num == n:
     count = count + 1
 return count

print(list([1, 4, 6, 7, 4]))
'''

'''
#Solución 2: Con una lista ya definida

list = [1, 3, 4, 5, 4, 5, 3, 4, 7]
cont = 0

n = int(input("Ingrese el número n: "))
for num in list:
    if num == n:
        cont = cont + 1
print(cont)
'''


#Solución 3: Ingresando la lista que queramos
lista = input("Ingrese los números de la lista (separelos por una ,) : ")
lista = lista.split(",")     # La función split permite dividir los caracteres del string para volverlo una lista
print('Lista : ',lista)

cont = 0

n = int(input("Ingrese el número n: "))
for num in lista:
    num = int(num)
    if num == n:
        cont = cont + 1
print(cont)


##
# 10. Escriba un programa que devuelva los últimos n caracteres de una cadena de caracteres.

'''
#Solución 1: Definiendo una función
def substring_copy(str):
   n = int(input("Ingrese el número n: "))
   b = len(str)
   c = b - n
   return(str[c:])

print(substring_copy('abcdef'))
'''

#Solución 2: Cadena de caracteres definida
palabra = 'Programacion'
n = int(input("Ingrese el número n correspondiente a la cantidad de los últimos caracteres que desea ver: "))
b = len(palabra)
c = b - n
print(palabra[c:])


##
# 11. Escriba un programa que calcule la suma de 3 números. Sin embargo, si los tres números son iguales
#el programa debe retornar cero.

x1 = int(input('Ingrese el número 1'))
x2 = int(input('Ingrese el número 2'))
x3 = int(input('Ingrese el número 3'))

if x1 == x2 and x1 == x3:
    sum = 0
else:
    sum = x1 + x2 + x3
print(sum)

##
# 12. Escriba un programa que devuelva la suma de dos números. Sin embargo, si la suma está entre 15 y
#20 el programa debe devolver 20.

x1 = int(input('Ingrese el número 1'))
x2 = int(input('Ingrese el número 2'))

sum = x1 + x2

if sum <= 20 and sum >= 15:
    res = 20
else:
    res = sum
print(res)

##
# 13. Escriba un programa que devuelva la siguiente operación entre dos números: (x + y) * (x + y).

x = int(input('Ingrese el número x'))
y = int(input('Ingrese el número y'))

res = (x+y) * (x+y)
print(res)

##
# 14. Escriba un programa que devuelva la distancia Euclidiana entre dos puntos x1, y1) y (x2, y2).
print("Ingrese cada punto separado por una coma: x1,y1")

x = input('Ingrese el punto 1')
punto_x = x.split(",")
print('El primer punto tiene coordenadas:', punto_x)

y = input('Ingrese el punto 2')
punto_y = y.split(",")
print('El segundo punto tiene coordenadas:', punto_y)

dist = ( (int(punto_x[0]) - int(punto_y[0]))**2 + (int(punto_x[1]) - int(punto_y[1]))**2 ) ** (0.5)
print (dist)

##
# 15. Escriba un programa que convierte un número de segundos en días, horas, minutos y segundos.

time = float(input("Ingrese el tiempo en segundos: "))
dia = time // (24 * 3600)
#print(day)
time = time % (24 * 3600)
#print(time)

hora = time // 3600
time %= 3600

minutos = time // 60
time %= 60

seg = time

print("%d d: %d h: %d m: %d s" % (dia, hora, minutos, seg))


##
# 16. Escriba un programa que imprima todos los números primos desde 1 hasta n.

n = int(input("Ingrese un número n para saber los números primos en el intervalo [1,n]"))
primo = []
for x in range(2, n+1):
    for n in range(2, x):
        if x % n == 0:
            #print(x, "NO es primo")
            break
    else:
        #print(x, "es primo")
        primo.append(x)
print(primo)

##
# 17. Escriba un programa que sume todos los enteros positivos desde 1 hasta n.

n = int(input("Ingrese el valor de n para conocer la suma de los números en el intervalo [1,n]"))

sum = 0
num = []

for x in range(1,n+1):
    num.append(x)
print(num)

for i in num:
    sum = sum + i
x = print(sum)

##
# 18. Escriba un programa que encuentre el máximo de un arreglo de números.

num = input('Ingrese el arreglo de números (sepárelos por una ,)')
num = num.split(",")
print('El arreglo de números es:',num)

x0 = int(num[0])       # Tomamos el primer número del arreglo para compararlo con los demás
for valor in num:      # Recorremos cada elemento del arreglo, estos se asignan a la variable: 'valor'
    valor = int(valor) # Volvemos la variable valor de 'str' a (int)
    if valor > x0:
       x0 = valor      # Se modifica x0 cada vez que se encuentre un número mayor
print('El número máximo del arreglo es:', x0)  # Se imprime el número máximo que fue hallado

##
# 19. Escriba un programa que encuentre el mínimo de un arreglo de números.

num = input('Ingrese el arreglo de números (sepárelos por una ,)')
num = num.split(",")
print('El arreglo de números es:',num)

x0 = int(num[0])       # Tomamos el primer número del arreglo para compararlo con los demás
for valor in num:      # Recorremos cada elemento del arreglo, estos se asignan a la variable: 'valor'
    valor = int(valor) # Volvemos la variable valor de 'str' a (int)
    if valor < x0:
       x0 = valor      # Se modifica x0 cada vez que se encuentre un número menor
print('El número mínimo del arreglo es:', x0)  # Se imprime el número mínimo que fue hallado

##
# 20. Escriba un programa que encuentre el promedio de un arreglo de números.
data = input('Ingrese el arreglo de números (sepárelos por una ,)')
data = data.split(",")
#print(data)

sum = 0

for valor in data:      # Recorremos cada elemento del arreglo, estos se asignan a la variable: 'valor'
    valor = int(valor) # Volvemos la variable valor de 'str' a (int)
    sum = sum + valor
    media = sum / len(data)
print('El promedio del arreglo de números:', data, "es:", media)  # Se imprime el promedio de los valores del arreglo


##
# 21. Escriba un programa que encuentre la desviación estándar de un arreglo de números.

data = input('Ingrese el arreglo de números (sepárelos por una ,)')
data = data.split(",")

sum = 0
sum_2 = 0

for valor in data:      # Recorremos cada elemento del arreglo, estos se asignan a la variable: 'valor'
    valor = int(valor) # Volvemos la variable valor de 'str' a (int)
    sum = sum + valor
    media = sum / len(data)
    #print(media)

for valor in data:
    valor = int(valor)
    x1  = (valor - media)**2
    sum_2 = sum_2 + x1

    x2 = sum_2 / len(data)
    Desvi = (x2)**(1/2)

print("La desviacion estandar del arreglo es: " , Desvi)

##
# 22. Escriba un programa que encuentre la mediana de un arreglo de números enteros.

data = input('Ingrese el arreglo de números (sepárelos por una ,)')
data = data.split(",")
#print(data)

new_list = []

while data:
    min = int(data[0])  # arbitrary number in list
    for x in data:
        x = int(x)
        if x < min:
            min = x
    new_list.append(min)
    data.remove(str(min))

mod = len(new_list) % 2

if mod == 1:
    i = (len(new_list)/2) - 0.5
    mediana = new_list[int(i)]
    print("La mediana del arreglo de números:",new_list, "es:",mediana)

elif mod == 0:
    x1 = (len(new_list)/2) - 1
    x2 = (len(new_list)/2)
    num = new_list[int(x1)] + new_list[int(x2)]
    mediana = num / 2
    print("La mediana del arreglo de números:",new_list, "es:",mediana)

##
# 23. Escriba un programa que encuentre la moda de un arreglo de números enteros.

data = input('Ingrese el arreglo de números (sepárelos por una ,)')
data = data.split(",")
#print(data)

new_list = []

while data:
    min = int(data[0])  # arbitrary number in list
    for x in data:
        x = int(x)
        if x < min:
            min = x
    new_list.append(min)
    data.remove(str(min))
#print('El arreglo organizado de menor a mayor es:',new_list)

aux = 0
cont = 0
moda = 0

for i in range(0, len(new_list) - 1):
    if (new_list[i] == new_list[i + 1]):
        cont = cont + 1
        if cont >= aux:
            aux = cont
            moda = new_list[i]
    else:
        cont = 0
print('La moda para los datos ordenados:', new_list,'es:', moda)

##
# 24. Escriba un programa que ordene un arreglo de números de mayor a menor.

data = input('Ingrese el arreglo de números (sepárelos por una ,)')
data = data.split(",")
#print(data)

new_list = []

while data:
    max = int(data[0])  # arbitrary number in list
    for x in data:
        x = int(x)
        if x > max:
            max = x
    new_list.append(max)
    data.remove(str(max))
print('El arreglo organizado de mayor a menor es:',new_list)

##
# 25. Escriba un programa que determine, a partir de un arreglo de números enteros, el número de
#elementos que son múltiplos de 7.

data = input('Ingrese el arreglo de números enteros (sepárelos por una ,)')
data = data.split(",")

multi = []

for i in data:
    i = int(i)
    if i%7 == 0:
        multi.append(i)
print('Los números múltiplos de 7 son:', multi)

##
# 26. Escriba un programa que asigne todos los elementos de una matriz de tamaño NxM con un valor n.

N = int(input('Ingrese el número de filas (N)'))
M = int(input('Ingrese el número de columnas (M)'))
n = int(input('Ingrese el valor (n)'))

#Solución 1
Matriz = [[n for colum in range (M)] for filas in range (N)]
print(Matriz)

'''
#Solución 2
Matriz=[]
for filas in range (N):
   Matriz.append ([])
   for colum in range(M):
       Matriz[filas].append((n))
print(Matriz)
'''

##
#27. Escriba un programa que calcule la suma de los elementos de la diagonal principal de una matriz
#cuadrada.

n = int(input('Ingrese el número de filas y columnas que desea para la matriz cuadrada'))

Matriz=[]
sum = 0

for filas in range(n):
    Matriz.append([])
    for colum in range(n):
        #Matriz.append ([filas,colum])
        print("Digíte el valor de la posición ",filas," y ",colum)
        num = int(input())
        #print(Matriz)
        Matriz[filas].append(num)
        if filas == colum:
            sum = sum + num
print('La matriz ingresada fue', Matriz)
print('La suma de los elementos de la matriz principal es:', sum)

##
#28. Escriba un programa que calcule la suma de los elementos de la diagonal secundaria de una matriz
#cuadrada.

n = int(input('Ingrese el número de filas y columnas que desea para la matriz cuadrada'))

Matriz=[]
sum = 0

for filas in range(n):
    Matriz.append([])
    for colum in range(n):
        #Matriz.append ([filas,colum])
        print("Digíte el valor de la posición ",filas," y ",colum)
        num = int(input())
        #print(Matriz)
        Matriz[filas].append(num)

t =  len(Matriz)

for filas in range (t):
    colum = t - filas -1
    sum = sum + int(Matriz[filas][colum])

print('La matriz ingresada fue', Matriz)
print('La suma de los elementos de la matriz secundaria es:', sum)

##

#29. Escriba un programa que calcule una matriz resultante de la suma de los elementos
#correspondientes de dos matrices cuadradas de tamaño NxN.

n = int(input('Ingrese el número de filas y comlumnas que desea para las matrices cuadradas'))

Matriz_1 = []
Matriz_2 = []
Matriz_sum = []

Matriz_1 = [[int(input('Ingrese los valores para la Matriz 1')) for colum1 in range(n)] for filas1 in range(n)]
Matriz_2 = [[int(input('Ingrese los valores para la Matriz 2')) for colum2 in range(n)] for filas2 in range(n)]

print('La matriz 1 resultante es:', Matriz_1)
print('La matriz 2 resultante es:', Matriz_2)

Matriz_sum = [[Matriz_1[filas][colum] + Matriz_2[filas][colum] for colum in range(n)] for filas in range(n)]
print('La suma de las 2 matrices es:', Matriz_sum)

##
#30. Escriba un programa que devuelva la matriz transpuesta de una matriz dada.


N = int(input('Ingrese el número de filas (N)'))
M = int(input('Ingrese el número de columnas (M)'))

Matriz = []
Matriz_tra = []

Matriz = [[int(input('Ingrese un valor')) for colum in range(M)] for filas in range(N)]
print('La matriz ingresada (M):',Matriz)

Matriz_tra = [[ Matriz[filas][colum] for filas in range(N)] for colum in range(M)]
print('La matriz transpuesta es:', Matriz_tra)