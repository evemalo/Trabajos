lista=[]
for x in range(5):
    valor=float(input("Ingrese un valor: "))
    lista.append(valor)
print(lista)
suma_num=0
for numero in lista:
    suma_num += numero
print("La suma de la lista es:",suma_num)
a=len(lista)
print(a)
print("El promedio de la lista es:",suma_num/a)

c=str(input("Ingrese una cadena de texto: "))
print("La cantidad de carcteres que contiene la cadena ingresada es de: ",len(c))

pares=[]
num=[1,2,3,4,5,6,7,8,9,10]
print("La lista es:",num)
for e in num:
    if e % 2 != 0:
        continue
    pares.append(e)
print("Lista de numeros pares",pares)
impares=[]
num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    if i % 1 != pares:
        continue
    impares.append(e)
print("Lista de numeros impares",impares)


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
