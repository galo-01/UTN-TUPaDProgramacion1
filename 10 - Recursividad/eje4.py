




def agregar_sig_binario(num):
    if num == 0:
        return ""
    else:
        return agregar_sig_binario(num // 2) + str(num % 2)

def deci_a_bin(num):
    if num == 0:
        print("0")
    else:
        binario = agregar_sig_binario(num)
        print(binario)


deci_a_bin(21)
deci_a_bin(33)