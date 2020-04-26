"""
    Veremos las sentencias condicionales compuestas en Python
    Estas son las sentencias condicionales conocidas como If Else
    Como ya las vimos en Java
"""
#Declaramos nuestras variables a usar

print("Sistema para calcular el promedio de un alumno.")
nombre = input("Para comezar, ¿Cual es tu nombre?: ")

matematicas = int(input( nombre + " ¿Cual es tu calificación en matematicas: "))
quimica = int(input(nombre + " ¿Cual es tu calificación en quimica: "))
biologia = int(input(nombre + " ¿Cual es tu calificación en biologia: "))

promedio = (matematicas + quimica + biologia)/3

if (promedio >= 6):
    print('Felicidades ' + nombre + ' "Aprobastes El Curso" con un promedio de: ' , promedio)
    print('Felicidades ' + nombre + ' "Aprobastes El Curso" con un promedio de: ' , round(promedio,2))
else:
    print('Felicidades ' + nombre + ' "Aprobastes El Curso" con un promedio de: ' + str(promedio))
    print('Felicidades ' + nombre + ' "Aprobastes El Curso" con un promedio de: ' + str(round(promedio,2)))

print("Fin....")
