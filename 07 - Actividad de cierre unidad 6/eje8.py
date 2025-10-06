

def calcular_imc(peso, altura):
    return (peso / (altura**2))


peso, altura = map(float, input("Ingrese el peso y la altura separando con espacio. ").split())

print("")
print("- Indice de masa corporal -")
print(calcular_imc(peso, altura))
