print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 30/03/2023\n")
salario=float(input("Ingrese su sueldo: "))
porcentaje=0
if salario < 10000:
    print("El impuesto del: 5%") 
    porcentaje = 5/100
elif salario >= 10000 and salario <= 20000:
    print("El impuesto es del: 15%")
    porcentaje = 15/100
elif salario >= 20000 and salario <= 35000:
    print("El impuesto es del: 20%")
    porcentaje = 20/100
elif salario>= 35000 and salario < 60000:
    print("El impuesto es del: 30%")
    porcentaje = 30/100
elif salario >= 60000:
    print("El impuesto es del: 45%")
    porcentaje = 45/100
else:
    print("El salario ingresado es incorrecto")

total = salario*porcentaje
print("El valor a pagar es:",total)
print("El salario a recibir es:",salario-total)