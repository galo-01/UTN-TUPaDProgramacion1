
#[ ejercicio 3 ]

inicio = int(input("[Ingrese un primer numero]:"))
fin = int(input("[Ingrese un segundo numero]:"))

total = 0

for i in range(inicio+1,fin,1):
    total += i

print(f"Suma de numeros intermediarios: {total}")