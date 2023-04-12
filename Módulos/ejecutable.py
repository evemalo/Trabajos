from funciones import*
from paquetes.metodos import*
#####Menú de Opciones#####
opcion=0
while opcion >= 0 and opcion <= 10:
    print("Menú de opciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Saludar")
    print("0. Salir")
    opcion=int(input("Ingrese la opción: "))
    if opcion == 0:
        print("Ha seleccionado la opcion salir")
        break
    elif opcion == 1:
        a=int(input("Ingrese el primer número: "))
        b=int(input("Ingrese el primer número: "))
        print("El resultado de la suma es: ",suma(a,b))
    elif opcion == 2:
        a=int(input("Ingrese el primer número: "))
        b=int(input("Ingrese el primer número: "))
        print("El resultado de la resta es: ",resta(a,b))
    elif opcion == 3:
        a=int(input("Ingrese el primer número: "))
        b=int(input("Ingrese el primer número: "))
        print("El resultado de la multiplicación es: ",multiplicacion(a,b))
    elif opcion == 4:
        a=int(input("Ingrese el primer número: "))
        b=int(input("Ingrese el primer número: "))
        print("El resultado de la división es: ",division(a,b))
    elif opcion == 5:
        mensaje=input("Ingrese un mensaje: ")
        print("Mensaje",saludar(mensaje))
    else:
        print("La opción ingresada no se encuentra en el Menú")
    