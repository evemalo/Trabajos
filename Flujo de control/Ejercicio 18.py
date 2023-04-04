print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 30/03/2023\n")
palabra=input("Ingrese una palabra: ")
print(palabra.lower())
if palabra[::-1].lower() == palabra.lower():
    print(f"La palabra {palabra} es un palíndromo")
else:
    print(f"La palabra {palabra} no es un palíndromo")