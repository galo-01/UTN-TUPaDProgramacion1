
#[ ejercicio 10 ]

#no veo necesidad de usar bucles

num = input("[Ingrese un numero de multiples digitos]:")

lista = list(num)
lista.reverse()

print("".join(lista))