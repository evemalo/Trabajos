print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 30/03/2023\n")
numeros=[]
numeros=[1,2,3,4,5]
print(numeros)
amix=['Estefania','Jennifer','Nayeli','Melanie']
print(amix[0])
pares=[]
num=[1,2,3,4,5,6,7,8,9,10]
for e in num:
    if e % 2 != 0:
        continue
    pares.append(e)
print("Lista de numeros pares",pares)
amix=['Estefania','Jennifer','Nayeli','Melanie']
print(amix[-1])
print(amix[3])
num=[1,2,3,4,5,6,7,8,9,10]
print(num[-1])
impares=[]
num=[1,2,3,4,5,6,7,8,9,10]
for e in num:
    if e % 7 != e % 2 and not e % 2 != 0:
        continue
    impares.append(e)
print("Lista de numeros impares",impares)
amix=['Estefania','Jennifer','Nayeli','Melanie']
amix.append('Maria')
print(amix)
num=[1,2,3,4,5,6,7,8,9,10]
print(f"El numero {num[0]} es el inicio de la lista y el numero {num[-1]} es el final de la lista")
amix=['Estefania','Jennifer','Nayeli','Melanie']
print("La cantidad de elementos de la lista es:",len(amix))
num=[1,2,3,4,5,6,7,8,9,10]
print("La suma de todos los números es:",sum(num))