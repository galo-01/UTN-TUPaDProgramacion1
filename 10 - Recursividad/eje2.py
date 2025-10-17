


# estoy orgulloso de esta solución :,)



def agregar_sig_fibonacci(serie: list,num:int):
    if len(serie) == num:
        return
    else:
        serie.append(serie[-2]+serie[-1])
        agregar_sig_fibonacci(serie,num)



def fibonacci(num):
    serie = [0,1]
    agregar_sig_fibonacci(serie,num)
    print(serie)


fibonacci(5)
fibonacci(10)

fibonacci(15)