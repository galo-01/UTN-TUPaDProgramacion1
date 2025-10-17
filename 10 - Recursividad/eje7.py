

def contar_bloques(num):
    if num == 1:
        return 1
    return num + contar_bloques(num - 1)


print(contar_bloques(15))
print(contar_bloques(32))
