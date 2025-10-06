
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32


temp = float(input("[Ingrese temperatura en celsius]:"))

print(f"{temp} en ferengeid es {celsius_a_fahrenheit(temp)}")