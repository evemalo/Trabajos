instituto={'carreras':['Big Data','Desarrollo de software','Infraestructura','Cyberseguridad','Producción y realización de audiovisuales','Entrenamiento deportivo'],
           'materias':['Cálculo','Mátematica','Estadística','Lenguaje','Introducción a la programacion','Introduccion a big data'],
           'profesores':['Paul','Vilma','Vilma','Juliana','Fabián','Lady'],
           'notas':[91,75,74,83,85,71]}
print(instituto['carreras'])
print(instituto['materias'])
print(instituto['profesores'])
print(instituto['notas'])
suma=0
for e in instituto['notas']:
    suma += float(e)
print(suma)
promedio = suma/len(instituto['notas'])
print(promedio)
print(sum(instituto['notas'])/len(instituto['notas']))
print(round(sum(instituto['notas'])/len(instituto['notas']),2))
minimo=min(instituto['notas'])
print(minimo)
posicion=instituto['notas'].index(minimo)
print(posicion)
print(instituto['profesores'][posicion])
print(instituto['materias'][posicion])
