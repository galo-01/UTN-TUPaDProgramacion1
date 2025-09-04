
#[ ejercicio 5 ]

import random

numero_random = random.randint(0, 10)

intentos = 1

num = int(input("[Intente adivinar el numero del 0 al 10]:"))

while num != numero_random:
    print("INCORRECTO")
    intentos += 1
    num = int(input("[Intente adivinar el numero del 0 al 10]:"))


print(f"Lo lograste! Solo te costó {intentos} intentos.")