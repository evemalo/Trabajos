lista=[1,2,3,4,5,6,7,8,9,10]
for i,v in enumerate(lista):
    print(i,v)

colores={"amarillo":"yellow","azul":"blue","verde":"green"}
for c in colores:
    print(colores[c])
for c,v in colores.items():
    print(c,v)

texto="Hola Mundo"
for i, letra in enumerate(texto):
    print(i, letra)

for e in range (1,101):
    print(e)

for e in range (0,101,2):
    print(e)

for e in range (0,101,3):
    print(e)