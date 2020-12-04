print("Ejercicio10")
print("Programa para convertir horas")
print("Lilibeth Puchaicela")

print("Programa para convertir las horas en formato de " ,24, "de formato de 12 horas" )
#Ingresar los datos de entrada
h24= int(input("Ingrese la hora en formato 24 a transformar"))
m24 = int(input("Ingrese los minutos a transformar"))
# Proceso
m12 = 0
periodo= "a.m."
if h24 >= 0 and h24 <= 24 and m24 >= 0 and m24 <= 60:

    if m24 == 60: 
    	h24 = h24 + 1
    	m24 = 0
    else:
    	m12 = m24 

    if h24>=12:
        h12=h24-12
        periodo= "p.m."
    else:
        h12= h24

    print ("La hora en formato 24 horas es " , h24, "horas y " ,m24, "minutos " )
    print ("La hora en formato 12 horas es " , h12, "horas y " ,m12, "minutos " ,periodo )

else:
    print("Los datos son incorrectos " )
