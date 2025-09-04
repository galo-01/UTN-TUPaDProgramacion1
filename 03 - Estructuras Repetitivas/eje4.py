
#[ ejercicio 4 ]

total = 0

num = int(input("[Ingrese un numero para comenzar]:"))
total += num

while num != 0 :
    num = int(input("[Ingrese el siguiente numero (0 para finalizar)]:"))
    total += num

print(f"Suma de todos los numeros: {total}")