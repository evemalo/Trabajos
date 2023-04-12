#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.
def contadorascendente(num):
    cont=0
    while cont <= num:
        print(cont)
        cont+=1

#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.
def contadordescendente(num):
    while num >= 0:
        print(num)
        num-=1

#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.
def sumanumeros(num):
    suma=0
    contador=0
    while contador <= num:
        suma+=contador
        contador+=1
        print(suma)

#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.
def factorial(num):
   if num==0 or num==1:
        resultado=1
   elif num>1:
        resultado=num*factorial(num-1)
   return resultado

#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado, el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir "¡Felicitaciones, adivinaste el número!" y terminar.
import random
def adivinar(aleatorio):
    adivinanza = 0
    while adivinanza != aleatorio:
        adivinanza=int(input("Ingrese un Número del 1 al 100: "))
        if adivinanza > aleatorio:
            print("El número ingresado es mayor al número a adivinar")
        elif adivinanza < aleatorio:
            print("El número ingresado es menor al número a adivinar")
        else:
            print("Felicidades adivino el número",adivinanza)

#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.
def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador+=1
	return contador

#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde cero hasta ese número y lo imprima en la pantalla.
def suma(numeros):
    suma=0
    e=0
    while e <= numeros:
        if e % 2 == 0:
            e+=1
    return suma
#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la base elevada al exponente y lo imprima en la pantalla.
def potencia(numero,exponente):
    resultado=1
    cont=1
    while cont <= exponente:
        resultado=resultado*numero
        cont +=1
    print(resultado)
#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la pantalla.
def promedio(lista_numeros):
    suma=0
    cont=0
    while cont < len(lista_numeros):
        suma=suma + lista_numeros[cont]
        cont += 1
    return suma / len(lista_numeros)

#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena. Para simplificar el problema, puedes considerar que las palabras están separadas por espacios en blanco.
def contador_palabras(cadena):
    cadena=cadena.split(" ")
    return len(cadena)
