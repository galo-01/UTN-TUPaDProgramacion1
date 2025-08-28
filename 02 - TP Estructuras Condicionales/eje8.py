#ejercicio 8
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario
#  e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() 
# de Python para convertir entre mayúsculas y minúsculas.


nombreUsuario = input("Hola!, Ingresa tu nombre: \n")
menuUsuario = input("Ingresa el numero correspondiente a como lo quieres ver: \n1.Mayúsculas \n2.Minusculas \n3.Primera mayuscula, resto minuscula\n")

if menuUsuario == "1": print(nombreUsuario.upper())
if menuUsuario == "2": print(nombreUsuario.lower())
if menuUsuario == "3": print(nombreUsuario.title()