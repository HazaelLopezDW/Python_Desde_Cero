"""
    Ahora veremos las sentencias condicionales anidadas como
    if(condicion){
        if(condicion){
            instrucciones
        }else{
            intrucciones
        }
    }else if(condiciones){
        if(condicion){
            instrucciones
        }else{
            intrucciones
        }
    }else{
        intruciones
    }
"""
# Programa que convierte de palabras a numero y de numeros a palabras
print("=========")
print("Conversor")
print("=========")

print("Menu de Opciones: \n")
print("Presiona 1 para convertir de número a plabra.")
print("Presiona 2 para convertir de plabra a número. \n")

opcion = int(input("¿Cual es tu opcion deseada?: "))

if(opcion == 1):
    print("\n Conversor de número a palabra. \n")
    opcion_uno = int(input("¿Cual es el numero que deseas convertir a palabra: "))
    
    if(opcion_uno == 1):
        print("El numero es: 'Uno'")
    elif(opcion_uno == 2):
        print("El numero es: 'Dos'")
    elif(opcion_uno == 3):
        print("El numero es: 'Tres'")
    elif(opcion_uno == 4):
        print("El numero es: 'Cuatro'")
    elif(opcion_uno == 5):
        print("El numero es: 'Cinco'")
    else:
        print("El número selecionado no esta registrado.")
        
elif(opcion == 2):
    print("\n Conversor de palabra a número. \n")

    opcion_dos = input("¿Cual es el palabra que deseas convertir a numero: ")
    opcion_dos = opcion_dos.lower()
    
    if(opcion_dos == "uno"):
        print("El número es: '1'")
    elif(opcion_dos == "dos"):
        print("El numero es: '2'")
    elif(opcion_dos == "tres"):
        print("El numero es: '3'")
    elif(opcion_dos == "cuatro"):
        print("El numero es: '4'")
    elif(opcion_dos == "cinco"):
        print("El numero es: '5'")
    else:
        print("El número selecionado no esta registrado.")
else:
    print("Opcion no disponible")

print("Fin....")































