print("Curso: Fundamentos de Python")
print("Estudiante: Evelyn Malo")
print("Fecha: 30/03/2023\n")
dato=int(input('Digite el número a verfificar si es múltiplo de 3: '))
if(dato%3==0):
    print('El número {} es múltiplo de 3'.format(dato))
else:
    print(f'El número: {dato} no es multiplo de 3')