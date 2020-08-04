'''
                    "Laboratorio 2: Sistemas Numéricos"
                          Programación Científica
                          Universidad de los Andes
Autor: Julio Nicolás Reyes
'''

##
# Número entero positivo a binario

try:
    num = int(input('Ingrese el número entero positivo'))
except:
    print('El número ingresado NO es entero')

bin = []
res = 0

while num >= 1:

    res = int(num % 2)
    print('residuo', res)
    num = num // 2
    print(num)
    bin.append(res)
print(bin)

for i in range(len(bin)-1, -1, -1):
    print(bin[i], end=" ")


##
# Número entero positivo a binario

numi = int(input('Ingrese el número entero positivo'))
n = int(input('Número de bits (n)'))

bin = []
res = 0
num =numi

while n > 0:
    res = int(num % 2)
    #print('residuo', res)
    num = num // 2
    #print(num)
    bin.append(res)
    n -= 1
#print(bin)

print('El equivalente del número entero',numi,'en binario es:')
for i in range(len(bin)-1, -1, -1):
    print(bin[i], end=" ")

##
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce el número a convertir a binario: '))
print(binarizar(numero))



##



##
# from pythoned.basicas.pila import Pila
# def convertirBase(numeroDecimal,base):
#     digitos = "0123456789ABCDEF"
#
#     pilaResiduo = Pila()
#
#     while numeroDecimal > 0:
#         residuo = numeroDecimal % base
#         pilaResiduo.incluir(residuo)
#         numeroDecimal = numeroDecimal // base
#
#     nuevaCadena = ""
#     while not pilaResiduo.estaVacia():
#         nuevaCadena = nuevaCadena + digitos[pilaResiduo.extraer()]
#
#     return nuevaCadena
#
# print(convertirBase(250,2))
# print(convertirBase(25,16))


##
# Número entero en complemento a 2

numc = int(input('Ingrese el número entero para conocer su equivalente en complemento a 2'))
n = int(input('Número de bits (n)'))

bin = []
res = 0
com = 0

num = numc
num = num * (-1)

com = (2 ** n) - num
print(com)
while n > 0:
    res = int(com % 2)
    #print('residuo', res)
    com = com // 2
    #print(com)
    bin.append(res)
    n -= 1
#print(bin)

print('El equivalente del número entero', numc, 'en formato de complemento a 2 es:')
for i in range(len(bin) - 1, -1, -1):
    print(bin[i], end=" ")


##
# Número entero en Offset binario

numo = int(input('Ingrese el número entero para conocer su equivalente en Offset binario'))
n = int(input('Número de bits (n)'))

bin = []
res = 0
com = 0

num = numo
num = num * (-1)


com = (2 ** n) - num
#print(com)
while n > 0:
    res = int(com % 2)
    #print('residuo', res)
    com = com // 2
    #print(com)
    bin.append(res)
    n -= 1
print(bin)

if bin[len(bin)-1] == 0:
    bin[len(bin) - 1] = 1
else:
    bin[len(bin) - 1] = 0
print('El equivalente del número entero', numo, 'en formato de complemento a 2 es:')
for i in range(len(bin) - 1, -1, -1):
    print(bin[i], end=" ")

##

# Representación binaria de punto flotante 32-bits IEEE754

numF = float(input('Ingrese el número real para conocer su representación en punto flotante de 32 bits'))
n_s = 1
n_e = 8
n_m = 23
bin_t = []

# Nos aseguramos que el algoritmo se ejecute con un número positivo. Si el número es negativo, se agrega en el correspondiente bit de signo al final
if numF < 0:
    numf = numF * (-1)
else:
    numf = numF

# Obtenemos la parte entera del número
num = int(numf)
#print(num)


# Obtenemos la parte decimal del número
num_d = numf - num
num_d = format(num_d, '.7g')
num_d = float(num_d)
numd = num_d
#print(num_d)


# Paso 1: Hallamos la representación binaria de la parte entera del número
bin = []
res = 0

while num >= 1:
    res = int(num % 2)
    #print('residuo', res)
    num = num // 2
    #print(num)
    bin.append(res)
#print(bin)

print('El equivalente del número entero',int(numf),'en binario es:')
for i in range(len(bin)-1, -1, -1):
    bin_t.append(bin[i])
    print(bin[i], end=" ")


# Paso 2: Hallamos la representación binaria de la parte decimal del número
bin_d = []
res_d = 0
num_e = 0

a = len(bin_t)
b = n_m - a
while (b) != 0:
    num_e = num_d * 2
    #print('num_e',num_e)

    if num_e >= 1:
        res_d = 1
        bin_d.append(res_d)

        num_d = num_e - 1
    else:
        res_d = 0
        num_d = num_e
        bin_d.append(res_d)
    b -= 1
