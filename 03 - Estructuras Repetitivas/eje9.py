
#[ ejercicio 9 ]

total = 0
cantidad = 100

for i in range(0,cantidad,1):
    total += int(input("[Ingrese numero entero]:"))

print(f"Media: {total/cantidad}")
