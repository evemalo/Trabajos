numero = input("Ingrese un numero: ")
if len(numero) != 1:
     print(f"No se puede procesar el {numero}, debe ingresar un solo número")
elif numero in "0,1,2,3,4,5,6,7,8,9":
    print(f"El número {numero} pertenece al rango")
else:
    print(f"El número {numero} no pertenece al rango")