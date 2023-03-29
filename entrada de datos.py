num1=int(input("Ingrese num1: "))
num2=int(input("Ingrese num2: "))
x=num1 == num2
a=num1 != num2
b=num1 > num2
c=num1 <= num2
print("Es igual ",x)
#Opción 1
print("Los números: " + str(num1) + " y " + str(num2) + "son iguales: " + str(x))
#Opción 2
print("Los números:" , (num1) , "y" , (num2) , "son iguales:" , (x))
#Opción 3
print(f"Los números: {num1} y {num2} son iguales: {x}")
#Opción 4
print("Los números: {} y {} son iguales: {}\n".format(num1,num2,x))

print("Son diferentes: ",a)
#Opción 1
print("Los números: " + str(num1) + " y " + str(num2) + "son diferentes: " + str(a))
#Opción 2
print("Los números: " , (num1) , "y" , (num2) , "son diferentes:" , (a))
#Opción 3 
print(f"Los números: {num1} y {num2} son diferentes: {a}")
#Opción 4
print("Los números: {} y {} son diferentes: {}\n".format(num1,num2,a))

print("El primer número es mayor: ",b)
#Opción 1
print("Entre los números: " + str(num1) + " y " + str(num2) + "el primero es mayor: " + str(b))
#Opcion 2
print("Entre los números:" , (num1) , "y" , (num2) , "el primero es mayor:" , (b))
#Opción 3
print(f"Entre los números: {num1} y {num2} el primero es mayor: {b}")
#opcion 4
print("Entre los números: {} y {} el primero es mayor: {}\n".format(num1,num2,b))

print("El segundo número es mayor o igual al primero: ",c)
#Opcion 1
print("Entre los números: " + str(num1) + " y " + str(num2) + "el segundo es mayor o igual al primero:" + str(c))
#Opción 2
print("Entre los números:" , (num1) , "y" , (num2) , "el segundo es mayor o igual al primero:" , (c))
#Opción 3
print(f"Entre los números: {num1} y {num2} el segundo es mayor o igual al primero: {c}")
#Opción 3
print("Entre los números: {} y {} el segundo es mayor o igual al primero: {}".format(num1,num2,c))
