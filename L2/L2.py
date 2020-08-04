n=input("Ingrese el número a pasar a binario")
if(float(n)<0 or "." in n):
    print("Error, el número es negativo o no es entero")
else:
    n=int(n)
    bin = ""
    if(n>0):
        while(n>0):
            bin+=str(n%2)
            n=n//2
    else:
        bin="0"
    rta=[x for x in bin[::-1]]
    print("".join(rta))
##
n = input("Ingrese el numero que desea convertir a complemento a 2")
numBits = int(input("Ingrese el numero de bits"))
if("." in n):
    print("El número es flotante")
else:
        n=int(n)
        if (n > 2 ** (numBits - 1) - 1 or n < -(2 ** (numBits - 1))):
            print("Son necesarios mas bits para representar el numero")
        else:
            if n > 0:  # Si el numero es positivo lo represento de forma binaria
                bin=""
                while (n > 0):
                    bin += str(n % 2)
                    n = n // 2
                for i in range(numBits - len(bin)):
                    bin+="0"
                rta = [x for x in bin[::-1]]
                print(''.join(rta))
            elif n == 0:
                print("0" * numBits)
            else:
                    z = 0
                    n *=-1
                    while (2 ** z < n):  # Hallo el numero minimo de bits que necesito para representar el numero N
                        z += 1
                    numero = int(2 ** z - n)  # Hallo el numero al cual  tengo que convertir a binario
                    bin = ""
                    while (numero > 0):
                        bin += str(numero % 2)
                        numero = numero // 2
                    if z > len(bin):  # Agrego ceros en caso de que me falten bits para completar los bits que necesito para representar el numero
                        for i in range(z - len(bin)):
                            bin += "0"
                    for i in range(numBits - len(bin)):
                        bin+="1"
                    rta = [x for x in bin[::-1]]
                    print(''.join(rta))
##
n = input("Ingrese el numero que desea convertir a complemento a 2")
numBits = int(input("Ingrese el numero de bits"))
if("." in n):
    print("El número es flotante")
else:
        n=int(n)
        if (n > 2 ** (numBits - 1) - 1 or n < -(2 ** (numBits - 1))):
            print("Son necesarios mas bits para representar el numero")
        else:
            if n > 0:  # Si el numero es positivo lo represento de forma binaria
                bin=""
                while (n > 0):
                    bin += str(n % 2)
                    n = n // 2
                for i in range(numBits - len(bin)):
                    bin+="0"
                rta = [x for x in bin[::-1]]
                print(''.join(rta))
            elif n == 0:
                print("0" * numBits)
            else:
                    z = 0
                    n *=-1
                    while (2 ** z < n):  # Hallo el numero minimo de bits que necesito para representar el numero N
                        z += 1
                    numero = int(2 ** z - n)  # Hallo el numero al cual  tengo que convertir a binario
                    bin = ""
                    while (numero > 0):
                        bin += str(numero % 2)
                        numero = numero // 2
                    if z > len(bin):  # Agrego ceros en caso de que me falten bits para completar los bits que necesito para representar el numero
                        for i in range(z - len(bin)):
                            bin += "0"
                    for i in range(numBits - len(bin)):
                        bin+="1"
                    rta = [x for x in bin[::-1]]
        #Se pasa de complemento A2 a offset
            if (rta[0] == "0"):
                rta[0] = "1"
            else:
                rta[0] = "0"
            print(''.join(rta))
##
'''Punto 4.'''
numero = float(input("Ingrese un numero"))
rta=''
i=0
if(numero<0):
    rta+="1"
    numero*=-1 #Encuentro el signo
else:
    rta+="0"
while(True):
   if(2**i<numero):
       i+=1    ##Calculo la potencia de 2 que no me de mayor al número
   else:
       break
bin=""
if(numero!=0):
    n=127+i-1
    while(n>0):
        bin+=str(n%2) ##Encuentro el exponente
        n=n//2
else:
    bin+="00000000"
rta+=''.join([x for x in bin[::-1]])
numero/=2**(i-1)
numero-=(numero//1)
for i in range(1,24):       #Encuentro la mantisa
    if(numero-2**((-1)*i)<0):
        rta+="0"
    else:
        rta+="1"
        numero-=2**((-1)*i)
print("\n"+rta)


##
'''Punto 5.'''
numero = float(input("Ingrese un numero"))
rta=''
i=0
if(numero<0):
    rta+="1"    #Encuentro el signo
    numero*=-1
else:
    rta+="0"
while(True):
   if(2**i<numero):
       i+=1
   else: #Calculo la potencia de 2 que no sea mayor al número
       break
bin=""
if(numero!=0): #Encuentro el exponente
    n=1023+i-1
    while(n>0):
        bin+=str(n%2)
        n=n//2
else:
    bin+="00000000000"
rta+=''.join([x for x in bin[::-1]])
numero/=2**(i-1)
numero-=(numero//1)
for i in range(1,53):
    if(numero-2**((-1)*i)<0):
        rta+="0" #Encuentro la mantisa
    else:
        rta+="1"
        numero-=2**((-1)*i)
print("\n"+rta)
