print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 30/03/2023\n")
calificacion= int (input( "Ingrese la calificación del examen: "))
print(calificacion )
if calificacion >= 90:
    print("La calificación es: A")
elif calificacion >= 80:
    print("La calificación es: B")
elif calificacion >= 70:
    print("La calificación es: C")
elif calificacion >= 60:
    print("La calificación es: D")
else :
    print("La calificación es: F")