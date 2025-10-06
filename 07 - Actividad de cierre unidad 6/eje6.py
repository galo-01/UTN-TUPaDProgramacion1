
def tabla_multiplicar(num):
    for i in range(1,11):
        print(f"{num}x{i} = {num*i}")

num = int(input("[Ingrese un numero entero]:"))

tabla_multiplicar(num)