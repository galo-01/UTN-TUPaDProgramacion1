




def suma_digitos(num):
    if num < 10:
        return num
    return (num % 10) + suma_digitos(num // 10)


print(suma_digitos(4))
print(suma_digitos(10))
