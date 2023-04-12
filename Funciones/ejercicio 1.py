def mayoredad(edad):
    bandera=False
    if edad >= 17:
        bandera=True
    return bandera
while True:
    dato=int(input("Ingrese la edad: "))
    print(mayoredad(dato))
    if mayoredad(dato):
        print("Es mayor de edad")
        break
    else:
        print("Es menor de edad")