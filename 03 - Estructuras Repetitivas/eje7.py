
#[ ejercicio 7 ]

num = int(input("[Ingrese un numero entero positivo]:"))
total = 0

for i in range(0,num,1):
    total += i

print(f"La suma de 0 a {num} es de {total}")