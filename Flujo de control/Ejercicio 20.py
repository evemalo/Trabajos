print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 30/03/2023\n")
horas=24
minxhora=60
segxmin=60
dias=int(input("Ingrese el número de dias: "))
a=(dias*horas)
a1=(a*minxhora)
a2=(a1*segxmin)
print(f"En {dias} días hay",a,"horas",a1,"minutos y",a2,"segundos")
print(dias*(horas*minxhora*segxmin))
