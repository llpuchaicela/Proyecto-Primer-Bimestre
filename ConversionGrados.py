print("Ejercicio9")
print("Programa la temperatura en grados celsius")

#Ingrese Datos
gc=float(input("Ingrese la temperatura en grados centigrados: " ))
gc=float(gc)

if gc > 0:
	gf = (gc*9//5)+32
	gk = gc + 237.15;
	print("Los grados celsius convertidos a grados Farenheit son:", gf)
	print("Los grados celsius convertidos a grados kelvin " , gk)
