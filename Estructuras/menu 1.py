def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicacion(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def saludo():
    print("Hola Evelyn")
def formateo(nombre,apellido):
    print(nombre,apellido)
bandera = True
while bandera:
    print("Menú de opciones")
    print("Presione 1 para sumar")
    print("Presione 2 para restar")
    print("Presione 3 para multiplicar")
    print("Presione 4 para dividir")
    print("Presione 5 para saludar")
    print("Presione 6 para formatear")
    print("Presione 7 para salir")
    opcion=int(input("Ingrese una opción: "))
    if opcion != 7:
        num1=int(input("Ingrese un numero: "))
        num2=int(input("Ingrese un numero: "))
        if opcion == 1:
            print("La suma de los números es:",suma(num1,num2))
        elif opcion == 2:
            print("La resta de los números es:",resta(num1,num2))
        elif opcion == 3:
            print("La multiplicación de los números es:",multiplicacion(num1,num2))
        elif opcion == 4:
            print("La división de los números es:",division(num1,num2))
        elif opcion == 5:
            saludo()
        else:
            formateo("Evelyn","Malo")
    else:
        bandera=False
        print("Fin del ciclo")
print("Nueva Línea")