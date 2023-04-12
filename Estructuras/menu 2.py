lista=[]
num=0
while num != 100:
    num+=1
    lista.append(num)
print(lista)
for e in lista:
    if e % 2 == 0:
        print(e)
for e in lista:
    if e % 2 == 1:
        print (e)