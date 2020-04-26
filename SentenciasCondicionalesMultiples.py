"""
    Veremos las condicionales multiples que es la misma de if(condicion){ instrucciones } else if(condicion){ instruccioes}
    else if(condicion){ instrucciones } else { instrucciones }
    esta es la manera de codiciones multiples
"""

# Programa que permite convertir de numero a letras... Jajajajajajaja... De hecho solo si el numero coincide en las condiciones
# Mostrar ese mismo numero sulo que en un mensaje

#Primero mostramos el mensaje de que es lo que hace el programa
print("===================================")
print("¡¡CONVERTIDOR DE NUMERO A LESTRAS!!")
print("===================================")

numero = int(input("¿Cual es el numero que deseas convertir?: "))

if (numero == 1):
    print("El número es: 'Uno'")
elif(numero == 2):
    print("El número es: 'Dos'")
elif(numero == 3):
    print("El número es: 'Tres'")
elif(numero == 4):
    print("El número es: 'Cuatro'")
elif(numero == 5):
    print("El número es: 'Cinco'")
else:
    print("Este programa solo puede convertir hasta el número 5")

print("Fin.....")
