
telefonos = {}

for i in range(5):
    nombre = input("[Ingrese el nombre de un nuevo contacto]:")
    numero = int(input("[Ingrese el número de teléfono del contacto]:"))

    telefonos[nombre] = numero

print("")
contacto = input("[Ahora ingrese un nombre a consultar]:")

print(f"El numero de {contacto} es {telefonos[contacto]}")