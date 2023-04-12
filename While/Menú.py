###CURSO DE FUNDAMENTOS DE PYTHON
from metodos import*
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
opcion=0
while opcion >= 0 and opcion <= 10:
    print("Menú de opciones")
    print("1. Contador Ascendente")
    print("2. Contador Descendente")
    print("3. Suma de Números")
    print("4. Factorial")
    print("5. Adivinar un Número")
    print("6. Contador de vocales")
    print("7. Suma de números pares")
    print("8. Cálculo de potencia")
    print("9. Cálculo de promedio")
    print("10. Contador de palabras")
    print("0. Salir")
    opcion=int(input("Ingrese una opción: "))
    if opcion == 0:
        print("Ha seleccionado salir")
    elif opcion == 1:
        print("Ha seleccionado la opcion 1")
        num=int(input("Ingrese un número: "))
        contadorascendente(num)
    elif opcion == 2:
        print("Ha seleccionado la opcion 2")
        num=int(input("Ingrese un número: "))
        contadordescendente(num)
    elif opcion == 3:
        print("Ha seleccionado la opcion 3")
        num=int(input("Ingrese un número: "))
        sumanumeros(num)
    elif opcion == 4:
        print("Ha seleccionado la opcion 4")
        num=int(input("Ingrese un número: "))
        print("El factorial del número ingresado es:",factorial(num))
    elif opcion == 5:
        print("Ha seleccionado la opcion 5")
        aleatorio=random.randint(1,100)
        print("El número que se genero es: ",str(aleatorio))
        adivinar(aleatorio)
    elif opcion == 6:
        print("Ha seleccionado la opcion 6")
        cadena=input("Ingrese la cadena: ")
        cantidad = contar_vocales(cadena)
        print(f"En la cadena '{cadena}'' hay {cantidad} vocales")
    elif opcion == 7:
        print("Ha seleccionado la opcion 7")
        numeros=int(input("Ingrese un número: "))
        print("La suma de los números pares desde cero hasta ",numeros,"es",suma(numeros))
    elif opcion == 8:
        print("Ha seleccionado la opcion 8")
        numero=int(input("Ingrese un número: "))
        exponente=int(input("Ingrese el exponente: "))
        potencia(numero,exponente)
    elif opcion == 9:
        print("Ha seleccionado la opcion 9")
        num=input("Ingrese una lista separada por comas: ")
        num_list=[int(num) for num in num.split(",")]
        print(promedio(num_list))
    elif opcion == 10:
        print("Ha seleccionado la opcion 10")
        palabras=input("Ingrese una cadena de palabras: ")
        print(contador_palabras(palabras))