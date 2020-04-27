"""
    Vermos los operadores logicos en Python estos operadores logicos nos sirver para comprovar si se cumplen una o mas
    condiciones logicas 
"""

# Conjuncion
print("Conjunción (and)")

num_uno = int(input("Escribe un mumero mayor a 2 y menor a 5: "))

if(num_uno > 2 and num_uno < 5):
    print("El numero " , num_uno , " cumple con la condicion. \n")
else:
    print("El numero " , num_uno , " No cumple con la condicion. \n")

# Disyuncion
print("Disyunción (or)")

palabra = input("Para cumplir con la condicion escribe 'si' o 'yes': ")

if(palabra == "si" or palabra == "yes"):
    print("La condicion se ha cumplido.\n")
else:
    print("La condicion  No se ha cumplido.\n")


#Negacion
print("Negacion (not)")

num_uno = int(input("Introduce un numero igual a 5: "))

if not(num_uno == 5):
    print("\n El numero es diferente de cincco y Si cumple la condicion.\n")
else:
    print("\n El número es igual a cinco y No cumple la condicion.\n")

print("Fin del Programa....")





















