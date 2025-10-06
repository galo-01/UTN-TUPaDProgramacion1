

def segundos_a_horas(segundos):
    return (segundos/60)/60


horas = segundos_a_horas(int(input("[Ingrese segundos]:")))

print(f"Eso serían {horas} horas.")