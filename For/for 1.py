print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 11/04/2023\n")
###CURSO DE FUNDAMENTOS DE PYTHON
# Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menú en el que le permitira seleccionar al usuario que ejercicios ejecutar.
#1. Suma de elementos de una lista: Dada una lista de números, escribe un programa que calcule la suma de todos los elementos de la lista usando un bucle for.
numeros=[1,2,3,4,5,6,7,8,9,10]
suma_num=0
for numero in numeros:
    suma_num += numero
print("La suma de los números es:",suma_num)
a=len(numeros)
print(a)
print("El promedio de los números es:",suma_num/a)

#2. Contar elementos en una lista: Dada una lista de elementos, escribe un programa que cuente cuántos elementos hay en la lista usando un bucle for.
list=[5,4,6,7,8,9,3]
for i in list:
    if i in list:
        print("Los numeros de la lista son",i)
print(f"La lista contiene {len(list)} elementos")
#3. Imprimir elementos de una lista: Dada una lista de elementos, escribe un programa que imprime cada elemento de la lista en una línea separada usando un bucle for.
numlist=[1,2,3,4,5,6,7,8,9,10]
for i in numlist:
    if i in numlist:
        print("Los elementos de la lista son",i)
#4. Contar caracteres en una cadena: Dada una cadena de caracteres, escribe un programa que cuente cuántos caracteres hay en la cadena usando un bucle for.
c=str("hola ¿como estas?")
print("La cantidad de carcteres que contiene la cadena ingresada es de: ",len(c))
#5. Imprimir caracteres de una cadena: Dada una cadena de caracteres, escribe un programa que imprime cada carácter de la cadena en una línea separada usando un bucle for.
d=str("hola, lindo dia")
for i in d:
    if i in d:
        print(i)
#6. Imprimir los primeros N números naturales: Dado un número entero N, escribe un programa que imprime los primeros N números naturales usando un bucle for.

#7. Imprimir los primeros N números pares: Dado un número entero N, escribe un programa que imprima los primeros N números pares usando un bucle for.
pares=[]
num=[1,2,3,4,5,6,7,8,9,10]
print("La lista es:",num)
for e in num:
    if e % 2 != 0:
        continue
    pares.append(e)
print("Lista de numeros pares",pares)
#8. Imprimir los primeros N números impares: Dado un número entero N, escribe un programa que imprima los primeros N números impares usando un bucle for.
impares=[]
num=[1,2,3,4,5,6,7,8,9,10]
for e in num:
    if e % 7 != e % 2 and not e % 2 != 0:
        continue
    impares.append(e)
print("Lista de numeros impares",impares)
#9. Imprimir la tabla de multiplicar de un número: Dado un número entero N, escribe un programa que imprima la tabla de multiplicar de N usando un bucle for.
m=int(input("Ingrese el número del cual desea obtener su tabla de miultiplicar: "))
for e in num:
    if m == e:
        print(f"La tabla de multiplicar del número {m} es:\n",m*1,m*2,m*3,m*4,m*5,m*6,m*7,m*8,m*9,m*10,m*11,m*12)
        print(f"{m} * 1 = ",m*1)
        print(f"{m} * 2 = ",m*2)
        print(f"{m} * 3 = ",m*3)
        print(f"{m} * 4 = ",m*4)
        print(f"{m} * 5 = ",m*5)
        print(f"{m} * 6 = ",m*6)
        print(f"{m} * 7 = ",m*7)
        print(f"{m} * 8 = ",m*8)
        print(f"{m} * 9 = ",m*9)
        print(f"{m} * 10 = ",m*10)
        print(f"{m} * 11 = ",m*11)
        print(f"{m} * 12 = ",m*12)
#10. Imprimir los primeros N números de la serie de Fibonacci: Dado un número entero N, escribe un programa que imprime los primeros N números de la serie de Fibonacci usando un bucle for.