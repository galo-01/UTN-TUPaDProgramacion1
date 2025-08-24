
# Gabriel DAnna

# 1)

print("Hola mundo!")

# 2)

nombre = input("[Ingrese su nombre]:")
print(f"Hola {nombre}!")

# 3)

nombre = input("[Ingrese su nombre]:")
apellido = input("[Ingrese su apellido]:")
edad = input("[Ingrese su edad]:")
pais = input("[Ingrese su pais de residencia]:")

print(f"Hola, mi nombre es {nombre} {apellido}, tengo {edad} años de edad y vivo en {pais}")

# 4)

import math

radio = int(input("[Ingrese el radio de un circulo]:"))

print(f"El area del circulo es de {math.pi * radio**2} y el perimetro es de {2 * math.pi * radio}")

# 5)

segundos = int(input("[Ingrese una cantidad de segundos]:"))

print(f"Esas son { (segundos/60)/60 } horas")

# 6)

num = int(input("[Ingrese un numero]:"))

print(f"{num} x 1 = {num}")
print(f"{num} x 2 = {num*2}")
print(f"{num} x 3 = {num *3}")
print(f"{num} x 4 = {num*4}")
print(f"{num} x 5 = {num*5}")
print(f"{num} x 6 = {num*6}")
print(f"{num} x 7 = {num*7}")
print(f"{num} x 8 = {num*8}")
print(f"{num} x 9 = {num*9}")
print(f"{num} x 10 = {num*10}")

# 7)

num1 = int(input("[Ingrese primer numero entero]:"))
num2 = int(input("[Ingrese segundo numero entero]:"))

print(f"Suma: {num1+num2}")
print(f"Resta: {num1-num2}")
print(f"Multiplicacion: {num1*num2}")
print(f"Division: {num1/num2}")

# 8)

peso = float(input("[Ingrese su peso (kg)]:"))
altura = float(input("[Ingrese su altura (m)]:"))

print(f"Tu masa corporal es de: {peso/(altura**2)}")

# 9)

temp = float(input("[Ingrese una temperatura en Cº]:"))
print(f"La temperatura en Fahrenheit es de {9/5 * temp + 32}")

# 10)

num1 = int(input("[Ingrese primer numero]:"))
num2 = int(input("[Ingrese segundo numero]:"))
num3 = int(input("[Ingrese tercer numero]:"))

print(f"El promedio de los numeros es de {(num1 + num2 + num3) /3}")