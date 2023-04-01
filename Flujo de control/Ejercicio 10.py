print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 30/03/2023\n")
año=int(input("Ingrese el año: "))
if año % 400 == 0 or año % 4 == 0 and not año % 100 == 0:
    print(f"El año {año} es bisiesto")
elif año % 100 == 0:
    print(f"El año {año} no es bisiesto")
else:
    print(f"El año {año} no es bisiesto")