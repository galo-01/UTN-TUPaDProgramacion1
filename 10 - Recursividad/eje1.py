

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)




def factorial_de_numeros_hasta(num):
    if num > 0:
        print(f"Factorial de {num} = {factorial(num)}")
        factorial_de_numeros_hasta(num-1)



factorial_de_numeros_hasta(int(input("[Ingrese numero entero]:")))