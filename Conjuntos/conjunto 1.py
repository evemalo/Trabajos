print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 11/04/2023\n")

#CURSO DE FUNDAMENTOS DE PYTHON
#EJERCICIOS DE CONJUNTOS
#Crear un conjunto con los números del 1 al 10 e imprimirlo en pantalla.
a={1,2,3,4,5,6,7,8,9,10}
#Crear dos conjuntos, uno con los números pares del 1 al 10 y otro con los impares del 1 al 10. Luego, imprimir los conjuntos y la conexión entre ellos.
a={2,4,6,8,10}
b={1,3,5,7,9}
print("La union de los conjuntos es:",a.intersection(b))
#Crear un conjunto con los elementos "manzana", "banana" y "naranja". Luego, pedirle al usuario que ingrese un elemento y determinar si ese elemento se encuentra en el conjunto o no.
frutas={"manzana", "banana","naranja"}
print(frutas)
fruts=input("Ingrese un elemento: ")
d=frutas.difference(fruts)
if fruts in frutas:
    print(f"El elemento {fruts} se encuentra en el conjunto")
elif fruts in frutas:
    print(f"El elemento {fruts} se encuentra en el conjunto")
elif fruts in frutas:
    print(f"El elemento {fruts} se encuentra en el conjunto")
else:
    print(f"El elemento {fruts} no pertenece al conjunto")
#Crear un conjunto con los números del 1 al 5 y otro con los números del 4 al 8. Luego, unir los conjuntos y eliminar los elementos repetidos. Finalmente, imprimir el conjunto resultante.
e={1,2,3,4,5}
f={4,5,6,7,8}
print(e.union(f))
#Crear un conjunto con los elementos "leche", "pan", "huevos" y "azúcar". Luego, elimine el elemento "azúcar" del conjunto y agregue el elemento "harina". Finalmente, imprimir el conjunto resultante.
x={"leche","pan","huevos","azúcar"}
x.discard("azúcar")
x.add("harina")
print(x)
#Crear un conjunto con los nombres "Juan", "María", "Pedro" y "Luisa". Luego, imprima el número de elementos del conjunto.
y={"Juan", "María", "Pedro", "Luisa"}
print("El conjunto contiene",len(y),"elementos")
#Crear dos conjuntos, uno con los números del 1 al 5 y otro con los números del 4 al 8. Luego, imprima los conjuntos y la diferencia simétrica entre ellos.
c1={1,2,3,4,5}
c2={4,5,6,7,8}
d1=c1.symmetric_difference(c2)
print("lla diferencia simétrica de los conjuntos es:",d1)
#Crear un conjunto con los números del 1 al 10 y otro con los números del 5 al 15. Luego, imprime los conjuntos y la unión entre ellos.
a1={1,2,3,4,5,6,7,8,9,10}
b1={5,6,7,8,9,10,11,12,13,14,15}
print("El primer conjunto es:",a1)
print("El segundo conjunto es:",b1)
print("La unión de ambos conjuntos es:",a1.union(b1))
#Crear un conjunto con los elementos "manzana", "banana", "naranja" y "pera". Luego, imprima los elementos del conjunto en orden alfabético.
z={"manzana", "banana", "naranja", "pera"}
print("El conjunto ordenado alfabéticamente es:",sorted(z))
#Crear un conjunto con los números del 1 al 10 y otro con los números del 6 al 15. Luego, imprimir los conjuntos y la intersección entre ellos.
x1={1,2,3,4,5,6,7,8,9,10}
y1={6,7,8,9,10,11,12,13,14,15}
print("La interseccion entre los conjuntos es:",x1.intersection(y1))