

frase = input("[Ingrese una frase u oración]:")

print("")

lista_palabras = frase.split(" ")

palabras_set = set(lista_palabras)
palabras_cantidad = {}

for i in lista_palabras:
    if (not i in palabras_cantidad):
        palabras_cantidad[i] = 0
    palabras_cantidad[i] += 1

print(palabras_set)
print(palabras_cantidad)
