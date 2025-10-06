
import math

def calcular_area_circulo(r):
    return math.pi * r**2

def calcular_perimetro_circulo(r):
    return math.pi * 2 * r



radio = int(input("[Ingrese el radio de un circulo]:"))
print("Area:")
print(calcular_area_circulo(radio))
print("Perimetro:")
print(calcular_perimetro_circulo(radio))