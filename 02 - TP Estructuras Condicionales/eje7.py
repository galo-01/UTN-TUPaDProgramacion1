

#ejercicio 7
#7) Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla
#  en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

palabraUsuario = input("Ingresa una palabra: \n")

if palabraUsuario[-1].lower() in "aeiou":
    print(palabraUsuario + "!")
else:
    print(palabraUsuario)