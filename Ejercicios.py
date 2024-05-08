 #Solicitar la edad al usuario
edad = int(input("Ingresa tu edad: "))

# Verificar si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")





contraseña_guardada = "alder"
contraseña_ingresada = input("ingrese tu maldita  contraseña: ")

if contraseña_ingresada.lower() == contraseña_guardada:
    print("tu maldita contraseña es correcta")
else:
    print("La contraseña es incorrecta por manco")



numero = int(input("Ingresa un número entero positivo como tu hermano: "))

if numero <= 0:
    print("El número ingresado no es válido. Debe ser un número entero positivo.")
else:
    cuenta_regresiva = list(range(numero, -1, -1))
    cuenta_regresiva = list(map(str, cuenta_regresiva))
    cuenta_regresiva = ",".join(cuenta_regresiva)
    print(cuenta_regresiva)