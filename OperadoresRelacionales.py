"""
    Veremos los operadores relaciones en Python. Por lo general son los mismo que tenemos en casi todos los
    leguajes de programacion estos son
    <    Menor que 
    >    Mayor que 
    <=   Menor o igual que
    >=   Mayor o igual que 
    ==   Igual a
    !=   Distinto de
"""
# Comparación de dos numero introducidos por el usuario
print("Introduce dos numero a comparar: \n")

primer_numero = int(input("Introduce el primer numero: "))
segundo_numero = int(input("Introduce el segundo numero: "))

print("\nLos numeros a comprar son: " , primer_numero , segundo_numero , "\n")

if(primer_numero == segundo_numero):
    print("Los numeros son iguales....")
if(primer_numero > segundo_numero):
    print("El número " , primer_numero , "es mayor que " , segundo_numero)
if(primer_numero >= segundo_numero):
    print("El número " , primer_numero , "es mayor he igual que " , segundo_numero)
if(primer_numero < segundo_numero):
    print("El número " , primer_numero , "es menor que " , segundo_numero)
if(primer_numero <= segundo_numero):
    print("El número " , primer_numero , "es menor he igual que " , segundo_numero)
if(primer_numero != segundo_numero):
    print("Los números " , primer_numero , " y " , segundo_numero , "Son distintos")

print("Fin del programa......")
