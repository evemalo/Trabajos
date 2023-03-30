print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 30/03/2023\n")
salario=float(input("Ingrese su sueldo: "))
impuesto=0
if salario < 10000:
    print("El impuesto del 5%") 
    impuesto = 0.05
elif salario >= 10000 and salario <= 20000:
    print("El impuesto es del 15%")
    impuesto = 0.15
elif salario >= 20000 and salario <= 35000:
    print("El impuesto es del 20%")
    impuesto = 0.20
elif salario>= 35000 and salario <= 60000:
    print("El impuesto es del 30%")
    impuesto = 0.30
elif salario >= 60000:
    print("El impuesto es del 45%")
    impuesto = 0.45