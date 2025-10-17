


def contar_digito(num, digito):
    if num == 0:
        return 0
    ultimo = num % 10
    if ultimo == digito:
        return 1 + contar_digito(num // 10, digito)
    else:
        return contar_digito(num // 10, digito)



print(contar_digito(4252,2))
print(contar_digito(53673356473,3))
