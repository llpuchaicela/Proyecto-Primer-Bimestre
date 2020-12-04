print("Ejercicio8")
print("Programa para calcular el número mayor")
print("Lilibeth Puchaicela")

#Declarar e inicializar
N1=0
N2=0
N3=0
R=0

N1=int(input("Ingrese un número"))
print(N1)

N2=int(input("Ingrese un número"))
print(N2)

N3=int(input("Ingrese un número"))
print(N3)

#Proceso
if N1>N2 and N1>N3:
	R=print('El número mayor es ',N1)

if N2>N1 and N2>N3:
	R=print('El número mayor es ' , N2)

if N3>N1 and N3>N2:
	R=print ('El número mayor es ' ,N3)

print("----------------------------------------------")

#Ingreso de datos
N1=int(input("Ingrese un número "))
print(N1)

N2=int(input("Ingrese un número "))
print(N2)

N3=int(input("Ingrese un número "))
print(N3)
#Proceso
if N1>N2 and N1>N3:
	R=print('El número mayor es ',N1)
else:
	print()

if N2>N1 and N2>N3:
	R=print('El número mayor es ' , N2)
else:
	print()

if N3>N1 and N3>N2:
	R=print ('El número mayor es ' ,N3)
else:
	print()

print("---------------------------------------------")

print("Programa  para verificar un número mayor  condición anidada")
N1=int(input("Ingrese un número "))
print(N1)

N2=int(input("Ingrese un número "))
print(N2)

N3=int(input("Ingrese un número "))
print(N3)

#Proceso
if N1>N2 and N1>N3:
	R=print('El número mayor es ', N1)
else:
	print()
	if N2>N1 and N2>N3:
		R=print('El número mayor es ' , N2)
	else:
		print()

		if N3>N1 and N3>N2:
			R=print('El número mayor es ' , N3)
		else:
			print()
		










