import math
#
# Punto 1
#
r=int(input("Ingrese el radio"))
print(math.pi*(r**2))

##
#
#Punto 2
#
nombre=input("Ingrese su nombre")
apellido=input("Ingrese su apellido")
print(apellido,nombre)
##

#
#Punto 3
#
n=int(input("Ingrese el número n"))
print(n+(n**2)+(n**3))
##

#
#Punto 4
#
fecha1=input("Ingrese la primera fecha")
fecha2=input("Ingrese la segunda fecha")
anio1=int(fecha1.split("-")[0])
mes1=int(fecha1.split("-")[1])
dia1=int(fecha1.split("-")[2])
anio2=int(fecha2.split("-")[0])
mes2=int(fecha2.split("-")[1])
dia2=int(fecha2.split("-")[2])
print((abs(anio1-anio2)*365)+(abs(mes1-mes2)*30)+abs(dia1-dia2))
##

#
#Punto 5
#
r=int(input("Ingrese el radio"))
print(math.pi*(r**3)*4/3)
##

#
#Punto 6
#
n=int(input("Ingrese el número n"))
if(n-12>12):
    print(abs(n-12)**2)
else:
    print(n-12)
##

#
#Punto 7
#
n=int(input("Ingrese el número n"))
if(n<100):
    print("El número es menor que 100")
elif(n>=100 and n<=1000):
    print("El número está entre 100 y 1000")
elif(n>1000 and n<=2000):
    print("El número está entre 1000 y 2000")
else:
    print("El número es mayor a 2000")
##

#
#Punto 8
#
n=int(input("Ingrese el número"))
if(n%2==0):
    print("El número es par")
else:
    print("El número es impar")
##

#
#Punto 9
#
n=int(input("Ingrese el número"))
arr=[int(x) for x in input("Ingrese el arreglo de números separados por un espacio").split(" ")]
print(arr.count(n))
##

#
#Punto 10
#
n=int(input("Ingrese n"))
cadena=input("Ingrese la cadena")
print(''.join(cadena[len(cadena)-n:len(cadena)]))
##

#
#Punto 11
#
a,b,c=(int(x) for x in(input("Ingrese los 3 numeros separados por espacios")))
if( a==c and b==c ):
    print(0)
else:
    print(a+b+c)
##

#
#Punto 12
#
a,b=(int(x) for x in (input("Ingrese los dos números separados por espacios").split("")))
if(a+b>=15 and a+b<=20):
    print(20)
else:
    print(a+b)
##

#
#Punto 13
#
a,b=(int(x) for x in (input("Ingrese los dos números separados por espacios").split("")))
print((a+b)**2)
##

#
#Punto 14
#
x1,y1=(int(x) for x in (input("Ingrese los dos números x1,y1 separados por espacios").split(" ")))
x2,y2=(int(z) for z in (input("Ingrese los dos números x2,y2 separados por espacios").split(" ")))
print(((x2-x1)**2+(y2-y1)**2)**0.5)
##

#
#Punto 15
#
segundos=int(input("Ingrese los segundos"))
dias=segundos/86400
horas=(dias%86400)/3600
minutos=(horas%3600)/60
segundos=(minutos%60)/60
print("dias:",dias,"horas:",horas,"minutos:",minutos,"segundos:",segundos)
##

#
#Punto 16
#
n=int(input("Ingrese el número"))
stri=''
for x in range(n):
    r=True
    for y in range(2,(int(x**0.5))+1):
        if(x%y==0):
            r=False
    if(r==True):
        stri+=str(x)+' '
print(stri)
##

#
#Punto 17
#
n=int(input("Ingrese el número"))
print(n*(n+1)/2)
##

#
#Punto 18
#
arr=(int(x) for x in input("Ingrese los números del arreglo separados por un espacio").split(" "))
print(max(arr))
##

#
#Punto 19
#
arr=(int(x) for x in input("Ingrese los números del arreglo separados por un espacio").split(" "))
print(min(arr))
##

#
#Punto 20
#
arr=(int(x) for x in input("Ingrese los números del arreglo separados por un espacio").split(" "))
print(sum(arr)/len(arr))
##

#
#Punto 21
#
arr=(int(x) for x in input("Ingrese los números del arreglo separados por un espacio").split(" "))
prom=sum(arr)/len(arr)
sa=0
for y in arr:
    sa+=(y-prom)**2
print((sa/len(arr))**0.5)
##

#
#Punto 22
#
arr=(int(x) for x in input("Ingrese los números del arreglo separados por un espacio").split(" "))
arr=sorted(arr)
if(len(arr)%2!=0):
    print(arr[int(len(arr)/2)])
else:
    print((arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)])/2)
##

#
#Punto 23
#
arr=(int(x) for x in input("Ingrese los números del arreglo separados por un espacio").split(" "))
arr=sorted(arr)
cm=0
moda=0
ca=0
act=arr[0]
for numero in arr:
    if(numero==act):
        ca+=1
    else:
        if(cm<ca):
            cm=ca
            moda=act
        ca=1
        act=numero
print(moda)
##

#
#Punto 24
#
arr=(int(x) for x in input("Ingrese los números del arreglo separados por un espacio").split(" "))
arr=sorted(arr)
print(arr)
##

#
#Punto 25
#
arr=(int(x) for x in input("Ingrese los números del arreglo separados por un espacio").split(" "))
c=0
for numero in arr:
    if(numero%7==0):
        c+=1
print(c)

##
#
#Punto 26
#
N,M,n=[int(x) for x in input("Ingrese N,M y n separados por un espacio").split(" ")]
matriz=[[n for x in range(M)] for i in range (N)]
print (matriz)

##
#
#Punto 27
#
matriz=[[1,2,3],[33,23,13],[4,5,6]]
suma=0
for i in range(len(matriz)):
    suma+=matriz[i][i]
print (suma)

##

#
#Punto 28
#
matriz=[[10,20,30],[30,20,10],[40,50,60]]
suma=0
for i in range(len(matriz)):
    suma+=matriz[i][len(matriz[i])-1-i]
print (suma)

###
#
#Punto 29
#
matriz1=[[1,2,3],[33,23,13],[4,5,6]]
matriz2=[[10,20,30],[30,20,10],[40,50,60]]
for i in range(len(matriz1)):
    for j in range(len(matriz1)):
        matriz1[i][j]+=matriz2[i][j]
print(matriz1)
###
#
#Punto 30
#
matriz1=[[1,2,3],[3,2,1],[4,5,6]]
matriz2=[[0 for i in range(len(matriz1))] for i in range (len(matriz1))]
for i in range(len(matriz1)):
    for j in range(len(matriz1)):
        matriz2[j][i]=matriz1[i][j]
print(matriz2)
##

