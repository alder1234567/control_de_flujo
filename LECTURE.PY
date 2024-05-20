# ESTE CIDIGO IMPRIME LOS NUMEROS
#DEL U1 AL 10
for n in range(1,11):
    print(n)



##crear un programa que me imprima las cinco vocales 

vocales:str="aeiou"
for n in range(0,5):
 print(vocales [n])

 ##crear un programa que me muestre los 8 primos pares 
 for n in range( 1,17 ):
    if n%2==0:
     contador+:1 
    print:(f"(n)EL NUMERO(contador)")
  


#crear al programa que pida al usuario escribir una oracion 
#y muestrre por terminalla cantidad de valores a que tiene esa oracion 
#OJO SOLO LAS "a" MINUSCULA
oracion    :  =str=input("escrube una oracion: ")
contador:int=0
for n in range(0,1en(oracion)).
  if oracion[n]=="a":
    contador=contador+1
    #contador+=1
for n in "aeiou":
   print(n)

for indica,letra in enumerate("aeiou"):
  print(f"el indice es [1] y la letra es (1)")

print(f"la cantidad de letras a que tengo es (contador) ")

# crear un programa que me cuente la cantidad de comas y mem uestre 
#sus indices
#ojo:tiene que pedir al ususario 

frase:str=input("ingrese una frace:")
ontador=0
for indice,caracter in enumerate(frase):
  if caracter==',':
    print(f"su indice es (indice)")
    contador+=1
  
  print("cantidad de comas :",contador)


  #escribi un programa que pregunte al ususario su edad y muestre por pantalla 
  #todos los años que ha cumpliendo (desde 1 año hasta su edad)

edad=int(input("ingresa tu edad:"))
for in I range(1 edad+1):
  if I ==1:
    print("HAS CUMPLIDO 1 AÑOS")
    print("HAS CUMPLIDO",str(i),"años")

#crear un programa que me pidad el nombre de tres personas y guardar variable global su ultimas letras de sus nombres
#mostrar por pantalla  la variable gloval con los tres ultimas letras del nombre de cada persona

ultima_letra:=str=""
for _ in range (3):
  nombre:str=input("escribe tu nombre: ")
  #ultima_letra+=nombre[-1]
  last_letter:str=nombre[-1]
  ultima_letra+=last_letter
  #ultima_letras=ultima_letra+las_letter
print(ultima_letra)



#crear un programa que muestre por terminal la siguiente figura a,e,i,o,u
 
letras = ['a', 'e', 'i', 'o', 'u']

for i in range(len(letras)):
    linea = ""
    for j in range(i+1):
      linea+=letra[I]
      print(linea)


condiciones=true
while condiciones:
   eval=imput("desea continuar [S/N]:")
   if eval=="S"
    print("continuas en el bucle")
    continue
   else:
       print("se termino el pograma")
       condicones=false
       break
   



contador=0
white contador<=5:
  print(contador)
  contador+=1
  prin(f"valor final [contador]")


  nombre"jose"
  nombre.upper() #convierteel texto en mayusculas 

  apellido="apellidos"
  print(apellido.lower()) #convierte la primera letra en mayuscula

  #crear un programa que pida la cantidad de notas que se deve registrar 
  #luego me dira las notas e imprimira el promedio 
  num_notas = int(input("Ingrese la cantidad de notas a registrar: "))
suma_notas = 0

white i in range(num_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    suma_notas += nota

promedio = suma_notas / num_notas

print("\nEl promedio de las notas ingresadas es: ", promedio)