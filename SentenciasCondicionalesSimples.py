#Programa SentenciasCondicionalesSimples en Python IDLE 
"""
    Veremos las sentencias condicionales simples en Pythonl
    Son los los if(){} esta son sin la instruccion else
"""

#Declaramos nuestras variables a usar

print("Sistema para calcular el promedio de un alumno.")
nombre = input("Para comezar, ¿Cual es tu nombre?: ")

matematicas = int(input( nombre + " ¿Cual es tu calificación en matematicas: "))
quimica = int(input(nombre + " ¿Cual es tu calificación en quimica: "))
biologia = int(input(nombre + " ¿Cual es tu calificación en biologia: "))

promedio = (matematicas + quimica + biologia)/3
promedio = int(promedio)

if (promedio >= 6):
    print('Felicidades ' + nombre + ' "Aprobastes El Curso" con un promedio de:' , promedio)

print("Fin....")
    

               

