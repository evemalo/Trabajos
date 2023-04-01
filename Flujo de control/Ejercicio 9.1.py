print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 30/03/2023\n")
calificacion= float(input( "Ingrese la calificación del examen con punto: "))
print(calificacion )
if calificacion >= 9.50 and calificacion<= 10:
    print("La calificación es: Excelente")
elif calificacion >= 8.50 and calificacion < 9.50:
    print("La calificación es: Muy bueno")
elif calificacion >= 7.00 and calificacion < 8.50:
    print("La calificación es: Bueno")
elif calificacion >= 4.00 and calificacion < 7.50:
    print("La calificación es: Regular")
else :
    print("La calificación es: Deficiente")