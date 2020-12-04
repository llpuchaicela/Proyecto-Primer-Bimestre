print("Ejercicio4")
print("Programa que permite el cálculo")
print("Lilibeth Puchaicela")
#Inicialización de variables
A= 0
B=0
C=0
D=0
at=0
ar=0


A= float(input("Ingrese la altura del paralelogramo "))
B= float(input("Ingrese el largo del rectángulo "))
C= float(input("Ingrese la altura del rectangulo "))

D= A**C
print('La altura de el triángulo es : ', D)
at=(B*A)//2
print('El área de el triángulo es: ', at)
ar= B*C
print('El área de el rectángulo es:',ar )

areatotal = at+ar

print('El area de el terreno compuesto es: ', areatotal, 'compuesto por un rectángulo de largo ',A, 'y por un rectángulo de largo'
	,B,'y una altura de rectángulo',C )

Costo_Terreno=float(input("Ingrese el costo del metro cuadrado: "))
print(Costo_Terreno)
Area_Total= float(input("Ingrese el areatotal del paralelogramo"))
Costo_Total=print('El costo total de el terreno es: ', Area_Total * Costo_Terreno)
