print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 30/03/2023\n")
letra = input("Ingrese una letra: ")
if len(letra) != 1:
    print("No se puede procesar el dato. Debe ingresar una sola letra.")
elif letra in "aeiouAEIOU":
    print("Es vocal")
else:
    print("No es vocal")