print('\nEl equivalente de la parte decimal',float(numd),'en binario es:')
for i in range(len(bin_d)-1, -1, -1):
    print(bin_d[i], end=" ")


#Paso 3: Hallamos el exponente correspondiente y su representación en binario:

exp = (len(bin) - 1) + ((2**n_e)/2 - 1)
expo = exp

bine = []
bin_e = []
res = 0

while exp >= 1:

    res = int(exp % 2)
    #print('residuo', res)
    exp = exp // 2
    #print(exp)
    bine.append(res)
#print(bine)

print('\nEl exponente', expo,'en binario es:')
for i in range(len(bine)-1, -1, -1):
    print(bine[i], end=" ")
    bin_e.append(bine[i])


# Paso 4:  Hallamos la matiza
bin_m = bin_t + bin_d
bin_m = bin_m[1:]


#Llenamos la mantiza de 0 hasta que complete los 23 espacios que requiere
for i in range((n_m)-len(bin_m)):
    bin_m.append(0)



# Paso 5:  Imprimimos el número en representación de coma flotante de 32 bits

bin_32 = []

if numF >=0:
    bin_32 = [0] + bin_e + bin_m
    print('\nEl número', numF, 'en representación de punto flotante de 32 bits es:')
    #print(bin_32)
    for i in range(len(bin_32)):
         print(bin_32[i], end=" ")
else:
    bin_32 = [1] + bin_e + bin_m
    print('\nEl número', numF, 'en representación de punto flotante de 32 bits es:')
    # print(bin_32)
    for i in range(len(bin_32)):
        print(bin_32[i], end=" ")




##
# Representación binaria de punto flotante 64-bits IEEE754 (Precisión doble)

numF = float(input('Ingrese el número real para conocer su representación en punto flotante de 64 bits'))
n_s = 1
n_e = 11
n_m = 52
bin_t = []

# Nos aseguramos que el algoritmo se ejecute con un número positivo. Si el número es negativo, se agrega en el correspondiente bit de signo al final
if numF < 0:
    numf = numF * (-1)
else:
    numf = numF

# Obtenemos la parte entera del número
num = int(numf)
#print(num)


# Obtenemos la parte decimal del número
num_d = numf - num
num_d = format(num_d, '.7g')
num_d = float(num_d)
numd = num_d
#print(num_d)


# Paso 1: Hallamos la representación binaria de la parte entera del número
bin = []
res = 0

while num >= 1:
    res = int(num % 2)
    #print('residuo', res)
    num = num // 2
    #print(num)
    bin.append(res)
#print(bin)

print('El equivalente del número entero',int(numf),'en binario es:')
for i in range(len(bin)-1, -1, -1):
    bin_t.append(bin[i])
    print(bin[i], end=" ")


# Paso 2: Hallamos la representación binaria de la parte decimal del número
bin_d = []
res_d = 0
num_e = 0

a = len(bin_t)
b = n_m - a
while (b) != 0:
    num_e = num_d * 2
    #print('num_e',num_e)

    if num_e >= 1:
        res_d = 1
        bin_d.append(res_d)

        num_d = num_e - 1
    else:
        res_d = 0
        num_d = num_e
        bin_d.append(res_d)
    b -= 1
print('\nEl equivalente de la parte decimal',float(numd),'en binario es:')
for i in range(len(bin_d)-1, -1, -1):
    print(bin_d[i], end=" ")


#Paso 3: Hallamos el exponente correspondiente y su representación en binario:

exp = (len(bin) - 1) + ((2**n_e)/2 - 1)
expo = exp

bine = []
bin_e = []
res = 0

while exp >= 1:

    res = int(exp % 2)
    #print('residuo', res)
    exp = exp // 2
    #print(exp)
    bine.append(res)
#print(bine)

print('\nEl exponente', expo,'en binario es:')
for i in range(len(bine)-1, -1, -1):
    print(bine[i], end=" ")
    bin_e.append(bine[i])


# Paso 4:  Hallamos la matiza
bin_m = bin_t + bin_d
bin_m = bin_m[1:]


#Llenamos la mantiza de 0 hasta que complete los 52 espacios que requiere
for i in range((n_m)-len(bin_m)):
    bin_m.append(0)



# Paso 5:  Imprimimos el número en representación de coma flotante de 64 bits

bin_64 = []

if numF >=0:
    bin_64 = [0] + bin_e + bin_m
    print('\nEl número', numF, 'en representación de punto flotante de 64 bits es:')
    #print(bin_32)
    for i in range(len(bin_64)):
         print(bin_64[i], end=" ")
else:
    bin_64 = [1] + bin_e + bin_m
    print('\nEl número', numF, 'en representación de punto flotante de 64 bits es:')
    # print(bin_32)
    for i in range(len(bin_64)):
        print(bin_64[i], end=" ")
