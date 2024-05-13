edad = int(input("Ingresa tu edad: "))

# Verificar si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")






numero = int(input("Ingresa un número entero positivo: "))

if numero <= 0:
    print("El número ingresado no es válido. Debe ser un número entero positivo.")
else:
    cuenta_regresiva = list(range(numero, -1, -1))
    cuenta_regresiva = list(map(str, cuenta_regresiva))
    cuenta_regresiva = ",".join(cuenta_regresiva)
    print(cuenta_regresiva)









contraseña_guardada ="contraseña"
contraseña_ingresada = input("Ingresa la contraseña: ")

if contraseña_ingresada.lower() == contrasena_guardada:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta"